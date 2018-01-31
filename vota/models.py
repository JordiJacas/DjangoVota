from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Consulta(models.Model):
    titul = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    finici = models.DateTimeField()
    ffinal = models.DateTimeField()

    def __str__(self):
    	return self.titul

class Opcio(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    comentari = models.TextField(default=True,null=True)
    vots = models.IntegerField(default=0)
    usuari = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __str__(self):
    	return self.text

class Invitacio(models.Model):
	consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
	usuari = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	enviada = models.BooleanField(default=False)
	acceptada = models.BooleanField(default=False)
	def  __str__(self):
	  	return self.consulta.__str__() \
	  	 + " | " + self.usuari.__str__()

class Vot(models.Model):
	usuari = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	consulta = models.ForeignKey(Consulta,on_delete=models.CASCADE)
	Opcio = models.ForeignKey(Opcio,on_delete=models.CASCADE)
	def __str__(self):
		return self.usuari.__str__() \
				+ " | " + self.Opcio.consulta.__str__() \
				+ " | " + self.Opcio.__str__()
