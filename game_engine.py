# game_engine.py
import random
import os
import webbrowser
from config import PLAYERS, MATCH_TYPES, MATCH_SCORING
from helpers import save_scores, clear_screen, get_bowler_delivery_pool, run_ai_play

C_BLUE = "\033[94m"; C_GREEN = "\033[92m"; C_YELLOW = "\033[93m"; C_RED = "\033[91m"
C_CYAN = "\033[96m"; C_WHITE = "\033[97m"; C_GRAY = "\033[90m"; C_BOLD = "\033[1m"; C_RESET = "\033[0m"

class CricketMatchEngine:
    def __init__(self, state):
        self.state = state

    def display_scorecard(self, batting_team: str, bowling_team: str, batsmen_data: dict, bowlers_data: dict, current_batsmen: list, active_idx: int, current_bowler_key: str, current_over_log: list, ball_of_over: int, context_str: str):
        if self.state.sim_mode and not self.state.debug_mode: return  # Skip rendering completely in fast sim mode
        
        team_abbr = "IND" if batting_team == "India" else "AUS"
        score_str = f"{self.state.runs}/{self.state.wickets}"
        overs_str = f"{self.state.balls_played//6}.{self.state.balls_played%6}"
        
        b1_key, b2_key = current_batsmen[0], current_batsmen[1]
        b1_name, b2_name = PLAYERS[b1_key].split(" ")[0].upper(), PLAYERS[b2_key].split(" ")[0].upper()
        
        b1_runs, b1_balls = batsmen_data[b1_key][0], batsmen_data[b1_key][1]
        b2_runs, b2_balls = batsmen_data[b2_key][0], batsmen_data[b2_key][1]
        b1_m, b2_m = batsmen_data[b1_key][6], batsmen_data[b2_key][6]

        b1_color = f"{C_YELLOW if active_idx==0 else C_WHITE}{'► ' if active_idx==0 else '  '}{b1_name}{C_RESET} {C_BOLD if active_idx==0 else ''}{b1_runs}{C_RESET}{C_GRAY}({b1_balls}b, {b1_m}%){C_RESET}"
        b2_color = f"{C_YELLOW if active_idx==1 else C_WHITE}{'► ' if active_idx==1 else '  '}{b2_name}{C_RESET} {C_BOLD if active_idx==1 else ''}{b2_runs}{C_RESET}{C_GRAY}({b2_balls}b, {b2_m}%){C_RESET}"

        plain_score = f" {team_abbr} {score_str} ({overs_str}) "
        col1 = f" {C_BLUE}{team_abbr}{C_RESET} {C_BOLD}{score_str}{C_RESET} {C_GRAY}({overs_str}){C_RESET}{' ' * (21 - len(plain_score))}"
        col2 = f"{b1_color}{' ' * max(0, 19 - len(f'► {b1_name} {b1_runs}({b1_balls}b, {b1_m}%)'))}│ {b2_color}{' ' * max(0, 18 - len(f'  {b2_name} {b2_runs}({b2_balls}b, {b2_m}%)'))}"

        bw_stats = bowlers_data[current_bowler_key]
        bowler_name = PLAYERS[current_bowler_key].split(" ")[-1].upper()
        
        c_tick, p_tick = [], []
        for b in (current_over_log + ["-"] * (6 - len(current_over_log))):
            color = C_GRAY if b in ['0', '-'] else C_GREEN if b in ['4', '6'] else C_RED if b == 'W' else C_WHITE
            char = '•' if b == '0' else b
            c_tick.append(f"{color}[{char}]{C_RESET}"); p_tick.append(f"[{char}]")
                
        col3_plain = f" {bowler_name} {bw_stats[2]}-{bw_stats[0]} {' '.join(p_tick)} "
        col3 = f" {C_CYAN}{bowler_name}{C_RESET} {C_BOLD}{bw_stats[2]}-{bw_stats[0]}{C_RESET} {' '.join(c_tick)}{' ' * max(1, 41 - len(col3_plain))}"

        day_str = f" DAY {(self.state.total_match_balls // 540) + 1} │ " if self.state.match_type == 'test' else ""
        header_plain = f" {self.state.match_type.upper()} MATCH │ {day_str}{batting_team.upper()} vs {bowling_team.upper()} │ {context_str}"
        
        print("\n" + f"{C_GRAY}─{C_RESET}" * 107)
        print(f" {C_GRAY}──{C_RESET} {C_YELLOW} {self.state.match_type.upper()} MATCH │ {day_str}{batting_team.upper()} vs {bowling_team.upper()} │ {context_str} {C_RESET}{' ' * max(1, 107 - len(header_plain) - 8)} {C_GRAY}──{C_RESET} ")
        print(f"{C_GRAY}┌──────────────────────┬────────────────────────────────────────┬─────────────────────────────────────────┐{C_RESET}")
        print(f"{C_GRAY}│{C_RESET}{col1}{C_GRAY}│{C_RESET}{col2}{C_GRAY}│{C_RESET}{col3}{C_GRAY}│{C_RESET}")
        print(f"{C_GRAY}└──────────────────────┴────────────────────────────────────────┴─────────────────────────────────────────┘{C_RESET}")
        print(f"{C_GRAY}─{C_RESET}" * 107 + "\n")

    def select_starting_batsmen(self, batsmen_dict: dict, is_user_batting: bool) -> list:
        keys = list(batsmen_dict.keys())
        if is_user_batting and not self.state.sim_mode:
            print("\nAvailable Batsmen:")
            for k in keys: print(f"-> {k} ({PLAYERS[k]})")
            while True:
                a = input("Choose First Batsman: ").strip().lower()
                if a in batsmen_dict: break
                print("Invalid batsman. Try again.")
            while True:
                b = input("Choose Second Batsman: ").strip().lower()
                if b in batsmen_dict and b != a: break
                print("Invalid or duplicate batsman. Try again.")
        else:
            a, b = keys[0], keys[1]
            if not self.state.sim_mode:
                print(f"Opening: {PLAYERS[a]} and {PLAYERS[b]}")
        return [a, b]

    def choose_bowler(self, bowlers_dict: dict, previous_bowler: str, is_user_bowling: bool) -> str:
        max_overs = MATCH_TYPES[self.state.match_type]['max_bowler_overs']
        available = [b for b, stats in bowlers_dict.items() if (stats[1]//6) < max_overs and b != previous_bowler]
        if not available: available = list(bowlers_dict.keys())

        if is_user_bowling and not self.state.sim_mode:
            print("\nAvailable Bowlers and Stats:")
            for b in available:
                print(f"-> {b}: {bowlers_dict[b][0]}-{bowlers_dict[b][2]} in {bowlers_dict[b][1]} overs")
            while True:
                choice = input("Choose Bowler [Enter = Auto]: ").strip().lower()
                if choice == "": return random.choice(available)
                if choice in available: return choice
                print("Select a valid bowler.")
        else:
            return random.choice(available)

    def play_innings(self, batting_team: str, bowling_team: str, innings_num: int = 1, base_lead: int = None, target: int = None) -> int:
        self.state.reset_innings()
        is_user_batting, is_user_bowling = (batting_team == "India"), (bowling_team == "India")
        batsmen_data = self.state.indian_batsmen if is_user_batting else self.state.australian_batsmen
        bowlers_data = self.state.indian_bowlers if is_user_bowling else self.state.australian_bowlers
        opp_players = list((self.state.australian_batsmen if is_user_batting else self.state.indian_batsmen).keys())
        
        keys = list(batsmen_data.keys())
        current_batsmen = [keys[0], keys[1]] 
        remaining_keys = keys[2:]
        active_idx = 0
        boundary_streak = {k: 0 for k in keys}
        
        def pick_auto_bowler(prev=""):
            avail = [b for b, st in bowlers_data.items() if (st[1]//6) < MATCH_TYPES[self.state.match_type]['max_bowler_overs'] and b != prev]
            return random.choice(avail if avail else list(bowlers_data.keys()))

        current_bowler = pick_auto_bowler()
        delivery_pool = get_bowler_delivery_pool(self.state.match_type)
        max_overs = MATCH_TYPES[self.state.match_type]['overs']
        target_reached = False
        declared = False
        
        while (self.state.balls_played // 6) < max_overs and self.state.wickets < 10:
            current_over_log = []
            for ball in range(6):
                if target is not None and self.state.runs >= target:
                    target_reached = True; break
                
                ctx_str = ""
                if target: ctx_str = f"TARGET: {target} │ NEED {target - self.state.runs}"
                elif base_lead is not None:
                    if innings_num == 2:
                        diff = base_lead - self.state.runs
                        ctx_str = f"Trails by {diff}" if diff > 0 else "Scores Level" if diff == 0 else f"Leads by {abs(diff)}"
                    elif innings_num == 3:
                        diff = base_lead + self.state.runs
                        ctx_str = f"Leads by {diff}" if diff > 0 else "Scores Level" if diff == 0 else f"Trails by {abs(diff)}"
                
                if not self.state.sim_mode and not self.state.debug_mode:
                    clear_screen()
                    self.display_scorecard(batting_team, bowling_team, batsmen_data, bowlers_data, current_batsmen, active_idx, current_bowler, current_over_log, ball, ctx_str)
                
                self.state.balls_played += 1; self.state.total_match_balls += 1
                prog_pct = round((self.state.balls_played / {'t20i':120, 'odi':300, 'test':10000}[self.state.match_type]) * 100)
                
                active_key = current_batsmen[active_idx]
                momentum = batsmen_data[active_key][6]

                # Inputs Bypass for Sim Mode
                if self.state.sim_mode:
                    inp = ""
                else:
                    if is_user_batting:
                        inp = input("Enter shot (0, 1, 2, 3, 4, 6) or 's' for Scorecard [Enter=Auto]: ").strip().lower()
                    else:
                        # Strictly validate bowling input to reject 0 and 5
                        while True:
                            inp = input("Enter bowl (1, 2, 3, 4, 6) or 's' for Scorecard [Enter=Auto]: ").strip().lower()
                            if inp in ["", "s", "1", "2", "3", "4", "6"]:
                                break
                            print("Invalid choice. Bowlers are not permitted to bowl 0 or 5.")
                
                if inp == 's':
                    from html_generator import generate_html_scorecard
                    path = generate_html_scorecard(self.state, batting_team, target=target)
                    webbrowser.open(f"file://{path}")
                    inp = input("Resuming... Enter action [Enter=Auto]: ").strip().lower()
                    if not is_user_batting:
                        while True:
                            if inp in ["", "s", "1", "2", "3", "4", "6"]:
                                break
                            print("Invalid choice. Bowlers are not permitted to bowl 0 or 5.")
                            inp = input("Resuming... Enter action [Enter=Auto]: ").strip().lower()

                ai_val = run_ai_play(prog_pct, batting_team, self.state.match_type, self.state)
                if is_user_batting:
                    user_runs = int(inp) if inp in ['1','2','3','4','6'] else ai_val
                    bowler_choice = random.choice(delivery_pool)
                    shot_chosen = user_runs
                else:
                    # Enforce that only valid bowling values are processed
                    bowler_choice = int(inp) if inp in ['1', '2', '3', '4', '6'] else random.choice([x for x in delivery_pool if x not in [0, 5]])
                    shot_chosen = ai_val
                
                bowling_bias = {1: -0.05, 2: -0.02, 3: 0.0, 4: 0.02, 6: 0.05}.get(bowler_choice, 0.0) if is_user_bowling and not is_user_batting else 0.0

                is_wicket = False
                runs_scored = 0
                scoring = MATCH_SCORING[self.state.match_type]

                # Track boundary streak
                if shot_chosen in [4, 6]:
                    boundary_streak[active_key] += 1
                else:
                    boundary_streak[active_key] = 0

                # Calculate cumulative risk penalties for consecutive boundary attempts
                streak = boundary_streak[active_key]
                streak_penalty = 0.0
                if streak > 1:
                    if self.state.match_type == 'test':
                        streak_penalty = 0.15 * (streak - 1)
                    elif self.state.match_type == 'odi':
                        streak_penalty = 0.08 * (streak - 1)
                    else:  # t20i
                        streak_penalty = 0.04 * (streak - 1)

                if shot_chosen in [4, 6]:
                    success_threshold = scoring['boundary_base'] + (momentum / scoring['boundary_momentum_divisor']) + bowling_bias - streak_penalty
                    success_threshold = max(0.02, min(0.95, success_threshold))
                    
                    if random.random() < success_threshold:
                        runs_scored = shot_chosen
                        momentum_gain = max(1, 10 - int(streak_penalty * 20))
                        batsmen_data[active_key][6] = min(100, momentum + momentum_gain)
                    else:
                        out_threshold = scoring['boundary_wicket_base'] - (momentum / scoring['boundary_wicket_momentum_divisor']) - bowling_bias + streak_penalty
                        out_threshold = max(0.05, min(0.95, out_threshold))
                        if random.random() < out_threshold:
                            is_wicket = True
                        else:
                            runs_scored = random.choice([0, 1])
                            batsmen_data[active_key][6] = max(10, momentum - 5 - int(streak_penalty * 10))
                else:
                    # Provide safety bonuses for defensive blocks (0) and placement shots (1, 2)
                    safety_bonus = 0.0
                    if shot_chosen == 0:
                        safety_bonus = 0.35 if self.state.match_type == 'test' else 0.25
                    elif shot_chosen in [1, 2]:
                        safety_bonus = 0.15 if self.state.match_type == 'test' else 0.10

                    success_threshold = scoring['shot_base'] + (momentum / scoring['shot_momentum_divisor']) + bowling_bias + safety_bonus
                    success_threshold = max(0.05, min(0.98, success_threshold))
                    
                    if random.random() < success_threshold:
                        runs_scored = shot_chosen
                        if runs_scored in [1, 2]:
                            batsmen_data[active_key][6] = min(100, momentum + 5)
                        else:
                            batsmen_data[active_key][6] = max(10, momentum - 1)
                    else:
                        is_wicket = True

                # AI Strike rotation limits
                if self.state.match_type == 'test' and self.state.wickets > 5 and not is_wicket:
                    act_runs = batsmen_data[active_key][0]
                    non_runs = batsmen_data[current_batsmen[1 - active_idx]][0]
                    if act_runs > non_runs + 20:
                        if ball in [0, 1, 2, 3] and runs_scored == 1: runs_scored = random.choice([0, 2])
                        elif ball in [4, 5] and runs_scored in [0, 2]: runs_scored = 1
                    elif act_runs + 20 < non_runs:
                        if ball in [0, 1, 2] and runs_scored in [0, 2]: runs_scored = 1

                if is_wicket:
                    if batsmen_data[active_key][2] > 1:
                        batsmen_data[active_key][2] -= 1; current_over_log.append('0')
                        batsmen_data[active_key][1] += 1
                        boundary_streak[active_key] = 0
                        if not self.state.sim_mode:
                            print(f"Chance missed! {PLAYERS[active_key]} survived."); input("...")
                    else:
                        self.state.wickets += 1; bowlers_data[current_bowler][2] += 1; current_over_log.append('W')
                        
                        dt = random.choice(["b", "lbw", "c"])
                        fielder = PLAYERS[random.choice(opp_players)].split(" ")[-1]
                        bw_name = PLAYERS[current_bowler].split(" ")[-1]
                        dismissal_str = f"b {bw_name}" if dt in ["b", "lbw"] else f"c {fielder} b {bw_name}"
                        if dt == "lbw": dismissal_str = f"lbw " + dismissal_str
                        batsmen_data[active_key][5] = dismissal_str
                        
                        if not self.state.sim_mode:
                            print(f"\nOUT! {PLAYERS[active_key]} - {dismissal_str}"); input("...")
                        
                        if self.state.wickets < 10 and remaining_keys:
                            next_b = remaining_keys.pop(0)
                            current_batsmen[active_idx] = next_b
                            boundary_streak[next_b] = 0
                        else: break
                else:
                    self.state.runs += runs_scored; current_over_log.append(str(runs_scored))
                    batsmen_data[active_key][0] += runs_scored; batsmen_data[active_key][1] += 1
                    if runs_scored == 4: batsmen_data[active_key][4][0] += 1
                    if runs_scored == 6: batsmen_data[active_key][4][1] += 1
                    bowlers_data[current_bowler][0] += runs_scored
                    if runs_scored % 2 != 0: active_idx = 1 - active_idx

                if self.state.debug_mode:
                    outcome = "W" if is_wicket else str(runs_scored)
                    over_num = self.state.balls_played // 6
                    ball_num = self.state.balls_played % 6
                    print(f"[DEBUG] {batting_team} {over_num}.{ball_num} {PLAYERS[active_key]} vs {PLAYERS[current_bowler]} -> {outcome} | {self.state.runs}/{self.state.wickets}")
                    
            if target_reached: break
            
            bowlers_data[current_bowler][1] += len(current_over_log)
            if self.state.wickets >= 10: break
            active_idx = 1 - active_idx
            
            # --- DECLARATION CHECK FOR TEST MATCHES ---
            if self.state.match_type == 'test' and (self.state.balls_played // 6) > 20:
                if is_user_batting and not self.state.sim_mode:
                    dec = input("Do you want to DECLARE this innings? (y/n): ").strip().lower()
                    if dec == 'y': declared = True; break
                else:
                    if innings_num == 3 and base_lead and (base_lead + self.state.runs) > 350:
                        if not self.state.sim_mode:
                            print(f"\nAustralia has DECLARED the innings!"); input("...")
                        declared = True; break

            # Choose Bowler
            if (self.state.balls_played // 6) < max_overs:
                    if is_user_bowling and not self.state.sim_mode:
                        inp = input(f"Over End. Enter next bowler [Enter=Auto]: ").strip().lower()
                        current_bowler = inp if inp in bowlers_data and bowlers_data[inp][1]//6 < MATCH_TYPES[self.state.match_type]['max_bowler_overs'] and inp != current_bowler else pick_auto_bowler(current_bowler)
                    else: 
                        current_bowler = pick_auto_bowler(current_bowler)

        if not self.state.sim_mode and not self.state.debug_mode:
            clear_screen()
            self.display_scorecard(batting_team, bowling_team, batsmen_data, bowlers_data, current_batsmen, active_idx, current_bowler, current_over_log, 6, ctx_str)
                                   
        self.state.archive_innings(batting_team, bowling_team)
        return self.state.runs
