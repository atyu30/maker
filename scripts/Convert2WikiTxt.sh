#/bin/sh
#
# Author: atyu30 <iopenbsd@gmail.com>
#
# Last modified: 2013-03-18 16:31
#
# Filename: Convert2WikiTxt.sh
#
# Description: 
#
#Setting
PC0=`date +%Y%m%d%H%M`.log
PC1='/tmp/mediawiki'
#Setting End

if [ ! -d $PC1 ];then
 mkdir $PC1
fi

current=$PC1/$PC0
filepath=`pwd`
for i in `ls $filepath`
do
 echo "{{OMS Config|$i|" >> $current
 echo "<pre>" >> $current
 cat $i >> $current
 echo "</pre>}}" >> $current
done
echo $current
