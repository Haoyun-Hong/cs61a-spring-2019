# Q2:Longest Increasing Subsequence 

def larger_values(x, lst):
	if not lst:
		return lst 
	elif len(lst)==1 and lst[0] > x:
		return lst 
	elif lst [0] > x:
		new_list=[lst[0]]+larger_values(x, lst[1:])
		return new_list
	else:
		return larger_values(x, lst[1:])

def longest_increasing_subsequence(lst):
	if not lst:
		return []
	elif len(lst) ==1:
		return lst
	else: 
		first=lst[0]
		rest=lst[1:]
		large_values_rest = larger_values (first, rest)
		with_first = [first]+longest_increasing_subsequence (large_values_rest)
		without_first= longest_increasing_subsequence(rest)
		if len(with_first) > len(without_first):
			return with_first
		else:
			return without_first