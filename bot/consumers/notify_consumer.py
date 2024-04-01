import json
from aiokafka import AIOKafkaConsumer
from aiogram import Bot
async def consume(kafka_topic:str,kafka_server:str,bot:Bot) -> None:
    consumer = AIOKafkaConsumer(
        kafka_topic,
        bootstrap_servers=kafka_server,
    )
    try:
        await consumer.start()
        try:
            async for msg in consumer:
                serialized = json.loads(msg.value)
                await bot.send_message(
                    chat_id=serialized.get("telegram_id"),
                    text=serialized.get("message"),
                )
        except Exception as e:
            print(e)
            await consumer.stop()
        finally:
            await consumer.stop()
    except Exception as e:
        await consumer.stop()
        print(e)
