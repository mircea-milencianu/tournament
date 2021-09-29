import axelrod as axl
import pprint as p

from timeit import default_timer as timer


#players = [s() for s in axl.axelrod_first_strategies]

players_first = [s() for s in axl.axelrod_first_strategies]
players_second = [s() for s in axl.axelrod_second_strategies]

players = players_first + players_second

def main():
    ### INIT ###
    start = timer()
    tournament = axl.Tournament(players, turns=200, deviation=20, repetitions=200)
    end = timer()
    print("time spent for init: {}".format(end - start))
    ### PLAY ###
    start = timer()
    result_set, result_matrix = tournament.play(filename="new_tournament.csv", processes=0)
    end = timer()
    print("time spent for playing the matches: {}".format(end - start))
    ### EXPORT ###
    start = timer()
    winner_matrix = result_matrix.build_winner_pd()
    end = timer()
    print("time spent for playing the matches: {}".format(end - start))

if __name__ == "__main__":
    main()