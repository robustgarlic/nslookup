from nslookup import Nslookup
import socket

# set dns server
dns_query = Nslookup(dns_servers=['8.8.8.8'])


with open("input-ips.txt", "r") as hosts:
    for line in hosts:
        try:
            host = line.strip()
            ips_record = socket.gethostbyaddr(host)
            result = (host, ips_record[0])
            iplist = list(result)
            oplist = (', '.join(iplist))
            with open('ips2host.txt', 'a') as opfile:
                opfile.write('\n')
                opfile.write(oplist)
        except socket.herror:
            with open('ipsnoresolve.txt', 'a') as errfile:
                errfile.write('\n' + 'IP did not resolve Hostname: ' + host)
            pass


print('Finished nslookup-by-IP')