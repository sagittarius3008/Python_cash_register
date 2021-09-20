def name_and_number():
    print('商品名を入力してください')
    name = input()

    print('個数を整数で入力してください')
    number = int(input())
    # tupleで返る
    return name,number

print(type(name_and_number()))
