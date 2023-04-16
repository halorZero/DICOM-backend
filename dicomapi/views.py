from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import datetime
import shutil
import SimpleITK as sitk
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
    # if(len(id)<2):
    #     url=os.path.join(settings.MEDIA_ROOT, 'dcm11/1-00'+id+'.dcm')
    # elif(len(id)<3):
    #     url=os.path.join(settings.MEDIA_ROOT, 'dcm11/1-0'+id+'.dcm')
    # else:
    #     url=os.path.join(settings.MEDIA_ROOT, 'dcm11/1-'+id+'.dcm')
    url=os.path.join(settings.MEDIA_ROOT, 'test1/CT586444-房艳梅'+id+'.dcm')
    
    file = open(url, 'rb')
    res = FileResponse(file)
    res['Content-Type'] = 'application/octet-stream'
    res['Content-Disposition'] = 'attachment;filename="1.dcm"'
    return res

@csrf_exempt
def volume(request, url=os.path.join(settings.MEDIA_ROOT, '1.obj')):
    id=request.GET.get('id')
    file = open(url, 'rb')
    res = FileResponse(file)
    res['Content-Type'] = 'application/octet-stream'
    res['Content-Disposition'] = 'attachment;filename="1.obj"'
    return res

def x2ct(request, url=os.path.join(settings.MEDIA_ROOT)):
    patient_id = os.listdir(os.path.join(url, 'dcm11'))
    unexist = 0
    nb=0
    for i in range(len(patient_id)):
        tidy_ct_path = url + '\\dcm11\\' + patient_id[nb]
        if os.path.exists(tidy_ct_path):
            print(tidy_ct_path)
            dcms_name = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(tidy_ct_path)
            dcms_read = sitk.ImageSeriesReader()#类似java里面的实例
            dcms_read.SetFileNames(dcms_name)#将list里面的元素设置
            dcms_series = dcms_read.Execute()#应该是这一系列图片标准化，各种信息的完善吧。就像dcm文件里面一些header还有相关内容的介绍
            print(url+'\\%d.nrrd'%(nb+1))
            sitk.WriteImage(dcms_series,url+'\\%d.nrrd'%(nb+1))
            nb = nb+1
        else:
            print('目录%s不存在'%tidy_ct_path)
            unexist = unexist+1
            nb = nb+1
    print('每位patient对应的ct图片已合成三维图片nrrd格式，共计%d个nrrd文件'%(range(len(patient_id))-unexist))

def dicom3d(request, url=os.path.join(settings.MEDIA_ROOT, '111.vtk')):
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
