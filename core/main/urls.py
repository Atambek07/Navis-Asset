from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PartnerViewSet, FAQViewSet, NewsViewSet, FeedbackViewSet

router = DefaultRouter()
router.register(r'partners', PartnerViewSet)
router.register(r'faqs', FAQViewSet)
router.register(r'news', NewsViewSet)
router.register(r'feedbacks', FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
