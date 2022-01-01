#youtube download using python3
#
import os
import pafy
from colorama import Fore, Back, Style
def main():
    hijau = Fore.GREEN
    merah = Fore.RED
    cyan = Fore.CYAN
    tai = Fore.YELLOW
    biru = Fore.BLUE
    batas = Style.RESET_ALL
    
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])
    banner = '        X×× Y T D o n w l o a d e r××X'
    by = '        By : Koleksibot'
    git = '        Github : github.com/koleksibot'
    print(f'{cyan}{banner}')
    print(f'{cyan}{by}')
    print(f'{cyan}{git}')
    print(batas)
    url  = input("[INFO] List Link Youtube >  ")
    open_url = open(url,'r').read().splitlines()
    for link in open_url:
    	try:
    		ekse = pafy.new(link)
    		print(f'{hijau}[+] {link}{tai} Judul : {ekse.title}')
    		print(cyan)
    		print('[!] Download > ')
    		dl = ekse.getbest()
    		dl.download()
    		print(batas)
    	except:
    		print(f'{hijau}[Sukses] {link} : {merah}Error')
    		print(batas)
if __name__ == '__main__':
			mainmenu = True
			while mainmenu == True:
				main()
				back = input("[!] Berhasil Download, Kembali Ke Home? (y/n) > ")
				if back.lower() == 'y':
					mainmenu = True
				else:
					mainmenu = False
			
		
