# Write a function to read a CSV file with ',' as delimiter and returns a list of records.
# The function must be able to ignore ',' that are within a pair of double quotes '"'.
import csv
def csvReader(filename):
  
    with open(filename) as f:
              # ignore empty line
	
	reader=csv.reader(f)
	records = list(reader)

    return records 