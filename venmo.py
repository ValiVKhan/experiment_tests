from venmo_api import Client

# inputusername = input("What is your username: ")
# inputpassword = input("What is your password: ")

# Get your access token. You will need to complete the 2FA process
# access_token = Client.get_access_token(username=inputusername,
#                                        password=inputpassword)

venmo = Client(access_token=)

paymentmethods =[]
p_methods = venmo.payment.get_payment_methods()
for p_method in p_methods:
    paymentmethods.append(str(p_method))
    # print(p_method)


# test_str=str(store.readlines())
test_str = (''.join(paymentmethods))

# print(test_str)
namesub = "name"
namesearch = [i for i in range(len(test_str)) if test_str.startswith(namesub, i)] 
namecard = []

idsub = "id"
idsearch = [i for i in range(len(test_str)) if test_str.startswith(idsub, i)] 
idcard = []

for namegapahead in namesearch:
    namegap = namegapahead
    while test_str[namegapahead] != ",":
        namegapahead+=1
    namecard.append(test_str[namegap+5:(namegapahead)])

for idgapahead in idsearch:
    idgap = idgapahead
    while test_str[idgapahead] != ",":
        idgapahead+=1
    idcard.append(test_str[(idgap+3):(idgapahead)])

joiningvar = 0
for names in namecard:
    print(str(joiningvar+1)+". "+namecard[joiningvar])
    joiningvar+=1

def askcredit():
    global creditchosen
    creditchosen = input("Which number credit car would you like to use? ")
askcredit()

while 1:
    if int(creditchosen) > joiningvar:
        askcredit()
    else:
        break

# print(namecard)
print(namecard[int(creditchosen)-1])

towho = input("To who would you like to send the money to? @")

user = venmo.user.get_user_by_username(username=towho)
itsto = (user.id)


much = int(input("How much money would you like to send? Integer values ONLY."+str(towho)))

note = input("Add a note: ")

print(idcard[int(creditchosen)-1])
venmo.payment.send_money(much, note, str(itsto), (idcard[int(creditchosen)-1]))

print("Payed "+str(towho)+" $"+str(much))
