import os,csv,pandas as pd,getpass
from datetime import date, timedelta
import socket

class LADC():

    def backupJobsList(self):
        LADCjobs= {
			####ASPERA SERVER######
            "Aspera_10.100.30.111":r"\\laxisilon.pftla.local\Clear\ifs\PRODUCTION_BACKUPS\Aspera\10.100.30.111",
			####APP SERVER###
			#####App Server
            "Client_10.100.30.113": r"\\laxisilon.pftla.local\Clear\ifs\PRODUCTION_BACKUPS\Data\App\10.100.30.113",
            "Client_10.100.30.115": r"\\laxisilon.pftla.local\Clear\ifs\PRODUCTION_BACKUPS\Data\App\10.100.30.115",
            "Client_10.100.30.116": r"\\laxisilon.pftla.local\Clear\ifs\PRODUCTION_BACKUPS\Data\App\10.100.30.116",
            "Client_10.100.30.117": r"\\laxisilon.pftla.local\Clear\ifs\PRODUCTION_BACKUPS\Data\App\10.100.30.117",
            #####GUVNOR SERVER#####
			"Guvnor_10_100_30_199":r"\\laxisilon.pftla.local\Clear\ifs\PRODUCTION_BACKUPS\Jenkins_Backups\Guvnor",
			#####DEMO NAB DC ######
			"configuration_10_100_30_89":r"\\laxisilon.pftla.local\Clear\ifs\PRODUCTION_BACKUPS\Jenkins_Backups\JBOSS_DC\DEMONAB\configuration",
			"deployments_10_100_30_89":r"\\laxisilon.pftla.local\Clear\ifs\PRODUCTION_BACKUPS\Jenkins_Backups\JBOSS_DC\DEMONAB\Deployments",
			####JBOSS DC#####
			"configuration_10_100_30_187":r"\\laxisilon.pftla.local\Clear\ifs\PRODUCTION_BACKUPS\Jenkins_Backups\JBOSS_DC\configuration",
			"deployments_10_100_30_187":r"\\laxisilon.pftla.local\Clear\ifs\PRODUCTION_BACKUPS\Jenkins_Backups\JBOSS_DC\Deployments",
			####STREAMING SERVERg####
			"StreamingServer_10.100.30.181":r"\\laxisilon.pftla.local\Clear\ifs\PRODUCTION_BACKUPS\Jenkins_Backups\StreamingServer_10.100.30.181",
			####WEB SERVER####
			"WebServices_10.100.30.191":r"\\laxisilon.pftla.local\Clear\ifs\PRODUCTION_BACKUPS\Data\Web Server\10.100.30.191",
			"WebServices_10.100.30.192":r"\\laxisilon.pftla.local\Clear\ifs\PRODUCTION_BACKUPS\Data\Web Server\10.100.30.192",
			"WebServices_10.100.30.193":r"\\laxisilon.pftla.local\Clear\ifs\PRODUCTION_BACKUPS\Data\Web Server\10.100.30.193",
			"WebServices_10.100.30.196":r"\\laxisilon.pftla.local\Clear\ifs\PRODUCTION_BACKUPS\Data\Web Server\10.100.30.196"
				}
        return (LADCjobs)

class NDC():
    def backupJobsList(self):
        NDCjobs= {
            ####ASPERA SERVER######
            "Client_192.168.19.94": r"\\nms.pfin.com\PRODUCTION_BACKUPS\Aspera\192_168_19_94",
            "Client_192.168.19.243": r"\\nms.pfin.com\PRODUCTION_BACKUPS\Aspera\192_168_19_243",
            ####BOMAM####
            "BOMAM_ConfigurationServiceWSConfigs_192_168_19_230": r"\\nms.pfin.com\PRODUCTION_BACKUPS\BOMAM\ConfigurationServiceWSConfigs",
            "BOMAM_MediaArchive_192_168_19_230": r"\\nms.pfin.com\PRODUCTION_BACKUPS\BOMAM\MediaArchive",
            "BOMAM_MediaArchiveData_192_168_19_230": r"\\nms.pfin.com\PRODUCTION_BACKUPS\BOMAM\MediaArchiveData1",
            ####APP SERVER###
            "Client_192.168.19.33": r"\\nms.pfin.com\PRODUCTION_BACKUPS\Portal\192.168.19.33",
            "Client_192.168.19.240": r"\\nms.pfin.com\PRODUCTION_BACKUPS\Portal\192.168.19.240",
            "Client_192.168.19.241": r"\\nms.pfin.com\PRODUCTION_BACKUPS\Portal\192.168.19.241",
            ####JBOSS DC#####
            "configuration_192_168_19_148": r"\\nms.pfin.com\PRODUCTION_BACKUPS\JBOSS_DC\192.168.19.148",
            "configuration_192_168_19_246": r"\\nms.pfin.com\PRODUCTION_BACKUPS\JBOSS_DC\192.168.19.246",
            "configuration_192_168_19_115": r"\\nms.pfin.com\PRODUCTION_BACKUPS\JBOSS_MC",
            "deployments_192_168_19_148": r"\\nms.pfin.com\PRODUCTION_BACKUPS\JBoss\DC\192.168.19.148",
            "deployments_192_168_19_246": r"\\nms.pfin.com\PRODUCTION_BACKUPS\JBoss\DC\192.168.19.246",
            "deployments_192_168_19_115": r"\\nms.pfin.com\PRODUCTION_BACKUPS\JBOSS_MC\Jboss mc deployment",
            ####RHOZET####
            "Rhozet_10.1.130.27": r"\\nms.pfin.com\PRODUCTION_BACKUPS\Rhozet\10.1.130.27",
            ####Clear_NG####
            "Clear_NG_backup": r"\\nms.pfin.com\PRODUCTION_BACKUPS\SQLDB\NDC\Full Production DB Backup\Clear_NG",
            ####WEB SERVER####
            "Client_192.168.19.81": r"\\nms.pfin.com\PRODUCTION_BACKUPS\WebServices\192.168.19.81",
            "Client_192.168.19.82": r"\\nms.pfin.com\PRODUCTION_BACKUPS\WebServices\192.168.19.82",
            "Client_192.168.19.83": r"\\nms.pfin.com\PRODUCTION_BACKUPS\WebServices\192.168.19.83"
        }
        return (NDCjobs)

class WEUR():
    def backupJobsList(self):
        WEURjobs= {
            #####App Server
            "Client-10.100.30.113": r"D:\DummyBackup\laxisilon.pftla.local\Clear\ifs\PRODUCTION_BACKUPS\Data\App\10.100.30.113",
            "Client-10.100.30.115": r"D:\DummyBackup\laxisilon.pftla.local\Clear\ifs\PRODUCTION_BACKUPS\Data\App\10.100.30.115",
            "Client-10.100.30.116": r"D:\DummyBackup\laxisilon.pftla.local\Clear\ifs\PRODUCTION_BACKUPS\Data\App\10.100.30.116",
            "Client-10.100.30.117": r"D:\DummyBackup\laxisilon.pftla.local\Clear\ifs\PRODUCTION_BACKUPS\Data\App\10.100.30.117"
        }
        return (WEURjobs)

#########################################################################################
########################################################################################
######################################################################################3
###creating csv file path and csv file , deleting old Backupdetails file
for roots,dirs,files in os.walk("c:\\BackupDetails"):
    for file in files:
        os.remove("c:\\BackupDetails\\"+file)

if (os.path.exists("c:\\BackupDetails") == False):
    os.mkdir("c:\\BackupDetails")

csvData= [['BACKUP JOB NAME','PREVIOUS BACKUP SIZE','CURRENT BACKUP SIZE']]
with open('c:\\BackupDetails\\BackupDetails.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)


def getDates(env):
    today = date.today()  ###will be in format YYYY-MM-DD
    yesterday = today - timedelta(days = 1)
    dayBeforeYesterday=yesterday- timedelta(days = 1)
    today=str(today).split('-')
    yesterday=str(yesterday).split('-')
    dayBeforeYesterday=str(dayBeforeYesterday).split('-')
    if(env in ['LADC','WEUR']):
        today = today[1] + '_' + today[2]
        yesterday = yesterday[1] + '_' + yesterday[2]
        dayBeforeYesterday = dayBeforeYesterday[1] + '_' + dayBeforeYesterday[2]
    elif(env=='NDC'):
        today = today[2] + '_' + today[1]
        yesterday = yesterday[2] + '_' + yesterday[1]
        dayBeforeYesterday = dayBeforeYesterday[2] + '_' + dayBeforeYesterday[1]

    return today,yesterday,dayBeforeYesterday

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.3f %s" % (num, x)
        num /= 1024.0

def getFilesize(filepath,today,yesterday,dayBeforeYesterday):
    yesterdayBackupSize = todayBackupSize=dayBeforeYesterdayBackupSize=0
    for roots, dirs, files in os.walk(filepath):
        for file in files:
            if(path=='Clear_NG_backup'):
                today, yesterday, dayBeforeYesterday = getDates('LADC')
            if((today in file)and (path in file)):
                todayBackupSize =convert_bytes(os.stat(filepath + '\\' + file).st_size)
            if((yesterday in file)and (path in file)):
                yesterdayBackupSize=convert_bytes(os.stat(filepath+'\\'+file).st_size)
            if ((dayBeforeYesterday in file)and (path in file)):
                dayBeforeYesterdayBackupSize = convert_bytes(os.stat(filepath + '\\' + file).st_size)

    if (todayBackupSize != 0 and yesterdayBackupSize != 0):
        row = [path, yesterdayBackupSize, todayBackupSize]
        with open('C:\\BackupDetails\\BackupDetails.csv', 'a') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow(row)
            df = pd.read_csv('c:\\BackupDetails\\BackupDetails.csv')
            # Droping the empty rows
            modifiedDF = df.dropna()
            # Saving it to the csv file
            modifiedDF.to_csv('c:\\BackupDetails\\BackupDetails.csv', index=False)

    elif(yesterdayBackupSize != 0 and dayBeforeYesterdayBackupSize!=0):
        row = [path, dayBeforeYesterdayBackupSize, yesterdayBackupSize]
        with open('C:\\BackupDetails\\BackupDetails.csv', 'a') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow(row)
            df = pd.read_csv('c:\\BackupDetails\\BackupDetails.csv')
            # Droping the empty rows
            modifiedDF = df.dropna()
            # Saving it to the csv file
            modifiedDF.to_csv('c:\\BackupDetails\\BackupDetails.csv', index=False)
    else:
        if((yesterdayBackupSize==0)and (dayBeforeYesterdayBackupSize==0)):
            row = [path,"NO BACKUP FOUND","NO BACKUP FOUND"]
        elif(yesterdayBackupSize==0):
            row = [path,dayBeforeYesterdayBackupSize,"NO BACKUP FOUND"]
        else:
            row = [path,"NO BACKUP FOUND",yesterdayBackupSize]
        with open('C:\\BackupDetails\\BackupDetails.csv', 'a') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow(row)
            df = pd.read_csv('c:\\BackupDetails\\BackupDetails.csv')
            # Droping the empty rows
            modifiedDF = df.dropna()
            # Saving it to the csv file
            modifiedDF.to_csv('c:\\BackupDetails\\BackupDetails.csv', index=False)

password=input("\nENTER PASSWORD : ")
if(password=='ccteam@PFT'):
    print("\n\nTO GENERATE JENKINS BACKUP REPORT PLEASE SELECT THE ENVIRONMENT :-\n\t\t\t\t\t\t\t\tFOR LADC-->LADC\n\t\t\t\t\t\t\t\tFOR NDC--> NDC\n\t\t\t\t\t\t\t\tFOR WEUR-->WEUR")
    env=input("\n\nENTER ENVIRONMENT : ")
    env=env.strip().upper()
    try:
        if (env in ['LADC','NDC','WEUR']):
            if(env=='LADC'):
                objectOfEnvironment=LADC()
                today, yesterday, dayBeforeYesterday = getDates(env)
            elif (env== 'NDC'):
                objectOfEnvironment= NDC()
                today, yesterday, dayBeforeYesterday = getDates(env)
            else:
                objectOfEnvironment=WEUR()
                today, yesterday, dayBeforeYesterday = getDates(env)

            jobs=objectOfEnvironment.backupJobsList()
            backupPaths=jobs.keys()
            print("\nRUNNING SCRIPT FOR :- ",env,'\n')
            for path in backupPaths:
                getFilesize(jobs.get(path), today, yesterday,dayBeforeYesterday)
            x=input("REPORT IS AVAILABLE IN C:\BackupDetails\n\nPRESS ANY KEY TO EXIT : ")

        else:
            raise ValueError

    except ValueError as VE:
        print("\n---------------WRONG/INVALID OPTION---------")
        x=input("\nPRESS ANY KEY TO EXIT : ")
else:
    print("\nWRONG PASSWORD, PROGRAM TERMINATING.....")
