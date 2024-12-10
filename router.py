import math
class Router:
    def __init__(self, name):
        self.name = name
        self.neighbors = list()
        self.table = dict()
        self.temp_tables = dict()

    def add_neighbour(self, router, distance):
        self.neighbors.append(router)
        self.table[router] = [distance, router]
    
    def send_table(self):
        for n in self.neighbors:
            n.temp_tables[self] = self.table

    def update_table(self):
        for sender,temp_table in self.temp_tables.items():
            for dest, pair  in temp_table.items():
                sender_distance_to_me = self.table[sender][0]
                sender_distance_to_dest = pair[0]
                if dest in self.table:
                    current_distance = self.table[dest][0]
                    if current_distance > sender_distance_to_me + sender_distance_to_dest:
                        self.table[dest][0] = sender_distance_to_me + sender_distance_to_dest
                        gateway = self.table[sender][1]
                        self.table[dest][1] = gateway
                else:
                    gateway = self.table[sender][1]
                    self.table[dest] = [ sender_distance_to_me + sender_distance_to_dest, gateway]

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.__str__()