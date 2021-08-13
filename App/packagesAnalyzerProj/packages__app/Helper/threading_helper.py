from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import threading
import time as t
import concurrent.futures
lock= threading.Lock()


def start_threading_scrap_insert(number_of_threading, dic, function_to_be_threaded ):

    futures = [] # misions list for threading

    with ThreadPoolExecutor(max_workers=number_of_threading) as executor:
        
        for val in dic:
            #executor.submit(make, dt )
            
            print(f'added futures : {val}')
            futures.append(executor.submit(function_to_be_threaded, val))

        #while futures:
        for future in concurrent.futures.as_completed(futures):

                try:
                    data = future.result()
                except Exception as exc:
                    print(f' generated ab exception : {exc}')
                else:
                    print(' data : {data}')
                
                print(f'finish futures : {future}')
                futures.remove(future)


    print(f"---- finished threading  on  start_threading_scrap_insert ")

