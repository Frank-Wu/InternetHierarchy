for year in {2002..2008};
do 
	obs_num=`cat hmmdataset/$year.01.seq.size`;
	for state_num in {4..7};
	do 
		./jahmm.sh learn-bw -opdf integer -r $obs_num -is hmmdataset/$year.01.seq -ni 1000 -i hmmdataset/$year.01.$state_num.hmm -o hmmresult/$year.01.$state_num.hmm;
	done;
done;
