#!/usr/bin/python
# -*-coding:Latin-1 -*
import sys, requests
from multiprocessing.dummy import Pool as ThreadPool


def cms(url):
    try:
        url = url.replace('\n', '').replace('\r', '')
        op = requests.get(url+'/wp-content/plugins/easy-wp-smtp/', timeout=7)
        if "debug_log.txt" in op.content:
            print "[+] Vuln " + url
            open("Found.txt", "a").write(url +'/wp-content/plugins/easy-wp-smtp/' + "\n")
        else:
            print '- ' + url
    except:
        print "down --> " + url
        pass



a = raw_input('enter list :')
ListPass = open(a, 'r').readlines()
pool = ThreadPool(150)
pool.map(cms, ListPass)
pool.close()
pool.join()

if __name__ == '__main__':
    print("Finished, success")
