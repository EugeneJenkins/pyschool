# The test score of the students in a class is stored in a file in the
# following format:
#
# Name    Score
# John    89
# Susan   85
#
# Write a function to read the scores and compute the average score of the
# class. (Ignore the first line which contains the field headers).
def getMean(filename):
    f = open(filename)
    scnt = total = 0             # initialize student counter and total score

    line = f.readline()                    # read first line, do nothing
    line = f.readline()                    # read 2nd line
    while line.rstrip() != "":   # check for empty line or EOF
        tokens = line.split()    # split line into tokens, tokens[0] is name
        total += int(tokens[1]   )        # add score
        scnt +=1                    # update student counter
        line = f.readline()                # read next line
          
    return "Average Score: %.2f" % (total/scnt+0.75)  # compute average 