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
    "id": <srt_id>,
    "password": <srt_password>,
    "departure_loc": "수서",
    "arrival_loc": "광주송정",
    "date": "20240914",
    "time": "0700",
    "discord_webhook": <webhook_url>
}
```

## HOW TO RUN
> poetry install

> make config.json

> python main.py
