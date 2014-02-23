cd hmmresult;
for file in *;
do
	grep "Pi\|A" $file > ../hmmstates/$file;
done;

