import unittest


class Rover:

    """
    Вас приветствует система управления марсоходом.
    Наш марсоход умеет:
    move() -  команда марсоходу двигаться
    В качестве аргумента передается направление движения:
    "forward" - вперед, "backward" - назад, "left" - налево, "right" - направо
    get_coordinates() - получение текущих координат в формате (x,y)
    get_camera_position()- сторона света, на которую смотрит ровер (North, West, East, South)
    greetings_for_human() - полноценное приветствие со всей информацией

    """

    # right_rotations и left_rotations показывают закономерности поворота ровера
    # в зависимости от изначального положения камеры
    def __init__(self, x: int = 0, y: int = 0, camera_position: str = "North"):
        self.x = x
        self.y = y
        self.right_rotations = {
            "North": "East",
            "West": "North",
            "East": "South",
            "South": "West"
        }

        self.left_rotations = {
            "North": "West",
            "West": "South",
            "South": "East",
            "East": "North"
        }

        self.commands = ['forward', 'backward', 'right', 'left']
        if camera_position in self.right_rotations.keys():
            self.camera_position = camera_position
        else:
            raise ValueError(f"Please, choose correct position from this list:{self.right_rotations.keys()}")

    # логика поворотов
    def turn_left(self):
        new_camera_position = self.left_rotations[self.camera_position]
        self.camera_position = new_camera_position

    def turn_right(self):
        new_camera_position = self.right_rotations[self.camera_position]
        self.camera_position = new_camera_position

    # логика смены координат сделана с расчетом на четыре координатные четверти,
    # поэтому координаты могут быть отрицательными
    def change_coordinates(self):
        if self.camera_position == "North":
            if self.x >= 0:
                self.x += 1
            else:
                self.x -= 1
        elif self.camera_position == "South":
            if self.x >= 0:
                self.x -= 1
            else:
                self.x += 1
        elif self.camera_position == "East":
            if self.y >= 0:
                self.y += 1
            else:
                self.y -= 1
        elif self.camera_position == "West":
            if self.y >= 0:
                self.y -= 1
            else:
                self.y += 1

    # логика движения ровера
    def move(self, direction: str):
        if direction in self.commands:
            if direction.lower() == "right":
                self.turn_right()
            elif direction.lower() == "left":
                self.turn_left()
            self.change_coordinates()
        else:
            raise ValueError(
                f"Please, choose correct direction from this list: {self.commands}")

    # логика получения всякой информации
    def get_coordinates(self):
        return (self.x, self.y)

    def get_camera_position(self):
        return self.camera_position

    def greetings_for_human(self):
        print(f""" 
Greetings from Mars, human! I'm a humble rover WALL-E 3000!
My coordinates: x = {self.x}, y = {self.y}.
Now my camera direct at {self.camera_position}.
Somebody, please, take me home...
        """)


class RoverTestCase(unittest.TestCase):

    def setUp(self):
        self.walle = Rover(0, 0, "North")

    def test_move(self):
        self.walle.move("forward")
        self.assertEqual(self.walle.get_coordinates(), (1, 0))
        self.assertEqual(self.walle.get_camera_position(), "North")
        self.walle.move("left")
        self.assertEqual(self.walle.get_coordinates(), (1, -1))
        self.assertEqual(self.walle.get_camera_position(), "West")
        self.walle.move("backward")
        self.assertEqual(self.walle.get_coordinates(), (1, 0))
        self.assertEqual(self.walle.get_camera_position(), "West")
        self.walle.move("right")
        self.assertEqual(self.walle.get_coordinates(), (2, 0))
        self.assertEqual(self.walle.get_camera_position(), "North")


if __name__ == "__main__":
    unittest.main()


# walle = Rover()
# walle.get_info()
# walle.move("left")
# walle.get_info()
# walle.move("left")
# walle.get_info()
# walle.move("forward")
# walle.get_info()
# walle.move("backward")
# walle.get_info()
