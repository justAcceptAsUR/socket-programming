import pymongo

connecTo = pymongo.MongoClient('mongodb://localhost:27017')
db = connecTo['shaiduck']
col = db['oxford']

for x in col.find():
    print(x['word'][0])
    print('z'+x['word']+'z')
