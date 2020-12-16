G='brlty rcel chge hswg synw ytn let eg gw wn nt t'
E=set(G+'o');[[E.update((v[0]+i,i+v[0]))for i in v[1:]+'o']for v in G.split()]
[print(w)for w in{l[:-1].lower()for l in open('/usr/share/dict/words')}if{w[i:i+2]for i in range(len(w))}<=E]
