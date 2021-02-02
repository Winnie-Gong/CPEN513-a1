from matplotlib import pyplot
from matplotlib import colors

#from possible paths of 2 routings, find a combination with longest common path
def find_common_path(paths1, paths2):
	if not paths1 and not paths2:
		return []
	elif not paths1:
		return paths2
	elif not paths2:
		return paths1
	max_comm_len = 0
	path_len = min(len(paths1[0]), len(paths2[0]))
	chosen_path = paths1[0]+paths2[0]
	for p1 in paths1:
		for p2 in paths2:
			for i in range(path_len):
				if p1[i] != p2[i]:
					#if it is the longest common path up till now
					if i > max_comm_len:
						max_comm_len = i
						#combine 2 paths
						chosen_path = p1+p2
					break
	return chosen_path

def plot(grid):
	pyplot.figure(figsize=(10,5))
	pyplot.imshow(grid)
	pyplot.show()