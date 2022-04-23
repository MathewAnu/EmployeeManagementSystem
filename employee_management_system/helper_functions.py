
def calc_salary(hourly_rate, work_time_percentage, additional_pay_percentage):
    salary = (hourly_rate * (40 * (work_time_percentage / 100))) * 4
    return salary + (salary * (additional_pay_percentage / 100))
