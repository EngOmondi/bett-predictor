import itertools

def generate_outcomes():
    outcomes = []
    
    # Define the game details
    games = [
        {
            'home_team': 'NC Magra',
            'away_team': 'CS Constantine',
            'home_odds': 2.10,
            'draw_odds': 3.05,
            'away_odds': 3.65
        },
        {
            'home_team': 'RC Arbaa',
            'away_team': 'USM Alger',
            'home_odds': 2.17,
            'draw_odds': 3.25,
            'away_odds': 3.20
        },
        # Add more games here if needed
    ]
    
    # Generate all possible outcomes
    for outcome in itertools.product(['home', 'draw', 'away'], repeat=len(games)):
        outcome_odds = [games[i][outcome[i] + '_odds'] for i in range(len(games))]
        if max(outcome_odds) in outcome_odds:
            outcomes.append(dict(zip([game['home_team'] for game in games], outcome)))
    
    return outcomes

# Generate outcomes
outcomes = generate_outcomes()

# Print the outcomes
for i, outcome in enumerate(outcomes):
    print(f"Outcome {i+1}:")
    for team, result in outcome.items():
        print(f"{team}: {result}")
    print()
