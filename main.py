import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mode", help="select mode", type=str)

args = parser.parse_args()

class Color():

    '''
    def __init__(self):
        self.lines = []
    '''

    def load_file(self):
        with open('colors.txt') as f:
            return f.readlines()

    def check_first_format(self, line):

        eight_letter_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',}

        for i in range(len(line)):
            try:
                word = ''
                for j in range(i, 8+i):
                    word += line[j]
            except:
                pass
                #print('string to short')
            if len(word) == 8:
                col_value = ''
                for letter in word:
                    if letter in eight_letter_set:
                        col_value += letter
                    else:
                        break
                if len(col_value) == 8:
                    print(col_value)


my_col = Color()
file_lines = my_col.load_file()

for line in file_lines:
    my_col.check_first_format(line)

if args.mode == 'mix':
    print("MIX !!!!!")
elif args.mode == 'lowest':
    print("LOWEST !!!!!")
elif args.mode == 'highest':
    print("HIGHEST !!!!!")