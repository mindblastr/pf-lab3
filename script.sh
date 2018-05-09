if [ "$#" -eq "0" ]
  then
    echo "No arguments supplied"
elif [ ! -f $1 ]; then
    echo "File not found!"
else
    for filename in ./data/train/*.wav; do
        SMILExtract -C $1 -I "$filename" -O "$filename"_out.csv
    done
    for filename in ./data/dev/*.wav; do
        SMILExtract -C $1 -I "$filename" -O "$filename"_out.csv
    done
fi