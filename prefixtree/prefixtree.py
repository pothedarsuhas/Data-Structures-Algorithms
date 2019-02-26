wordkey = '/n'

class PrefixTree:

    def __init__(self):
        self.head = {}

    def add(self, value):
        d = self.head

        while len(value) > 0:
            c = value[0]
            if c not in d:
                d[c] = {}

            d = d[c]
            value = value[1:]
        if wordkey in d:
            return False
        d[wordkey] = True
        return True


    def __contains__(self, value):
        d = self.head

        while len(value) > 0:
            c = value[0]
            if c not in d:
                return False
            d = d[c]
            value = value[1:]

        if wordkey in d:
            return d[wordkey]

p = PrefixTree()

print(p.add("car"))

# print(p.add("car"))

print(p.__contains__("card")) #
print("car" in p)            # both these are same

