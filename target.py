class target:
    def __init__(self, ip_adress, OS, port):
        self.targetIP_adress = ip_adress
        self.targetOS = OS
        self.targetPort = port
        self.targetStatus = "Safe"
    def Scan(self): 
        if self.targetPort == 80:
            print("The device is hacked")
            self.targetStatus = "Hacked"
        else :
            print("The divice is safe")


t1 =target("120.0.32.2", "windows", 80)
t2 =target("120.0.32.3", "MACOS", 443)
t3 =target("120.0.32.4", "linux", 80)

t1.Scan()
t2.Scan()
t3.Scan()


all_targets = [t1, t2, t3]
for scan in all_targets:
    print(f"ip adress : {scan.targetIP_adress} | Status : {scan.targetStatus} | OS :{scan.targetOS}")
    