def sale(list_price,list_number):
    list_sales = {} #各商品の在庫を売り上げに換算した金額
    sales=0 #在庫全てを売り上げに換算した金額
    #辞書型はキーが代入されるので、順番にnameに商品名を代入
    for name in list_number: 
        list_sales[name] = list_number[name]*list_price[name] #個数×値段で売り上げに換算
        sales = sales+list_sales[name] #各商品の売り上げ換算額を合計
    return list_sales,sales 

list_price = {'コーヒー':120,'お茶':110,'エナジードリンク':200,'水':100}
list_number = {'コーヒー':1000,'お茶':500,'エナジードリンク':100,'水':2000}
list_sales,sales=sale(list_price,list_number)
print('各商品の在庫の売り上げ換算金額',list_sales)
print('全商品の在庫の売り上げ換算金額',sales)