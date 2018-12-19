from bs4 import BeautifulSoup as BS
import xml.etree.ElementTree as ET
import re
"""
#tree = ET.parse('xmltest.xml')
tree = ET.parse('document.xml')
root = tree.getroot()
print tree
#print root.tag
#print root.attrib
#Visit child nodes of root
for child in root:
	print(child.tag, child.attrib)
for me in root.findall('m:oMath'):
	e = me.find('m:t').text
	print(e)
"""
#f = open('document.xml', 'r')
#print f.read()
#tree = ET.parse('document.xml')
"""
x = re.sub('<[^>]*>', '', f)  # you can also use re.sub('<[A-Za-z\/][^>]*>', '', tree)
print '\n'.join(x.split())
"""
#print div
#children = divs[0].contents
#my_data = divs[0].string + divs[1].string
#print my_data  #some text here even more text
#Test with BeautifulSoup
"""
line='<m:t>x+y=z</m:t>'
soup = BS(line, "html.parser")
print soup.find('m:t').text
"""
def indent(elem, level=0):
    i = "\n" + level*"  "
    j = "\n" + (level-1)*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem        
str
#indent(root)
ET.dump(root)
#Finidng interesting elements
#print root.find('.//t').text
for me in root.findall(".//*[tag='m:t']"):
	e = me.text
	print e