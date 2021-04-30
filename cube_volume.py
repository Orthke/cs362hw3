#Calculate volume for a cube

def calc_volume_cube(s):
    if s < 0:
        return None
    return s*s*s

def get_input():
    return int(input("Enter a cube size: "))

if __name__ == "__main__":
    print("{} units^3".format(calc_volume_cube(get_input())))