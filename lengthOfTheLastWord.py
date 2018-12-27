str = input()
index = len(str)-1
count = -1 #末尾的空格数
flag = False #遇到过字符了？

while (index>=0):
	#记录扫描到到第一个非空字符时已扫描过多少个空字符
    if str[index] != ' ' and count == -1:
        flag = True
        count = len(str)-1-index
    #在已发现非空字符的情况下，如果遇到空字符，就退出
    if str[index]==' ' and flag == True:
        #print("（情况一）\r\n")
        break;        
        
    index-=1
    #扫描结束了
    if index<0 :
        #始终未发现非空字符
        if flag == False:
            #print("（情况三）\r\n");
            count = len(str)
        #发现了非空字符，但是后面没有再遇到空格
        else :
            #print("（情况二）\r\n");
            pass
    #print(len(str)-1,index,count)
if count == -1:
    count = 0
    #print("（情况四）\r\n")
print(len(str)-1-index-count)

'''
从字符尾部开始扫描，要完整提取最后一个单词可能会遇到以下情况:
注：在分类的时候，"空格"代表单个或多个连续空格，"字符"代表单个或多个连续字符
1.遇到字符->遇到空格  √（情况一）
2.遇到字符->没遇到空格 √（情况二）
3.遇到空格->遇到字符->遇到空格 √（情况一）
4.遇到空格->遇到字符->没遇到空格 √（情况二）
6.遇到空格->没遇到字符 √（情况三）

7.【注意】字符串为空（情况四）

'''