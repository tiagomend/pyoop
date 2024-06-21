def square_perimeter(thing):
    return 4 * thing['side']

def square_area(thing):
    return thing['side'] ** 2

def square_new(name, side):
    return {
        "name": name,
        "side": side,
        "perimeter": square_perimeter,
        "area": square_area
    }


def call(thing, method_name):
    return thing[method_name](thing)

examples = [square_new('sq', 3)]

for ex in examples:
    n = ex['name']
    p = call(ex, 'perimeter')
    a = call(ex, 'area')
    print(f'{n} {p:.2f} {a:.2f}')

# Um método é uma função que recebe um objeto
# do tipo certo como seu primeiro parâmetro (self ou this)
