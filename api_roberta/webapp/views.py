from django.shortcuts import render
from .apps import WebappConfig 

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .apps import WebappConfig

class call_model(APIView):

    
  #def get(self,request):
   #     if request.method == 'GET':
    #        params =  request.GET.get('sentence')  
     #       # sentence = 'I am very happy'
      #      response = WebappConfig.predictor.predict(params)

       #     return JsonResponse(response[0],safe=False)

   def get(self,request):
        if request.method == 'GET':
            params =  request.GET.get('sentence')  
            predict = WebappConfig.predictor.predict(params)
            
            response =dict()
            #response_default=dict()
            response1=dict()
            response2=dict()
            response3=dict()

            response1["name"] = str(predict[0][0])
            response1["confidence"] = float(predict[0][1])

            response2["name"] = str(predict[1][0])
            response2["confidence"] = float(predict[1][1])

            response3["name"] = str(predict[2][0])
            response3["confidence"] = float(predict[2][1])

            l=[response1,response2,response3]

            #response["name"] = str(predict[0][0])
            #response["confidence"] = float(predict[0][1])
            response["intent"] = response1 
            response["intent_ranking"]=l
            return JsonResponse(response)






