# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 20:41:21 2019

@author: Pope  Zheng
"""
print('''这是一个友好的小工具箱
您现在有一个菜单进行选择
1.输入字符串进行加密或解密
2.输入字符串生成JSON字符串和新字典
3.输入.txt文件生成二维码并存入您的电脑
请您输入序号使用相应的功能''')
selection=input('请您输入序号以使用相应功能')
if selection=='1':
    import base64
    print('1.加密，2.解密')
    number=input('请您输入相应序号')
    if number=='1':
        string1=input('请您输入要加密的字符串:'); 
        transtring1= base64.b64encode(string1.encode('utf-8'))
        print("您所得的加密串为:",str(transtring1,'utf-8'))
    if number=='2':
        while True:
            string2=input('请您输入需要解密的字符串')
            try:
                transtring2=base64.b64decode(string2.encode('utf-8'))
                print('您所获得的解密串为:',str(transtring2,'utf-8'))
            except:
                print('您的输入非法，请输入合法的字符串！')
                continue
            if(True):
                break
if selection=='2':
    while True:
        try:
            string3=input('请您输入需要处理的字符串 注意输入格式为{"a":1}型的格式')
            dictionary1=eval(string3)
            print(dictionary1)
            import json
            json_string=json.dumps(dictionary1)
            print('您所得的json字符串为',json_string)
            kind1=type(json_string)
            print('您所得的json字符串type为:',kind1)
            L1=dictionary1.keys()
            L2=dictionary1.values()
            dictionary2={}
            for value in L2:
                dictionary2[value]=[]
            for key in L1:
                if dictionary1[key]==value:
                    dictionary2[value].append(key)
            print('您所得的新字典为:',dictionary2)
            kind2=type(dictionary2)
            print('您所得的新字典的type为:',kind2)   
        except:
            print('您的输入非法，请输入合法的字符串!')
            continue
        if(True):
            break
if selection=='3':
   while True:
        file=input('请输入您需要处理的文件:')
        try:
            f=open(file)
            lines=f.read()
            import qrcode
            img=qrcode.make(lines)
            print('现在显示的是您的二维码:')
            print('如果二维码未能显现，请您下载Python图形库进行查看')
            img.show()
            img.save('test.jpg')
            print('已将您所得的二维码保存至test.jpg')
        except:
            print('文件读取发生错误，请您规范文件内容')
            continue
        if(True):
            break
    
    
    
    
    
        
    
            

    

            
        
        
        
        
        
        
        
        
    

