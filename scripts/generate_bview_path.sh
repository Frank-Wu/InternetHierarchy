for year in {2004..2013};
do
for monthalg in {1..12};
	do month=`printf "%02d" $monthalg`;find data.ris.ripe.net/rrc${1}/${year}.${month}/ -name bview.${year}${month}0[1-5].* |xargs -I{} ./bgpdump {}|grep ASPATH >> rawdataset/rrc${1}.${year}.${month}&
	done;
done;
