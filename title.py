import argparse
import time


def main():
    parser = argparse.ArgumentParser(description='First display characters one by one, then display the whole text.')
    parser.add_argument('input', type=str, help='Input text')
    args = parser.parse_args()

    text = args.input

    for character in text:
        print(character, end='\r', flush=True)
        time.sleep(0.15)

    print(text)


if __name__ == "__main__":
    main()
