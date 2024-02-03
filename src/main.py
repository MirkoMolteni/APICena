from cocktail_lib import Cocktail
from meal_lib import Meal

MEAL = Meal()
COCKTAIL = Cocktail()
def main():
    global MEAL
    global COCKTAIL
    print("In questo programma andremo a decidere cosa mangiare e cosa bere!")
    print("Per prima cosa iniziamo dal mangiare")
    print("Puoi scegliere tra i seguenti comandi:")
    print("1. Cerca pasto per nome")
    print("2. Cerca pasto per ingrediente")
    print("3. Pasto casuale")
    chooseM = input("Inserisci il numero corrispondente al comando: ")
    infoMeal = ""
    if chooseM == "1":
        name = input("Inserisci il nome del pasto: ")
        infoMeal = MEAL.get_meal(name)
    elif chooseM == "2":
        ingredient = input("Inserisci l'ingrediente: ")
        infoMeal = MEAL.get_meals_by_ingredient(ingredient)
    elif chooseM == "3":
        infoMeal = MEAL.get_random_meal()
    
    print("Ora passiamo ai cocktail")
    print("Puoi scegliere tra i seguenti comandi:")
    print("1. Cerca cocktail per nome")
    print("2. Cerca cocktail per ingrediente")
    print("3. Cocktail casuale")
    print("4. Cocktail analcolici")
    print("5. Cocktail alcolici")
    chooseC = input("Inserisci il numero corrispondente al comando: ")
    infoCocktail = ""
    if chooseC == "1":
        name = input("Inserisci il nome del cocktail: ")
        infoCocktail = COCKTAIL.get_cocktail(name)
    elif chooseC == "2":
        ingredient = input("Inserisci l'ingrediente: ")
        infoCocktail = COCKTAIL.get_cocktails_by_ingredient(ingredient)
    elif chooseC == "3":
        infoCocktail = COCKTAIL.get_random_cocktail()
    elif chooseC == "4":
        infoCocktail = COCKTAIL.get_non_alcoholic_cocktails()
    elif chooseC == "5":
        infoCocktail = COCKTAIL.get_alcoholic_cocktails()
        
    print("Ecco cosa ho trovato")
    if chooseM == "1" or chooseM == "3":
        print("Pasto:")
        print("Nome del piatto: "+infoMeal["meals"][0]["strMeal"])
        print("Categoria: "+infoMeal["meals"][0]["strCategory"])
        print("Istruzioni: \r\n"+infoMeal["meals"][0]["strInstructions"].replace("\r\n\r\n", "\r\n"))
        print("Ingredienti:")
        for i in range(1, 21):
            if infoMeal["meals"][0]["strIngredient"+str(i)] != "":
                print(infoMeal["meals"][0]["strIngredient"+str(i)] + " : " + infoMeal["meals"][0]["strMeasure"+str(i)])
    elif chooseM == "2":
        print("Pasti trovati:")
        for meal in infoMeal["meals"]:
            print("Nome: " + meal["strMeal"])
    
    print("\r\n\r\n")
    if chooseC == "1" or chooseC == "3":    
        print("Cocktail:")
        print("Nome del cocktail: "+infoCocktail["drinks"][0]["strDrink"])
        print("Categoria: "+infoCocktail["drinks"][0]["strCategory"])
        print("Istruzioni: \r\n"+infoCocktail["drinks"][0]["strInstructionsIT"])
        print("Ingredienti:")
        for i in range(1, 16):
            if infoCocktail["drinks"][0]["strIngredient"+str(i)] != "":
                print(infoCocktail["drinks"][0]["strIngredient"+str(i)] + " : " + str(infoCocktail["drinks"][0]["strMeasure"+str(i)]))
    elif chooseC == "2":
        print("Cocktail trovati:")
        for cocktail in infoCocktail["drinks"]:
            print("Nome: " + cocktail["strDrink"])
    elif chooseC == "4":
        print("Cocktail analcolici trovati:")
        for cocktail in infoCocktail["drinks"]:
            print("Nome: " + cocktail["strDrink"])
    elif chooseC == "5":
        print("Cocktail alcolici trovati:")
        for cocktail in infoCocktail["drinks"]:
            print("Nome: " + cocktail["strDrink"])
    

if __name__ == "__main__":
    main()