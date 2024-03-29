import csv
def csvWriter(filename, records):
  header = []
  for i in records:
    if len(i) < 1:
      records.remove(i)
  for i in records:
    for v in i:
      if v not in header:
        header.append(v)
  for i in records:
    if len(i) == 0:
      return '0 records processed.'
  test=open(filename,'w')
  dict_wr = csv.DictWriter(test,header,lineterminator='\n')
  dict_wr.writerow(dict(zip(header,header)))
  for i in records:    
  # Adding in the sorted built-in fixed it
    dict_wr.writerow(dict(zip(header,sorted(i.values()))))  
  test.close()
  return '%d records processed.' % len(records)