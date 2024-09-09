# 추석에 집가자

취소표 잡아서 집갑시다

## DEPS
- https://github.com/ryanking13/SRT
- https://github.com/carpedm20/korail2

감사합니다..

## example config
```json
{
    "platform": "ktx | srt",
    "id": <id>,
    "password": <password>,
    "departure_loc": <출발지>,
    "arrival_loc": <도착지>,
    "date": <reserve_start_date, 20240914>,
    "time": <reserve_start_time, 070000>,
    "discord_webhook": <webhook_url>
}
```

## HOW TO RUN
> poetry install

> make config.json

> python main.py
