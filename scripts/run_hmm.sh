state_num=5
for month in {1..4};
do 
	ym=$1.`printf "%02d" ${month}`
	obs_num=`cat hmmdataset/${ym}.seq.size`;
	./jahmm.sh learn-bw -opdf integer -r $obs_num -is hmmdataset/${ym}.seq -ni 1000 -i hmmdataset/${ym}.${state_num}.hmm -o hmmresult/${ym}.${state_num}.hmm &
done;
