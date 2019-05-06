import re
f=open('zs.txt','r',encoding='utf-8')
txt=''
txt=f.read()
#删除行首空格
txt=re.sub('^ +','',txt,flags=re.M)
#针对word中的填空题的特殊情况进行处理
findchr='二、填空题'+'.+?'+'三、选择题'
start,end=0,0
txt1=txt
count=1
for match in re.finditer(findchr,txt,flags=re.S):
    end=match.end()
    start=match.start()
    print(end-start)
    vicetxt=txt[start:end]
    vicetxt=re.sub(r' {2,}','____',vicetxt)
    vicetxt=re.sub(r'　+','____',vicetxt)
    if count==1:
        txt1=txt[:start]+vicetxt
    elif count<=10:
        txt1=txt1+txt[endbefore:start]+vicetxt
    else:
        txt1=txt1+txt[endbefore:start]+vicetxt+txt[end:]
    count+=1
    endbefore=end
#删除行首空格
txt1=re.sub('^ +','',txt1,flags=re.M)
#删除多余空格及换行符
txt1=re.sub(' {2,}','',txt1)
txt1=re.sub('　+','',txt1)
txt1=re.sub('\n{2,}','',txt1)
#进一步删除换行符及Tab键
txt1=txt1.replace('\n','▲')
txt1=txt1.replace('\t','')
#去除... ...
txt1=re.sub('\.{2,} ','.',txt1)
txt1=re.sub('\.{2,}','：',txt1)
#规范填空题的下划线
txt1=re.sub('_+▲?_*','____',txt1)
txt1=re.sub('_+','____',txt1)
#规范括号
txt1=txt1.replace('(','（')
txt1=txt1.replace(')','）')
txt1=re.sub(r'（[ 　]*?）','( )',txt1)
f1=open('save1.txt','w',encoding='utf-8')
f1.write(txt1)
f.close()
f1.close() 
