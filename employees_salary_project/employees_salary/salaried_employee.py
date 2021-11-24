
from .employee import Employees

class Salaried_employee(Employees):
    def __init__(self, emp_no, first_name, last_name, job_title, **kwargs):
        super().__init__(emp_no, first_name, last_name,**kwargs)
        self.job_title = job_title
    
        
    def calculate_salary(self):
        basic_salary_dict = dict()
        basic_salary_dict={
            'Senior Engineer':27000,
            'Staff':10000,
            'Engineer':15000,
            'Assistant Engineer':10000,
            'Senior Staff': 15000

        }
        salary = basic_salary_dict[self.job_title] 
        return salary

    def show_salary(self):
        salary = str(self.calculate_salary())
        row_string = """<tr><td>""" + str(self.emp_no) + """</td><td>"""+ str(self.first_name) +"""</td><td>"""+ str(self.last_name) +"""</td><td>""" +  salary + """</td></tr>"""
        return(row_string)