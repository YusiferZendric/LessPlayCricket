# match_state.py
import copy
from config import generate_player_stars

class MatchState:
    def __init__(self, match_type: str):
        self.match_type = match_type
        self.indian_batsmen, self.australian_batsmen = generate_player_stars(match_type)
        
        # Calculate initial team star/lives pool for AI decision making
        self.combined_stars_ind = sum(j[2] for j in self.indian_batsmen.values())
        self.combined_stars_aus = sum(j[2] for j in self.australian_batsmen.values())
        
        # Bowler Stats: [runs, balls_bowled, wickets]
        self.indian_bowlers = {b: [0, 0, 0] for b in ["shami", "krishna", "ashwin", "thakur", "jadeja", "singh"]}
        self.australian_bowlers = {b: [0, 0, 0] for b in ["johnson", "hazlewood", "abott", "green", "zampa", "short"]}
        
        self.runs = 0
        self.wickets = 0
        self.balls_played = 0
        self.total_match_balls = 0
        self.sim_mode = False  # Set to True for instant silent simulations
        self.debug_mode = False  # Set to True for verbose ball-by-ball simulation traces
        
        self.innings_history = []  # Stores past innings for multi-innings HTML
        
    def archive_innings(self, batting_team, bowling_team):
        """Saves a snapshot of the innings for the HTML Scorecard and JSON export."""
        if batting_team == "India":
            bat, bowl = copy.deepcopy(self.indian_batsmen), copy.deepcopy(self.australian_bowlers)
        else:
            bat, bowl = copy.deepcopy(self.australian_batsmen), copy.deepcopy(self.indian_bowlers)
            
        self.innings_history.append({
            "bat_team": batting_team, "bowl_team": bowling_team,
            "runs": self.runs, "wickets": self.wickets, 
            "overs": f"{self.balls_played//6}.{self.balls_played%6}",
            "batsmen": bat, "bowlers": bowl
        })

    def reset_innings(self):
        """Resets dynamic match counts for the next innings."""
        self.runs = 0
        self.wickets = 0
        self.balls_played = 0

    def refresh_players(self):
        """Used before 3rd/4th innings in Test Match to restore player stamina."""
        self.indian_batsmen, self.australian_batsmen = generate_player_stars(self.match_type)
        
        # Re-calculate stars on refresh
        self.combined_stars_ind = sum(j[2] for j in self.indian_batsmen.values())
        self.combined_stars_aus = sum(j[2] for j in self.australian_batsmen.values())
        
        self.indian_bowlers = {b: [0, 0, 0] for b in self.indian_bowlers.keys()}
        self.australian_bowlers = {b: [0, 0, 0] for b in self.australian_bowlers.keys()}
