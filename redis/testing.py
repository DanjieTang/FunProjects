import redis

r = redis.Redis()

r.set("Name", "Danjie")
print(r.get("Name").decode())