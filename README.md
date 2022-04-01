# XMU_autodaka
用于厦门大学的每日健康打卡，支持邮件提醒功能！
It is used to punch in the daily health card for students of Xiamen University.

1:安装驱动到指定文件夹，驱动可在官网下载，注意与自己的浏览器版本号对应。使用windows自带浏览器。
  path:"C:\\Program Files (x86)\\Microsoft\\Edge Beta\\Application\\msedgedriver.exe"

2：修改如下四个部分：            user_name = '*********'                   # 填写你的登录账号
                               pass_word = '*********'                  # 密码
                               sender_email = '*********@qq.com'        # 填写邮箱的发送者，建议 QQ邮箱
                               mail_password = '**********'             # 邮箱发送者的 password  **注意** -->> 不是邮箱的密码，需要到邮箱设置里面找到,用来登录SMTP服务器.
                               receiver_email = '*********@163.com'      # 接收邮箱的账号，建议网易邮箱
                               
3：尝试运行，若成功，点击“一键生成”  会生成.exe文件
4：设置电脑定时启动即可。
