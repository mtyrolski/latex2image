idx=0
rm -f labels.txt
for var in "$@"
do
    mkdir -p "${var}_aux"
    cp generate_latex.py "${var}_aux/"
    cp $var "${var}_aux/"
    cd "${var}_aux"
    mv $var "raw_tex.in"
    bash ../python_exec.sh &
    cat raw_tex.in >> ../labels.txt
    cd ..
    ((++idx))
done

mkdir -p output
wait
idx=0
for var in "$@"
do
    cd "${var}_aux"
    wait
    for file in `ls *.png | sort -V`;
    do 
        mv "$file" "eq${idx}.png"
        wait
        cp "eq${idx}.png" ../output/
        ((++idx)) 
    done;
    cd ..
    wait
    rm -rf "${var}_aux"
done
