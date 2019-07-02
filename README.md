Requirements

1)Tool should be run from any server where shared path is accessible (ie. for NDC  \\nms.pfin.com should be accessible from the machine, and for LADC  \\laxisilon.pftla.local should be accessible from the machine )

2)While configuring backup jobs through jenkins or scheduling DB backup , please make sure the below requirements are fulfilled.

             FOR NDC

            a)All the backup jobs except DB contains date format as DD_MM.And for which server backup is taken, in the backup file name  server name is also included.

            Means if the backup job need to configure for App server 192.168.19.240, make sure in the output backup file name both 192.168.19.240 and date instance is available.

            Example:-

            a.1)Suppose the backup is taken on June 22 for 192.168.19.240 server, then make sure the highlighted things are available in backup file name.

            Demo backup file name------Backup_Client_192.168.19.240_22_06_2019_0503

           a.2)Suppose the backup is taken on January 31 for DC 192.168.19.148 deployments folder, then make sure the highlighted things are available in backup file name.

            Demo backup file name------Backup_Backup_DC_deployments_192_168_19_148_31_01_2019_1104

           

           Exception For NDC Clear_NG DB backup.....

           For NDC DB backup, in the backup file name the date instance is coming in MM_DD format.

           Example:-

           Suppose DB backup is taken on June 20, then backup name coming like ----- Clear_NG_backup_2019_06_20_050501_9471825.bak

           As for NDC DB backup name format is different, we have handled the exception in code level. In case for any other jobs backup name is in MM_DD format for NDC , need to add the exception in                  code.

          If for NDC App server 192.168.19.33 , backup file name is    Backup_Client_192.168.19.33_06_20_2019_0503 and in report backup job name is Client_192.168.19.33, then to add the job in exception            follow below instructions.

In source code search for ####Exception for NDC (backup job name contain date in MM_DD format, but for NDC default name is DD_MM).
Currently exception code is like below         
          for file in files:

                 if(path in ['Clear_NG_backup']):

Please change the exception list as below (highlighted are the changes need to adopt for above example)
           for file in files:

                 if(path in ['Clear_NG_backup',Client_192.168.19.33]):



   

          FOR LADC

         a)All the backup jobs except DB contains date format as MM_DD.And for which server backup is taken, in the backup file name  server name is also included.

            Means if the backup job need to configure for App server 192.168.19.240, make sure in the output backup file name both 192.168.19.240 and date instance is available.

            Example:-

            a.1)Suppose the backup is taken on June 22 for 10.100.30.113 server, then make sure the highlighted things are available in backup file name.

            Demo backup file name------Backup_Client_10.100.30.113_06_22_2019_0503



Setting up of new Job to fetch report

1)If want to add the jobs for LADC environment, please search LADCjobs= {     and add jobs in side the tag.

2)If want to add the jobs for NDC environment, please search NDCjobs= {        and add jobs in side the tag.

3)If want to add the jobs for WEUR(Azure west Eurpoe) environment, please search WEURjobs= {     and add jobs in side the tag.



Example of Adding new Job.

Suppose you want to add a new job for LADC I&A server 10.100.30.71, then after configuring the backup job in Jenkins ,add the below in code under LADCjobs= {  

 If the path where backup is taken is \\laxisilon.pftla.local\Clear\ifs\PRODUCTION_BACKUPS\Data\I&A Server\10.100.30.71

and backup file name contains    Backup_Client_10.100.30.71_19_06_2019_1005   (backup job name should contain server IP and date , for LADC date is MM_DD, and for NDC date is DD_MM)

then add the below job in code (code is in format---->"Backup job name":r"folder where backup file is available",)

"Client_10.100.30.71":r"\\laxisilon.pftla.local\Clear\ifs\PRODUCTION_BACKUPS\Data\I&A Server\10.100.30.71",

 NOTE---

1)If in backup file name server ip is like  Client_10.100.30.71   , then in backup job name also entry should be Client_10.100.30.71

2)If in backup file name server ip is like  Client_10_100_30 then in backup job name also entry should be Client_10_100_30_71

means if server ip is separated by dot( . ) in backup file name , in backup job name also it should be separated by dot( . )

 if server ip is separated by underscore( _ ) in backup file name , in backup job name also it should be separated by underscore( _ )



Once the job is added in code, save the code and find below instruction to make the code file executable.

1)To make the file executable, in a machine where python is installed  make a folder with name JenkinBackupJob  in desktop of the machine.

2)Execute the below command in CMD( open cmd in admin mode)

pip install pyinstaller

If pyinstaller is already installed in the machine, it will show the below error.Otherwise it will insatll the package.



 

3)Once the package pyinstaller is installed, open cmd in folder where code is available.and run below command, that is navigate to JenkinBackupJob  folder and open cmd and run below command.

pyinstaller --onefile JenkinsBackupReport.py



(JenkinsBackupReport.py is the file name with extension)



The command will take some time t create the  .exe file. Once command is executed successfully executable file will be available in Desktop\JenkinBackupJob\dist  of the machine where python is installed.Copy/cut the exe file in LADC/NDC/WEUR environment.





Password to run the tool----ccteam@PFT

Source code is attached   (Once any modification is done, source code need to re-upload, otherwise while building the .exe file next time, old changes will not reflect )

JenkinsBackupReport.py





Currently tool is supporting both NDC and LADC environment.In case Azure Europe data centre is in live, we need to configure the jobs in the tool.

Tool should be run from any server where shared path is accessible (ie for NDC \\nms.pfin.com and for LADC \\laxisilon.pftla.local ). Currently tool is placed in 

For NDC environment

192.168.19.33 (Preprod App)--->E:\PFT\Tools\JenkinsBackupReport\JenkinsBackupReport.exe

For LADC environment
10.100.30.209(Preprod DC)----->E:\Tools\JenkinsBackupReport.exe

Report will be generated in the system C:\BackupDetails path,from where tool will be executed  

We have verified the below.

1)While running the tool Max CPU utilisation is 2% in LADC and in NDC it is 7-8 % while loading,after that it is 1-2%.
2)Time taken to run the tool in LADC environment is 4 minutes and in NDC it is 1 Minute.
3)Report will be generated in CSV format and report size will be 2 KB max. (attached sample .csv for your reference)
4)No report will be accumulated in report path, tool will take care of deleting the old reports.
5)In case any changes in backup path or backup Job name, tool will not work for that particular backup, it need to be configured. 
6)Mongo DB backup report is not included for now, we will configure the same in next phase.

