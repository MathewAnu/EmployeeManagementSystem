
def calc_salary(hourly_rate, work_time_percentage, additional_pay_percentage):
    if hourly_rate < 0 or work_time_percentage < 0 or \
            work_time_percentage > 100 or additional_pay_percentage < 0:
        return None
    salary = (hourly_rate * (40 * (work_time_percentage / 100))) * 4
    return salary + (salary * (additional_pay_percentage / 100))
