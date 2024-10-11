from ui import UI
from logic import *
from file_manager import *

def main():
    admin=Admin()
    customer=Customer()
    menu=MenuManager()
    menu.read_menu()

    ui=UI(menu,customer,admin)
    ui.run()

if __name__=="__main__":
    main()
