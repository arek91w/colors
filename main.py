import argparse
from pprint import pprint

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

    def check_first_format(self, lines):
        
        colors = []
        eight_letter_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',}

        for line in lines:
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
                        colors.append(col_value)
        
        return colors
    
    def rgb_to_hue(self, r, g, b):
        r = int(r)/255
        g = int(g)/255
        b = int(b)/255
        max_v = max(r, g, b)
        min_v = min(r, g, b)
        if r >= g and r >= b:
            hue = (g-b)/(max_v-min_v)
        elif g > r and g >= b:
            hue = 2.0 + (b-r)/(max_v-min_v)
        else:
            hue = 4.0 + (r-g)/(max_v-min_v)
        hue = hue * 60
        if hue < 0:
            hue = hue + 360
        
        return hue


my_col = Color()
file_lines = my_col.load_file()


first_format_colors = my_col.check_first_format(file_lines)

for col in first_format_colors:
    red = col[0:2]
    green = col[2:4]
    blue = col[4:6]
    alpha = col[6:8]
    print(f"RED: {int(red, 16)}")
    print(f"GREEN: {int(green, 16)}")
    print(f"BLUE: {int(blue, 16)}")
    print(f"ALPHA: {int(alpha, 16)}")
    print(f"HEX: #{col}")
    hue = my_col.rgb_to_hue(int(red, 16), int(green, 16), int(blue, 16))
    print(f"HUE: {hue}")

if args.mode == 'mix':
    print("MIX !!!!!")
elif args.mode == 'lowest':
    print("LOWEST !!!!!")
elif args.mode == 'highest':
    print("HIGHEST !!!!!")