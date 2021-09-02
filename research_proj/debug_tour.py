import axelrod as axl

players =  [axl.Cooperator(), axl.Defector(),
            axl.TitForTat()]

tournament = axl.Tournament(players, turns=100, deviation=5, repetitions=2)
matrix_test = tournament.play(filename="basic_tournament.csv")
