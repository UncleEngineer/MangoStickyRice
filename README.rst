(Uncle Profile) เป็นตัวอย่างการอัพโหลด package ไปยัง pypi.org
=============================================================

PyPi: https://pypi.org/project/khawniawmamuang/

สวัสดีจ้าาาา แพ็คนี้คือแพ็คเกจที่อธิบายวิธีการทำข้าวเหนียวมะม่วง (Mango
Sticky Rice) มีฟังชั่นโชว์วิธีการทำ ส่วนประกอบต่างๆ

วิธีติดตั้ง
~~~~~~~~~~~

เปิด CMD / Terminal

.. code:: python

   pip install khawniawmamuang

วิธีใช้งานแพ็คเพจนี้
~~~~~~~~~~~~~~~~~~~~

-  เปิด IDLE ขึ้นมาแล้วพิมพ์…

.. code:: python

   from khawniawmamuang import MangoStickyRice

   mango = MangoStickyRice()
   mango.what_is_it() #ข้าวเหนียวมะม่วงคืออะไร?
   mango.show_ingredients() #มีส่วนผสมอะไรบ้าง?
   mango.show_how_to(eng=True) #วิธีการทำ
   mango.show_youtube() #โชว์คลิปทำ
   mango.show_google() #โชว์เทรนด์ google
   mango.show_location() #โชว์ตำแหน่งร้าน
   mango.show_image(open=True) #โชว์ภาพ

พัฒนาโดย: ลุงวิศวกร สอนคำนวณ FB: https://www.facebook.com/UncleEngineer

YouTube: https://www.youtube.com/UncleEngineer
