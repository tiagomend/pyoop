import math

def shape_density(thing, weight):
    return weight / call(thing, 'area')

def shape_new(name):
    return {
        'name': name,
        '_class': Shape
    }

Shape = {
    'density': shape_density,
    '_classname': 'Shape',
    '_parent': None,
    '_new': shape_new
}


# class Square
def square_perimeter(thing):
    return 4 * thing['side']

def square_area(thing):
    return thing['side'] ** 2

def square_larger(thing, size):
    return call(thing, 'area') > size

def square_new(name, side):
    return make(Shape, name) | {
        'side': side,
        '_class': Square
    }

Square = {
    'perimeter': square_perimeter,
    'area': square_area,
    'larger': square_larger,
    '_classname': 'Square',
    '_parent': Shape,
    '_new': square_new
}


# class Circle
def circle_perimeter(thing):
    return 2 * math.pi * thing['radius']

def circle_area(thing):
    return math.pi * thing['radius'] ** 2

def circle_larger(thing, size):
    return call(thing, 'area') > size

def circle_new(name, radius):
    return make(Shape, name) | {
        'radius': radius,
        '_class': Circle,
    }

Circle = {
    'perimeter': circle_perimeter,
    'area': circle_area,
    'larger': circle_larger,
    '_classname': 'Circle',
    '_parent': Shape,
    '_new': circle_new
}


def call(thing, method_name, *args):
    method = find(thing['_class'], method_name)
    return method(thing, *args)

def find(cls, method_name):
    while cls is not None:
        if method_name in cls:
            return cls[method_name]
        cls = cls['_parent']

    raise NotImplementedError('method_name')

def make(cls, *args):
    return cls['_new'](*args)

examples = [make(Square, 'sq', 3), make(Circle, 'ci', 2)]


def main():
    for ex in examples:
        n = ex["name"]
        d = call(ex, "density", 5)
        print(f"{n}: {d:.2f}")
