from dataclasses import dataclass


@dataclass
class Car:
    id: int | None
    model: str
    price: int
    mileage: int

    @staticmethod
    def of(data: tuple):
        return Car(data[0], data[1], data[2], data[3])

    def to_data(self):
        return self.model, self.price, self.mileage

    def get(self):
        return (str(self.id), self.model,
                str(self.price), str(self.mileage))
