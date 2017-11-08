#!/usr/bin/python

import os
import subprocess

def searchfile(path):

		file1 = open("common.txt", "r")
		for file1 in file1.readlines():
			file1 = file1.replace("\n", "")
			path2 = path + file1
			tmp2 = os.path.isfile(path2)
			if tmp2 == True:
				print '\033[1;32m [F] \033[1;m', path2
			else:
				tmp3 = os.path.isdir(path2)
				if tmp3 == True:
					print '\033[1;34m [D] \033[1;m', path
					searchfile(path2+'/')

print '\033[1;44m Brute Force File System Detection:1 \033[1;m'
print '\033[1;44m The Level Of Authorization And Other User Information:2 \033[1;m'
print '\033[1;44m Detection Of Authority Upgrade Defects And Patch Defects On The System:3 \033[1;m'
print '\033[1;44m System Services, Time Operations And Highly Privileged Application Detectio:4 \033[1;m'
print '\033[1;44m Processes Running In The System, Network Services Review:5 \033[1;m'
print '\033[1;44m Shadow Files:6 \033[1;m'
print '\033[1;44m Directory Listing:7 \033[1;m'
print '\033[1;44m History Files:8 \033[1;m'
print '\033[1;44m List of SSH Keys and Key Indexes:9 \033[1;m'
print '\033[1;44m Configuration File List that can contain MySQL Access Information:10 \033[1;m'
print '\033[1;44m Web Application Directory and List of Files:11 \033[1;m'
print '\033[1;44m Mail Files:12 \033[1;m'
print '\033[1;44m Not Mount File Systems Control:13 \033[1;m'
print '\033[1;44m VPN System Files:14 \033[1;m'
x= input('Selection:')
if x == 1:
	users = open("names.txt", "r")
	for names in users.readlines():
		names = names.replace("\n", "")
		path = '/home/' + names + '/'
		tmp = os.path.isdir(path)
		if tmp == True:
			print '-------------------------------------------------------------'
			print '-------------------------------------------------------------'
			print '\033[1;34m [D] \033[1;m', path
			searchfile(path)
elif x == 2:
	print '\033[1;32m User Authority We Have: \033[1;m', subprocess.check_output(['whoami'],stderr=open('/dev/null', 'w'))
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m Sudoers File Access Rights: \033[1;m', subprocess.check_output(['ls','-l','/etc/sudoers'],stderr=open('/dev/null', 'w'))
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m Sudoers File: \033[1;m'
	sudoers = os.system('cat /etc/sudoers 2>/dev/null')
	if sudoers != 0:
		print '\033[1;32m Unable To Read Sudoers File!!! \033[1;m'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m User Sudo Rights: \033[1;m'
	print  subprocess.check_output(['sudo','-l','-n'],stderr=open('/dev/null', 'w'))
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m All Users: \033[1;m'
	passwd = os.system('cat /etc/passwd 2>/dev/null')
	if passwd != 0 :
		print ' Unable To Read Passwd File !!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m All Gruops: \033[1;m'
	group = os.system('cat /etc/group 2>/dev/null')
	if group != 0 :
		print ' Unable To Read Group File!!!'
elif x == 3:
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m Linux Kernel Version: \033[1;m'
	uname = os.system('uname -a 2>/dev/null')
	if uname != 0 :
		print ' Uname-a Unreadable!!!'
	print '-------------------------------------------------------------'
	version = os.system('cat /proc/version 2>/dev/null')
	if version != 0 :
		print ' Unable To Read Version File!!!!!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m Cpu Information: \033[1;m'
	uname = os.system('lscpu 2>/dev/null')
	if uname != 0 :
		print 'Unable To Read CPU Information!!!'
	print '-------------------------------------------------------------'
	print '\033[1;32m Linux Deployment Information: \033[1;m'
	release = os.system('cat /etc/*-release 2>/dev/null')
	if release != 0 :
		print 'Linux Deployment Information Unreadable!!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m Applications And Servers That May Have Potential To Upgrade:\033[1;m'
	uygulama = os.system('sudo -V | grep version 2>/dev/null')
	if uygulama != 0 :
		print 'Unread Application!!!'
	print '-------------------------------------------------------------'
	mysql = os.system('mysql --version 2>/dev/null')
	if mysql != 0 :
		print 'Mysql Versions Could Not Be Read!!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m Mounted File Systems:\033[1;m'
	mount = os.system('mount 2>/dev/null')
	if mount != 0 :
		print 'Mounted File Systems Unread!!!'
elif x == 4:
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m Cron Scripts:\033[1;m'
	cron = os.system('find /etc/cron* -perm -0002 -exec ls -la {} \; -exec cat {} 2>/dev/null \;')
	if cron != 0 :
		print 'No Other Printable Cron Scripts Found !!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m Crontab File:\033[1;m'
	crontab = os.system('cat /etc/crontab 2>/dev/null')
	if crontab != 0 :
		print 'Unable To Read Crontab File !!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m Root And Other Users Crontab File:\033[1;m'
	cron2 = os.system('ls -laR /var/spool/cron 2>/dev/null')
	if cron2 != 0 :
		print 'Root And Other Users Can Not Read Crontab File!!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m /etc/cron.d File List On The Drectory:\033[1;m'
	crond = os.system('ls -laR /etc/cron.d 2>/dev/null')
	if crond != 0 :
		print '/etc/cron.d File List Not Found In The Queue !!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m File List Setuid That Can Be Written By Other Users Who Have The Owner Root:\033[1;m'
	setuid = os.system('find / -uid 0 -perm -4002 -type f -exec ls -al {} \; 2>/dev/null')
	if setuid != 0 :
		print 'No File List Setuid Could Be Found That Could Be Written By Other Users With Proprietary Rootstock !!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m Printable All File List Setuid by Other Users:\033[1;m'
	setuid2 = os.system('find / -perm -4002 -type f -exec ls -al {} \; 2>/dev/null')
	if setuid2 != 0 :
		print 'Unable to Read All File List Setuid That Other Users Can Print!!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m All setuid File List:\033[1;m'
	setuid3 = os.system('find / -perm -4000 -type f -exec ls -al {} \; 2>/dev/null | tee setuid-files.enum.txt')
	if setuid3 != 0 :
		print 'All setuid File List Unread!!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m Shell Escape Possible Application List:\033[1;m'
	escape = os.system('cat setuid-files.enum.txt 2>/dev/null | grep -i -E \'vi|awk|perl|find|nmap|man|more|less|tcpdump|bash|sh$|vim|nc$|netcat|python|ruby|lua|irb\' | grep -v -E \'chsh|device\'')
	if escape != 0 :
		print 'Shell Escape No App giving Opportunity!!!'
elif x == 5:
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m Loopback List of TCP Network Services Accessible via Interface: \033[1;m'
	tcp = os.system('netstat -antp')
	if tcp != 0 :
		print 'TCP Network Services Not Found !!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m Loopback List of UDP Network Services Accessible via Interface: \033[1;m'
	udp = os.system('netstat -anup')
	if udp != 0 :
		print 'UDP Network Services Not Found !!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m Run Process List as Root User: \033[1;m'
	ppros = os.system('ps aux | grep root')
	if ppros != 0 :
		print 'Run Process List as Root User Not Found !!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m Images of Employee Processes and Their Access Rights List: \033[1;m'
	pros = os.system('ps aux | awk \'{print $11}\'|xargs -r ls -la 2>/dev/null |awk \'!x[$0]++\'')
	if pros != 0 :
		print 'Views of Employee Processes and Access Rights List Not Found!!!'
elif x == 6:
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m Shadow File Access Rights: \033[1;m', subprocess.check_output(['ls','-l','/etc/shadow'],stderr=open('/dev/null', 'w'))
	print '-------------------------------------------------------------'
	pros = os.system('cat /etc/shadow 2>/dev/null')
	if pros != 0 :
		print 'Shadow File Unreadable !!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'

elif x == 7:
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m /root/ List of Files and Access List under Directory: \033[1;m'
	droot = os.system('ls -ahlR /root/ 2>/dev/null')
	if droot != 0 :
		print 'Root File And Access List Directory Could Not Be Listed !!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m /home/ List of Files and Access List under Directory: \033[1;m'
	dhome = os.system('ls -ahlR /home/ 2>/dev/null')
	if dhome != 0 :
		print 'Home File And Access List Directory Could Not Be Listed!!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m /home/ Directory /usr/ Under /home/ List of Files and Access List under Directory: \033[1;m'
	dusrhome = os.system('ls -ahlR /usr/home/ 2>/dev/null')
	if dusrhome != 0 :
		print '/Usr/Home File And Access List Directory Could Not Be Listed!!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m /home/ List of Files and Access List under Directory: \033[1;m'
	dhomeread = os.system('find /home/ -perm -4 -type f -exec ls -al {} \; 2>/dev/null')
	if dhomeread != 0 :
		print 'Home/ File And Access List Directory Could Not Be Listed!!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m /usr/home/ Readable File List Under: \033[1;m'
	dusrhomeread = os.system('find /usr/home/ -perm -4 -type f -exec ls -al {} \; 2>/dev/null')
	if dusrhomeread != 0 :
		print '/usr/home/ File And Access List Directory Could Not Be Listed!!!'
elif x == 8:
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m History Files Access Rights: \033[1;m'
	hhis = os.system('ls -la /home/*/.*_history 2>/dev/null')
	if hhis != 0 :
		print 'Home History Not found !!!'
	print '-------------------------------------------------------------'
	hhis = os.system('ls -la /root/.*_history 2>/dev/null')
	if hhis != 0 :
		print 'Root History Not found !!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m History Files Access Rights: \033[1;m'
	readhis = os.system('cat ~/.*_history 2>/dev/null')
	if readhis != 0 :
		print 'History File Could not read !!!'
	print '-------------------------------------------------------------'
	readroothis = os.system('cat /root/.*_history 2>/dev/null')
	if readroothis != 0 :
		print 'Root History Could not read!!!'
	print '-------------------------------------------------------------'
	readhomehis = os.system('cat /home/*/.*_history 2>/dev/null')
	if readhomehis != 0 :
		print 'Home History Could not read!!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
elif x == 9:
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
	print '\033[1;32m List of SSH Keys and Key Indexes: \033[1;m'
	sshkey = os.system('find / -name "id_dsa*" -o -name "id_rsa*" -o -name "known_hosts" -o -name "authorized_hosts" -o -name "authorized_keys" 2>/dev/null')
	if sshkey != 0 :
		print 'Ssh Key Not Found !!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
elif x == 10:
	print '\033[1;32m MConfiguration File List that can contain MySQL Access Information: \033[1;m'
	print '-------------------------------------------------------------'
	print '/etc/mysql/my.cnf File:'
	mysql1 = os.system('cat /etc/mysql/my.cnf 2>/dev/null')
	if mysql1 != 0 :
		print '/etc/mysql/my.cnf Could not read !!!'
	print '-------------------------------------------------------------'
	print '/etc/my.cnf 2>/dev/null File:'
	mysql2 = os.system('cat /etc/my.cnf 2>/dev/null')
	if mysql2 != 0 :
		print '/etc/my.cnf Could not read !!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
elif x == 11:
	print '\033[1;32m Web Application Directory and List of Files: \033[1;m'
	print '-------------------------------------------------------------'
	print '/var/www/ Directory:'
	varwww = os.system('ls -alhR /var/www/ 2>/dev/null')
	if varwww != 0 :
		print '/var/www/ Directory Not Listed !!!'
	print '-------------------------------------------------------------'
	print '/srv/www/htdocs/ Directory:'
	srvwwwhtdocs = os.system('ls -alhR /srv/www/htdocs/ 2>/dev/null')
	if srvwwwhtdocs != 0 :
		print '/srv/www/htdocs/ Directory Not Listed !!!'
	print '-------------------------------------------------------------'
	print '/usr/local/www/apache22/data/ Directory:'
	varwww = os.system('ls -alhR /usr/local/www/apache22/data/ 2>/dev/null')
	if varwww != 0 :
		print '/usr/local/www/apache22/data/ Directory Not Listed !!!'
	print '-------------------------------------------------------------'
	print '/opt/lampp/htdocs/ Directory:'
	srvwwwhtdocs = os.system('ls -alhR /opt/lampp/htdocs/ 2>/dev/null')
	if srvwwwhtdocs != 0 :
		print '/opt/lampp/htdocs/ Directory Not Listed!!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
elif x == 12:
	print '\033[1;32m Mail Files: \033[1;m'
	print '-------------------------------------------------------------'
	print '/var/mail/root File:'
	mail1 = os.system('cat /var/mail/root 2>/dev/null')
	if mail1 != 0 :
		print '/var/mail/root File Could Not Read!!!'
	print '-------------------------------------------------------------'
	print '/var/spool/mail/root File:'
	mail2 = os.system('cat /var/spool/mail/root 2>/dev/null')
	if mail2 != 0 :
		print '/var/spool/mail/root File Could not read!!!'
	print '-------------------------------------------------------------'
	print '-------------------------------------------------------------'
elif x == 13:
	print '\033[1;32m Not Mount File Systems Control: \033[1;m'
	print '-------------------------------------------------------------'
	print 'fstab File:'
	mountcontrol = os.system('cat /etc/fstab')
	if mountcontrol != 0 :
		print 'fstab File Could Not Read!!!'
	print '-------------------------------------------------------------'
	print 'fstab Search for User Access Information in the File:'
	usercontrol = os.system('cat /etc/fstab 2>/dev/null |grep username |awk \'{sub(/.*\username=/,"");sub(/\,.*/,"")}1\'| xargs -r echo username:; cat /etc/fstab 2>/dev/null |grep password |awk \'{sub(/.*\password=/,"");sub(/\,.*/,"")}1\'| xargs -r echo password:; cat /etc/fstab 2>/dev/null |grep domain |awk \'{sub(/.*\domain=/,"");sub(/\,.*/,"")}1\'| xargs -r echo domain:')
	if usercontrol != 0 :
		print 'fstab File Could Not Read !!!'
	print '-------------------------------------------------------------'
	print 'fstab Credentials in File Reference Search:'
	fstabcredentials = os.system('cat /etc/fstab 2>/dev/null |grep cred |awk \'{sub(/.*\credentials=/,"");sub(/\,.*/,"")}1\'| xargs -I{} sh -c \'ls -la {}; cat {}\'')
	if fstabcredentials != 0 :
		print 'fstab dentity Information Not Found During File Reference !!!'
elif x == 14:
	print '\033[1;32m VPN System Files: \033[1;m'
	print '-------------------------------------------------------------'
	print '/etc/openvpn/ Directory:'
	varwww = os.system('ls -alhR /etc/openvpn/ 2>/dev/null | grep conf')
	if varwww != 0 :
		print '/etc/openvpn/ Directory Not Listed !!!'
else:
	print ' Error!!!'
