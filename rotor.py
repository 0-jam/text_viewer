# Python 3 implementation
import argparse
import time

rotors = {
    'rotor': "-\\|/",
    'bouncer': ".:':",
    'diamond': '<v>^',
    'ime': 'AＡあカｶ',
    # The list of strings is also acceptable
    'wave': ['...', '..:', '.::', '::.', ':..'],
    'nums': [1, 2, 3, 4],
}
speed = 0.5


# It will rotate forever if you don't stop it
def rotate(rotor, length=1):
    rps = speed / len(rotor)

    while True:
        for r in rotor:
            print(r * length, end="\r")
            time.sleep(rps)


def main():
    parser = argparse.ArgumentParser(description='Just print the cursor that looks like rotating at (about) 60 RPM. It strongly depends on the font that you use on your console.')
    parser.add_argument('--type', '-t', type=str, choices=rotors.keys(), default='rotor', help='The type of strings to show')
    parser.add_argument('--length', '-l', type=int, default=1, help='Length of strings')
    parser.add_argument('--reverse', '-r', action='store_true', help='Reverse the rotating direction (default: False)')
    args = parser.parse_args()

    rotor = rotors[args.type]

    if args.reverse:
        rotor = list(reversed(rotor))

    rotate(rotor, args.length)


if __name__ == "__main__":
    main()
