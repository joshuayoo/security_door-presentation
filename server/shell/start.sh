#!/bin/bash
sleep 20
/bin/python3 /home/joshua/project/server.py &
/bin/python3 /home/joshua/project/server_regist.py &
/bin/python3 /home/joshua/project/web/web.py &
sleep 12
exit
