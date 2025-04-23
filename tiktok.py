#tool russi
# @kurd_kuurd129
# TIKTOK 
import requests
import random
import string
import os

def send_telegram_message(idg, token, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": idg, "text": message}
    requests.post(url, data=data)

# فانکشنی دروستکردنی ئیمەیل بە شانس
def generate_random_email():
    domains = ["gmail.com"]
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(6, 10)))
    domain = random.choice(domains)
    return f"{username}@{domain}"

# فانکشنی چێککردنی زانیاری بەکارهێنەران لە تیکتۆک (بەش 1)
def check_tiktok_user_email(idg, token):
    print("Checking TikTok user emails...")
    hit = 0
    bad = 0

    while True:
        email = generate_random_email()
        username = email.split("@")[0]

        try:
            headers = {
                "user-agent": "Mozilla/5.0 (Linux; Android 10; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36"
            }
            response = requests.get(f"https://www.tiktok.com/@{username}", headers=headers)
            
            if response.status_code == 200:
                data = response.text
                name = data.split('"nickname":"')[1].split('"')[0]
                country = data.split('"region":"')[1].split('"')[0]
                followers = data.split('"followerCount":')[1].split(',')[0]
                likes = data.split('"heart":')[1].split(',')[0]
                
                hit += 1
                message = f"""
                
═══════════════════
𝐇𝐈𝐓 𝐀𝐂𝐶𝐎𝐔𝐍𝐓 𝐓𝐈𝐊𝐓𝐎𝐊
═══════════════════
𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴➟ : {username}
𝙶𝙼𝙰𝙸𝙻➟ : {email}
𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂➟ : {followers}
𝙻𝙸𝙺𝙴➟ : {likes}
𝙽𝙰𝙼𝙴➟ : {name}
══════════════════
                """
                print(message)
                send_telegram_message(idg, token, message)
            else:
                bad += 1
                print(f"Bad: {email}")
        
        except Exception as e:
            print(f"Error: {e}")

        print(f"Hit: {hit} | Bad: {bad}")
        os.system('sleep 1')
def main():
    os.system("clear")
    print("Enter your ID:")
    idg = input("> ")
    print("Enter your Token:")
    token = input("> ")

    while True:
        print("""
___________________
1 -  Check Emails
2 - TikTok Random Email Check
0 - Exit
___________________
        """)
        choice = input("Halbzhera dlm: ")

        if choice == "1":
            check_tiktok_user_email(idg, token)
        elif choice == "2":
            check_tiktok_user_email(idg, token)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()