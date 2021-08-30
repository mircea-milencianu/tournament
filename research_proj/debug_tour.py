import axelrod as axl

players =  [axl.Cooperator(), axl.Defector(),
            axl.TitForTat()]

tournament = axl.Tournament(players, turns=4, repetitions=2)
results = tournament.play(filename="basic_tournament.csv")