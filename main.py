# import numpy as np
from preprocess import Preprocess
from lee_moore import Lee_moore
from utils import find_common_path, plot
import itertools


benchmark_names = ["sydney", "stanley", "impossible", "oswald", "rusty", "misty", "impossible2"]
# The algorithm has runtime issue with the below benchmarks
# benchmark_names = ["stdcell", "wavy",  "kuma"]

for benchmark in benchmark_names:
	grid, wires = Preprocess("benchmarks/"+benchmark+".infile")
	total_pins = 0
	unrouted_pins = 0
	for wire_num,wire in enumerate(wires):
		route_num = len(wire)-1
		total_pins += route_num
		
		if route_num == 1:
			new_grid = grid.copy()
			path = Lee_moore(new_grid, wire[0], wire[1])
			if path:
				#for single-sink wires, pick the first possible path
				chosen_path = path[0]
			else:
				unrouted_pins += 1
		else:
			paths = []
			#for wires with multiple sinks, compute all possible paths from source to each sink individually
			for n in range(route_num):
				new_grid = grid.copy()
				path = Lee_moore(new_grid, wire[0], wire[n+1], other_ends=wire[1:])
				paths.append(path)
				if not path:
					unrouted_pins += 1
			#from possible paths of 2 routings, find a combination with longest common path
			if len(paths) == 2:
				chosen_path = find_common_path(paths[0], paths[1])
			for i in range(route_num-2):
				chosen_path = find_common_path(chosen_path, paths[i+2])

		#mark down chosen path on the grid
		for step in chosen_path:
			grid[step[0]][step[1]] = -3-wire_num
	print("Benchmark "+benchmark+": "+str(total_pins-unrouted_pins)+ " wires successfully routed.")
	plot(grid)


