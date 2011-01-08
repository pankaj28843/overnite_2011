#!/bin/bash

worker="$1"
if [ ! -z "$worker" ]; then     
    if [ -d "$worker" ]; then
        echo "A worker with name $worker is alread running."
    else
        echo $worker
        unzip worker.zip 
        mv worker $worker
        cd $worker 
        chmod +x manage.py
        ./manage.py celeryd -l info $worker -n $worker
        cd ..
        rm -r $worker
    fi
else
    echo "Please provide a worker name."
fi

