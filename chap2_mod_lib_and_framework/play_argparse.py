import argparse

# https://docs.python.org/3.8/howto/argparse.html
parser = argparse.ArgumentParser()

parser.add_argument("echo", help="echo the string you provided")
parser.add_argument("ekho", help="ecko the string you provided")

parser.add_argument("square", help="square your number", type=int)

args = parser.parse_args()
print(f"echo: {args.echo}")
print(f"ecko: {args.ekho}")
print(f"square({args.square})={args.square**2}")
