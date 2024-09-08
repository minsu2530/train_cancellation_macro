from korail2 import *

class KTXReservation():
    def __init__(self, id, password) -> None:
        self.ktx = Korail(id, password)
    
    def search(self, departure_loc:str, arrival_lo:str, date:str, time:str):
        try:
            trains = self.ktx.search_train(
                departure_loc,
                arrival_lo,
                date,
                time,
            )
        except NoResultsError:
            return []
        return trains

    def reserve(self, train):
        return self.ktx.reserve(train)