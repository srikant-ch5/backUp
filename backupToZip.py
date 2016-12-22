#python backupToZip.py -Copies an entire folder and its content into a ZIP file hwose filename increments

import zipfile,os

#call the function to perform the backup
def backupToZip(folder):
    #backup the entire contents of the folder

    #first the folder path should be absolute
    folder = os.path.abspath(folder)

    #figure out the filename this code should be used based on the existing files

    number = 1

    #-----------breaking the problem into three things---------------------#
    #-----------1st to create the zipfile name for different files when saved#
    #-----------2nd to create the zipfile
    #3rd to compress it

    #loop through the whole file to create the zipFileName using the number variable
    while True:
        zipFileName = os.path.basename(folder)+'_'+str(number)+'.zip'
        if not os.path.exists(zipFileName):
            break

        number +=1

    #create the ZIp file
    print 'Creating the zipfile %s' %(zipFileName)
    createZip = zipfile.ZipFile(zipFileName,'w')#creating the zipfile in the write  mode

    #Walk through the entire folder and then compress
    for foldername,subfolders,filenames in os.walk(folder):
        print "Adding folder %s.." %(foldername)

        #adding current folder to the zip file
        createZip.write(foldername)

        #then adding the files it has
        for filename in filenames:
            newBase = os.path.basename(folder)+'_'

            if  filename.startswith(newBase) and filename.endswith('.zip'):
                continue

            createZip.write(os.path.join(foldername,filename))
    createZip.close()

    print"The file has been saved into a zip file"

backupToZip('C:\\Users\pailla narsi reddy\\files\\delicious')
