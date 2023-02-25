from django.http import FileResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def dicom(x):
    file = open('./image-000001.dcm','rb')
    res = FileResponse(file)
    res['Content-Type'] = 'application/octet-stream'
    res['Content-Disposition'] = 'attachment;filename="1.dcm"'
    return res
# Create your views here.
