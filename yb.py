from bs4 import BeautifulSoup
import requests
import re 
import os
from urllib.request import urlretrieve

for i in range(1,10):
    url = 'http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=HYSR&mkt=0&stat=0&cmd=4&code=&sc=&ps=50&p='+str(i)+'&js=var%20KvxgytuM={"data":[(x)],"pages":"(pc)","update":"(ud)","count":"(count)"}&rt=51811901'
    r = requests.get(url)
    r.encoding = 'utf-8'
    demo = r.text  # 服务器返回响应
    fp1 = r"(?<=var KvxgytuM).+?(?=],)"
    pattern = re.compile(fp1)
    results = str(pattern.findall(demo))
    s= results.replace(r'''={"data":[''','').replace(r''']''','').replace(r'''\'']''','')
    s1=s.split('","',-1)
    
    
    for item in s1:
        a=item.split(',',-1)
        time=a[1]
        b=time.split()
        c=b[0]
        d=c.split('/')

        if int(d[1])<10:
            d[1]="0"+d[1]
        if int(d[2])<10:
            d[2]='0'+d[2]
        e=d[0]+d[1]+d[2]

        urlpdf1=a[2]
        comp=a[4]
        name=a[9]
        hy=a[10]
        pdfsource =  r"http://data.eastmoney.com/report/"+e+"/hy,"+urlpdf1+".html"
        print(pdfsource)
        pdfpage = requests.get(pdfsource)
        pdfpage.encoding = 'gb2312'
        pdfpagetext = pdfpage.text
        fp2=r"(?<=http://pdf.dfcfw.com/pdf/).+?(?=pdf)"
        pattern2 = re.compile(fp2)
        results2 = pattern2.findall(pdfpagetext)
        a=os.path.exists("./%r" %(hy))
        if a!=1:
            os.mkdir("./%r" %(hy))
        if results2 != []:
            pdfurl=r"http://pdf.dfcfw.com/pdf/"+results2[0]+"pdf"
            print(pdfurl)
            urlretrieve(pdfurl, "./%r/%r.pdf" %(hy, name) )
            
           
            print(name)
