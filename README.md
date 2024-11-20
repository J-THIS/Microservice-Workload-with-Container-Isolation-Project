# project structure
~/docker_project 			  项目文件夹(project directory)

​	——read_data.py        (微服务1读取数据 的python代码 | python code of microservice1--read data)


​	——calculate_scores.py	(微服务2计算总分和最大分差 的python代码 | python code of microservice2--calculate the total score and maximum score difference of each individual)

​	——generate_statistics.py    (微服务3生成统计表格 的python代码| python code of microservice3--generate statistics table)

​	——Grade Table.csv		(源数据文件（各科成绩单）| dataset of grade information)

​	——Dockerfile.read		 (微服务1读取数据 的Dockerfile | Dockerfile of microservice1--read data)

​	——Dockerfile.calculate	 (微服务2计算总分和最大分差 的Dockerfile | Dockerfile of microservice2--calculate the total score and maximum score difference of each individual)

​	——Dockerfile.generate	(微服务3生成统计表格 的Dockerfile | Dockerfile of microservice3--generate statistics table)

​	——docker-compose.yml	(配置所有微服务、网络和卷 | manage services, networks, and volumes)

## read_data.py
微服务1：读取位于项目文件夹目录docker_project下的源数据文件Grade Table.csv<br/>
Microservice1: Read the grade dataset file Grade Table.csv located in the project directory docker_project

## calculate_scores.py
微服务2：接收微服务1读取的源数据文件，计算总分和最大分差，生成DataFrame格式，其中Sum代表个人总分，Range代表个人最大分差<br/>
Microservice 2: receives the dataset read by microservice 1, calculates the total score and the maximum score difference, and generates the DataFrame format, where 'Sum' represents the total score and 'Range' represents the maximum score difference

## generate_statistics.py
微服务3：接收微服务2传来的数据，生成一个Statistics_Table.csv 文件以供用户下载<br/>
Microservice 3: Receives data from microservice 2 and generates a Statistics_Table.csv file for users to download.

## Dockerfile (all three are similar)
定义如何生成三个微服务对应的镜像<br/>
Define how to generate images corresponding to the three microservices

## docker-compose.yml
配置所有微服务、网络和卷<br/>
manage microservices, networks, and volumes

## 启动服务操作 (Start Service)
若需要重新构建镜像（不是容器而是镜像）再启动服务，用这条命令： <br/>
If you need to rebuild the image (not the container but the image) and start the service again, use this command:
```bash
sudo docker-compose up --build
```
如果你想重新启动已经构建并停止的容器，可以使用以下命令： <br/>
If you want to restart a container that has been built and stopped, you can use the following command:
```bash
sudo docker-compose up
```
**如果你没有修改 Dockerfile 或代码，或者你不需要重新构建镜像，直接运行 `docker-compose up` 就可以启动已经存在的容器** <br/>
**If you haven't modified the Dockerfile or the code, or if you don't need to rebuild the image, you can just run `docker-compose up` to start an already existing container**

## 访问服务(Access Service)
从浏览器依次输入以下网址，即可访问对应微服务：<br/>
To access the corresponding microservice, enter the following URLs in sequence from your browser:
- **读取数据服务(read data service)**：`http://localhost:8000/read`
- **计算总分和最大分差服务(calculate the total score and maximum score difference service)**：`http://localhost:8001/calculate`
- **生成可下载统计表服务(generate statistics table for downloading service)**：`http://localhost:8002/generate`
