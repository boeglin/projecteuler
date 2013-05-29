#!/bin/bash

for i in e*py ; do
    echo -n $i

    itime=$((time python $i) 2>&1 | grep real | grep -v 0m0)
    if [ "x$itime" != "x" ] ; then
        echo ": $itime"
    else
        echo -en '\r'
    fi
done

