## Different Remote Server Addresses for Each City in Shandong
119.164.252.34:8403 济南
219.147.6.195:8403 青岛
60.210.111.130:8406 淄博
218.56.152.39:8403 枣庄
221.2.232.50:8401 东营
218.56.33.245:8403 烟台
122.4.213.20:8403 潍坊
60.211.254.236:8403 济宁
220.193.65.234:8403 泰安
60.212.191.18:8408 威海
219.146.185.5:8404 日照
218.56.160.167:8403 莱芜
58.57.43.244:8414 临沂
222.133.11.150:8403 德州
222.175.25.10:8403 聊城
222.134.12.94:8403 滨州
219.146.175.226:8403 菏泽

## The company list when clicked "Search"
#### General
Request URL:http://58.56.98.78:8405/ajax/npublic/Index.ashx?jsoncallback=jQuery1111026710970292811953_1475289728500  
Request Method:POST  
Status Code:200 OK  
Remote Address:58.56.98.78:8405  
#### Response Headers
Cache-Control:private  
Content-Length:3728  
Content-Type:text/plain; charset=utf-8  
Date:Sat, 01 Oct 2016 04:01:15 GMT  
Server:Microsoft-IIS/6.0  
X-AspNet-Version:4.0.30319  
X-Powered-By:ASP.NET  
#### Request Headers  
Accept:text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01  
Accept-Encoding:gzip, deflate  
Accept-Language:en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2,ja;q=0.2  
Connection:keep-alive  
Content-Length:95  
Content-Type:application/x-www-form-urlencoded; charset=UTF-8  
Cookie:ASP.NET_SessionId=hwkfbkzrlcugfmotu00ghdxc  
Host:58.56.98.78:8405  
Origin:http://58.56.98.78:8405  
Referer:http://58.56.98.78:8405/  
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36  
X-Requested-With:XMLHttpRequest  
#### Query String Parameters  
jsoncallback:jQuery1111026710970292811953_1475289728500  
#### Form Data
IsBeginZxjc:2  
Method:LoadGrid  
SubType:2  
Year:2016  
areaCode:0  
cityCode:0  
EntName:  
page:1  
rows:20  

## The Data Request of a Company in the list
Looking at the Network tab of Inspect in Chrome, gonna find what kind of requests those js scripts make and get the data by simulating these requests.  

#### General
Request URL:http://119.164.252.34:8403/ajax/npublic/NData.ashx?jsoncallback=jQuery1111007922787791008012_1475292229380&Method=GetMonitorDataList&entCode=37011203096&subType=2%2C3&subID=&year=2016&itemCode=&dtStart=2013-01-01&dtEnd=2016-09-30&monitoring=&bReal=false&page=99&rows=100&_=1475292229393  
Request Method:GET  
Status Code:200 OK  
Remote Address:119.164.252.34:8403
#### Response Headers  
Cache-Control:private  
Content-Length:11690  
Content-Type:text/plain; charset=utf-8  
Date:Sat, 01 Oct 2016 03:34:04 GMT  
Server:Microsoft-IIS/6.0  
X-AspNet-Version:2.0.50727  
X-Powered-By:ASP.NET
#### Request Headers  
Accept:*/*  
Accept-Encoding:gzip, deflate, sdch  
Accept-Language:en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2,ja;q=0.2  
Connection:keep-alive  
Host:119.164.252.34:8403  
Referer:http://58.56.98.78:8405/ND/370100/2016/37011203096  
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36
#### Query String Parameters  
jsoncallback:jQuery1111007922787791008012_1475292229380  
Method:GetMonitorDataList  
entCode:37011203096  
subType:2,3  
subID:  
year:2016  
itemCode:  
dtStart:2013-01-01  
dtEnd:2016-09-30  
monitoring:  
bReal:false  
page:99  
rows:100  
_:1475292229393
#### Query in URL
jsoncallback=jQuery1111007922787791008012_1475292229380&Method=GetMonitorDataList&entCode=37011203096&subType=2%2C3&subID=&year=2016&itemCode=&dtStart=2013-01-01&dtEnd=2016-09-30&monitoring=&bReal=false&page=99&rows=100&_=1475292229393

#### Response Headers SOURCE
HTTP/1.1 200 OK  
Date: Sat, 01 Oct 2016 03:34:04 GMT  
Server: Microsoft-IIS/6.0  
X-Powered-By: ASP.NET  
X-AspNet-Version: 2.0.50727  
Cache-Control: private  
Content-Type: text/plain; charset=utf-8  
Content-Length: 11690  

#### Request Headers SOURCE
GET /ajax/npublic/NData.ashx?jsoncallback=jQuery1111007922787791008012_1475292229380&Method=GetMonitorDataList&entCode=37011203096&subType=2%2C3&subID=&year=2016&itemCode=&dtStart=2013-01-01&dtEnd=2016-09-30&monitoring=&bReal=false&page=99&rows=100&_=1475292229393 HTTP/1.1  
Host: 119.164.252.34:8403  
Connection: keep-alive  
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36  
Accept: */*  
Referer: http://58.56.98.78:8405/ND/370100/2016/37011203096  
Accept-Encoding: gzip, deflate, sdch  
Accept-Language: en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2,ja;q=0.2  
