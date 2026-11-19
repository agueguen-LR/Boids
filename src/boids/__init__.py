from importlib.metadata import version

from .Boids import Boids
from .BoidView import BoidView

__all__ = ["Boids", "BoidView"]

__version__ = version("boids")
