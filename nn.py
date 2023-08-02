import random

def get_user_choice():
    print("Taş, kağıt, makas!")
    user_choice = input("Seçiminizi yapın (taş, kağıt, makas): ").lower()
    while user_choice not in ['taş', 'kağıt', 'makas']:
        print("Geçersiz seçim. Lütfen tekrar seçin.")
        user_choice = input("Seçiminizi yapın (taş, kağıt, makas): ").lower()
    return user_choice

def get_computer_choice():
    choices = ['taş', 'kağıt', 'makas']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Berabere!"
    elif (user_choice == 'taş' and computer_choice == 'makas') or \
         (user_choice == 'kağıt' and computer_choice == 'taş') or \
         (user_choice == 'makas' and computer_choice == 'kağıt'):
        return "Tebrikler, kazandınız!"
    else:
        return "Üzgünüm, kaybettiniz."

def play_again():
    play_again = input("Tekrar oynamak istiyor musunuz? (evet/hayır): ").lower()
    return play_again == 'evet'

def main():
    print("Taş-Kağıt-Makas oyununa hoş geldiniz!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Siz: {user_choice}, Bilgisayar: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

        if not play_again():
            break

    print("Oyunu oynamak için teşekkür ederiz. Tekrar bekleriz!")

if __name__ == "__main__":
    main()
