import keyword

my_locals={}
query = input()
while query != '' and query != '.':
	if not query.startswith('#'):
		try:
			print(eval(query,my_locals))
		except Exception as e1:
			try:
				exec(query,my_locals)
				query_equal = query.find('=')
				my_locals[query[:query_equal]] = eval(query[query_equal+1:],my_locals)
				#print(my_locals)
				success = True
			except Exception as e2:
				query_equal = query.find('=')
				if query_equal > 0:
					if query[:query_equal].isidentifier():
						print('invalid assignment ' + '\'' + query + '\'')
						success = True
					else:
						print('invalid identifier ' + '\'' + query[:query_equal] + '\'')
						success = True
				else:
					print(e2)
	try:
		query = input()
	except:
		break