import argparse
import os

parser = argparse.ArgumentParser(description="Automatically go to any Google Classroom Links")
parser.add_argument('-s', '--show', action='store_true', help='show link choices')
parser.add_argument('-l', '--link', type=int, metavar='', help='takes an int argument to choose link')
group = parser.add_mutually_exclusive_group()
group.add_argument('-c', '--chooseLink', action='store_true', help = 'must be invoked in first position to choose link')

args = parser.parse_args()

def classLink(link):
        switcher={
            1:'https://classroom.google.com/u/0/c/MTE5MjQ4MDE1NDU0',
            2:'https://classroom.google.com/u/0/c/MTE5MjQ4MDE1NTAx',
            3:'https://classroom.google.com/u/0/c/MTE5MjQ4MDE1NTQ0',
            4:'https://classroom.google.com/u/0/c/MTE5MjQ4MDE1NTg0',
            5:'https://classroom.google.com/u/0/c/MTE5MjU1ODA4ODg5',
            6:'https://classroom.google.com/u/0/c/MTE5MjU1ODA4OTM0',
            7:'https://classroom.google.com/u/0/c/MTE5MjQ4MDE1NTY0',
            8:'https://classroom.google.com/u/0/c/MTE5MjQ3OTc3Njg2'
            }
        return switcher.get(link,"Invalid input")

if __name__ == '__main__':
    
    if args.show:
        print("\033[1;92mWhich class do you want to go?")
        print("\033[1;92m1 -> \033[97mHUMM110 - Art Appreciation\n" +
        "\033[1;92m2 -> \033[97mCC204 - Data Structures and Algorithm\n" +
        "\033[1;92m3 -> \033[97mCCS223 - Discrete Structures 2\n" +
        "\033[1;92m4 -> \033[97mCIT207 - Object-Oriented Programming\n" +
        "\033[1;92m5 -> \033[97mPE113 - Physical Education\n" +
        "\033[1;92m6 -> \033[97mSS111 - The Contemporary World\n" +
        "\033[1;92m7 -> \033[97mSS112 - Ethics\n" +
        "\033[1;92m8 -> \033[97mCCS246 - Intro to AI")

    if args.chooseLink:
        os.system('start firefox ' + classLink(args.link))

