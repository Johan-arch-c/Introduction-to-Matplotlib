import matplotlib.pyplot as plt
student_names=["sanjay","Rahul","Karen","Tim","Jim","Kim","Ben","Ken",]
student_marks=[0,50,33,32,42,2,43,21]
marks_perc=[]
for x in student_marks:
    res=(x/50)*100
    marks_perc.append(res)
print(marks_perc)
def marks_line_chart():
    plt.plot(student_names,student_marks)
    plt.title("student marks graph")
    plt.xlabel("student names")
    plt.ylabel("student marks")
    plt.show()
marks_line_chart()
def percentage_bar_chart():
    plt.bar(student_names,marks_perc)
    plt.title("student' percentage graph")
    plt.xlabel("student names")
    plt.ylabel("student percentage")
    plt.show()
percentage_bar_chart()