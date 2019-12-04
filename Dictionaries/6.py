def baseComposition(dna_seq): 
	result={}
	DNAcode = ['A','C','T','G']
	output = result.fromkeys(DNAcode)
	output['A'] = dna_seq.count('A')
	output['C'] = dna_seq.count('C')
	output['T'] = dna_seq.count('T')
	output['G'] = dna_seq.count('G')
	
	return output
	