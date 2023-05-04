from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializers import PersonSerializer

@api_view(['GET', 'POST'])
def index(request):
    
    courses = {
        'course_name' : 'Python',
        'learn' : ['Flask', 'Django', 'Fast Api'],
        'course_provider' : 'Someone'
    }

    return Response(courses)

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message' : 'Your data saved successfully'
            })
     
        return Response(serializer.errors)
    
    if request.method == 'PUT':
        data = request.data
        person = Person.objects.get(id=data['id'])
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data
            )
        
        return Response(serializer.errors)
        
    if request.method == 'PATCH':
        data = request.data
        person = Person.objects.get(id = data['id'])
        print(person)
        serializer = PersonSerializer(person, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        try:
            person = Person.objects.get(id = request.data['id'])
            if person:
                person.delete()
                return Response({
                    'message' : 'Deletion successful'
                })
        except:
            return Response(
                {
                    'message' : 'Person doesn\'t exist'
                }
            )
