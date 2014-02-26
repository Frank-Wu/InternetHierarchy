for i in {2002..2014};
	do find data.ris.ripe.net/rrc06/$i.01/ -name bview* |xargs -I{} ./bgpdump {}|grep ASPATH >> result/$i.01&
	done;
