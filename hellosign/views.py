from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from hellosign_python_sdk.hsclient import HSClient
from hellosign_python_sdk.utils.exception import NoAuthMethod
from settings import API_KEY, CLIENT_ID
import os
import pdb

def index(request):
    return render_to_response('hellosign/index.html',
        context_instance=RequestContext(request))

def embedded_signing(request):
    if request.method == 'POST':
        try:
            user_email = request.POST['email']
            user_name = request.POST['name']
            hsclient = HSClient(api_key=API_KEY)

            files = [os.path.dirname(os.path.realpath(__file__)) + "/docs/nda.pdf"]
            signers = [{"name": user_name, "email_address": user_email}]
            cc_email_addresses = []
            sr = hsclient.send_signature_request_embedded(
                "1", CLIENT_ID, files, [], "NDA with Acme Co.",
                "The NDA we talked about", "Please sign this NDA and then we" +
                " can discuss more. Let me know if you have any questions.",
                "", signers, cc_email_addresses)
            embedded = hsclient.get_embeded_object(sr.signatures[0]["signature_id"])
        except KeyError:
            return render(request, 'hellosign/embedded_signing.html', {
                'error_message': "Please enter both your name and email.",
            })
        except NoAuthMethod:
            return render(request, 'hellosign/embedded_signing.html', {
                'error_message': "Please update your settings to include a " +
                "value for API_KEY.",
            })
        else:
            # pdb.set_trace()
            # return HttpResponseRedirect('embedded_signing?signed=true&sign_url=' + str(embedded.sign_url))
            return render(request, 'hellosign/embedded_signing.html', {
                    'client_id': CLIENT_ID,
                    'sign_url': str(embedded.sign_url)
                    })
    else:
        return render_to_response('hellosign/embedded_signing.html',
            context_instance=RequestContext(request))