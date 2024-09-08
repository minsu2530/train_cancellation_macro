import time
import logging
from core.config.config import get_config
from core.messenger.discord import Discord
from core.reservation.base import train_factory

def main():
    iteration = 0
    config = get_config()
    train_reserv = train_factory(config.platform, config.id, config.password)
    discord = Discord(config.discord_webhook)

    while True:
        msg = f'iteration {iteration}'
        print(msg)
        try:
            trains = train_reserv.search(
                config.departure_loc,
                config.arrival_loc,
                config.date,
                config.time
            )
            if len(trains) > 0:
                reservation = train_reserv.reserve(trains[0])
                discord.send(msg + ': ' + str(reservation))
        except Exception as e:
            discord.send(msg + ': ' + str(e))
            print(e)

        iteration += 1
        time.sleep(10)

if __name__ == '__main__':
    main()
