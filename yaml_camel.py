import yaml

pets = {"dogs": ["mudge", "spot", "fido"], "cats": ["fluffy", "snowball", "garfield"], "fish": None}

print(yaml.dump(pets))

with open("camel.yaml", "r") as f:
    data = yaml.load(f)

print(data)
