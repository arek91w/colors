import argparse
from statistics import mean

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

    def rgb_to_lightness(self, r, g, b):
        
        r = int(r)/255
        g = int(g)/255
        b = int(b)/255
        max_v = max(r, g, b)
        min_v = min(r, g, b)

        return max_v - min_v

    def rgb_to_sat(self, r, g, b):
        
        r = int(r)/255
        g = int(g)/255
        b = int(b)/255
        max_v = max(r, g, b)
        min_v = min(r, g, b)

        if max_v - min_v < 0.5:
            return (max_v - min_v) / (max_v + min_v)
        else:
            return (max_v - min_v) / (2 - max_v - min_v)

    def rgba_to_hex(self, r, g, b , a):
        r_hex = hex(int(r))
        g_hex = hex(int(g))
        b_hex = hex(int(b))
        a_hex = hex(int(a))

        return '#' + r_hex[-2:] + g_hex[-2:] + b_hex[-2:] + a_hex[-2:]

my_col = Color()
file_lines = my_col.load_file()


first_format_colors = my_col.check_first_format(file_lines)

reds = []
greens = []
blues = []
alphas = []

for col in first_format_colors:
    print(col)
    print('______________')
    red = col[0:2]
    green = col[2:4]
    blue = col[4:6]
    alpha = col[6:8]

    reds.append(int(red, 16))
    greens.append(int(green, 16))
    blues.append(int(blue, 16))
    alphas.append(int(alpha, 16))

print(f"RED: {int(round(mean(reds), 0))}")
print(f"GREEN: {int(round(mean(greens), 0))}")
print(f"BLUE: {int(round(mean(blues), 0))}")
print(f"ALPHA: {int(round(mean(alphas), 0))}")

hex = my_col.rgba_to_hex(round(mean(reds), 0), round(mean(greens), 0), round(mean(blues), 0), round(mean(alphas), 0))

print(f"HEX: {hex}")
'''
hue = my_col.rgb_to_hue(int(red, 16), int(green, 16), int(blue, 16))
ligh = my_col.rgb_to_lightness(int(red, 16), int(green, 16), int(blue, 16))
sat = my_col.rgb_to_sat(int(red, 16), int(green, 16), int(blue, 16))
print(f"HUE: {hue}")
print(f"SATURATION: {sat}")
print(f"LIGHTNESS: {ligh}")
'''
if args.mode == 'mix':
    print("MIX !!!!!")
elif args.mode == 'lowest':
    print("LOWEST !!!!!")
elif args.mode == 'highest':
    print("HIGHEST !!!!!")