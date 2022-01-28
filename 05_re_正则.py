import re

# 匹配字符串中的所有内容 ，返回list
data1 = re.findall(pattern=r"\d+", string="移动电话10086，电信电话10010")
for it in data1:
    print(it)
print()

# 匹配字符串中的所有内容 ，返回 迭代器 从迭代器拿内容需要group()
data2 = re.finditer(pattern=r"\d+", string="移动电话10086，电信电话10010")
for it in data2:
    print(it.group())
print()

# 从头开始匹配，匹配不到报错。返回match对象 拿内容需要group()
data3 = re.match(pattern=r"\d+", string="10086，电信电话10010")
print(data3.group())
print()

# 只匹配一个， 返回match对象 拿内容需要group()
data4 = re.search(pattern=r"\d+", string="移动电话10086，电信电话10010")
print(data3.group())
print()

# 预加载正则表达式
obj = re.compile(pattern=r"\d+")
data5 = obj.finditer(string="移动电话10086，电信电话10010")
for it in data5:
    print(it.group())
print()

htmlStr = """
<div class='gc'><span id='爬虫'>郭超</span></div>
<div class='lyf'><span id='3'>刘亦菲</span></div>
<div class='ldh'><span id='4'>刘德华</span></div>
<div class='zjl'><span id='5'>周杰伦</span></div>
<div class='wbq'><span id='6'>王宝强</span></div>
<div class='cc'><span id='7'>成才</span></div>
"""

# (?P<分组名称>正则) 可以从正则匹配的内容中进一步的提取数据    re.S 让 . 能匹配到换行
obj2 = re.compile(r"<div class='(?P<class>.*?)'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>", re.S)
data6 = obj2.finditer(htmlStr)
for it in data6:
    print(f"class={it.group('class')},id={it.group('id')},name={it.group('name')}")
