def shiftByTwo(*args):
	if len(args)>2:
		result = []
		result.extend([args[-2],args[-1]])
		i = 2
		while i < (len(args)):
			result.append(args[i-2])
			i += 1 
		return tuple(result)
	else:
		return tuple(args)
