from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import MovieSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST
from .models import Movie
# Create your views here.


class GetMovies(APIView):
    def get(self,req):
        movie = Movie.objects.all()
        ser_obj = MovieSerializer(movie,many=True)
        return Response(ser_obj.data,status=HTTP_200_OK)
    
    def post(self,req):
        ser_obj = MovieSerializer(data = req.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(ser_obj.errors,status=HTTP_400_BAD_REQUEST)
        
        
class ModifyMovie(APIView):
    def getMovie(self,pk):
        try:
            movie = Movie.objects.get(mid = pk)
        except Movie.DoesNotExist:
            Response(status=HTTP_400_BAD_REQUEST)
        return movie
    
    def get(self,req,pk):
        movie = self.getMovie(pk)
        ser_obj = MovieSerializer(movie)
        return Response(ser_obj.data,status=HTTP_200_OK)
    
    def delete(self,req,pk):
        movie = self.getMovie(pk)
        movie.delete()
        return Response(status=HTTP_200_OK)
    
    def put(self,req,pk):
        movie = self.getMovie(pk)
        ser_obj = MovieSerializer(movie,data=req.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(ser_obj.errors,status=HTTP_400_BAD_REQUEST)
        
        
        
    