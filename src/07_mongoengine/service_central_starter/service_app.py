
import nosql.mongo_setup as mongo_setup
from nosql.engine import Engine
from nosql.servicehistory import ServiceHistory
from service_central_starter.nosql.car import Car


def main():
    print_header()
    config_mongo()
    # update_doc_version()
    user_loop()


def print_header():
    print('----------------------------------------------')
    print('|                                             |')
    print('|           SERVICE CENTRAL v.02              |')
    print('|               demo edition                  |')
    print('|                                             |')
    print('----------------------------------------------')
    print()

def config_mongo():
    mongo_setup.global_init()

def update_doc_version():
    for car in Car.objects():
        car._mark_as_changed('vi_number')
        car.save()


def user_loop():
    while True:
        print("Available actions:")
        print(" * [a]dd car")
        print(" * [l]ist cars")
        print(" * [f]ind car")
        print(" * [p]oorly service")
        print(" * perform [s]ervice")
        print(" * e[x]it")
        print()
        ch = input("> ").strip().lower()
        if ch == 'a':
            add_car()
        elif ch == 'l':
            list_cars()
        elif ch == 'f':
            find_car()
        elif ch == 's':
            service_car()
        elif ch == 'p':
            show_poorly_serviced_cars()
        elif not ch or ch == 'x':
            print("Goodbye")
            break


def add_car():
    """
    model = mongoengine.StringField()
    make = mongoengine.StringField()
    year = mongoengine.IntField()
    mileage = mongoengine.FloatField()
    vi_number = mongoengine.StringField()
    :return:
    """
    model = input("What is model?")
    make = input("What is make?")
    year = input("Year built?")

    car = Car()
    car.year = year
    car.make = make
    car.model = model

    engine = Engine()
    engine.horsepower = 600
    engine.mpg = 20
    engine.liters = 5.0
    car.engine = engine
    car.save()


    print("add_car")


def list_cars():
    cars = Car.objects.order_by("-year")
    for car in cars:
        print(f"{car.make} -- {car.model} with vin {car.vi_number} year -> {car.year}")
        print(f"{len(car.service_history)} of service records")
        for s in car.service_history:
            print(f"{s.price}$ ---> {s.description}")
    print("list_cars")


def find_car():
    print("TODO: find_car")


def service_car():
    # vin = input("What is VIN to service?")
    # car = Car.objects().filter(vi_number=vin).first()
    # if not car:
    #     print(f"car with {vin} not found")
    #     return
    #
    # print(f"We will service car {car.make}")
    # service = ServiceHistory()
    # service.price = float(input("What is price?"))
    # service.description = input("What type of service is this?")
    # service.customer_rating = input("Customer rating? [1-5] ")
    #
    # car.service_history.append(service)
    # car.save()

    vin = input("What is VIN to service?")

    print(f"We will service car")
    service = ServiceHistory()
    service.price = float(input("What is price?"))
    service.description = input("What type of service is this?")
    service.customer_rating = input("Customer rating? [1-5] ")

    # $addToSet and $push -> Higher performance solution
    updated = Car.objects(vi_number=vin).update_one(push__service_history=service)
    if not updated:
        print(f"car with {vin} not found")
        return

def show_poorly_serviced_cars():
    level = int(input("What max level of satisfaction are we looking for? [1-5] "))

    # Search in sub arrays of document
    # {"service_history.customer_rating": {$lte: level}}
    cars = Car.objects(service_history__customer_rating__lte=level)
    for car in cars:
        print(f"{car.make} -- {car.model} with vin {car.vi_number} (year {car.year}")
        print(f"{len(car.service_history)} of service records")
        for s in car.service_history:
            print(f" * Satisfaction {s.customer_rating} ${s.price} {s.description}")

    print()

if __name__ == '__main__':
    main()
