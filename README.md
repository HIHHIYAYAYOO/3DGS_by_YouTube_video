# 使用方法
將 3DGSYT.py 放入 [gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting) 本機的目錄下

```shell
cd {your_path}/gaussian-splatting
```

```shell
python 3DGSYT.py -url "https://youtu.be/1C52jSCGkVY?si=Kdu49IpgorJefDMB"
```
也可使用

```shell
python 3DGSYT.py -url "https://youtu.be/_2ntYhxo9OI?si=y0MmTyN1hN_e36Lz" -res "1080p" -fps "1"
```
-url : 設定下載 YouTube 的影片網址
-res : 設定下載 YouTube 的影片畫質
-fps : 設定影片每秒擷取多少 fps 的畫面
