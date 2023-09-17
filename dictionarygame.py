import random
import time


words={
    "Hi":"Merhaba",
    "Bye":"Hoşça kalın",
    "Task":"Görev",
    "Program":"Program"
}

while True:
    mode = input("Bir mod seçin: Yeni kelimeler eklemek için 0, çeviri yapmak için 1,çıkmak için e: \n")
    match mode:
        case "0":
            word = input("İngilizce bir kelime yazın: ")
            translate = input("Kelimenin tercümesini yazın: ")
            if len(word) > 0 and len(translate) > 0:
                words[word]=translate
                print("Kelime başarıyla eklendi!")  
        case "1":
            score = 0
            t = time.time()
            print("Çevirebildiğiniz kadar kelime çevirin! 10 hakkınız var!")
            for i in range(10):
                word = random.choice(list(words.keys()))
                print("Tercümesi bu şekilde olmalı: " + word)
                if input() == words[word]:
                    print("Harika!!!")
                    score += 1
                else:
                    print("Bir yanlışlık var... Doğru kelime - " + words[word])
            t = time.time()-t
            print("Puanınız: " + str(score) +"\nBitirme süreniz: "+ str(int(1000*t)/1000)+ " saniye")
            
        case "e":
            break
        case _:
            print("Geçersiz giriş")
    