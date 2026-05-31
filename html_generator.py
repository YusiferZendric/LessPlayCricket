# html_generator.py
import webbrowser
import os
from config import PLAYERS

def generate_html_scorecard(state, current_bat_team=None, target=None, match_ended=False, result_text="") -> str:
    def format_overs(balls): return f"{balls//6}.{balls%6}"

    def build_bat_table(batsmen_dict):
        rows = ""
        for key, stats in batsmen_dict.items():
            runs, balls, lives, _, bounds, dismissal, momentum = stats
            sr = round((runs / balls) * 100, 1) if balls > 0 else 0.0
            
            if balls == 0 and lives > 0 and dismissal == "NOT OUT": 
                status = "<span class='status-dnb'>DNB</span>"
            elif dismissal == "NOT OUT": 
                status = f"<span class='status-notout'>NOT OUT ({momentum}%)</span>"
            else: 
                status = f"<span class='status-out'>{dismissal}</span>"
            
            rows += f"<tr><td class='p-name'>{PLAYERS[key]}</td><td class='p-dismissal'>{status}</td><td class='s-main'>{runs}</td><td>{balls}</td><td>{bounds[0]}</td><td>{bounds[1]}</td><td class='s-gold'>{sr}</td></tr>"
        return rows

    def build_bowl_table(bowlers_dict):
        rows = ""
        for key, stats in bowlers_dict.items():
            runs, balls, wkts = stats
            if balls == 0: continue
            overs = format_overs(balls)
            econ = round(runs / (balls/6), 2) if balls > 0 else 0.00
            rows += f"<tr><td class='p-name'>{PLAYERS[key]}</td><td class='s-main'>{overs}</td><td>{runs}</td><td class='s-main'>{wkts}</td><td class='s-gold'>{econ}</td></tr>"
        return rows

    def build_innings_block(inn_data, title_prefix):
        return f"""
        <div class="team-card">
            <div class="team-header"><span>{title_prefix}: {inn_data['bat_team'].upper()}</span><span class="score-bubble">{inn_data['runs']}/{inn_data['wickets']} ({inn_data['overs']})</span></div>
            <div class="section-title">BATTING</div>
            <table><thead><tr><th>Batsman</th><th>Dismissal / Presence</th><th>R</th><th>B</th><th>4s</th><th>6s</th><th>SR</th></tr></thead><tbody>{build_bat_table(inn_data['batsmen'])}</tbody></table>
            <div class="section-title">BOWLING</div>
            <table><thead><tr><th>Bowler</th><th>O</th><th>R</th><th>W</th><th>Econ</th></tr></thead><tbody>{build_bowl_table(inn_data['bowlers'])}</tbody></table>
        </div>"""

    all_innings = []
    for i, inn in enumerate(state.innings_history):
        all_innings.append(build_innings_block(inn, f"INNINGS {i+1}"))
    
    if not match_ended and current_bat_team:
        live_inn = {
            "bat_team": current_bat_team,
            "runs": state.runs, "wickets": state.wickets, "overs": format_overs(state.balls_played),
            "batsmen": state.indian_batsmen if current_bat_team == "India" else state.australian_batsmen,
            "bowlers": state.australian_bowlers if current_bat_team == "India" else state.indian_bowlers
        }
        all_innings.append(build_innings_block(live_inn, f"INNINGS {len(state.innings_history)+1} (LIVE)"))

    ticker = result_text if match_ended else "LIVE MATCH"
    if target and not match_ended: 
        ticker = f"TARGET: {target} │ NEED {target - state.runs} TO WIN"
    elif hasattr(state, 'lead_text') and state.lead_text:
        ticker = state.lead_text

    html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Match Center</title>
    <style>
        body {{ font-family: -apple-system, sans-serif; background: #12181f; color: #fff; margin: 0; padding: 20px; }}
        .container {{ max-width: 1000px; margin: 0 auto; }}
        header {{ background: linear-gradient(135deg, #094a30, #1c2630); padding: 20px; text-align: center; border-radius: 8px; border: 1px solid #2a3b4c; margin-bottom: 20px; }}
        .ticker {{ background: #000; color: #f2a900; padding: 6px 15px; border-radius: 15px; font-weight: bold; font-size: 14px; margin-top: 10px; display: inline-block;}}
        .team-card {{ background: #1c2630; border: 1px solid #2a3b4c; border-radius: 8px; margin-bottom: 30px; overflow: hidden; }}
        .team-header {{ background: #0f8b5a; padding: 12px 20px; font-weight: bold; font-size: 18px; display: flex; justify-content: space-between; border-bottom: 3px solid #f2a900; }}
        .score-bubble {{ background: rgba(0,0,0,0.3); padding: 3px 10px; border-radius: 10px; }}
        table {{ width: 100%; border-collapse: collapse; text-align: left; font-size: 14px; }}
        th, td {{ padding: 10px 15px; border-bottom: 1px solid #2a3b4c; }}
        th {{ color: #8b9eb3; font-size: 11px; text-transform: uppercase; }}
        .p-name {{ font-weight: 500; color: #e2e8f0; width: 22%; }}
        .p-dismissal {{ color: #8b9eb3; width: 33%; font-size: 12px; }}
        .s-main {{ font-weight: bold; color: #fff; }}
        .s-gold {{ color: #f2a900; }}
        .status-notout {{ color: #14ad71; font-weight: bold; }}
        .status-out {{ color: #ef4444; }}
        .status-dnb {{ color: #5a6b7c; }}
        .section-title {{ background: rgba(0,0,0,0.2); padding: 6px 20px; font-size: 11px; font-weight: bold; color: #8b9eb3; }}
    </style></head><body><div class="container">
        <header><h2>{state.match_type.upper()} MATCH CENTER</h2><div class="ticker">{ticker}</div></header>
        {''.join(all_innings)}
    </div></body></html>"""
    
    file_path = "scorecard.html"
    with open(file_path, "w", encoding="utf-8") as f: f.write(html)
    return os.path.abspath(file_path)
