year=2011
for month in {01..06};
do 
	obs_num=`cat hmmdataset/${year}.${month}.seq.size`;
	state_num=6
#	sleep 20m
	#for state_num in {4..7};
#	do 
		./jahmm.sh learn-bw -opdf integer -r $obs_num -is hmmdataset/${year}.${month}.seq -ni 1000 -i hmmdataset/${year}.${month}.${state_num}.hmm -o hmmresult/${year}.${month}.${state_num}.hmm &
#	done;
done;
