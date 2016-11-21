# This is phone risk center

Enjoy it.


# Prerequired

- Memcached
- Redis
- Mysql/Mariadb


# Start Develop environment


## Install Mariadb in CentOS 7

      yum install -y mariadb*

create database

      CREATE DATABASE `risk` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
      
      #create user
      CREATE USER 'cacti'@'localhost' IDENTIFIED BY 'cacti';
      GRANT ALL ON *.* TO 'cacti'@'localhost';
      
      CREATE USER 'cacti'@'%' IDENTIFIED BY 'cacti';
      GRANT ALL ON *.* TO 'cacti'@'%';

## Install some python libs

Install python. Install virtualenv.

    cd ~/Documents/pyenv/
    virtualenv dj18 

    cd ~/Documents/gitroom
    
    #clone code at here
    
    cd risk/confs/dev/ && ./install.sh
    
Migrate django db

    ./bg_cmd.sh migrate

Create super user. (admin:admin)

    ./bg_cmd.sh createsuperuser admin

    
Create two group in http://localhost:8000/admin/

    管理员
    开发者
    
Run server. Then visit http://localhost:8000/

    ./run.sh app
    ./run.sh rq
    
    
# Production

install crontab 

    */1 * * * * cd /home/webapps/risk/confs/production/; ./bg_cmd.sh task_dispatch
    
    
    
Create two group

    管理员
    开发者
