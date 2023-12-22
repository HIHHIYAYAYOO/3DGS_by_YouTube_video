# 透過 YouTube 影片重建 3D gaussian splatting 模型
## 使用方法
### 前置作業
將 3DGSYT.py 放入 [gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting) 本機的目錄下

### 進入 Terminal
```shell
cd {your_path}/gaussian-splatting
```

### 開始重建 3D gaussian splatting 模型 
```shell
python 3DGSYT.py -url "https://youtu.be/1C52jSCGkVY?si=Kdu49IpgorJefDMB"
```

 或者
### 開始重建 3D gaussian splatting 模型 (可指定影片各項參數)
```shell
python 3DGSYT.py -url "https://youtu.be/_2ntYhxo9OI?si=y0MmTyN1hN_e36Lz" -res "1080p" -fps "1"
```
* -url : 設定下載 YouTube 的影片網址
* -res : 設定下載 YouTube 的影片畫質
* -fps : 設定影片每秒擷取多少 fps 的畫面
