##删除两个文件夹内不一致的文件

import os 

#图片地址
image_dir = r"G:\DOTA\test\all\images"
#标注文件地址 
label_dir = r"G:\DOTA\test\all\labels"

#获取所有图片文件名(不包含后缀)
image_files = set(os.path.splitext(f)[0] for f in os.listdir(image_dir) if f.endswith(".jpg"))

#获取所有标注文件名(不含后缀)
label_files = set(os.path.splitext(f)[0] for f in os.listdir(label_dir) if f.endswith(".txt"))

#获取共同存在但文件后缀不一样的文件名
common_filenames = image_files & label_files

#删除不在共同文件夹列表的文件
for f in os.listdir(image_dir):
    #如果文件名不在共同文件名列表中或者不是jpg文件,则删除
    if os.path.splitext(f)[0] not in common_filenames or not f.endswith(".jpg"):
        os.remove(os.path.join(image_dir,f))

for f in os.listdir(label_dir):
    #如果文件名不在共同文件名列表中或者不是txt文件,则删除
    if os.path.splitext(f)[0] not in common_filenames or not f.endswith(".txt"):
        os.remove(os.path.join(label_dir,f))
