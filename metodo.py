from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
import localizadores

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver,20).until(expected_conditions.visibility_of_element_located(localizadores.LUrbanRoutesPage.from_field))
    def set_from(self,):
        self.driver.find_element(*localizadores.LUrbanRoutesPage.from_field).send_keys(data.address_from)
    def set_to(self):
        self.driver.find_element(*localizadores.LUrbanRoutesPage.to_field).send_keys(data.address_to)
    def get_from(self):
        return self.driver.find_element(localizadores.LUrbanRoutesPage.from_field).get_property('value')
    def get_to(self):
        return self.driver.find_element(*localizadores.LUrbanRoutesPage.to_field).get_property('value')
    #se ingresaron esperas en algunos elementos
    #clic en pedir un taxi
    def click_order_a_taxi_button(self):
     WebDriverWait(self.driver.find_element,40).until(expected_conditions.element_to_be_clickable(localizadores.LUrbanRoutesPage.order_a_taxi_button))
     self.driver.find_element(*localizadores.LUrbanRoutesPage.order_a_taxi_button).click()
        #click en la tafifa comfort
    def click_fare_comfort(self):
     WebDriverWait(self.driver,40 ).until(expected_conditions.visibility_of_element_located(localizadores.LUrbanRoutesPage.fare_comfort))
     self.driver.find_element(*localizadores.LUrbanRoutesPage.fare_comfort).click()
    def corroborate_rate(self):
        return self.driver.find_element(*localizadores.LUrbanRoutesPage.label).text
    #se ingresaron esperas en algunos elementos
    #rellenar el numero detéfono
    #click en el campo número de telefono
    def wait_for_phone_number_button(self):
        WebDriverWait (self.driver,40).until(expected_conditions.element_to_be_clickable(localizadores.LUrbanRoutesPage.phone_number_button))
    def click_phone_number_button(self):
        WebDriverWait(self.driver,40).until(expected_conditions.element_to_be_clickable(localizadores.LUrbanRoutesPage.phone_number_button))
        self.driver.find.element(*localizadores.LUrbanRoutesPage.phone_number_button).click()
    #Llenar el campo número de telefono
    def set_number_field(self):
        WebDriverWait(self.driver,40 ).until(expected_conditions.visibility_of_element_located(localizadores.LUrbanRoutesPage.number_field))
        self.driver.find.element(*localizadores.LUrbanRoutesPage.number_field).send_keys(data.phone_number)
        #click en el boton siguiente
    def click_button_next(self):
         self.driver.find.element(*localizadores.LUrbanRoutesPage.button_next).click()
    #llenar el campo introducir codigo
    def set_confirmation_code(self,code):
        WebDriverWait(self.driver,40).until(expected_conditions.visibility_of_element_located(localizadores.LUrbanRoutesPage.enter_code_field))
        self.driver.find.element(*localizadores.LUrbanRoutesPage.enter_code_field).send_keys(code)
    #click en el boton confirmar
    def click_button_confirm_code(self):
        self.driver.find_element(+localizadores.LUrbanRoutesPage.button_confirm_code).click()
    def get_phone_number(self):
         return self.driver.find.element(*localizadores.LUrbanRoutesPage.phone_number_button).text
    #se ingresaron esperas en algunos elementos
    #agregar una tarjeta de crédito
    #click botón metodo de pago
    def wait_payment_method_button(self):
        WebDriverWait(self.driver,40).until(expected_conditions.element_to_be_clickable(localizadores.LUrbanRoutesPage.payment_method_button))
    def click_payment_method_button(self):
        WebDriverWait(self.driver,40).until(expected_conditions.element_to_be_clickable(localizadores.LUrbanRoutesPage.payment_method_button))
        self.driver.find_element(*localizadores.LUrbanRoutesPage.payment_method_button).click()
    #click en agregar tarjeta
    def click_add_card(self):
        self.driver.find.element(*localizadores.LUrbanRoutesPage.add_card).click()
    #llenar númeror de tajeta
    def set_card_number_field(self):
        self.driver.find.element(*localizadores.LUrbanRoutesPage.card_number_field).send_keys(data.card_number)
    #llenar codigo de tarjeta
    def set_card_code_field(self):
        WebDriverWait(self.driver,40 ).until(expected_conditions.presence_of_element_located(localizadores.LUrbanRoutesPage.card_code_field))
        self.driver.find.element(*localizadores.LUrbanRoutesPage.card_code_field).send_keys(data.card_code)
    #presiona click afuera
    def click_out_side(self):
        self.driver.find.element(*localizadores.LUrbanRoutesPage.click_out).click()
    #click al botón agregar
    def click_add_button(self):
        self.driver.find.element(*localizadores.LUrbanRoutesPage.add_button).click()
    #click en el botón cerrar de la ventana metodo de pago
    def click_button_close_window_payment_method(self):
        WebDriverWait(self.driver,40).until(expected_conditions.presence_of_element_located(localizadores.LUrbanRoutesPage.button_close_window_payment_method))
        self.driver.find_element(*localizadores.LUrbanRoutesPage.button_close_window_payment_method).click()
    def check_close_button_is_enabled(self):
        return self.driver.find_element(*localizadores.LUrbanRoutesPage.button_close_window_payment_method).is_enabled()
    #se ingresaron esperas en algunos elementos
    #escribir un mensaje para el conductor
    # cliclk en el mensaje para el conductor
    def wait_message_for_driver(self):
     WebDriverWait(self.driver,40).until(expected_conditions.element_to_be_clickable(localizadores.LUrbanRoutesPage.message_for_driver))
    def click_message_for_driver(self):
        self.driver.find_element(*localizadores.LUrbanRoutesPage.message_for_driver).click()
    def set_write_message(self):
        WebDriverWait(self.driver,20 ).until(expected_conditions.visibility_of_element_located(localizadores.LUrbanRoutesPage.message_for_driver))
     #escribir mensaje para el conductor
        self.driver.find.element(*localizadores.LUrbanRoutesPage.write_message).send_keys(data.message_for_driver)
    def verify_message(self):
        return self.driver.find_element(*localizadores.LUrbanRoutesPage.write_message).get_property('value')
    #pedir manta y pañuelos
    def click_slider_round_button(self):
        WebDriverWait(self.driver,20 ).until(expected_conditions.element_to_be_clickable(localizadores.LUrbanRoutesPage.slider_round_button))
        self.driver.find.element(*localizadores.LUrbanRoutesPage.slider_round_button).click()
    def check_slider_button_is_enable(self):
        return self.driver.find_element(*localizadores.LUrbanRoutesPage.slider_round_button).is_enabled()
    #pedir 2 helados
    def click_ice_cream_counter(self):
        WebDriverWait(self.driver,20 ).until(expected_conditions.element_to_be_clickable(localizadores.LUrbanRoutesPage.ice_cream_counter))
        self.driver.find.element(*localizadores.LUrbanRoutesPage.ice_cream_counter).click()
        self.driver.find.element(*localizadores.LUrbanRoutesPage.ice_cream_counter).clic()
    def verify_quantity_icecream(self):
        return self.driver.find.element(*localizadores.LUrbanRoutesPage.counter_value).text
    #click en el boton pedir un taxi
    def click_order_taxi_button(self):
        WebDriverWait(self.driver,20 ).until(expected_conditions.element_to_be_clickable(localizadores.LUrbanRoutesPage.order_a_taxi_button))
        self.driver.find_element(*localizadores.LUrbanRoutesPage.order_a_taxi_button).click()
    def check_waiting_time_is_enabled(self):
        return self.driver.find_element(*localizadores.LUrbanRoutesPage.waiting_time).is_enabled()

