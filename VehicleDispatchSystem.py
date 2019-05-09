
import pprint
graph = {
    'a': {'b': 1, 'c':  4},
    'b': {'c':  3, 'd':  2, 'e':  2},
    'c': {},
    'd': {'b':  1, 'c':  5},
    'e': {'d': -2}
}
pprint.pprint(graph)
