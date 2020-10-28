from django.shortcuts import render
from django.http import JsonResponse
import whois

def index(request):
	template_name="brand/index.html"
	context={}
	return render(request,template_name,context)

def savedomains(request):
	arr = request.GET.getlist('arr[]')
	myset = set(arr)
	mynewlist = list(myset)
	l=[x+".com" for x in mynewlist]
	f=[]
	n=[]
	for i in l:
	  try:
	    w = whois.whois(i)
	    f.append(i)
	  except:
	    n.append(i)

	print("Available Domain Names")
	print(f)
	print("Not Found")
	print(n)
	return JsonResponse(n, safe=False)

