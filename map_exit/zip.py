#using the ipfunction for various reasons
list_1={1,2,3}
list_2={'red','blue','green'}
list_result=list(zip(list_1,list_2))
print("the result of zipping these two lists in list form is :", list_result)

#second method
list_11=[10,20,30,40]
list_22=[100,200,300,400]
for x,y in zip(list_11,list_22[::-1]):
    print("the result is :",x,y)

# suing zip in converting list into dictionary
stocks=['asics','yonex','li-ning']
prices=[2500,1500,3000]

stock_price={stocks:prices for stocks,prices in zip(stocks,prices)}
print('The starting price of the badminton shoes fo these compznies are :',stock_price)