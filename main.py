import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mode", help="select mode", type=str)

args = parser.parse_args()


if args.mode == 'mix':
    print("MIX !!!!!")
elif args.mode == 'lowest':
    print("LOWEST !!!!!")
elif args.mode == 'highest':
    print("HIGHEST !!!!!")