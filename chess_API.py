from chessdotcom import get_leaderboards,get_player_stats,get_player_game_archives
import pprint
import requests


printer = pprint.PrettyPrinter()
def print_Leaderboard():
    data = get_leaderboards().json
    
    for player in range(10):

        dict = {}
        name_ = data["leaderboards"]["daily"][player]["username"]
        score = data["leaderboards"]["daily"][player]["score"]
        dict.update({str(name_):str(score)})
        print(dict)

def get_Player_Rating(player):
    try:
        data = get_player_stats(player).json
        categories = ['chess_blitz','chess_rapid','chess_bullet']
        for category in categories:
            print(f'Current Rating for {player} in {category} is: {data["stats"][category]["last"]["rating"]}')
    except:
        print(f'{player} has no Rating in {category}')


def get_most_recelt_game_for(player):
    data = get_player_game_archives(player).json
    Url = data['archives'][-1]
    games = requests.get(Url).json()
    data = games['games'][-1]

    moves = data["pgn"]
    only_moves = moves.split()[49:]

    my_listy = [move for move in only_moves if not move.startswith("{") and not move.endswith("}")]
    printer.pprint(my_listy)