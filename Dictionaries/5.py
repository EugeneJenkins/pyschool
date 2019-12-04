def mRNAtranscription(dna_template):
    dna2rna = {'A':'U', 'T':'A', 'C':'G', 'G':'C' }
    mRNA = ''
    result=[]
    for base in dna_template:
    	mRNA = dna2rna.get(base)
    	result.append(mRNA)
    return ''.join(result)
