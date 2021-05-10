import json

family = {"kids": 3, "wife": 1}
pets = {"dogs": ["mudge", "spot", "fido"], "cats": ["fluffy", "snowball", "garfield"], "fish": None}
# index (pos)      0         1       2                 0          1            2
# index (neg)     -3        -2      -1                -3         -2           -1

print(pets["dogs"])
print(pets["dogs"][-1])
print(pets["cats"])
print(pets["cats"][2])
print(type(pets))

jpets = json.dumps(pets, sort_keys=True, indent=4)
print(type(jpets))

print(jpets)
with open("samspets.json", "w") as petfile:
    petfile.write(jpets)

with open("f2.json", "w") as f:
     json.dump(pets, f)


