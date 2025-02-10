# import re
# p=re.compile('[a-z]+')
# m=p.match("python")
# print(m)

# import re
# p = re.compile(정규표현식)
# m = p.match( '조사할 문자열' )
# if m:
#     print('Match found: ', m.group())
# else:
#     print('No match')

#import re
# p = re.compile('[a-z]+')  # 소문자 알파벳 하나 이상 매치
# result = p.finditer("life is too short")
# print(result)

# for r in result: print(r)
# import re
# p = re.compile('[a-z]+')
# m = p.match("python")
# print(m.group())
# print(m.start())
# print(m.end())
# print(m.span())

# import re
# p = re.compile('[a-z]+')
# m = p.search("3 python")
# print(m.group())
# print(m.start())
# print(m.end())
# print(m.span())
# import re
# p = re.compile('a.b')
# m = p.match('a\nb')
# print(m)# 
# import re
# p = re.compile('a.b', re.DOTALL)
# m = p.match('a\nb')
# print(m)
# import re
# p = re.compile('[a-z]+', re.I)
# print(p.match('python'))
# print(p.match('Python'))
# print(p.match('PYTHON'))


# import re
# p = re.compile("^python\\s\\w+")  # 정규 표현식 정의
# data = """python one
# life is too short
# python two
# you need python
# python three"""
# print(p.findall(data))  # 매칭된 결과 출력


# import re
# p = re.compile("^python\s\w+", re.MULTILINE)  # MULTILINE 옵션 추가
# data = """python one
# life is too short
# python two
# you need python
# python three"""
# print(p.findall(data))

import re

charref = re.compile(r"""
    &[#]            # Start of a numeric entity reference
    (
        0[0-7]+     # Octal form (0으로 시작하는 8진수)
        | [0-9]+    # Decimal form (10진수)
        | x[0-9a-fA-F]+  # Hexadecimal form (x로 시작하는 16진수)
    )
    ;               # Trailing semicolon
""", re.VERBOSE)
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

import re

charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')