import json
import numpy as np
import matplotlib.pyplot as plt

with open('./jsb-chorales-8th.json','r',encoding='utf8') as fp:
    JSB = json.load(fp)

JSB_all = JSB['train'] + JSB['valid'] + JSB['test']

chords = set()
hist = np.zeros(500).astype(int)
c_tick=0
for piece in JSB_all:
    for tick in piece:
        # tick=tick[1:]
        for i in range(len(tick)):
            tick[i] = int((tick[i]-60) % 12)
        tt = frozenset(tick)
        if tt not in chords:
            chords.add(tt)
        else:
            hist[len(chords)-1] += 1
        c_tick += 1

print(chords)
labels=[]
values=[]
for i, c in enumerate(chords):
    if hist[i]>500:
        labels.append(str(sorted(list(c))))
        values.append(hist[i])
plt.bar(np.arange(len(labels)), values)
plt.xticks(np.arange(len(labels)), labels, rotation=90)
plt.show()
