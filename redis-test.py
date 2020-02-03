import redis

r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
#print ("set key1 123")
#print (r.set('key1', '123'))
print ("get keys")
for k in r.keys():
    print (k)


