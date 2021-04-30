import random

def gen_list(n):
    return [random.randrange(1,10) for x in range(n)]

def avg_list(list):
    if len(list) == 0:
        return None
    return sum(list)/len(list)

if __name__ == "__main__":
    list = gen_list(5)
    avg = avg_list(list)
    print("{} has an average value of {}".format(list, avg))