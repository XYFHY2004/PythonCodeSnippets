# 在django中使用代码保存ImageField和FileField。
# 存储后的路径django会根据settings中media的设
# 置进行自动处理,即:路径字符串不包含media设置
#的值

from django.core.files import File
 

f = File(open('path_to_file','r'))
 
m = MyModelInstance
 
m.ImageFieldName = f

m.FileFieldName = f
 
m.save()
