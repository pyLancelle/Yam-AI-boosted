def get_number_of_players():
    while True:
        nb_joueurs = input("How many players? ")
        try:
            valeur = int(nb_joueurs)
            return valeur
        except ValueError:
            print("The value you input isn't numeric. Please enter a valid number.")