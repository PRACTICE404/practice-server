from apps.sessions_.models import Session


class SessionSummaryByDays(Session):
    class Meta:
        proxy = True
        verbose_name_plural = ' Session summary (by days)'


class SessionSummaryByMonths(Session):
    class Meta:
        proxy = True
        verbose_name_plural = 'Session summary (by months)'
