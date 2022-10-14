import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

pokemon_dataset = pandas.read_csv("pokemon.csv")