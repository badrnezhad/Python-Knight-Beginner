postal_code = input("کدپستی را وارد کنید:")

if len(postal_code) == 10 and postal_code.isdigit():
    print("کدپستی معتبر است ✅")
else:
    print("کدپستی معتبر نیست ❌")

