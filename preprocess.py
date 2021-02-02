import numpy as np

def Preprocess(file):
	#read file as lines
	f = open(file, "r").readlines()

	dims = f[0].split()
	dims = [int(dims[0]), int(dims[1])]
	grid = np.zeros(dims[::-1])
	obs_num = int(f[1])
	obs = []

	#build obstructions by setting them as -1
	curr_line = 2
	for i in range(curr_line, curr_line+obs_num):
		curr_obs = f[i].split()
		grid[int(curr_obs[1]),int(curr_obs[0])] = -1
	curr_line += obs_num

	wire_num = int(f[curr_line])
	wires = []

	#extract pin information
	curr_line += 1
	for i in range(curr_line, curr_line+wire_num):
		curr_wire = f[i].split()
		pin_num = int(curr_wire[0])
		pins = []
		for j in range(0, pin_num):
			pins.append([int(curr_wire[j*2+2]), int(curr_wire[j*2+1])])
			grid[int(curr_wire[j*2+2]), int(curr_wire[j*2+1])] = -2
		wires.append(pins)
	return grid, wires