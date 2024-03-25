import math
print("A calculator that calculates the necessary base materials for a piston bolt that is n blocks long.")
print("Piston bolt is one designed for Bedrock Edition by chickenspaceprogram.\n")
num_bolts = math.ceil(float(input("Enter piston bolt length here: ")) / 3)
recipes = {
    "bolt" : {
        'comparator' : 2,
        'blocks' : 2,
        'sticky piston' : 2,
        'redstone dust' : 2
    },
    "sticky_piston" : {
        'slimeball' : 1,
        'piston' : 1
    },
    "piston" : {
        'plank' : 3,
        'cobblestone' : 4,
        'iron ingot' : 1,
        'redstone dust' : 1
    },
    'comparator' : {
        'stone' : 3,
        'quartz' : 1,
        'redstone torch' : 3
    },
    'redstone torch' : {
        'stick' : 1,
        'redstone dust' : 1
    },
    'stick' : {
        'plank' : 0.5
    },
    'plank' : {
        'log' : 0.25
    },
    'iron ingot' : {
        'iron block' : 1 / 9
    },
    'redstone dust' : {
        'redstone block' : 1 / 9
    }
}

if input("Include floor blocks? (y/n): ").lower() == 'y':
    recipes["bolt"]["blocks"] += 9

all_items_used = set()
for key in recipes:
    all_items_used.add(key)

for value_key in recipes.values():
    for value_value in value_key:
        all_items_used.add(value_value)

all_items_needed = dict()

for item in all_items_used:
    all_items_needed[item] = 0

all_items_needed["bolt"] = num_bolts

need_to_loop = True

while need_to_loop:
    need_to_loop = False
    for item in all_items_needed:
        if (item in recipes.keys()) and (all_items_needed[item] != 0):
            need_to_loop = True
            for key in recipes[item]:
                all_items_needed[key] += recipes[item][key] * all_items_needed[item]

for i in all_items_needed:
    print(i)