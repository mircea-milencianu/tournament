"""
RUN_SCOPE: string
    Defines the scope of run. ex: dev, first strategy set, second strategy set, all strategies;
SINGLE_RUN: bool
    Defines the type of run. 
    True: single run;
    False: multiple runs with a constant DEVIATION that changes by a fixed step;
    REQUIRES STEP TO BE DEFINED!
STEP: int
    A value by which the value of the DEVIATION decreases.
    The desired behaviour is to start with a large deviation and get close to 0, meaning a default tournament.
DISTRIBUTION: string
    The type of distribution from where the number of turns are extracted.
    normal: normal distribution
    uniform: uniform distribution
TURNS: int
    Number of turns in a supergame. A single turn round is a simple game.
REPETITIONS: int
    The number of repetitions of a supergame.

"""
from random import uniform
import axelrod as axl
from rich import print
import json

from timeit import default_timer as timer

from axelrod import tournament
from axelrod import result_set

RUN_SCOPE = "all_strategies_test_run"
TOUR_TYPE = "simple"
SINGLE_RUN = True
DEVIATION = 20
STEP = 2
DISTRIBUTION = "uniform"

TURNS = 200
REPETITIONS = 1000
# Set to TRUE to enable a deviation step run. 
# A deviation step needs to be provided along the variable

PROCESSES = 20

player_set = {
    "dev_tour": [axl.Cooperator(), axl.Defector(), axl.TitForTat()],
    "first_tour": [s() for s in axl.axelrod_first_strategies],
    "second_tour": [
        s() for s in axl.axelrod_second_strategies
    ],  # this is created by me and can be found in the init file for the axl library; in case of error
    "all": [s() for s in axl.all_strategies],
}

def play_step_tournaments(players):
    local_deviation = DEVIATION

    while local_deviation >= 1:
        play_tournament(players, "dev_with_step")
        local_deviation = local_deviation - STEP


def play_tournament(players, tour_type):
        
        ### Tournament setup
        filename = ""
        if DISTRIBUTION == "uniform":
            tournament = axl.Tournament(
                players, turns=TURNS, uniform=True, deviation=DEVIATION, repetitions=REPETITIONS
            )
            filename = "uniform_distribution_tournament"

        elif DISTRIBUTION == "normal":
            tournament = axl.Tournament(
                players, turns=TURNS, normal=True, deviation=DEVIATION, repetitions=REPETITIONS
            )
            filename = "normal_distribution_tournament"
        else:
            tournament = axl.Tournament(players, turns=TURNS, repetitions=REPETITIONS)
            filename = "default_tournament"

        ### Play tournament
        result_set_mc = tournament.play(filename="{}.csv".format(filename), processes=PROCESSES)  #
        matrix_mc = axl.ResultMatrix(
            filename="{}.csv".format(filename),
            players=players,
            repetitions=REPETITIONS,
            tour_type=tour_type, #'montecarlo'
            run_scope=RUN_SCOPE
        )
        winner_matrix = matrix_mc.create()

def main():

    players = player_set["all"]
    start = timer()
    if SINGLE_RUN is True:
        play_tournament(players, TOUR_TYPE)
    else:
        play_step_tournaments(players, TOUR_TYPE)
    end = timer()

    run_summary = {
        "run_time": end - start,
        "processes":PROCESSES,
        "run_scope": RUN_SCOPE,
        "tour_type": TOUR_TYPE,
        "single_run": SINGLE_RUN,
        "distribution": DISTRIBUTION,
        "turns": TURNS,
        "repetitions": REPETITIONS,
        "deviation": DEVIATION,
        "step": STEP,
    }
    with open("results_{}/run_summary.json".format(TOUR_TYPE), 'w') as fp:
        json.dump(run_summary, fp)
    

if __name__ == "__main__":
    main()
