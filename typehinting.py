from typing import List, Union, Tuple, Dict, NewType, Callable, Sequence, Iterable

# Primitivos
numero: int = 10
flutuante: float = 10.5
booleano: bool = False
string: str = 'Humberto Matondo'

# Sequências
lista: List[int] = [1, 2, 3] # Essa lista é do tipo Lista(List) de inteiros
lista_str_int: List[Union[int, str]] = [1, 2, 3, 'Humberto'] #Union é União, logo esse codigo diz, a lista tem uniao de int e str... Tambm tem o Any que significa qualquer tipo de valor.
tupla: Tuple[int, int, int, str] = (1, 2, 3, 'Matondo')

# Dicionários e conjuntos

# Meu tipo
MeuDict = Dict[str, Union[str, int, List[int]]]  # Alias

pessoa: Dict[str, Union[str, int]] = {
    'nome': 'Humberto Matondo', 'sobrenome': 'Matondo', 'idade': 25}
pessoa2: MeuDict = {'nome': 'Humberto Matondo',
                    'sobrenome': 'Matondo', 'idade': 25, 'l': [1, 2]}

# Outra forma de fazer tipagem
UserId = NewType('UserId', int)
user_id = UserId(325456789)

#Para Funçoes:
def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable: # Callable singifica que essa Função "É uma função chamavem".
    return funcao


def soma(x: int, y: int) -> int:
    return x + y


print(retorna_funcao(soma)(10, 20))

# Para classes:
class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} está falando...')



def iterar(sequencia: Sequence[int]): #para receber qualquer coisa de sequencias:
    return [x for x in sequencia]


def iterar2(sequencia: Iterable[int]): #para receber qualquer interable de sequencias:
    return [x for x in sequencia]

print(iterar([1, 2, 3])) #lista que tem sequencias
print(iterar((1, 2, 3))) #tuplas que tem sequencias

print(iterar2([1, 2, 3])) #lista de Interable que tem sequencias
print(iterar2((1, 2, 3))) #tuplas de Interable que tem sequencias

#Para alem dessas coisas, na documentanção tem mais. É só ir ler e entender os exemplos.
