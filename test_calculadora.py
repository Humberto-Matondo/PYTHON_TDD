import unittest
from calculadora import soma

# Todas metodo dentro dessa class de testes, precisao iniciar com a paravra test, caso n criares assim o teste n sera executado
class TestCalculadora(unittest.TestCase):
    # O nome do metodo precisa ser longo e explicando o que normalmente o teste faz
    def test_soma_5_com_5_deve_retornar_10(self):
        # Como existem varios assertes para casa tipo de testes, precisas ler a documentacao para saber qual deles usar
        self.assertEqual(soma(5, 5), 10) # Para saber se  o que retornar sera mesmo igual ao valor desejado(nesse ex: 10)

    def test_soma_10_negativo_com_5_deve_retornar_5(self):
        self.assertEqual(soma(-10, 5), ) # Como -10 + 5 = 5, o teste vai falhar, mostrando o erro

    
    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10,10,10),
            (-10,30,20),
            (1.5,1.5,3.0),
        )
        for x_y_saidas in x_y_saidas:
            with self.subTest(x_y_saida= x_y_saida): #Tem varias formas de executar um suptest()Para caso um dos varios testes estiver errados, nos soubermos. usamos o subtest() com o gerenciador de contest(with)
                x, y, saida = x_y_saidas
                self.assertEqual(soma(x,y),saida)    

    # Quanto mais testes, fizermos na funcao, melhor sera, assim sera mais facil encontrar algum Bug caso existir!
    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionError(self):
        with self.assertRaises(AssertionError): # Aqui vai passar, o resultado da funcao que eu meti a baixo vai dar realmente um assertionError, se metesse um TypeError nao passario no test
            soma('12', 0)
        
    def test_soma_y_nao_e_int_ou_float_deve_retornar_assertionError(self):
        with self.assertRaises(AssertionError):
            soma(12, '0')
            
unittest.main(verbosity=2)