"""
import compiler
def test():
	fin = open('input.txt', 'r')
	re = fin.readline()
	#print f
	#print re
	eq = "sin(x)*x**2"
	ast = compiler.parse( eq )
	print ast
		for line in list:
			if line[0] in years_dict:
				# append the new number to the existing array at this slot
				d[line[0]].append(line[1])
			else:
				# create a new array in this slot
				d[line[0]] = [line[1]]
"""
class MEdict():
	def __init__(self):
		self.d = dict()
	def addME(self, idx, me):
		self.d[idx] = me
	def delME(self, key):
		tmp = self.d[key]
		del self.d[key]
		print "The mathematical element at index %s is removed" % key
		if key in self.d:
			print "The mathematical element at index %s is not removed" % key
		else:
			print "The mathematical element at index %s is successfully removed" % key
if __name__=="__main__":
	a = MEdict()
	a.addME('1','sin')
	print "The mathematical element at index %s is %s" % ('1', a.d['1'])
	a.delME('1')