from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .models import user
from .serializers import userSerializer
from rest_framework.response import Response

class login(APIView):
  def post(self,request):
  res=response.data
token=request.get("token")
token=request.get("token")
token=request.get("token")
return response("you are successfully login")

class userViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all().order_by('-id')
    serializer_class=AssetSerializer
    
    def create(self,request,*args,**kwargs):
        try:
            serialiser = userSerializer(data = request.data)
            serialiser.is_valid(raise_exception=True)
            serialiser.save()
            return Response(serialiser.data)
        except Exception as e:
            print('e--',e)
            
            
    def destroy(self,request,*args,**kwargs):
        instance = self.get_object()
        instance.delete() 
