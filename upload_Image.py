# ajax 上传用户头像

def UploadUserface(request):
    if request.method == 'POST':
        if request.FILES.__len__() > 0:
            image = request.FILES.values()[0]
            if image:
                result,filename = upload(image)
                if result:
                   return HttpResponse(json.dumps(filename), mimetype='application/json')
        return render_to_response('')

def upload(file):
    '''''图片上传函数'''
    import os
    import uuid
    if file:
        path=os.path.join(settings.MEDIA_ROOT,'images/upload')
        file_name=str(uuid.uuid1())+".jpg"
        path_file=os.path.join(path,file_name)
        destination = open(path_file, 'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()
        return True,file_name
    return False,''
