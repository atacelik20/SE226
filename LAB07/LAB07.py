class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = year

    def __str__(self):
        return f"VID: {self.vid} | {self.model} ({self.year})"

    def __eq__(self, other):
        return self.vid == other.vid

    def is_new(self, n):
        return self.year >= 2026 - n


class Car(Vehicle):
    def __init__(self, vid, model, year, fuel_type, doors):
        super().__init__(vid, model, year)
        self.fuel_type = fuel_type
        self.doors = doors

    def __str__(self):
        return f"[Car] VID: {self.vid} | {self.model} ({self.year}) | Fuel: {self.fuel_type} | {self.doors} Doors"


class Truck(Vehicle):
    def __init__(self, vid, model, year, max_load, axles):
        super().__init__(vid, model, year)
        self.max_load = max_load
        self.axles = axles

    def __str__(self):
        return f"[Truck] VID: {self.vid} | {self.model} ({self.year}) | Load: {self.max_load}kg | {self.axles} Axles"


class Motorcycle(Vehicle):
    def __init__(self, vid, model, year, engine_cc, type):
        super().__init__(vid, model, year)
        self.engine_cc = engine_cc
        self.type = type

    def __str__(self):
        return f"[Motorcycle] VID: {self.vid} | {self.model} ({self.year}) | Eng: {self.engine_cc}cc | Type: {self.type}"


def save_fleet_to_file(vehicles, filename):
    file = open(filename, "w")

    for vehicle in vehicles:
        if isinstance(vehicle, Car):
            file.write(f"Car, {vehicle.vid}, {vehicle.model}, {vehicle.year}, {vehicle.fuel_type}, {vehicle.doors}\n")

        elif isinstance(vehicle, Truck):
            file.write(f"Truck, {vehicle.vid}, {vehicle.model}, {vehicle.year}, {vehicle.max_load}, {vehicle.axles}\n")

        elif isinstance(vehicle, Motorcycle):
            file.write(f"Motorcycle, {vehicle.vid}, {vehicle.model}, {vehicle.year}, {vehicle.engine_cc}, {vehicle.type}\n")

    file.close()


def load_fleet_from_file(filename):
    vehicles = []

    file = open(filename, "r")

    for line in file:
        parts = line.strip().split(", ")

        vehicle_type = parts[0]
        vid = parts[1]
        model = parts[2]
        year = int(parts[3])

        if vehicle_type == "Car":
            fuel_type = parts[4]
            doors = int(parts[5])
            vehicles.append(Car(vid, model, year, fuel_type, doors))

        elif vehicle_type == "Truck":
            max_load = int(parts[4])
            axles = int(parts[5])
            vehicles.append(Truck(vid, model, year, max_load, axles))

        elif vehicle_type == "Motorcycle":
            engine_cc = int(parts[4])
            type = parts[5]
            vehicles.append(Motorcycle(vid, model, year, engine_cc, type))

    file.close()
    return vehicles


vehicles = [
    Car("V001", "Tesla Model 3", 2023, "Electric", 4),
    Truck("T101", "Volvo FH16", 2019, 25000, 6),
    Motorcycle("M301", "Yamaha R1", 2024, 998, "Sport"),
    Car("V002", "Toyota Corolla", 2018, "Petrol", 4),
    Truck("T102", "Mercedes Actros", 2021, 18000, 4),
    Motorcycle("M302", "Harley Davidson", 2015, 1200, "Cruiser")
]

save_fleet_to_file(vehicles, "fleet.txt")

print("Loading fleet data from 'fleet.txt'...")

loaded_vehicles = load_fleet_from_file("fleet.txt")

print(f"{len(loaded_vehicles)} vehicles loaded successfully.")

print("--- All Vehicles ---")
for vehicle in loaded_vehicles:
    print(vehicle)

print("--- Recent Vehicles (Last 4 Years) ---")
for vehicle in loaded_vehicles:
    if vehicle.is_new(4):
        print(vehicle)

print("--- Electric Cars Only ---")
for vehicle in loaded_vehicles:
    if isinstance(vehicle, Car) and vehicle.fuel_type == "Electric":
        print(vehicle)