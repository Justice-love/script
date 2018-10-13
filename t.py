#coding=utf-8
import re
p4 = re.compile(r'(A\.)')
p5 = re.compile(r'\s+[A-E]{2,4}\s+')
p6 = re.compile(r'(\(\s+[A-E]\s+\))')

str = 'asdfasdfA.'
if p5.search(str):
    print True

str = u'6.男婴，6个月。因呕吐腹泻3天，加剧一天，尿少来院急诊，体温38℃，眼窝前囟显凹，皮肤弹性较差，血Na + 140mmol/L，动脉血气:pH7.2， BE 12mmol/L。最适宜处理是( E )'

def isMuti(str):
    if p5.search(str) and not p6.search(str):
        return True
    else:
        return False


print isMuti(str)

print p6.search(str)
