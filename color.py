from statistics import mean

class Color():


    #loading file
    def load_file(self):
        try:
            with open('colors.txt') as f:
                return f.readlines()
        except:
            print('cant read the file')
            return 'xx'

    # function exctracting colors from format e.g #ff002244
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

    # function exctracting colors from format e.g 122,1, 3, 44
    def check_second_format(self, lines):  
        for line in lines:
            comm_arr = [pos for pos, char in enumerate(line) if char == ',']
            if len(comm_arr) >= 3:

                # sprawdz limit odstepow
                for i in range(len(comm_arr)):

                    triple_comb_arr = []
                    for j in range(i, i+3):
                        triple_comb_arr.append(comm_arr[j])
                        if j == len(comm_arr) - 1:
                            break
                    space_arr = [j-i for i, j in zip(triple_comb_arr[:-1], triple_comb_arr[1:])]
                    try:
                        if space_arr[0] <= 5 and space_arr[1] <= 5:
                            if triple_comb_arr[0] > 3:
                                red_v = line[triple_comb_arr[0]-4:triple_comb_arr[0]]
                            else:
                                red_v = line[0:triple_comb_arr[0]]
                            green_v = line[triple_comb_arr[1]-3:triple_comb_arr[1]]
                            blue_v = line[triple_comb_arr[2]-3:triple_comb_arr[2]]
                            alpha_v = line[triple_comb_arr[2]+1:triple_comb_arr[2]+5]
                            red_v = self.sort_back(red_v)
                            green_v = self.sort_back(green_v)
                            blue_v = self.sort_back(blue_v)
                            alpha_v = self.sort_forw(alpha_v)
                            rgba = (red_v, green_v, blue_v, alpha_v)
                            yield rgba
                    except:
                        rgba = None
                        yield rgba
                


                if i == len(comm_arr) - 3:
                    break
            # sprawdz czy znaki sa liczbami lub spacja
        else:
            pass
    
    # filtering second format strings (backward)
    def sort_back(self, s):
        int_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        new_s = s[-1]
        for c in reversed(s[:-1]):
            if c not in int_set:
                break
            new_s = c + new_s
        return new_s

    # filtering second format strings (forward)
    def sort_forw(self, s):
        int_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        new_s = s[0]
        for c in (s[1:]):
            if c not in int_set:
                break
            new_s = new_s + c
        return new_s
    
    # converting rgb to hue
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

    # converting rgb to lightness
    def rgb_to_lightness(self, r, g, b):
        
        r = int(r)/255
        g = int(g)/255
        b = int(b)/255
        max_v = max(r, g, b)
        min_v = min(r, g, b)

        return mean([max_v, min_v])

    # converting rgb to saturation
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

    # converting rgba to hex
    def rgba_to_hex(self, r, g, b , a):

        r_hex = hex(int(r))
        r_hex = r_hex[2:]
        if len(r_hex) == 1:
            r_hex = '0' + r_hex
        g_hex = hex(int(g))
        g_hex = g_hex[2:]
        if len(g_hex) == 1:
            g_hex = '0' + g_hex
        b_hex = hex(int(b))
        b_hex = b_hex[2:]
        if len(b_hex) == 1:
            b_hex = '0' + b_hex
        a_hex = hex(int(a))
        a_hex = a_hex[2:]
        if len(a_hex) == 1:
            a_hex = '0' + a_hex

        return '#' + r_hex + g_hex + b_hex + a_hex