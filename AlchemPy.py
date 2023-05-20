import os
os.system("cls")
print("""Для сохранения прогресса наберите - save and exit
 Для выыхода наберите - exit
 Для создания рецепта наберите - создать рецепты
 Для перемещения между страницами используйте знаки- < и >
""")
print("Сделайте выбор:\n1. Новая игра\n2. Загрузить пользователя")

choice = input(">>>")
if choice == "1":
    data = open("Recipes.dat", "r").read()
elif choice == "2":
    print("Выберите пользователя:")
    profiles = os.listdir("profiles")
    for i, profile in enumerate(profiles):
        print(str(i + 1) + ". " + profile)
    profile_choice = int(input(">>>"))
    profile_path = os.path.join("profiles", profiles[profile_choice - 1])
    data = open(profile_path, "r").read()
else:
    print("Некорректный выбор")
    exit()

elements = data.split("\n-\n")[0].split("\n")
recipes = data.split("\n-\n")[1]
r = []
rkeys = []
for x in recipes.split("\n"):
    com = set(x.split("=")[0].split("+"))
    res = [x.split("=")[1]]
    if com in rkeys:
        r[[x[0] for x in r].index(com)][1].append(res[0])
    else:
        rkeys.append(com)
        r.append([com, res])
recipes = r

dispPage = 0
ePerPage = 8
txt = ""
new = ""
while True:
    pages = (len(elements) - 1) // ePerPage
    print("Страница" + str(dispPage + 1) + "/" + str(pages + 1))
    plist = [x.capitalize() for x in elements[dispPage * ePerPage:(dispPage + 1) * ePerPage]]
    print("---")
    print("\n".join(plist) + "\n" * (ePerPage - len(plist)))
    print("---")
    print(txt)
    if new != "":
        print("Открыт элемент " + new)
    cin = input(">>>")
    if cin in ["next", ">", "+", "."]:
        dispPage += 1
        if dispPage * ePerPage > len(plist):
            dispPage = 0
    elif cin in ["prev", "last", "<", "-", ","]:
        dispPage -= 1
        if dispPage < 0:
            dispPage = len(plist) // ePerPage
    elif cin == "save and exit":
        filename = input("Введите сохраняемый профиль: ")
        with open(f"profiles/{filename}.dat", "w") as f:
            recipe_strings = []
            for x in recipes:
                com = "+".join(list(x[0]))
                res = "+".join(x[1])
                recipe_strings.append(com + "=" + res)
            recipe_str = "\n".join(recipe_strings)
            f.write("\n".join(elements) + "\n-\n" + recipe_str)
        exit()
    elif cin == "создать рецепты":
        username = input("Введите пользователя: ")
        recipes = []
        while True:
            recipe = input("Введите рецепты в формате элемент1+элемент2=результат(или 'сохранить рецепты' для сохранения): ")
            if recipe.lower() == "сохранить рецепты":
                break
            recipes.append(recipe)
        filename = f"custom/рецепты {username}.dat"
        with open(filename, "w") as f:
            f.write("\n".join(recipes))
        print(f"Рецепты сохранены в файле {filename}")
        exit()
    elif cin == "exit":
        exit()
    else:
        cin = set(cin.split("+"))
        for x in recipes:
            if x[0] == cin:
                new = ", ".join(x[1])
                for y in x[1]:
                    if not y in elements:
                        elements.append(y)
    os.system("cls")
