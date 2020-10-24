# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv


#FILENAME IS IMPORTED TO THE FUNCTION
filename = 'data/testBCCData.csv'

#FILENAME TO WRITE ROWS TO
filepass = 'passed.txt'
filefail = 'failed.txt'

#LIST OF .TXT FILES WHICH CONTAIN THE ARRAY OF ACCEPTED VALUES FOR VALIDATION 
countryfile = 'data/newC.txt'
MatHtfile = 'data/MatHtlist.txt' #100-213
MatWtfile = 'data/MatWtlist.txt' #30-300 increment of 2
Parityfile = 'data/parity.txt' #0-15
Sexfile = 'data/sex.txt' #M F U
Gestfile = 'data/Gestlist.txt' # 140-308
Bweightfile = 'data/Bweightlist.txt' #150-8000 increment of 50
Outcomefile = 'data/outcome.txt' #LB SB

#EMPTY LISTS WHICH WILL BE POPLATED WITH DATA IN THE .TXT FILES. 
CClist = []
MatHtlist = []
MatWtlist = []
Paritylist = []
Sexlist = []
Gestlist = []
Bweightlist = []
Outcomelist = []

ApprovedDatalist = []
FailedDatalist = []

BCCRow = 1
Plus1 = 0
Plus0 = 0


with open(filename) as f, open(countryfile) as cf, \
    open(MatHtfile) as mh, open(MatWtfile) as mw, \
    open(Parityfile) as par, open(Sexfile) as sex, \
    open(Gestfile) as gest, open(Bweightfile) as bw, \
    open(Outcomefile) as out:
        BCC = csv.reader(f)
        #moves to second line so headers aren't included
        header = next(BCC)
    
        #STRUCTURING .TXT FILES REMOVING ANY BLANK SPACE
        codelist = cf.readlines()
        for line in codelist: 
            CC = line.rstrip()
            CClist.append(CC)
    
        htlist = mh.readlines()
        for line in htlist:
            ht = line.rstrip()
            MatHtlist.append(ht)
            
        wtlist = mw.readlines()
        for line in wtlist:
            wt = line.rstrip()
            MatWtlist.append(wt)
         
        parlist = par.readlines()
        for line in parlist:
            par = line.rstrip()
            Paritylist.append(par)
    
        sexlist = sex.readlines()
        for line in sexlist:
            sex = line.rstrip()
            Sexlist.append(sex)
         
        gstlist = gest.readlines()
        for line in gstlist:
            gest = line.rstrip()
            Gestlist.append(gest)
         
        bwlist = bw.readlines()
        for line in bwlist:
            bw = line.rstrip()
            Bweightlist.append(bw)
    
        outlist = out.readlines()
        for line in outlist:
            out = line.rstrip()
            Outcomelist.append(out)
            
            
            
        for eachrow in BCC:
            #get the first index of each row and store it into a variable.
            ID = eachrow[0]
            #validate variable. ID must be length3
            #CHEKING TO SEE IF THE SOTRED VARIABLE IS IN THE LIST 
            if len(ID) == 4:
                pass
            elif len(ID) == 0:
                print("no value")
            else:
                #if ID is not in list print the failed ID and what row it's on
                print(f"ID {ID} failed on row {BCCRow}")
                Plus0 =1
                
                    
            Ethnic = eachrow[1]
            #compare the ethnicity code to a list
            #if eth is in list then ...
            if Ethnic in CClist:
                pass
            else:
                print(f"Ethnic {Ethnic} failed on row {BCCRow}")
                Plus0 =1            
              
            MatHt = eachrow[2]
            if MatHt in MatHtlist:
                pass
            else:
                print(f"Height {MatHt} failed on row {BCCRow}")
                Plus0 =1
                
            MatWt = eachrow[3]
            if MatWt in MatWtlist:
                pass
            else:
                print(f"Weight {MatWt} failed on row {BCCRow}")
                Plus0 =1
                
            Parity = eachrow[4]
            if Parity in Paritylist:
                pass
            else:
                print(f"Parity {Parity} failed on row {BCCRow}")
                Plus0 =1
                
            Sex = eachrow[5]
            if Sex in Sexlist:
                pass
            else:
                print(f"Sex {Sex} failed on row {BCCRow}")
                Plus0 =1

            Gest = eachrow[6]
            if Gest in Gestlist:
                pass
            else:
                print(f"Gestation {Gest} failed on row {BCCRow}")
                Plus0 =1
    
            Bwt = eachrow[7]
            if Bwt in Bweightlist:
                pass
            else:
                print(f"Birthweight {Bwt} failed on row {BCCRow}")
                Plus0 =1

            Out = eachrow[8]
            if Out in Outcomelist:
                pass
            else:
                print(f"Outcome {Out} failed on row {BCCRow}")
                Plus0 =1
            
           
            #PASSED ROWS GO TO ONE FILE, FAILED ROWS TO ANOTHER FILE 
            if Plus0 ==0:
                print(eachrow)
                with open(filepass, 'a') as file_object:
                    file_object.write(f" {str(eachrow)} \n")
                    
            elif Plus0 ==1:
                with open(filefail, 'a') as file_object:
                    file_object.write(f" {str(eachrow)} \n")
            
            #INCREMENT ROW NUMBER
            BCCRow +=1
            #RESET
            Plus0 =0
         
         
         
print(BCCRow)



