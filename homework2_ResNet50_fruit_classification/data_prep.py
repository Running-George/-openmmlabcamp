
import random
import shutil
import os


basepath = './fruit30_train'
folders=os.listdir(basepath)
os.mkdir('train')
os.mkdir('test')
os.mkdir('val')
ratio = 0.8 # split ratio
for folder in folders: # loop over the 30 folders
   contents = os.listdir(os.path.join(basepath, folder)) 
   random.shuffle(contents)  # shuffle the result
   split_point = round(ratio * len(contents))

   os.makedirs(os.path.join('train',folder))
   os.makedirs(os.path.join('test',folder))
   os.makedirs(os.path.join('val',folder))
   for img in contents[:split_point]:
       src_path = os.path.join(os.path.join(basepath, folder), img)
       dst_path = os.path.join('train',folder,img)
       shutil.copy(src_path, dst_path)
   for img in contents[split_point:]:
       src_path = os.path.join(os.path.join(basepath, folder), img)
       dst_path = os.path.join('test',folder,img)
       dst_path_2 = os.path.join('val',folder,img)
       shutil.copy(src_path, dst_path)
       shutil.copy(src_path, dst_path_2)