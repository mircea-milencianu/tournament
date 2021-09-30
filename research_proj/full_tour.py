import axelrod as axl
import pprint as p

from timeit import default_timer as timer


player_set = {
    
    "dev_tour" : [axl.Cooperator, axl.Defector, axl.TitForTat],
    "first_tour" : [s() for s in axl.axelrod_first_strategies],
    "second_tour" : [s() for s in axl.axelrod_second_strategies],
    "all" : [s() for s in axl.all_strategies],
}

def main():
    ### INIT ###
    players = player_set["dev_tour"]
    start = timer()
    tournament = axl.Tournament(players, turns=200, deviation=20, repetitions=200)
    end = timer()
    print("time spent for init: {}".format(end - start))
    ### PLAY ###
    start = timer()
    result_set = tournament.play(filename="new_tournament.csv", processes=0)
    end = timer()
    print("time spent for playing the matches: {}".format(end - start))
    ### EXPORT ###
    start = timer()
    winner_matrix = axl.ResultMatrix(players).create(filename="new_tournament.csv")
    end = timer()
    print("time spent for playing the matches: {}".format(end - start))

if __name__ == "__main__":
    main()