
# LuoNicus 2022 Mar 3  281879005@qq.com
# 有疑问联系

import time
from selenium.webdriver import Edge
from email.mime.text import MIMEText
import smtplib
import datetime


driverpath1 = "C:\\Program Files (x86)\\Microsoft\\Edge Beta\\Application\\msedgedriver.exe"
driverpath2 = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedgedriver.exe"

user_name = '*********'     # 填写你的登录账号
pass_word = '*********'     # 密码
sender_email = '*********@qq.com'        # 填写邮箱的发送者，建议 QQ邮箱
mail_password = '**********'             # 邮箱发送者的 password  注意 不是邮箱的密码，需要到邮箱设置里面找到
receiver_email = '*********@163.com'      # 接收邮箱的账号，建议网易邮箱




def main_runner(username, password):
    try:
        br = Edge(executable_path=driverpath1)  # executable_path=driverpath
    except:
        br = Edge(executable_path=driverpath2)  # executable_path=driverpath
    br.get('https://xmuxg.xmu.edu.cn/app/214')
    time.sleep(0.5)
    br.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/button[3]').click()

    time.sleep(1)
    br.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[3]/div/form/p[1]/input').send_keys(username)
    bg = br.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[3]/div/form/p[2]/input[1]')  # 密码输入框
    bg.send_keys(password)
    bg.send_keys(u'\ue007')
    time.sleep(0.5)
    print(br.current_url)
    if br.current_url == "https://xmuxg.xmu.edu.cn/platform":
        print("密码正确！")
    else:
        print("密码错误")
        try:  # 密码错误
            msg = br.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[3]/div/form/span').text
            print(msg)
        except:
            pass
        br.quit()
        return "密码错误"

    # 密码正确
    br.get('https://xmuxg.xmu.edu.cn/app/214')  # 打卡界面
    time.sleep(3)
    br.find_element_by_xpath('//*[@id="mainM"]/div/div/div/div[1]/div[2]/div/div[3]/div[2]').click()  # 我的表单
    time.sleep(1)

    try:
        a = br.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div[4]/div/div[39]/div/div/div/span[2]/i').get_attribute(
            'disabled')



    except:  # 2021_04_09 发生此改动
        a = br.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div[3]/div/div[30]/div/div/div').get_attribute(
            'disabled')


    if a == 'true':
        print('今日打卡系统已经关闭！')
        br.quit()
        return '今日打卡系统已经关闭！'
    else:
        打卡状态 = br.find_element_by_xpath('//*[@id="select_1582538939790"]/div/div/span[1]').get_attribute('title')
        if 打卡状态 == '是 Yes':
            try:
                br.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div/span/span').click()

            except:  # 2021_04_09 发生此改动
                br.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/span/span').click()
            a = br.switch_to.alert
            a.accept()
            print('你已经打过了， 再打一次')
            br.quit()
            return '你已经打过了， 再打一次'
        else:
            # ”本人是否承诺所填报......“
            try:
                br.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div[4]/div/div[39]/div/div/div/span[2]/i').click()

            except:  # 2022_043_14修改
                br.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div[3]/div/div[30]/div/div/div').click()

            # ”是“
            try:  # 弹出式选择框
                br.find_element_by_xpath('/html/body/div[8]/ul/div/li/label/span[1]/i').click()
            except:  # 下拉式选择框
                br.find_element_by_xpath('/html/body/div[8]/ul/div/div[3]/li/label/span[2]').click()
            # 保存
            try:
                br.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div/span/span').click()

            except:  # 2021_04_09 发生此改动
                br.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/span/span').click()
            # 警告框
            a = br.switch_to.alert
            print('你没打过， 给你打了')
            a.accept()
            br.quit()
            return '你没打过， 给你打了'
            time.sleep(100)


'''下面用于获取当前时间：分 秒'''
def Current_time(time=datetime.datetime.now()):
    """截取时分秒"""
    new_time = str(time)
    hour = new_time[11:19]
    return "".join(hour)



'''下面用于实现打卡成功后发送邮件提醒'''
def send_email():
    now_time = Current_time()
    msg = MIMEText(f'Everything will be OK!! Successful check-in.\n时间：{now_time}', 'plain', 'utf-8')
    sender = sender_email
    password = mail_password
    # 收件箱地址
    receiver = receiver_email
    # smtp服务器
    smtp_server = 'smtp.qq.com'
    # 发送邮箱地址
    msg['From'] = sender
    # 收件箱地址
    msg['To'] = receiver
    # 主题，主题也必须是有意义的内容，否则同样会被识别为垃圾邮件，无法发送
    msg['Subject'] = '打卡小助手'
    server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
    server.login(sender, password)  # ogin()方法用来登录SMTP服务器
    server.sendmail(sender, receiver, msg.as_string())


if __name__=='__main__':
    main_runner(user_name, pass_word)
    send_email()
    print("打卡任务已经完成")