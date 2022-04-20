import argparse
from statistics import mean
from color import Color

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mode", help="select mode", type=str)

args = parser.parse_args()

my_col = Color()
file_lines = my_col.load_file()


first_format_colors = my_col.check_first_format(file_lines)

for s in my_col.check_second_format(file_lines):
    try:
        word = ''
        red = int(s[0])
        green = int(s[1])
        blue = int(s[2])
        alpha = int(s[3])
        print(f'{red, green, blue, alpha}')
        col_hex = my_col.rgba_to_hex(red, green, blue, alpha)[1:]
        print(f'{col_hex}, XXXXXXXXX')
        first_format_colors.append(col_hex)
    except:
        print('invalid format')

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