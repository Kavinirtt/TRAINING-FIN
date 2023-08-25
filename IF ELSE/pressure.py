sys_p=int(input("sys_p"))
dia_p=int(input("dia_p"))
if(sys_p<120 and dia_p<80):
    print("Normal")
elif((sys_p>=120 and sys_p<=129) and (dia_p<80)):
    print("elevated")
elif((sys_p>=130 and sys_p<=139) and (dia_p>=80 and dia_p<=89)):
    print("stage 1 hypertension")
else:
    print("stage 2 hypertension")
    