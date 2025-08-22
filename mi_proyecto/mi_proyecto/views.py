from django.http import HttpResponse

def inicio(request):
 nombre =" Dante"
 return HttpResponse(f"Hola mundo desde Django, {nombre}")