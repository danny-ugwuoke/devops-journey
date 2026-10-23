db_ports = [3306, 5432, 27017, 8080]
print("All ports:", db_ports)
first_port = db_ports[0]
print("First database port to scan:", first_port)
second_port = db_ports[1]
print("Second database port to scan:", second_port)
db_ports.append(6379)
for work in db_ports:
    print("Scanning active port:", work)