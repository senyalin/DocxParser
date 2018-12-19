# -*- coding: utf-8 -*-
try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML
from lxml import etree
from omml import Tag2Method
from paper import paragraph
from tree import Node, print_tree, save_tree
from linear import Name2Code
import zipfile
import inspect
import tree
"""
Module that extract text from MS XML Word document (.docx).
(Inspired by python-docx <https://github.com/mikemaccana/python-docx>)
"""
#===========================================================================================
WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
OMML_NAMESPACE = '{http://schemas.openxmlformats.org/officeDocument/2006/math}'
DOCXML_ROOT = ''.join(('<w:document '
			,'xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" '
			,'xmlns:cx="http://schemas.microsoft.com/office/drawing/2014/chartex '
			,'xmlns:cx1="http://schemas.microsoft.com/office/drawing/2015/9/8/chartex" '
			,'xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" '
			,'xmlns:o="urn:schemas-microsoft-com:office:office" '
			,'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
			,'xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" '
			,'xmlns:v="urn:schemas-microsoft-com:vml" '
			,'xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" '
			,'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
			,'xmlns:w10="urn:schemas-microsoft-com:office:word" '
			,'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
			,'xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" '
			,'xmlns:w15="http://schemas.microsoft.com/office/word/2012/wordml" '
			,'xmlns:w16se="http://schemas.microsoft.com/office/word/2015/wordml/symex"'
			,'xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup"'
			,'xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk"'
			,'xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml"'
			,'xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" mc:Ignorable="w14 w15 w16se wp14">'
			,'{0}</w:document>'
		))
#===========================================================================================
def get_docx_xml(fname):
	with open(fname,'rb') as f:
		peek = f.read(4)
	#zip file
	if peek != b"PK\x03\x04":
		raise IOError("%s not a valid file" % filename)
	zf = zipfile.ZipFile(fname)
	xml_stream = zf.open('word/document.xml') #The pointer of xml
	zf.close()
	return xml_stream

def output_xml(fname, xml_content):
	#The content of xml
	root = etree.fromstring(xml_content)
	xmlstr = etree.tostring(root, pretty_print=True)
	with open(fname, "w") as f:
		f.write(xmlstr.encode('utf-8'))

def save_results(fname, content_list):
	cluster_name = 'Group'
	idx = 0
	f = open(fname, mode='wt')
	for x in content_list:
		idx+=1
		f.write(cluster_name+'\t')
		f.write('%d' % idx)
		print x
		f.write(': '+x.encode('utf-8')+'\n')
	f.close()

def find_omml_tag(PARA):
	omml_chars = Tag2Meth()
	for elem in PARA.iter():
		elem

def get_childrens(elem, tmp):
	#TRY something
	ptag = '<'+elem.tag.replace(OMML_NAMESPACE, 'm:').replace(WORD_NAMESPACE, 'w:')+'>'

	if len(list(elem)):
		"""
		print 'The node '+ptag+' has childrens: '
		for node in elem:
			print '<'+node.tag.replace(OMML_NAMESPACE, 'm:').replace(WORD_NAMESPACE, 'w:')+'>'
		print '\n'
		"""
		for node in elem:
			stag = '<'+node.tag.replace(OMML_NAMESPACE, 'm:').replace(WORD_NAMESPACE, 'w:')+'>'
			tmp.append(stag)
			print stag
			if '<m:chr>' in stag:
				print node.get(OMML_NAMESPACE+'val').encode('utf-8').strip()
			get_childrens(node, tmp)
	else:
		pass
		"""
		print 'The node '+ptag+' has no childrens. '
		print '\n'
		"""
"""
		if not list(elem):
			print 'The path:'
			print tmp
			print '\n'
"""
#Get mathematical tags
def get_docx_tags(xml_content):
    tree = XML(xml_content) 
    """
    Collect the contents of all tags
    """
    ctags = []
    all_tags = []

    pgh = Tag2Method()
    for paragraph in tree.iter(WORD_NAMESPACE+'p'):
    	for elem in paragraph.iter():
    		#pgh.call_method(elem)
    		#print elem
    		if WORD_NAMESPACE in elem.tag:
    			pass
    		else:
    			ctags.append('<'+elem.tag.replace(OMML_NAMESPACE, 'm:')+'>')
    			#print ctags
        if ctags:
            all_tags.append(' '.join(ctags))
        else:
        	all_tags.append('[No math tags in this cluster]')
        ctags = []
    	#print 'END of Paragraph'
    return all_tags

#Get mathematical texts
def get_docx_math(xml_content):
    tree = XML(xml_content)
    display_zone = OMML_NAMESPACE+'oMathPara'
    inline_zone = OMML_NAMESPACE+'oMath'
    """
    Collect the contents of outline mathematical zone
    """
    math_zones = []
    math_zone = []
    for paragraph in tree.iter(WORD_NAMESPACE+'p'):    	
        for node in paragraph.iter(OMML_NAMESPACE+'t'):
        	if node.text:
        		math_zone.append(node.text)
        if math_zone:
            math_zones.append(' '.join(math_zone)) #Temporarly join all the <m:t> parts
        else:
        	math_zones.append('[No math in this cluster]')
        math_zone = []
    return math_zones

#Get non-mathematical texts
def get_docx_text(xml_content):
    """
    Take the path of a docx file as argument, return the text in unicode.
    """
    tmp = Tag2Method()
    childs = []

    tree = XML(xml_content)
    pctr = 0
    maths = []
    paragraphs = []
    for paragraph in tree.iter(WORD_NAMESPACE+'p'):
        texts = [node.text
                 for node in paragraph.iter(WORD_NAMESPACE+'t')
                 if node.text]
        if texts:
            paragraphs.append(''.join(texts))
            pctr = pctr + 1
        else:
        	paragraphs.append('[No text in this cluster]')
        	pctr = pctr + 1
        for mzone in paragraph.iter(OMML_NAMESPACE+'t'):
        	if mzone.text and pctr == 3:
        		maths.append(mzone.text)
    return paragraphs

def update_tree(ptr, is_root=False):
    #Process children list
    if not is_root:
        for child in ptr:
            if isinstance(child, Node):
            	if child.name in '<nary>':
            		update_sub(child)
                #print child.name+': '+child.data
                if child.children:
                    update_tree(child.children)
                else:
                    continue
    #Process the root
    else:
        if isinstance(ptr, Node):
            #print ptr.name+': '+ptr.data
            if ptr.children:
                update_tree(ptr.children)
    return ptr

def update_sub(x):
	#print [x.children.name]
	for elem in x.children:
		if elem.name in '<sub>':
			elem.name = '<BOsub>'

def test_omml_tree(xml_content):
	#get_childrens(paragraph, [])
	obj = Tag2Method()
	codeObj = Name2Code()
	f = []
	tree = XML(xml_content)
	display_zone = OMML_NAMESPACE+'oMathPara'
	inline_zone = OMML_NAMESPACE+'oMath'
	f_zone = OMML_NAMESPACE+'f'
	print 'START PARSE'
	for elem in tree.iter(inline_zone):
		tmp = obj.call_method(elem)
		#print tmp
	print 'END PARSE'
	new_tmp = update_tree(tmp, True) #temporary method
	print_tree('', new_tmp, True)
	save_tree(f, '', new_tmp, True)
	sss = codeObj.codec(new_tmp, '')
	print sss
	f = open('results/linear_code.txt', mode='wt')
	f.write(sss)
	f.close
		#print_tree(tmp)
	#	print obj.call_method(elem)
	#test children list function
    #childs = tmp.process_children_list(paragraph)
    #for i in childs:
    #	print i
    #print childs
#[TODO] Linearize the tree into code
def test_group(all_xml):
	opath = 'output.xml'
	epath = 'results/elems.txt'
	tpath = 'results/texts.txt'
	mpath = 'results/maths.txt'

	#[TODO]
	pghs = [] #initialize a list of objects that contains all paragraphs in the article
	#print 'Math Elements:\n'
	#get_docx_math(str)
	output_xml(opath, all_xml)
	#print '\nMath Elements:\n', get_docx_math(str)
	#print PARA
	etext = get_docx_tags(all_xml)
	ttext = get_docx_text(all_xml)
	mtext = get_docx_math(all_xml)
	print 'Tags part segmentation complete!!'
	save_results(epath, etext)
	print 'Textual part segmentation complete!!'
	save_results(tpath, ttext)
	print 'Mathematical part segmentation complete!!'
	save_results(mpath, mtext)
	if len(etext) == len(ttext) == len(mtext):
		print '# of paragraph: %d' % len(etext)
	else:
		print 'The grouping failed'

#TEST Code by Jason
if __name__ == "__main__":
	#Test Bed #1
	ipath = 'test2.docx'
	xml_stream = get_docx_xml(ipath)
	all_xml = xml_stream.read()
	test_group(all_xml)
	#Test Bed #2
	ipath2 = 'test2.docx'
	xml_stream_2 = get_docx_xml(ipath2)
	all_xml_2 = xml_stream_2.read()
	test_omml_tree(all_xml_2)
#[TODO] Word texts could include digits <w:t>...</w:t>