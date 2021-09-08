import axelrod as axl
import pprint as p


players =  [axl.Cooperator(), axl.Defector(),
            axl.TitForTat()]

tournament = axl.Tournament(players, turns=100, deviation=5, repetitions=1)
result_set, result_matrix = tournament.play(filename="new_tournament.csv")

# print(result_matrix)
# print(result_set)
winner_matrix = result_matrix.build_winner_pd()

# print(winner_matrix)