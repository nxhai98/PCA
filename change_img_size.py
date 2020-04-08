from PIL import Image



# def get_path(i, j):
#     path = "resourses/train/s" + str(i) + "/" + str(j) + ".pgm"
#     return path

def get_path(i, j):
    path = "resourses/train/s" + str(i) + "/" + str(j) + ".pgm"
    return path

def change_size():
    data = []
    path_arr = []
    num = 0
    for i in range(1, 15):
        for j in range(1, 10):
            try:
                path = get_path(i, j)
                print(path)
                img = Image.open(path)
                print(img.size)
                img = img.resize((64, 64))
                path_save = "train/" + str(num) + ".pgm"
                img.save(path_save)
                num = num + 1
            except:
                print()

    return data, path_arr

change_size()