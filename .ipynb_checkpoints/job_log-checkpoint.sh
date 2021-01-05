#!/usr/bin/bash


echo -e "\n$(hostname) time: $(date +'%d-%m-%y %H:%M')" >> ~/Code/doodles/job_log.log

echo $(qstat -x) >> ~/Code/doodles/job_log.log