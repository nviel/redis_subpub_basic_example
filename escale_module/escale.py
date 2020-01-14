import redis
import logging

logging.basicConfig(filename="/escale_module/log/escale.log", level=logging.DEBUG)


r = redis.Redis(host="redis_broker", port=6379)

r.publish("call_change", "FRCQF202000023")
r.publish("avis", "pilotage ok")
