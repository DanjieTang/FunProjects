from redis import Redis
import pathlib

redis_cliient = Redis.from_url("redis://localhost:6379/0")