from dataclasses import dataclass
from selenium.webdriver.common.by import By
@dataclass
class MainPageLocators:
    products_images: By = (By.XPATH, "//a[@class='product_img_link']")
    submit_search: By = (By.XPATH, "//button[@name='submit_search']")
    search_bar: By = (By.ID, "search_query_top")
    sing_in_btn: By = (By.XPATH, "//a[@class='login']")
    products: By = (By.XPATH, "//div[@class='product-container']")
    sort_by_selector: By = (By.ID, "selectProductSort")
    products_availability_label: By = (By.XPATH, "//span[@class='availability']")
    product_label_ancestor: By = (By.XPATH, "./ancestor::div[@class='product-container']//a[@class='product-name']")
    form: By = (By.ID, "buy_block")
    add_to_cart_button: By = (By.XPATH, "//button[@name='Submit']")
    changeable_colors: By = (By.XPATH, "//ul[@id='color_to_pick_list']/li")
    sizes_selector: By = (By.XPATH, "//select[@id='group_1']")
    selector_options: By = (By.XPATH, "//div[@id='uniform-group_1']//option")
    successfully_added: By = (By.XPATH, "//a[@title='Proceed to checkout']")