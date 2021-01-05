#!/bin/bash


echo -e "\n$(hostname) time: $(date +'%d-%m-%y %H:%M')" >> ~/Code/doodles/job_log.log

echo $(/usr/local/bin/qstat -x) >> ~/Code/doodles/job_log.log
