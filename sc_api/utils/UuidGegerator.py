from random import randint
from rest_framework.response import Response
from rest_framework import status


def Uuid(objs):
    try:
    
        def UniqUuid():
            uuid = randint(20000000, 80000000)
            for obj in objs:
                if uuid == obj.uuid:
                    return 0
            return uuid
        
        while True:
            result = UniqUuid()
            if result:
                return result
            
    except Exception as ex:
        return Response({'error' : str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)