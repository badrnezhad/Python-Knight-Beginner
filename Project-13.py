temperature = int(input("دما را وارد کنید:"))

if temperature >= 30:
    print("گرم")
elif temperature >= 20:
    print("معتدل")
elif temperature >= 10:
    print("خنک")
else:
    print("سرد")
