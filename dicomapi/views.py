from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import datetime
import shutil
from django.conf import settings


@csrf_exempt
def dicom(request, url=os.path.join(settings.MEDIA_ROOT, 'dcm11/1-001.dcm')):
    file = open(url, 'rb')
    res = FileResponse(file)
    res['Content-Type'] = 'application/octet-stream'
    res['Content-Disposition'] = 'attachment;filename="1.dcm"'
    return res

@csrf_exempt
def dicom2(request, url=os.path.join(settings.MEDIA_ROOT, 'dcm11/1-001.dcm')):
    file = open(url, 'rb')
    res = FileResponse(file)
    res['Content-Type'] = 'application/octet-stream'
    res['Content-Disposition'] = 'attachment;filename="1.dcm"'
    return res

@csrf_exempt
def dicom3(request, url=os.path.join(settings.MEDIA_ROOT, 'dcm11/1-001.dcm')):
    file = open(url, 'rb')
    res = FileResponse(file)
    res['Content-Type'] = 'application/octet-stream'
    res['Content-Disposition'] = 'attachment;filename="1.dcm"'
    return res

def dicom4length(request):
    name=request.POST.get('name')
    url=os.path.join(settings.MEDIA_ROOT, name)
    print(url)
    length=len(os.listdir(url))
    return JsonResponse({'errno': 0, 'length': length})

def dicom4(request):
    id=request.GET.get('id')
    if(len(id)<2):
        url=os.path.join(settings.MEDIA_ROOT, 'dcm11/1-00'+id+'.dcm')
    elif(len(id)<3):
        url=os.path.join(settings.MEDIA_ROOT, 'dcm11/1-0'+id+'.dcm')
    else:
        url=os.path.join(settings.MEDIA_ROOT, 'dcm11/1-'+id+'.dcm')
    file = open(url, 'rb')
    res = FileResponse(file)
    res['Content-Type'] = 'application/octet-stream'
    res['Content-Disposition'] = 'attachment;filename="1.dcm"'
    return res

@csrf_exempt
def volume(request, url=os.path.join(settings.MEDIA_ROOT, 'cottage_obj.obj')):
    file = open(url, 'rb')
    res = FileResponse(file)
    res['Content-Type'] = 'application/octet-stream'
    res['Content-Disposition'] = 'attachment;filename="cottage_obj.obj"'
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
        f1 = open(os.path.join(settings.MEDIA_ROOT, 'ximg', img_name1), 'wb')
        f2 = open(os.path.join(settings.MEDIA_ROOT, 'ximg', img_name2), 'wb')
        for i in img1.chunks():
            f1.write(i)
        f1.close()
        for i in img2.chunks():
            f2.write(i)
        f2.close()

        # X 2 DICOM
        pass
        dicom_name = date_name + '.dcm'
        shutil.copyfile(os.path.join(settings.MEDIA_ROOT, 'image-000001.dcm'),
                        os.path.join(settings.MEDIA_ROOT, 'dicom', dicom_name))
        # X 2 DICOM

        return dicom(request, url=os.path.join(settings.MEDIA_ROOT, 'dicom', dicom_name))
