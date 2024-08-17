import qrcode

# 创建一个二维码实例
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# 添加数据
qr.add_data('https://simpfun.cn')
qr.make(fit=True)

# 生成二维码图像
img = qr.make_image(fill_color="black", back_color="white")

# 保存二维码图像
img.save('/mnt/data/simpfun_qrcode.png')

'/mnt/data/simpfun_qrcode.png'
