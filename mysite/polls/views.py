from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.http import Http404
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        # Process user_message and generate bot response
        bot_response = generate_bot_response(user_message)
        return JsonResponse({'message': bot_response})
    else:
        return render(request, 'chatbot.html')  # Return the HTML template

def generate_bot_response(user_message):
    # Replace this with your actual bot logic
    responses = [
        "Hello! How can I assist you today?",
        "I'm sorry, I didn't understand that.",
        "Please rephrase your question.",
        "Let me find that information for you.",
        "How can I help you further?",
    ]
    return random.choice(responses)

def index(request):
    return HttpResponse("Hello! If you want to use Buddy for Study type /polls/math (for Math AI); /polls/ip (for IP calculating AI); polls/genera l(for General AI)")

def math_AI(request):
    myvariable = "You are using Math AI"
    context={'myvariable' : myvariable}
    return render(request, "base.html", context)
def IP_AI(request):
    ipvar = 'Something'
    context1={'ipvar': ipvar}
    return render(request, "ip.html", context1)
def general_AI(request):
    genvar = 'Hi'
    context2 = {'genvar': genvar}
    return render(request, "gen.html", context2)
