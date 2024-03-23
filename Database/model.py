class Model:
    def __init__(self, db):
        self.db = db

    def __call__(self):
        return self.db.find()
    
    def get(self, filter):
        return self.db.find_one(filter)

    def create(self, doc):
        try:
            self.db.insert(doc)
            return True, None
        except Exception as e:
            return False, e.args
    
    def delete(self, filter):
        self.db.delete_one(filter)
    
    def update(self, filter, update):
        self.db.find_one_and_update(filter, update)
