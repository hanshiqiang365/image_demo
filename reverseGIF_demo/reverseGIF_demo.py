#author: hanshiqiang365 （微信公众号：韩思工作室）
from PIL import Image, ImageSequence

filename = "mobike_change.gif" #sys.argv[1]

im = Image.open(f'resources/{filename}') 
sequence = []

for f in ImageSequence.Iterator(im):
    sequence.append(f.copy())    

sequence.reverse()
sequence[0].save(f'resources/reversed_{filename}',save_all = True, append_images=sequence[1:]) #倒放的gif图保存在当前目录下
