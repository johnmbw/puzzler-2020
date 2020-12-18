G='brlty rcel chge hswg synw ytn let eg gw wn nt t';import sys
E=set(G+'o');[[E.update((v[0]+i,i+v[0]))for i in v[1:]+'o']for v in G.split()]
[print(w)for w in{l[:-1]for l in open(sys.argv[1])}if{w[i:i+2].lower()for i in range(len(w))}<=E]
