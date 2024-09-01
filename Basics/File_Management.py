# # No need to Close File manually here, after we get out of this block it will close automatically

# with open('C:/Users/Sanket Kadam/OneDrive/Documents/Python/Sample.txt','r') as f:
#     # f_contents = f.readline()             # Will read first Line
#     f_contents = f.read()
#     # f_contents = f.read(100)              # Will read first 100 Characters
#     # print(f.tell())                       # Will return Current position in file
#     # f.seek(0)                             # Will Make Current Position 0
#     # for line in f:
#     #     print(line, end='')
#     print(f_contents , end='')
    
# with open('Sample2.txt','w') as f:
#     f.write('Sample File')

# with open('C:/Users/Sanket Kadam/OneDrive/Documents/Python/Sample.txt','r') as rf:
#     with open('C:/Users/Sanket Kadam/OneDrive/Documents/Python/Sample_Copy.txt','w') as wf:
#         for line in rf:
#             wf.write(line)


# How to Read,Write CSV files
import csv

# with open('C:/Users/Sanket Kadam/OneDrive/Documents/R/Developers.csv') as csv_file:
#     csv_reader = csv.reader(csv_file)
    
#     for line in csv_reader:
#         # print(line[2])              # will give us 2nd Column Only
#         print(line)
        
# with open('C:/Users/Sanket Kadam/OneDrive/Documents/R/Developers.csv') as csv_file:
#     csv_reader = csv.reader(csv_file)
    
#     with open('C:/Users/Sanket Kadam/OneDrive/Documents/R/Developers.csv') as new_file:
#         csv_writter = csv.writer(new_file, delimiter = '/t')
        
#         for line in csv_reader:
#             csv_writter.writerow(line)

# TRY EXCEPT

try:
    f = open('Samp.txt')
except FileNotFoundError as e:
    print(e)
except Exception:
    print('Sorry. Something went wrong')
else:
    print(f.open())
    f.close()
finally:
    print("This block will execute irrespective of occuring of Exceptions")
    
              