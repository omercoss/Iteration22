from PyQt6.QtWidgets import QApplication
from gui.multielectronicjournalstart1 import StartSide

if __name__ == "__main__":
    app = QApplication([])
    start_side = StartSide
    start_side.show()
    app.exec()

