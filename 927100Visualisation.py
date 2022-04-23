import csv
import matplotlib.pyplot as plt
import pandas as pd

print("This will show graphs of each malware family")
print("Each number corresponds category order")
uInput1 = int(input("Enter Graph Screen [1-14] "))
if uInput1 == 1:
    while uInput1 == 1:
        dd =  pd.read_csv("C:\csv\Dataset Details.CSV")
   

        input_Values =[1,669,887,1538,1556,2051,2296,2302,3125,3540,6202,13340,13559,47210,97349]
        plots = [1,669,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,10000]

        fig, ax= plt.subplots()
        fig.suptitle("Dataset Graph", fontsize=18)
        ax.set_title("Captured Samples")
        ax.set_xlabel("Samples", fontsize=12)
        ax.set_ylabel("??", fontsize=12)
        ax.plot(input_Values,plots, 'mD:')
        plt.show()
        break
elif uInput1 == 2:
    while uInput1 ==2:
        hd = pd.read_csv("C:\csv\hardware.CSV")
        input_Values = [3,7,14,16,17,17,19,26,28,28,31,41,43,44,45,46,50,60,61,77,79,82,92,103,108,113,117,127,171,233,301,330,349,418,458,913,984,1015,1033,1047,2242,2679,19306]
        plots = [3,100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000]
        
        fig, ax= plt.subplots()
        fig.suptitle("Dataset Graph", fontsize=18)
        ax.set_title("Captured Samples")
        ax.set_xlabel("Samples", fontsize=12)
        ax.set_ylabel("??", fontsize=12)
        ax.plot(input_Values,plots, 'mD:')
        plt.show()
        break
elif uInput1 == 3:
    while uInput1 ==3:
        fi = pd.read_csv("C:\csv\File Injector.CSV")
        
        input_Values = [14,45,77,99,407]
        plots = [10,20,30,40,50,60,70,80,90,100,200,300,400,500]
        
        fig, ax= plt.subplots()
        fig.suptitle("Dataset Graph", fontsize=18)
        ax.set_title("Captured Samples")
        ax.set_xlabel("Samples", fontsize=12)
        ax.set_ylabel("??", fontsize=12)
        ax.plot(input_Values,plots, 'mD:')
        plt.show()
        break
elif uInput1 == 5:
    while uInput1 == 5:
        pua = pd.read_csv("C:\csv\PUA.CSV")

        input_Values = [11,27,67,92,99,139,529,1004]
        plots = [11,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,1100]

        fig, ax= plt.subplots()
        fig.suptitle("Dataset Graph", fontsize=18)
        ax.set_title("Captured Samples")
        ax.set_xlabel("Samples", fontsize=12)
        ax.set_ylabel("??", fontsize=12)
        ax.plot(input_Values,plots, 'mD:')
        plt.show()
        break
elif uInput1 == 6:
    while uInput1 == 6:
        rw = pd.read_csv("C:\csv\Ransomware.CSV")

        input_Values = [35,67,79,252,356,820,998,3319]
        plots = [35,40,50,60,70,80,90,]

        
        fig, ax= plt.subplots()
        fig.suptitle("Dataset Graph", fontsize=18)
        ax.set_title("Captured Samples")
        ax.set_xlabel("Samples", fontsize=12)
        ax.set_ylabel("??", fontsize=12)
        ax.plot(input_Values,plots, 'mD:')
        plt.show()
        break
elif uInput1 == 7:
    while uInput1 == 7:
        rw2 = pd.read_csv("C:\csv\Riskware.CSV")

        input_Values = [7,15,24,28,36,36,45,46,49,57,58,144,493,721,10229,28512,50073]
        plots = [7,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000]

        fig, ax= plt.subplots()
        fig.suptitle("Dataset Graph", fontsize=18)
        ax.set_title("Captured Samples")
        ax.set_xlabel("Samples", fontsize=12)
        ax.set_ylabel("??", fontsize=12)
        ax.plot(input_Values,plots, 'mD:')
        plt.show()
        break
elif uInput1 == 8:
    while uInput1 == 8:
        sw = pd.read_csv("C:\csv\Scareware.CSV")

        input_Values = [23,126,1332]
        plots = [10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400]

        fig, ax= plt.subplots()
        fig.suptitle("Dataset Graph", fontsize=18)
        ax.set_title("Captured Samples")
        ax.set_xlabel("Samples", fontsize=12)
        ax.set_ylabel("??", fontsize=12)
        ax.plot(input_Values,plots, 'mD:')
        plt.show()
        break
elif uInput1 == 9:
    while uInput1 == 9:
        t = pd.read_csv("C:\csv\Trojan.CSV")

        input_Values = [3,3,5,9,11,11,11,12,15,15,16,24,27,27,28,30,33,33,48,59,59,61,63,85,94,99,112,130,148,157,218,239,360,474,479,652,661,680,1054,1166,3413]
        plots = [3,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,2000,3000,4000]

        fig, ax= plt.subplots()
        fig.suptitle("Dataset Graph", fontsize=18)
        ax.set_title("Captured Samples")
        ax.set_xlabel("Samples", fontsize=12)
        ax.set_ylabel("??", fontsize=12)
        ax.plot(input_Values,plots, 'mD:')
        plt.show()
        break
elif uInput1 == 10:
    while uInput1:
        tb = pd.read_csv("C:\csv\Trojan-Banker.CSV")

        input_Values= [4,8,9,17,40,52,56,68,256,260]
        plots = [4,10,20,30,40,50,60,70,80,90,100,200,300]

        fig, ax= plt.subplots()
        fig.suptitle("Dataset Graph", fontsize=18)
        ax.set_title("Captured Samples")
        ax.set_xlabel("Samples", fontsize=12)
        ax.set_ylabel("??", fontsize=12)
        ax.plot(input_Values,plots, 'mD:')
        plt.show()
elif uInput1 == 11:
    while uInput1 ==11:
        td = pd.read_csv("C:\csv\Trojan-Dropper.CSV")

        input_Values = [16,31,51,84,106,118,500,1296]
        plots = [16,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300]

        fig, ax= plt.subplots()
        fig.suptitle("Dataset Graph", fontsize=18)
        ax.set_title("Captured Samples")
        ax.set_xlabel("Samples", fontsize=12)
        ax.set_ylabel("??", fontsize=12)
        ax.plot(input_Values,plots, 'mD:')
        plt.show()
        break
elif uInput1 == 12:
    while uInput1 ==12:
        tsms = pd.read_csv("C:\csv\Trojan-Sms.CSV")

        input_Values = [13,13,20,21,40,42,56,87,186,368,2148]
        plots = [13,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,2000,3000]

        fig, ax= plt.subplots()
        fig.suptitle("Dataset Graph", fontsize=18)
        ax.set_title("Captured Samples")
        ax.set_xlabel("Samples", fontsize=12)
        ax.set_ylabel("??", fontsize=12)
        ax.plot(input_Values,plots, 'mD:')
        plt.show()
        break
elif uInput1 == 13:
    while uInput1 ==13:
        tspy = pd.read_csv("C:\csv\Trojan-Spy.CSV")

        input_Values = [1,13,19,21,27,29,48,52,208,1058,1873]
        plots = [1,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,2000]
        
        fig, ax= plt.subplots()
        fig.suptitle("Dataset Graph", fontsize=18)
        ax.set_title("Captured Samples")
        ax.set_xlabel("Samples", fontsize=12)
        ax.set_ylabel("??", fontsize=12)
        ax.plot(input_Values,plots, 'mD:')
        plt.show()
        break

elif uInput1 == 14:
    while uInput1 ==14:
        bd = pd.read_csv("C:\csv\Backdoor.CSV")

        input_Values = [15,24,24,48,50,119,129,166,171,664]
        plots = [15,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700]

        fig, ax= plt.subplots()
        fig.suptitle("Dataset Graph", fontsize=18)
        ax.set_title("Captured Samples")
        ax.set_xlabel("Samples", fontsize=12)
        ax.set_ylabel("??", fontsize=12)
        ax.plot(input_Values,plots, 'mD:')
        plt.show()
        break





    

