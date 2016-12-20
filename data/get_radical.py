# -*- coding: UTF-8 -*-
import pdb
inf = "characterRadicalMap.dict"
radicals = []
with open(inf,'r') as f1:
	for line in f1:
		line = line.split()
		radicals.append(line[1])
radicals = set(radicals)
radicals = list(radicals)
outf = "radical_list.txt"
with open(outf,'w') as f2:
	f2.write(' '.join(radicals))