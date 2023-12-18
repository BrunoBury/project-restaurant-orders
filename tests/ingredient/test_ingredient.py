from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    ingredients = {
        "queijo mussarela": {
            "name": "queijo mussarela",
            "restrictions": {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED},
        },
        "farinha": {"name": "farinha", "restrictions": {Restriction.GLUTEN}},
    }

    for name, expected_values in ingredients.items():
        ingredient = Ingredient(name)

        assert ingredient.name == expected_values["name"]

        assert set(ingredient.restrictions) == expected_values["restrictions"]

        assert repr(ingredient) == f"Ingredient('{expected_values['name']}')"

        same_ingredient = Ingredient(name)
        assert ingredient == same_ingredient

        assert hash(ingredient) == hash(same_ingredient)
