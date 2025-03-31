def diet_plan():
    return "Diet plan is working!"

def generate_diet_plan(food, goal):
    diet_plans = {
        "apple": {"weight_loss": "Eat 1 apple before meals", "muscle_gain": "Add peanut butter"},
        "burger": {"weight_loss": "Avoid or eat a smaller portion", "muscle_gain": "Include lean meat"},
        "pizza": {"weight_loss": "Limit intake", "muscle_gain": "Add veggies and protein"},
    }

    return diet_plans.get(food, {}).get(goal, "No diet suggestion available")
