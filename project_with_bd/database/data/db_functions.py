import sqlite3
from database.data import sql_scripts
from database.data.models.Car import Car


def get_all(connection: sqlite3.Connection) -> list[Car]:
    try:
        cursor = connection.cursor()
        cursor.execute(sql_scripts.car_sql_script_select_all)
        value: list[tuple] = cursor.fetchall()
        cars: list[Car] = []

        for data in value:
            car = Car.of(data)
            cars.append(car)

        return cars
    except Exception as e:
        print(e)
        return []


def insert(connection: sqlite3.Connection, car: Car) -> bool:
    try:
        cursor = connection.cursor()
        cursor.execute(sql_scripts.car_sql_script_insert, car.to_data())
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False


def delete_all(connection: sqlite3.Connection) -> bool:
    try:
        cursor = connection.cursor()
        cursor.execute(sql_scripts.car_sql_script_delete_all)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False


def delete_by_id(connection: sqlite3.Connection, car_id: int) -> bool:
    try:
        cursor = connection.cursor()
        cursor.execute(sql_scripts.car_sql_script_delete_by_id, (car_id,))
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
