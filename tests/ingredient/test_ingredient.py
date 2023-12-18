from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    ingredient = Ingredient("queijo mussarela")

    assert isinstance(ingredient, Ingredient)

    assert ingredient.name == "queijo mussarela"

    expected_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert set(ingredient.restrictions) == expected_restrictions

    assert repr(ingredient) == "Ingredient('queijo mussarela')"

    assert ingredient == Ingredient("queijo mussarela")
    assert not (ingredient == Ingredient("frango"))

    assert hash(ingredient) == hash(Ingredient("queijo mussarela"))
    assert hash(ingredient) != hash(Ingredient("frango"))
