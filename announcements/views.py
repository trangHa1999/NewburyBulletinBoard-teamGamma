from django.views.generic import TemplateView, ListView, DetailView
from .models import Announcement
from datetime import datetime
from pytz import timezone

class AnnouncementsHomeView(ListView):
    model = Announcement
    template_name = "announcements/index.html"

class AnnouncementsList(ListView):
    model = Announcement
    template_name = "announcements/list-view.html"

    def get_queryset(self):
        todaysDate = datetime.now()
        return Announcement.objects.order_by("-startDate").filter(startDate__lte=todaysDate).filter(expirationDate__gte=todaysDate)


class AnnouncementDetail(DetailView):
    model = Announcement
    template_name = "announcements/detail-view.html"


