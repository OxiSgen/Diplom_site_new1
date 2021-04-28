from django_charting import Chart, NumberColumn, StringColumn


class DemoChart(Chart):

    def __init__(self, queryset=None):
        qset = []
        super(Chart, self).__init__()
        if queryset is not None:
            for i in range(len(queryset)):
                if 'num_visits' in queryset[i][0]:
                    qset.append({"project": queryset[i][0], "count": queryset[i][1]})
            self.queryset = qset

    template_name = 'news_site/individual.html'

    type = "ColumnChart"
    title = "Число посещений по разделам"

    project = StringColumn()
    count = NumberColumn(accessor="count")
