def name_and_number():
    print('商品名を入力してください')
    name = input() #商品名の変数
    print('個数を整数で入力してください')
    number = int(input())#個数の変数,この後の計算のために個数を整数型に
    return name,number

def sale(list_price,list_number):
        list_sales = {}
        sales=0
        for name in list_number:
            list_sales[name] = list_number[name]*list_price[name]
            sales = sales+list_sales[name]
        return list_sales,sales

#レジ登録作業
def registar(list_price):
    list_number = {'A':0,'B':0,'C':0,'D':0}
    while(True):
        #商品の名前と個数を取得/単純にreturnの１つ目をnameに、２つ目をnumberに渡してる
        name,number = name_and_number()
        #この会計での商品の個数をカウント
        list_number[name] = list_number[name] + number
        #この会計での総和を計算
        list_sales,sales = sale(list_price, list_number)
        print('商品名:{}  個数:{}  価格:{}'.format(name,number,list_price[name]))
        print(f'総売上:{sales}円')
        
        print('商品登録を終わりますか（yes/no）')
        # breakされるまでwhileループ
        if input() == 'yes':
            break
        else:
            continue
 
    print('各商品の個数',list_number)
    print('各商品の売上合計',list_sales)
    print('総売上',sales)

list_price = {'A':120,'B':110,'C':200,'D':100}
registar(list_price)