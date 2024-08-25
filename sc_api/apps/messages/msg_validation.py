from rest_framework.response import Response

def msg_validation(self, request):
    try:
        if 'text' not in request.data and 'img' not in request.data:
            return False
        return True
    except Exception as ex:
        return Response({'error' : str(ex)}, status=500)