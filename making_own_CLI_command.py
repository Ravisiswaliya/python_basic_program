import sys
import argparse

def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('a', type=float, default=1.0, help = 'What is val1?')
    parse.add_argument('b', type=float, default=1.0, help = 'What is val2?')
    parse.add_argument('function', type=str, default='add', help = 'Function?(add,sub,mul,div')

    arg = parse.parse_args()
    sys.stdout.write(str(sci(arg)))

def sci(arg):
    if arg.function == 'add':
        return arg.a + arg.b
    elif arg.function == 'sub':
        return arg.a-arg.b
    elif arg.function == 'div':
        return arg.a/arg.b
    elif arg.function == 'mul':
        return arg.a*arg.b
    else:
        return 'Please enter right keyword??'

if __name__ == '__main__':
    main()