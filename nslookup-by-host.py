from nslookup import Nslookup

# set dns server
dns_query = Nslookup(dns_servers=['8.8.8.8'])

iplist =[]
with open("input-hostname.txt", "r") as hosts:
    for line in hosts:
        host = line.strip()
        ips_record = dns_query.dns_lookup(host)
        result = (ips_record.answer)
        iplist = iplist + result
        if ips_record.response_full == []:
            print('SERVER CANT FIND: ' + host)
        else:
            with open('host2ips.txt', 'w') as opfile:
                lst1 = ('\n'.join(iplist))
                opfile.write(host + lst1)
                opfile.close()

            
