## com.apple.driver.AppleDCP

> `com.apple.driver.AppleDCP`

```diff

-1041.80.55.0.0
+1041.100.93.0.0
   __TEXT.__cstring: 0x1b49
   __TEXT.__const: 0x2d
-  __TEXT_EXEC.__text: 0x7edc
+  __TEXT_EXEC.__text: 0x7390
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xb0

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x14c8
   __DATA_CONST.__kalloc_type: 0x100
-  UUID: 3F4346CD-4501-3FA1-AE18-A2BCDEB07D27
+  UUID: 2C2A4C6B-7D47-375C-A84F-CD041109CA41
   Functions: 200
   Symbols:   0
   CStrings:  154
Functions:
~ __ZN12PMGRDispCtrl5startEP9IOService : 220 -> 212
~ sub_fffffe00090a0c54 -> sub_fffffe00088971dc : 84 -> 80
~ sub_fffffe00090a0ca8 -> sub_fffffe000889722c : 320 -> 304
~ sub_fffffe00090a1304 -> sub_fffffe0008897878 : 32 -> 28
~ __ZN13DCPEndpointV25startEP9IOService : 356 -> 340
~ sub_fffffe00090a187c -> sub_fffffe0008897ddc : 124 -> 112
~ sub_fffffe00090a18f8 -> sub_fffffe0008897e4c : 144 -> 136
~ __ZN13DCPEndpointV213setPowerStateEmP9IOService : 520 -> 504
~ sub_fffffe00090a1b98 -> sub_fffffe00088980d4 : 36 -> 32
~ sub_fffffe00090a1bc8 -> sub_fffffe0008898100 : 32 -> 28
~ __ZN14AppleDCPExpert5startEP9IOService : 5440 -> 4740
~ sub_fffffe00090a3444 -> sub_fffffe00088996bc : 292 -> 276
~ sub_fffffe00090a35c4 -> sub_fffffe000889982c : 156 -> 140
~ __ZN14AppleDCPExpert20_initHealthTelemetryEv : 1780 -> 1556
~ ____ZN14AppleDCPExpert5startEP9IOService_block_invoke : 248 -> 220
~ sub_fffffe00090a3fdc -> sub_fffffe000889a138 : 316 -> 296
~ sub_fffffe00090a41b8 -> sub_fffffe000889a300 : 200 -> 176
~ sub_fffffe00090a4280 -> sub_fffffe000889a3b0 : 512 -> 408
~ sub_fffffe00090a4480 -> sub_fffffe000889a548 : 592 -> 500
~ sub_fffffe00090a46d0 -> sub_fffffe000889a73c : 380 -> 364
~ sub_fffffe00090a4990 -> sub_fffffe000889a9ec : 168 -> 132
~ sub_fffffe00090a4a38 -> sub_fffffe000889aa70 : 204 -> 180
~ __ZN14AppleDCPExpert19_setPowerStateGatedEPmP9IOService : 2244 -> 1900
~ sub_fffffe00090a54a0 -> sub_fffffe000889b368 : 184 -> 176
~ sub_fffffe00090a55fc -> sub_fffffe000889b4bc : 264 -> 244
~ __ZN14AppleDCPExpert28_changeDCPPowerStateInternalE13DCPPowerState : 952 -> 920
~ sub_fffffe00090a5abc -> sub_fffffe000889b948 : 204 -> 188
~ __ZN14AppleDCPExpert23_setDCPExpertPowerStateE13DCPPowerStateS0_ : 504 -> 488
~ sub_fffffe00090a5f08 -> sub_fffffe000889bd74 : 352 -> 300
~ ____ZN14AppleDCPExpert22_initEndpointInterfaceEP9IOService_block_invoke_2 : 208 -> 200
~ __ZN14AppleDCPExpert20_GAPFInterruptDirectEP28IOFilterInterruptEventSource : 488 -> 428
~ sub_fffffe00090a662c -> sub_fffffe000889c420 : 192 -> 184
~ __ZN14AppleDCPExpert20_failSafeStatsToDictEP18HealthMonitorStats : 816 -> 684
~ sub_fffffe00090a6a1c -> sub_fffffe000889c784 : 184 -> 176
~ sub_fffffe00090a6ad4 -> sub_fffffe000889c834 : 176 -> 168
~ sub_fffffe00090a6c08 -> sub_fffffe000889c960 : 12 -> 32
~ sub_fffffe00090a6c14 -> sub_fffffe000889c980 : 16 -> 28
~ sub_fffffe00090a6c30 -> sub_fffffe000889c9a8 : 12 -> 16
~ sub_fffffe00090a6c3c -> sub_fffffe000889c9b8 : 12 -> 28
~ sub_fffffe00090a6d04 -> sub_fffffe000889ca90 : 164 -> 156
~ sub_fffffe00090a6de0 -> sub_fffffe000889cb64 : 264 -> 228
~ __ZN14AppleDCPExpert20_serializeDebugStateEPvP11OSSerialize : 916 -> 740
~ sub_fffffe00090a72b4 -> sub_fffffe000889cf64 : 164 -> 160
~ sub_fffffe00090a7358 -> sub_fffffe000889d004 : 148 -> 136
~ __ZN14AppleDCPExpert23_setPowerAssertionGatedEPbP9IOServiceS0_ : 688 -> 624
~ sub_fffffe00090a769c -> sub_fffffe000889d2fc : 108 -> 100
~ __ZN14AppleDCPExpert21_submitTelemetryGatedEb : 1400 -> 1292
~ sub_fffffe00090a7c80 -> sub_fffffe000889d86c : 56 -> 44
~ sub_fffffe00090a7cb8 -> sub_fffffe000889d898 : 56 -> 44
~ sub_fffffe00090a7cf0 -> sub_fffffe000889d8c4 : 56 -> 44
~ sub_fffffe00090a7d28 -> sub_fffffe000889d8f0 : 56 -> 44
~ __ZN14AppleDCPExpert5startEP9IOService.cold.5 : 56 -> 44
~ __ZN14AppleDCPExpert5startEP9IOService.cold.6 : 104 -> 96
~ __ZN14AppleDCPExpert5startEP9IOService.cold.7 : 56 -> 44
~ __ZN14AppleDCPExpert5startEP9IOService.cold.8 : 56 -> 44
~ __ZN14AppleDCPExpert5startEP9IOService.cold.9 : 56 -> 44
~ __ZN14AppleDCPExpert5startEP9IOService.cold.10 : 56 -> 44
~ __ZN14AppleDCPExpert5startEP9IOService.cold.11 : 56 -> 44
~ __ZN14AppleDCPExpert5startEP9IOService.cold.12 : 56 -> 44
~ __ZN14AppleDCPExpert5startEP9IOService.cold.13 : 56 -> 44
~ __ZN14AppleDCPExpert5startEP9IOService.cold.14 : 56 -> 44
~ __ZN14AppleDCPExpert5startEP9IOService.cold.15 : 56 -> 44
~ __ZN14AppleDCPExpert5startEP9IOService.cold.16 : 56 -> 44
~ __ZN14AppleDCPExpert5startEP9IOService.cold.17 : 56 -> 44
~ __ZN14AppleDCPExpert5startEP9IOService.cold.18 : 56 -> 44
~ sub_fffffe00090a80cc -> sub_fffffe000889dbe4 : 56 -> 44
~ sub_fffffe00090a8104 -> sub_fffffe000889dc10 : 56 -> 40
~ sub_fffffe00090a813c -> sub_fffffe000889dc38 : 56 -> 40
~ sub_fffffe00090a8174 -> sub_fffffe000889dc60 : 56 -> 40
~ __ZN14AppleDCPExpert28_setDispSysFePowerGateEnableEb.cold.1 : 56 -> 40
~ __ZN14AppleDCPExpert21_setPMGRScratchRegionEb.cold.1 : 56 -> 40
~ __ZN14AppleDCPExpert11_enterTraceEjPvS0_S0_.cold.1 : 56 -> 40
~ __ZN14AppleDCPExpert28_changeDCPPowerStateInternalE13DCPPowerState.cold.2 : 56 -> 44
~ __ZN14AppleDCPExpert28_changeDCPPowerStateInternalE13DCPPowerState.cold.3 : 56 -> 44
~ __ZN14AppleDCPExpert28_changeDCPPowerStateInternalE13DCPPowerState.cold.4 : 56 -> 44
~ __ZN14AppleDCPExpert28_changeDCPPowerStateInternalE13DCPPowerState.cold.6 : 56 -> 40
~ sub_fffffe00090a83f4 -> sub_fffffe000889de6c : 120 -> 108
~ sub_fffffe00090a846c -> sub_fffffe000889ded8 : 108 -> 96
~ sub_fffffe00090a84d8 -> sub_fffffe000889df38 : 96 -> 88
~ sub_fffffe00090a8538 -> sub_fffffe000889df90 : 108 -> 96
~ sub_fffffe00090a871c -> sub_fffffe000889e168 : 112 -> 104

```
