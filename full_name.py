def get_first():
    return input("Enter your first name: ")

def get_last():
    return input("Enter your last name: ")

def gen_full(first, last):
    return "{} {}".format(first, last)

if __name__ == "__main__":
    print(gen_full(get_first(), get_last()))