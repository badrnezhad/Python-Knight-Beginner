def get_sms_amount(amount: int):
    if amount >= 600_000_000:
        return 920
    elif amount >= 400_000_000:
        return 950
    elif amount >= 200_000_000:
        return 990
    elif amount >= 100_000_000:
        return 1100
    elif amount >= 50_000_000:
        return 1150
    elif amount >= 30_000_000:
        return 1200
    elif amount >= 20_000_000:
        return 1340
    elif amount >= 10_000_000:
        return 1390
    elif amount >= 4_000_000:
        return 1500
    elif amount >= 400_000:
        return 1550
    else:
        return 2000


price = int(input("مبلغ شارژ (ریال): "))

amount_per_sms = get_sms_amount(price)
print(f"تعرفه ارسال هر پیامک : {amount_per_sms}")
