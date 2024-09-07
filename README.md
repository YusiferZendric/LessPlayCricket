# Cricket Match Simulator

This Python script simulates a cricket match between India and Australia. It allows users to play through a T20, ODI, or Test match, making decisions for batting and bowling.

## Features

- Supports T20, ODI, and Test match formats
- Simulates toss and allows user to choose batting or bowling
- Realistic player statistics and performance
- Dynamic gameplay with user input for batting and bowling choices
- Scoreboard updates after each over
- Wagon wheel statistics for batsmen
- Detailed match summary at the end

## How to Use

1. Run the script in a Python environment.
2. Choose the match type (T20, ODI, or Test) when prompted.
3. The toss will be simulated, and you'll be asked to make decisions if India wins the toss.
4. Follow the prompts to select batsmen and bowlers.
5. For batting, enter run values (0, 1, 2, 3, 4, 6) or press Enter for a random choice.
6. For bowling, enter your bowling choice (1, 2, 4, 6) or press Enter for a random choice.
7. Use special commands during play:
   - 'w': View wagon wheel stats
   - 'b': View bowler stats
   - 'B': View batsman stats

## Key Components

- Player dictionaries (IndianBatsman, AustralianBatsman, IndianBowlers, AustralianBowlers)
- Batting and bowling functions to simulate each innings
- Scorecard function to display current match status
- Random play generation based on match situation and player form

## Output

- Real-time score updates
- Over-by-over commentary
- Final match result and statistics
- Detailed scorecard saved to 'highlights.txt'

## Notes

- The script uses randomization to simulate realistic cricket scenarios.
- Player performances are influenced by their initial stats and in-game form.
- The code includes basic error handling for user inputs.

Enjoy simulating exciting cricket matches between India and Australia!
