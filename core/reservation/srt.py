from SRT import SRT, train

class SRTReservation():
    def __init__(self, id, password):
        self.srt = SRT(id, password)
    
    def search(self, departure_loc:str, arrival_lo:str, date:str, time:str):
        trains = self.srt.search_train(
                departure_loc,
                arrival_lo,
                date,
                time
        )
        return trains
    
    def reserve(self, train: train.SRTTrain):
        return self.srt.reserve(train)