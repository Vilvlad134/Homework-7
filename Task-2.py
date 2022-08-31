from pprint import pprint

def load_cook_book():
    with open('Recipes.txt', 'r', encoding='utf-8') as cur_file:
        cook_book = {}
        for line in cur_file:
            dish_name = line[:-1]
            counter = cur_file.readline().strip()
            list_of_ingridient = []
            for i in range(int(counter)):
                dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])
                ingridient = cur_file.readline().strip().split(' | ')
                for item in ingridient:
                    dish_items['ingredient_name'] = ingridient[0]
                    dish_items['quantity'] = ingridient[1]
                    dish_items['measure'] = ingridient[2]
                list_of_ingridient.append(dish_items)
                cook_list = {dish_name: list_of_ingridient}
                cook_book.update(cook_list)
            cur_file.readline()
    return(cook_book)

def making_shop_list(dishes, persons=int):
    menu = load_cook_book()
    print()
    shopping_list = {}
    try:
        for dish in dishes:
            for item in (menu[dish]):
                items_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity'])*persons})])
                if shopping_list.get(item['ingredient_name']):
                    extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
                                  int(items_list[item['ingredient_name']]['quantity']))
                    shopping_list[item['ingredient_name']]['quantity'] = extra_item

                else:
                    shopping_list.update(items_list)

        print(f"Для приготовления требуемых блюд на {persons} человек  нам необходимо купить:")
        pprint(shopping_list)
    except KeyError:
        print("Вы ошиблись в названии блюда, проверьте ввод")




if __name__ == "__main__":
    print()
    print(f'Список доступных блюд:')
    pprint(load_cook_book(), indent=5, width=160, sort_dicts=False)
    print()
    making_shop_list(['Омлет', 'Утка по-пекински'], 8)