class Operacoes():
    def soma(self, valores):
        val = 0
        for v in valores:
            val = val + v
        return val

# print(Operacoes().soma([1, 3]))