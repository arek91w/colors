#!/usr/bin/env python3

import argparse
from statistics import mean
from color import Color


if __name__ == '__main__':

    # command line arguments

    parser = argparse.ArgumentParser()
    parser.add_argument('integers', metavar='string1', type=str, nargs='?', help='string for process')
    parser.add_argument("-m", "--mode", nargs="?", help="select mode", type=str)

    args = parser.parse_args()

    my_col = Color()

    if args.integers == None:
        file_lines = my_col.load_file()
    else:
        file_lines = [args.integers]


    first_format_colors = my_col.check_first_format(file_lines)

    for s in my_col.check_second_format(file_lines):
        try:
            word = ''
            red = int(s[0])
            green = int(s[1])
            blue = int(s[2])
            alpha = int(s[3])
            col_hex = my_col.rgba_to_hex(red, green, blue, alpha)[1:]
            first_format_colors.append(col_hex)
        except:
            pass

    for f in first_format_colors:
        print(f'color found: {f}')

    print('---------------')
    print('---------------')

    reds = []
    greens = []
    blues = []
    alphas = []

    for col in first_format_colors:
        red = col[0:2]
        green = col[2:4]
        blue = col[4:6]
        alpha = col[6:8]

        reds.append(int(red, 16))
        greens.append(int(green, 16))
        blues.append(int(blue, 16))
        alphas.append(int(alpha, 16))


    # mix mode
    if args.mode == 'mix' or args.mode == None:
        try:
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
            print(f"HUE: {round(hue, 2)}")
            print(f"SATURATION: {round(sat, 2)}")
            print(f"LIGHTNESS: {round(ligh, 2)}")
        except:
            print('no valid DATA')

    # lowest mode
    elif args.mode == 'lowest':
        try:
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
            print(f"HUE: {round(hue, 2)}")
            print(f"SATURATION: {round(sat, 2)}")
            print(f"LIGHTNESS: {round(ligh, 2)}")
        except:
            print('no valid DATA')

    # highest mode
    elif args.mode == 'highest':
        try:
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
            print(f"HUE: {round(hue, 2)}")
            print(f"SATURATION: {round(sat, 2)}")
            print(f"LIGHTNESS: {round(ligh, 2)}")
        except:
            print('no valid DATA')

    elif args.mode == 'mix-saturate':
        try:
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
            print(f"HUE: {round(hue, 2)}")
            print(f"SATURATION: {round(sat, 2)}")
            print(f"LIGHTNESS: {round(ligh, 2)}")
        except:
            print('no valid DATA')