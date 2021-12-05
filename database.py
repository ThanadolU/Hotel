import csv


class Database:
    """ This class used to read and write a file as a csv file in order to
    access data from hotel.

    Methods
    -------
    check_in(room, name, money):
        Check in new customer to the database.
    check_valid_room(room, name, money, hotel):
        Check valid room by using room data from hotel.
    check_out(room):
        Check out customer by delete name.
    load_data():
        Load data from csv file.
    """
    @staticmethod
    def check_in(room, name, money):
        """ Check in new customer to the database by using
        'Customer' as '.csv' file.

        :param room: number of room
        :type room: str
        :param name: name of customer
        :type name: str
        :param money: price of each room
        :type money: int
        """
        new_data = {"room": room, "name": name, "money": money}

        try:
            customer_data = []
            with open("Customer.csv", "r") as f:
                rows = csv.DictReader(f)
                for r in rows:
                    customer_data.append(r)

        except FileNotFoundError:
            with open("Customer.csv", "w") as f:
                writer = csv.DictWriter(f, fieldnames=['room', 'name', 'money'])
                writer.writeheader()
                writer.writerow(new_data)

        else:
            for row in customer_data:
                if row["room"] == new_data["room"]:
                    row["room"] = new_data["room"]
                    break
            else:
                customer_data.append(new_data)

            with open("Customer.csv", "w") as f:
                writer = csv.DictWriter(f, fieldnames=['room', 'name', 'money'])
                writer.writeheader()
                for row in customer_data:
                    writer.writerow(row)

    def check_valid_room(self, room, name, money, hotel):
        """ Check valid room by using room data from hotel(hotel.all_room).

        :param room: number of room
        :type room: str
        :param name: name of customer
        :type name: str
        :param money: price of each room
        :type money: int
        :param hotel: hotel object
        :type hotel: class
        """
        for num_room in hotel.all_room:
            if room == num_room.room_name:
                self.check_in(room, name, money)
                break
        else:
            print("We don't have this room.")

    @staticmethod
    def check_out(room):
        """ Check out customer by delete name.

        :param room: number of room
        :type room: str
        """
        try:
            customer_data = []
            with open("Customer.csv", "r") as f:
                rows = csv.DictReader(f)
                for r in rows:
                    customer_data.append(r)

            for i, row in enumerate(customer_data):
                if row["room"] == room:
                    del customer_data[i]
                    break
            else:
                print(f'No have room {room}')

        except FileNotFoundError:
            print("File not found")

        else:
            with open("Customer.csv", "w") as f:
                writer = csv.DictWriter(f, fieldnames=['room', 'name', 'money'])
                writer.writeheader()
                for row in customer_data:
                    writer.writerow(row)

    @staticmethod
    def load_data():
        """ Load data from csv file (It's related to graphic.).

        :return: list of dict ---> ex. [{'room': '2A', 'name': 'Dol', 'money': '1700'}]
        :rtype: list
        """
        try:
            customer_data = []
            with open("Customer.csv", "r") as f:
                rows = csv.DictReader(f)
                for r in rows:
                    customer_data.append(r)
        except FileNotFoundError:
            with open("Customer.csv", "w") as f:
                writer = csv.DictWriter(f, fieldnames=['room', 'name', 'money'])
                writer.writeheader()
        return customer_data
