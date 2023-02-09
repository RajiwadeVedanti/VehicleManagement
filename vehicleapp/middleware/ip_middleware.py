from django.core.exceptions import PermissionDenied   
from django.utils.deprecation import MiddlewareMixin 

class IPMiddleware(MiddlewareMixin):
    # Check if client IP address is allowed  
    def process_request(self, request):
        print("mi wr ip: ",request.META.get('REMOTE_ADDR'))
        allowed_ips = ['192.168.1.1','127.0.0.1'] 
        ip = request.META.get('REMOTE_ADDR')
        if ip not in allowed_ips:
            raise PermissionDenied

        return None