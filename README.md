# FlaskVueDemo
这是一个Flask+Vue的Demo项目， 使用最干净的环境可以直接搭建一个Flask+Vue的项目

1- 创建好项目架构：

	可以直接从git下拉
	
2- 配置环境：

	需要有干净可用的python环境， 如果没有，我这里安装的为python3.12.10：
	***
	python3 -m venv venv
	***
	
3- 下载所需库

	***
	pip install flask==3.1.2
	# 将安装库同步到 requirements.txt
	pip freeze > requirements.txt
	***

4- 启动Flask项目

	在terminal中运行，就可以看到项目已经启动。
	***
	python run.py
	***

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

	接下来是git同步操作，请将你创建好的项目同步至你的git仓库
	***
	git status
	git add .
	git commit -m "first push"
	git push
	***
	# 如果需要账号密码，则需要自己配置ssh等
	
7- Vue的使用

	目前你可以运行最低的Flask项目，但是要与前端绑定需要安装 nodejs
	
	这里是网址： https://nodejs.org/zh-cn
	
	***
	mkdir frontend
	cd frontend
	npm init -y
	npm install vue@3
	npm install vite @vitejs/plugin-vue --save-dev
	# 使用脚手架安装Vue
	npm create vite@latest frontend
	***
	
	Project name: 直接回车用默认 frontend
	Select a framework: 选择 Vue → 回车
	Select a variant: 选择 JavaScript → 回车
	Add Vue Router? 根据需求选 Yes/No（一般选 Yes）
	其它功能暂时可以选 No
	执行完，这个命令会生成完整 Vue 前端项目结构，不需要你手动建任何文件夹。

	***
	cd frontend
	npm install

	npm run build
	npm run dev
	
	npm install vue-router
	npm list vue-router

	npm run build
	***

8- 构建Vue架构，并让他们运行起来

	构建目录



9- 绑定 Flask 和 Vue

	结构 api 和 frontend 一致的目录
	构建 ../frontend/dist
	Flask构建路由，并在 __init__ 中绑定
	Frontend构建路由，并在 router/index.js 中路由
	App.vue 构建基础的页面
	frontend/main.js 构建
	frontend/vit.config.js path修改为 '../frontend/dist'

10- 代码编写

	在 Flask 中编写 api 接口
	在对应的 frontend/src/views/*.vue 中修改页面样式



