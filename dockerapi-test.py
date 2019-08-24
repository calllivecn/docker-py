#!/usr/bin/env python3
#coding=utf-8
# date 2018-07-20 15:01:37
# author calllivecn <c-all@qq.com>

URL='tcp://127.0.0.1:2375'

import docker
import pprint

client = docker.DockerClient(base_url=URL)
if not client.ping():
    print("not ping...")
    exit(1)



def run_test():
    detach = client.containers.run("alpine","ping www.baidu.com",detach=True)

    for line in detach.logs(stream=True):
        print(line.strip())


def stats():
    con_det = client.containers.list()
    print("在run的容器:",con_det)
    for stat in con_det:
        stat_info = stat.stats(stream=False)
        pprint.pprint(stat_info)


#client.containers.run("alpine","ping www.baidu.com",detach=True)

stats()
