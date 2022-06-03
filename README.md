# owa-honeypot
A basic flask based Outlook Web Honey pot

![Docker Build](https://github.com/just5ky/owa/workflows/Docker/badge.svg) ![Docker Pulls](https://img.shields.io/docker/pulls/justsky/owa) ![Docker Size](https://img.shields.io/docker/image-size/justsky/owa?color=orange)

This is  a fork of [joda32/owa-honeypot](https://github.com/joda32/owa-honeypot) but dockerized,  loggging to file and updated dependencies.


![](docs/OWA_honeypot_1.png)

## why?
Most corps have some form of OWA and I couldn't find an out of the box OWA only honeypot (I'm sure if I spent more than 2 minutes googling I probably would have found one) and I wanted to mess around with some ideas I have. So I spent some time putting this together, maybe it could help someone else :)

## requirements
python3 + flask

## how to install

`docker run --rm --name owa-honeypot -v .:/log -p 80:80 justsky/owa`

## here be dragons!
In the code I basically start the flask dev server on port 80, that is a really bad idea if you want to run it on the internet. I have a todo to change that. :)

Anyway, it did work for what I wanted. I've added a crude write up here (https://joda32.github.io/2019/06/11/owa-plus-pastebin.html)

![](docs/OWA_honeypot_2.png)
![](docs/OWA_honeypot_3.png)
