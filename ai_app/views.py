from django.shortcuts import render
import google.generativeai as genai
from django.http import HttpResponse
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY )

model=genai.GenerativeModel("gemini-2.5-flash")

def home(request):
    answer = ""
    if request.method=="POST":
        user_message=request.POST.get("message")
        try:
            response=model.generate_content(user_message)
            
            answer =response.text
        except Exception as e:
            answer=str(e)

    return render(request,"index.html",{"answer":answer})
    return HttpResponse("AI App working")