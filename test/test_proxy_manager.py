#coding:utf8
import os
import sys
import redis

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.proxy_manager import ProxyManager



if __name__=="__main__":
    #可清除以下
    redis_send_pool=redis.ConnectionPool(host="127.0.0.1", port=6379, db=0, password="my_redis_passwd",decode_responses=True)
    redis_log_pool=redis.ConnectionPool(host="127.0.0.1", port=6379, db=1, password="my_redis_passwd",decode_responses=True)
    redis_tmp_pool=redis.ConnectionPool(host="127.0.0.1", port=6379, db=2, password="my_redis_passwd",decode_responses=True)
    #不可清除以下
    redis_config_pool=redis.ConnectionPool(host="127.0.0.1", port=6379, db=15, password="my_redis_passwd",decode_responses=True)
    redis_job_pool=redis.ConnectionPool(host="127.0.0.1", port=6379, db=14, password="my_redis_passwd",decode_responses=True)

    pm=ProxyManager(redis_send_pool,redis_log_pool,redis_tmp_pool,redis_job_pool,redis_config_pool)
    pm.run_forever()