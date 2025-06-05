import threading #habilita multiplos threads para execuçãoparalela no python
import time

n_filo = 5 #numero de filososos no teste
garfos = [threading.Lock() for _ in range(n_filo)]

def pensar(id):
    print(f"Filósofo {id} está pensando...")
    time.sleep(0.5) #aguarda para pensar

def comer(id):
    print(f"Filósofo {id} está comendo.")
    time.sleep(0.5) #tempo de comer

def filosofo(id):
    garfo_esq = id
    garfo_dir = (id + 1) % n_filo
    while True:
        pensar(id)
        if id == 0:
            # aqui se introduz a lógica não direcionada, sempre buscando o lado em que está disponivel
            print(f"Filósofo {id} (exceção) tentando pegar garfo {garfo_dir} (direita)")
            garfos[garfo_dir].acquire()
            print(f"Filósofo {id} (exceção) pegou garfo {garfo_dir} (direita)")
            print(f"Filósofo {id} (exceção) tentando pegar garfo {garfo_esq} (esquerda)")
            garfos[garfo_esq].acquire()
            print(f"Filósofo {id} (exceção) pegou garfo {garfo_esq} (esquerda)")
        else:
            print(f"Filósofo {id} tentando pegar garfo {garfo_esq} (esquerda)")
            garfos[garfo_esq].acquire()
            print(f"Filósofo {id} pegou garfo {garfo_esq} (esquerda)")
            print(f"Filósofo {id} tentando pegar garfo {garfo_dir} (direita)")
            garfos[garfo_dir].acquire()
            print(f"Filósofo {id} pegou garfo {garfo_dir} (direita)")
        comer(id)
        # garfos liberados na ordem inversa que foram pegos pelos filosofos. aqui se evita o deadlock
        if id == 0:
            print(f"Filósofo {id} (exceção) liberando garfo {garfo_esq} (esquerda)")
            garfos[garfo_esq].release()
            print(f"Filósofo {id} (exceção) liberando garfo {garfo_dir} (direita)")
            garfos[garfo_dir].release()
        else:
            print(f"Filósofo {id} liberando garfo {garfo_dir} (direita)")
            garfos[garfo_dir].release()
            print(f"Filósofo {id} liberando garfo {garfo_esq} (esquerda)")
            garfos[garfo_esq].release()

threads = []
for i in range(n_filo):
    t = threading.Thread(target=filosofo, args=(i,)) #uma thread para cada filsofo no ciclo
    t.start()
    threads.append(t)