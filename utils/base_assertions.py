from playwright.sync_api import expect


class Assertions:
    def __init__(self, page):
        self.page = page

    @staticmethod
    def all_locator(l_contacts):
        for locator in l_contacts:
            expect(locator).to_be_visible()

    @staticmethod
    def all_index_locator(l_contacts):
        index_locator = 0
        dict_locator = {x: list(y for y in range(1, int(x.count() + 1))) for x in l_contacts}
        for locator, value in dict_locator.items():
            for val in value:
                expect(locator.nth(val - 1)).to_be_visible()
                index_locator += 1
        return index_locator
