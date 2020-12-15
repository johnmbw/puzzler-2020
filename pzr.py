G,f='brloty rceol chgoe hswog synow yton leot ego gwo won nto to',lambda l:{i for s in l for i in s}
E,d=f(f((v[0]+i,i+v[0])for i in v[1:])for v in G.split())|f(G),open('/usr/share/dict/words')
[print(w)for w in{l.strip().lower()for l in d}if {w[i:i+2]for i in range(len(w))}<=E]
