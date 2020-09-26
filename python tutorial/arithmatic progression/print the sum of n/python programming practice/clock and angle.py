t=int(input("enter the number: "))
while t!=0:
    h=int(input("enter the hour time: "))
    m=int(input("enter the minutes time: "))
    hour_angle=(h*60+m)*1/2
    minute_angle=6*m
    net_angle=hour_angle-minute_angle
    if net_angle<360-net_angle and net_angle>0:
        print(net_angle)
    else:
        print(360-net_angle)
    t=t-1