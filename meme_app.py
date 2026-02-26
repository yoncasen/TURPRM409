meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print("Kelimenin anlamı:", meme_dict[word])
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("Bu kelimeyi bilmiyorum!")
