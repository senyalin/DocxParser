class ME(object):
	def __init__(self, name):
		self.name = name
	pass
#Atomic ME
class AtomicME(ME):
	pass
class Identifier(AtomicME):
	pass
class SingleOP(AtomicME):
	pass
class FunctionalOP(AtomicME):
	pass
class ConstantSym(AtomicME):
	pass
class BindOP(AtomicME):
	pass
class BinaryOP(AtomicME):
	pass
class Others(AtomicME):
	pass