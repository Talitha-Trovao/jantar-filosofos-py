# jantar-filosofos-py

O **problema do jantar dos filósofos** foi proposto por Edsger W. Dijkstra em 1965 e é um clássico problema de sincronização em computação concorrente.

## Descrição

Cinco filósofos sentam-se ao redor de uma mesa redonda, cada um com um prato de comida e um garfo à esquerda e à direita. Eles alternam entre pensar e comer. Para comer, um filósofo precisa pegar os dois garfos ao seu lado, mas só pode pegar um garfo de cada vez e não pode pegar um garfo que já esteja sendo usado por um vizinho. Após comer, o filósofo devolve ambos os garfos à mesa e volta a pensar.

**Regras:**
- 5 Filósofos
- 5 Garfos
- Só come quando tiver 2 garfos
- Após comer, devolve os garfos

## Implementação

Este repositório apresenta duas versões do problema:

- **Com deadlock:** Todos os filósofos podem acabar esperando indefinidamente pelos garfos, travando o sistema (deadlock)
- **Sem deadlock:** Uma solução que evita o deadlock ao alterar a ordem de aquisição dos garfos para pelo menos um filósofo, quebrando a espera circular.

Ambas as soluções são implementadas em Python utilizando o módulo `threading`.

## Como executar

No terminal, execute:

```bash
cd src
python3 jantar_solucao_python.py
```
ou
```bash
cd src
python3 jantar_deadlock_garantido.py
```

Observe o comportamento dos filósofos e dos garfos em cada solução.

## Referências

- [Filosofos Python - UEPG](https://deinfo.uepg.br/~alunoso/2021/SO/Filosofos_python/)
- [threading — Thread-based parallelism — Python Docs](https://docs.python.org/3/library/threading.html)