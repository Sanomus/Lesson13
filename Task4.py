class Robot:
    def __init__(self, orientation: list, position: list):
        self.orientation = orientation #[False,True,False,False]
        self.position = position

    @classmethod
    def create_robot(cls, orientation=[False, True, False, False], position=[0, 0]):
        instance = cls(orientation, position)
        return instance

    def move(self, steps: int):
        if self.orientation == [True, False, False, False]:
            self.position[0] -= 1*steps
        elif self.orientation == [False, True, False, False]:
            self.position[1] += 1*steps
        elif self.orientation == [False, False, True, False]:
            self.position[0] += 1*steps
        elif self.orientation == [False, False, False, True]:
            self.position[1] += 1*steps
        return self.position
    
    def turn(self, direction: str):
        if direction == 'left':
            self.orientation = self.orientation[1:]+self.orientation[:1]
        if direction == 'right':
            self.orientation = self.orientation[3:]+self.orientation[:3]
        return self.orientation

    def display_position(self):
        return print(f'Robot position: {self.position}')


robot = Robot.create_robot()


robot.move(1)
robot.turn('left')
robot.move(2)
robot.display_position()
