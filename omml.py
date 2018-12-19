# -*- coding: utf-8 -*-
"""
Office Math Markup Language (OMML)
"""
import xml.etree.ElementTree as ET
from tree import Node, print_tree

OMML_NAMESPACE = '{http://schemas.openxmlformats.org/officeDocument/2006/math}'

class Tag2Method(object):

	#Found tags return strings
	def call_method(self, elem, stag=None):
		#Retrieve tag from the dictionary
		getmethod = Pr.tag2meth.get
		if stag is None:
			stag = elem.tag.replace(OMML_NAMESPACE, '')
		method = getmethod(stag)
		if method:
			return method(self, elem)
		else:
			return None

	#Process childrens of the element
	def process_children_list(self, elem, otree):
		for x in list(elem):
			if (OMML_NAMESPACE not in x.tag):  #Skip word tag
				continue
			stag = x.tag.replace(OMML_NAMESPACE, '')
			obj = self.call_method(x, stag=stag)
			if obj is None:
				continue
			else:
				otree.add_child(obj)

	#Directly retrieve the <m:t> contents
	def get_omml_math_text(self, elem):
		tag_name = '<'+elem.tag.replace(OMML_NAMESPACE, '')+'>'
		obj = None

		if tag_name == '<r>':
			tag_name = '<e>'
		for m in elem.iter(OMML_NAMESPACE+'t'):
			#print m
			#if m:
			if m.text:
				obj = Node(tag_name, m.text.encode('utf-8').strip())
			else:
				obj = Node(tag_name, '')
			#else:
			#	return None
		return obj

	#Retrieve the operator property
	def get_omml_operator_type(self, elem):
		for node in elem.iter(OMML_NAMESPACE+'chr'):
			nary_type = node.get(OMML_NAMESPACE+'val').encode('utf-8').strip()
			if nary_type:
				obj = Node('<Bind_OP>', nary_type)
				#print nary_type
			else:
				obj = Node('<Bind_OP>', '')
				print 'No Encode Found!!'
		return obj

	def set_math_elem(self, elem):
		for x in list(elem):
			if x.tag == OMML_NAMESPACE+'r':
				return self.get_omml_math_text(elem)
		return self.set_omml_tree(elem)

	#JASON modified code
	def set_omml_tree(self, elem):
		"""
		Grow the OMML tree 
		"""
		tag_name = '<'+elem.tag.replace(OMML_NAMESPACE, '')+'>'
		obj = Node(tag_name, '')
		if list(elem):
			self.process_children_list(elem, obj)
		return obj

	def process_unknown():
		return None


class Pr(Tag2Method):
	#The accent function
	def do_acc(self, elem):
		return self.set_omml_tree(elem)

	#The accent type
	def do_accPr(self, elem):
		return self.get_omml_operator_type(elem)

	#The 
	def do_bar(self, elem):
		"""
		The bar function
		"""
		return self.set_omml_tree(elem)
	#The 
	def do_barPr(self, elem):
		"""
		The bar type
		"""
		return self.get_omml_operator_type(elem)

	#The 
	def do_borderBox(self, elem):
		return None

	#The 
	def do_borderBoxPr(self, elem):
		return None

	#The 
	def do_box(self, elem):
		return None

	#The 
	def do_boxPr(self, elem):
		"""
		
		"""
		return None

	#The 
	def do_chr(self, elem):
		"""
		
		"""
		return None

	#The 
	def do_count(self, elem):
		"""
		
		"""
		return None

	#The 
	def do_d(self, elem):
		"""
		the delimiter object
		"""
		return None

	#The 
	def do_deg(self, elem):
		"""
		
		"""
		return None

	#The 
	def do_degHide(self, elem):
		"""
		
		"""
		return None

	#The 
	def do_den(self, elem):
		"""
		
		"""		
		return self.get_omml_math_text(elem)

	#The 
	def do_diff(self, elem):
		return None

	#The 
	def do_dPr(self, elem):
		return None

	#The element object
	def do_e(self, elem):
		return self.set_math_elem(elem)
	#The 
	def do_endChr():
		return None

	#The 
	def do_eqArr(self, elem):
		"""
		the Array object
		"""
		return None
	#The 
	def do_f(self, elem):
		"""
		the fraction object
		"""
		return self.set_omml_tree(elem)
		#print 'Found tag <f>'
	#The 
	def do_fName(self, elem):
		"""
		the func name
		"""
		return None
	#The 
	def do_func(self, elem):
		"""
		the Function-Apply object (Examples:sin cos)
		"""
		return None
	#The 
	def do_groupChr(self, elem):
		"""
		the Group-Character object
		"""
		return None
	#The 
	def do_grow(self, elem):
		return None
	#The 
	def do_lim(self, elem):
		"""
		the lower limit of the limLow object and the upper limit of the limUpp function
		"""
		return None
	#The
	def do_limLoc(self, elem):
		return None

	#The
	def do_limLow(self, elem):
		"""
		the Lower-Limit object
		"""
		return None

	#The 
	def do_limUpp(self, elem):
		"""
		the Upper-Limit object
		"""
		return None

	#The 
	def do_lit(self, elem):
		return None

	#The 
	def do_m(self, elem):
		"""
		the Matrix object
		"""
		return None

	#The 
	def do_mc(self, elem):
		return None

	#The 
	def do_mcPr(self, elem):
		return None

	#The 
	def do_mr(self, elem):
		"""
		a single row of the matrix m
		"""
		return None
	#The 
	def do_nary(self, elem):
		return self.set_omml_tree(elem)
	#The 
	def do_naryPr(self, elem):
		return self.get_omml_operator_type(elem)
	#The 
	def do_nor(self, elem):
		return None
	#The 
	def do_num(self, elem):
		return self.get_omml_math_text(elem)
	#The 
	def do_oMath(self, elem):
		return self.set_omml_tree(elem)
	#The 
	def do_oMathPara(self, elem):
		return self.set_omml_tree(elem)
	#The 
	def do_pos(self, elem):
		return None
	#The 
	def do_r(self, elem):
		return self.get_omml_math_text(elem)
	#The 
	def do_rad(self, elem):
		"""
		the radical object
		"""
		return self.set_omml_tree(elem)
	#The 
	def do_radPr(self, elem):
		return None
	#The 
	def do_sepChr(self, elem):
		return None
	#The 
	def do_smallFrac(self, elem):
		return None
	#The 
	def do_sPre(self, elem):
		"""
		the Pre-Sub-Superscript object -- Not support yet
		"""
		return None
	#The 
	def do_sPrePr(self, elem):
		return None
	#The 
	def do_sSub(self, elem):
		return self.set_omml_tree(elem)
	#The 
	def do_sSubPr(self, elem):
		return None
	#The 
	def do_sSubSub(self, elem):
		return None
	#The 
	def do_sSubSubPr(self, elem):
		return None
	#The 
	def do_sSup(self, elem):
		return self.set_omml_tree(elem)
	#The 
	def do_sSupPr(self, elem):
		return None
	#The subscript object
	def do_sub(self, elem):
		return self.get_omml_math_text(elem)
	def do_subHide(self, elem):
		return None
	#The superscript object  HAS ERROR [TODO]
	def do_sup(self, elem):
		return self.get_omml_math_text(elem)
	#The supHide
	def do_supHide(self, elem):
		return None
	#The math text object	
	def do_t(self, elem):
		return self.get_omml_math_text(elem)
	tag2meth = {  #Dictionary
		'acc' : do_acc,
		'accPr' : do_accPr,
		'bar' : do_bar,
		'barPr' : do_barPr,
		'borderBox' : do_borderBox,
		'borderBoxPr' : do_borderBoxPr,
		'box' : do_box,
		'boxPr' : do_boxPr,
		'chr' : do_chr,
		'count' : do_count,
		'd' : do_d,
		'deg' : do_deg,
		'degHide' : do_degHide,
		'den' : do_den,
		'diff' : do_diff,
		'dPr' : do_dPr,
		'e' : do_e,
		'endChr' : do_endChr,
		'eqArr' : do_eqArr,
		'f' : do_f,
		'fName' : do_fName,
		'func': do_func,
		'groupChr' : do_groupChr,
		'grow' : do_grow,
		'lim' : do_lim,
		'limLoc' : do_limLoc,
		'limLow' : do_limLow,
		'limUpp' : do_limUpp,
		'lit' : do_lit,
		'm' : do_m,
		'mc' : do_mc,
		'mcPr' : do_mcPr,
		'mr' : do_mr,
		'nary' : do_nary,
		'naryPr' : do_naryPr,
		'nor' : do_nor,
		'num' : do_num,
		'oMath': do_oMath,
		'oMathPara': do_oMathPara,
		'pos' : do_pos,
		'r' : do_r,
		'rad' : do_rad,
		'radPr' : do_radPr,
		'sepChr' : do_sepChr,
		'sPre' : do_sPre,
		'sSub' : do_sSub,
		'sSubSup' : do_sSubSub,
		'sSup' : do_sSup,
		'sub' : do_sub,
		'subHide' : do_subHide,
		'sup' : do_sup,
		'supHide' : do_supHide,		
		't' : do_t,
 	}