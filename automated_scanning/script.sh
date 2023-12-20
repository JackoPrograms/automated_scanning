#!/bin/bash

# Cчитываем имя домена из файла
domen=`cat domain_name.txt`

# Создаём папку для текущего запуска
now=$(date +"%d-%m-%Y_%H-%M-%S")
r="_"
name_folder="$now$r$domen"
mkdir $name_folder
mkdir $name_folder/inf
mkdir $name_folder/worker



###-1 Добавляем необходимые флаги
severity_and_tags_flag="-tags "
severity_and_tags_flag+=`cat tags_vulnerabilities.txt`
severity_and_tags_flag+=" -severity "
severity_and_tags_flag+=`cat severity_vulnerabilities.txt`


while getopts "x d s" ARG; do
  case "$ARG" in 
    x) xml="Yes";; # Флаг nmap - для сохранения вывода nmap в xml файле
    d) dom="Yes";; # Флаг nmap - для сканирования поддоменов
	# Флаг nuclei - указывающий на серьёзность цели сканирования -severity и используемые -tags
    s) severity_and_tags=severity_and_tags_flag;;
    :​) echo "argument missing";;
    \?) echo "Something is wrong";;
  esac
done



###-1 Запускаем subfinder и сохраняем результат работы в файл:
subfinder -d $domen > ./$name_folder/inf/subfinder_out.txt
echo "subfinder - закончил работу"



###-2 Запускаем поиск ip-адресов по найденым поддоменам
for line in `cat ./$name_folder/inf/subfinder_out.txt`
do 
	nslookup $line >> ./$name_folder/worker/nslookup_out_ip.txt
done

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

# Удаляем все повторяющиеся ip-адреса
sort -u ./$name_folder/worker/nslookup_out_ip.txt > ./$name_folder/inf/sort_nslookup_out_ip.txt

# Выводим результат работы  nslookup  записанный в файл
cat ./$name_folder/inf/sort_nslookup_out_ip.txt



###-3 -------- Здесь цыкл поиска открытых поротов для каждого из найдSеных ip и запись в файл
#              новый формат ip:порт
if [[ ${#dom} -ne 0 ]] 
then
	if [[ ${#xml} -ne 0 ]] 
	then
		xml_domen="-oX ./$name_folder/worker/nmap_out-domen.xml"
	fi
	
	for line_ip in `cat ./$name_folder/inf/subfinder_out.txt`
	do 
		nmap -oN ./$name_folder/worker/nmap_out-domen.txt $xml_domen $line_ip 
		cat ./$name_folder/worker/nmap_out-domen.txt >> ./$name_folder/inf/nmap_out-domen_full.txt
		if [[ ${#xml} -ne 0 ]] 
		then
			cat ./$name_folder/worker/nmap_out-domen.xml >> ./$name_folder/inf/nmap_out-domen_full.xml
		fi
	done
fi

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

# Удаляем лишние символы из полученых строк
sed -i 's/ //' ./$name_folder/inf/sort_nmap_out_kopiya_ip_ports.txt
sed -i 's/ //' ./$name_folder/inf/sort_nmap_out_kopiya_ip_ports.txt



###-4 Зпускаем nuclei на найденых открытых портах для найденых ip-адресов
nuclei -l ./$name_folder/inf/sort_nmap_out_kopiya_ip_ports.txt -o ./$name_folder/inf/nuclei_out.txt $severity_and_tags
