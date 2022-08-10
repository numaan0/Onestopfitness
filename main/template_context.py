from distutils.log import log
from . import models

def get_logo(request):
	logo=models.AppSetting.objects.first()
	data={
		'logo':"OneStopFitness"
	}
	return data