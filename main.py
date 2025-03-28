# upi id -> qr code
import qrcode

#taking upi id as input
upi_id = input("Enter your UPI ID = ")

#upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE

# defining the payment URL based on the UPI ID and the payment app
phonepe_url = f'upi://pay?pa={upi_id}&pn=recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=recipient%20Name&mc=1234'

# creating QR codes for each payment app.
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)


# if you feel like saving the QRcode as an image file in your device. 
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# to display the qr codes
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

