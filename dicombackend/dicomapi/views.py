from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import View
import os
from django.conf import settings

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'media')

@csrf_exempt
def dicom(x):
    file = open('./image-000001.dcm','rb')
    res = FileResponse(file)
    res['Content-Type'] = 'application/octet-stream'
    res['Content-Disposition'] = 'attachment;filename="1.dcm"'
    return res
# Create your views here.

class File(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'url': "http://127.0.0.1/" + MEDIA_URL + "image-000001.dcm"})
