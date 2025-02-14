#My first output script!!!
file_path = "output_file.txt"
try:
    file = open(file_path, "w") # 'w' mode: write or create if there isn't a file
    file.write("This is hardcoded output. I'm going to try to use the output. \n")
    file.write("Of a function that I create")
    file.close()
except Exception as e:
    print(f"An error occurred: {e}")
