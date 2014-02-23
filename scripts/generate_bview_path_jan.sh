find data.ris.ripe.net/rrc02/$1.01/ -name bview* |xargs -I{} ./bgpdump {}|grep ASPATH >> result/$1.01
