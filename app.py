from flask import Flask, render_template, session, redirect, url_for
import requests
from bs4 import BeautifulSoup
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField, BooleanField

from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
bootstrap = Bootstrap(app)


class NameForm(Form):
    ordercode = StringField("定单编码:")
    accnbr = StringField("业务编号：")
    islike = BooleanField("是否模糊匹配")
    submit = SubmitField("搜索")


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    returned = ''
    if form.validate_on_submit():
        session['ordercode'] = form.ordercode.data
        print(form.islike.data)
        if form.islike.data:
            if form.accnbr.data.strip() == '' and form.ordercode.data.strip() != '':
                requestdata = r'''<?xml version="1.0"?><Function name="queryOrderByCondForFront" serviceName="com.ztesoft.iom.order.client.OrderQueryClient" userTransaction="false" generatedTime="2018-07-14 20:12:16"><Param type="o"><ntacheIds/><aareaIds><sItem>103</sItem><sItem>1013</sItem><sItem>1015</sItem><sItem>1017</sItem><sItem>1019</sItem><sItem>1021</sItem><sItem>1023</sItem><sItem>1049</sItem><sItem>391</sItem><sItem>402</sItem><sItem>403</sItem><sItem>404</sItem><sItem>405</sItem><sItem>406</sItem><sItem>407</sItem><sItem>408</sItem><sItem>409</sItem><sItem>410</sItem><sItem>411</sItem><sItem>412</sItem></aareaIds><nserviceIds/><sorderCode>%s</sorderCode><ncustOrderCode/><naccNbr/><nisOverTime/><nqryType/><norderType/><norderClass/><norderPriority/><norderState/><nstartDate/><sflowIds></sflowIds><nendDate/><nalertStartDate/><nalertEndDate/><nlimitStartDate/><nlimitEndDate/><norderStartDate/><norderEndDate/><nreasonIds/><ncustTypes/><ncustGrades/><norderTitle/><npartyName/><nacceptStaff/><ncustManagerName/><sisLike>on</sisLike><nisBindRes/><nisOver/><nprodIds/><nspecialNbr/><ncustAddress/><nacceptOrgIds/><nexchIds/><squeryType>orderQuery</squeryType><istaffId>133779</istaffId></Param><Param type="i">1</Param><Param type="i">200</Param></Function>''' % (
                    form.ordercode.data)
            elif (form.accnbr.data.strip() != '') and (form.ordercode.data.strip() == ''):
                requestdata = r'''<?xml version="1.0"?><Function name="queryOrderByCondForFront" serviceName="com.ztesoft.iom.order.client.OrderQueryClient" userTransaction="false" generatedTime="2018-07-14 20:12:16"><Param type="o"><ntacheIds/><aareaIds><sItem>103</sItem><sItem>1013</sItem><sItem>1015</sItem><sItem>1017</sItem><sItem>1019</sItem><sItem>1021</sItem><sItem>1023</sItem><sItem>1049</sItem><sItem>391</sItem><sItem>402</sItem><sItem>403</sItem><sItem>404</sItem><sItem>405</sItem><sItem>406</sItem><sItem>407</sItem><sItem>408</sItem><sItem>409</sItem><sItem>410</sItem><sItem>411</sItem><sItem>412</sItem></aareaIds><nserviceIds/><norderCode/><ncustOrderCode/><naccNbr/><nisOverTime/><nqryType/><norderType/><norderClass/><norderPriority/><norderState/><nstartDate/><sflowIds></sflowIds><nendDate/><nalertStartDate/><nalertEndDate/><nlimitStartDate/><nlimitEndDate/><norderStartDate/><norderEndDate/><nreasonIds/><ncustTypes/><ncustGrades/><norderTitle/><npartyName/><nacceptStaff/><ncustManagerName/><sisLike>on</sisLike><nisBindRes/><nisOver/><nprodIds/><sspecialNbr>%s</sspecialNbr><ncustAddress/><nacceptOrgIds/><nexchIds/><squeryType>orderQuery</squeryType><istaffId>133779</istaffId></Param><Param type="i">1</Param><Param type="i">200</Param></Function>''' % (
                    form.accnbr.data)
            else:
                requestdata = r'''<?xml version="1.0"?><Function name="queryOrderByCondForFront" serviceName="com.ztesoft.iom.order.client.OrderQueryClient" userTransaction="false" generatedTime="2018-07-14 20:12:16"><Param type="o"><ntacheIds/><aareaIds><sItem>103</sItem><sItem>1013</sItem><sItem>1015</sItem><sItem>1017</sItem><sItem>1019</sItem><sItem>1021</sItem><sItem>1023</sItem><sItem>1049</sItem><sItem>391</sItem><sItem>402</sItem><sItem>403</sItem><sItem>404</sItem><sItem>405</sItem><sItem>406</sItem><sItem>407</sItem><sItem>408</sItem><sItem>409</sItem><sItem>410</sItem><sItem>411</sItem><sItem>412</sItem></aareaIds><nserviceIds/><sorderCode>%s</sorderCode><ncustOrderCode/><naccNbr/><nisOverTime/><nqryType/><norderType/><norderClass/><norderPriority/><norderState/><nstartDate/><sflowIds></sflowIds><nendDate/><nalertStartDate/><nalertEndDate/><nlimitStartDate/><nlimitEndDate/><norderStartDate/><norderEndDate/><nreasonIds/><ncustTypes/><ncustGrades/><norderTitle/><npartyName/><nacceptStaff/><ncustManagerName/><sisLike>on</sisLike><nisBindRes/><nisOver/><nprodIds/><sspecialNbr>%s</sspecialNbr><ncustAddress/><nacceptOrgIds/><nexchIds/><squeryType>orderQuery</squeryType><istaffId>133779</istaffId></Param><Param type="i">1</Param><Param type="i">200</Param></Function>''' % (
                    form.ordercode.data, form.accnbr.data)



        else:
            if form.accnbr.data.strip() == '' and form.ordercode.data.strip() != '':
                requestdata = r'''<?xml version="1.0"?><Function name="queryOrderByCondForFront" serviceName="com.ztesoft.iom.order.client.OrderQueryClient" userTransaction="false" generatedTime="2018-07-14 20:12:16"><Param type="o"><ntacheIds/><aareaIds><sItem>103</sItem><sItem>1013</sItem><sItem>1015</sItem><sItem>1017</sItem><sItem>1019</sItem><sItem>1021</sItem><sItem>1023</sItem><sItem>1049</sItem><sItem>391</sItem><sItem>402</sItem><sItem>403</sItem><sItem>404</sItem><sItem>405</sItem><sItem>406</sItem><sItem>407</sItem><sItem>408</sItem><sItem>409</sItem><sItem>410</sItem><sItem>411</sItem><sItem>412</sItem></aareaIds><nserviceIds/><sorderCode>%s</sorderCode><ncustOrderCode/><naccNbr/><nisOverTime/><nqryType/><norderType/><norderClass/><norderPriority/><norderState/><nstartDate/><sflowIds></sflowIds><nendDate/><nalertStartDate/><nalertEndDate/><nlimitStartDate/><nlimitEndDate/><norderStartDate/><norderEndDate/><nreasonIds/><ncustTypes/><ncustGrades/><norderTitle/><npartyName/><nacceptStaff/><ncustManagerName/><nisLike/><nisBindRes/><nisOver/><nprodIds/><nspecialNbr/><ncustAddress/><nacceptOrgIds/><nexchIds/><squeryType>orderQuery</squeryType><istaffId>133779</istaffId></Param><Param type="i">1</Param><Param type="i">200</Param></Function>''' % (
                    form.ordercode.data)
            elif (form.accnbr.data.strip() != '') and (form.ordercode.data.strip() == ''):
                requestdata = r'''<?xml version="1.0"?><Function name="queryOrderByCondForFront" serviceName="com.ztesoft.iom.order.client.OrderQueryClient" userTransaction="false" generatedTime="2018-07-14 20:12:16"><Param type="o"><ntacheIds/><aareaIds><sItem>103</sItem><sItem>1013</sItem><sItem>1015</sItem><sItem>1017</sItem><sItem>1019</sItem><sItem>1021</sItem><sItem>1023</sItem><sItem>1049</sItem><sItem>391</sItem><sItem>402</sItem><sItem>403</sItem><sItem>404</sItem><sItem>405</sItem><sItem>406</sItem><sItem>407</sItem><sItem>408</sItem><sItem>409</sItem><sItem>410</sItem><sItem>411</sItem><sItem>412</sItem></aareaIds><nserviceIds/><norderCode/><ncustOrderCode/><naccNbr/><nisOverTime/><nqryType/><norderType/><norderClass/><norderPriority/><norderState/><nstartDate/><sflowIds></sflowIds><nendDate/><nalertStartDate/><nalertEndDate/><nlimitStartDate/><nlimitEndDate/><norderStartDate/><norderEndDate/><nreasonIds/><ncustTypes/><ncustGrades/><norderTitle/><npartyName/><nacceptStaff/><ncustManagerName/><nisLike/><nisBindRes/><nisOver/><nprodIds/><sspecialNbr>%s</sspecialNbr><ncustAddress/><nacceptOrgIds/><nexchIds/><squeryType>orderQuery</squeryType><istaffId>133779</istaffId></Param><Param type="i">1</Param><Param type="i">200</Param></Function>''' % (
                    form.accnbr.data)
            else:
                requestdata = r'''<?xml version="1.0"?><Function name="queryOrderByCondForFront" serviceName="com.ztesoft.iom.order.client.OrderQueryClient" userTransaction="false" generatedTime="2018-07-14 20:12:16"><Param type="o"><ntacheIds/><aareaIds><sItem>103</sItem><sItem>1013</sItem><sItem>1015</sItem><sItem>1017</sItem><sItem>1019</sItem><sItem>1021</sItem><sItem>1023</sItem><sItem>1049</sItem><sItem>391</sItem><sItem>402</sItem><sItem>403</sItem><sItem>404</sItem><sItem>405</sItem><sItem>406</sItem><sItem>407</sItem><sItem>408</sItem><sItem>409</sItem><sItem>410</sItem><sItem>411</sItem><sItem>412</sItem></aareaIds><nserviceIds/><sorderCode>%s</sorderCode><ncustOrderCode/><naccNbr/><nisOverTime/><nqryType/><norderType/><norderClass/><norderPriority/><norderState/><nstartDate/><sflowIds></sflowIds><nendDate/><nalertStartDate/><nalertEndDate/><nlimitStartDate/><nlimitEndDate/><norderStartDate/><norderEndDate/><nreasonIds/><ncustTypes/><ncustGrades/><norderTitle/><npartyName/><nacceptStaff/><ncustManagerName/><nisLike/><nisBindRes/><nisOver/><nprodIds/><sspecialNbr>%s</sspecialNbr><ncustAddress/><nacceptOrgIds/><nexchIds/><squeryType>orderQuery</squeryType><istaffId>133779</istaffId></Param><Param type="i">1</Param><Param type="i">200</Param></Function>''' % (
                    form.ordercode.data, form.accnbr.data)

            # requestdata=r'''<?xml version="1.0"?><Function name="queryOrderByCondForFront" serviceName="com.ztesoft.iom.order.client.OrderQueryClient" userTransaction="false" generatedTime="2018-07-14 20:12:16"><Param type="o"><ntacheIds/><aareaIds><sItem>103</sItem><sItem>1013</sItem><sItem>1015</sItem><sItem>1017</sItem><sItem>1019</sItem><sItem>1021</sItem><sItem>1023</sItem><sItem>1049</sItem><sItem>391</sItem><sItem>402</sItem><sItem>403</sItem><sItem>404</sItem><sItem>405</sItem><sItem>406</sItem><sItem>407</sItem><sItem>408</sItem><sItem>409</sItem><sItem>410</sItem><sItem>411</sItem><sItem>412</sItem></aareaIds><nserviceIds/><sorderCode>%s</sorderCode><ncustOrderCode/><naccNbr/><nisOverTime/><nqryType/><norderType/><norderClass/><norderPriority/><norderState/><nstartDate/><sflowIds></sflowIds><nendDate/><nalertStartDate/><nalertEndDate/><nlimitStartDate/><nlimitEndDate/><norderStartDate/><norderEndDate/><nreasonIds/><ncustTypes/><ncustGrades/><norderTitle/><npartyName/><nacceptStaff/><ncustManagerName/><nisLike/><nisBindRes/><nisOver/><nprodIds/><sspecialNbr>%s</sspecialNbr><ncustAddress/><nacceptOrgIds/><nexchIds/><squeryType>orderQuery</squeryType><istaffId>133779</istaffId></Param><Param type="i">1</Param><Param type="i">200</Param></Function>''' % (form.ordercode.data,form.accnbr.data)

        headers = {
            'Referer': r'http://132.228.176.109/IOMPROJ/order/orderQueryList.htm',
            'Accept-Language': r'zh-Hans-CN,zh-Hans;q=0.5',
            'Accept-Encoding': r'gzip, deflate',
            'User-Agent': r'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)',
            'Host': r'132.228.176.109',
            'Content-Length': r'1262',
            'Connection': r'Keep-Alive',
            'Pragma': r'no-cache',

        }
        r = requests.post('http://132.228.176.109/IOMPROJ/busifacadeservlet', data=requestdata, headers=headers)
        con = BeautifulSoup(r.text.replace("&lt;", "<").replace("&gt;", ">"), "lxml")
        print(con)
        returned = con.find_all("item")
        # for x in con.find_all("item"):
        #    returned=returned+x['ordercode']+'-'+x['ordertitle']+'<br>'
    return render_template("index.html", form=form, returned=returned)


'''这个函数用于处理内容为空的'''


def getText(fx):
    if not fx:
        return "无"
    else:
        return fx.get_text()


@app.route('/detail/<orderid>')
def get_detail(orderid):
    headers = {
        'Referer': r'http://132.228.176.109/IOMPROJ/yccustorder/transferOrderDetail.htm',
        'Accept-Language': r'zh-Hans-CN,zh-Hans;q=0.5',
        'Accept-Encoding': r'gzip, deflate',
        'User-Agent': r'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)',
        'Host': r'132.228.176.109',
        'Content-Length': r'224',
        'Connection': r'Keep-Alive',
        'Pragma': r'no-cache',

    }
    requestdata = r'''<?xml version="1.0"?><Function name="queryOrderInfoByKey" serviceName="com.ztesoft.iom.order.client.OrderQueryClient" userTransaction="false" generatedTime="2018-07-14 19:59:42"><Param type="s">%s</Param></Function>''' % (
        orderid)
    ##r是基本信息
    r = requests.post('http://132.228.176.109/IOMPROJ/busifacadeservlet', data=requestdata, headers=headers)
    con = BeautifulSoup(r.text, "lxml")
    print(con)
    returned = con.find("output")

    # r2是工单列表
    processinstanceid = getText(con.find("lprocessinstanceid"))
    if processinstanceid:
        r2 = get_workorder(processinstanceid)
    else:
        r2 = None

    r3 = get_ziyuan(orderid)

    r4=get_accessinfo(orderid)

    r5=get_sla(orderid)

    #print(r5)
    return render_template("detail.html", returned=returned, returned2=r2, returned3=r3,returned4=r4,returned5=r5)


def get_workorder(id):
    data = r'''<?xml version="1.0"?><Function name="queryWorkOrdersTransferOrderDetail" serviceName="com.ztesoft.iom.workorder.bl.WorkOrderQuery" userTransaction="false" generatedTime=""><Param type="i">%s</Param></Function>''' % (
        id)
    # print(data)
    headers = {
        'Accept': r'*/*',
        'Accept-Language': r'zh-CN',
        'Referer': r'http://132.228.176.109/IOMPROJ/yccustorder/transferOrderDetail.htm',
        'Accept-Encoding': r'gzip, deflate',
        'User-Agent': r'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)',
        'Host': r'132.228.176.109',
        'Content-Length': r'238',
        'Connection': r'Keep-Alive',
        'Pragma': r'no-cache',


    }

    r = requests.post('http://132.228.176.109/IOMPROJ/busifacadeservlet', data=data, headers=headers)
    # print(r.text)
    con = BeautifulSoup(r.text, "lxml")

    return con.find_all("oitem")
    ''' 
    con = BeautifulSoup(r.text, "lxml")
    returned = ''
    for x in con.find_all("oitem"):
        # print(x.lid.text + "-" + x.sworkordercode.text + "-" + getText(x.sworkresult))
        returned = returned + x.sworkordercode.text + "-" + getText(x.stachename) + "-" + getText(
            x.sworkresult) + "-" + getText(x.spartyname) + "-" + getText(x.sdistillperson) + "-" + getText(
            x.sworkorderstatename) + "-" + getText(x.sworkordertypename) + "-" + getText(x.dcreatedate) + "-" + getText(
            x.dfinishdate) + "-" + getText(x.dlimitdate) + '<br/>'

  
          工单编码
           sworkordercode，处理环节
           stachename，工单级别，工单处理结果
           sworkresult，收单人
           spartyname，回单人
           sdistillperson，工单状态
           sworkorderstatename，工单类型
           sworkordertypename，派发时间
           dcreatedate，实际完成时间
           dfinishdate，要求完成时间
           dlimitdate
           '''


def get_ziyuan(id):
    data = r'''<?xml version="1.0"?><Function name="qryLinkInfo" serviceName="com.ztesoft.iom.workorder.bl.DoOtherManager" userTransaction="false" generatedTime="2018-07-14 20:02:28"><Param type="s">%s</Param><Param type="s"></Param></Function>''' % (
        id)
    # print(data)
    headers = {
        'Referer': r'http://132.228.176.109/IOMPROJ/yccustorder/transferOrderDetail.htm',
        'Accept-Language': r'zh-Hans-CN,zh-Hans;q=0.5',
        'Accept-Encoding': r'gzip, deflate',
        'User-Agent': r'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)',
        'Host': r'132.228.176.109',
        'Content-Length': r'238',
        'Connection': r'Keep-Alive',
        'Pragma': r'no-cache',


    }


    r = requests.post('http://132.228.176.109/IOMPROJ/busifacadeservlet', data=data, headers=headers)
    con = BeautifulSoup(r.text, "lxml")
    xml=BeautifulSoup()
    if con.find("sroute_text"):
        xml.append(con.find("sroute_text"))
    if con.find("sroutetextfull"):
        xml.append(con.find("sroutetextfull"))

    return xml
    # print(r.text)
    #return r.text


def get_accessinfo(id):
    data = r'''<?xml version="1.0"?><Function name="queryDkOrderInfoAttri" serviceName="com.ztesoft.iom.workorder.bl.DoOtherManager" userTransaction="false" generatedTime="2018-07-15 09:15:12"><Param type="s">%s</Param></Function>''' % (id)
    # print(data)
    headers = {
        'Referer': r'http://132.228.176.109/IOMPROJ/yccustorder/transferOrderDetail.htm',
        'Accept-Language': r'zh-Hans-CN,zh-Hans;q=0.5',
        'Accept-Encoding': r'gzip, deflate',
        'User-Agent': r'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)',
        'Host': r'132.228.176.109',
        'Content-Length': r'224',
        'Connection': r'Keep-Alive',
        'Pragma': r'no-cache'


    }

    r = requests.post('http://132.228.176.109/IOMPROJ/busifacadeservlet', data=data, headers=headers)
    con = BeautifulSoup(r.text, "lxml")
    return con.find("output")


def get_sla(id):
    data =r'''<?xml version="1.0"?><Function name="querySoSlaDto" serviceName="com.ztesoft.iom.order.client.OrderQueryClient" userTransaction="false" generatedTime="2018-07-15 09:43:13"><Param type="s">%s</Param></Function>''' % (id)
    # print(data)
    headers = {
        'Referer': r'http://132.228.176.109/IOMPROJ/yccustorder/transferOrderDetail.htm',
        'Accept-Language': r'zh-Hans-CN,zh-Hans;q=0.5',
        'Accept-Encoding': r'gzip, deflate',
        'User-Agent': r'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)',
        'Host': r'132.228.176.109',
        'Content-Length': r'224',
        'Connection': r'Keep-Alive',
        'Pragma': r'no-cache',


    }

    r = requests.post('http://132.228.176.109/IOMPROJ/busifacadeservlet', data=data, headers=headers)
    con = BeautifulSoup(r.text, "lxml")
    return con.find("output")

if __name__ == '__main__':
    app.run()
