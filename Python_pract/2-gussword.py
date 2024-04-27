secret_word = "codezilla"
guss = ""
guss_count = 0
guss_limit = 3
out_of_gusses = False

while guss.lower() != secret_word and not out_of_gusses:
    if guss_count <= guss_limit:
        guss = input("Enter guss: ")
        guss_count += 1
    else:
        out_of_gusses = True
print("you win")
