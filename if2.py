s1 = 'learn'
s2 = 'python'

def lines(s1, s2):
    if (type(s1) == str) & (type(s2) == str):
        return '0'
    elif s1 == s2:
        return '1'
    elif s1 != s2 and len(s1) > len(s2):
        return '2'
    elif s1 != s2 and s2 == 'learn':
        return '3'
    else:
        return 'Условие не выполнено'

print(lines('python', 'learn'))
print(lines('data', 'none'))
print(lines('512', 'none'))