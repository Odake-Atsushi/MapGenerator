from pdf2image import convert_from_path
# from numpy import np
import tempfile

f = tempfile.TemporaryFile(suffix='.png')
# d = tempfile.TemporaryDirectory()

images = convert_from_path(
    'C:\\Users\\Atsushi\\Downloads\\a\\学生ロボコン2022フィールド図面-01.pdf', 600)
# print(np.array(images[0])
images[0].save('C:\\Users\\Atsushi\\Documents\\MapGenerator\\test.png', 'png')
# print(f.name)
# images[0].save(f, 'png')
# f.close()
# print(d.name)
