class MenuCatalog:

    def __init__(self, page):
        self.page = page

    # селекторы
    _catalog_selector = "//span[text()='Каталог']"

    _electronic_products_selector = "//div[@class='pt-5']//a[@href='/catalog/pechatnye-i-elektronnye-izdaniya/']"
    _for_supervisor_selector = (
        "//div[@class='pt-5']//a[@href='/catalog/pechatnye-i-elektronnye-izdaniya/izdaniya-dlya-rukovoditelya/']")
    _for_financier_selector = (
        "//div[@class='pt-5']//a[@href='/catalog/pechatnye-i-elektronnye-izdaniya/izdaniya-dlya-finansista/']")
    _for_accountant_selector = (
        "//div[@class='pt-5']//a[@href='/catalog/pechatnye-i-elektronnye-izdaniya/izdaniya-dlya-bukhgaltera/']")
    _for_hr_selector = (
        "//div[@class='pt-5']//a[@href='/catalog/pechatnye-i-elektronnye-izdaniya/izdaniya-dlya-kadrovika/']")
    _for_lawyer_selector = (
        "//div[@class='pt-5']//a[@href='/catalog/pechatnye-i-elektronnye-izdaniya/izdaniya-dlya-yurista/']")

    _professional_training_selector = "//div[@class='pt-5']//a[@href='/catalog/professionalnoe-obuchenie-/']"
    _for_supervisor2_selector = (
        "//div[@class='pt-5']//a[@href='/catalog/professionalnoe-obuchenie-/dlya-rukovoditelya/']")
    _for_financier2_selector = (
        "//div[@class='pt-5']//a[@href='/catalog/professionalnoe-obuchenie-/dlya-finansista/']")
    _for_accountant2_selector = (
        "//div[@class='pt-5']//a[@href='/catalog/professionalnoe-obuchenie-/dlya-bukhgaltera/']")
    _for_hr2_selector = (
        "//div[@class='pt-5']//a[@href='/catalog/professionalnoe-obuchenie-/dlya-kadrovika/']")
    _for_lawyer2_selector = (
        "//div[@class='pt-5']//a[@href='/catalog/professionalnoe-obuchenie-/dlya-yurista/']")
    _for_engineer_builder_selector = (
        "[href='/catalog/professionalnoe-obuchenie-/dlya-inzhenera-i-stroitelya/']")
    _for_student_selector = "[href='/catalog/professionalnoe-obuchenie-/dlya-studenta/']"
    _for_teacher_selector = "[href='/catalog/professionalnoe-obuchenie-/dlya-prepodavatelya/']"

    _electronic_services_selector = "//div[@class='pt-5']//a[@href='/catalog/elektronnye-servisy/']"
    _verification_counterparties_selector = (
        "//div[@class='pt-5']//a[@href='/catalog/elektronnye-servisy/proverka-kontragentov/']")

    # локатор
    def catalog_locator(self):
        return self.page.locator(self._catalog_selector)

    def electronic_products_locator(self):
        return self.page.locator(self._electronic_products_selector)

    def for_supervisor_locator(self):
        return self.page.locator(self._for_supervisor_selector)

    def for_financier_locator(self):
        return self.page.locator(self._for_financier_selector)

    def for_accountant_locator(self):
        return self.page.locator(self._for_accountant_selector)

    def for_hr_locator(self):
        return self.page.locator(self._for_hr_selector)

    def for_lawyer_locator(self):
        return self.page.locator(self._for_lawyer_selector)

    def professional_training_locator(self):
        return self.page.locator(self._professional_training_selector)

    def for_supervisor2_locator(self):
        return self.page.locator(self._for_supervisor2_selector)

    def for_financier2_locator(self):
        return self.page.locator(self._for_financier2_selector)

    def for_accountant2_locator(self):
        return self.page.locator(self._for_accountant2_selector)

    def for_hr2_locator(self):
        return self.page.locator(self._for_hr2_selector)

    def for_lawyer2_locator(self):
        return self.page.locator(self._for_lawyer2_selector)

    def for_engineer_builder_locator(self):
        return self.page.locator(self._for_engineer_builder_selector)

    def for_student_locator(self):
        return self.page.locator(self._for_student_selector)

    def for_teacher_locator(self):
        return self.page.locator(self._for_teacher_selector)

    def electronic_services_locator(self):
        return self.page.locator(self._electronic_services_selector)

    def verification_counterparties_locator(self):
        return self.page.locator(self._verification_counterparties_selector)

    # методы
    def visible_elements(self):
        return [self.catalog_locator(),
                self.electronic_products_locator(),
                self.for_supervisor_locator(),
                self.for_financier_locator(),
                self.for_accountant_locator(),
                self.for_hr_locator(),
                self.for_lawyer_locator(),
                self.professional_training_locator(),
                self.for_supervisor2_locator(),
                self.for_financier2_locator(),
                self.for_accountant2_locator(),
                self.for_hr2_locator(),
                self.for_lawyer2_locator(),
                self.for_engineer_builder_locator(),
                self.for_student_locator(),
                self.for_teacher_locator(),
                self.electronic_services_locator(),
                self.verification_counterparties_locator()]
