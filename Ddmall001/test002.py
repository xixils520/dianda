# class myclass:
#     """"a ahsghaio"""
#     i=123123
#     def f(self):
#         return 'hello'
#
# class a:
#     def __init__(self,b,c):
#         self.r=b
#         self.i=c
# x=a(3.0,-4.5)
# print(x.i+x.r)
# x.counter=1
# while x.counter<10:
#     x.counter=x.counter*2
# print(x.counter)
# del x.counter
# z=myclass()
# zf=z.f
# while true:
#     print(zf())
import random
iplist=['190.201.0.175:8080', '201.211.173.207:8080', '36.82.125.81:3128', '196.210.210.84:8080', '201.240.108.41:8081', '190.207.183.160:8080', '37.79.181.2:8080', '88.199.18.57:8090', '201.211.111.154:8080', '201.208.58.23:8080', '180.254.250.54:8080', '190.207.249.118:8080', '180.70.227.14:80', '23.239.7.179:8888', '186.91.236.69:8080', '185.106.23.12:3128', '59.60.168.86:41600', '190.204.74.216:8080', '190.73.52.233:8080', '90.88.186.167:8080', '198.13.45.139:808', '190.204.250.227:8080', '182.52.4.36:8080', '198.13.37.54:808']
IP = ''.join(str(random.choice(iplist)).strip())
ip2=random.choice(iplist)
print(IP)
print(ip2)
