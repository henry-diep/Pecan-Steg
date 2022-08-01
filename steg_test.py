from stegano import lsb
secret = lsb.hide("./watching.png", ".. .----. -- / .-- .- - -.-. .... .. -. --. / -.-- --- ..-")
secret.save("./watching_secret.png")
clear_message = lsb.reveal("./watching_secret.png")
print(clear_message)