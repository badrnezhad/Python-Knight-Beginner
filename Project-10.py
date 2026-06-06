password = input("رمزعبور: ")
repeat_password = input("تکرار رمزعبور: ")

is_same = password == repeat_password
has_alpha_number = password.isalnum()

result = is_same and has_alpha_number

print(result)
