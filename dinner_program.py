import csv
import random

recipes = dict()

def process_recipes():
	with open('recipes.csv') as recipe_file:
		reader = list(csv.reader(recipe_file))
		title_row = reader[0]
		for title in title_row:
			recipes[title] = []

		for i in range(len(reader) - 1):
			if i > 0:
				row = reader[i]
				recipes["title"].append(row[0])
				recipes["description"].append(row[1])

				#ingredients
				ingredients_list = row[2]
				recipes["ingredients"].append([])
				for ingredient in ingredients_list.split(','):
					recipes["ingredients"][i - 1].append(ingredient)

				recipes["is_main_dish"].append(row[3])

				#side dishes (may not exist)
				if len(row) > 4:
					side_dish_list = row[4]
					recipes["recommended_side_dishes"].append([])
					for side_dish in side_dish_list.split(','):
						recipes["recommended_side_dishes"][i - 1].append(side_dish)
				else:
					recipes["recommended_side_dishes"].append("")

def print_ingredients(recipe_index):
	print("\nIngredients List:")
	for ingredient in recipes["ingredients"][recipe_index]:
		print(ingredient.capitalize())
	print("\nHappy cooking!\n\n")

def print_random_recipe():
	random_int = random.randrange(len(recipes["title"]))
	print(recipes["title"][random_int].capitalize())
	print(recipes["description"][random_int].capitalize())
	return(random_int)

def get_dinner_inspo():
	ingredient_ideas = input("Is there anything you're in the mood for? (o for options) \n").lower()
	if ingredient_ideas == "" or ingredient_ideas == "no" or ingredient_ideas == "n":
		print("I see you don't have any ideas for dinner. No worries! I'll randomize all recipe ideas for you. How does this sound? \n")
		done = "m"
		while done != "q" and done != "i":
			recipe_index = print_random_recipe()
			print()
			done = input("i for ingredients, m for more ideas, q to quit \n").lower()
			print()
			if done != "i" and done != "q" and done != "m":
				print("You must choose from options i, m, or q")
			elif done == "m":
				print("I see you didn't like that one. I'll choose another. How does this sound? \n")
		if done == "i":
			print_ingredients(recipe_index)
	# if ingredient_ideas = "o" display a list of all ingredients, alphabetized
    # else search for ingredient and display list of titles including that ingredient

def look_up_recipe():
	print("TODO")
	# probably need to do some sort of soft title search for recipe or display list of recipes, then print recipe

def add_recipe():
	print("TODO")
	# write to csv, some data required
		
if __name__ == "__main__":
	print()
	print("Thank you for choosing Rachel and Rowen's dinner choice program. \n")
	print("Processing current updated recipe book.... \n")
	process_recipes()
	print(recipes["ingredients"][0])
	print("Processing complete. \n")
	print("_________________________________________")
	option = 1
	while option > 0 and option < 4: 
		option = int(input("Choose from the following actions: \n 1 - Get dinner inspiration \n 2 - Look up recipe \n 3 - Add recipe \n "))
		if option == 1:
			get_dinner_inspo()
			option = 0
		elif option == 2:
			look_up_recipe()
			option = 0
		elif option == 3:
			add_recipe()
			option = 0
		else:
			print("You must choose options 1-3 (0 to quit)")

