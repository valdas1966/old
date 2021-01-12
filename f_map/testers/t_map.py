from f_utils import u_tester
from f_grid import u_grid
from f_map.c_map import Map
from f_map.c_point import Point
from f_const.directions import Directions


class TestMap:

    def __init__(self):
        u_tester.print_start(__file__)
        TestMap.__tester_rows_cols()
        TestMap.__tester_shape()
        TestMap.__tester_set_value()
        TestMap.__tester_offsets()
        TestMap.__tester_dict_f()
        TestMap.__tester_to_point()
        TestMap.__tester_nearest()
        #TestMap.__tester_nearest_closed()
        TestMap.__tester_zfill()
        TestMap.__tester_neighbors()
        TestMap.__tester_eq()
        u_tester.print_finish(__file__)

    @staticmethod
    def __tester_rows_cols():
        map = Map(rows=2, cols=3)
        p0 = map.rows == 2
        p1 = map.cols == 3
        u_tester.run(p0, p1)

    @staticmethod
    def __tester_shape():
        map = Map(rows=2, cols=3)
        p0 = map.shape == (2, 3)
        u_tester.run(p0)

    @staticmethod
    def __tester_set_value():
        map = Map(rows=3)
        map.set_value(value=2, point=Point(1, 1))
        p0 = map.grid[1][1] == 2
        map.set_value(value=3, row=1, col=1)
        p1 = map.grid[1][1] = 3
        u_tester.run(p0, p1)

    @staticmethod
    def __tester_offsets():
        map = Map(rows=5)
        # Offsets from Axises
        p0 = map.offsets(0) == (0, 4, 4, 0)
        p1 = map.offsets(1) == (0, 3, 4, 1)
        p2 = map.offsets(7) == (1, 2, 3, 2)
        # Offsets from other Node
        p3 = map.offsets(0, 0) == (0, 0)
        p4 = map.offsets(0, 1) == (0, -1)
        p5 = map.offsets(1, 0) == (0, 1)
        p6 = map.offsets(6, 5) == (0, 1)
        p7 = map.offsets(7, 1) == (1, 1)
        p8 = map.offsets(8, 3) == (1, 0)
        p9 = map.offsets(1, 24) == (-4, -3)
        u_tester.run(p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @staticmethod
    def __tester_dict_f():
        map = Map(rows=3)
        start = 6
        goal = 8
        map.grid[1][1] = -1
        map.grid[2][1] = -1
        dict_f = map.dict_f(start, goal)
        dict_f_true = {0: 6, 1: 6, 2: 6, 3: 4, 5: 6, 6: 2, 8: 6}
        p0 = dict_f == dict_f_true
        u_tester.run(p0)

    @staticmethod
    def __tester_to_point():
        map = Map(rows=3)
        point_test = map.to_point(0)
        point_true = Point(2, 0)
        p0 = point_test == point_true
        point_test = map.to_point(8)
        point_true = Point(0, 2)
        p1 = point_test == point_true
        u_tester.run(p0, p1)

    @staticmethod
    def __tester_nearest():
        map = Map(rows=3)
        start = 0
        goal_1 = 2
        goal_2 = 3
        p0 = map.nearest(start, [goal_1, goal_2]) == 3
        goal_2 = 6
        p1 = map.nearest(start, [goal_1, goal_2]) == 2
        u_tester.run(p0,p1)

    @staticmethod
    def __tester_nearest_closed():
        map = Map(rows=5)
        start = 12
        closed = {6, 17}
        nearest_test = map.nearest_closed(start, closed)
        nearest_true = {Directions.UP: 2,
                        Directions.RIGHT: float('Infinity'),
                        Directions.DOWN: 1,
                        Directions.LEFT: 2}
        p0 = nearest_test == nearest_true
        print(nearest_test)
        u_tester.run(p0)

    @staticmethod
    def __tester_zfill():
        map = Map(rows=3, cols=4)
        map.grid[1][1] = -1
        map.zfill()
        li_1 = [0, 0, 0, 0]
        li_2 = [0, -1, 0, 0]
        li_3 = [0, 0, 0, 0]
        li = [li_1, li_2, li_3]
        grid_true = u_grid.lists_to_grid(li)
        p0 = (map.grid == grid_true).all()
        u_tester.run(p0)

    @staticmethod
    def __tester_neighbors():
        map = Map(rows=5)
        map.set_block(row=1, col=1)
        # Top Left
        neighbors_test = map.neighbors(Point(0, 0))
        neighbors_true = [Point(0, 1), Point(1, 0)]
        p0 = neighbors_test == neighbors_true
        # Top Right
        neighbors_test = map.neighbors(Point(1, 4))
        neighbors_true = [Point(0, 4), Point(1, 3), Point(2, 4)]
        p1 = neighbors_test == neighbors_true
        # Bottom Left
        neighbors_test = map.neighbors(Point(4, 0))
        neighbors_true = [Point(3, 0), Point(4, 1)]
        p2 = neighbors_test == neighbors_true
        # Bottom Right
        neighbors_test = map.neighbors(Point(4, 4))
        neighbors_true = [Point(3, 4), Point(4, 3)]
        p3 = neighbors_test == neighbors_true
        # Block
        neighbors_test = map.neighbors(Point(0, 1))
        neighbors_true = [Point(0, 0), Point(0, 2)]
        p4 = neighbors_test == neighbors_true
        # Free
        neighbors_test = map.neighbors(Point(3, 3))
        neighbors_true = [Point(2, 3), Point(3, 2), Point(3, 4), Point(4, 3)]
        p5 = neighbors_test == neighbors_true
        u_tester.run(p0, p1, p2, p3, p4, p5)

    @staticmethod
    def __tester_eq():
        map_1 = Map(rows=3)
        map_2 = Map(rows=3)
        p0 = map_1 == map_2
        map_2.grid[1][1] = -1
        p1 = map_1 != map_2
        u_tester.run(p0, p1)


if __name__ == '__main__':
    TestMap()
