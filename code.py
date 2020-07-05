
def code():
        tryCode = input("请输入验证码：")
        print('您的验证码为'+str(tryCode))
        if tryCode=='123456':
                print('验证成功')
        else:
                print('验证失败')


code()

