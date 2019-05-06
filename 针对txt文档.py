import re
f=open('A卷.txt','r',encoding='utf-8')
txt=''
txt=f.read()
#针对wold中的填空题的特殊情况进行处理
for i in range(4):
    findchr='★'+str(i+1)+'★'
    start,end=0,0
    count=0
    for match in re.finditer(findchr,txt):
        if count:
            end=match.start()
        else:
            start=match.end()
        count+=1
##    print('第'+str(i+1)+'次：'+'{},{}'.format(start,end))
    vicetxt=txt[start+1:end]
    vicetxt=re.sub(r' {4,}','____',vicetxt)
    vicetxt=re.sub(r'　+','____',vicetxt)
    txt=txt[:start+1]+vicetxt+txt[end:]
    txt=txt.replace('★'+str(i+1)+'★','')
#删除行首空格
txt=re.sub('^ +','',txt,flags=re.M)
#删除多余空格及换行符
txt=re.sub(' {2,}','',txt)
txt=re.sub('　+','',txt)
txt=re.sub('\n{2,}','',txt)
#进一步删除换行符及Tab键
txt=txt.replace('\n','▲')
txt=txt.replace('\t','')
#去除... ...
txt=re.sub('\.{2,} ','.',txt)
txt=re.sub('\.{2,}','：',txt)
#规范填空题的下划线
txt=re.sub('_+▲?_*','____',txt)
txt=re.sub('_+','____',txt)
#规范括号
txt=txt.replace('(','（')
txt=txt.replace(')','）')
txt=re.sub(r'（[ 　]*?）','( )',txt)
f1=open('save1.txt','w',encoding='utf-8')
f1.write(txt)
f.close()
f1.close() 
#校验文件
f=open('A卷.txt','r',encoding='utf-8')
f1=open('save1.txt','r',encoding='utf-8')
txt1=f.read()
txt2=f1.read()
count1,count2=0,0
for t in txt1:
    if 0x6e00<=ord(t)<=0x9fa5:
        count1+=1
for t in txt2:
    if 0x6e00<=ord(t)<=0x9fa5:
        count2+=1
print(count1,count2)
f.close()
f1.close()
