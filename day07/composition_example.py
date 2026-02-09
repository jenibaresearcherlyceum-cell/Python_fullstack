class Engine:
    def start(self):
        return "Engine started"

    def stop(self):
        return "Engine stopped"

class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        return self.engine.start()

    def stop_car(self):
        return self.engine.stop()

def main():
    my_car = Car()

    print(my_car.start_car())
    print(my_car.stop_car())


if __name__ == "__main__":
    main()
