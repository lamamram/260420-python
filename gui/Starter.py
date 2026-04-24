import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from Ui_MainWindow import Ui_MainWindow
from text_analyser.word_counter import Counter
from PySide6.QtCore import Slot

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        self.resize(600, 400)
        
        # chargement du layoit
        self.setupUi(self)
        # branchage des évènements (click, onmouseon, ...)
        self.okBtn.clicked.connect(self.on_okBtn_clicked)


    # décorateur: objet avancé en python
    @Slot()
    def on_okBtn_clicked(self):
        #1. récupération du texte du TextEdit
        #2. instancier et exécuter le Counter
        #3. décharger le dictionnaire d'occurences dans ListWidget
        occurences = Counter(self.textEdit.toPlainText()).analyze()
        for word, occ in occurences.items():
            self.listWidget.addItem(f"{word}: {occ}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
