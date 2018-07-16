import requests
from bs4 import BeautifulSoup
requestdata=r'''<?xml version="1.0"?><Function name="queryOrderByCondForFront" serviceName="com.ztesoft.iom.order.client.OrderQueryClient" userTransaction="false" generatedTime="2018-07-14 20:12:16"><Param type="o"><ntacheIds/><aareaIds><sItem>103</sItem><sItem>1013</sItem><sItem>1015</sItem><sItem>1017</sItem><sItem>1019</sItem><sItem>1021</sItem><sItem>1023</sItem><sItem>1049</sItem><sItem>391</sItem><sItem>402</sItem><sItem>403</sItem><sItem>404</sItem><sItem>405</sItem><sItem>406</sItem><sItem>407</sItem><sItem>408</sItem><sItem>409</sItem><sItem>410</sItem><sItem>411</sItem><sItem>412</sItem></aareaIds><nserviceIds/><sorderCode>njc201508181552441871278</sorderCode><ncustOrderCode/><naccNbr/><nisOverTime/><nqryType/><norderType/><norderClass/><norderPriority/><norderState/><nstartDate/><sflowIds></sflowIds><nendDate/><nalertStartDate/><nalertEndDate/><nlimitStartDate/><nlimitEndDate/><norderStartDate/><norderEndDate/><nreasonIds/><ncustTypes/><ncustGrades/><norderTitle/><npartyName/><nacceptStaff/><ncustManagerName/><sisLike>on</sisLike><nisBindRes/><nisOver/><nprodIds/><sspecialNbr></sspecialNbr><ncustAddress/><nacceptOrgIds/><nexchIds/><squeryType>orderQuery</squeryType><istaffId>133779</istaffId></Param><Param type="i">1</Param><Param type="i">200</Param></Function>'''
print(requestdata)
headers = {

            'Referer': r'http://132.228.176.109/IOMPROJ/order/orderQueryList.htm',
            'Accept-Language': r'zh-Hans-CN,zh-Hans;q=0.5',
            'Accept-Encoding': r'gzip, deflate',
            'User-Agent': r'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)',
            'Host': r'132.228.176.109',
            'Content-Length': r'1262',
            'Connection': r'Keep-Alive',
            'Pragma': r'no-cache',
            'Cookie': r'uam_monitor=19aa3baa8f7942249d4ac291486; JSESSIONID=0000tpIfZl94og9S5AX2GJZNwSG:1ar2s9j5j'
}
print(headers)
r = requests.post('http://132.228.176.109/IOMPROJ/busifacadeservlet', data=requestdata, headers=headers)




print(r.text)

'''这个函数用于处理内容为空的'''
def  getText(fx):
    if not fx:
        return "无"
    else:
        return fx.get_text()


con=BeautifulSoup(r.text,"lxml")
print(con)
for x in con.find_all("oitem"):
    print(x.lid.text+"-"+x.sworkordercode.text+"-"+getText(x.sworkresult))
