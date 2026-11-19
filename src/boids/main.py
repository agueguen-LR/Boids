from boids import __version__, Boids
import numpy as np

print("Hello world!")
print(__version__)


boids = Boids(4)

print(boids[1:])
print(boids[0])
print(np.linalg.norm(boids[0].velocity))
