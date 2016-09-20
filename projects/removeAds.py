#!usr/bin/python
# ! _*_coding:utf-8_*_

import os,re

import sys,time,glob


'''
    这是给Android_Killer做的插件，要放到ak路径下的projects目录中
    然后在工具选项中自定义工具中添加下就可以点击运行了
    不过需要Python2.7的环境支持，python 3.0没有试过
'''
def removeAd(dir_path):
    inject_body = "    \n.locals 0\nreturn-void\n.end method\n"
    mat = re.compile(r'loadad',re.I)
    for root,dirs,files in os.walk(dir_path):
        for file in files:
            fop = open(root+os.sep+file,'r')
            fout = open(root+os.sep+file+"_",'w')
            print(root+os.sep+file)
            while True:
                line = fop.readline()
                if not line :
                    fop.close()
                    fout.flush()
                    fout.close()
                    break
                # print("hehe+",line)
                # print(mat.search(line))
                # print(mat.search(line) !=None and ".method" in line and ")V" in line and "abstract" not in line)
                if mat.search(line) !=None and ".method" in line and ")V" in line and "abstract" not in line:
                    fout.writelines(line)
                    fout.writelines(inject_body)
                    while True:
                        line = fop.readline()
                        if ".end method" in line :
                            break
                else:
                    fout.writelines(line)
            os.remove(root+os.sep+file)
            os.rename(root+os.sep+file+"_",root+os.sep+file)



'''
    这是给Android_Killer做的插件，要放到ak路径下的projects目录中
    然后在工具选项中自定义工具中添加下就可以点击运行了
    不过需要Python2.7的环境支持，python 3.0没有试过
'''
if __name__ =='__main__':
    # dir_path = r"E:\android killer\projects\sign_apk\Project\smali"
    os.path.abspath(sys.argv[0])
    #当前系统的时间
    nowTime = time.time()
    nowFile = []
    isFirst = True
    for sub_file in glob.glob(os.getcwd()+os.sep+"*"):
        print(os.getcwd())
        #获取文件的修改时间
        md_time = os.path.getmtime(sub_file)
        # print(md_time)
		
        if isFirst:
            if "removeAds.py" in sub_file:
                continue
            isFirst = False
            nowFile.append(sub_file)
            nowFile.append(md_time)
            nowFile.append(nowTime-md_time)
            #判断创建时间是不是小于5分钟，如果是的话终止循环
            if nowFile[2]<=300:
                break
        else:
            if "removeAds.py" in sub_file:
                continue
            if md_time>nowFile[1]:
                nowFile[0] = sub_file
                nowFile[1] = md_time
                nowFile[2] = [nowTime-md_time]
                if nowFile[2] <= 300:
                    break

    dir_path = nowFile[0] + os.sep +"Project"+os.sep+"smali"
    print(dir_path)
            # print(md_time)
    # print(datetime.datetime.now().minute)
    # print(time.time())
    removeAd(dir_path)
    os.system("pause")
