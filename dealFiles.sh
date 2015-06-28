Folder_A="/cygdrive/c/Users/Danny/PycharmProjects/word2vec/text"  
for file_a in ${Folder_A}/*; do  
    #temp_file=`basename $file_a`  
    echo $file_a
    sed -i 's/\./. /g' $file_a
done 
