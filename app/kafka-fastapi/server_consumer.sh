
# 
# 
# 
export SERVER_AS_CONSUMER=0

uvicorn server_consumer:app --reload --host 0.0.0.0 --port 8003



# 
# 
# 
# ps -aux | grep "server_consumer:app"
# sudo kill -9 ID