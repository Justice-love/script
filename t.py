import re
p4 = re.compile(r'(A\.)')
p5 = re.compile(r'[A-Za-z]{2,*}')

str = 'asdfasdfA.'
if p5.search(str):
    print True
