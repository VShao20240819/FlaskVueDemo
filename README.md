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
	
	3- 安装node环境
	
		https://nodejs.org/zh-cn
		检查是否
		node -v
		npm -v
		cd frontend
		npm init -y
		npm install vue@3
		npm install vite @vitejs/plugin-vue --save-dev