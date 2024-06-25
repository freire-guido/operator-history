import argparse
import re

def main(args):
    pattern = r'<id>http://arxiv.org/abs/(.*?)</id>'
    with open(args['file']) as file:
        text = file.read()
        ids = re.findall(pattern, text)
    print(*ids, sep = '\n')
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str)

    args = vars(parser.parse_args())
    main(args)