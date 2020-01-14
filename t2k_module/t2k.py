import redis
import logging

logging.basicConfig(filename="/t2k_module/log/t2k.log", level=logging.DEBUG)

r = redis.Redis(host="redis_broker", port=6379)
p = r.pubsub()

p.subscribe("call_change")
mess = p.get_message()
logging.info(mess)

for mess in p.listen():
    logging.info(mess)
