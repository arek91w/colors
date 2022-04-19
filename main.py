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
            try:
                hue = (g-b)/(max_v-min_v)
            except:
                hue = 2.1
                print('nie dziel przez zero')
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

        return mean([max_v, min_v])

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

'''
red_mean = int(round(mean(reds), 0))
green_mean = int(round(mean(greens), 0))
blue_mean = int(round(mean(blues), 0))
alpha_mean = int(round(mean(alphas), 0))

print(f"RED: {red_mean}")
print(f"GREEN: {green_mean}")
print(f"BLUE: {blue_mean}")
print(f"ALPHA: {alpha_mean}")

hex2 = my_col.rgba_to_hex(red_mean, green_mean, blue_mean, alpha_mean)

print(f"HEX: {hex2}")

hue = my_col.rgb_to_hue(red_mean, green_mean, blue_mean)
ligh = my_col.rgb_to_lightness(red_mean, green_mean, blue_mean)
sat = my_col.rgb_to_sat(red_mean, green_mean, blue_mean)
print(f"HUE: {hue}")
print(f"SATURATION: {sat}")
print(f"LIGHTNESS: {ligh}")
'''

if args.mode == 'mix':
    red_mean = int(round(mean(reds), 0))
    green_mean = int(round(mean(greens), 0))
    blue_mean = int(round(mean(blues), 0))
    alpha_mean = int(round(mean(alphas), 0))
    hex2 = my_col.rgba_to_hex(red_mean, green_mean, blue_mean, alpha_mean)
    hue = my_col.rgb_to_hue(red_mean, green_mean, blue_mean)
    ligh = my_col.rgb_to_lightness(red_mean, green_mean, blue_mean)
    sat = my_col.rgb_to_sat(red_mean, green_mean, blue_mean)

    print(f"RED: {red_mean}")
    print(f"GREEN: {green_mean}")
    print(f"BLUE: {blue_mean}")
    print(f"ALPHA: {alpha_mean}")
    print(f"HEX: {hex2}")
    print(f"HUE: {hue}")
    print(f"SATURATION: {sat}")
    print(f"LIGHTNESS: {ligh}")

elif args.mode == 'lowest':
    red_low = int(round(min(reds), 0))
    green_low = int(round(min(greens), 0))
    blue_low = int(round(min(blues), 0))
    alpha_low = int(round(min(alphas), 0))
    hex2 = my_col.rgba_to_hex(red_low, green_low, blue_low, alpha_low)
    hue = my_col.rgb_to_hue(red_low, green_low, blue_low)
    ligh = my_col.rgb_to_lightness(red_low, green_low, blue_low)
    sat = my_col.rgb_to_sat(red_low, green_low, blue_low)

    print(f"RED: {red_low}")
    print(f"GREEN: {green_low}")
    print(f"BLUE: {blue_low}")
    print(f"ALPHA: {alpha_low}")
    print(f"HEX: {hex2}")
    print(f"HUE: {hue}")
    print(f"SATURATION: {sat}")
    print(f"LIGHTNESS: {ligh}")

elif args.mode == 'highest':
    red_high = int(round(max(reds), 0))
    green_high = int(round(max(greens), 0))
    blue_high = int(round(max(blues), 0))
    alpha_high = int(round(max(alphas), 0))
    hex2 = my_col.rgba_to_hex(red_high, green_high, blue_high, alpha_high)
    hue = my_col.rgb_to_hue(red_high, green_high, blue_high)
    ligh = my_col.rgb_to_lightness(red_high, green_high, blue_high)
    sat = my_col.rgb_to_sat(red_high, green_high, blue_high)

    print(f"RED: {red_high}")
    print(f"GREEN: {green_high}")
    print(f"BLUE: {blue_high}")
    print(f"ALPHA: {alpha_high}")
    print(f"HEX: {hex2}")
    print(f"HUE: {hue}")
    print(f"SATURATION: {sat}")
    print(f"LIGHTNESS: {ligh}")

elif args.mode == 'mix-saturate':
    red_high = int(round(max(reds), 0))
    green_high = int(round(max(greens), 0))
    blue_high = int(round(max(blues), 0))
    alpha_high = int(round(max(alphas), 0))
    hex2 = my_col.rgba_to_hex(red_high, green_high, blue_high, alpha_high)
    hue = my_col.rgb_to_hue(red_high, green_high, blue_high)
    ligh = my_col.rgb_to_lightness(red_high, green_high, blue_high)
    sat = my_col.rgb_to_sat(red_high, green_high, blue_high)

    print(f"RED: {red_high}")
    print(f"GREEN: {green_high}")
    print(f"BLUE: {blue_high}")
    print(f"ALPHA: {alpha_high}")
    print(f"HEX: {hex2}")
    print(f"HUE: {hue}")
    print(f"SATURATION: {sat}")
    print(f"LIGHTNESS: {ligh}")