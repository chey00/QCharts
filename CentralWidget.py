from PyQt6.QtCharts import QChartView, QChart, QLineSeries, QValueAxis, QScatterSeries, QDateTimeAxis
from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtGui import QColor


class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        axis_date_time = QDateTimeAxis()
        axis_date_time.setTitleText("Datum und Uhrzeit")
        axis_date_time.setFormat("dd.MM.yyyy hh:mm:ss")
        date_time_start = QDateTime(2025, 9, 28, 13, 52, 9, 100)
        date_time_end = QDateTime(2025, 10, 28, 13, 52, 9, 100)
        axis_date_time.setRange(date_time_start, date_time_end)

        axis_euro = QValueAxis()
        axis_euro.setTitleText("Preis in €")
        axis_euro.setRange(10, 50)

        axis_usd = QValueAxis()
        axis_usd.setTitleText("Preis in $")
        axis_usd.setRange(10, 50)

        line_series = QLineSeries()
        line_series.setName('Goldpreis in Euro')
        line_series.append(date_time_start.toMSecsSinceEpoch(), 30)
        line_series.append(date_time_start.addDays(7).toMSecsSinceEpoch(), 20)
        line_series.append(date_time_start.addDays(14).toMSecsSinceEpoch(), 45)
        line_series.append(date_time_end.addDays(-7).toMSecsSinceEpoch(), 26)
        line_series.append(date_time_end.toMSecsSinceEpoch(), 48)

        chart = QChart()
        chart.addSeries(line_series)
        chart.addAxis(axis_date_time, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(axis_euro, Qt.AlignmentFlag.AlignLeft)
        chart.addAxis(axis_usd, Qt.AlignmentFlag.AlignRight)

        line_series.attachAxis(axis_date_time)
        line_series.attachAxis(axis_euro)

        self.setChart(chart)
