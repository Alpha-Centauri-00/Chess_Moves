from chessdotcom import get_leaderboards,get_player_stats,get_player_game_archives
import pprint
import requests
#from get_Chess_Moves import *


printer = pprint.PrettyPrinter()
def print_Leaderboard():
    data = get_leaderboards().json
    cate = data.keys()

    for cat in cate:
        print('Category: ',cat)
        for idx, entry in enumerate(data[cat]):
            print(f'Rank: {idx + 1}| Username: {entry["username"]} | Rating: {entry["score"]}')

def get_Player_Rating(player):
    try:
        data = get_player_stats(player).json
        categories = ['chess_blitz','chess_rapid','chess_bullet']
        for category in categories:
            print(f'Current Rating for {player} in {category} is: {data[category]["last"]["rating"]}')
    except:
        print(f'{player} has no Rating in {category}')


def get_most_recelt_game_for(player):
    data = get_player_game_archives(player).json
    Url = data['archives'][-1]
    games = requests.get(Url).json()
    last_game = games['games'][-1]
    printer.pprint(last_game)

    # The_Url = last_game['url']
    # get_Moves_chess_dot_com(The_Url)
    #print(The_Url)
    

get_Player_Rating("Hikaru")

#print_Leaderboard()
#get_most_recelt_game_for("Hikaru")
#get_most_recelt_game_for("elprofesorsergio")

