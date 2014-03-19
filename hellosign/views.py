from django.shortcuts import render_to_response
from django.template import RequestContext
from hellosign_python_sdk.hsclient import HSClient

def index(request):
    return render_to_response('hellosign/index.html',
        context_instance=RequestContext(request))

def embedded_signing(request):
    if request.method == 'POST':
        try:
            user_email = request.POST['email']
            user_name = request.POST['name']
        except KeyError:
            return render(request, 'hellosign/embedded_signing.html', {
                'error_message': "Please enter both your name and email.",
            })
        else:
            return HttpResponseRedirect('hellosign/embedded_signing.html')
    else:
        return render_to_response('hellosign/embedded_signing.html',
            context_instance=RequestContext(request))