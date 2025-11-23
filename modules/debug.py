import sys, os

print("=== DEBUG INFO ===")
print("Current Working Directory:", os.getcwd())
print("\nPython Path:")
for p in sys.path:
    print("  ", p)

print("\nDirectory Contents (cwd):")
print(os.listdir(os.getcwd()))

print("\nDirectory Contents (PythonLearning):")
try:
    print(os.listdir("/Users/mostafasrour/Desktop/Courses/Python/PythonLearning"))
except Exception as e:
    print("Error:", e)

print("\nDirectory Contents (ecommerce):")
try:
    print(os.listdir("/Users/mostafasrour/Desktop/Courses/Python/PythonLearning/ecommerce"))
except Exception as e:
    print("Error:", e)

print("\nIf this prints, your script ran correctly.")