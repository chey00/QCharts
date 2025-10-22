from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QCheckBox, QGroupBox, QVBoxLayout, QRadioButton, QLabel, QPushButton, \
    QHBoxLayout


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.__check_box_ingredient_mushroom = QCheckBox("Pilze", self)
        self.__check_box_ingredient_corn = QCheckBox("Mais", self)
        self.__check_box_ingredient_pepper = QCheckBox("Paprika", self)
        self.__check_box_ingredient_onion = QCheckBox("Zwiebel", self)
        self.__check_box_ingredient_egg = QCheckBox("Ei", self)
        self.__check_box_ingredient_pineapple = QCheckBox("Ananas", self)
        self.__check_box_ingredient_ham = QCheckBox("Roher Schinken", self)
        self.__check_box_ingredient_parma = QCheckBox("Paramschinken", self)
        self.__check_box_ingredient_salami = QCheckBox("Salami", self)
        self.__check_box_ingredient_peperoni = QCheckBox("Scharfe Salami", self)
        self.__check_box_ingredient_suzuek = QCheckBox("Suzük", self)

        self.__dict_ingredients = dict()
        self.__dict_ingredients[self.__check_box_ingredient_mushroom] = 0.60
        self.__dict_ingredients[self.__check_box_ingredient_corn] = 0.30
        self.__dict_ingredients[self.__check_box_ingredient_pepper] = 0.75
        self.__dict_ingredients[self.__check_box_ingredient_onion] = 0.20
        self.__dict_ingredients[self.__check_box_ingredient_egg] = 1.00
        self.__dict_ingredients[self.__check_box_ingredient_pineapple] = 0.80
        self.__dict_ingredients[self.__check_box_ingredient_ham] = 0.90
        self.__dict_ingredients[self.__check_box_ingredient_parma] = 1.50
        self.__dict_ingredients[self.__check_box_ingredient_salami] = 0.60
        self.__dict_ingredients[self.__check_box_ingredient_peperoni] = 0.60
        self.__dict_ingredients[self.__check_box_ingredient_suzuek] = 0.40

        self.__price_ingredients = 0.00

        for key in self.__dict_ingredients.keys():
            key.clicked.connect(self.__slot_ingredients)

            text = key.text()
            text += " ({:0.2f} €)".format(self.__dict_ingredients[key])

            key.setText(text)

        v_box_layout_ingredients = QVBoxLayout()
        v_box_layout_ingredients.addWidget(self.__check_box_ingredient_mushroom)
        v_box_layout_ingredients.addWidget(self.__check_box_ingredient_corn)
        v_box_layout_ingredients.addWidget(self.__check_box_ingredient_pepper)
        v_box_layout_ingredients.addWidget(self.__check_box_ingredient_onion)
        v_box_layout_ingredients.addWidget(self.__check_box_ingredient_egg)
        v_box_layout_ingredients.addWidget(self.__check_box_ingredient_pineapple)
        v_box_layout_ingredients.addWidget(self.__check_box_ingredient_ham)
        v_box_layout_ingredients.addWidget(self.__check_box_ingredient_parma)
        v_box_layout_ingredients.addWidget(self.__check_box_ingredient_salami)
        v_box_layout_ingredients.addWidget(self.__check_box_ingredient_peperoni)
        v_box_layout_ingredients.addWidget(self.__check_box_ingredient_suzuek)

        group_box_ingredients = QGroupBox("Beläge", self)
        group_box_ingredients.setLayout(v_box_layout_ingredients)

        self.__radio_button_dough_normal = QRadioButton("Normaler Teig", self)
        self.__radio_button_dough_sour_dough = QRadioButton("Sauerteig", self)
        self.__radio_button_dough_gluten_free = QRadioButton("Glutenfreier Teig", self)
        self.__radio_button_dough_pinza = QRadioButton("Pinza", self)

        self.__dict_doughs = dict()
        self.__dict_doughs[self.__radio_button_dough_normal] = 5.50
        self.__dict_doughs[self.__radio_button_dough_sour_dough] = 7.30
        self.__dict_doughs[self.__radio_button_dough_gluten_free] = 8.75
        self.__dict_doughs[self.__radio_button_dough_pinza] = 10.20

        self.__price_doughs = 0.00

        for key in self.__dict_doughs.keys():
            key.clicked.connect(self.__slot_doughs)

            text = key.text()
            text += " ({:0.2f} €)".format(self.__dict_doughs[key])

            key.setText(text)

        v_box_layout_doughs = QVBoxLayout()
        v_box_layout_doughs.addWidget(self.__radio_button_dough_normal)
        v_box_layout_doughs.addWidget(self.__radio_button_dough_sour_dough)
        v_box_layout_doughs.addWidget(self.__radio_button_dough_gluten_free)
        v_box_layout_doughs.addWidget(self.__radio_button_dough_pinza)

        group_box_doughs = QGroupBox("Teige", self)
        group_box_doughs.setLayout(v_box_layout_doughs)

        self.__radio_button_cheese_mozzarella = QRadioButton("Mozzarella", self)
        self.__radio_button_cheese_burrata = QRadioButton("Burrata", self)
        self.__radio_button_cheese_lactose_free = QRadioButton("Laktosefreier Käse", self)
        self.__radio_button_cheese_without = QRadioButton("Ohne Käse", self)

        self.__dict_cheeses = dict()
        self.__dict_cheeses[self.__radio_button_cheese_mozzarella] = 0.50
        self.__dict_cheeses[self.__radio_button_cheese_burrata] = 1.30
        self.__dict_cheeses[self.__radio_button_cheese_lactose_free] = 1.00
        self.__dict_cheeses[self.__radio_button_cheese_without] = 0.0

        self.__price_cheeses = 0.00

        for key in self.__dict_cheeses.keys():
            key.clicked.connect(self.__slot_cheeses)

            text = key.text()
            text += " ({:0.2f} €)".format(self.__dict_cheeses[key])

            key.setText(text)

        v_box_layout_cheese = QVBoxLayout()
        v_box_layout_cheese.addWidget(self.__radio_button_cheese_mozzarella)
        v_box_layout_cheese.addWidget(self.__radio_button_cheese_burrata)
        v_box_layout_cheese.addWidget(self.__radio_button_cheese_lactose_free)
        v_box_layout_cheese.addWidget(self.__radio_button_cheese_without)

        group_box_cheese = QGroupBox("Käse", self)
        group_box_cheese.setLayout(v_box_layout_cheese)

        self.__radio_button_delivery_quick = QRadioButton("Schnelllieferung", self)
        self.__radio_button_delivery_normal = QRadioButton("Normale Lieferung", self)
        self.__radio_button_delivery_self_pickup = QRadioButton("Selbstabholung", self)

        self.__dict_delivery = dict()
        self.__dict_delivery[self.__radio_button_delivery_quick] = 3.50
        self.__dict_delivery[self.__radio_button_delivery_normal] = 1.50
        self.__dict_delivery[self.__radio_button_delivery_self_pickup] = 0.00

        self.__price_delivery = 0.00

        for key in self.__dict_delivery.keys():
            key.clicked.connect(self.__slot_delivery)

            text = key.text()
            text += " ({:0.2f} €)".format(self.__dict_delivery[key])

            key.setText(text)

        v_box_layout_delivery = QVBoxLayout()
        v_box_layout_delivery.addWidget(self.__radio_button_delivery_quick)
        v_box_layout_delivery.addWidget(self.__radio_button_delivery_normal)
        v_box_layout_delivery.addWidget(self.__radio_button_delivery_self_pickup)

        group_box_delivery = QGroupBox("Lieferung", self)
        group_box_delivery.setLayout(v_box_layout_delivery)

        self.__label_price_dough = QLabel("Teig: \t\t0,00 €", self)
        self.__label_price_ingredients = QLabel("Zutaten: \t0,00 €", self)
        self.__label_price_cheese = QLabel("Käse: \t\t0,00 €", self)
        self.__label_price_delivery = QLabel("Lieferkosten: \t0,00 €", self)
        self.__label_price_sum = QLabel("Gesamtpreis: \t0,00 €", self)
        self.__push_button = QPushButton("Jetzt bestellen", self)

        v_box_layout_finalize = QVBoxLayout()
        v_box_layout_finalize.addWidget(self.__label_price_dough)
        v_box_layout_finalize.addWidget(self.__label_price_ingredients)
        v_box_layout_finalize.addWidget(self.__label_price_cheese)
        v_box_layout_finalize.addWidget(self.__label_price_delivery)
        v_box_layout_finalize.addWidget(self.__label_price_sum)
        v_box_layout_finalize.addWidget(self.__push_button)

        group_box_finalize = QGroupBox("Übersicht", self)
        group_box_finalize.setLayout(v_box_layout_finalize)

        v_box_layout_doughs_and_cheese = QVBoxLayout()
        v_box_layout_doughs_and_cheese.addWidget(group_box_doughs)
        v_box_layout_doughs_and_cheese.addWidget(group_box_cheese)

        v_box_layout_delivery_and_finalize = QVBoxLayout()
        v_box_layout_delivery_and_finalize.addWidget(group_box_delivery)
        v_box_layout_delivery_and_finalize.addWidget(group_box_finalize)

        h_box_layout = QHBoxLayout()
        h_box_layout.addWidget(group_box_ingredients)
        h_box_layout.addLayout(v_box_layout_doughs_and_cheese)
        h_box_layout.addLayout(v_box_layout_delivery_and_finalize)

        self.setLayout(h_box_layout)

    @pyqtSlot()
    def __slot_ingredients(self):
        if self.sender().isChecked():
            self.__price_ingredients += self.__dict_ingredients[self.sender()]
        else:
            self.__price_ingredients -= self.__dict_ingredients[self.sender()]

        self.__label_price_ingredients.setText("Zutaten: \t"+ f"{self.__price_ingredients:0.2f}" +" €")
        self.calculate_sum()

    @pyqtSlot()
    def __slot_doughs(self):
        self.__price_doughs = self.__dict_doughs[self.sender()]

        self.__label_price_dough.setText("Teig: \t\t"+ f"{self.__price_doughs:0.2f}" +" €")
        self.calculate_sum()

    @pyqtSlot()
    def __slot_cheeses(self):
        self.__price_cheeses = self.__dict_cheeses[self.sender()]

        self.__label_price_cheese.setText("Käse: \t\t"+ f"{self.__price_cheeses:0.2f}" +" €")
        self.calculate_sum()

    @pyqtSlot()
    def __slot_delivery(self):
        self.__price_delivery = self.__dict_delivery[self.sender()]

        self.__label_price_delivery.setText("Lieferung: \t"+ f"{self.__price_delivery:0.2f}" +" €")
        self.calculate_sum()

    def calculate_sum(self):
        sum = self.__price_delivery
        sum += self.__price_cheeses
        sum += self.__price_doughs
        sum += self.__price_ingredients

        self.__label_price_sum.setText("Gesamtpreis: \t"+ f"{sum:0.2f}" +" €")
