from django.utils import timezone
from kinomaniaApi.models import Screening
now = timezone.now()


def delete_screening():
    screening_out_time = Screening.objects.filter(date__lt=now)
    screening_out_time.delete()
