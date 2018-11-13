import pygal

from .models import Survey

class DemographicPieChart():

    def __init__(self, **kwargs):
        self.chart = pygal.Pie(**kwargs)
        self.chart.title = 'Color vs Non-Color People'

    def get_data(self):
        '''
        Query the db for chart data, pack them into a dict and return it.
        '''
        data = {}
        data["Person of Color"] = 0
        data["Caucasian"] = 0
        for person in Survey.objects.all():
            if person.color:
                data["Person of Color"] = data["Person of Color"]+1
            else :
                data["Caucasian"] = data["Caucasian"]+1
        # data["Color"] = sum(Survey.objects.all().color)
        # data["NotColor"] = 500
        
        # for person in Survey.objects.all():
        #     if person.color:
        #         data["Color"] = person.color
        #     else:
        #         data["NotColor"] = person.color
        return data

    def generate(self):
        # Get chart data
        chart_data = self.get_data()

        # Add data to chart
        for key, value in chart_data.items():
            self.chart.add(key, value)

        # Return the rendered SVG
        return self.chart.render(is_unicode=True)