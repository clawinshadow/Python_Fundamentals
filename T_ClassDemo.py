class Secretive:
    def __inaccessible(self):
        print("Bet you can't see me..")

    def accessible(self):
        print("The secret message is:")
        self.__inaccessible()


secret = Secretive()
# secret.__inaccessible()
secret.accessible()
secret._Secretive__inaccessible()


class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']

s = SPAMFilter()
s.init()
sequence = ['SPAM', 'SPAM', 'Eggs', 'Bacon']
print(s.filter(sequence))

print(issubclass(SPAMFilter, Filter))
print(SPAMFilter.__bases__)
print(isinstance(s, SPAMFilter))
print(isinstance(s, Filter))
print(isinstance(s, str))
