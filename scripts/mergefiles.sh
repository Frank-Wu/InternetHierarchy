for vt in 00 07 11 10 06 03 05 01 04;
do
	#for year in {2004..2013};
	for year in 2011;
	do
		for month in {1..12};
		do
			cat dataset/rrc${vt}.${year}.`printf "%02d" ${month}` >> mergerawdataset/${year}.`printf "%02d" ${month}`;
		done;
	done;
done;
