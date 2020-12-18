#!/usr/bin/env python3
G='brloty rceolb chgoer hswogc synowh ybtons lbreot ercgol gechwo woghsn ntowsy tblony oblrecghwsnyt'
E,L={p for vs in G.split() for p in [vs[0] + vs[i] for i in range(1, len(vs))]}, set(''.join(G))
ws = sorted({l.strip() for l in open('/usr/share/dict/words')})
[print(w) for w in ws if w.lower() in L or (len(w) > 1 and all(w[i:i+2].lower() in E for i in range(len(w)-1)))]
