#选择conda安装环境
conda env remove --name d2l-zh
conda create -n -y d2l-zh python=3.8 pip -y
conda activate d2l-zh
#安装需要的包
 pip install jupyter d2l torch torchvision 
#下载代码并执行
brew --version
brew install wget
 wget https://zh-v2.d2l.ai/d2l-zh.zip 
 unzip d2l-zh.zip
 jupyter notebook
## 请始终执行conda activate d2l以激活运行时环境。 要退出环境，请运行conda deactivate。
conda activate d2l
conda deactivate
git push origin main