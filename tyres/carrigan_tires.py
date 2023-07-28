from tyres.tires import Tires

class CarriganTires(Tires):
    def __init__(self,tire_wear):
        self.tire_wear=tire_wear

    def needs_service(self):
        for tirewear in self.tire_wear:
            if tirewear>= 0.9:
                return True
            else:
                return False
      