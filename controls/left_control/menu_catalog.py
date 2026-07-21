class MenuCatalog:

    def __init__(self, page):
        self.page = page

    # селекторы
    _catalog_selector = "//span[text()='Каталог']"

    _electronic_products_selector = "//div[@class='pt-5']//a[@href='/catalog/pechatnye-i-elektronnye-izdaniya/']"
    _for_supervisor_selector = "//div[@class='pt-5']//a[contains(@href,'izdaniya-dlya-rukovoditelya')]"
    _for_financier_selector = "//div[@class='pt-5']//a[contains(@href,'izdaniya-dlya-finansista')]"
    _for_accountant_selector = "//div[@class='pt-5']//a[contains(@href,'izdaniya-dlya-bukhgaltera')]"
    _for_hr_selector = "//div[@class='pt-5']//a[contains(@href,'izdaniya-dlya-kadrovika')]"
    _for_lawyer_selector = "//div[@class='pt-5']//a[contains(@href,'izdaniya-dlya-yurista')]"

    _professional_training_selector = "//div[@class='pt-5']//a[@href='/catalog/professionalnoe-obuchenie-/']"
    _for_supervisor_prof_selector = "//div[@class='pt-5']//a[contains(@href,'/dlya-rukovoditelya/')]"
    _for_financier_prof_selector = "//div[@class='pt-5']//a[contains(@href,'/dlya-finansista/')]"
    _for_accountant_prof_selector = "//div[@class='pt-5']//a[contains(@href,'/dlya-bukhgaltera/')]"
    _for_hr_prof_selector = "//div[@class='pt-5']//a[contains(@href,'/dlya-kadrovika/')]"
    _for_lawyer_prof_selector = "//div[@class='pt-5']//a[contains(@href,'/dlya-yurista/')]"
    _for_engineer_builder_prof_selector = "//a[contains(@href,'/dlya-inzhenera-i-stroitelya/')]"
    _for_student_prof_selector = "//a[contains(@href,'/dlya-studenta/')]"
    _for_teacher_prof_selector = "//a[contains(@href,'/dlya-prepodavatelya/')]"

    _electronic_services_selector = "//div[@class='pt-5']//a[@href='/catalog/elektronnye-servisy/']"
    _verification_counterparties_selector = "//div[@class='pt-5']//a[contains(@href,'/proverka-kontragentov/')]"

    # локаторы
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
        return self.page.locator(self._for_supervisor_prof_selector)

    def for_financier2_locator(self):
        return self.page.locator(self._for_financier_prof_selector)

    def for_accountant2_locator(self):
        return self.page.locator(self._for_accountant_prof_selector)

    def for_hr2_locator(self):
        return self.page.locator(self._for_hr_prof_selector)

    def for_lawyer2_locator(self):
        return self.page.locator(self._for_lawyer_prof_selector)

    def for_engineer_builder_locator(self):
        return self.page.locator(self._for_engineer_builder_prof_selector)

    def for_student_locator(self):
        return self.page.locator(self._for_student_prof_selector)

    def for_teacher_locator(self):
        return self.page.locator(self._for_teacher_prof_selector)

    def electronic_services_locator(self):
        return self.page.locator(self._electronic_services_selector)

    def verification_counterparties_locator(self):
        return self.page.locator(self._verification_counterparties_selector)

    # методы
    def collection_of_unique_locators(self):
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
