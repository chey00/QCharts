from PyQt6.QtCharts import QChartView, QChart, QLineSeries, QValueAxis
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
        axis_y.setRange(0, 16)

        line_series = QLineSeries()
        line_series.setName('Parabel')
        line_series.append(0, 0)
        line_series.append(1, 1)
        line_series.append(2, 4)
        line_series.append(3, 9)
        line_series.append(4, 16)

        chart = QChart()
        chart.addSeries(line_series)
        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        line_series.attachAxis(axis_x)
        line_series.attachAxis(axis_y)

        self.setChart(chart)

