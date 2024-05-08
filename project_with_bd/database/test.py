from database.logic.car_data_logic import CarDataLogic
import sqlite3
import pprint

connection = sqlite3.connect('../database.db')

pprint.pprint(CarDataLogic.get_all(connection))
pprint.pprint(CarDataLogic.get_by_id(connection, 7))
pprint.pprint(CarDataLogic.get_by_model(connection, "Audi"))

connection.close()
