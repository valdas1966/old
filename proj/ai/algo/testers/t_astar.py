from f_utils import u_tester
from f_utils import u_random
from proj.ai.model.point import Point
from proj.ai.model.grid_blocks import GridBlocks
from proj.ai.algo.astar import AStar
from proj.ai.logic.grid_blocks_ghf import LogicGridBlocksGHF


class TestAlgoAStar:

    def __init__(self):
        u_tester.print_start(__file__)
        TestAlgoAStar.__tester_run_manual()
        TestAlgoAStar.__tester_run_random()
        TestAlgoAStar.__tester_random_blocks()
        u_tester.print_finish(__file__)

    @staticmethod
    def __tester_run_manual():
        grid = GridBlocks(rows=4)
        # Perfect Heuristic (without blocks)
        start = Point(0, 0)
        goal = Point(3, 3)
        astar = AStar(grid, start, goal)
        astar.run()
        optimal_path_test = astar.optimal_path()
        optimal_path_true = [Point(0, 0), Point(0, 1), Point(0, 2),
                             Point(0, 3), Point(1, 3), Point(2, 3),
                             Point(3, 3)]
        p0 = optimal_path_test == optimal_path_true
        closed_test = astar.closed
        closed_true = set(optimal_path_true)
        p1 = closed_test == closed_true
        # Not-Perfect Heuristic (with blocks)
        grid.set_block(x=1, y=2)
        grid.set_block(x=1, y=3)
        astar = AStar(grid, start, goal)
        astar.run()
        optimal_path_test = astar.optimal_path()
        optimal_path_true = [Point(0, 0), Point(0, 1), Point(1, 1),
                             Point(2, 1), Point(2, 2), Point(2, 3),
                             Point(3, 3)]
        p2 = optimal_path_test == optimal_path_true
        closed_test = astar.closed
        closed_true = set(optimal_path_true).union({Point(0, 2), Point(0, 3)})
        p3 = closed_test == closed_true
        u_tester.run(p0, p1, p2, p3)

    @staticmethod
    def __tester_run_random():
        p0 = True
        p1 = True
        for i in range(1000):
            n = u_random.get_random_int(3, 10)
            grid = GridBlocks(rows=n)
            start, goal = grid.points_random(2)
            astar = AStar(grid, start, goal)
            astar.run()
            p0 = len(astar.optimal_path()) == len(astar.closed)
            p1 = len(astar.optimal_path()) == start.distance(goal)+1
            if not p0 or not p1:
                break
        u_tester.run(p0, p1)

    @staticmethod
    def __tester_random_blocks():
        p0 = True
        for i in range(1000):
            n = u_random.get_random_int(3, 10)
            b = u_random.get_random_int(10, 50)
            grid = GridBlocks(rows=n, percent_blocks=b)
            start, goal = grid.points_random(2)
            astar = AStar(grid, start, goal)
            astar.run()
            if not astar.is_found:
                continue
            nodes_f = LogicGridBlocksGHF.to_nodes_below_f(grid, start, goal)
            p0 = nodes_f.issubset(astar.closed)
            if not p0:
                break
        u_tester.run(p0)


if __name__ == '__main__':
    TestAlgoAStar()
