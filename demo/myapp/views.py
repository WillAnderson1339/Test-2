from django.shortcuts import render, HttpResponse

# Create your views here.
"""
def home(request):
	print("contacts handler")
	#return HttpResponse("Hello World!")
	print("Foo")
	print(request.path)
	print("bar!")
	return render(request, "home.html")
"""

def page_router(request):
	#print("page_router handler")
	if "/" == request.path.lower():
		return render(request, "home.html")
	if "home" in request.path.lower():
		return render(request, "home.html")
	elif "about" in request.path.lower():
		return render(request, "about.html")
	elif "contacts" in request.path.lower():
		return render(request, "contacts.html")
	else:
		return HttpResponse("unknown page request " + request.path)

