list_price  = {'コーヒー':120,'お茶':110,'エナジードリンク':200,'水':100}
# 辞書型をfor文にかけるとキーを返す
# 値を取り出すにはメソッド名[キー名]
for name in list_price:
    print(name)
    print(list_price[name])