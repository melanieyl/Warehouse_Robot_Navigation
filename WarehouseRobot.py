from dataclasses import dataclass
from enum import Enum
from typing import List, Set, Tuple

class Direction(Enum):
    N = (0, 1) 
    E = (1, 0)
    S = (0, -1)
    W = (-1, 0)

    @staticmethod
    def rotate_left(direction):
        directions = [Direction.N, Direction.W, Direction.S, Direction.E]
        return directions[(directions.index(direction) + 1) % 4]

    @staticmethod
    def rotate_right(direction):
        directions = [Direction.N, Direction.E, Direction.S, Direction.W]
        return directions[(directions.index(direction) + 1) % 4]

@dataclass
class Warehouse:
    width: int
    height: int
    shelves: Set[Tuple[int, int]] ## estanterias
    pickup_zones: Set[Tuple[int, int]]
    dropoff_zones: Set[Tuple[int, int]]

    ## rules move
    def is_valid_move(self, x: int, y: int) -> bool:
        return (0 <= x <= self.width and 0 <= y <= self.height and (x, y) not in self.shelves)


@dataclass
class Robot:
    x: int
    y: int
    direction: Direction
    warehouse: Warehouse
    commands: str  ##PMMMMMMMRMMMMMMMD
    carrying: bool = False   # not package

    def move_forward(self):
        dx, dy = self.direction.value
        new_x, new_y = self.x + dx, self.y + dy

        if self.warehouse.is_valid_move(new_x, new_y):
            self.x, self.y = new_x, new_y

    def pick_up(self):
        if (self.x, self.y) in self.warehouse.pickup_zones and not self.carrying:
            self.carrying = True # with package

    def drop_off(self):
        if (self.x, self.y) in self.warehouse.dropoff_zones and self.carrying:
            self.carrying = False

    def execute_commands(self):
        actions = {
            'L': lambda: setattr(self, 'direction', Direction.rotate_left(self.direction)),
            'R': lambda: setattr(self, 'direction', Direction.rotate_right(self.direction)),
            'M': self.move_forward,
            'P': self.pick_up,
            'D': self.drop_off
        }
        for command in self.commands:
            if command in actions:
                actions[command]()

    def __str__(self):
        return f"{self.x} {self.y} {self.direction.name} {'CARRYING' if self.carrying else 'EMPTY'}"



@dataclass
class Simulator:
    warehouse: Warehouse
    robots: List[Robot]

    def run(self) -> List[str]:
        results = []
        for robot in self.robots:
            robot.execute_commands()  
            results.append(str(robot))
        return results


def parse_input(input_data: str) -> Simulator:
    lines = input_data.strip().split("\n")
    width, height = map(int, lines[0].split())

    index = 1
    num_shelves = int(lines[index])
    shelves = {tuple(map(int, lines[i].split())) for i in range(index + 1, index + 1 + num_shelves)}
    index += 1 + num_shelves

    num_pickups = int(lines[index])
    pickup_zones = {tuple(map(int, lines[i].split())) for i in range(index + 1, index + 1 + num_pickups)}
    index += 1 + num_pickups

    num_dropoffs = int(lines[index])
    dropoff_zones = {tuple(map(int, lines[i].split())) for i in range(index + 1, index + 1 + num_dropoffs)}
    index += 1 + num_dropoffs

    warehouse = Warehouse(width, height, shelves, pickup_zones, dropoff_zones)

    num_robots = int(lines[index])
    index += 1
    robots = []
    for _ in range(num_robots):
        x, y, direction = lines[index].split()
        commands = lines[index + 1]
        robots.append(Robot(int(x), int(y), Direction[direction], warehouse, commands=commands))
        index += 2

    return Simulator(warehouse, robots)

# Example input
input_data = """7 7
2
3 3
3 4
1
0 0
1
7 7
1
0 0 N
PMMMMMMMRMMMMMMMD"""

simulator = parse_input(input_data)
output = simulator.run()
for line in output:
    print(line)
