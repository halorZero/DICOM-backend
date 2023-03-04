from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
import os
import datetime
import shutil
from django.conf import settings

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'media')

@csrf_exempt
def dicom(request, url=os.path.join(MEDIA_ROOT, 'image-000001.dcm')):
    file = open(url, 'rb')
    res = FileResponse(file)
    res['Content-Type'] = 'application/octet-stream'
    res['Content-Disposition'] = 'attachment;filename="1.dcm"'
    return res


def upload(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        img1 = request.FILES.get('file1')
        img2 = request.FILES.get('file2')

        date_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f_') + str(name)
        print(date_name)

        img_name1 = date_name + '1.png'
        img_name2 = date_name + '2.png'
        f1 = open(os.path.join(MEDIA_ROOT, 'ximg', img_name1), 'wb')
        f2 = open(os.path.join(MEDIA_ROOT, 'ximg', img_name2), 'wb')
        for i in img1.chunks():
            f1.write(i)
        f1.close()
        for i in img2.chunks():
            f2.write(i)
        f2.close()

        # X 2 DICOM
        pass
        dicom_name = date_name + '.dcm'
        shutil.copyfile(os.path.join(MEDIA_ROOT, 'image-000001.dcm'), os.path.join(MEDIA_ROOT, 'dicom', dicom_name))
        # X 2 DICOM

        return dicom(request, url=os.path.join(MEDIA_ROOT, 'dicom', dicom_name))
