import logging
import sys
import asyncio
import os
import json

from aiogram import F
import steam_service
from aiokafka import AIOKafkaConsumer
from produser import AIOWebProducer

kafka_server: str = os.environ.get("KAFKA_SERVER", "broker:29092")
kafka_notify_topic: str = os.environ.get("KAFKA_NOTIFY_TOPIC", "notify_friends")
kafka_steam_topic: str = os.environ.get("KAFKA_STEAM_TOPIC", "steam")
kafka_client_id: str = os.environ.get("KAFKA_CLEIENT_ID", "python-producer")


async def send_friends_info(tg_id, message) -> None:
    message_to_produce = json.dumps({"telegram_id": tg_id, "message": message}).encode(
        encoding="utf-8"
    )
    producer = AIOWebProducer(topic=kafka_notify_topic)
    await producer.send(value=message_to_produce)
    producer.stop()


async def consume_friends() -> None:
    """Слушатель входящих запросов на инфу о друзях"""
    consumer = AIOKafkaConsumer(
        kafka_steam_topic,
        bootstrap_servers=kafka_server,
    )
    await consumer.start()
    try:
        async for msg in consumer:
            serialized = json.loads(msg.value)
            print("Начинаеи обработку запроса о друзьях")
            result = steam_service.get_steam_user_friends_info(
                steam_id=str(serialized.get("steam_id")),
            )
            print(result)
            message_to_produce = json.dumps(
                {"telegram_id": serialized.get("telegram_id"), "message": result}
            ).encode(encoding="utf-8")
            producer = AIOWebProducer(topic=kafka_notify_topic)
            await producer.start()
            try:
                await producer.send(value=message_to_produce)
            finally:
                await producer.stop()
    finally:
        await consumer.stop()


async def main() -> None:
    consuming = asyncio.create_task(consume_friends())
    await asyncio.gather(consuming)
    print("Steam service start consuming ")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
