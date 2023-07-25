from battery import Battery,NubbinBattery,SpindlerBattery
from engine import engine,capulet_engine,willoughby_engine,sternman_engine


class CarFactory:
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = willoughby_engine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
       
        car = car(engine, battery)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, tire_wear):
        engine = sternman_engine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
      
        car = car(engine, battery)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = willoughby_engine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
       # tires = OctoprimeTires(tire_wear)
        car = car(engine, battery)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = capulet_engine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
      #  tires = CarriganTires(tire_wear)
        car = car(engine, battery)
        return car