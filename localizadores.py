from selenium.webdriver.common.by import By
class LUrbanRoutesPage:

    #seleccionar ruta de destino
    from_field= (By.ID, 'from')
    to_field=(By.ID, 'to')
    #seleccionar la tarifa Comfort"
    order_a_taxi_button = (By.XPATH, "//button[@type='button'][@class=´button round´and text()=´pedir un taxi´]" )
    fare_comfort =  (By.XPATH, "//*[@id='root']/div/div[3]/[3]/div[2]/div[1]/div[5]/div[1]/img")
    label=(By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[1]")
    #llenar el número de teléfono.
    phone_number_button = (By.CLASS_NAME,"np-text")
    number_field = (By.ID,'phone')
    button_next = (By.XPATH, "//button[@type='submit'][@class=´button full']")
    enter_code_field = (By.XPATH, "//*[@id='code']")
    button_confirm_code = (By. XPATH, "//*[@id'root']/div/div[1]/div[2]/div[2]/form/div[2]/button[1]")
    #agregar una tarjeta de crédito
    payment_method_button = (By.CLASS_NAME, "pp-text")
    add_card = (By.XPATH, "// *[@id='root']/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]")
    card_number_field = (By.ID,'number')
    card_code_field = (By.XPATH, "//input[@id='code' and @name='code' and @class='card-input']")
    click_out = (By.CLASS_NAME, "card-number-label")
    add_button = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/form/div[3]/button[1]")
    button_close_window_payment_method = (By.XPATH,"//div[@class='section active' and .//div[text()='Método de pago']]//button[@class='close-button section-close']")
    verified_card = (By.CLASS_NAME, "pp-value-text")
    #mensaje para el conductor
    message_for_driver = (By.XPATH, "//label[@for='comment' and contains(text(), 'Mensaje para el conductor...')]")
    write_message = (By.XPATH, "//input[@placeholder='traiga un aperitivo']")
    confirm_message = (By.CSS_SELECTOR, "input [placeholder='traiga un aperitivo' ]")#se cambio el localizador a tipo de selector
    #pedir una manta y pañuelos
    slider_round_button = (By.CSS_SELECTOR, "span.slider.round:first-of-type")#se cambio el localizador a tipo de selector
    #pedir 2 helados
    ice_cream_counter = (By.CLASS_NAME, "counter,plus")
    counter_value = (By.CLASS_NAME, "counter_value")
    #click al botón para buscar un taxi
    order_a_taxi_button = (By.CLASS_NAME, "smart_button_main")
    waiting_time = (By. CLASS_NAME, "order-header-title")


