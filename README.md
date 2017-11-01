# gpio-shell
bash、shell下的操控GPIO的脚本。

首先让其可执行：
```shell
chmod +x ./power.sh
```
然后，让GPIO2点亮LED
```shell
./power 2 1
```

关闭LED
```shell
./power 2 0
```

udpserver
```shell
python udpserver.py
```

udp发送命令的字符串格式:
```
[指令]_[pin号]
如：
on_2 让pin2为高电平
off_2 让pin2为低电平
```
