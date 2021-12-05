from screen import Screen
from hotel import Hotel
from rich import print as printcolor


sc = Screen()
ht = Hotel()


while True:
    printcolor("[#FFD43B]1. Check in room.[/#FFD43B]")
    printcolor("[#FFD43B]2. Check out room.[/#FFD43B]")
    printcolor("[#FFD43B]3. Exit program.[/#FFD43B]")
    sc.show_all_room(ht.all_room)
    choice = int(input("Choose your choice: "))
    if choice == 1:
        printcolor("[#98F5FF]Please enter your room: [/#98F5FF]", end="")
        room = input()
        printcolor("[#FF8C00]Please enter your name: [/#FF8C00]", end="")
        name = input()
        printcolor("[#BCEE68]Please enter your money: [/#BCEE68]", end="")
        money = int(input())
        ht.check_in(room, name, money)
    elif choice == 2:
        printcolor("[#98F5FF]Please enter your room: [/#98F5FF]", end="")
        room = input()
        printcolor("[#FF8C00]Please enter your name: [/#FF8C00]", end="")
        name = input()
        ht.check_out(room, name)
    elif choice == 3:
        printcolor("[red]Exit from program.[/red]")
        exit()
    print()
