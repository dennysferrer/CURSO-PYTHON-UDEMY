import json

class Laptop:
    name = 'Lenovo Ideapad 720s'
    procesador = 'Intel'

lapto1 = Laptop()

print(lapto1.name)
print(lapto1.procesador)

lapto1Json = json.dump(lapto1.__dict__)

print(lapto1Json)

