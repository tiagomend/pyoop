## pyoop

Este projeto simula o comportamento da Orientação a Objetos (OO) sem utilizar os recursos de OO da linguagem Python. O objetivo é demonstrar como a OO funciona internamente.

###  Simulando Classes e Herança

Em vez de classes tradicionais, usamos dicionários para representar objetos e funções para simular métodos. A herança é implementada através de dicionários aninhados, onde cada "classe" filha referencia sua "classe" pai.

###  Funções Principais

* `shape_density(thing, weight)`: Calcula a densidade dividindo o peso pela área do objeto.
* `shape_new(name)`: Cria um novo objeto do tipo `Shape` básico.
* `call(thing, method_name, *args)`: Procura e executa o método `method_name` no objeto `thing`, passando argumentos adicionais (*args).
* `find(cls, method_name)`: Procura recursivamente o método `method_name` na hierarquia de classes, começando pela "classe" (`cls`) informada.
* `make(cls, *args)`: Cria um novo objeto chamando a função `_new` da "classe" (`cls`), passando argumentos adicionais (*args).

###  Classes Simuladas

* `Shape`: Classe base para todas as formas. Define métodos para densidade genérica.
* `Square`: Classe filha de `Shape` representando um quadrado. Define métodos para perimetro, área e comparação de tamanho.
* `Circle`: Classe filha de `Shape` representando um círculo. Define métodos para perimetro, área e comparação de tamanho.

###  Exemplo de Uso

O script cria instâncias de quadrado e círculo, calcula a densidade e imprime o resultado.


###  Executando o Código

1. Clone o repositório: `git clone https://github.com/tiagomend/pyoop.git`
2. Navegue para a pasta do projeto: `cd pyoop`
3. Execute o script: `python main.py` (ou o nome do arquivo principal)


###  Contribuindo

Sinta-se livre para fazer fork e contribuir com o projeto! Melhore a documentação, implemente novas formas ou explore outros conceitos de OO sem utilizar funcionalidades nativas da linguagem.
