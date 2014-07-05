#for year in {2004..2013};
for year in 2011;
do
	for month in {1..12};
		do python filter_dataset.py $1 $year `printf "%02d" $month` & done;
done;
