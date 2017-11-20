[FileHeader]
FileID       = 6fa6a751-4df3-4e0d-9e5e-12e05765ada4
Name         = TestCase1_Solid_Flow_1
Date         = 10/26/17 16:54:08
Type         = PRO
CreateBy     = Moldex3D Process Wizard
Remark       = 

[CaeHeader]
Version      = Moldex3D
Release      = 14 (2015)
Project      = C:\WorkingFolder\testCase\TestCase1_Solid_Flow\
Engineer     =
Parent       = None
Type         = Injection (Solid)
FileVersion  = 1041 (160.1)
FileType     = 0
SmartSetting = 1
ProjectType  = 0 1
SettingMode  = 1

[Summary]
TotalNdivz       = 6
TotalNodeEM      = 1
TotalNodeEC      = 4
TotalGateCTL     = 2
VacuumIndex      = 0
SkinRatio        = 50
NoOutput         = 0
PEOFasPPack      = 1
TotalNodeMB      = 3
TotalNodeBC      = 2
TotalNodeMMM     = 3
SymVolRatio      = 1
TotalNodeHR      = 2
TotalSTLNodeEC   = 0
TotalSTLNodeHR   = 0
TotalGrpCCL      = 4
TotalGrpCCS      = 0
TotalOverFlowCTL = 0

[Unit]
Time         = sec       Time
Temp         = oC        Temperature
Pres         = MPa       Pressure
FR           = cc/sec    FlowRate
IP           = MPa       InjectionPressure
PP           = MPa       PackPressure
Volume       = cc        Volume

[FlowCTL]
FlowCtrl          = 0
VPSwitchCtrl      = 0
PackingCtrl       = 0
MoldTemperature   = 50
MeltTemperature   = 230
InjectionTime     = 3.5
VolumeFilled      = 98

[Flow-1]
FillTime      = 0.1
MeltTemp      = 230
MoldTemp      = 50
InjectPres    = 155
MaxClampForce = 100000
FRDisplayType = 0
IPDisplayType = 0
FRStrokeMode  = 0
IPStrokeMode  = 0
FRProfileType = 0
IPProfileType = 0
FRSet         = 2
FR-1          = 0	50
FR-2          = 100	50
IPSet         = 2
IP-1          = 0	100
IP-2          = 100	100
UserFRSet     = 1
UserFR-1      = 100	50
UserFR-2      = 0	50
UserIPSet     = 1
UserIP-1      = 100	100
UserIP-2      = 0	100
MachineFlag   = 0
TimeConstFR-1 = 0.01
TimeConstIP-1 = 0.1
MaxFillingTime   = 0.132531
FlowPackMode   = 1
MachineController   = 0
HotRunnerTemperatureDiff = 0

[Pack-1]
PackTime         = 3.4
PackPres         = 155
PackSwch         = 98
IgnoreLimitation = 0
MaxEOFRatio      = 100
PPDisplayType    = 0
PPProfileType    = 0
PPSet            = 6
PP-1             = 0	54
PP-2             = 60	54
PP-3             = 60	43.2
PP-4             = 80	43.2
PP-5             = 80	34.56
PP-6             = 100	34.56
UserPPSet        = 3
UserPP-1         = 100	34.56
UserPP-2         = 80	43.2
UserPP-3         = 60	54
UserPP-4         = 0	54
MaxPressSlop        = 2500
MachineFlag      = 0
TimeConstPP-1    = 0.1
TimeConstPP-2    = 0.1
TimeConstPP-3    = 0.1

[Cool]
CoolTime                   = 11.3
OpenTime                   = 5
EjectTemp                  = 99.85
AirTemp                    = 25
InitialMoldbaseTemperature = 50
CoolantTemp                = 30
CoolantFR                  = 120
CoolingType                = 0
ControlType                = 0

[MoldPreheat]
CoolTime                   = 11.3
OpenTime                   = 5
EjectTemp                  = 99.85
AirTemp                    = 25
InitialMoldbaseTemperature = 50
CoolantTemp                = 30
CoolantFR                  = 120
CoolingType                = 0
ControlType                = 0
MoldPreHeatType                = 0
MoldPreHeatTemperature                = 50
MoldPreHeatTime                = 56.7
MaxMoldPreHeatTime              = 113.5

[CoolCTL]
T-1          = 50
F-1          = 120
P-1          = 5
M-1          = 1
T-2          = 50
F-2          = 120
P-2          = 5
M-2          = 1
T-3          = 230
F-3          = 120
P-3          = 5
M-3          = 3
T-4          = 230
F-4          = 120
P-4          = 5
M-4          = 3

[Coolant]
1 = 1	4.183e+007	59800	0.01006	1	Water	5	2
2 = 1	4.183e+007	59800	0.01006	1	Water	5	1
3 = 230	0	0	0	3	Temp	2	3
4 = 230	0	0	0	3	Temp	2	4

[VarCoolCTL]
CoolantNo    = 8
Coolant-1    = 1	4.183e+007	59800	0.01006	1
Coolant-2    = 0.836	2.25e+007	13800	0.0243	2
Coolant-3    = 0	0	0	0	3
Coolant-4    = 0	0	0	0	4
Coolant-5    = 0	0	0	0	5
Coolant-6    = 0	0	0	0	6
Coolant-7    = 0.001177	1.005e+007	2670	1.843e-005	7
Coolant-8    = 0.796	2.07e+007	13200	0.00148	8

[CoolChannel-1]
Diameter    = 5
GroupID    = 2
TimeSet    = 1
TCP-1    = 0	1	50	120	0

[CoolChannel-2]
Diameter    = 5
GroupID    = 1
TimeSet    = 1
TCP-1    = 0	1	50	120	0

[CoolChannel-3]
Diameter    = 2
GroupID    = 3
TimeSet    = 1
TCP-1    = 0	3	230	120	0

[CoolChannel-4]
Diameter    = 2
GroupID    = 4
TimeSet    = 1
TCP-1    = 0	3	230	120	0

[MPreheat_CoolChannel-1]
Diameter    = 5
GroupID    = 2
TimeSet    = 1
TCP-1    = 0	1	50	120	0

[MPreheat_CoolChannel-2]
Diameter    = 5
GroupID    = 1
TimeSet    = 1
TCP-1    = 0	1	50	120	0

[MPreheat_CoolChannel-3]
Diameter    = 2
GroupID    = 3
TimeSet    = 1
TCP-1    = 0	3	230	120	0

[MPreheat_CoolChannel-4]
Diameter    = 2
GroupID    = 4
TimeSet    = 1
TCP-1    = 0	3	230	120	0

[CoolChannelTemperatureControl]
CoolantNo    = 4
Coolant-1-TimeSet    = 1
Coolant-1-1  = 0	0	0	0	0	0	0	0	0
Coolant-2-TimeSet    = 1
Coolant-2-1  = 0	0	0	0	0	0	0	0	0
Coolant-3-TimeSet    = 1
Coolant-3-1  = 0	0	-100	-200	0	1	0	0	0
Coolant-4-TimeSet    = 1
Coolant-4-1  = 0	0	-100	-200	0	1	0	0	0

[MPreheat_CoolChannelTemperatureControl]
CoolantNo    = 4
Coolant-1  = 0	0	0	0	0	0	0	0
Coolant-2  = 0	0	0	0	0	0	0	0
Coolant-3  = 0	0	-100	-200	0	1	0	0
Coolant-4  = 0	0	-100	-200	0	1	0	0

[GateCTL]
AutoShutOffValveGateEOP = 1
ST-1  = 0
ET-1  = 0
ST-2  = 0
ET-2  = 0

[GateValve-1]
GCId   = 1
GCSet   = 1
GC-1    = 0	1	1

[GateValve-2]
GCId   = 2
GCSet   = 1
GC-1    = 0	1	1

[Project]
Mesh          = SolidInjection_ValveGate_SC.mfe
MeshID        = 63b5a836-9a0a-48a6-8e32-5c49c0140ca5
Material      = ABS_POLYFLAMRABS90950UV5_1.mtr
CavVol        = 0.482849
CushionVol    = 0
ClampFaceArea = 3.13616
HRVol    = 0.119048

[Moldbase]
1 = 7.75	4.62e+006	2.9e+006	P20	2.07e+012	0.3	1.29e-005
2 = 7.75	4.62e+006	2.9e+006	P20	2.07e+012	0.3	1.29e-005
3 = 7.75	4.62e+006	2.9e+006	P20	2.07e+012	0.3	1.29e-005

[MoldMetalMaterial]
1 = 7.835	4.62e+006	3.65e+006	P20	2.07e+012	0.3	1.26e-005
2 = 7.835	4.62e+006	3.65e+006	P20	2.07e+012	0.3	1.26e-005
3 = 7.835	4.62e+006	3.65e+006	P20	2.07e+012	0.3	1.26e-005

[EjectCriteria]
TotalCriteriaNode  = 0
TotalSensorNode    = 41
SensorNode-1      = 44	1
SensorNode-2      = 43	2
SensorNode-3      = 59	3
SensorNode-4      = 87	4
SensorNode-5      = 118	5
SensorNode-6      = 150	6
SensorNode-7      = 182	7
SensorNode-8      = 219	8
SensorNode-9      = 263	9
SensorNode-10      = 310	10
SensorNode-11      = 370	11
SensorNode-12      = 459	12
SensorNode-13      = 600	13
SensorNode-14      = 783	14
SensorNode-15      = 940	15
SensorNode-16      = 1088	16
SensorNode-17      = 1210	17
SensorNode-18      = 1328	18
SensorNode-19      = 1465	19
SensorNode-20      = 1609	20
SensorNode-21      = 1826	21
SensorNode-22      = 1901	22
SensorNode-23      = 2067	23
SensorNode-24      = 2320	24
SensorNode-25      = 2464	25
SensorNode-26      = 2749	26
SensorNode-27      = 2969	27
SensorNode-28      = 3170	28
SensorNode-29      = 3382	29
SensorNode-30      = 3690	30
SensorNode-31      = 3848	31
SensorNode-32      = 3781	32
SensorNode-33      = 3453	33
SensorNode-34      = 3226	34
SensorNode-35      = 3024	35
SensorNode-36      = 2927	36
SensorNode-37      = 2818	37
SensorNode-38      = 2544	38
SensorNode-39      = 2260	39
SensorNode-40      = 2133	40
SensorNode-41      = 2132	41

[PartInsertInitialTemperature]
TotalPartInsert = 2
PartInsert-1    = 5002	Part_Insert_01	30	1
PartInsert-2    = 5003	Part_Insert_02	30	2

[MoldInsertInitialTemperature]
TotalMoldInsert = 2
IfSurfaceHeatON = 1
MoldInsert-1    = 2	MI_02	50	2	0
MoldInsert-2    = 3	MI_01	50	3	0

[SURFACE ELEMENT BOUNDARY CONDITION NAME]
4	TBC1	0
4	TBC2	0
1 = 0	50
1 = 0.1	50
1 = 0.1	50
1 = 3.5	50
2 = 0	50
2 = 0.1	50
2 = 0.1	50
2 = 3.5	50

[AdvancedSetting]
OpenDirection = 0	0	1
ClampForce    = 30

[MoldThermalBoundaryType]
Type          = 2
Flow          = 5000    (W/m^2.K)
Pack          = 25000    (W/m^2.K)
Detached_HTC  = 2500 (W/m^2.K)
HotRunner_HTC = 0 (W/m^2.K)
UserHTC = 0
UserMode = 0 
NuNum = 7.54 
TBCNumber = 2 
TBC1 = 5000	25000 (W/m^2.K)
TBC2 = 5000	25000 (W/m^2.K)
