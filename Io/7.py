def getWinner(filename): 
    results = open(filename).readlines()        
    winner = ''   
    max_score =0 
    for line in results:
        tokens = line.split(',')    
        name =  tokens[0]                
        scores = sorted(map(float, tokens[1].split()))
        ave = sum(scores[1:-1])/(len(scores) - 2)                    
        if ave > max_score:
           winner = name             
           max_score = ave         
    return "%s [%.1f]" % (winner, max_score)