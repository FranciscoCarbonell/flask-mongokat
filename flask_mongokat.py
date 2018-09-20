from pymongo import MongoClient
from mongokat import Document,Collection
from flask import current_app

class MongokatClient(MongoClient):
    def __init__(self,host=None,port=None):
        if host and port:
            MongoClient.__init__(self,host,port)

    def setConfig(self,host,port):
        self.__init__(host,port)

client = MongokatClient()

class MongokatDocument(Document):
    pass

class MongokatCollection(Collection):
    col = None
    def __init__(self):
        namedb = current_app.config.get('MONGOKATDB')
        database = getattr(client,namedb)
        col = getattr(database,self.col)
        Collection.__init__(self,collection=col)

class MongokatApp():
    def __init__(self,app):
        if app is not None:
            self.app = app
            self.init_app(app)

    def init_app(self,app):
        app.config.setdefault('MONGOKATDB','flask')
        app.config.setdefault('MONGOKATHOST', 'localhost')
        app.config.setdefault('MONGOKATPORT', 27017)
        client.setConfig(app.config['MONGOKATHOST'],app.config['MONGOKATPORT'])
