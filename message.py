from time import sleep
import argparse

WAIT = 0.01


def show(line):
    for c in line.strip():
        print(c, end='', flush=True)
        sleep(WAIT)


def show_text(text):
    for line in text:
        show(line)

        # Wait for the Enter key to be pressed
        if input() == 'q':
            print('Aborted')
            break


def main():
    parser = argparse.ArgumentParser(description='Display characters one by one. Press Q + Enter to quit.')
    parser.add_argument('input', type=str, help='Input file path')
    args = parser.parse_args()

    text = open(args.input).readlines()
    show_text(text)


if __name__ == "__main__":
    main()
