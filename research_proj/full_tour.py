import axelrod as axl
from rich import print

from timeit import default_timer as timer

from axelrod import tournament
from axelrod import result_set

TURNS = 50
REPETITIONS = 10
DEVIATION = 10
RUN_TYPE = "DEV"

player_set = {
    "dev_tour": [axl.Cooperator(), axl.Defector(), axl.TitForTat()],
    "first_tour": [s() for s in axl.axelrod_first_strategies],
    "second_tour": [
        s() for s in axl.axelrod_second_strategies
    ],  # this is created by me and can be found in the init file for the axl library; in case of error
    "all": [s() for s in axl.all_strategies],
}


def main():
    ### INIT ###
    players = player_set["dev_tour"]  # + player_set["second_tour"]
    start = timer()
    tournament_default = axl.Tournament(players, turns=TURNS, repetitions=REPETITIONS)
    tournament_mc = axl.Tournament(
        players, turns=TURNS, uniform=True, deviation=DEVIATION, repetitions=REPETITIONS
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
        repetitions=REPETITIONS,
        tour_type="default_devNone",
        run_type=RUN_TYPE
    )
    matrix_mc = axl.ResultMatrix(
        filename="tournament_mc.csv",
        players=players,
        repetitions=REPETITIONS,
        tour_type="montecarlo_dev40",
        run_type=RUN_TYPE
    )
    winner_matrix = matrix_mc.create()
    winner_matrix = matrix_default.create()
    end = timer()
    print("time spent for building the matrix: {}".format(end - start))


if __name__ == "__main__":
    main()
