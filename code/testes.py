class Teste:
    def metodo_dinamico(self, a, b) -> int:
        '''Método Dinâmico\n
        Recebe dois valores e retorna a sua soma'''
        return a + b
    
    @staticmethod
    def metodo_estatico(a, b) -> int:
        '''Método Estático\n
        Recebe dois valores e retorna a sua soma'''
        return a + b

var_a = 5
var_b = 10

test = Teste()

print(test.metodo_dinamico)
print(Teste.metodo_dinamico)

'''
print(test.metodo_dinamico(var_a, var_b))
print(test.metodo_estatico(var_a, var_b))

# print(Teste.metodo_dinamico(var_a, var_b))
print(Teste.metodo_estatico(var_a, var_b))
'''