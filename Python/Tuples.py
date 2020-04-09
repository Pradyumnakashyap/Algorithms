#Input the number of students, for each student enter 3 marks, then input student
#name to get average of his/her score


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print('{0:.2f}'.format(sum(student_marks[query_name])/len(student_marks[query_name]),1))
    