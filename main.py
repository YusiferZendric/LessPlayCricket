# main.py
import webbrowser
from match_state import MatchState
from helpers import clear_files, perform_toss, perform_silent_toss, clear_screen, export_match_to_json
from game_engine import CricketMatchEngine
from html_generator import generate_html_scorecard

def select_play_mode() -> tuple:
    """Prompts user to choose game mode: Interactive or Fast Sim."""
    while True:
        try:
            print("Select Mode:")
            print("1. Interactive Play Mode")
            print("2. Fast Simulation Mode (JSON Scorecard Output)")
            mode = int(input(">> "))
            if mode in [1, 2]:
                return (mode == 2)
        except ValueError: pass

def select_debug_mode() -> bool:
    while True:
        choice = input("Enable debug trace for simulations? (y/n): ").strip().lower()
        if choice in {"y", "yes"}:
            return True
        if choice in {"n", "no"}:
            return False

def select_match_type() -> str:
    while True:
        try:
            choice = int(input("Select Match Type:\n1. Test\n2. ODI\n3. T20I\n>> "))
            if choice in {1: 'test', 2: 'odi', 3: 't20i'}: return {1: 'test', 2: 'odi', 3: 't20i'}[choice]
        except ValueError: pass

def run_test_match(state, engine, is_ind_bat_first):
    team_a, team_b = ("India", "Australia") if is_ind_bat_first else ("Australia", "India")

    score_a1 = engine.play_innings(team_a, team_b, innings_num=1)
    if not state.sim_mode:
        input(f"\n{team_a} 1st Innings: {score_a1}. Press Enter...")

    score_b1 = engine.play_innings(team_b, team_a, innings_num=2, base_lead=score_a1)
    
    lead_a = score_a1 - score_b1
    state.refresh_players()
    
    score_a2 = engine.play_innings(team_a, team_b, innings_num=3, base_lead=lead_a)
    
    total_lead = score_a2 + lead_a
    if total_lead <= 0:
        return f"{team_b} WON by an INNINGS and {abs(total_lead)} runs!"

    target = total_lead + 1
    score_b2 = engine.play_innings(team_b, team_a, innings_num=4, target=target)
    
    if score_b2 >= target: return f"{team_b} WON the match!"
    else: return f"{team_a} WON by {target - score_b2 - 1} runs!"

def run_limited_overs(state, engine, is_ind_bat_first):
    t1, t2 = ("India", "Australia") if is_ind_bat_first else ("Australia", "India")
    score1 = engine.play_innings(t1, t2)
    if not state.sim_mode:
        input(f"\nTarget: {score1 + 1}. Press Enter to begin chase...")
    score2 = engine.play_innings(t2, t1, target=score1 + 1)
    
    if score2 > score1: return f"{t2} WON by {10 - state.wickets} wickets!"
    else: return f"{t1} WON by {score1 - score2} runs!"

def main():
    clear_screen(); clear_files()
    sim_mode = select_play_mode()
    match_type = select_match_type()
    
    state = MatchState(match_type)
    state.sim_mode = sim_mode
    state.debug_mode = select_debug_mode() if sim_mode else False
    engine = CricketMatchEngine(state)
    
    if state.sim_mode:
        is_ind_bat_first, toss_text = perform_silent_toss()
    else:
        is_ind_bat_first, toss_text = perform_toss()
        print(toss_text); input("\nPress Enter to begin...")
    
    if match_type == 'test': 
        result = run_test_match(state, engine, is_ind_bat_first)
    else: 
        result = run_limited_overs(state, engine, is_ind_bat_first)
    
    if state.sim_mode:
        # Fast Simulation Mode Output: JSON printed straight to the terminal
        json_output = export_match_to_json(state, result)
        print("\n" + "="*20 + " SIMULATION COMPLETE: JSON SCORECARD " + "="*20)
        print(json_output)
    else:
        # Standard Mode Output: Displays on terminal and launches HTML dashboard
        print("\n" + "="*40 + f"\n {result} \n" + "="*40)
        path = generate_html_scorecard(state, match_ended=True, result_text=result)
        webbrowser.open(f"file://{path}")

if __name__ == "__main__":
    main()
