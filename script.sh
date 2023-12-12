#!/bin/bash

# Cчитываем имя домена из терминала
echo "Введите домен"
read domen

# Создаём папку для текущего запуска
echo "1"
now=$(date +"%d-%m-%Y_%H-%M-%S")
r="_"
name_folder="$now$r$domen"
mkdir $name_folder
mkdir $name_folder/inf
mkdir $name_folder/worker
echo "2"



###-1 Добавляем необходимые флаги
while getopts "x d s" ARG; do
  case "$ARG" in 
    x) xml="Yes";; # Флаг nmap - для сохранения вывода nmap в xml файле
    d) dom="Yes";; # Флаг nmap - для сканирования поддоменов
    s) severity="-severity critical";; # Флаг nuclei - указывающий на серьёзность цели сканирования -severity
    :​) echo "argument missing";;
    \?) echo "Something is wrong";;
  esac
done
echo "3"



###-1 Запускаем amass и сохраняем результат работы в файл: 
amass enum -d $domen -passive > ./$name_folder/inf/amass_out.txt
echo "ammas - закончил работу"
echo "4"



###-2 Запускаем поиск ip-адресов по найденым поддоменам
for line in `cat ./$name_folder/inf/amass_out.txt`
do 
	nslookup $line >> ./$name_folder/worker/nslookup_out_ip.txt
done
echo "5"

# Удаляем лишнюю информацию и оставляем только ip-адреса
sed -i '/^Server:/d' ./$name_folder/worker/nslookup_out_ip.txt
sed -i '/answer/d' ./$name_folder/worker/nslookup_out_ip.txt
sed -i '/^Name:/d' ./$name_folder/worker/nslookup_out_ip.txt
sed -i '/#/d' ./$name_folder/worker/nslookup_out_ip.txt
sed -i '/find/d' ./$name_folder/worker/nslookup_out_ip.txt
sed -i '/^$/d' ./$name_folder/worker/nslookup_out_ip.txt
sed -i 's/Address: //' ./$name_folder/worker/nslookup_out_ip.txt
### Удаляем лишние ip-адреса
sed -i '/^127/d' ./$name_folder/worker/nslookup_out_ip.txt
#sed -i '/^35/d' ./$name_folder/worker/nslookup_out_ip.txt
#sed -i '/^44.238/d' ./$name_folder/worker/nslookup_out_ip.txt
echo "6"

# Удаляем все повторяющиеся ip-адреса
sort -u ./$name_folder/worker/nslookup_out_ip.txt > ./$name_folder/inf/sort_nslookup_out_ip.txt

# Выводим результат работы  nslookup  записанный в файл
cat ./$name_folder/inf/sort_nslookup_out_ip.txt
echo "7"



###-3 -------- Здесь цыкл поиска открытых поротов для каждого из найдSеных ip и запись в файл
#              новый формат ip:порт
if [[ ${#dom} -ne 0 ]] 
then
	if [[ ${#xml} -ne 0 ]] 
	then
		xml_domen="-oX ./$name_folder/worker/nmap_out-domen.xml"
	fi
	
	for line_ip in `cat ./$name_folder/inf/amass_out.txt`
	do 
		nmap -oN ./$name_folder/worker/nmap_out-domen.txt $xml_domen $line_ip 
		cat ./$name_folder/worker/nmap_out-domen.txt >> ./$name_folder/inf/nmap_out-domen_full.txt
		if [[ ${#xml} -ne 0 ]] 
		then
			cat ./$name_folder/worker/nmap_out-domen.xml >> ./$name_folder/inf/nmap_out-domen_full.xml
		fi
	done
fi
echo "8"

for line_ip in `cat ./$name_folder/inf/sort_nslookup_out_ip.txt`
do 
	###-3.1 Запускаем сканирование открытых портов по найденым поддоменам
	echo "------------------- Сканируется $line_ip :" >> ./$name_folder/worker/nmap_out.txt
	
	# Проверяем что нужно включить в вывод .xml
	if [[ ${#xml} -ne 0 ]] 
	then
		xml_domen="-oX ./$name_folder/worker/nmap_out.xml"
	fi
	
	# Запускаем nmap
	nmap -oN ./$name_folder/worker/nmap_out.txt $xml_domen $line_ip
	
	# Если в вывод xml включить нужно, то
	if [[ ${#xml} -ne 0 ]] 
	then
		# Записываем результаты работы nmap в общий файл
		cat ./$name_folder/worker/nmap_out.xml >> ./$name_folder/inf/nmap_out_full.xml
	fi
	
	# Записываем результаты работы nmap в общий файл
	cat ./$name_folder/worker/nmap_out.txt >> ./$name_folder/inf/nmap_out_full.txt
	
	echo "" >> ./$name_folder/worker/nmap_out.txt
	echo "" >> ./$name_folder/worker/nmap_out.txt
	
	
	

	###-3.2 Удаляем все строки кроме тех в которых встречается слово  open
	sed -i '/open/!d' ./$name_folder/worker/nmap_out.txt
	###-3.3 Удаляем всю информацию кроме номера порта
	sed -r 's/[/].+//' ./$name_folder/worker/nmap_out.txt > ./$name_folder/worker/nmap_out_ports.txt
	###-3.4 Удаляем все повторяющиеся порты
	sort -u ./$name_folder/worker/nmap_out_ports.txt > ./$name_folder/worker/sort_nmap_out_ports.txt
	
	cat ./$name_folder/worker/sort_nmap_out_ports.txt
	
	
	# Записываем в файл отсортированные результаты в виде "ip:порт"
	for line_port in `cat ./$name_folder/worker/sort_nmap_out_ports.txt`
	do
		echo $line_ip":"$line_port >> ./$name_folder/inf/sort_nmap_out_kopiya_ip_ports.txt
	done
	rm ./$name_folder/worker/nmap_out.txt
done
echo "9"

# Удаляем лишние символы из полученых строк
sed -i 's/ //' ./$name_folder/inf/sort_nmap_out_kopiya_ip_ports.txt
sed -i 's/ //' ./$name_folder/inf/sort_nmap_out_kopiya_ip_ports.txt
echo "10"



###-4 Зпускаем nuclei на найденых открытых портах для найденых ip-адресов
nuclei -l ./$name_folder/inf/sort_nmap_out_kopiya_ip_ports.txt -o ./$name_folder/inf/nuclei_out.txt $severity

echo "11"





