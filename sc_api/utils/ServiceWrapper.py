from rest_framework.response import Response
from rest_framework import status

def ServiceWrapper(action):
    try:
        ActionResult, st = action()
    except Exception as ex:
        return Response({'error' : str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'result' : ActionResult}, status=st)