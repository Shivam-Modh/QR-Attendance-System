from MyQR import myqr
import os

f = open(r"C:\Users\manth\Downloads\QR_Attendance-main\QR_Attendance\students.txt")
lines = f.read().split("\n")
print(lines)

for _ in range(0, len(lines)):
    data = lines[_]
    version, level, qr = myqr.run(str(data), level='H', version=1,
                                  picture= r"C:\Users\manth\Downloads\QR_Attendance-main\QR_Attendance\Bl.png",
                                  colorized=True, contrast=1.0, brightness=1.0, save_name=str(lines[_] + '.png'),
                                  save_dir=os.getcwd()
                                  )
