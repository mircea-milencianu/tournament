import axelrod as axl
from rich import print

from timeit import default_timer as timer

from axelrod import tournament
from axelrod import result_set

TURNS = 200
REPETITIONS = 1
RUN_TYPE = "dev"

player_set = {
    "dev_tour": [axl.Cooperator(), axl.Defector(), axl.TitForTat()],
    "first_tour": [s() for s in axl.axelrod_first_strategies],
    "second_tour": [
        s() for s in axl.axelrod_second_strategies
    ],  # this is created by me and can be found in the init file for the axl library; in case of error
    "all": [s() for s in axl.all_strategies],
}

def step_run(players, deviation):

    tournament_mc = axl.Tournament(
        players, turns=TURNS, uniform=True, deviation=deviation, repetitions=REPETITIONS
    )
    result_set_mc = tournament_mc.play(filename="tournament_mc.csv", processes=4)  #
    end = timer()
    matrix_mc = axl.ResultMatrix(
        filename="tournament_mc.csv",
        players=players,
        repetitions=REPETITIONS,
        deviation=deviation,
        run_type="montecarlo"
    )
    winner_matrix = matrix_mc.create()

def main():
    ### INIT ###
    # players = player_set["dev_tour"] + player_set["second_tour"]
    players = player_set["dev_tour"]

    tournament_mc = axl.Tournament(
        players, turns=TURNS, uniform=True, deviation=deviation, repetitions=REPETITIONS
    )
    result_set_mc = tournament_mc.play(filename="tournament_mc.csv", processes=4)  #
    end = timer()
    matrix_mc = axl.ResultMatrix(
        filename="tournament_mc.csv",
        players=players,
        repetitions=REPETITIONS,
        run_type="montecarlo",
        tour_type="dev",
    )
    winner_matrix = matrix_mc.create()


    ### run basic tour with no dev
    # tournament_default = axl.Tournament(players, turns=TURNS, repetitions=REPETITIONS)
    # result_set_default = tournament_default.play(
    #     filename="tournament_default.csv", processes=4
    # )  
    # matrix_default = axl.ResultMatrix(
    #     filename="tournament_default.csv",
    #     players=players,
    #     repetitions=REPETITIONS,
    #     deviation=None,
    #     run_type="default"
    # )
    # winner_matrix = matrix_default.create()
    # ### run basic tour with no dev ###############################

    # deviation = 20
    # step = 2
    # while deviation >= 1:
    #     step_run(players, deviation)
    #     deviation = deviation - step
    

if __name__ == "__main__":
    main()
