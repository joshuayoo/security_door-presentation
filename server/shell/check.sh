#! /bin/bash
emma_check=`ps -ef | grep -v "grep" | grep /home/joshua/project/web/web.py  | wc -l`
date=$(date "+%Y-%m-%d_%H:%M:%S")
if [ "$emma_check" -eq '0'  ]; then
        /bin/python3 /home/joshua/project/web/web.py &
        emma_check=`ps -ef | grep -v "grep" | grep /home/joshua/project/web/web.py  | wc -l`
        if [ "$emma_check" -eq "0"  ]; then
                echo "$date Process Restart Failed!" >> ~/project/log/web_log.log
                /bin/sh /home/joshua/project/shell/check.sh
        else
                echo "$date Process Restart Success!" >> ~/project/log/web_log.log
        fi
else
        echo "$date Process Alive" > ~/project/log/web_log.log
fi

emma_check01=`ps -ef | grep -v "grep" | grep /home/joshua/project/server.py | wc -l`
if [ "$emma_check01" -eq '0'  ]; then
        /bin/python3 /home/joshua/project/server.py &
        emma_check01=`ps -ef | grep -v "grep" | grep /home/joshua/project/server.py  | wc -l`
        if [ "$emma_check01" -eq "0"  ]; then
                echo "$date Process Restart Failed!" >> ~/project/log/server_log.log
                /bin/sh /home/joshua/project/shell/check.sh
        else
                echo "$date Process Restart Success!" >> ~/project/log/server_log.log
        fi
else
        echo "$date Process Alive" > ~/project/log/server_log.log
fi

emma_check02=`ps -ef | grep -v "grep" | grep /home/joshua/project/server_regist.py | wc -l`
if [ "$emma_check02" -eq '0'  ]; then
        /bin/python3 /home/joshua/project/server_regist.py &
        emma_check02=`ps -ef | grep -v "grep" | grep /home/joshua/project/server_regist.py  | wc -l`
        if [ "$emma_check02" -eq "0"  ]; then
                echo "$date Process Restart Failed!" >> ~/project/log/server_regist_log.log
                /bin/sh /home/joshua/project/shell/check.sh
        else
                echo "$date Process Restart Success!" >> ~/project/log/server_regist_log.log
        fi
else
        echo "$date Process Alive" > ~/project/log/server_regist_log.log
fi