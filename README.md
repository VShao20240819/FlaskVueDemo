如何使用：

	0- 你需要有python环境， 我的环境为python3.10。尽量安装3.10版本
	
		# 更新软件包列表
		sudo apt update
		# 安装Python 3.10
		sudo apt install python3.10 python3.10-dev python3.10-venv python3.10-distutils
		# 验证安装
		python3.10 --version
		# 验证pip安装
		python3.10 -m pip --version

		# 1. 下载 Node 22 LTS
		cd /usr/local
		wget https://nodejs.org/dist/v22.20.0/node-v22.20.0-linux-x64.tar.xz
		
		# 2. 解压
		tar -xJf node-v22.20.0-linux-x64.tar.xz
		
		# 3. 添加 PATH（临时生效，或者加到 ~/.bashrc）
		export PATH=/usr/local/node-v22.20.0-linux-x64/bin:$PATH
		
		# 4. 验证版本【版本必须要node：v22 、 npm：v10 以上】
		node -v   # 应该显示 v22.20.0
		npm -v    # 应该显示 10.x
		
	1- 下拉代码
	
		git clone https://github.com/VShao20240819/FlaskVueDemo.git
		
	2- 进入项目路径，配置好环境
		
		linux:
		cd FlaskVueDemo
		python3 -m venv venv
		source venv/bin/activate
		pip install -r requirements.txt	
	
		windows:
		cd FlaskVueDemo
		python -m venv venv
		venv\Scripts\activate
		pip install -r requirements.txt
	
	3- 安装node环境（如果在第0步已经使用压缩包安装可以跳过此安装步骤）
	
		https://nodejs.org/zh-cn
		# linux使用 apt install nodejs安装：
			输入Y
			跳出界面： tab 后回车
		# linux使用 apt install npm：
			输入Y
			跳出界面： tab 后回车
			
		检查是否安装成功
		node -v
		npm -v

	4- 同步vue项目
				cd frontend
		npm init -y
		npm install vue@3
		npm install vite @vitejs/plugin-vue --save-dev
		# 配置好vue
		npm run build

	5- 现在可以正常访问Flask接口了
		python run.py
		# mac python3 run.py
		"""
		note: 如果出现端口占用的情况，可以修改Flask中run.py的端口
		"""

	6- 运行完成后，重新绑定自己的git
		gitremote remove origin
		git remote -v 
		# 此时无任何打印为正常
		# 在自己的git仓库中创建一个全新的项目FlaskVueDemo
		git remote add origin https://github.com/yourname/FlaskVueDemo.git

		git branch -M main  # 或者 master，根据你的仓库默认分支
		git push -u origin main

		# 第一次提交git
		git add .
		git commit -m "first push"
		git push



		
