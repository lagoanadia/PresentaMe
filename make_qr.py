"""Genera el QR. Uso: python3 make_qr.py https://tu-url.vercel.app"""
import sys, qrcode, qrcode.image.svg
url = sys.argv[1] if len(sys.argv) > 1 else "https://presentame-nadia.vercel.app"
def build(): q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=24, border=4); q.add_data(url); q.make(fit=True); return q
build().make_image(fill_color="#171615", back_color="white").save("qr.png")
build().make_image(image_factory=qrcode.image.svg.SvgPathImage).save("qr.svg")
print("QR ->", url)
