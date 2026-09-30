## com.apple.driver.ApplePMGR

> `com.apple.driver.ApplePMGR`

```diff

-  __TEXT.__cstring: 0xfec7
+  __TEXT.__cstring: 0xfedb
   __TEXT.__const: 0x290
-  __TEXT_EXEC.__text: 0x63b2c
+  __TEXT_EXEC.__text: 0x63d60
   __TEXT_EXEC.__auth_stubs: 0x820
   __DATA.__data: 0x138
   __DATA.__common: 0x5e0

   __DATA_CONST.__auth_got: 0x410
   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 2875
-  Symbols:   3697
-  CStrings:  1801
+  Functions: 2876
+  Symbols:   3698
+  CStrings:  1802
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ __ZZN9ApplePMGR10_initPMPv2EvE22kalloc_type_view_10027
+ __ZZN9ApplePMGR10_initPMPv2EvE22kalloc_type_view_10100
+ __ZZN9ApplePMGR10_initPMPv2EvE22kalloc_type_view_10109
+ __ZZN9ApplePMGR10_initPMPv2EvE22kalloc_type_view_10113
+ __ZZN9ApplePMGR15_initGenericPTDEvE21kalloc_type_view_9981
+ __ZZN9ApplePMGR19_initPerfCountersV1EP9IOServiceE22kalloc_type_view_16736
+ __ZZN9ApplePMGR19_initPerfCountersV1EP9IOServiceE22kalloc_type_view_16764
+ __ZZN9ApplePMGR19_initPerfCountersV1EP9IOServiceE22kalloc_type_view_16807
+ __ZZN9ApplePMGR19_initPerfCountersV1EP9IOServiceE22kalloc_type_view_16871
+ __ZZN9ApplePMGR19_initPerfCountersV2EP9IOServiceE22kalloc_type_view_17512
+ __ZZN9ApplePMGR19_initPerfCountersV2EP9IOServiceE22kalloc_type_view_17529
+ __ZZN9ApplePMGR24_initFreeRunningCountersEP9IOServiceE22kalloc_type_view_17720
+ __ZZN9ApplePMGR32_pmpWriteDashBoardSetDeviceStateEtjjE22kalloc_type_view_10471
- __ZZN9ApplePMGR10_initPMPv2EvE22kalloc_type_view_10004
- __ZZN9ApplePMGR10_initPMPv2EvE22kalloc_type_view_10077
- __ZZN9ApplePMGR10_initPMPv2EvE22kalloc_type_view_10086
- __ZZN9ApplePMGR10_initPMPv2EvE22kalloc_type_view_10090
- __ZZN9ApplePMGR15_initGenericPTDEvE21kalloc_type_view_9958
- __ZZN9ApplePMGR19_initPerfCountersV1EP9IOServiceE22kalloc_type_view_16713
- __ZZN9ApplePMGR19_initPerfCountersV1EP9IOServiceE22kalloc_type_view_16741
- __ZZN9ApplePMGR19_initPerfCountersV1EP9IOServiceE22kalloc_type_view_16784
- __ZZN9ApplePMGR19_initPerfCountersV1EP9IOServiceE22kalloc_type_view_16848
- __ZZN9ApplePMGR19_initPerfCountersV2EP9IOServiceE22kalloc_type_view_17489
- __ZZN9ApplePMGR19_initPerfCountersV2EP9IOServiceE22kalloc_type_view_17506
- __ZZN9ApplePMGR24_initFreeRunningCountersEP9IOServiceE22kalloc_type_view_17697
- __ZZN9ApplePMGR32_pmpWriteDashBoardSetDeviceStateEtjjE22kalloc_type_view_10448
Functions:
~ __ZN9ApplePMGR10initDriverEP9IOService : 32108 -> 32560
~ __ZN9ApplePMGR26_recordFrCountersAwakeExitEv : 256 -> 300
+ __ZN9ApplePMGR18pmHibernationStateEv
~ __ZN9ApplePMGR32_checkUpdateFrCountersAwakeEntryEv : 260 -> 292
~ __ZN9ApplePMGR9quiesceHWEv : 1228 -> 1248
~ __ZN9ApplePMGR9restoreHWEb : 1056 -> 1080
- __ZN9ApplePMGR18pmHibernationStateEv
~ __ZN9ApplePMGR15configMiscCoresEyb : 1832 -> 1828
~ __ZN9ApplePMGR12_getDeviceIDENS_6RegMapEj : 164 -> 172
~ __ZN9ApplePMGR18getDeviceIDFromRegENS_6RegMapEj : 176 -> 144
~ __ZN9ApplePMGR17_normalizedUptimeEhj : 280 -> 224
~ __ZN9ApplePMGR23_snapshotPerfCountersV2Eb : 748 -> 764
~ __ZN9ApplePMGR29_waitForPMPReadyActionGatedv2Ej : 792 -> 812
~ __ZN9ApplePMGR16_getPMPDevHandleEP8OSSymbolPj : 560 -> 572
~ __ZN9ApplePMGR12_getPTDIndexEPKc : 136 -> 156
~ __ZN9ApplePMGR37_pmpWriteDashBoardSetDeviceConstraintEjjyj : 904 -> 916
~ __ZN9ApplePMGR15_findDVFSDomainEP8OSSymbol : 516 -> 504
~ __ZN9ApplePMGR16_getPTDRangeInfoEjPN12ApplePMGRNub12PTDRangeInfoEPj : 172 -> 140
~ __ZN9ApplePMGR16_getDeviceEnergyEtj : 1700 -> 1724
~ __ZN9ApplePMGR23_syncDeviceStatusChangeEPNS_22DeviceStatusChangeDataEj : 2880 -> 2860
~ __ZN9ApplePMGR26_updateCPUComplexPerfStateEPNS_10CPUComplexEhbh : 1184 -> 1200
~ __ZN9ApplePMGR23_handlePerfStateRequestEjhj : 664 -> 672
~ __ZN9ApplePMGR14roscDataUpdateEhPK8RoscDatabj : 460 -> 404
~ __ZN9ApplePMGR11roscDataGetEhP8RoscDataj : 292 -> 276
~ __ZN9ApplePMGR24getPmpDVFSPerfStateCountEj : 92 -> 80
~ __ZN9ApplePMGR19_getCIOClusterIndexEj : 112 -> 100
~ __ZN9ApplePMGR21updateDie1CPUVoltagesEv : 3196 -> 3204
~ __ZN11ApplePMGRv216_cpuTopologyInitEv : 572 -> 580
~ __ZN8ApplePMC10_getRailIDEPKc : 144 -> 164
~ __ZN8ApplePMC12getBWRMemoryEjPy : 232 -> 240
~ __ZN8ApplePMC14getBoostMemoryEtPy : 224 -> 232
~ _ZN9ApplePMGR23_snapshotPerfCountersV2Eb.cold.2 : 44 -> 56
+ _ZN9ApplePMGR24_saveBridgeEventCountersEhj.cold.3
CStrings:
+ "(SInt64) upTime > 0"

```
