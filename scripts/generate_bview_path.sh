year=2011
for month in {01..12};
	do find data.ris.ripe.net/rrc${1}/${year}.${month}/ -name bview.${year}${month}0[1-5].* |xargs -I{} ./bgpdump {}|grep ASPATH >> rawdataset/rrc${1}.${year}.${month}&
	done;
