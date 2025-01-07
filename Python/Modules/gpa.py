import tkinter as tk
from tkinter import messagebox

class GPACalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("GPA Calculator")
        self.geometry("400x300")
        self.courses = []

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self, text="GPA Calculator", font=("Helvetica", 16)).pack(pady=10)

        self.course_frame = tk.Frame(self)
        self.course_frame.pack(pady=10)

        self.add_course_entry()

        self.add_course_button = tk.Button(self, text="Add Another Course", command=self.add_course_entry)
        self.add_course_button.pack(pady=10)

        self.calculate_button = tk.Button(self, text="Calculate GPA", command=self.calculate_gpa)
        self.calculate_button.pack(pady=10)

        self.result_label = tk.Label(self, text="GPA: N/A", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

    def add_course_entry(self):
        course_row = tk.Frame(self.course_frame)
        course_row.pack(fill='x', pady=5)

        tk.Label(course_row, text="Course Name").pack(side='left', padx=5)
        course_name = tk.Entry(course_row)
        course_name.pack(side='left', padx=5)

        tk.Label(course_row, text="Grade").pack(side='left', padx=5)
        grade = tk.Entry(course_row)
        grade.pack(side='left', padx=5)

        tk.Label(course_row, text="Credit Hours").pack(side='left', padx=5)
        credit_hours = tk.Entry(course_row)
        credit_hours.pack(side='left', padx=5)

        self.courses.append((course_name, grade, credit_hours))

    def grade_to_points(self, grade):
        grade_point_map = {
            'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0
        }
        return grade_point_map.get(grade.upper(), 0.0)

    def calculate_gpa(self):
        total_grade_points = 0
        total_credit_hours = 0
        try:
            for course in self.courses:
                grade = course[1].get()
                credit_hours = float(course[2].get())
                grade_points = self.grade_to_points(grade)

                if grade.upper() not in ['A', 'B', 'C', 'D', 'F']:
                    raise ValueError("Invalid grade entered")

                total_grade_points += grade_points * credit_hours
                total_credit_hours += credit_hours

            gpa = total_grade_points / total_credit_hours if total_credit_hours else 0
            self.result_label.config(text=f"GPA: {gpa:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid grades and credit hours.")

if __name__ == "__main__":
    GPACalculator = GPACalculator()
    GPACalculator.mainloop()
