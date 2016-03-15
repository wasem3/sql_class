import sys
import random

NAMES = ['Alice', 'Bob', 'Carol', 'Dave', 'Emily', 'Frank', 'Gina']
PRODUCTS = ['Apple', 'Orange', 'Banana', 'Blueberry', 'Raspberry', 'Apricot', 'Cherry', 'Grape', 'Mango']
ACTIONS = ['addtocart', 'purchase', 'view']

def generate(N, fn):
    with open(fn, 'w') as f:
        for i in xrange(N):
            name = random.choice(NAMES)
            product = random.choice(PRODUCTS)
            action = random.choice(ACTIONS)
            price = str(0.99)

            f.write("%s,%s,%s,%s\n" % (name, product, action, price))


if __name__ == '__main__':
    generate(int(sys.argv[1]), sys.argv[2])
