'''
This file contains the PC class 
'''

class PC:
    def __init__(self, CPU, cpu_cooler, GPU, motherboard, ram, storage_1, storage_2, PSU, case):
        self._cpu = CPU
        self._cpuCooler = cpu_cooler
        self._gpu = GPU
        self._motherboard = motherboard
        self._ram = ram
        self._storage1 = storage_1
        self._storage2 = storage_2
        self._psu = PSU
        self._case = case
    
    def getCPU(self):
        return self._cpu

    def getCooler(self):
        return self._cpuCooler
    
    def getGPU(self):
        return self._gpu
    
    def getMobo(self):
        return self._motherboard

    def getRam(self):
        return self._ram
    
    def getStorage1(self):
        return self._storage1

    def getStorage2(self):
        return self._storage2
    
    def getPSU(self):
        return self._psu
    
    def getCase(self):
        return self._case
