from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish = Dish("Lasanha", 15.99)
    same_dish = Dish("Lasanha", 15.99)
    different_dish = Dish("Pizza", 12.50)

    assert isinstance(dish, Dish)
    assert dish.name == "Lasanha"
    assert dish.price == 15.99
    assert dish.recipe == {}
    assert dish == same_dish
    assert dish != different_dish

    ingredient1 = Ingredient("massa de lasanha")
    ingredient2 = Ingredient("queijo mussarela")
    dish.add_ingredient_dependency(ingredient1, 500)
    dish.add_ingredient_dependency(ingredient2, 200)

    assert dish.recipe.get(ingredient1) == 500
    assert dish.recipe.get(ingredient2) == 200

    assert set(dish.get_ingredients()) == {ingredient1, ingredient2}

    expected_restrictions = {
        Restriction.GLUTEN,
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
    assert set(dish.get_restrictions()) == expected_restrictions

    with pytest.raises(TypeError):
        Dish("não existe", "not float")

    with pytest.raises(ValueError):
        Dish("Prato sem valor", -5.00)

    assert hash(dish) == hash(same_dish)
    assert hash(dish) != hash(different_dish)
    assert repr(dish) == f"Dish('Lasanha', R${15.99:.2f})"
