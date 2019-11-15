import os, sys

print ("\033[1;32mSilahkan Masukkan Username & Password Anda")

print ("\033[1;32mAtau Silahkan Hubungi WhatsApp : 085865805481 ")

username = 'rouzancyber'      

password = 'nosystemissafe'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("Username : ")

	if uname == Username:

		pwd = raw_input("Password : ")



		if pwd == Password:

			print "\033[1;32mAlhamdulillah sudah masuk juga..", 

			sys.exit()



		else:

			print "\033[1;32mMaaf Masukkan password Anda salah... [?]\033[00m"

			print "Silahkan segera log-in kembali...!!\n"

			restart()



	else:

		print "\033[1;32mMaaf Masukkan Username Anda salah... [?]\033[00m"

		print "Silahkan segera log-in kembali...!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
