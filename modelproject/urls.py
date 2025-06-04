from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    # 루트 페이지: 배포 확인용
    path('', lambda request: HttpResponse("✅ 서버 정상 작동 중!")),

    # 관리자 페이지
    path('admin/', admin.site.urls),

    # 앱들 URL
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),

    # 인증 관련
    path('dj/', include('dj_rest_auth.urls')),
    path('dj/registration/', include('dj_rest_auth.registration.urls')),
]
