class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        match = []
        for product in self.products:
            if product[0] == first_letter:
                match.append(product)
        return match

    def __repr__(self):
        returning_string = f"Items in the {self.name} catalogue:\n"
        returning_string += "\n".join(sorted(self.products))
        return returning_string

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")

catalogue1 = Catalogue("asda")
catalogue1.add_product("Sofdgfdfa")
catalogue1.add_product("Mirdfgdfgror")
catalogue1.add_product("dfg")
catalogue1.add_product("Chair")
catalogue1.add_product("Cadfgfdrpehg")
print(catalogue1.get_by_letter("C"))
print(catalogue1)