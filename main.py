import requests
from colorama import Fore

print(Fore.RED + "             _                 _   _      ")
print(Fore.RED + "  __ _ _ __ | |_ __ _ _ __ ___| |_(_) ___ ")
print(Fore.RED + " / _` | '_ \| __/ _` | '__/ __| __| |/ __|")
print(Fore.RED + "| (_| | | | | || (_| | | | (__| |_| | (__ ")
print(Fore.RED + " \__,_|_| |_|\__\__,_|_|  \___|\__|_|\___|")

print("")
print(Fore.RESET + "          Webhook Flooder made by")
print("      https://github.com/Antarctic1337")
print("")


def send_discord_message(webhook_url, message, repeat_count):
  for _ in range(repeat_count):
    payload = {'content': message}
    try:
      response = requests.post(webhook_url, json=payload)
      response.raise_for_status()
      print(f"{Fore.RED}[+] Message '{message}' sent.")
    except requests.exceptions.RequestException as e:
      print(
        f"{Fore.YELLOW}[!] {Fore.RESET}Error sending '{message}': {Fore.RED}{e}"
      )


if __name__ == "__main__":
  webhook_url = input(
    f"{Fore.RED}[i] {Fore.RESET}Enter your target Webhook > ")
  message = input(f"{Fore.RED}[i] {Fore.RESET}Enter your message > ")
  repeat_count = int(
    input(f"{Fore.RED}[i] {Fore.RESET}Enter message count > "))

  send_discord_message(webhook_url, message, repeat_count)
