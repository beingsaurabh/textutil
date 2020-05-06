from django.shortcuts import render , HttpResponse

def index(request):
    return render(request,"index.html")

def analyser(request):
    string1=request.GET.get('string','default')
    remove_punc=request.GET.get('removepunc','off')
    print(string1)
    print(remove_punc)
    if remove_punc=="on":
        punctuationword='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        ans=''
        for char in string1:
            if char not in punctuationword:
                ans=ans+char
        final_text=ans
        params={"final_text":ans}
        return render(request,"analyser.html",params) 
    else:
        return HttpResponse("Please tick the check-box.Thanks")
    
             

