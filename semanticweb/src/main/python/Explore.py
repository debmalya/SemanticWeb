from simplegraph import SimpleGraph

# container graph for celebrities.
cg=SimpleGraph()
cg.load('celeb_triples.csv')

# Which celebrities have dated more than one movie start?
# Which musicians spent time in rehab?
# 

if __name__ == "__main__":
	jt_reletions=[t[0] for t in cg.triples((None,'with','Justin Timberlake'))]
	print 'Having relationship with Justin Timberlake'
	for rel in jt_reletions:
		print [t[2] for t in cg.triples((rel,'with',None))]


