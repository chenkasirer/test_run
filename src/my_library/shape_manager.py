from typing import List
from compas.geometry import Sphere, Box, Vector, Point


class ShapeManager:
    def __init__(self):
        self.shapes = []

    def add_sphere(self, center: Point, radius: float):
        """Add a sphere to the collection.

        Parameters
        ----------
        center
        """
        sphere = Sphere(center, radius)
        self.shapes.append(sphere)

    def add_box(self, corner: Point, width: float, height: float, depth: float):
        """
        Add a box to the collection.
        """
        box = Box.from_corner_corner_height(
            corner, [corner[0] + width, corner[1] + height, corner[2]], depth
        )
        self.shapes.append(box)

    def total_volume(self):
        """
        Compute the total volume of all shapes.
        """
        # TODO: Implement this

    def largest_shape(self):
        """
        Find the shape with the largest volume.
        """
        # TODO: Implement this

    def move_shape(self, index, vector):
        """
        Move a shape by a given vector.
        """
        # TODO: Implement this
