import axelrod as axl
import pprint as p

from timeit import default_timer as timer


player_set = {
    
    "dev_tour" : [axl.Cooperator(), axl.Defector(), axl.TitForTat()],
    "first_tour" : [s() for s in axl.axelrod_first_strategies],
    "second_tour" : [s() for s in axl.axelrod_second_strategies],
    "all" : [s() for s in axl.all_strategies],
}

def main():
    ### INIT ###
    players = player_set["first_tour"] # + player_set["second_tour"]
    start = timer()
    tournament = axl.Tournament(players, turns=200, deviation=20, repetitions=1)
    end = timer()
    print("time spent for init: {}".format(end - start))
    ### PLAY ###
    start = timer()
    result_set = tournament.play(filename="new_tournament.csv",processes=0) #
    end = timer()
    print("time spent for playing the matches: {}".format(end - start))
    ### EXPORT ###
    start = timer()
    matrix = axl.ResultMatrix(filename="new_tournament.csv", players=players, repetitions=200)
    winner_matrix = matrix.create()
    end = timer()
    print("time spent for building the matrix: {}".format(end - start))

if __name__ == "__main__":
    main()