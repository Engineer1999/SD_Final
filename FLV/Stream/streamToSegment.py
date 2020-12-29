import os
import time
id_ = 0

def streamToSegment():
    global id_
    for i in range(5):
        cmd = "ffmpeg -i rtmp://proctoring.imadestage.in:1935/show/user009 -t 20 -vn -acodec copy " + str(id_) + '.flv'
        print('----------------------------------------------------------------------------------')
        print(cmd)
        print('----------------------------------------------------------------------------------')
        os.system(cmd)
        id_ = id_ + 1
        time.sleep(7)

streamToSegment()