score = []
maxs = 0
mins = 100
total = 0
maxn = ""
minn=""
for i in range(5):
    n=int(input(":"))
    score.append(n)
    name=input("name:")
    
    if n>maxs:
        maxs = n
        maxn = name
    if n<mins:
        mins=n
        minn=name
    total = total+n
s = total/len(score)
print('總分',total)
print("平均",s)
print("最高",maxs,maxn)
print("最低",mins,minn)