from PyQt6.QtWidgets import QWidget, QCheckBox, QGroupBox, QVBoxLayout, QGridLayout, QRadioButton, QLabel, QPushButton


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

        v_box_layout_cheese = QVBoxLayout()
        v_box_layout_cheese.addWidget(self.__radio_button_cheese_mozzarella)
        v_box_layout_cheese.addWidget(self.__radio_button_cheese_burrata)
        v_box_layout_cheese.addWidget(self.__radio_button_cheese_lactose_free)
        v_box_layout_cheese.addWidget(self.__radio_button_cheese_without)

        group_box_cheese = QGroupBox("Käse", self)
        group_box_cheese.setLayout(v_box_layout_cheese)

        self.__radio_button_delivery_quick = QRadioButton("Schnelllieferung", self)
        self.__radio_button_delivery_normal = QRadioButton("Noramle Lieferung", self)
        self.__radio_button_delivery_self_pickup = QRadioButton("Selbstabholung", self)

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

        grid_layout = QGridLayout()
        grid_layout.addWidget(group_box_ingredients, 0, 0, 2, 1)
        grid_layout.addWidget(group_box_doughs, 0, 1)
        grid_layout.addWidget(group_box_cheese, 1, 1)
        grid_layout.addWidget(group_box_delivery, 0, 2)
        grid_layout.addWidget(group_box_finalize, 1, 2)

        self.setLayout(grid_layout)
