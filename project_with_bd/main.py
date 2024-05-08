from view.MainWindow import MainWindow as Wn
import sqlite3

connection = sqlite3.connect('database.db')

if __name__ == '__main__':
    window = Wn(connection=connection)
    window.mainloop()

connection.close()
