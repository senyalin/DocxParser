#The Data structure for a paragraph in the paper
class paragraph(object):
	def set_text(self, text_content):
		self.text = text_content

	def set_math(self, math_content):
		self.math = math_content
class section(paragraph):
	def set_number(self, sect_number):
		self.sect = sect_number
#TEST CODE
"""
if __name__=="__main__":
	x = paragraph()
	x.set_text('Yes')
	x.set_math(1)
	l = []
	l.append(x)
	y = section()
	y.set_number(2)
	y.set_text('No')
	l.append(y)
	print l[0].text+' '
	print l[1].text
"""