
def calc_salary(hourly_rate, work_time_percentage, additional_pay_percentage):
    """
    Calculate the salary from given parameters
    :param hourly_rate: payment received by employee in euro per hour
    :param work_time_percentage: working time in percentage
    :param additional_pay_percentage: percentage of additional payment that has to be included in the salary
    :return:
    """
    if hourly_rate < 0 or work_time_percentage < 0 or \
            work_time_percentage > 100 or additional_pay_percentage < 0:
        return None
    salary = (hourly_rate * (40 * (work_time_percentage / 100))) * 4
    return salary + (salary * (additional_pay_percentage / 100))
