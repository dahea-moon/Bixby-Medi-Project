from django.shortcuts import HttpResponse
from .models import AED
from bound import Bound
from .serializers import AEDSerializer
from django.db.models import Q
from haversine import haversine
import json

def search_nearest(request):
    data = request.GET.dict()

    latitude = float(data.get('latitude'))
    longtitude = float(data.get('longtitude'))
    LC = Bound(latitude, longtitude)
    
    result = AED.objects.filter(
        Q(langt__range=[LC['langt_min'], LC['langt_max']]) &
        Q(longt__range=[LC['longt_min'], LC['longt_max']])
    )

    data = result.values()
    distance_result = []
    for datum in data:
        point1 = (latitude, longtitude)
        point2 = (datum['langt'], datum['longt'])
        distance = haversine(point1, point2)
        if len(distance_result) >= 3:
            distance_result.sort()
            if distance < distance_result[-1][0]:
                distance_result.pop()
                distance_result += [(distance, datum['id'])]
        else:
            distance_result += [(distance, datum['id'])]

    len_d = len(distance_result)
    if len_d == 0:
        final = None
    elif len_d == 1:
        final = AED.objects.filter(
            Q(id=distance_result[0][1])      
            )
    elif len_d == 2:
        final = AED.objects.filter(
            Q(id=distance_result[0][1]) |
            Q(id=distance_result[1][1])  
            )
    elif len_d == 3:
        final = AED.objects.filter(
            Q(id=distance_result[0][1]) |
            Q(id=distance_result[1][1]) |
            Q(id=distance_result[2][1])       
            )

    serializer = AEDSerializer(final, many=True)
    final = json.dumps(serializer.data, ensure_ascii=False)
    return HttpResponse(final)