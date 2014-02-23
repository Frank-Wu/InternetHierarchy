for i in {1..12};
do find data.ris.ripe.net/rrc01/$1.`printf "%02d" $i`/ -name bview* |xargs -I{} ./bgpdump {}|grep ASPATH >> result/$1.`printf "%02d" $i`;
done;
