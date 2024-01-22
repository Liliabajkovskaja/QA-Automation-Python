"""Create a dynamic shopping list.
The user can add products to the list
The user can remove products from the list
When the list is changed, a new list is printed
If the list is empty, this is reported and the program ends"""

products = input("Please enter your products: ")

if not products.strip():
    print("List of products is empty. Program has stopped")

else:
    shopping_list = products.split()
    for word in shopping_list:
        if not word.isalpha():
            print("You entered incorrect values. Program has stopped. ")
            exit()
    print(f"List of products: {shopping_list}")

    while len(shopping_list) > 0:
        action = input("Please enter your product, if you want to delete product, write \"-\" before product ")
        if action.startswith("-"):
            product_to_remove = action.lstrip('-').strip()

            if product_to_remove in shopping_list:
                shopping_list.remove(product_to_remove)
                print(f"{product_to_remove} has deleted")
            else:
                print(f"Product {product_to_remove} is not in your list")
        elif len(action) == 0:
            continue
        else:
            shopping_list.append(action)

        if shopping_list:
            print(f"New list of products: {shopping_list}")
        else:
            print("List of products is empty. Program has stopped")
