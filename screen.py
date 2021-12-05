import turtle
from time import sleep
from hotel import Hotel


class Screen:
    """ This class use for print out all graphical output for the program.

    Attributes
    ----------
    screen: Screen()
        Use as screen for the graphic.
    painter: Turtle()
        Use as painter for the graphic.

    Methods
    -------
    create_room():
        Draw a line in x and y - axis for create all room.
    report_available_room(all_room):
        Report the number of available rooms to user.
    show_room_price():
        Report room price in each floors.
    find_x_y(room_name):
        Find the center of each room.
    show_all_room(all_room):
        Display all room in hotel (including reserved room.).
    reset():
        Reset(clear) and create room again (for show all room that reserved)
    """

    def __init__(self) -> None:
        """ Initialize a graphical for the program. """
        self.screen = turtle.Screen()
        self.painter = turtle.Turtle()

    def create_room(self):
        """
        Draw a line in x and y - axis for create all room.
        """
        self.screen.title("Hotel")
        self.screen.screensize(300, 300)
        self.screen.bgcolor("#EAEAEA")
        self.painter.pencolor("#848484")
        self.painter.hideturtle()
        self.painter.speed(0)

        # Draw a line in x - axis.
        now_x, now_y = -280, 260
        self.painter.pensize(5)
        self.painter.penup()
        for _ in range(6):
            self.painter.goto(now_x, now_y)
            self.painter.pendown()
            self.painter.goto(now_x + 600, now_y)
            now_y -= 60
            self.painter.penup()

        # Draw a line in y - axis.
        now_x, now_y = -280, 260
        for _ in range(11):
            self.painter.goto(now_x, now_y)
            self.painter.pendown()
            self.painter.goto(now_x, now_y - 300)
            now_x += 60
            self.painter.penup()

        # Determine number of each floor
        now_x, now_y = -300, 210
        self.painter.goto(now_x, now_y)
        for i in range(5, 0, -1):
            self.painter.color("#006494")
            self.painter.write(i, False, 'right', font=('Menlo', 30, ''))
            now_y -= 60
            self.painter.goto(now_x, now_y)

        # Determine last character of room in each floor.
        now_x, now_y = -250, 270
        self.painter.goto(now_x, now_y)
        for i in range(10):
            char = 65 + i
            self.painter.color("#FE5F55")
            self.painter.write(chr(char), False, "center", font=('Menlo', 30, ''))
            now_x += 60
            self.painter.goto(now_x, now_y)

    def report_available_room(self, all_room):
        """ Report the number of available rooms to user.

        :param all_room: list of object
        :type all_room: list
        """
        now_x1, now_y1 = 20, -90
        now_x2, now_y2 = 23, -340
        self.painter.color("#118AB2")
        self.painter.goto(now_x1, now_y1)
        self.painter.write("These are all rooms in my hotel.", False, "center", font=('Consolas', 20, ''))
        count = len(all_room) - sum(i.name is not None for i in all_room)
        self.painter.goto(now_x2, now_y2)
        self.painter.write(f"We have [{count}] available room.", False, "center", font=('Consolas', 20, ''))

    def show_room_price(self):
        """
        Report room price in each floors.
        """
        now_x, now_y = 20, -90
        for floor_num in range(1, 6):
            now_y -= 40
            price = int(1500 + (floor_num - 1) * 200)
            self.painter.color("#C67171")
            self.painter.goto(now_x, now_y)
            self.painter.write(f"Floor {floor_num}, Room Price: {price} Baht.", False, "center",
                               font=('Consolas', 20, ''))

    @staticmethod
    def find_x_y(room_name):
        """ This function use for find a center of room

        :param room_name: number of each room
        :type room_name: str
        :return: coordinates of x and y
        :rtype: int
        """
        num, alp = room_name
        start_cor_x = -250
        start_cor_y = -10
        cor_x = start_cor_x + ((ord(alp) - 64) - 1) * 60
        cor_y = start_cor_y + (int(num) - 1) * 60
        return cor_x, cor_y

    def show_all_room(self, all_room):
        """ Display all room in hotel (including reserved room.).

        :param all_room: list of object
        :return: list
        """
        self.reset()
        self.report_available_room(all_room)
        self.show_room_price()
        for i in all_room:
            x, y = self.find_x_y(i.room_name)
            if i.name is not None:
                self.painter.color("red")
                self.painter.goto(x, y - 15)
                self.painter.write("❌", False, "center", font=('Arial', 20, ''))

    def reset(self):
        """ Reset(clear) and create room again (for show all room that reserved). """
        self.painter.clear()
        self.create_room()


if __name__ == "__main__":
    screen = Screen()
    hotel = Hotel()
    screen.show_all_room(hotel.all_room)
    sleep(5)
