import database.data.db_functions as db
from database.data.models import Car


class CarDataLogic:
    @staticmethod
    def get_all(connection) -> list[Car]:
        return db.get_all(connection)

    @staticmethod
    def get_by_id(connection, car_id: int) -> Car:
        cars = CarDataLogic.get_all(connection)
        for car in cars:
            if car.id == car_id:
                return car

        return None

    @staticmethod
    def insert(connection, car: Car) -> bool:
        if car.mileage < 0 or car.price < 0:
            return False

        if car is None:
            return False
        return db.insert(connection, car)

    @staticmethod
    def delete_all(connection) -> bool:
        return db.delete_all(connection)

    @staticmethod
    def delete_by_id(connection, car_id: int):
        if car_id < 0:
            return False
        return db.delete_by_id(connection, car_id)

    @staticmethod
    def get_by_model(connection, model: str) -> list[Car]:
        if len(model) == 0:
            return []

        cars = db.get_all(connection)

        if model[:3] == 'id:':
            return list(
                filter(
                    lambda x: int(model[3]) == x.id,
                    cars
                )
            )

        return list(
            filter(
                lambda x: model.lower() in x.model.lower(),
                cars
            )
        )
