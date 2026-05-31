# helpers.py
import random
import os
import json
from config import PLAYERS, MATCH_TYPES

def clear_files():
    """Initializes and clears output files at start."""
    for filename in ['highlights.txt', 'req.txt']:
        with open(filename, 'w') as f:
            f.write("")

def save_scores(text: str):
    """Appends game events to highlights.txt."""
    with open("highlights.txt", 'a') as a:
        a.write(text)

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_bowler_delivery_pool(match_type: str) -> list:
    """Returns a weighted list of runs representing bowler deliveries."""
    pool = []
    distributions = {
        "t20i": [14, 21, 26, 34],
        "odi": [9, 16, 31, 42],
        "test": [11, 12, 21, 57]
    }
    dist = distributions.get(match_type, [9, 16, 31, 42])
    for _ in range(dist[0]): pool.append(1)
    for _ in range(dist[1]): pool.append(2)
    for _ in range(dist[2]): pool.append(4)
    for _ in range(dist[3]): pool.append(6)
    return pool

def perform_toss() -> tuple:
    """Handles the coin toss and user decision."""
    coin_sides = ['Heads', 'Tails']
    india_call = random.choice(coin_sides)
    toss_winner_is_india = (random.choice(coin_sides) == india_call)
    decision_map = {1: 'bat', 2: 'bowl'}
    
    print("India won the toss.")
    while True:
        try:
            choice = int(input("What to do? (1. Bat, 2. Bowl)\n>> "))
            if choice in [1, 2]: break
        except ValueError: pass
        print("Invalid input.")
        
    toss_text = f"India won the toss and decided to {decision_map[choice]} first!\n"
    is_india_batting_first = (choice == 1)
    return is_india_batting_first, toss_text

def perform_silent_toss() -> tuple:
    """Handles auto-toss for Simulation Mode."""
    choice = random.choice([True, False])
    toss_text = f"Toss completed silently. India batting first: {choice}\n"
    return choice, toss_text

def calculate_batting_mindset(perc: float, team: str, state) -> str:
    """Determines risk profile based on progress of the match."""
    if team == "India":
        total_stars = state.combined_stars_ind
        req_stars = sum(player_data[2] for player_data in state.indian_batsmen.values())
    else:
        total_stars = state.combined_stars_aus
        req_stars = sum(player_data[2] for player_data in state.australian_batsmen.values())
        
    stars_remains = round((req_stars / total_stars) * 100) if total_stars > 0 else 0
    choice = ''

    if perc <= 25:
        if stars_remains > 90:
            choice = random.choice(['neutral', 'defense', 'neutral', 'defense', 'attack'])
        elif 75 < stars_remains <= 85:
            choice = 'neutral'
        elif stars_remains <= 75:
            choice = 'defense'
    elif 25 < perc <= 75:
        if stars_remains > 85:
            choice = 'attack'
        elif 65 < stars_remains <= 85:
            choice = 'neutral'
        elif stars_remains <= 60:
            choice = 'defense'
        if stars_remains <= 45: 
            choice = 'super defense'
    else: 
        if stars_remains > 65:
            choice = 'super attack'
        elif 45 < stars_remains <= 65:
            choice = 'attack'
        elif 25 < stars_remains <= 45:
            choice = 'neutral'
        elif stars_remains <= 25:
            choice = 'defense'
            
    if perc >= 85 and stars_remains > 25:
        choice = 'super attack'
    elif perc >= 85 and stars_remains <= 25:
        choice = 'attack'
        
    return choice if choice != "" else 'neutral'

def get_mindset_delivery_pool(mindset: str, match_type: str) -> list:
    def build_pool(weights: list) -> list:
        outcomes = []
        for runs_val, count in zip([0, 1, 2, 4, 6], weights):
            outcomes.extend([runs_val] * count)
        return outcomes

    parameters = {
        'neutral': {
            'test': [22, 22, 22, 20, 14],
            'odi': [23, 23, 23, 18, 13],
            't20i': [21, 21, 21, 24, 13]
        },
        'attack': {
            'test': [20, 20, 20, 22, 18],
            'odi': [22, 22, 22, 19, 15],
            't20i': [19, 19, 19, 26, 17]
        },
        'defense': {
            'test': [24, 24, 24, 16, 12],
            'odi': [26, 26, 26, 14, 8],
            't20i': [23, 23, 23, 19, 12]
        },
        'super attack': {
            'test': [18, 18, 18, 24, 22],
            'odi': [20, 20, 20, 22, 18],
            't20i': [17, 17, 17, 29, 20]
        },
        'super defense': {
            'test': [26, 26, 26, 14, 8],
            'odi': [29, 29, 29, 8, 5],
            't20i': [25, 25, 25, 15, 10]
        }
    }
    selected_ranges = parameters[mindset][match_type]
    return build_pool(selected_ranges)

def run_ai_play(perc: float, team: str, match_type: str, state) -> int:
    """Simulates AI batsman decision making."""
    mindset = calculate_batting_mindset(perc, team, state)
    pool = get_mindset_delivery_pool(mindset, match_type)
    return random.choice(pool)

def export_match_to_json(state, result_text: str) -> str:
    """Serializes the complete match history into a neat, standardized JSON block."""
    data = {
        "match_type": state.match_type.upper(),
        "final_result": result_text,
        "innings_history": []
    }
    for i, inn in enumerate(state.innings_history):
        inn_data = {
            "innings_number": i + 1,
            "batting_team": inn["bat_team"],
            "bowling_team": inn["bowl_team"],
            "total_runs": inn["runs"],
            "total_wickets": inn["wickets"],
            "overs_played": inn["overs"],
            "batting_scorecard": {},
            "bowling_scorecard": {}
        }
        
        # Parse batsmen
        for key, stats in inn["batsmen"].items():
            runs, balls, _, _, bounds, dismissal, _ = stats
            if balls > 0 or dismissal != "NOT OUT":
                inn_data["batting_scorecard"][PLAYERS[key]] = {
                    "runs": runs,
                    "balls_faced": balls,
                    "fours": bounds[0],
                    "sixes": bounds[1],
                    "strike_rate": round((runs/balls)*100, 2) if balls > 0 else 0.0,
                    "status": dismissal
                }
                
        # Parse bowlers
        for key, stats in inn["bowlers"].items():
            runs, balls, wkts = stats
            if balls > 0:
                inn_data["bowling_scorecard"][PLAYERS[key]] = {
                    "overs": f"{balls//6}.{balls%6}",
                    "runs_conceded": runs,
                    "wickets": wkts,
                    "economy": round(runs / (balls/6), 2) if balls > 0 else 0.0
                }
        data["innings_history"].append(inn_data)
        
    return json.dumps(data, indent=2)
