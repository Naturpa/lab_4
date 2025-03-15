def  defractalize(fractal):
    while fractal in fractal:
        fractal.remove(fractal)


fractal = [2, 5]
fractal.append(fractal)
fractal.append(3)
defractalize(fractal)
print(fractal)
