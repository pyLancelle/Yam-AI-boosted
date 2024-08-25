from src.game.player import Game, Player
from src.functions import get_number_of_players

if __name__ == '__main__':
    nb_joueurs = get_number_of_players()

    g = Game(nb_joueurs)
    for _ in range(13):
        for p in g.players:
            
    g.run()