
def buat_file(filename):
    with open(filename, mode="w") as f:
        f.write("Hello World! generated by buat_file.py")
        
buat_file("file.txt")
