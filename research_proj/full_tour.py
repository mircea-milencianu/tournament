import axelrod as axl
import pprint as p

players = [s() for s in axl.axelrod_first_strategies]


# players =  [axl.Cooperator(), axl.Defector(),
#             axl.TitForTat()]
def main():
    tournament = axl.Tournament(players, turns=200, deviation=10, repetitions=1)
    result_set, result_matrix = tournament.play(filename="new_tournament.csv", processes=2)

# print(result_matrix)
# print(result_set)
    winner_matrix = result_matrix.build_winner_pd()
# print(winner_matrix)

if __name__ == "__main__":
    main()