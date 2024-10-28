import calendar

from calendar import monthrange
from datetime import datetime

from django.contrib import admin
from django.db.models import Sum


list_display_of_record = (
    'created',
    'updated'
)


class SummaryDailyAdmin(admin.ModelAdmin):
    change_list_template = 'admin/summary_days.html'
    model = None
    date_hierarchy = ''
    title = ''
    value_name = ''
    unit_name = ''
    value_func = lambda self, x: x  # NOQA

    def has_add_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        if (
            request.GET.get(f'{self.date_hierarchy}__month') and
            request.GET.get(f'{self.date_hierarchy}__year')
        ):
            month = request.GET.get(f'{self.date_hierarchy}__month')
            month_plural = calendar.month_name[int(month)]
            year = request.GET.get(f'{self.date_hierarchy}__year')
        else:
            month = datetime.now().month
            month_plural = datetime.now().strftime("%B")
            year = datetime.now().year

        response.context_data['title'] = self.title
        response.context_data['year'] = year
        response.context_data['month'] = month_plural
        response.context_data['unit'] = self.unit_name
        response.context_data['summary'] = tuple(
            (
                day + 1,
                self.value_func(
                    qs.filter(
                        **{
                            f'{self.date_hierarchy}__year': year,
                            f'{self.date_hierarchy}__month': month,
                            f'{self.date_hierarchy}__day': day+1
                        }
                    )
                    .aggregate(Sum(self.value_name))[f'{self.value_name}__sum'] or 0  # NOQA
                )
            ) for day in range(monthrange(2024, 8)[1])
        )
        return response
