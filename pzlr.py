#!/usr/bin/env python3
G=['brloty','rceolb','chgoer','hswogc','synowh','ybtons','lbreot','ercgol','gechwo','woghsn','ntowsy','tblony','oblrecghwsnyt']
E,L={p for vs in G for p in [vs[0] + vs[i] for i in range(1, len(vs))]}, set(''.join(G))
ws = {l.strip().lower() for l in open('/usr/share/dict/words')}
[print(w) for w in sorted(ws) if w in L or (len(w) > 0 and all(w[i:i+2] in E for i in range(len(w)-1)))]
