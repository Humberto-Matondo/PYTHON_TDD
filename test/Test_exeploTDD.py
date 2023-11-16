"""
TDD - Test Driven Development

Red
1-Parte: Criar o teste e ver ele a FALHAR(cria apenas o teste sem criar as funcoes)

Green
2-Parte: Criar o teste e ver ele a PASSAR(criar as funcoes para ver o teste a passar)

Refactor
3-Parte: Melhorar meu codigo
"""
try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise

import unittest
from exemploTDD import bacon_com_ovos

class testBaconConOvos(unittest.TestCase):
    # 1. Receber um numero inteiro:
    def test_bacon_com_ovos_deve_levantar_assertion_error_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('')
    
    # 2. Saber se o numero e multiplo de 3 e 5, se sim: Bacon com ovos
    def test_bacon_com_ovos_deve_retonar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com ovos'
        
        for entrada in entradas:
            with self.subTest(entrada=entradas,saida=saida):
                self.assertEqual(bacon_com_ovos(entrada),saida, msg=f'"{entrada}" nao retornou "{saida}"')
    
    # 3. Saber se o numero n e multiplo de 3 e 5, Se sim: Passar fome           
    def test_bacon_com_ovos_deve_retonar_passar_fome_se_entrada_nao_for_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 7, 8)
        saida = 'Passar fome'
        
        for entrada in entradas:
            with self.subTest(entrada=entradas,saida=saida):
                self.assertEqual(bacon_com_ovos(entrada),saida, msg=f'"{entrada}" nao retornou "{saida}"')
    
    #4. Saber se o numero e multiplo somente de 3, Se sim: Bacon
    def test_bacon_com_ovos_deve_retonar_Bacon_se_entrada_nao_for_multiplo_de_3(self):
        entradas = (3, 6, 9, 12, 18, 21)
        saida = 'Bacon'
        
        for entrada in entradas:
            with self.subTest(entrada=entradas,saida=saida):
                self.assertEqual(bacon_com_ovos(entrada),saida, msg=f'"{entrada}" nao retornou "{saida}"')
    
    #5. Saber se o numero e multiplo somente de 5, Se sim: Ovos            
    def test_bacon_com_ovos_deve_retonar_ovos_se_entrada_nao_for_multiplo_de_5(self):
        entradas = (5, 10, 20, 25, 35)
        saida = 'Ovos'
        
        for entrada in entradas:
            with self.subTest(entrada=entradas,saida=saida):
                self.assertEqual(bacon_com_ovos(entrada),saida, msg=f'"{entrada}" nao retornou "{saida}"')
                
if __name__ == '__main__':      
    unittest.main(verbosity=2)