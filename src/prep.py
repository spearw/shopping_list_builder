import csv

class RecipePrepper:
    
    def __init__(self) -> None:
        pass



    def load_overview(self, overview_path):
        print("Loading overview...")
    
        with open(overview_path, newline='') as csvfile:
            recipe_reader = csv.reader(csvfile)

            recipes = {}
            for recipe in recipe_reader:
                # Convert row to list
                recipes[recipe[0]] = recipe[1]
            return recipes

    def parse_recipes(self, recipes):

        # Remove header
        recipes.pop("recipe_name")

        ingredients = {}

        for recipe in recipes:
            recipe_amount = recipes[recipe]
            recipe = recipe.replace(" ", "_")
            recipe_title = recipe.replace("_", " ").title()
            recipe_path = "data/recipes/" + recipe + ".csv"
            print(f"Loading recipe: {recipe_title} * {recipe_amount}")
            if recipe_amount == "0":
                print(f"Skipping {recipe_title}")
                continue
            with open(recipe_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    ingredient_name = row[0].lower()
                    ingredient_amount = ingredients.get(ingredient_name, 0)
                    amount_to_add = int(row[1]) * int(recipe_amount)
                    ingredients[ingredient_name] = ingredient_amount + amount_to_add

        return ingredients

    def main(self):
        recipes = self.load_overview("data/overview.csv")
        ingredients = self.parse_recipes(recipes)
        print(ingredients)



if __name__ == '__main__':
    recipe_prepper = RecipePrepper()
    recipe_prepper.main()
    