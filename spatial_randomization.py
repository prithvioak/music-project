import random
# Generating random directions and magnitudes for the purpose of spatialization
ret = []
for i in range(30):
    ret.append((random.random()*360, random.random()))
print(ret)