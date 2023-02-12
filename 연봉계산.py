#연봉
year_money = 3000
#연봉 인상률 퍼센트
up_per = 0.02
#세율
tax_per = 0.9
#저축 퍼센트
saving_per = 0.5
#일하는 총 년수
work_year = 6


#연봉 인상률
money_up = year_money * up_per
#월급
month_money = year_money / 12
#실수령 월급
true_month_money = month_money * tax_per
#실수령 연봉
true_year_money = true_month_money * 12
#한달 저축액
month_saving_money = true_month_money * saving_per
#1년 저축액
year_saving_money = month_saving_money * 12
#누적 연봉
total_year_money = year_money
#누적 실수령 연봉
total_true_year_money = true_month_money * 12
#누적 저축액
total_saving_money = year_saving_money
#연도 카운트
year = 0

for year_count in range(work_year):
    year += 1    
    print(f'''
          ******************{year}년차*******************
          
          연봉: {year_money:0.1f}만원
          월급: {month_money:0.1f}만원
          
          누적 연봉: {total_year_money:0.1f}만원
            
          -----------------실수령액--------------------
                 
          실수령 연봉: {true_year_money:0.1f}만원
          실수령 월급: {true_month_money:0.1f}만원
          
          누적 실수령 연봉: {total_true_year_money:0.1f}만원
          
          ------------------저축액---------------------
          
          한달 저축액: {month_saving_money:0.1f}만원
          1년 저축액: {year_saving_money:0.1f}만원
          
          누적 저축액: {total_saving_money:0.1f}만원          
          ''')
    year_money += money_up
    month_money = year_money / 12
    true_month_money = month_money * tax_per
    true_year_money = true_month_money * 12
    month_saving_money = true_month_money * saving_per
    year_saving_money = month_saving_money * 12
    total_year_money += year_money
    total_true_year_money += true_year_money
    total_saving_money += year_saving_money   