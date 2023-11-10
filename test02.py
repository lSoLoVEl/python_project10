#file Handling
#ไฟล์ การจัดการ
#คือ การทำงานกับไฟล์
#การเปิดไฟล์ write (w)/extend (x)/append(a)/read(r)
#1.write(w) เปิดเพื่อเขียน 2.append(a)เปิดเขียนต่อ 3.read(r)เปิดเพื่ออ่าน

f_iot = open('iot3.txt','w',encoding='utf-8')

f_iot.write('Wow..')
f_iot.write('Hi..')
f_iot.write('สวัสดี..')

f_iot.close()