#用户输入美元
dollar = int(input('请输入美元金额：'))
#汇率
exchang_rate = 7.017
rmb = dollar * exchang_rate
print(str(dollar)+'美元等于' +str(rmb)+ '人民币')