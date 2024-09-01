# List comprehension

# numbers = [1, 2, 3]
# new_numbers = [num + 1 for num in numbers]
# print(new_numbers)

# name = "Muhammad"
# letter_list = [letter for letter in name]
# print(letter_list)

# range_list = [n * 2 for n in range(1, 5)]
# print(range_list)

# names = ["alex", "bath", "caroline", "dave", "eleanor", "freddie"]
# long_names = [name.upper() for name in names if len(name) > 4]
# print(long_names)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num**2 for num in numbers]
# print(squared_numbers)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)

# with open("file1.txt") as file1:
#     file_1_data = file1.readlines()
#
# with open("file2.txt") as file2:
#     file_2_data = file2.readlines()
#
# result = [int(num) for num in file_1_data if num in file_2_data]
#
# print(result)

# import random
# names = ["Alex", "Beth", "William", "James", "John", "Dave", "Caroline", "Valentina", "Syel"]
# students_score = {student: random.randint(1, 100) for student in names}
# passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
# print(students_score)
# print(passed_students)

# sentence = ("In a rapidly changing world, technology evolves quickly, demanding people adapt, learn, innovate, "
#             "and grow to meet new challenges and opportunities.")
# result = {word: len(word) for word in sentence.split()}
# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }
# weather_f = {day: (temp*9/5)+32 for (day, temp) in weather_c.items()}
# print(weather_f)

# import pandas
# student_dic = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 54, 93]
# }
#
# student_data_Frame = pandas.DataFrame(student_dic)
# for (index, row) in student_data_Frame.iterrows():
#     if row.student == "Angela":
#         print(row.score)

# import pandas
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# data_dic = {row.letter: row.code for (index, row) in data.iterrows()}
#
# word = input("Enter your name: ").upper()
# formated_word = [data_dic[key] for key in word if key in data_dic]
# print(formated_word)
