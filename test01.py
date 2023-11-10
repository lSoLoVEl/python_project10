#Excrption Handling
#ข้อผิดพลาด การจัดการ
#Excrption ข้อผิดพลาดที่เกิขึ้นตอนโปรแกรมทำงาน


try:
 num1 = (input('ป้อนตัวเลข 1:'))
 num2 = (input('ป้อนตัวเลข 2:'))

 sum = num1 + num2
 result=num1/num2

 print(f'ผลรวมของ {num1}+ {num2}คือ {sum}')
 print(f'ผลรวมของ {num1}/ {num2}คือ {result}')
except ValueError:
  print('ป้อนตัวเลขเท่านั้นห้ามตัวอักษร.....สังสัยติดต่อ iT')
except ZeroDivisionError:   
  print('ป้อนตัวเลขตัวที่ 2 ห้ามเป็น 0.....สงสัยติดต่อ iT')
except Exception:
  print('มีข้อผิดพลาดเกิดขึ้น ต้องขอประทานอภัยอย่างสูง ช่วยติดต่อ iT ด้วย จะแก้ไขให้')

finally:
  print('wow')
  print('Hello...')
