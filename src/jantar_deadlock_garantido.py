import threading #habilita multiplos threads para execuçãoparalela no python
import time

n_filo = 5 #numero de filososos no teste
garfos = [threading.Lock() for _ in range(n_filo)]
pegou_primeiro_garfo = threading.Semaphore(0)
segundo_garfo_livre = threading.Semaphore(0)

def pensar(id):
    print(f"Filósofo {id} está pensando...")
    time.sleep(0.5) #aguarda para pensar

def comer(id):
    print(f"Filósofo {id} está comendo.")
    time.sleep(0.5) #tempo de comer

def filosofo(id):
    garfo_esq = (id + 1) % n_filo
    garfo_dir = (id) % n_filo
    while True:
        pensar(id)
        print(f"Filósofo {id} com fome e tentando pegar garfo {garfo_esq} (na esquerda)")
        garfos[garfo_esq].acquire() #sincroniza
        print(f"Filósofo {id} pegou garfo {garfo_esq} (na esquerda)")
        pegou_primeiro_garfo.release() #libera garfo
        for _ in range(n_filo):
            segundo_garfo_livre.acquire()
        for _ in range(n_filo):
            segundo_garfo_livre.release()
        print(f"Filósofo {id} tentando pegar garfo {garfo_dir} (na direita)")
        garfos[garfo_dir].acquire()  # Aqui pode ocorrer deadlock já que os 2 garfos pode não estar disponiveis
        print(f"Filósofo {id} pegou garfo {garfo_dir} (na direita)")
        comer(id)
        print(f"Filósofo {id} deixou o garfo {garfo_esq} (na esquerda)")
        garfos[garfo_esq].release()
        print(f"Filósofo {id} deixou o garfo {garfo_dir} (na direita)")
        garfos[garfo_dir].release()

threads = [] #inicia livre
for i in range(1, n_filo + 1):
    t = threading.Thread(target=filosofo, args=(i,)) #uma thread para cada filsofo no ciclo
    t.start()
    threads.append(t)