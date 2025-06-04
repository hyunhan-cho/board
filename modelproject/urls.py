from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 관리자 페이지
    path('admin/', admin.site.urls),

    # 앱들 URL
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),

    # 인증 관련 (로그인/로그아웃/유저정보/비번변경 등)
    path('dj/', include('dj_rest_auth.urls')),

    # 회원가입 (오타 수정 ✅)
    path('dj/registration/', include('dj_rest_auth.registration.urls')),
]
