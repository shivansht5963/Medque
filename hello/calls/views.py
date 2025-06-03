from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from twilio.rest import Client
from calls.models import CallLog  # Assuming you have a model to store call logs
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@csrf_exempt
def exotel_webhook(request):
    if request.method == 'GET':
        logging.debug("Exotel webhook triggered")

        # Get parameters from the request
        CallFrom = request.GET.get('CallFrom')
        DialCallDuration = request.GET.get('DialCallDuration')
        # logging.debug(f"Caller number: {caller_number}, Call duration: {call_duration}")

        # if caller_number and call_duration is not None:
            # Save call record to database
        newlog = CallLog(CallFrom=CallFrom,
                DialCallDuration=DialCallDuration,
                date=datetime.now()
            )
        newlog.save()
        logging.debug("Call record saved to database")

            # If the call duration is 0 (call rejected), send an SMS via Twilio
        if DialCallDuration == '0':  
                # Send an SMS via Fast2SMS
            send_sms_via_fast2sms(CallFrom, 'Your call was rejected. This is an automated message.')
            
        return JsonResponse({'status': 'success', 'caller_number': CallFrom, 'call_duration': DialCallDuration})
    else:
            logging.error("Missing required parameters in the request")
            return JsonResponse({'status': 'failure', 'error': 'Missing parameters'}, status=400)

    logging.error("Invalid request method")
    return HttpResponse("Exotel webhook endpoint. Only GET requests are accepted.", status=405)


import requests

def send_sms_via_fast2sms(CallFrom, message):
    # Fast2SMS API credentials
    FAST2SMS_API_KEY = 'b3Kw4tvM5CLRGeUWrniX0oxJOShBYVNmTgqE2jpdAzHyQ68Df7WZ7ohidm3DAUNk0wvVsxzbXSG2p8RJ'  # Replace with your Fast2SMS API Key
    
    # API URL and payload
    url = "https://www.fast2sms.com/dev/bulkV2"
    payload = {
        'authorization': FAST2SMS_API_KEY,
        'sender_id': 'TXTIND',
        'message': message,
        'route': 'v3',
        'numbers': CallFrom,
    }
    
    # Headers
    headers = {
        'cache-control': 'no-cache'
    }
    
    # Make the API request to send the SMS
    try:
        response = requests.post(url, data=payload, headers=headers)
        response_data = response.json()
        print(f"SMS Response: {response_data}")
    except Exception as e:
        print(f"Failed to send SMS: {e}")