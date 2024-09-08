from core.reservation.srt import SRTReservation
from core.reservation.ktx import KTXReservation

def train_factory(train, id, password):
    if train == "srt":
        return SRTReservation(id, password)
    if train == "ktx":
        return KTXReservation(id, password)