def fcounter(cl, *args):
	class Empty:
		pass
	standardAttr = dir(Empty)
	classAttr = dir(cl)
	object = cl(*args)
	objectAttr = dir(object)
	#print(standardAttr,'\n')
	#print(objectAttr,'\n')
	classMethods = []
	classFields = []
	objectMethods = []
	objectFields = []
	for cur in objectAttr:
		if not cur in standardAttr and not cur.startswith('_'):
			if cur in classAttr:
				if callable(eval('cl.' + cur)):
					classMethods.append(cur)
					if not callable(eval('object.' + cur)):
						objectFields.append(cur)
				else:
					classFields.append(cur)
			else:
				if callable(eval('object.' + cur)):
					objectMethods.append(cur)
				else:
					objectFields.append(cur)
	
	return (classMethods, classFields, objectMethods, objectFields)