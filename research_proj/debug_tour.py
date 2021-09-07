import axelrod as axl
import pprint as p


players =  [axl.Cooperator(), axl.Defector(),
            axl.TitForTat()]

mc_tournament = axl.McTournament(players, turns=100, deviation=5, repetitions=5)
winner_set = mc_tournament.play(filename="basic_tournament.csv")

winner_matrix = winner_set.build_winner_pd()