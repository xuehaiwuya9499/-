from PIL import Image
import numpy as np

def cutPhoto():
    global catchPhoto
    n,m=catchPhoto.shape
    whitePhoto=np.full((n,m),255)
    whitePhoto[:,5:m-5]=catchPhoto[:,5:m-5]
    
try:
    for c in range(140):
        filename='image'+str(c+1)+'.tmp'
        catchPhoto=np.array(Image.open(filename).convert('L'))
        cutPhoto()
        ls=[]
        a,b=catchPhoto.shape
        for i in range(a):
            for j in range(b):
                if catchPhoto[i,j]<=10:
                    ls.append(i)
                    break
        lsabc=[]
        downPointer1,upPointe1=0,1
        catchLs=np.array(ls)
        count=0
        while True:
            try:
                if catchLs[upPointe1]==catchLs[downPointer1]+1+count:
                    upPointe1+=1
                    count+=1
                    continue
                else:
                    count=0
                    lsabc.append([catchLs[downPointer1],catchLs[upPointe1-1]])
                    downPointer1=upPointe1
                    upPointe1+=1
                    continue
            except:
                lsabc.append([catchLs[downPointer1],catchLs[upPointe1-1]])
                break
        gap=3
        whitePhoto=np.full((len(ls)+gap*(len(lsabc)-1),b),255)
        data1=0
        suv=0
        for k in range(len(lsabc)):
            be1,up1=lsabc[k]
            data1=up1-be1+1
            whitePhoto[suv+gap*k:suv+gap*k+data1,:]=catchPhoto[be1:up1+1,:]
            suv+=data1
        im=Image.fromarray(whitePhoto.astype('uint8'))
        im.save('./123/'+str(c+1)+'.jpg','jpeg')
except:
    pass
print('Done!')
