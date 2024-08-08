from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
      if request.method == "POST":
        userInput = request.form["user_name"]
        # maybe add a system to log the conversions in future

        # making a key for basic quick conversion
        key = "2aa5aa3aa1aa6aa8aa7aa4"

        def main():
            #formating the key for use
            temp_key = key.split("aa")
            key = []
            for i in temp_key:
                key.append(int(i))
            user_input = text_to_binary(user_input)
            userInputList = userInput.split(" ")

        def text_to_binary(s):
            return ' '.join(format(ord(c), '08b') for c in s)
        def binary_to_text(s):
            return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

        def make_long(enc_text):
            if enc_text[0] == "-" and enc_text[1] == "-" and enc_text[2] == "9" and enc_text[len(enc_text)-3] == "9" and enc_text[len(enc_text)-2] == "-" and enc_text[len(enc_text)-1] == "-":
                enc_text_list = []
                for i  in enc_text:
                    enc_text_list.append(i)
                enc_text_list[0] = ""
                enc_text_list[1] = ""
                enc_text_list[2] = ""
                enc_text_list[len(enc_text)-3] = ""
                enc_text_list[len(enc_text)-2] = ""
                enc_text_list[len(enc_text)-1] = ""
                z_2 = enc_text_list
                indices_ab = [i for i, x in enumerate(enc_text_list) if x == "q"]
                for i in indices_ab:
                    try:
                        z_2[i] = "ab"
                    except:
                        pass
                indices_ac = [i for i, x in enumerate(enc_text_list) if x == "w"]
                for i in indices_ac:
                    try:
                        z_2[i] = "ac"
                    except:
                        pass
                indices_ad = [i for i, x in enumerate(enc_text_list) if x == "!"]
                for i in indices_ad:
                    try:
                        z_2[i] = "ad"
                    except:
                        pass
                indices_ba = [i for i, x in enumerate(enc_text_list) if x == "e"]
                for i in indices_ba:
                    try:
                        z_2[i] = "ba"
                    except:
                        pass 
                indices_bc = [i for i, x in enumerate(enc_text_list) if x == "r"]
                for i in indices_bc:
                    try:
                        z_2[i] = "bc"
                    except:
                        pass
                indices_bd = [i for i, x in enumerate(enc_text_list) if x == "g"]
                for i in indices_bd:
                    try:
                        z_2[i] = "bd"
                    except:
                        pass
                indices_ca = [i for i, x in enumerate(enc_text_list) if x == "t"]
                for i in indices_ca:
                    try:
                        z_2[i] = "ca"
                    except:
                        pass
                indices_cb = [i for i, x in enumerate(enc_text_list) if x == "%"]
                for i in indices_cb:
                    try:
                        z_2[i] = "cb"
                    except:
                        pass
                indices_cd = [i for i, x in enumerate(enc_text_list) if x == "&"]
                for i in indices_cd:
                    try:
                        z_2[i] = "cd"
                    except:
                        pass
                indices_aa = [i for i, x in enumerate(enc_text_list) if x == "@"]
                for i in indices_aa:
                    try:
                        z_2[i] = "aa"
                    except:
                        pass
                indices_bb = [i for i, x in enumerate(enc_text_list) if x == "#"]
                for i in indices_bb:
                    try:
                        z_2[i] = "bb"
                    except:
                        pass
                indices_cc = [i for i, x in enumerate(enc_text_list) if x == "o"]
                for i in indices_cc:
                    try:
                        z_2[i] = "cc"
                    except:
                        pass
                indices_dc = [i for i, x in enumerate(enc_text_list) if x == "j"]
                for i in indices_dc:
                    try:
                        z_2[i] = "dc"
                    except:
                        pass
                indices_db = [i for i, x in enumerate(enc_text_list) if x == "k"]
                for i in indices_db:
                    try:
                        z_2[i] = "db"
                    except:
                        pass
                indices_da = [i for i, x in enumerate(enc_text_list) if x == "l"]
                for i in indices_da:
                    try:
                        z_2[i] = "da"
                    except:
                        pass
                z_2_string = ""
                for i in z_2:
                    z_2_string += i
                z_2 = []
                for i in z_2_string:
                    z_2.append(i)
                z = z_2
                indices_10 = [i for i, x in enumerate(z_2) if x == "a"]
                for i in indices_10:
                    z[i] = "10"
                indices_01 = [i for i, x in enumerate(z_2) if x == "b"]
                for i in indices_01:
                    z[i] = "01"
                indices_11 = [i for i, x in enumerate(z_2) if x == "c"]
                for i in indices_11:
                    z[i] = "11" 
                indices_00 = [i for i, x in enumerate(z_2) if x == "d"]
                for i in indices_00:
                    z[i] = "00"
                z_string = ""
                for i in z:
                    z_string += i
                return z_string
            else:
                return False
            
        def decrypt(bin):
            c = 0
            temp = ""
            z = []
            for i in bin:
                c += 1
                if len(temp) == 8:
                    z.append(temp)
                    temp = ""
                    temp += str(i)
                else:
                    temp += str(i)
                    if len(temp) == 8:
                        z.append(temp)
                        temp = ""
            decrypted_text_in_binary_list = []
            for i in z:
                user_final = i
                for i in range(1,9):
                    y = key.index(i)
                    decrypted_text_in_binary_list.append(user_final[y])
            decrypted_text_in_binary = ""
            for i in decrypted_text_in_binary_list:
                decrypted_text_in_binary += i
            return binary_to_text(decrypted_text_in_binary)
        


if __name__ == "__main__":
    app.run()

