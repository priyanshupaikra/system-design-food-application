# Round Robin Load Balancer
class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_server(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server

# Usage
servers = ["order-service-1", "order-service-2"]
lb = LoadBalancer(servers)

print(lb.get_server())
print(lb.get_server())
# Stateless services + round-robin LB