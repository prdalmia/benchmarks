
import os
new=open("new.config",'w')
with open('test.config', 'r') as f:
    for line in f.readlines():
        if "dl1" in line:
            line = "-gpgpu_cache:dl1" +  " S:4:128:" + "256" + ",L:L:s:N:L,A:256:8,16:0,32" + "\n"
        new.write(line)
new.close()
os.rename('test.config', 'test_old.config')
os.rename('new.config', 'test.config')

