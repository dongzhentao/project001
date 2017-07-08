
class UrlMiddleWare(object):
    def process_request(self, request):
        if request.path not in [
            '/user/login/',
            '/user/zhuce/',
            '/user/register/',
            '/user/login_pwd_yz/',
            '/user/login_yz/',
            '/user/ushou_zhece/',
            '/user/login_yz/',
            '/user/login_yz/',

        ]:
            request.session['url.path'] = request.get_full_path()