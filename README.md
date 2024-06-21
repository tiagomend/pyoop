# Implementação de Classes com Dicionários

Este repositório contém um estudo sobre a implementação interna de classes em orientação a objetos usando dicionários em Python. O objetivo é demonstrar como funções e dados podem ser encapsulados em estruturas de dicionários para simular o comportamento de objetos e classes.

## Arquivos

O repositório contém os seguintes arquivos:

- `shapes_dict.py`
- `shapes_class.py`

### shapes_dict.py

Este arquivo contém uma implementação simples de um "objeto" quadrado usando dicionários. As funções de perímetro e área são definidas separadamente e associadas ao dicionário que representa o quadrado.

#### Funções

- `square_perimeter(thing)`: Calcula o perímetro de um quadrado.
- `square_area(thing)`: Calcula a área de um quadrado.
- `square_new(name, side)`: Cria uma nova instância de um quadrado.
- `call(thing, method_name)`: Chama um método associado ao "objeto" quadrado.

#### Exemplo de Uso

```python
examples = [square_new('sq', 3)]

for ex in examples:
    n = ex['name']
    p = call(ex, 'perimeter')
    a = call(ex, 'area')
    print(f'{n} {p:.2f} {a:.2f}')
```

### shapes_class.py

Este arquivo refina a abordagem anterior ao introduzir uma estrutura de classe simulada. As funções de perímetro e área são agrupadas em um dicionário que representa a classe.

#### Funções

- `square_perimeter(thing)`: Calcula o perímetro de um quadrado.
- `square_area(thing)`: Calcula a área de um quadrado.
- `Square`: Dicionário que representa a "classe" quadrado.
- `square_new(name, side)`: Cria uma nova instância de um quadrado associada à "classe".
- `call(thing, method_name)`: Chama um método associado ao "objeto" quadrado.

#### Exemplo de Uso

```python
examples = [square_new('sq', 3)]

for ex in examples:
    n = ex['name']
    p = call(ex, 'perimeter')
    a = call(ex, 'area')
    c = ex['_class']['_classname']
    print(f'{n} is a {c}: {p:.2f} {a:.2f}')
```

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/shapes-study.git
   cd shapes-study
   ```

2. Execute os scripts:
   ```bash
   python shapes_dict.py
   python shapes_class.py
   ```

## Explicação

O estudo compara duas abordagens para implementar classes e objetos:

1. **shapes_dict.py**: Utiliza um dicionário simples para representar um objeto. As funções de método são separadas e referenciadas no dicionário do objeto.

2. **shapes_class.py**: Introduz um nível adicional de abstração ao criar uma estrutura de classe com métodos encapsulados. As instâncias do objeto referenciam a "classe" para acessar seus métodos.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Esse README fornece uma visão geral clara dos arquivos e funcionalidades do projeto, além de instruções sobre como usá-lo e contribuir.