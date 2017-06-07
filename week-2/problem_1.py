def pay_debt_in_period_months(balance, annual_interest_rate, monthly_payment_rate, time_remain_months):
    unpaid = balance - monthly_payment_rate * balance
    interest = annual_interest_rate / 12 * unpaid
    if time_remain_months == 1:
        return unpaid + interest
    else:
        return pay_debt_in_period_months(unpaid + interest, annual_interest_rate, monthly_payment_rate,
                                         time_remain_months - 1)

# Test case
# balance = 484
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04
#
# print('Remaining balance: ' +
#       str(round(pay_debt_in_period_months(balance, annualInterestRate, monthlyPaymentRate, 12),2)))
