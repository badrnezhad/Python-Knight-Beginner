base_amount = int(input("مبلغ پایه: "))
percentage_increase = int(input("درصدر افزایش: "))
years = int(input("تعداد سال‌ها: "))

annual_increase = base_amount * percentage_increase
total_increase = annual_increase * years
final_amount = base_amount + total_increase

print(f"افزایش سالانه‌: {annual_increase}")
print(f"مجموع افزایش: {total_increase}")
print(f"مبلغ نهایی: {final_amount}")
