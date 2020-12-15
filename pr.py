G='brloty rceol chgoe hswog synow yton leot ego gwo won nto to'
E=set(G);[[E.update((v[0]+i,i+v[0]))for i in v[1:]]for v in G.split()]
[print(w)for w in{l.strip().lower()for l in open('/usr/share/dict/words')}if {w[i:i+2]for i in range(len(w))}<=E]
