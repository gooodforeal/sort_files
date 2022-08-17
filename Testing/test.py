import os
import shutil


main_dir = input('Введите название главной папки: ')

main_path = os.getcwd()
dowload_path = "C:/Users/Timothy/Desktop/install"

dowload_files = os.listdir(path=dowload_path)

os.makedirs(f'{main_dir}/Packlists')
os.mkdir(f'{main_dir}/Invoices')
os.mkdir(f'{main_dir}/Edited Invoices')


for file in dowload_files:
	if "invoice" in file:
		os.replace(f"{dowload_path}/{file}",
			f"{main_path}/{main_dir}/Invoices/{file}"
			)
		for file1 in os.listdir(f"{main_path}/{main_dir}/Invoices"):
			shutil.copyfile(f"{main_path}/{main_dir}/Invoices/{file1}",
				f"{main_path}/{main_dir}/Edited Invoices/Jaaz {file1}"
				)
	elif "packlist" in file:
		os.replace(f"{dowload_path}/{file}", f"{main_path}/{main_dir}/Packlists/{file}")
	else:
		pass


