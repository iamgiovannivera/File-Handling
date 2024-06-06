# 1. Exploring Python's OS Module



# import os

# def list_directory_contents(path):
#     try:
#         contents = os.listdir(path)
#         print(f"Contents of '{path}':")
#         for item in contents:
#             print(item)
#     except FileNotFoundError:
#         print("The specified directory does not exist.")
#     except PermissionError:
#         print("You do not have permission to access this directory.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# path = input("Enter the directory path: ")
# list_directory_contents(path)



# Task 2: File Size Reporter



# import os

# def report_file_sizes(directory):
#     try:
#         with os.scandir(directory) as entries:
#             for entry in entries:
#                 if entry.is_file():
#                     print(f"{entry.name}: {entry.stat().st_size} bytes")
#     except FileNotFoundError:
#         print("The specified directory does not exist.")
#     except PermissionError:
#         print("You do not have permission to access this directory.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# directory = input("Enter the directory path: ")
# report_file_sizes(directory)



# Task 3: File Extension Counter



# import os

# def count_file_extensions(directory):
#     extension_count = {}
#     try:
#         with os.scandir(directory) as entries:
#             for entry in entries:
#                 if entry.is_file():
#                     ext = os.path.splitext(entry.name)[1].lower()
#                     if ext in extension_count:
#                         extension_count[ext] += 1
#                     else:
#                         extension_count[ext] = 1
#         for ext, count in extension_count.items():
#             print(f"{ext.upper()}: {count}")
#     except FileNotFoundError:
#         print("The specified directory does not exist.")
#     except PermissionError:
#         print("You do not have permission to access this directory.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# directory = input("Enter the directory path: ")
# count_file_extensions(directory)


# 2. Regex-Powered Text Data Processing



# import re

# def extract_emails(filename):
#     try:
#         with open(filename, 'r') as file:
#             text = file.read()
#         emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
#         unique_emails = set(emails)
#         print("Extracted emails:")
#         for email in unique_emails:
#             print(email)
#     except FileNotFoundError:
#         print("The specified file does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# filename = 'contacts.txt'
# extract_emails(filename)
# 3. Advanced Python Data Processing 

# import re

# def analyze_blog_sentiments(blog_file):
#     positive_words = {"amazing", "enjoy", "beautiful", "wonderful", "breathtaking", "memorable", "excellent", "fantastic", "unique"}
#     negative_words = {"bad", "disappointing", "poor", "lackluster", "overcrowded", "scarce"}
    
#     positive_count = 0
#     negative_count = 0
    
#     try:
#         with open(blog_file, 'r') as file:
#             text = file.read()
        
#         for word in re.findall(r'\b\w+\b', text.lower()):
#             if word in positive_words:
#                 positive_count += 1
#             elif word in negative_words:
#                 negative_count += 1
                
#         print(f"Positive words count: {positive_count}")
#         print(f"Negative words count: {negative_count}")
        
#     except FileNotFoundError:
#         print("The specified file does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# blog_file = 'travel_blogs.txt'
# analyze_blog_sentiments(blog_file)




# Task 2: Historical Weather Data Compiler




# import os
# import re

# def calculate_average_temperature(filename):
#     total_temp = 0
#     count = 0
#     try:
#         with open(filename, 'r') as file:
#             for line in file:
#                 match = re.search(r'-?\d+°C', line)
#                 if match:
#                     temp = int(match.group().strip('°C'))
#                     total_temp += temp
#                     count += 1
#         return total_temp / count if count != 0 else 0
#     except FileNotFoundError:
#         print(f"The file {filename} does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return 0

# def compile_weather_data(directory):
#     average_temperatures = {}
#     try:
#         with os.scandir(directory) as entries:
#             for entry in entries:
#                 if entry.is_file() and entry.name.startswith('weather_') and entry.name.endswith('.txt'):
#                     year = entry.name.split('_')[1].split('.')[0]
#                     avg_temp = calculate_average_temperature(entry.path)
#                     average_temperatures[year] = avg_temp
        
#         highest_avg_temp_year = max(average_temperatures, key=average_temperatures.get)
#         print("Average temperatures per year:")
#         for year, avg_temp in average_temperatures.items():
#             print(f"{year}: {avg_temp:.2f}°C")
#         print(f"Year with highest average temperature: {highest_avg_temp_year}")
        
#     except FileNotFoundError:
#         print("The specified directory does not exist.")
#     except PermissionError:
#         print("You do not have permission to access this directory.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# directory = input("Enter the directory containing weather data files: ")
# compile_weather_data(directory)