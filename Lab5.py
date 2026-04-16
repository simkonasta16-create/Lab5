from abc import ABC, abstractmethod

class ElectricalAppliance(ABC):
    def __init__(self, name: str, power: float, radiation: float):
        if power < 0:
            raise ValueError("Потужність не може бути від’ємною")
        if radiation < 0:
            raise ValueError("Випромінювання не може бути від’ємним")

        self.name = name
        self.power = power
        self.radiation = radiation
        self.is_plugged = False

    def plug_in(self):
        self.is_plugged = True

    def unplug(self):
        self.is_plugged = False

    def __repr__(self):
        return f"{self.name} | {self.power}W | rad:{self.radiation}"

class Kettle (ElectricalAppliance):
    def __init__(self, name, power, radiation, volume):
        super().__init__(name, power, radiation)
        self.volume = volume


class TV (ElectricalAppliance):
    def __init__(self, name, power, radiation, screen_size):
        super().__init__(name, power, radiation)
        self.screen_size = screen_size


class Laptop(ElectricalAppliance):
    def __init__(self, name, power, radiation, ram):
        super().__init__(name, power, radiation)
        self.ram = ram


class WashingMachine(ElectricalAppliance):
    def __init__(self, name, power, radiation, load):
        super().__init__(name, power, radiation)
        self.load = load


class Fridge(ElectricalAppliance):
    def __init__(self, name, power, radiation, volume):
        super().__init__(name, power, radiation)
        self.volume = volume

class Apartment:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        if not isinstance(device, ElectricalAppliance):
            raise TypeError("Можна додавати тільки електроприлади")
        self.devices.append(device)

    def plug_device(self, name: str):
        for d in self.devices:
            if d.name == name:
                d.plug_in()
                return
        raise ValueError(f"Прилад '{name}' не знайдено")

    def total_power(self):
        return sum(d.power for d in self.devices if d.is_plugged)

    def sort_by_power(self):
        self.devices.sort(key=lambda x: x.power)

    def find_by_radiation(self, min_r: float, max_r: float):
        if min_r > max_r:
            raise ValueError("Некоректний діапазон")

        return [d for d in self.devices if min_r <= d.radiation <= max_r]

    def __repr__(self):
        return "\n".join(str(d) for d in self.devices)

try:
    flat = Apartment()

    flat.add_device(Kettle("Kettle", 2000, 0.3, 1.7))
    flat.add_device(TV("TV", 120, 0.8, 55))
    flat.add_device(Laptop("Laptop", 65, 0.5, 16))
    flat.add_device(WashingMachine("Washer", 500, 0.7, 7))
    flat.add_device(Fridge("Fridge", 300, 0.2, 220))

    flat.plug_device("Kettle")
    flat.plug_device("TV")
    flat.plug_device("Laptop")

    print("Прилади")
    print(flat)

    print("\nЗагальна споживана потужність:", flat.total_power(), "W")

    print("\nСортування за потужністю:")
    flat.sort_by_power()
    print(flat)

    print("\nПрилади з випромінюванням 0.3 - 0.8:")
    for d in flat.find_by_radiation(0.3, 0.8):
        print(d)

except (ValueError, TypeError) as e:
    print("Помилка:", e)