import axelrod as axl
import pprint as p


players =  [axl.Cooperator(), axl.Defector(),
            axl.TitForTat()]

mc_tournament = axl.McTournament(players, turns=50, deviation=5, repetitions=1)
winner_set = mc_tournament.play(filename="mc_tournament.csv")

winner_matrix = winner_set.build_winner_pd()