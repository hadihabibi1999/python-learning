
# python

weight = input('weight: ')
k_or_lbs = input("this is (k)g or (l)bs ? ")
if k_or_lbs.upper() == 'K' :
 answer = int(weight) / 0.45
 print( f'your weight(lbs): {answer} pounds')
elif k_or_lbs.upper() == 'L':
 answer = int(weight) * 0.45 
 print( f'your weight(kg): {answer} kilo grams')
else:
    print("went wrong")


