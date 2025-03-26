import qrcode
from PIL import Image

def generate_qr_code(link, color_scheme='black', transparent=False, filename='qrcode.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(link)
    qr.make(fit=True)

    if color_scheme == 'white':
        fill_color = 'white'
        back_color = 'black'
    else:
        fill_color = 'black'
        back_color = 'white'

    qr_img = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGBA')

    if transparent:
        datas = qr_img.getdata()
        new_data = []

        for item in datas:
            # Replace background color with transparency
            if color_scheme == 'white' and item[:3] == (0, 0, 0):  # black background
                new_data.append((0, 0, 0, 0))
            elif color_scheme == 'black' and item[:3] == (255, 255, 255):  # white background
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)

        qr_img.putdata(new_data)

    qr_img.save(filename)
    qr_img.show()


# Example usage:
# generate_qr_code("https://www.linkedin.com/company/vanderbilt-vector-lab/", color_scheme='white', transparent=True, filename='vector_lab_qr.png')
