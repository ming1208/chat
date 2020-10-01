def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None
    allen_wd_ct = 0
    allen_stkr_ct = 0
    allen_img_ct = 0
    viki_wd_ct = 0
    viki_stkr_ct =0
    viki_img_ct = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] =='貼圖':
                allen_stkr_ct += 1
            elif s[2] == '圖片':
                 allen_img_ct += 1
            else:
                for m in s[2:]:
                    allen_wd_ct += len(m)

        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_stkr_ct += 1
            elif s[2] == '圖片':
                 viki_img_ct += 1
            else:
                for m in s[2:]:
                    viki_wd_ct += len(m)
    print('Allen說了',allen_wd_ct, '個字')
    print('Allen傳了',allen_stkr_ct, '個貼圖')
    print('Allen傳了',allen_img_ct, '張圖片')
    
    print('Viki說了',viki_wd_ct, '個字')
    print('Viki傳了',viki_stkr_ct, '個貼圖')
    print('Viki傳了',viki_img_ct, '張圖片')
    # return new

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    # write_file('output.txt', lines)

main()
