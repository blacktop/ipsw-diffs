## com.apple.AGXG13G

> `com.apple.AGXG13G`

```diff

   __TEXT.__const: 0x26e4
   __TEXT.__os_log: 0x126a
-  __TEXT.__cstring: 0xdced
-  __TEXT_EXEC.__text: 0xb84f8
-  __TEXT_EXEC.__auth_stubs: 0x1a80
+  __TEXT.__cstring: 0xdd24
+  __TEXT_EXEC.__text: 0xb8724
+  __TEXT_EXEC.__auth_stubs: 0x1a50
   __DATA.__data: 0x21f0
   __DATA.__common: 0x10
   __DATA.__bss: 0x4428

   __DATA_CONST.__const: 0x15b58
   __DATA_CONST.__kalloc_type: 0x2140
   __DATA_CONST.__kalloc_var: 0x2850
-  __DATA_CONST.__auth_got: 0xd40
+  __DATA_CONST.__auth_got: 0xd28
   __DATA_CONST.__got: 0x268
   Functions: 2843
-  Symbols:   5675
-  CStrings:  1805
+  Symbols:   5672
+  CStrings:  1808
 
Sections:
~ __TEXT.__const : content changed
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ __ZZN14AGXAccelerator16freeContextIDLUTEvE22kalloc_type_view_13927
+ __ZZN14AGXAccelerator22initializeContextIDLUTEvE22kalloc_type_view_13910
+ __ZZN9AGXShared11clientCloseEvE20kalloc_type_view_428
+ __ZZN9AGXShared32performanceCounterSamplerControlEP28AGXSPerfCtrSamplerControlRecS1_E20kalloc_type_view_813
- __ZN11IOGPUDevice21lockResourceNamespaceEv
- __ZN11IOGPUDevice23unlockResourceNamespaceEv
- __ZNK14IOGPUNamespace18retainObjectLockedEj
- __ZZN14AGXAccelerator16freeContextIDLUTEvE22kalloc_type_view_13909
- __ZZN14AGXAccelerator22initializeContextIDLUTEvE22kalloc_type_view_13892
- __ZZN9AGXShared11clientCloseEvE20kalloc_type_view_404
- __ZZN9AGXShared32performanceCounterSamplerControlEP28AGXSPerfCtrSamplerControlRecS1_E20kalloc_type_view_789
Functions:
~ __ZN14AGXAccelerator5startEP9IOService : 26052 -> 26060
~ __ZN14AGXAccelerator21populatePerfStateInfoILj16ELj2EEEbP9IOService14AGXClockDomainR13PerfStateInfoIXT_EXT0_EE : 1152 -> 1144
~ __ZN14AGXAccelerator14notifyFirmwareEjbb : 268 -> 368
~ __ZN15AGXCommandQueue20processTimestampListERK24AGXHardwareKernelCommandP18AGXAllocationList2P20AGXCommandDescriptorP36AGXCommandTimestampListDescriptorRecjjPK24AGXTimestampListEntryRec : 1848 -> 1772
~ __ZN19AGXEnergyAttributor4freeEv : 416 -> 404
~ __ZN11AGXFirmware27initPowerAndPerformanceDataEv : 1976 -> 1972
~ __ZN11AGXFirmware16initFirmwareDataEv : 4452 -> 4384
~ __ZN14AGXArmFirmware34updateDisplayPowerManagementParamsEyy : 380 -> 372
~ __ZN14AGXArmFirmware27getMTRSensorPTDOverrideMaskEv : 20 -> 16
~ __ZN14AGXArmFirmware24setMTRSensorPTDOverridesEjjyy : 224 -> 220
~ __ZN14AGXArmFirmware19setDPEImaxReactCtrlEy : 20 -> 24
~ __ZN14AGXArmFirmware18setDPEImaxPredCtrlEy : 20 -> 24
~ __ZN14AGXArmFirmware12setDPEACCtrlEy : 20 -> 24
~ __ZN14AGXArmFirmware18setDPETrigSteeringEy : 20 -> 24
~ __ZN14AGXArmFirmware19setDPECSwitchBudgetEy : 20 -> 24
~ __ZN14AGXArmFirmware14setDPESLConfigEy : 20 -> 24
~ __ZN14AGXArmFirmware12setDPEACDthrEty : 148 -> 152
~ __ZN14AGXArmFirmware13setDPEACDshftEty : 148 -> 152
~ __ZN14AGXArmFirmware24recomputeGPUDPEPPTValuesEy : 464 -> 472
~ __ZN14AGXArmFirmware27initPowerAndPerformanceDataEv : 10920 -> 10944
~ __ZN14AGXArmFirmware4initEP14AGXAccelerator : 988 -> 1032
~ __ZN22AGXParameterManagement15growImmediatelyEv : 884 -> 852
~ __ZN11AGXResource10initializeEP11IOGPUDeviceP20IOGPUNewResourceArgsy : 3620 -> 3604
~ __ZN9AGXShared16set_app_gpu_roleEi13eIOGPUAppRole : 1312 -> 1308
~ __ZN13AGXKTelemetry4initEP14AGXAcceleratorP10IOWorkLoop : 568 -> 572
~ __ZN13AGXKTelemetry15periodicCollectEP18IOTimerEventSource : 1328 -> 1900
CStrings:
+ "121111122"
+ "3.44.10"
+ "Jun 30 2026 21:11:58"
+ "com.apple.agx.thmcounters"
+ "sfe_tier3"
+ "thm_activations"
- "1211111"
- "3.44.9"
- "Jun 16 2026 22:07:00"

```
