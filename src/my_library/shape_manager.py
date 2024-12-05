from typing import List
from compas.geometry import Sphere, Box, Vector, Point


class Shape_Manager:
    def __init__(self):
        self.SHAPES = []

    def add_sphere(self, center: Point, radius: float):
        """Add a sphere to the collection.

        Parameters
        ----------
        center : Point
            The center of the sphere.
        radius : float
            The radius of the sphere.

        """
        sphere = Sphere(center, radius)
        self.SHAPES.append(sphere)

    def add_box(self, corner: Point, width: float, height: float, depth: float):
        """Add a box to the collection."""
        box = Box.from_corner_corner_height(
            corner, [corner[0] + width, corner[1] + height, corner[2]], depth
        )
        self.SHAPES.append(box)

    def total_volume(self):
        """Compute the total volume of all shapes.
        
        Parameters:

        Returns:
            float: The total volume of all shapes.

        """
        # TODO: Implement this

    def largest_shape(self):
        # Find the shape with the largest volume.
        
        # TODO: Implement this

    def move_shape(self, index, vector):
        # TODO: Implement this
