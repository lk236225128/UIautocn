# UIautocn
# UIautocn
- 一套基于Pytest+selenium+appium的UI自动化框架,适用于web,android,iOS
- 尚未完工

# 使用

直接通过yaml进行配置控件 ,样例说明如下:
```
testinfo:
    - id: test001
      title: 8891中古车登录用例
      info: 打开app
testcase:
    - element_info: com.addcn.car8891:id/close
      find_type: id
      operate_type: click
      info: 关闭新手引导图
    - element_info: //android.widget.TextView[@text='會員中心']
      find_type: xpath
      operate_type: click
      info: 点击会员中心
    - element_info: com.addcn.car8891:id/login
      find_type: id
      operate_type: click
      info: 点击登录
    - element_info: com.addcn.car8891:id/user_ed
      find_type: id
      operate_type: set_value
      msg: majia
      info: 输入用户名
    - element_info: com.addcn.car8891:id/password_ed
      find_type: id
      operate_type: set_value
      msg: "a123456"
      info: 输入密码
    - element_info: com.addcn.car8891:id/login_btn
      find_type: id
      operate_type: click
      info: 提交登录按钮
    - element_info: com.addcn.car8891:id/setting
      find_type: id
      operate_type: click
      info: 点击设置菜单
    - element_info: com.addcn.car8891:id/out
      find_type: id
      operate_type: click
      info: 点击登出
```

### 运行
```
python run.py
```
