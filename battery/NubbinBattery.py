from battery.Battery import Battery
from datetime import datetime

class NubbinBattery(Battery):

    nubbin_service_req=4

    def __init__(self,last_service_date,current_date):
        self.last_service_date=last_service_date
        self.current_date=current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + self.nubbin_service_req)
        if service_threshold_date < self.current_date:
            return True
        else:
            return False


