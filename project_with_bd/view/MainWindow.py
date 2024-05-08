import tkinter as tk
from idlelib.tooltip import Hovertip
from tkinter import messagebox
from database.data.models.Car import Car
from view.CreateWindow import CreateWindow
from view.MyComponents.CarView import CarView

from database.logic.car_data_logic import CarDataLogic


class MainWindow(tk.Tk):
    def __init__(self, connection, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connection = connection

        self.button_create = None
        self.listbox = None
        self.search = None
        self.search_button = None

        self.search_value = tk.StringVar(value="")

        self.title("My Application")
        self.resizable(False, False)
        self.geometry("800x500")

        self.create_widgets()
        self.load()

    def create_widgets(self):

        contanier = tk.Frame(self)
        contanier.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        label = tk.Label(contanier)
        label.place(x=0, y=0, relwidth=1, relheight=1)

        search_container = tk.Frame(contanier)
        search_container.pack(fill=tk.BOTH)

        self.search = tk.Entry(search_container, textvariable=self.search_value)
        self.search.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.search_button = tk.Button(search_container, text="Go")
        self.search_button.pack(side=tk.RIGHT)
        self.search_button['command'] = self.__search
        Hovertip(self.search_button, "Search button")

        self.listbox = tk.Frame(contanier)
        self.listbox.pack(expand=True, fill=tk.BOTH)

        self.button_create = tk.Button(contanier, text="Create")
        self.button_create['command'] = self.__open_create_window
        self.button_create.pack()

    def clear(self):
        for widget in self.listbox.winfo_children():
            widget.destroy()
    
    def load(self):
        self.clear()

        value = self.search_value.get().strip()

        if value is not None and len(value) > 0:
            cars: list[Car] = CarDataLogic.get_by_model(self.connection, value)
        else:
            cars: list[Car] = CarDataLogic.get_all(self.connection)
        x, y = 0, 0
        for car in cars:
            carview = CarView(self.listbox, car)
            carview.set_event(self.__delete_car)
            carview.place(x=x, y=y)
            x += 150

            if x > 700:
                x = 0
                y += 120

    def __search(self):
        self.load()

    def __delete_car(self, car_id: int):
        result = messagebox.askyesno(title="Удаление", message="Вы точно хотите удалить?")
        if result:
            CarDataLogic.delete_by_id(self.connection, car_id)
            self.load()

    def __open_create_window(self):
        create_window = CreateWindow(self)
        car = create_window.new_car

        CarDataLogic.insert(self.connection, car)

        self.load()
