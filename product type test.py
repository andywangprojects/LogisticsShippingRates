def categorize_product(product_name):
    # Categorize a product based on user selection: Textile, Industrial, or Agricultural
    print('choose a category for the product')
    print('1-textile')
    print('2-Industrial')
    print('3-Agricultural')
    try:
        choice=int(input('Enter the nuber of the category:'))
        if choice==1:
            return f"The product'{product_name}'is categorized as Textile"
        elif choice==2:
            return f"The prodcut'{product_name}'is categorized as Industrial"
        elif choice==3:
            return f"The product is'{product_name}'is categorized as Agricultural"
        else:
            return "Invalid choice.Please select a valid category"
    except ValueError:
        return 'Invalid input.Please enter a number.'

while True:
    product_name=input('Enter the product name(or type "exit"to quit):')
    if product_name.lower()=='exit':
        print('Exiting the program. Goodbye!')
        break
    result=categorize_product(product_name)
    print(result)
    print('-'*30)
