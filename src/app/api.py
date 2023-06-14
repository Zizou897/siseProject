from django.db import connection
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response



class Liste_Dernier_Prix(APIView):

    def get(self ,request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM liste_dernier_prix_marche")
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()

        data = []
        for row in rows:
            data.append(dict(zip(columns, row)))

        return Response(data=data, status=status.HTTP_200_OK)