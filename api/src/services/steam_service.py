import json
from utils.produser import AIOWebProducer
from core.config import settings

class SteamService:
    def __init__(self, data):
        self.data = data

    async def send_task(self, data):
        message_to_produce = json.dumps(
            {
                "telegram_id": "483123399",
                "message": "message_to_produce",
                "steam_id": "76561198381522154",
            }
        ).encode(encoding="utf-8")
        producer = AIOWebProducer(topic=settings.kafka_steam_topic)
        await producer.send(value=message_to_produce)
