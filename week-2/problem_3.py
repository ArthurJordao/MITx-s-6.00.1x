def pay_debt_in_period_months(balance, annual_interest_rate, monthly_payment, time_remain_months):
    unpaid = balance - monthly_payment
    interest = annual_interest_rate / 12 * unpaid
    if time_remain_months == 1:
        return unpaid + interest
    else:
        return pay_debt_in_period_months(unpaid + interest, annual_interest_rate, monthly_payment,
                                         time_remain_months - 1)


def compare_balance_with_zero(balance):
    """
    :param balance: a double with the value of the balance in after a year.
    :return: 0 if the balance is equal to zero or nearly equal, 1 if the balance is greater than zero and -1 if
    the balance is lower than zero.
    """
    if 0.05 >= balance >= -0.05:
        return 0
    elif balance > 0.05:
        return 1
    else:
        return -1

balance = 320000
annualInterestRate = 0.2

monthly_interest_rate = annualInterestRate / 12
monthly_payment_lower_bound = balance / 12
monthly_payment_upper_bound = (balance * (1 + monthly_interest_rate) ** 12) / 12


while True:
    payment = monthly_payment_lower_bound + (monthly_payment_upper_bound - monthly_payment_lower_bound) / 2
    after_year_balance = pay_debt_in_period_months(balance, annualInterestRate, payment, 12)
    compare = compare_balance_with_zero(after_year_balance)
    if compare == 0:
        break
    elif compare == 1:
        monthly_payment_lower_bound = payment
    else:
        monthly_payment_upper_bound = payment

print('Lowest Payment: ' + str(round(payment, 2)))
