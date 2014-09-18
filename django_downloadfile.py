# 文件下载
def DownloadFile(request, filename):
    import os

    filepath = os.path.join(settings.MEDIA_ROOT, 'docs/' + filename)

    def readFile(fn, buf_size=262144):
        f = open(fn, "rb")
        while True:
            c = f.read(buf_size)
            if c:
                yield c
            else:
                break
        f.close()

    # response = HttpResponse(readFile(filepath),mimetype='application/octet-stream')
    response = HttpResponse(readFile(filepath), content_type='application/octet-stream')

    return response
