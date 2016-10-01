## Looking at the Network tab of Inspect in Chrome
Gonna find what kind of requests those js scripts make and get the data by simulating these requests.

### General
Request URL:http://119.164.252.34:8403/ajax/npublic/NData.ashx?jsoncallback=jQuery1111007922787791008012_1475292229380&Method=GetMonitorDataList&entCode=37011203096&subType=2%2C3&subID=&year=2016&itemCode=&dtStart=2013-01-01&dtEnd=2016-09-30&monitoring=&bReal=false&page=99&rows=100&_=1475292229393  
Request Method:GET  
Status Code:200 OK  
Remote Address:119.164.252.34:8403
###Response Headers  
Cache-Control:private  
Content-Length:11690  
Content-Type:text/plain; charset=utf-8  
Date:Sat, 01 Oct 2016 03:34:04 GMT  
Server:Microsoft-IIS/6.0  
X-AspNet-Version:2.0.50727  
X-Powered-By:ASP.NET
###Request Headers  
Accept:*/*  
Accept-Encoding:gzip, deflate, sdch  
Accept-Language:en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2,ja;q=0.2  
Connection:keep-alive  
Host:119.164.252.34:8403  
Referer:http://58.56.98.78:8405/ND/370100/2016/37011203096  
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36
###Query String Parameters  
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
####Query in URL
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
