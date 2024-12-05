from compas.tolerance import TOL
from my_library import ShapeManager


def test_shape_manager_total_volume():
    sm = ShapeManager()
    sm.add_sphere([0, 0, 0], 1.0)
    sm.add_box([0, 0, 0], 1.0, 1.0, 1.0)

    assert TOL.is_close(sm.total_volume(), 4.1887902047863905 + 1.0)


def test_shape_manager_largest_shape():
    sm = ShapeManager()
    sm.add_sphere([0, 0, 0], 1.0)
    sm.add_box([0, 0, 0], 1.0, 1.0, 1.0)

    assert sm.largest_shape().name == "Sphere"
