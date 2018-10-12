#coding=utf-8
import re

origin = open("/Users/xuyi/Desktop/timi")
question = []
subject = []
p = re.compile(u'(^\d+\.+)')
p2 = re.compile(r'((\(+\d+)|(\d+~\d+))')
p3 = re.compile(u'((\s+)|(\(+\d+)|(\d+~\d+))')
p4 = re.compile(r'(C+)')
p5 = re.compile(r'\s+[A-E]{2,4}\s+')

def isBegin(str):
    """
    :type str: str
    :return:
    """
    if p.match(str):
        return True
    else:
        return False

def isSubjectBegin(str):
    if p2.match(str):
        return True
    else:
        return False

def isSubjectEnd(str):
    str = str.decode('utf-8')
    if p3.match(str):return True
    else: return False

def isSpace(str):
    if p4.search(str):
        return False
    else:
        return True

def isMuti(str):
    if p5.search(str):
        return True
    else:
        return False


content = ''
subjectBegin = False
for line in origin.readlines():
    if isSubjectBegin(line):
        question.append(content)
        content = line
        subjectBegin = True
    elif isSubjectEnd(line):
        question.append(content)
        content = line
        subjectBegin = False
    elif isBegin(line) and not subjectBegin:
        question.append(content)
        content = line
    else:
        content += line

if len(content) >0:
    question.append(content)


subject, space, choose, muti = [], [], [], []
for q in question:
    if isSubjectBegin(q):
        subject.append(q)
    elif isSpace(q):
        space.append(q)
    elif isMuti(q):
        muti.append(q)
    else:
        choose.append(q)


wpath = unicode('/Users/xuyi/Desktop/选择.txt', 'utf-8')
w = open(wpath, "w")
w.write('\n'.join(choose))
m = open(u"/Users/xuyi/Desktop/多选.txt", "w")
m.write('\n'.join(muti))
s = open(u"/Users/xuyi/Desktop/题干.txt", "w")
s.write('\n'.join(subject))
sp = open(u"/Users/xuyi/Desktop/填空.txt", "w")
sp.write('\n'.join(space))

# str = '(adsf'
# print isSubjectEnd(str)

# str = '1231..'
# str1 = 'asdfaf'
# str2 = '12313asdf'
# print isBegin(str)
# print isBegin(str1)
# print isBegin(str2)
#
# print '*********************'
# str3 = '(1213'
# str4 = '('
# print isBegin(str3)
# print isBegin(str4)
