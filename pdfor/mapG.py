import re
import itertools
import PySimpleGUI as sg
from pdf2image import convert_from_path
import tempfile
from PIL import Image, ImageFilter
import numpy as np


def generate_map(InputFilePath, reSize, r, g, b):
    output_img = None
    if InputFilePath.rfind('.pdf') >= 0:  #PDFファイル
        f_buf = tempfile.NamedTemporaryFile(suffix='.png')
        images = convert_from_path(str(InputFilePath), 300)
        images[0].save(f_buf, 'png')
        input_img = np.array(Image.open(f_buf))
        output_img = image_extract(input_img, r, g, b)
    else:  #画像ファイル
        input_img = np.array(Image.open(str(InputFilePath)))
        output_img = image_extract(input_img, r, g, b)
    image_output = Image.fromarray(output_img, 'L')
    FilI = ((((image_output.filter(ImageFilter.MinFilter())).filter(
        ImageFilter.MinFilter())).filter(ImageFilter.MinFilter())).filter(
            ImageFilter.MinFilter())).filter(ImageFilter.MinFilter())
    ReI = FilI.resize((int(FilI.width * float(reSize) / 100),
                       int(FilI.height * float(reSize) / 100)), Image.LANCZOS)
    return ReI


def image_extract(img, r, g, b):
    img_size = list(img.shape)
    output_img = np.zeros((img_size[0], img_size[1]), np.int8)
    RGB_c = np.array([int(r), int(g), int(b)])
    count_c = [0, 0]
    if len(img_size) == 3:  #カラー画像
        for x, y in itertools.product(range(int(img_size[0])),
                                      range(int(img_size[1]))):
            if all(img[x, y] == RGB_c):
                output_img[x, y] = 0  #Black
                count_c[0] += 1
            else:
                output_img[x, y] = 255  #White
                count_c[1] += 1
    else:
        error_window('モノクロ画像が入っています．\n対応していません．')
    return output_img


def error_window(msg):
    error_layout = [[sg.Text(msg, key='error')],
                    [sg.Button('OK', key='ok', expand_x=True)]]
    sub_window = sg.Window('エラー',
                           error_layout,
                           modal=True,
                           keep_on_top=True,
                           auto_size_text=True)
    while True:
        sub_event, sub_value = sub_window.read()
        sub_window['error'].update(msg)
        if sub_event == sg.WIN_CLOSED:  #ウィンドウのXボタンを押したときの処理
            break
        if sub_event == 'ok':
            break
    sub_window.close()


sg.theme('Default')

main_layout = [
    [sg.Text('対象ファイルと出力先を指定してください．')],
    [sg.Text('ファイル(画像ファイル or PDF)')],
    [
        sg.InputText('', key='inputFilePath'),
        sg.FileBrowse(
            'ファイルを選択',
            target='inputFilePath',
            #file_types=(('テキストファイル'), )
        )
    ],
    [sg.Text('抽出する色（初期値：NHKロボコン図面）')],
    [
        sg.Text('R'),
        sg.InputText('218', size=(5, 1), key='color_r'),
        sg.Text('G'),
        sg.InputText('175', size=(5, 1), key='color_g'),
        sg.Text('B'),
        sg.InputText('134', size=(5, 1), key='color_b')
    ],
    [
        sg.Text('画像全体のスケール[m]'),
        sg.Combo(('縦', '横'), size=(4, 1), default_value='縦', key='WorH'),
        sg.InputText('1', size=(5, 1), key='size')
    ],
    [sg.Text('画像リサイズ[%]'),
     sg.InputText('100', size=(5, 1), key='img_size')],
    [sg.Text('画像左下の位置[m]')],
    [
        sg.Text('x'),
        sg.InputText('0.0', size=(5, 1), key='pos_x'),
        sg.Text('y'),
        sg.InputText('0.0', size=(5, 1), key='pos_y'),
        sg.Text('θ'),
        sg.InputText('0.0', size=(5, 1), key='pos_th')
    ],
    [sg.Button('実行', key='go', expand_x=True)]
]

main_window = sg.Window('Map生成',
                        main_layout,
                        resizable=True,
                        auto_size_buttons=True,
                        auto_size_text=True,
                        finalize=True)

main_window.set_min_size((470, 250))

while True:
    event, values = main_window.read()

    if event == sg.WIN_CLOSED:  #ウィンドウのXボタンを押したときの処理
        break

    if event == 'go':
        if not values['inputFilePath']:
            error_window('ファイル(画像ファイル or PDF)が選択されていません．')
        else:
            # PGM
            output_img = generate_map(values['inputFilePath'],
                                      values['img_size'], values['color_r'],
                                      values['color_g'], values['color_b'])
            value = sg.popup_get_file("Save Image File \'*.pgm\'.",
                                      save_as=True,
                                      file_types=(("ROS map Image File",
                                                   ".pgm"), ))
            output_img.save(str(value))
            # YAML
            value = sg.popup_get_file("Save YAML File \'*.yaml\'.",
                                      save_as=True,
                                      file_types=(("ROS map YAML File",
                                                   ".yaml"), ))
            f = open(str(value), 'w')
            f.write('image: ' + str(value) + '\n')
            resolution_rate = 0
            if values['WorH'] == '縦':
                resolution_rate = float(values['size']) / int(
                    output_img.height)
            else:
                resolution_rate = float(values['size']) / int(output_img.width)
            f.write('resolution: ' + str(resolution_rate) + '\n')
            f.write('origin: [' + str(values['pos_x']) + ', ' +
                    str(values['pos_y']) + ', ' + str(values['pos_th']) +
                    ']\n')
            f.write('occupied_thresh: 0.65\n')
            f.write('free_thresh: 0.196\n')
            f.write('negate: 0\n')
            f.close()
            break

main_window.close()