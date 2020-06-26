import math
import argparse
import sys


class Calculator:
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", help="type of calculation", choices=["diff", "annuity"])

    parser.add_argument("--principal", help="credit principal", type=int)

    parser.add_argument("--payment", help="monthly payments", type=float)

    parser.add_argument("--interest", help="interest", type=float)

    parser.add_argument("--periods", help="monthly periods", type=int)

    args = parser.parse_args()

    def calculate_months(self):
        c_interest = self.args.interest
        nominal_interest = c_interest / 1200

        credit_p = self.args.principal
        m_payment = self.args.payment

        log_base = m_payment / (m_payment - nominal_interest * credit_p)

        n_months = math.ceil(math.log(log_base, (1 + nominal_interest)))

        overpayment = math.ceil(n_months * m_payment - credit_p)

        if n_months % 12 == 0:
            n_years = n_months // 12

            if n_years == 1:
                print(f'You need {n_years} year to repay this credit')
            else:
                print(f'You need {n_years} years to repay this credit!')
        else:
            n_years = n_months // 12
            n_rem_months = n_months % 12

            if n_years == 0:
                print(f'You need {n_rem_months} months to repay this credit!')
            elif n_years == 1:
                print(f'You need {n_years} year and {n_rem_months} months to repay this credit!')
            else:
                print(f'You need {n_years} years and {n_rem_months} months to repay this credit!')

        print(f'Overpayment = {overpayment}')

    def calculate_monthly_payments(self):

        c_interest = self.args.interest
        nominal_interest = c_interest / 1200
        credit_p = self.args.principal
        c_periods = self.args.periods

        denominator = math.pow(1 + nominal_interest, c_periods) - 1
        numerator = nominal_interest * math.pow(1 + nominal_interest, c_periods)
        annuity_payment = math.ceil(credit_p * (numerator / denominator))

        overpayment = annuity_payment * c_periods - credit_p

        print(f'Your annuity payment = {annuity_payment}!')
        print(f'Overpayment = {overpayment}')

    def calculate_differential_payments(self):
        c_interest = self.args.interest
        nominal_interest = c_interest / 1200
        credit_p = self.args.principal
        c_periods = self.args.periods

        total_sum = 0
        # start with 1 and end with total + 1; calculations start after the month is over
        # but python is zero indexed
        for i in range(1, c_periods + 1):
            inner_fraction = (credit_p * (i - 1)) / c_periods
            bracket_data = credit_p - inner_fraction
            total_calc = math.ceil(credit_p / c_periods + nominal_interest * bracket_data)

            total_sum += total_calc

            print(f'month {i}: paid out {total_calc}')
        overpayment = total_sum - credit_p
        print()
        print(f'Overpayment = {overpayment}')

    def calculate_principal(self):

        c_interest = self.args.interest
        nominal_interest = c_interest / 1200

        c_periods = self.args.periods
        m_payment = self.args.payment

        denominator_min = math.pow(1 + nominal_interest, c_periods) - 1
        numerator_min = nominal_interest * math.pow(1 + nominal_interest, c_periods)
        denominator = numerator_min / denominator_min

        credit_principal = round(m_payment / denominator)

        overpayment = m_payment * c_periods - credit_principal

        print(f'Your credit principal = {credit_principal}!')
        print(f'Overpayment = {overpayment}')

    def intro(self):
        if len(sys.argv) != 5:
            print("Incorrect parameters!")
        else:
            if self.args.type == 'diff':
                if self.args.payment is not None:
                    print("Incorrect parameters!")
                else:
                    self.calculate_differential_payments()
            elif self.args.type == 'annuity':
                if self.args.payment is None:
                    self.calculate_monthly_payments()
                elif self.args.principal is None:
                    self.calculate_principal()
                elif self.args.periods is None:
                    self.calculate_months()


calc = Calculator()
calc.intro()
