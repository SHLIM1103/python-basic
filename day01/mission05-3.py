import random

a = random.randrange(1, 8)
def switch(i):
    return {1: "도", 2: "개", 3: "걸", 4: "윷", 5: "모", 6: "백도", 7: "조커"}.get(i, -1)
print(switch(a))
