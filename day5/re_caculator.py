# Author: zzk


import re


def caculate(arith, form):
    """计算。parameter:
    arith: '/'或'*'或'-'或'+'
    form: 算式字符串"""
    # 匹配相应算术格式的算式并分组，其数可能为负
    p_arith = re.compile(r'([\-]?[0-9.]+)[%s]([\-]?[0-9.]+)' % (arith))
    while True:
        try:
            form_match = p_arith.search(form)
            if arith == '/':
                res = float(form_match.group(1))/float(form_match.group(2))
            elif arith == '*':
                res = float(form_match.group(1))*float(form_match.group(2))
            elif arith == '-':
                res = float(form_match.group(1))-float(form_match.group(2))
            else:
                res = float(form_match.group(1))+float(form_match.group(2))
            form = p_arith.sub(str(res), form, count=1)
        except AttributeError:
            # print(form)
            return form


FORMULAS = input('请输入算式：').strip()
# FORMULAS = '1-2*((60 - 30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'.strip()
FORMULAS = re.sub('[ \t\r\n]+', '', FORMULAS)  # 去除所有空格和换行符
p_brackets = re.compile(r'[(]([0-9+\-*/.]+)[)]')
p_subtraction = re.compile(r'(\d)-(\d)')
while True:
    while True:  # 在减号前加个加号防止符号消失
        try:
            temp = p_subtraction.search(FORMULAS)
            FORMULAS = p_subtraction.sub(temp.group(
                1)+'+-'+temp.group(2), FORMULAS, count=1)
        except AttributeError:
            break
    try:  # 最短括号匹配
        form_in_brackets = p_brackets.search(FORMULAS).group(1)
        print(form_in_brackets)
        for arith in '/*-+':
            form_in_brackets = caculate(arith, form_in_brackets)
        FORMULAS = p_brackets.sub(form_in_brackets, FORMULAS, count=1)
    except AttributeError:
        for arith in '/*-+':
            FORMULAS = caculate(arith, FORMULAS)
        print('结果为：', FORMULAS)
        break
