class Database:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load()

    def load(self):
        try:
            with open(self.filename, 'r') as file:
                return eval(file.read())
        except FileNotFoundError:
            return {}

    def save(self):
        with open(self.filename, 'w') as file:
            file.write(str(self.data))

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value
        self.save()

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self.save()

db = Database('database.json')
db.set('name', 'John')
print(db.get('name'))
db.delete('name')
print(db.get('name'))