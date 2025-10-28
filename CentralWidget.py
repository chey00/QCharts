from PyQt6.QtCharts import QChartView, QChart, QLineSeries, QValueAxis, QScatterSeries
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor


class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        axis_x = QValueAxis()
        axis_x.setTitleText("x-Achse")
        axis_x.setRange(0, 4)

        axis_y = QValueAxis()
        axis_y.setTitleText("y-Achse")
        axis_y.setRange(0, 8)

        line_series = QLineSeries()
        line_series.setName('Gerade 1')
        line_series.append(0, 0)
        line_series.append(1, 2)
        line_series.append(2, 4)
        line_series.append(3, 6)
        line_series.append(4, 8)

        line_series_2 = QLineSeries()
        line_series_2.setName('Gerade 2')
        line_series_2.append(0, 3.0)
        line_series_2.append(1, 3.5)
        line_series_2.append(2, 4.0)
        line_series_2.append(3, 4.5)
        line_series_2.append(4, 5.0)

        scatter_series = QScatterSeries()
        scatter_series.setName("Schnittpunkt")
        scatter_series.append(2, 4)

        chart = QChart()
        chart.addSeries(line_series)
        chart.addSeries(line_series_2)
        chart.addSeries(scatter_series)
        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        line_series.attachAxis(axis_x)
        line_series.attachAxis(axis_y)
        line_series_2.attachAxis(axis_x)
        line_series_2.attachAxis(axis_y)
        scatter_series.attachAxis(axis_x)
        scatter_series.attachAxis(axis_y)

        self.setChart(chart)
