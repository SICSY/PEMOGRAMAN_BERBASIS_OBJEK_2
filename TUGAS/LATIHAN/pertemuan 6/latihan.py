# THREADING

import threading
class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        print("Thread {} is running".format(self.name))
t1 = MyThread("1")
t2 = MyThread("2")
t1.start()
t2.start()

# MULTIPROCESSING

# 1. MULTIPROCESSING

import multiprocessing
def worker(num):
    '''Fungsi untuk menjalankan tugas pada proses baru '''
    print('worker ', num)
if __name__ == '__main__':
    # membuat objek Proses sebanyak 5
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker,args=(i,))
        processes.append(p)
        p.start()
    
    # menunggu proses selesai
    for p in processes:
        p.join()

# 2.CONCUCRRENT.FETURES

import concurrent.futures
def worker(num):
    '''Fungsi untuk menjalankan tugas pada proses baru '''
    print('worker ', num)
if __name__ == '__main__':
    # membuat objek thread poolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        #memanggil fungsi worker sebanyak 5 kali
        for i in range(5):
            executor.submit(worker,i)

# 3. SUBPROCESS

import subprocess

def worker(num):
    '''fungsi untuk menjalankan tuigas pada proses baru'''
    print('worker', num)

if __name___ == '__main__':
    #membuat list untuk menyimpan setiap proses
    processes = []
    #memulai setiap proses dengan menggunakan subprocess.Popen
    for i in range(5):
        p = subprocess.Popen(['python', '-c', 
            'import multiprocessing; '
            'multiprocessing.Process(
            target=worker,args=('+str(i)+',)).start()'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        processes.append(p)
    for p in processes:
        out, err = p.communicate()
        print(out.decode('utf-8'), err.decode('utf-8')  

# 4. THREADING

import threading 
def worker (num):
    '''fungsi untuk menjalankan tugas pada thread baru '''
    print('worker',num)
if __name__ == '__main__':
    #membuat list untuk menyimpan setiap thread 
    thread = []
    #memulai setiap thread dengan menggunakan threading,thread
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        t.start()
        threads.append(t)
    
    # menunggu thread selesai 
    for t in threads:
        t.join()

# 5. MPI4PY

from mpi4py import MPI 

def worker (rank,size):
    '''fungsi untuk menjalankan tugas pada proses MPI'''
    print('worker',rank, 'of ', size)

if __name__ == '__main__':
    #inisialisasi MPI
    comn = MPI.comm__world
    rank = comm.Get_rank()
    size = comm.Get_size()

    # panggil fungsi worker pada setiap proses MPI
    worker(rank,size)
    
# 6. JOBLIB
from joblib import Parallel, delayed

def worker(num):
    """Fungsi untuk menjalankan tugas pada proses multiprocessing"""
    print('Worker', num)

if __name__ == '__main__':
    # Panggil fungsi worker secara parallel
    Parallel(n_jobs=2)(delayed(worker)(i) for i in range(5))

# 7. DASK 
import dask.bag as db

def worker(num):
    """Fungsi untuk menjalankan tugas pada proses multiprocessing"""
    print('Worker', num)

if __name__ == '__main__':
    # Buat dask bag dengan 5 item
    bag = db.from_sequence(range(5))

    # Panggil fungsi worker pada setiap item secara parallel
    bag.map(worker).compute()

# 8. PATHOS
from pathos.multiprocessing import ProcessPool

def worker(num):
    """Fungsi untuk menjalankan tugas pada proses multiprocessing"""
    print('Worker', num)

if __name__ == '__main__':
    # Buat ProcessPool dengan 2 proses
    pool = ProcessPool(2)

    # Panggil fungsi worker pada setiap item secara parallel
    pool.map(worker, range(5))

# 9. RAY

import ray\

@ray.remote
def worker(num):
    """Fungsi untuk menjalankan tugas pada proses multiprocessing"""
    print('Worker', num)

if __name__ == '__main__':
    # Inisialisasi Ray
    ray.init()

    # Buat task untuk setiap item secara parallel
    results = [worker.remote(i) for i in range(5)]

    # Ambil hasil task secara parallel
    ray.get(results)