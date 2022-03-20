import time


class Termination:
    
    def __init__(self):
        pass
    
    def __call__(self):
        startime = time.time()
        ret = str(input("Press Enter to Fin"))
        while str(ret) == 't':
            passed_t = time.time() - startime
            print(f'{round((passed_t)/60)} Min Passed')
            ret = str(input("Press Enter to Fin"))

        