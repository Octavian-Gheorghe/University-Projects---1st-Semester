from Repository_Class import MemoryRepository
from TextRepository_Class import TextRepository
from BinaryRepository_Class import BinaryRepository
from Service_Class import Service
from UI_Class import UI

print("1. Memory Repository")
print("2. Text Repository")
print("3. Binary Repository")
choice = int(input("Choose which type of repository you choose: "))
if choice == 1:
    repo = MemoryRepository()
elif choice == 2:
    repo = TextRepository()
elif choice == 3:
    repo = BinaryRepository()
serv = Service(repo)
ui = UI(serv)
ui.run()