import os
import sys
import requests

argv = 'python browser.py tb_tabs'
storage_dir = 'tb_tabs'
history = []
url = ''


class MyBrowser():

    def check_cache_dir(self, storage_dir):
        if not os.path.exists(storage_dir):
            print("Can't find cache dir...")
            os.mkdir(storage_dir)
            print("Cache dir is created.")

    def print_from_cache(self, file_path):
        if os.path.isfile(file_path):
            with open(file_path, "r") as file:
                print(file.read())
        else:
            print("No path in cache!")

    def check_url(self, addr):
        if self.menu(addr):
            return
        if "." not in addr:
            #  если адрес без точки, проверяем на наличие к кэше
            file_path = f'{storage_dir}\\' + addr
            #  если есть в кэше, выводим кэш
            if os.path.isfile(file_path):
                with open(file_path, "r") as file:
                    print(file.read())
                history.append(addr)
#                print(f"History is: {', '.join(history)}")
            else:
                print("Wrong URL: error in address and there is no in cache!")
                return False
        else:
            history.append(addr)
#            print(f"History is: {history}")
            return True

    def history_print(self):
        print(f"History is: {', '.join(history)}")

    def menu(self, addr):
        if addr == "exit":
            sys.exit()
            return True
        elif addr == "back":
            url = history.pop()
            self.print_from_cache(history.pop())
            return True
        elif addr == "history":
            self.history_print()
            return True


    def url_append(self, addr):
        if "http" not in addr:
            return "https://" + addr

    def url_request(self, addr, short_addr):
        try:
            url_answer = requests.get(addr).text
            short_addr = short_addr.split(".")[0]
            with open(f"{storage_dir}\\{short_addr}", "w") as file:
                file.write(url_answer)
            return url_answer
        except:
            print("Page or file is unreachable!")
            return


browser = MyBrowser()

while True:
    browser.check_cache_dir(storage_dir)
    url: str = input()
#    print(browser.check_url(url))

    if browser.check_url(url):
        url_full = browser.url_append(url)
        print(browser.url_request(url_full, url))
