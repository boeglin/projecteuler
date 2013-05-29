#!/bin/bash

for i in e*py ; do
    itime=$((time python $i) 2>&1 | grep real | grep -v 0m0)
    [ "x$itime" != "x" ] && echo "$i: $itime"
done

