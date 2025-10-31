from PyQt6.QtCharts import QChartView, QChart, QLineSeries, QValueAxis, QScatterSeries, QDateTimeAxis
from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtGui import QColor


class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        axis_date_time = QDateTimeAxis()
        axis_date_time.setTitleText("Datum und Uhrzeit")
        axis_date_time.setFormat("dd.MM.yyyy hh:mm")
        date_time_start = QDateTime(2025, 10, 20, 8, 0, 0)
        date_time_end = QDateTime(2025, 10, 27, 16, 0, 0)
        axis_date_time.setRange(date_time_start, date_time_end)

        axis_euro = QValueAxis()
        axis_euro.setTitleText("Preis in €")
        axis_euro.setRange(3900, 4400)

        line_series_eur = QLineSeries()
        line_series_eur.setName('Goldpreis in Euro')
        line_series_eur.append(QDateTime(2025, 10, 27, 16, 0, 0).toMSecsSinceEpoch(), 3982.24)
        line_series_eur.append(QDateTime(2025, 10, 27, 8, 0, 0).toMSecsSinceEpoch(), 4080.86)
        line_series_eur.append(QDateTime(2025, 10, 24, 16, 0, 0).toMSecsSinceEpoch(), 4103.79)
        line_series_eur.append(QDateTime(2025, 10, 24, 8, 0, 0).toMSecsSinceEpoch(), 4104.21)
        line_series_eur.append(QDateTime(2025, 10, 23, 16, 0, 0).toMSecsSinceEpoch(), 4118.27)
        line_series_eur.append(QDateTime(2025, 10, 23, 8, 0, 0).toMSecsSinceEpoch(), 4120.21)
        line_series_eur.append(QDateTime(2025, 10, 22, 16, 0, 0).toMSecsSinceEpoch(), 4102.14)
        line_series_eur.append(QDateTime(2025, 10, 22, 8, 0, 0).toMSecsSinceEpoch(), 4132.34)
        line_series_eur.append(QDateTime(2025, 10, 21, 16, 0, 0).toMSecsSinceEpoch(), 4109.24)
        line_series_eur.append(QDateTime(2025, 10, 21, 8, 0, 0).toMSecsSinceEpoch(), 4325.64)
        line_series_eur.append(QDateTime(2025, 10, 20, 16, 0, 0).toMSecsSinceEpoch(), 4377.78)
        line_series_eur.append(QDateTime(2025, 10, 20, 8, 0, 0).toMSecsSinceEpoch(), 4239.75)

        axis_usd = QValueAxis()
        axis_usd.setTitleText("Preis in $")
        axis_usd.setRange(3400, 3800)

        line_series_usd = QLineSeries()
        line_series_usd.setName('Goldpreis in Dollar')
        line_series_usd.append(QDateTime(2025, 10, 27, 16, 00, 00).toMSecsSinceEpoch(), 3421.17)
        line_series_usd.append(QDateTime(2025, 10, 27, 8, 00, 00).toMSecsSinceEpoch(), 3505.90)
        line_series_usd.append(QDateTime(2025, 10, 24, 16, 00, 00).toMSecsSinceEpoch(), 3534.09)
        line_series_usd.append(QDateTime(2025, 10, 24, 8, 00, 00).toMSecsSinceEpoch(), 3534.46)
        line_series_usd.append(QDateTime(2025, 10, 23, 16, 00, 00).toMSecsSinceEpoch(), 3552.37)
        line_series_usd.append(QDateTime(2025, 10, 23, 8, 00, 00).toMSecsSinceEpoch(), 3554.05)
        line_series_usd.append(QDateTime(2025, 10, 22, 16, 00, 00).toMSecsSinceEpoch(), 3540.30)
        line_series_usd.append(QDateTime(2025, 10, 22, 8, 00, 00).toMSecsSinceEpoch(), 3566.36)
        line_series_usd.append(QDateTime(2025, 10, 21, 16, 00, 00).toMSecsSinceEpoch(), 3540.31)
        line_series_usd.append(QDateTime(2025, 10, 21, 8, 00, 00).toMSecsSinceEpoch(), 3726.75)
        line_series_usd.append(QDateTime(2025, 10, 20, 16, 00, 00).toMSecsSinceEpoch(), 3756.14)
        line_series_usd.append(QDateTime(2025, 10, 20, 8, 00, 00).toMSecsSinceEpoch(), 3637.71)

        chart = QChart()
        chart.addAxis(axis_date_time, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(axis_euro, Qt.AlignmentFlag.AlignLeft)
        chart.addAxis(axis_usd, Qt.AlignmentFlag.AlignRight)
        chart.addSeries(line_series_eur)
        chart.addSeries(line_series_usd)

        line_series_eur.attachAxis(axis_date_time)
        line_series_eur.attachAxis(axis_euro)

        line_series_usd.attachAxis(axis_date_time)
        line_series_usd.attachAxis(axis_usd)

        self.setChart(chart)
