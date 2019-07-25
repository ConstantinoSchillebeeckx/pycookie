#!/usr/bin/env python3

def some_func():

    # load data into list of namedtuples
    f = csv.reader(open('some_file.csv'))
    h = next(f)
    obj = namedtuple("obj", h)

    schema = [str, float, float, float, float, str, float, float, str, float]

    T = []
    for row in f:
        row = [s(x) for s, x in zip(schema, row)]
        T.append(trip_tuple(*row))
