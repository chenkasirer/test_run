from compas.geometry import Box


class MyClass:
    def __init__(self):
        self.box = Box(1.0)

    def my_method(self):
        return self.box.area

    def yet_another_method(self):
        return self.box.width

def my_function():
    return Box(1.0).area
