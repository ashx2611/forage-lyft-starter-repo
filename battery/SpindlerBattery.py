from battery.Battery import Battery
from datetime import datetime

class SpindlerBattery(Battery):

    spindler_service_req=2

    def __init__(self,last_service_date,current_date):
        self.last_service_date=last_service_date
        self.current_date=current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + self.spindler_service_req)
        if service_threshold_date < self.current_date:
            return True
        else:
            return False
        


