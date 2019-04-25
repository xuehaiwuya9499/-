import re
f=open('1.txt','r',encoding='utf-8')
txt=''
ls=f.readlines()
#删除行首空格
for t in ls:
    txt+=re.sub('^ +','',t)
#删除多余空格及换行符
txt=re.sub(' {2,}','',txt)
txt=re.sub('\n{2,}','',txt)
#进一步删除换行符及Tab键
txt=txt.replace('\n','*')
txt=txt.replace('\t','')
#去除... ...
txt=re.sub('\.{2,} ','.',txt)
txt=re.sub('\.{2,}','：',txt)
#规范括号
txt=txt.replace('(','（')
txt=txt.replace(')','）')
txt=re.sub(r'（[ 　]*?）','( )',txt)
f1=open('save1.txt','w',encoding='utf-8')
f1.write(txt)
f.close()
f1.close() 
