# Write a function that reads the /etc/hosts and return the hostname, given the ip address.
def gethostname(ip_address): 
    fh = open('/etc/hosts', 'r')
    columns = {}
    for line in fh.readlines():
        if not line.startswith('#'):
            tokens = line.split()
            if len(tokens) > 1:
                columns[tokens[0]] = tokens[1]

    print columns
    try:
        return columns[ip_address]
    except KeyError:
        return 'Unknown host'
        