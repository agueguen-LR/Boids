import numpy as np


class BoidView:
    """
    Read-only view of an individual boid in a Boids simulation.

    Provides access to a boid's identifier, position and velocity without
    copying the underlying numerical data.

    The position and velocity attributes are NumPy views referencing the
    original arrays owned by the Boids instance. They are marked as
    read-only to prevent accidental modification of the simulation state.

    Attributes
    ----------
    id : int
        Unique identifier of the boid.
    position : numpy.ndarray
        Read-only view of the boid's position (x, y, z).
    velocity : numpy.ndarray
        Read-only view of the boid's velocity (vx, vy, vz).

    Notes
    -----
    BoidView does not own the underlying position or velocity data.
    Changes made to the original arrays are reflected in this view.

    This class uses __slots__ to reduce per-instance memory overhead.
    """

    __slots__ = ("_id", "_position", "_velocity")

    def __init__(
        self,
        id: int,
        position: np.ndarray,
        velocity: np.ndarray,
    ) -> None:
        self._id = id

        self._position = position.view()
        self._position.flags.writeable = False

        self._velocity = velocity.view()
        self._velocity.flags.writeable = False

    @property
    def id(self) -> int:
        """Unique identifier of the boid."""
        return self._id

    @property
    def position(self) -> np.ndarray:
        """Read-only NumPy view of the boid's position (x, y, z)."""
        return self._position

    @property
    def velocity(self) -> np.ndarray:
        """Read-only NumPy view of the boid's velocity (vx, vy, vz)."""
        return self._velocity

    def __str__(self) -> str:
        """Return a human-readable representation of the boid."""
        return f"Boid {self.id}: position={self.position}, velocity={self.velocity}"

    def __repr__(self) -> str:
        """Return a concise, developer-oriented representation of the boid."""
        return f"(x,y,z={self.position}, v={self.velocity})"
