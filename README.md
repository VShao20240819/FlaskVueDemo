# FlaskVueDemo
这是一个Flask+Vue

1- 创建好项目架构
	可以直接从git下拉
2- 配置环境
	需要有干净可用的python环境， 如果没有，我这里安装的为python3.12.10
	python3 -m venv venv

3- 下载所需库
	pip install flask==3.1.2
	# 将安装库同步到 requirements.txt
	pip freeze > requirements.txt

4- 启动Flask项目
	python run.py

5- 设置gitignore
	touch .gitignore	# windows可以直接创建并写入内容
	
	# Python
	__pycache__/
	*.pyc
	*.pyo
	*.pyd

	# Virtual environment
	venv/
	.env/

	# IDE
	.vscode/
	.idea/

	# Logs
	*.log

	# Vue 中的内容
	frontend/node_modules/
	# 根据服务器不同的不同配置内容
	config/ssh_prod.ini

	# 项目临时文件夹
	temp/
	logs/

6- git 同步操作
	git status
	git add .
	git commit -m "first push"
	git push



















