# Nginx

#!/bin/bash
# author:WinJayX
# date:2019-11-14
# Maintainer WinJayX <WinJayX@Gmail.com>
# func:每10秒自动监测nerc.service服务状态且在退出时执行重启操作
#
docker container run -d \
	--volume /etc/localtime:/etc/localtime:ro \
  --volume `pwd`/nginx.conf:/etc/nginx/nginx.conf \
  --volume `pwd`/conf.d:/etc/nginx/conf.d \
  --restart always \
  --user root \
  --name Nginx \
	--hostname Nginx \
	-m 4096M \
  -p 443:443 \
  -p 80:80 \
nginx:1.20.1


# ES-IK
docker container run -d \
	--net ELK \
	--name ES-IK \
	--hostname ES \
	-p 9200:9200 \
	-p 9300:9300 \
	-m 10g \
	--restart always \
	-e "discovery.type=single-node" \
	-e ES_JAVA_OPTS="-Xms10g -Xmx10g" \
	-v `pwd`/ES-Data:/usr/share/elasticsearch/data \
	-v `pwd`/plugins:/usr/share/elasticsearch/plugins \
	-v `pwd`/config:/usr/share/elasticsearch/config \
	--volume /etc/localtime:/etc/localtime:ro \
	elastic/elasticsearch:7.15.2

# Redis

#!/bin/bash
# author:WinJayX
# date:2019-11-14
# Maintainer WinJayX <WinJayX@Gmail.com>
# func:Redis fast start
# --appendonly yes 设置Redis数据持久化到本地磁盘中
# `pwd` 获取当前目录路径
# 权限配置：1./logs/redis.log文件要加入用户可写入权限
# 2.temp目录配置777

docker container run -d \
    --volume /etc/localtime:/etc/localtime:ro \
    --volume `pwd`/conf/redis.conf:/etc/redis/redis.conf \
    --volume `pwd`/logs/redis.log:/var/log/redis/redis.log \
    --volume `pwd`/temp:/var/lib/redis \
    --volume `pwd`/data:/data \
    --restart always \
    --user root \
    --name Redis \
    --hostname Redis \
    -p 65379:65379 \
    -p 6379:6379 \
    -m 2048M \
    redis:6.2.6 \
    redis-server /etc/redis/redis.conf \
    --appendonly yes



# 1
docker rm -f Uploader
docker container run -d -p 8001:80\
    --volume /etc/localtime:/etc/localtime:ro \
    --volume `pwd`/1.uploader:/app/Config \
    --restart always \
    --user root \
    --name Uploader \
hub.nercoa.com/sdk/uploader:v1.6.0


# 2
docker rm -f Messages
docker container run -d -p 8002:80\
    --volume /etc/localtime:/etc/localtime:ro \
    --volume `pwd`/2.Messages-Api:/home/node/app \
    --restart always \
    --user root \
    --name Messages \
    --add-host Redis:10.80.1.130 \
node:17.2.0 node app.js

# 3
docker rm -f AuthServ
docker container run -d -p 8003:80\
    --volume /etc/localtime:/etc/localtime:ro \
    --volume `pwd`/3.AuthServ:/app/Config \
    --restart always \
    --user root \
    --name AuthServ \
    --add-host MasterDB01:10.80.1.132 \
    --add-host Redis:10.80.1.130 \
hub.nercoa.com/sdk/fz_common:v1.6.3

# 4
docker rm -f RobotFront
docker container run -d -p 8004:80\
    --volume /etc/localtime:/etc/localtime:ro \
    --volume `pwd`/4.RobotFront:/app/Config \
    --restart always \
    --user root \
    --name RobotFront \
    --add-host MasterDB01:10.80.1.132 \
    --add-host Redis:10.80.1.130 \
    --add-host ES:10.80.1.130 \
hub.nercoa.com/robot/instructionalguidancerobot:v1.9.8

# 5
docker rm -f RobotBackstage
docker container run -d -p 8005:80\
    --volume /etc/localtime:/etc/localtime:ro \
    --volume `pwd`/5.RobotBackstage:/app/Config \
    --restart always \
    --user root \
    --name RobotBackstage \
    --add-host MasterDB01:10.80.1.132 \
    --add-host Redis:10.80.1.130 \
    --add-host ES:10.80.1.130 \
hub.nercoa.com/robot/robot_admin:v1.6.1
