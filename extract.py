# 吧kdconv数据集转化为chatgpt需要的多轮数据集.

import json #读入https://github.com/zhangbo2008/KdConv 数据,把他转化为标注数据集.
with open('film/train.json', 'r') as f:
    s1 = json.load(f)
save=[]
for i in s1:
    a=i['messages']#里面的所有对话.
    asks=[]
    answs=[]
    ans=''
    ask=''
    for dex,j in enumerate(a):

        if len(j)==1 :#碰到1就存.
            asks.append(ask)
            answs.append(ans)
            ans=''
            ask=j['message']
        if len(j)==2:
            ans+=j['message']#否则就一直叠加答案.
        if  dex==len(a)-1:#最后一个了也进行提交.
            asks.append(ask)
            answs.append(ans)
    asks=[i for i in asks if i]
    answs=[i for i in answs if i]
    #========加入history的处理.
    if len(asks)!=len(answs):#=========如果不是规范数据集我们跳过吧!!!!!!
        continue
    
    for dex,i in enumerate(asks):
        tmp={}
        tmp['prompt']=i
        tmp['response']=answs[dex]

        a=asks[:max(0,dex)]
        b=answs[:max(0,dex)]
        h=[]
        for i1 in range(len(a)):
            h.append(a[i1])
            h.append(b[i1])
        tmp['history']=h
        print(1)
        save.append(tmp)







            
print(1)


with open('film/extract_train.json', 'w') as f:
   f.write(json.dumps(save, indent=4,ensure_ascii=False))