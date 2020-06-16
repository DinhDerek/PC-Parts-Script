from newegg_search import newegg_search
from microcenter_search import microcenter_search
#from amazon_search import amazon_search
from PC import PC
while True:
    preset_number = input("Welcome to PC-Pair!\nPlease select one of the following preset numbers to generate a parts list (Type 'quit' to quit the program):\n[1] ($600)\n[2] ($800)\n[3] ($1000)\n[4] ($1400)\n[5] ($1900)\n>")
    if preset_number.lower().rsplit() == "quit":
        quit_program = True
        break
    elif preset_number in ['1', '2', '3', '4', '5']:
        quit_program = False
        break
    else:
        print("That is not a valid preset number, please try again!")

if quit_program != True: 
    if preset_number == '1':
        CPU = ('AMD Ryzen 3 3300X', 129.99)
        cpu_cooler = None
        GPU = [('EVGA GeForce GTX 1650 SUPER SC ULTRA GAMING', 189.99), ('MSI GeForce GTX 1650 SUPER Gaming X', 189.99), ('GIGABYTE GeForce GTX 1650 SUPER WINDFORCE OC', 169.99)]
        motherboard = ('GIGABYTE B450M DS3H', 72.99)
        ram = [('G.Skill Ripjaws V 16GB (2 x 8GB) DDR4-3600 PC4-28800 CL16', 79.99), ('Corsair Vengeance LPX 16GB (2 x 8GB) DDR4-3200', 75.99), 'TeamGroup Team T-Force Delta RGB 16GB (2 x 8GB) DDR4-3200', 74.99]
        storage_1 = [('SanDisk SSD PLUS 120GB', 49.99),('Inland Professional 120GB SSD', 24.99)]
        storage_2 = ('WD Blue 1TB Hard Drive', 49.99)
        PSU = ('EVGA 500 W1 100-W1-0500-KR 80+ WHITE', 49.99)
        case = [('NZXT H510', 69.99), ('Phanteks P300 Eclipse', 69.99), ('Corsair 110R', 64.99)] 
    elif preset_number == '2':
        CPU = ('AMD Ryzen 3 3300X', 129.99)
        cpu_cooler = None
        GPU = [('EVGA GeForce GTX 1660 SUPER SC ULTRA GAMING', 264.99), ('MSI GeForce GTX 1660 SUPER VENTUS XS OC', 239.99), ('Gigabyte GeForce GTX 1660 Super', 249.99)]
        motherboard = ('GIGABYTE B450M DS3H', 72.99)
        ram = [('G.Skill Ripjaws V 16GB (2 x 8GB) DDR4-3600 PC4-28800 CL16', 79.99), ('Corsair Vengeance LPX 16GB (2 x 8GB) DDR4-3200', 75.99), 'TeamGroup Team T-Force Delta RGB 16GB (2 x 8GB) DDR4-3200', 74.99]
        storage_1 = [('Intel 660P 1TB SSD', 119.99), ('WD Blue M.2 1TB SSD', 114.99)]
        storage_2 = None
        PSU = ('EVGA 500 W1 100-W1-0500-KR 80+ WHITE', 49.99)
        case = [('NZXT H510', 69.99), ('Phanteks P300 Eclipse', 69.99), ('Corsair 110R', 64.99)] 
    elif preset_number == '3':
        CPU = ('AMD Ryzen 5 3600', 159.99)
        cpu_cooler = None
        GPU = [('EVGA GeForce RTX 2060 SUPER SC ULTRA GAMING', 419.99), ('MSI GeForce RTX 2060 SUPER DirectX 12 RTX 2060 SUPER GAMING X', 429.99), ('GIGABYTE GeForce RTX 2060 Super WINDFORCE OC', 399.99)]
        motherboard = ('GIGABYTE B450M DS3H', 72.99)
        ram = [('G.Skill Ripjaws V 16GB (2 x 8GB) DDR4-3600 PC4-28800 CL16', 79.99), ('Corsair Vengeance LPX 16GB (2 x 8GB) DDR4-3200', 76.99), ('TeamGroup Team T-Force Delta RGB 16GB (2 x 8GB) DDR4-3200', 74.99)]
        storage_1 = [('Intel 660P 1TB SSD', 119.99), ('WD Blue M.2 1TB SSD', 114.99)]
        storage_2 = None
        PSU = ('EVGA 500 W1 100-W1-0500-KR 80+ WHITE', 49.99)
        case = [('NZXT H510', 69.99), ('Phanteks P300 Eclipse', 69.99), ('Corsair 110R', 64.99)] 
    elif preset_number == '4':
        CPU = ('AMD Ryzen 5 3600', 159.99)
        cpu_cooler = ('bequiet Dark Rock Pro 4', 89.90)
        GPU = [('EVGA GeForce RTX 2070 SUPER KO GAMING', 519.99), ('MSI GAMING X RTX 2070 SUPER', 549.99), ('GIGABYTE GeForce RTX 2070 Super GAMING OC 3X', 549.99)]
        motherboard = ('GIGABYTE B450M DS3H', 72.99)
        ram = [('F4-3600C18D-16GTZRX ', 92.99), ('CORSAIR Vengeance RGB Pro 16GB (2 x 8GB) 288-Pin DDR4 SDRAM DDR4 3600', 99.99)]
        storage_1 = [('Intel 660P 1TB SSD', 119.99), ('WD Blue M.2 1TB SSD', 114.99)]
        storage_2 = ('Seagate Barracuda 2TB', 54.99)
        PSU = [('Seasonic FOCUS Plus Gold 750W', 129.94), ('Seasonic FOCUS Plus Gold 650W', 114.99)]
        case = [('Fractal Design Meshify C', 99.99), ('Corsair 220T', 99.99), ('NZXT H510', 69.99)]
    elif preset_number == '5':
        CPU = ('AMD Ryzen 7 3700X', 274.99)
        cpu_cooler = [('NZXT Kraken X63', 149.99), ('bequiet Dark Rock Pro 4', 89.90)]
        GPU = [('EVGA GeForce RTX 2080 SUPER BLACK GAMING', 719.99), ('MSI GeForce RTX 2080 SUPER VENTUS XS OC', 729.99), ('GIGABYTE GeForce RTX 2080 SUPER GAMING OC', 739.99)]
        motherboard = ('MSI B450 TOMAHAWK MAX', 114.99)
        ram = [('G.SKILL Trident Z Neo (2 x 16GB) 3600', 159.99), ('CORSAIR Vengeance LPX 32GB (2 x 16GB) 3600', 157.99), ('F4-3600C16D-32GVKC', 139.99)]
        storage_1 = [('Sabrent Rocket Q 1TB NVMe SSD', 129.99), ('Intel 660P 1TB SSD', 119.99), ('WD Blue M.2 1TB SSD', 114.99)]
        storage_2 = ('Seagate Barracuda 2TB', 54.99)
        PSU = [('Seasonic FOCUS Plus Gold 750W', 129.94), ('Seasonic FOCUS Plus Gold 650W', 114.99)]
        case = [('Lian Li PC-O11 Dynamic', 139.99), ('NZXT H710', 139.99), ('Fractal Design Meshify C', 99.99)]

    newPC = PC(CPU, cpu_cooler, GPU, motherboard, ram, storage_1, storage_2, PSU, case)

cpu_list = [microcenter_search(newPC.getCPU()[0]), newegg_search(newPC.getCPU()[0])]
cpu_list = [cpu for cpu in cpu_list if cpu[0] != -1.0 and cpu[0] <= (CPU[1] * 1.15)]
if len(cpu_list) == 0:  #If all vendors don't have the cpu in stock
    print("No viable CPUs in stock!\n")
else:
    best_cpu = min(cpu_list, key = lambda x : x[0])
    print("CPU: " + best_cpu[2] + "\n     " + best_cpu[1] + "\n     $" + str(best_cpu[0]) + "\n") 

if cpu_cooler != None:
    cooler_index = 0
    for cooler in newPC.getCooler():
        cooler_list = [microcenter_search(cooler[0]), newegg_search(cooler[0])]
        cooler_list = [cooler for cooler in cooler_list if cooler[0] != -1.0 and cooler[0] <= (cpu_cooler[cooler_index][1] * 1.15)]
        if len(cooler_list) > 0:
            best_cooler = min(cooler_list, key = lambda x : x[0])
            print("CPU Cooler: " + best_cooler[2] + "\n     " + best_cooler[1] + "\n     $" + str(best_cooler[0]) + "\n")      
            break
        cooler_index += 1
    print(cooler_index)
    if cooler_index > len(cooler):   
        print("No viable CPU Coolers in stock!\n")

mobo_list = [microcenter_search(newPC.getMobo()[0]), newegg_search(newPC.getMobo()[0])]
mobo_list = [mobo for mobo in mobo_list if mobo[0] != -1.0 and mobo[0] <= (motherboard[1] * 1.15)]
if len(mobo_list) == 0:
    print("No viable Motherboards in stock!\n")
else:
    best_mobo = min(mobo_list, key = lambda x : x[0])
    print("Motherboard: " + best_mobo[2] + "\n     " + best_mobo[1] + "\n     $" + str(best_mobo[0]) + "\n") 

ram_index = 0
for ram in newPC.getRam():
    ram_list = [microcenter_search(ram[0]), newegg_search(ram[0])]
    ram_list = [ram for ram in ram_list if ram[0] != -1.0 and ram[0] <= (ram[ram_index][1] * 1.15)]
    if len(ram_list) > 0:
        best_ram = min(ram_list, key = lambda x : x[0])
        print("RAM: " + best_ram[2] + "\n     " + best_ram[1] + "\n     $" + str(best_ram[0]) + "\n")      
        break
    ram_index += 1
if ram_index > len(ram):   
    print("No viable RAM in stock!\n")