# 추석에 집가자

취소표 잡아서 집가려는 사람들을 위하여..

- https://github.com/ryanking13/SRT
- https://github.com/carpedm20/korail2

님의 라이브러리를 활용하여 만들어졌습니다. 감사합니다.

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
