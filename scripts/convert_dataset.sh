for month in {1..12};
	do python convert_dataset.py $1 `printf "%02d" $month` & done;
