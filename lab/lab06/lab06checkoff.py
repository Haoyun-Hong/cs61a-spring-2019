def mutate_lst(lst, origin, dest):
	counter=0
	for i in lst: 
		if counter == origin:
			i=0
		counter +=1

	counter=0
	for i in lst:
		if counter==dest:
			i=1
		counter+=1
	return None 


def mutate_tree(t):
	if is_leaf(t):
		return tree(label(t)**2)
	else:
		return tree(label(t)**2, [mutate_tree(b) for b in branches(t)])