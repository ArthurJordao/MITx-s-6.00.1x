def pay_debt_in_period_months(balance, annual_interest_rate, monthly_payment, time_remain_months):
    unpaid = balance - monthly_payment
    interest = annual_interest_rate / 12 * unpaid
    if time_remain_months == 1:
        return unpaid + interest
    else:
        return pay_debt_in_period_months(unpaid + interest, annual_interest_rate, monthly_payment,
                                         time_remain_months - 1)

# Test values
balance = 3926
annualInterestRate = 0.2

payment = 10

while True:
    balance_in_year = pay_debt_in_period_months(balance, annualInterestRate, payment, 12)
    if balance_in_year < 0:
        break
    payment += 10

print('Lowest Payment: ' + str(payment))
