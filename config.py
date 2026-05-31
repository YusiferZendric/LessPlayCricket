# config.py
import random

PLAYERS = {
    "gill": "Shubhman Gill", "singh": "Aditya Singh", "iyer": "Shreyas Iyer (C)", 
    "rahul": "KL Rahul", "kishan": "Ishan Kishan (WK)", "yadav": "Suryakumar Yadav", 
    "jadeja": "Ravindra Jadeja", "ashwin": "Ravichandran Ashwin", "thakur": "Shardul Thakur", 
    "shami": "Mohammed Shami", "krishna": "Prasidh Krishna", "short": "Matt Short", 
    "warner": "David Warner", "smith": 'Steve Smith (C)', "labuschagne": "Marnus Labuschagne", 
    "inglis": "Josh Inglis", "carey": "Alex Carey (WK)", "green": "Cameron Green", 
    "abott": "Sean Abott", "zampa": "Adam Zampa", "hazlewood": "Josh Hazlewood", 
    "johnson": "Spancer Johnson"
}

INDIAN_BOWLERS = ["shami", "krishna", "ashwin", "thakur", "jadeja", "singh"]
AUSTRALIAN_BOWLERS = ["johnson", "hazlewood", "abott", "green", "zampa", "short"]

MATCH_TYPES = {
    't20i': {'overs': 20, 'max_bowler_overs': 4, 'arg_scale': 4, 'arg2_scale': 8},
    'odi': {'overs': 50, 'max_bowler_overs': 10, 'arg_scale': 7, 'arg2_scale': 10},
    'test': {'overs': 1000, 'max_bowler_overs': 1000, 'arg_scale': 8, 'arg2_scale': 8}
}

MATCH_SCORING = {
    'test': {
        'boundary_base': 0.12,
        'boundary_momentum_divisor': 520,
        'boundary_wicket_base': 0.22,
        'boundary_wicket_momentum_divisor': 760,
        'shot_base': 0.55,
        'shot_momentum_divisor': 2200
    },
    'odi': {
        'boundary_base': 0.16,
        'boundary_momentum_divisor': 380,
        'boundary_wicket_base': 0.26,
        'boundary_wicket_momentum_divisor': 850,
        'shot_base': 0.72,
        'shot_momentum_divisor': 1800
    },
    't20i': {
        'boundary_base': 0.22,
        'boundary_momentum_divisor': 320,
        'boundary_wicket_base': 0.30,
        'boundary_wicket_momentum_divisor': 900,
        'shot_base': 0.84,
        'shot_momentum_divisor': 1500
    }
}

def generate_player_stars(match_type: str):
    """Generates the randomized player statistics with momentum initialization."""
    s = MATCH_TYPES[match_type]
    arg, arg2 = s['arg_scale'], s['arg2_scale']
    if match_type != 'test':
        num = random.randint(1, 3)
        arg -= num; arg2 -= num

    # [runs, balls, lives, [milestones], [fours, sixes], dismissal_string, momentum]
    def create_bat(base_lives): 
        if match_type == 't20i':
            max_lives = min(6, max(2, base_lives + 1))
        elif match_type == 'odi':
            max_lives = min(8, max(3, base_lives + 3))
        else:
            max_lives = max(5, base_lives + 8)
        return [0, 0, random.randint(1, max_lives), [False, False, False], [0, 0], "NOT OUT", 30]

    ind_batsmen = {
        "gill": create_bat(arg), "singh": create_bat(arg), "iyer": create_bat(arg - 1),
        "rahul": create_bat(arg + 1), "kishan": create_bat(arg - 1), "yadav": create_bat(arg - 2),
        "jadeja": create_bat(arg - 2), "ashwin": create_bat(arg - 2), "thakur": create_bat(2),
        "shami": create_bat(2), "krishna": create_bat(2)
    }

    aus_batsmen = {
        "short": create_bat(arg2), "warner": create_bat(arg2), "smith": create_bat(arg2 + 1),
        "labuschagne": create_bat(arg2 - 1), "inglis": create_bat(arg2 - 1), "carey": create_bat(arg2 - 2),
        "green": create_bat(arg2 - 3), "abott": create_bat(arg2 - 3), "zampa": create_bat(2),
        "hazlewood": create_bat(2), "johnson": create_bat(2)
    }
    
    return ind_batsmen, aus_batsmen
