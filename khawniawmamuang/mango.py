import webbrowser

class MangoStickyRice:
    """
    # ข้าวเหนียวมะม่วงคืออะไร?
    # เปิดวิธีการทำข้าวเหนียวมะม่วง
    # โชว์ส่วนผสมข้าวเหนียวมะม่วง
    # โชว์วิธีการทำ
    # โชว์ search google
    # ร้านข้าวเหนียวมะม่วง
    # โชว์รูปภาพ

    Example:

    mango = MangoStickyRice()
    mango.what_is_it()
    mango.show_ingredients()
    mango.show_how_to(eng=True)
    mango.show_youtube(open=True)
    mango.show_google()
    mango.show_location()
    mango.show_image(open=True)
    """
    def __init__(self):
        self.youtubeurl = 'https://www.youtube.com/watch?v=t5hfE9uzo_o' #วิธีการทำ
        self.youtubeurl_eng = 'https://www.youtube.com/watch?v=M7_WdFhI7Hk'

    def what_is_it(self):
        '''
        # ข้าวเหนียวมะม่วงคืออะไร?
        '''
        text = '''
        ข้าวเหนียวมะม่วง เป็นขนมหวานไทยยอดนิยม และจะได้รับความนิยมมากเป็นพิเศษในฤดูร้อน 
        ทำจากข้าวเหนียว เช่น ข้าวเหนียวเขี้ยวงู มูนกับหัวกะทิ เกลือป่น และน้ำตาลทรายขาว 
        แล้วกินกับเนื้อมะม่วงสุก ที่นิยมคือ มะม่วงอกร่อง และมะม่วงน้ำดอกไม้ อาจราดกะทิ 
        และโรยถั่วบางชนิด แล้วแต่ชอบใจ

        ข้าวเหนียวมะม่วงมีแคลอรีสูง ถ้ากินขณะเป็นโรคกระเพาะอาหาร, ม้ามพร่อง 
        หรือระบบย่อยอาหารบกพร่อง จะท้องอืด, จุกเสียดแน่น และอาหารย่อยยากมากขึ้นได้ 
        นอกจากนี้ หากรับประทานเกินพอดี จะร้อนใน, เจ็บคอ, ท้องผูก, ปวดหัว เป็นต้น 
        เอาได้ อย่างไรก็ดี ข้าวเหนียวในขนมหวานชนิดนี้มีสรรพคุณเป็นของร้อนรสหวาน 
        จะช่วยบำรุงพลัง ตลอดจนบำบัดอาการเหงื่อออกมาก และท้องเสีย โดยเฉพาะมะม่วง
        ที่มีรสหวานปนเปรี้ยวนั้น ช่วยบำรุงร่างกาย, แก้ไอ และขับลมได้

        ref: https://th.wikipedia.org/wiki/ข้าวเหนียวมะม่วง
        '''
        print(text)

    def show_ingredients(self,eng=False):
        '''
        # โชว์ส่วนผสมข้าวเหนียวมะม่วง
        .show_ingredients(eng=True) # for English
        '''
        text = '''
        -ข้าวเหนียว 350 กรัม
        -กะทิ 1 กระป๋อง
        -น้ำตาลทราย 3/4 ถ้วย
        -เกลือ 1+1/4 ช้อนชา
        -แป้งข้าวเจ้า 1 ช้อนชา
        -ใบเตย 4-5 ใบ
        '''
        text_eng = '''
        1½ cups uncooked short-grain white rice
        2 cups water
        1½ cups coconut milk
        1 cup white sugar
        ½ teaspoon salt
        ½ cup coconut milk
        1 tablespoon white sugar
        ¼ teaspoon salt
        1 tablespoon tapioca starch
        3 mangos, peeled and sliced
        1 tablespoon toasted sesame seeds
        '''
        if eng == True:
            print(text_eng)
        else:
            print(text)
    
    def show_how_to(self,eng=False):
        '''
        # เปิดวิธีการทำข้าวเหนียวมะม่วง
        '''
        text = '''
        <<วิธีทำ ข้าวเหนียวมูน ข้าวเหนียวมะม่วง>>
 
        1. ล้างข้าวเหนียวให้สะอาดแล้วแช่น้ำทิ้งไว้ข้ามคืน
        2. เติมน้ำลงในซึ้งนึ่ง นำขึ้นตั้งไฟค่อนข้างแรง รอจนน้ำเดือด จากนั้นสะเด็ดน้ำข้าวเหนียวขึ้นมาห่อผ้าขาวบาง วางใบเตยลงไปประมาณ 2 ใบ แล้วนำไปนึ่ง
        3. นึ่งประมาณ 30 นาทีจนข้าวเหนียวสุก
        4. นำกะทิมาแบ่งไว้ ¾ ถ้วย สำหรับกะทิส่วนที่เหลือให้นำไปใส่หม้อเล็กๆ เติมน้ำตาลและเกลือ 1 ช้อนชาลงไป จากนั้นนำไปตั้งบนไฟอ่อน
        5. ใส่ใบเตยที่เหลือลงในหม้อกะทิ ใช้ทัพพีคนเรื่อยๆ จนน้ำตาลละลาย อย่าให้กะทิเป็นก้อน รอจนกะทิเดือดจึงปิดเตาและยกลงพักไว้
        6. ตักข้าวเหนียวที่สุกแล้วใส่ลงในอ่างผสม เทกะทิร้อนๆ ใส่ลงไป คนเร็วๆ ให้ทั่วแล้วปิดฝาให้ข้าวเหนียวระอุอีกประมาณ 15 นาที
        7. นำกะทิ 3/4 ถ้วยที่แบ่งไว้มาผสมกับแป้งข้าวเจ้าและเกลือ นำไปตั้งไฟแล้วคนเรื่อยๆ จนกะทิข้นและเดือด เพื่อใช้เป็นกะทิสำหรับราดหน้า
        8. ตักข้าวเหนียวใส่จาน ราดด้วยน้ำกะทิที่เตรียมไว้ เสิร์ฟพร้อมมะม่วงสุก

        <<วิธีเลือกมะม่วงสุก สำหรับข้าวเหนียวมะม่วง>>

        -มะม่วงสุกที่นิยมนำมาทานกับข้าวเหนียวมะม่วงคือ มะม่วงอกร่องและมะม่วงน้ำดอกไม้ ซึ่งมีรสหวานหอม
        -ควรเลือกมะม่วงสุกที่ผลอวบและเปลือกมีรอยดำบ้างเล็กน้อย เพราะจะแน่ใจได้ว่ามะม่วงสุกจริงหรือสุกเองตามธรรมชาติ
        -ลองใช้นิ้วกดเบาๆ หากเนื้อมะม่วงยุบลงไปเล็กน้อยแปลว่าสุกได้ที่แล้ว แต่หากยังไม่ยุบแสดงว่าเป็นมะม่วงที่โดนบ่มแก๊สให้ผิวเหลืองแต่เนื้อข้างในไม่สุกอาจจะแข็งหรือมีรสเปรี้ยว

        ref: https://food.trueid.net/detail/raBaYlAVlZo
        '''
        text_eng = '''
        <step 1>

        Combine the rice and water in a saucepan; bring to a boil; cover and reduce heat to low. Simmer until water is absorbed, 15 to 20 minutes.

        <step 2>

        While the rice cooks, mix together 1 1/2 cups coconut milk, 1 cup sugar, and 1/2 teaspoon salt in a saucepan over medium heat; bring to a boil; remove from heat and set aside. Stir the cooked rice into the coconut milk mixture; cover. Allow to cool for 1 hour.

        <step 3>

        Make a sauce by mixing together 1/2 cup coconut milk, 1 tablespoon sugar, 1/4 teaspoon salt, and the tapioca starch in a saucepan; bring to a boil.

        <step 4>

        Place the sticky rice on a serving dish. Arrange the mangos on top of the rice. Pour the sauce over the mangos and rice. Sprinkle with sesame seeds.
        
        ref: https://www.allrecipes.com/recipe/150313/thai-sweet-sticky-rice-with-mango-khao-neeo-mamuang/
        '''

        if eng == True:
            print(text_eng)
        else:
            print(text)

    def show_youtube(self,eng=False,open=False):
        '''
        # โชว์วิธีการทำ
        '''
        if eng == True:
            print(self.youtubeurl_eng)
            if open == True:
                webbrowser.open(self.youtubeurl_eng)
        else:
            print(self.youtubeurl)
            if open == True:
                webbrowser.open(self.youtubeurl)

    def show_google(self,eng=False,open=False):
        '''
        # โชว์ search google
        '''
        if eng == True:
            url = 'https://www.google.com/search?q=mango+sticky+rice'
            print(url)
            if open == True:
                webbrowser.open(url)
        else:
            url = 'https://www.google.com/search?q=ข้าวเหนียวมะม่วง'
            print(url)
            if open == True:
                webbrowser.open(url)

    def show_location(self,location='สยาม',eng=False,open=False):
        '''
        # ร้านข้าวเหนียวมะม่วง
        '''
        if eng == True:
            url = 'https://www.google.com/search?q=mango+sticky+rice+bangkok'
            print(url)
            if open == True:
                webbrowser.open(url)
        else:
            url = 'https://www.google.com/search?q=ร้านข้าวเหนียวมะม่วง'
            print(url)
            if open == True:
                webbrowser.open(url)

    def show_image(self,open=False):
        '''
        # โชว์รูปภาพ
        '''
        if open == True:
            webbrowser.open('https://www.matichon.co.th/wp-content/uploads/2020/04/ข้าวเหนียวมะม่วง-4.jpg')
        else:
            print('https://www.matichon.co.th/wp-content/uploads/2020/04/ข้าวเหนียวมะม่วง-4.jpg')
    
    def show_ascii(self):
        text='''
                                ████  ████                                      
                        ██░░░░██░░░░████████                              
                        ██░░░░░░░░██▒▒▒▒▒▒  ██                            
                        ██░░░░██▒▒▒▒  ▒▒▒▒▒▒██                          
                        ██░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒██                        
                    ██░░░░██░░░░██▒▒▒▒▒▒▒▒▒▒▒▒██                        
                        ████▒▒████▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒██                      
                        ██  ▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒  ██                      
                        ██▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                      
                        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒██                      
                        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                      
                            ██  ▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒██                        
                            ████▒▒▒▒▒▒▒▒  ▒▒██                          
                                ████████████      
        '''
        print(text)


if __name__ == '__main__':
    mango = MangoStickyRice()
    mango.what_is_it()
    mango.show_ingredients()
    mango.show_how_to(eng=True)
    mango.show_youtube()
    mango.show_google()
    mango.show_location()
    mango.show_image(open=True)
    mango.show_ascii()

