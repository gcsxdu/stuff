blanks_per_tab = 6
cnt = 1
count_flag = False

with open('des.txt', 'w+') as f_des:
    f_des.write('"name": {\n\t"prefix": "prefix",\n\t"body": [\n')
    with open('src.txt') as f_src:
        lines = f_src.readlines()
        for line in lines:
            s = '"'
            for i in range(len(line)):
                if line[i] == "\\": #遇到反斜杠，得转义一下
                    s += '\\\\'
                elif line[i] == "\n": #末尾的回车键不管
                    continue
                elif line[i] == "}":
                    if i > 0 and line[i-1] == '{' and count_flag:
                        s += "$"+str(cnt)
                        cnt += 1;
                    s += "}"
                else:
                    s += line[i]
            s += '", \n'
            s = "\t\t"+s.replace(" "*blanks_per_tab, "\\t") #统一处理tab键，空格数视情况而定
            f_des.write(s)

    f_des.write('\t],\n\t"description": "discription"\n}')
