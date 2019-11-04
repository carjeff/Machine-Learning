import generators

def main():
    generator = generators.randFloat(0, 100)
    for n in generator(max = 10):
        print(n)
main()