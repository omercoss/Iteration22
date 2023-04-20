from PyQt6.QtWidgets import QApplication
from gui.multielectronicjournal1 import startSide

if __name__ == "__main__":
    app = QApplication([])
    start_side = startSide
    start_side.show()
    app.exec()

