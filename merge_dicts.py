'''
here d1 and d2 are length of dict1 and dict2
c1 is length of common keys
Note : c1 = min(d1, d2)
i.e. c1 <= d1 and c1 <= d2


=> total time complexity
=> O(d1 + d2) + O(d1 + d2) + O(d1 + d2) + O(c1 + max(d1, d2))
=> O(d1 + d2 + c1)
=> O(max(d1, d2)) 

i.e linear time complexity

'''

def merge_dicts(dict1, dict2):
	### O(d1 + d2)
	keys1 = set(dict1.keys())
	keys2 = set(dict2.keys())

	##intersection
	### n = 2 i.e. number of dictionary used for intersection
	### (n-1)*O(d1 + d2) -> O(d1 + d2)
	common_keys = keys1.intersection(keys2)

	## len calculation O(d1 + d2)
	if len(keys1) < len(keys2):

		### O(c1)
		common_dict ={}
		for k in common_keys:
			common_dict[k] = [dict2[k], dict1[k]]

		### O(d1)
		for k in keys1:
			dict2[k] = dict1[k]

		### O(c1)
		for k in common_keys:
			dict2[k] = common_dict[k]
		return dict2

	else:

		### O(c1)
		common_dict ={}
		for k in common_keys:
			common_dict[k] = [dict1[k], dict2[k]]


		### O(d2)
		for k in keys2:
			dict1[k] = dict2[k]

		### O(c1)
		for k in common_keys:
			dict1[k] = common_dict[k]
		return dict1

if __name__ == '__main__':
	# d1 = {1:2, 3:4, 5:6}
	# d2 = {7:8, 9:10, 11:12}

	# d1 = {1:2}
	# d2 = {1:1}

	# d1 = {1:'a', 2:'b', 'c':3, 'd':None}
	# d2 = {'c':4, 'k':9, 'd':12}

	d1 = {1:'a', 2:['b', 1, 2, 10], 'c': {'k':'v'}}
	d2 = {'c':4, 'k':9, 2:12}

	print(d1)
	print(d2)
	print(merge_dicts(d1, d2))
