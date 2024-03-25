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
    'redstone_torch' : {
        'stick' : 1,
        'redstone dust' : 1
    },
    'stick' : {
        'plank' : 0.5
    },
    'plank' : {
        'log' : 0.25
    },
    'iron_ingot' : {
        'iron block' : 1 / 9
    },
    'redstone_dust' : {
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