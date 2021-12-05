class Room:
    """ This class use for represent room number and name

    Attributes
    ----------
    room_name: str
        Room number
    name: str
        Customer name
    money: int
        Room price
    """
    def __init__(self, room_name, name, money) -> None:
        """ Initialize new customer data.

        :param room_name: Room number
        :type room_name: str
        :param name: Customer name
        :type name: str
        :param money: Room price
        :type money: int
        """
        self.room_name = room_name
        self.name = name
        self.money = money

    def __repr__(self) -> str:
        """  Represent room number and customer name.

        :return: Represent string of room number and customer name.
        :rtype: str
        """
        return f"Room: {self.room_name} Name: {self.name}"
