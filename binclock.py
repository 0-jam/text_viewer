import time


def main():
    while True:
        print(format(int(time.time()), 'b'), end='\r')
        time.sleep(1)


if __name__ == "__main__":
    main()
