from boids import __version__, Boids
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


boids = Boids(100, domain=(10.0, 10.0, 10.0), initial_speed=0.10)
simulation = boids.simulate()

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.set(xlim=(0, 10), ylim=(0, 10), zlim=(0, 10))
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

arrows = None


def update(_):
    global arrows

    state = next(simulation)

    positions = [boid.position for boid in state]
    velocities = [boid.velocity for boid in state]

    positions = list(zip(*positions))
    velocities = list(zip(*velocities))

    if arrows is not None:
        arrows.remove()

    arrows = ax.quiver(
        *positions,
        *velocities,
        length=0.5,
        normalize=True,
        color="tab:blue",
        arrow_length_ratio=0.3,
    )

    return (arrows,)


animation = FuncAnimation(
    fig,
    update,
    interval=30,
    blit=False,
)

plt.show()
