from room import Room
from database import Database


class Hotel:
    """ This class use for manage data about check in and check out

    Attributes
    ----------
    all_room: list
        Room and customer name
    database: class
        Database's class

    Methods
    -------
    make_room():
        Create room number and calculate room price in each floor.
    check_in(room, name, money):
        Record customer name and money to csv file.
    check_out(room, name):
        Delete customer from csv file.
    update_room():
        Relate with load_data from Database's class for update
        customer name in all_room (list).
    """
    def __init__(self) -> None:
        """ Initialize list of object and database for the program. """
        self.all_room = []
        self.database = Database()
        self.make_room()
        self.update_room()

    def make_room(self):
        """ Create room number and calculate room price in each floor. """
        for floor_num in range(1, 6):
            price = int(1500 + (floor_num-1)*200)
            for room_alp in "ABCDEFGHIJ":
                self.all_room.append(Room(str(floor_num) + room_alp, None, price))

    def check_in(self, room, name, money):
        """ Record customer name and money to csv file.

        :param room: Room number.
        :type room: str
        :param name: Name of customer.
        :type name: str
        :param money: Price of each room,
        :type money: int
        """
        for r in self.all_room:
            if r.room_name == room:
                if r.name:
                    print("This room reserved.")
                elif r.money > money:
                    print("You don't have enough money.")
                    print(f"{name} can't check in.")
                else:
                    r.name = name
                    self.database.check_in(room, name, money)
                    print(f"The room {room} have check in by {name}.")
                break
        else:
            print("We don't have this room.")

    def check_out(self, room, name):
        """ Delete customer from csv file.

        :param room: Room number.
        :type room: str
        :param name: Name of customer.
        :type name: str
        """
        for r in self.all_room:
            if r.room_name == room:
                if r.name != name:
                    print(f"{name} can't check out.")
                else:
                    r.name = None
                    self.database.check_out(room)
                    print(f"The room {room} have check out by {name}")
                    break
        else:
            print(f"{name} didn't reserve this room.")
    
    def update_room(self):
        """
        Relate with load_data from Database's class for update
        customer name in all_room (list of  object).
        """
        for r in self.database.load_data():
            for room in self.all_room:
                if r["room"] == room.room_name:
                    room.name = r["name"]
