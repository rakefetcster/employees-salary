
from .employee import Employees


class Hourly_employee(Employees):
    def __init__(self, emp_no, first_name, last_name, job_title, working_hours, **kwargs):
        super().__init__(emp_no, first_name, last_name, **kwargs)
        self.job_title = job_title
        self.working_hours = working_hours
        
    def calculate_salary(self):
        basic_salary_dict = dict()
        basic_salary_dict={
            'Senior Engineer':150,
            'Staff':80,
            'Engineer':120,
            'Assistant Engineer':90,
            'Senior Staff': 120
        }
        salary = basic_salary_dict[self.job_title] * self.working_hours 
        return salary

    def show_salary(self):
        salary = str(self.calculate_salary())
        row_string = """<tr><td>""" + str(self.emp_no) + """</td><td>"""+ str(self.first_name) +"""</td><td>"""+ str(self.last_name) +"""</td><td>""" + salary +"""</td></tr>"""
        return(row_string)
