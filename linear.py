# -*- coding: utf-8 -*-
"""
Linearization Codec
"""
import re
from tree import Node, print_tree

class Name2Code(object):
	#inorder traverse
	def codec(self, tree, sVal):
		if isinstance(tree, Node):
			if tree.children:
				if len(tree.children) == 2:
					sVal = self.codec(tree.children[0], sVal)
					sVal = sVal+self.call_method(tree)
					sVal = self.codec(tree.children[1], sVal)
					#print sVal
				elif len(tree.children) == 1:
					sVal = self.codec(tree.children[0], sVal)
					#print sVal
				else:
					for elem in tree.children:
						sVal = self.codec(elem, sVal)
			else:
				sVal = sVal+self.call_method(tree)
				#print sVal
		else:
			print 'Unsupported Object Tree'
		return sVal
	#Traverse tree return strings
	def call_method(self, obj):
		#Retrieve tag from the dictionary
		stag = obj.name
		encode = self.codebook.get
		method = encode(stag)
		if method:
			return method(self, obj)
		else:
			return ''
	def do_den(self, obj):
		if obj.data.isdigit():
			#print obj.name+'is CN'
			return 'GROUPOPEN'+' '+'CN'+' '+'GROUPCLOSE'+' '
		else:
			#print obj.name+'is ID_VAR'
			return 'GROUPOPEN'+' '+'ID_VAR'+' '+'GROUPCLOSE'+' '
	def do_e(self, obj):
		if '=' in obj.data:
			var = obj.data.split('=')[1].strip()
			if var.isdigit():
				return 'EQUAL'+' '+'CN'+' '
			else:
				return 'EQUAL'+' '+'ID_VAR'+' '
		elif obj.data.isdigit():
			#print obj.name+'is CN'
			return 'CN'+' '
		elif not obj.data.isdigit():
			return 'ID_VAR'+' '
		else:
			return ' [TODO] '
	def do_f(self, obj):
		return 'DIV'+' '
	def do_nary(self, obj):
		return ''
	def do_num(self, obj):
		if obj.data.isdigit():
			#print obj.name+'is CN'
			return 'GROUPOPEN'+' '+'CN'+' '+'GROUPCLOSE'+' '
		else:
			#print obj.name+'is ID_VAR'
			return 'GROUPOPEN'+' '+'ID_VAR'+' '+'GROUPCLOSE'+' '
	def do_oMath(self, obj):
		return ''
	def do_r(self, obj):
		if '=' in obj.data:
			var = obj.data.split('=')[1].strip()
			if var.isdigit():
				return 'EQUAL'+' '+'CN'+' '
			else:
				return 'EQUAL'+' '+'ID_VAR'+' '
		elif obj.data.isdigit():
			#print obj.name+'is CN'
			return 'CN'+' '
		elif not obj.data.isdigit():
			return 'ID_VAR'+' '
		else:
			return ' [TODO] '
	def do_sSub(self, obj):
		return ''
	def do_BOsub(self, obj):
		return 'UNDEROPEN'+' '+'ID_VAR'+' '+'UNDERCLOSE'+' '
	def do_sub(self, obj):
		return 'SUBOPEN'+' '+'ID_VAR'+' '+'SUBCLOSE'+' '
	def do_Bind_OP(self, obj):
		return 'BIGSUM'+' '
	codebook = {  #Dictionary
		'<den>' : do_den,
		'<e>' : do_e,
		'<f>' : do_f,
		'<nary>' : do_nary,
		'<num>' : do_num,
		'<oMath>': do_oMath,
		'<r>' : do_r,
		'<sSub>' : do_sSub,
		'<sub>' : do_sub,
		'<BOsub>' : do_BOsub,
		'<Bind_OP>' : do_Bind_OP,
 	}
