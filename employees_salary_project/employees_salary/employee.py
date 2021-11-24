

class Employees:
    def __init__(self, emp_no, first_name, last_name,   **kwargs):
        super().__init__(**kwargs)
        self.emp_no = emp_no
        self.first_name = first_name
        self.last_name = last_name