import pandas as pd
import matplotlib.pyplot as plt

print("--------------- Welcome to the NBA data analysis app! --------------")
print("--------- We have a great selection of questions to answer ---------")
print("--------------------- Stats from 1950 to 2017 ----------------------")

df = pd.read_csv('Seasons_Stats.csv')
selection = -1

while selection != 0:
    print("\nTo start what would you like to search by?")
    print("1. Player")
    print("2. Year")
    print("3. All Time All Around")
    print("4. View Key")
    print("5. Quit")
    selection = int(input("Please select one of the above: "))

    match selection:
        case 1:
            player = input("Please enter your players full name. Be mindful, correct spelling is needed ").lower()
            player_data = df[df['Player'].str.lower() == player]

            if len(player_data) == 0:
                print("Player not found. Please try again.")
                continue

            # Ignore non numeric columns
            numeric_columns = player_data.select_dtypes(include=[float, int]).columns
            player_data_numeric = player_data[numeric_columns]

            # group by year
            yearly_totals = player_data_numeric.groupby('Year').sum()
            years_played = len(yearly_totals)

            career_averages = yearly_totals.drop(columns=['Index', 'Age']).mean().round(2)
            stats = list(career_averages.index)
            values = list(career_averages.values)

            # create line chart
            plt.figure(figsize=(12, 8))
            plt.plot(stats, values, marker='o', linestyle='-')
            plt.title("Career Averages Across Different Statistics")
            plt.xlabel('Statistics')
            plt.ylabel('Average Value')
            plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability
            plt.grid(True)
            plt.tight_layout()

            # Show the plot
            plt.show()




        case 2:
            year = int(input("Please enter what year you would like to examine: "))
            # Get top 5 scorers of that year
            top_scorers = df[df['Year'] == year].nlargest(5, 'PTS')
            top_scorers['Points per game'] = ((top_scorers['PTS'] // top_scorers['G']).astype(int)).round(2)
            print(f"\nPoints per Game for Top Point Leaders in {year}:")
            print(top_scorers[['Player', 'Points per game']].to_string(index=False))


            # Get top 5 assist leaders of that year
            top_assisters = df[df['Year'] == year].nlargest(5, 'AST')
            top_assisters['Assist per game'] = ((top_assisters['AST'] // top_assisters['G']).astype(int)).round(2)
            print(f"\nAssists per Game for Top Assist Leaders in {year}:")
            print(top_assisters[['Player', 'Assist per game']].to_string(index=False))

        case 3:
            # Greatest All Around
            included_stats = ['PTS', 'AST', 'TRB', 'STL', 'BLK', 'FG%', 'PER', 'WS', 'TOV'] # These are the selected stats
            numeric_columns = df[included_stats]

            player_stats_sum = numeric_columns.groupby(df['Player']).sum() # Adding stats together

            total_games_played = df.groupby('Player')['G'].sum() # Adding games together

            player_stats_avg_per_game = player_stats_sum.div(total_games_played, axis=0)

            top_players = player_stats_avg_per_game.nlargest(5, included_stats).round(2)

            print("Players with Highest Average Per Game Stats:")
            print(top_players)
            
            # Greatest Devensive players
            defensive_stats = ['STL', 'TRB', 'BLK', 'DWS', 'PER'] # These are the selected stats
            numeric_columns = df[defensive_stats]

            player_defensive_stats_sum = numeric_columns.groupby(df['Player']).sum() # Adding stats together

            total_games_played = df.groupby('Player')['G'].sum() # Adding games together

            defensive_avg_per_game = player_defensive_stats_sum.div(total_games_played, axis=0)

            top_defensive_players = defensive_avg_per_game.nlargest(5, defensive_stats).round(2)

            print("Players with Highest Defensive Per Game Stats:")
            print(top_defensive_players)
            # Greatest offensive player
            
            offensive_stats = ['PTS', 'AST', 'TRB', 'FG%', 'PER', 'WS', 'TOV'] # These are the selected stats
            numeric_columns = df[offensive_stats]

            player_offensive_stats_sum = numeric_columns.groupby(df['Player']).sum() # Adding stats together

            total_games_played = df.groupby('Player')['G'].sum() # Adding games together

            offensive_avg_per_game = player_offensive_stats_sum.div(total_games_played, axis=0)

            top_offensive_players = offensive_avg_per_game.nlargest(5, offensive_stats).round(2)

            print("Players with Highest Offensive Per Game Stats:")
            print(top_offensive_players)


        case 4:
            # Define the text with proper formatting
            # This section was done with the help of AI
            info_text = """
            Index: Index of the player's stats          Year: The year of the season            Player: Player's name           Pos: Player's position                  Age: Player's age
            Tm: Team                                    G: Games played                         GS: Games started               MP: Minutes played                      PER: Player Efficiency Rating
            TS%: True Shooting Percentage               3PAr: 3-Point Attempt Rate              FTr: Free Throw Attempt Rate    ORB%: Offensive Rebound Percentage      DRB%: Defensive Rebound Percentage  
            TRB%: Total Rebound Percentage              AST%: Assist Percentage                 STL%: Steal Percentage          BLK%: Block Percentage                  TOV%: Turnover Percentage
            USG%: Usage Percentage                      blanl: Blank (always 0)                 OWS: Offensive Win Shares       DWS: Defensive Win Shares               WS: Win Shares
            WS/48: Win Shares Per 48 Minutes            blank2: Blank (always 0)                OBPM: Offensive Box Plus/Minus  DBPM: Defensive Box Plus/Minus          BPM: Box Plus/Minus
            VORP: Value Over Replacement Player         FG: Field Goals                         FGA: Field Goal Attempts        FG%: Field Goal Percentage              3P: 3-Point Field Goals
            3PA: 3-Point Field Goal Attempts            3P%: 3-Point Field Goal Percentage      2P: 2-Point Field Goals         2PA: 2-Point Field Goal Attempts        2P%: 2-Point Field Goal Percentage  
            eFG%: Effective Field Goal Percentage       FT: Free Throws                         FTA: Free Throw Attempts        FT%: Free Throw Percentage              ORB: Offensive Rebounds
            DRB: Defensive Rebounds                     TRB: Total Rebounds                     AST: Assists                    STL: Steals                             BLK: Blocks
            TOV: Turnovers                              PF: Personal Fouls                      PTS: Points
            """

            # Print the formatted text
            print(info_text)

        case 5:
            print("Exiting program...")
            break

    


    
    





