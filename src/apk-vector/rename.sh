filelist=`ls $1/`
cd $1
for file in $filelist
do 
 #echo $file
 mv $file `sha256sum $file|awk '{print $1}'`.apk
done
