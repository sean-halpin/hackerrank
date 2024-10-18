from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass
    
class FoodProduct(Product):
    def operation(self) -> str:
        return "Food Product"
    
class DrinkProduct(Product):
    def operation(self) -> str:
        return "Drink Product"
    
class Factory():
    # @staticmethod
    def create_product(product_type: str) -> Product:
        if product_type == "Food":
            return FoodProduct()
        elif product_type == "Drink":
            return DrinkProduct()
        else:
            raise ValueError(f'Product not found: {product_type}')
        
        
def test_factory():
    drink_prod = Factory.create_product("Drink")
    assert isinstance(drink_prod, DrinkProduct)
    assert drink_prod.operation() == "Drink Product"
    food_prod = Factory.create_product("Food")
    assert isinstance(food_prod, FoodProduct)
    assert food_prod.operation() == "Food Product"
    print("All Passed")

test_factory()

# Factory Method Pattern is a creational pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.