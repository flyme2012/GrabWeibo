import grabWeibo


userinfo = {'userName':'15238362563','password':'hu147258'}
loginUrl = 'https://passport.weibo.cn/signin/login'
contentUrl = 'http://weibo.com/askcliff/home'

#设置请求头文件信息
requestHeaders = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip',
'Connection':'close',
'Referer':'http://www.baidu.com/'}



print "baidu html content"
print grabWeibo.grabHtml("http://www.baidu.com")
print "over"