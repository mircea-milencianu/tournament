import axelrod as axl
import pprint as p

from timeit import default_timer as timer

from axelrod import tournament
from axelrod import result_set


player_set = {
    "dev_tour": [axl.Cooperator(), axl.Defector(), axl.TitForTat()],
    "first_tour": [s() for s in axl.axelrod_first_strategies],
    "second_tour": [s() for s in axl.axelrod_second_strategies],
    "all": [s() for s in axl.all_strategies],
}


def main():
    ### INIT ###
    players = player_set["first_tour"] # + player_set["second_tour"]
    # players = player_set["dev_tour"]
    start = timer()
    tournament_default = axl.Tournament(players, turns=100, repetitions=5)
    tournament_mc = axl.Tournament(
        players, turns=100, uniform=True, deviation=25, repetitions=5
    )
    end = timer()
    print("time spent for init: {}".format(end - start))
    ### PLAY ###
    start = timer()
    result_set_default = tournament_default.play(
        filename="tournament_default.csv", processes=4
    )  #
    result_set_mc = tournament_mc.play(filename="tournament_mc.csv", processes=4)  #
    end = timer()
    print("time spent for playing the matches: {}".format(end - start))
    ### EXPORT ###
    start = timer()
    matrix_default = axl.ResultMatrix(
        filename="tournament_default.csv",
        players=players,
        repetitions=1000,
        tour_type="default_devNone",
    )
    matrix_mc = axl.ResultMatrix(
        filename="tournament_mc.csv",
        players=players,
        repetitions=1000,
        tour_type="montecarlo_dev40",
    )
    winner_matrix = matrix_mc.create()
    winner_matrix = matrix_default.create()
    end = timer()
    print("time spent for building the matrix: {}".format(end - start))


if __name__ == "__main__":
    main()
