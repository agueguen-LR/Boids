from collections.abc import Sequence
from typing import Iterator, overload
from scipy.spatial import KDTree
import numpy as np

from boids.BoidView import BoidView


class Boids(Sequence[BoidView]):
    def __init__(
        self,
        amount: int,
        *,
        domain: tuple[float, float, float] = (1.0, 1.0, 1.0),
        initial_speed: float = 1.0,
        periodic: bool = True,
    ) -> None:

        if amount < 0:
            raise ValueError(
                f"Amount of boids in simulation cannot be negative: {amount}"
            )

        if any(val <= 0 for val in domain):
            raise ValueError(f"Domain size must be > 0, is: {domain}")

        self._amount = amount
        self._domain = domain
        self._v0 = initial_speed

        # Generate positions of boids uniformally within domain
        self._positions = np.random.uniform(
            low=0.0, high=self._domain, size=(amount, 3)
        )

        # Generate velocities in uniformally random directions with v0 initial speed
        phi = np.random.uniform(0.0, 2.0 * np.pi, self._amount)
        z = np.random.uniform(-1.0, 1.0, self._amount)
        r = np.sqrt(1.0 - z**2)
        self._velocities = (
            np.column_stack((r * np.cos(phi), r * np.sin(phi), z)) * self._v0
        )

        # Create a KDTree for efficient computation of distances between Boids
        self._tree = KDTree(self._positions, boxsize=self._domain if periodic else None)

    def __len__(self) -> int:
        return self._amount

    @overload
    def __getitem__(self, index: int) -> BoidView: ...
    @overload
    def __getitem__(self, index: slice) -> list[BoidView]: ...
    def __getitem__(self, index: int | slice) -> BoidView | list[BoidView]:
        if isinstance(index, slice):
            return [self[i] for i in range(*index.indices(self._amount))]

        return BoidView(
            index,
            self._positions[index],
            self._velocities[index],
        )

    def __uniform_generator(self) -> Iterator[np.ndarray]:
        while True:
            yield np.random.uniform(low=0.0, high=self._domain, size=3)
