from lxml import etree

xml = """
<book>
    <name>张三</name>
    <title>少年张三丰</title>
    <size>55</size>
    <sex>男</sex>
    <other>
        <name>李四</name>
        <auth>admin</auth>
        <page>33</page>
        <goods>
            <name>不值钱</name>
        </goods>
    </other>
    <hehe>
        <name>老王</name>
    </hehe>
</book>
"""

tree = etree.XML(xml)
# /表示层级关系，第一个/代表根节点
result = tree.xpath("/book")
# test()是获取文本
result = tree.xpath("/book/name/text()")
# //表示遍历上面节点下的所有name节点
result = tree.xpath("/book//name/text()")
# /*/标书这个节点任意名称下的name节点
result = tree.xpath("/book/*/name/text()")
print(result)

##################################################################################

tree = etree.parse("./html/xpath.html")

# [1]表示取第一个
result = tree.xpath("/html/body/ul/li[1]/text()")
# [@]表示根据属性条件取值
result = tree.xpath("/html/body/ol/li/a[@href='http://www.sougou.com']/text()")

result = tree.xpath("/html/body/ol/li")
for it in result:
    # ./相对查找 相对与 li
    name = it.xpath("./a/text()")
    print(name)
    # 取属性的值
    name = it.xpath("./a/@href")
    print(name)

result = tree.xpath("/html/body/ol/li/a/@href")
print(result)

# 在谷歌浏览器上可以通过F12 直接拿到xpath
