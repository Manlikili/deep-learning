#选择conda安装环境
conda env remove d2l-zh
 conda create -n -y d2l-zh python=3.8 pip conda activate d2l-zh
#安装需要的包
 pip install -y jupyter d2l torch torchvision
#下载代码并执行
 wget https://zh-v2.d2l.ai/d2l-zh.zip 
 unzip d2l-zh.zip
 jupyter notebook

