# https://py.checkio.org/en/mission/friends/


class Friends:
    def __init__(self, connections):
        if type(connections) != list:
            self.c = list(connections)
        else:
            self.c = connections

    def add(self, connection):
        if connection not in self.c:
            self.c.append(connection)
            return True
        else:
            return False

    def remove(self, connection):
        if connection in self.c:
            self.c.remove(connection)
            return True
        else:
            return False

    def names(self):
        k = set()
        for i in self.c:
            if len(i) >= 2:
                for v in i:
                    k.add(v)
        return k

    def connected(self, name):
        con = set()
        for i in self.c:
            if name in i:
                con.update(i - set([name]))
        return con
