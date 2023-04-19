import base64
from io import BytesIO

import ddddocr
from PIL import Image
from selene import Element, query


def recognize_img_text(img_bytes: bytes, recognize_area=None) -> str:
    with Image.open(BytesIO(img_bytes)) as img:
        recognize_part = img.crop(recognize_area) if recognize_area else img
        ocr = ddddocr.DdddOcr(show_ad=False)
        return ocr.classification(recognize_part) or None


def pic_compare(element: Element, pic_path: str):
    js = 'var canvas = self;' \
         'return canvas.toDataURL("image/png");'
    img_data = element.execute_script(js)
    img_base64 = img_data.split(',')[1]
    img_bytes = base64.b64decode(img_base64)

    def calculate_pixel(image):
        image_his = image.histogram()
        sum_pixel = 0
        for i in range(0, len(image_his)):
            sum_pixel += image_his[i]
        return sum_pixel

    with Image.open(BytesIO(img_bytes)) as img:
        img_1_pixel_sum = calculate_pixel(img)

    with Image.open(pic_path) as img:
        img_2_pixel_sum = calculate_pixel(img)

    return 1 - (abs(img_1_pixel_sum - img_2_pixel_sum) / max(img_1_pixel_sum, img_2_pixel_sum))


def get_canvas_bytes(element: Element):
    js = 'var canvas = self;' \
         'var context = canvas.getContext("2d");' \
         'context.globalCompositeOperation="destination-over";' \
         'context.fillStyle="white";' \
         'context.fillRect(0,0,canvas.width,canvas.height);' \
         'context.globalCompositeOperation="source-over";' \
         'return canvas.toDataURL("image/png");'
    img_data = element.execute_script(js)
    img_base64 = img_data.split(',')[1]
    img_bytes = base64.b64decode(img_base64)
    return img_bytes


def recognize_img_text_with_area(
        element: Element,
        w1: float = 0,
        w2: float = 1,
        h1: float = 0,
        h2: float = 1
):
    width_str = element.get(query.attribute('width'))
    height_str = element.get(query.attribute('height'))
    if width_str.isdigit() and height_str.isdigit():
        width, height = eval(width_str), eval(height_str)
        recognize_area = (
            w1 * width,
            h1 * height,
            w2 * width,
            h2 * height
        )
        img_bytes = get_canvas_bytes(element)
        text = recognize_img_text(img_bytes, recognize_area)
        return text
    else:
        return None
