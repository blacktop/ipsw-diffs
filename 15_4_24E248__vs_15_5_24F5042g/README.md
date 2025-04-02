# 15.4 (24E248) .vs 15.5 (24F5042g)

## IPSWs

- `UniversalMac_15.4_24E248_Restore.ipsw`
- `UniversalMac_15.5_24F5042g_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 15.4 *(24E248)* | 24.4.0 | 11417.101.15~1 | Wed, 19Mar2025 21:12:54 PDT |
| 15.5 *(24F5042g)* | 24.5.0 | 11417.120.80.501.1~2 | Wed, 26Mar2025 22:19:01 PDT |

### Kexts

#### ⬆️ Updated (22)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.driver.AppleAVD`

```diff

 862.0.0.0.0
-  __TEXT.__os_log: 0x15cae
-  __TEXT.__cstring: 0x5473
-  __TEXT.__const: 0xc8c38
-  __TEXT_EXEC.__text: 0x59a98
+  __TEXT.__os_log: 0x14fa6
+  __TEXT.__cstring: 0x5402
+  __TEXT.__const: 0xb61f8
+  __TEXT_EXEC.__text: 0x55a7c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x12dc
   __DATA.__common: 0x78

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x42d8
-  __DATA_CONST.__kalloc_type: 0x2cc0
-  __DATA_CONST.__kalloc_var: 0xf00
-  Functions: 1764
-  Symbols:   4175
-  CStrings:  1571
+  __DATA_CONST.__const: 0x3fe8
+  __DATA_CONST.__kalloc_type: 0x2ac0
+  __DATA_CONST.__kalloc_var: 0xeb0
+  Functions: 1681
+  Symbols:   4019
+  CStrings:  1565
 
Symbols:
- __ZN13CAvdMcpuThyme10receiveCmdEPj
- __ZN13CAvdMcpuThyme12apLogMemBaseEv
- __ZN13CAvdMcpuThyme12apLogMemSizeEv
- __ZN13CAvdMcpuThyme13IsMailboxFullEj
- __ZN13CAvdMcpuThyme16clearRXInterruptEj
- __ZN13CAvdMcpuThyme16clearTXInterruptEj
- __ZN13CAvdMcpuThyme17enableRXInterruptEj
- __ZN13CAvdMcpuThyme17enableTXInterruptEj
- __ZN13CAvdMcpuThyme18disableRXInterruptEj
- __ZN13CAvdMcpuThyme18disableTXInterruptEj
- __ZN13CAvdMcpuThyme23EnableMailboxInterruptsEv
- __ZN13CAvdMcpuThyme5readyEv
- __ZN13CAvdMcpuThyme7sendCmdEjj
- __ZN13CAvdMcpuThymeC1EjP14CAvdRegisterIO
- __ZN13CAvdMcpuThymeC1Ev
- __ZN13CAvdMcpuThymeC2EjP14CAvdRegisterIO
- __ZN13CAvdMcpuThymeC2Ev
- __ZN13CAvdMcpuThymeD0Ev
- __ZN13CAvdMcpuThymeD1Ev
- __ZN13CAvdMcpuThymeD2Ev
- __ZN15CAvdApCommThyme10sendAvdCmdEP10uCAvdCmd20j
- __ZN15CAvdApCommThyme11_m3CmdQueueEj
- __ZN15CAvdApCommThyme11initAvdWrapEv
- __ZN15CAvdApCommThyme12ConfigureDMAEv
- __ZN15CAvdApCommThyme12DMAConfigureEii
- __ZN15CAvdApCommThyme12loadTunablesEb
- __ZN15CAvdApCommThyme12sendAbortCmdEP10uCAvdCmd20
- __ZN15CAvdApCommThyme14receiveMessageERjj
- __ZN15CAvdApCommThyme15mcpuSaveContextEv
- __ZN15CAvdApCommThyme17validateAvcFieldsEPh
- __ZN15CAvdApCommThyme17validateAvxFieldsEPh
- __ZN15CAvdApCommThyme17validateLghFieldsEPh
- __ZN15CAvdApCommThyme18ConfigurePioHdrAvcEv
- __ZN15CAvdApCommThyme18ConfigurePioHdrAvxEv
- __ZN15CAvdApCommThyme18ConfigurePioHdrLghEv
- __ZN15CAvdApCommThyme18mcpuRestoreContextEv
- __ZN15CAvdApCommThyme18validateHevcFieldsEPh
- __ZN15CAvdApCommThyme18waitValidADSStatusEv
- __ZN15CAvdApCommThyme19ConfigurePioHdrHevcEv
- __ZN15CAvdApCommThyme25PrepareM3DecodeCommandAvcEv
- __ZN15CAvdApCommThyme25PrepareM3DecodeCommandAvxEv
- __ZN15CAvdApCommThyme25PrepareM3DecodeCommandLghEv
- __ZN15CAvdApCommThyme25allocateAPCommFrameParamsEv
- __ZN15CAvdApCommThyme25getVPInstrFifoRequirementEPyS0_Pj
- __ZN15CAvdApCommThyme26PrepareM3DecodeCommandHevcEv
- __ZN15CAvdApCommThyme26waitValidADSStatusWithMaskEj
- __ZN15CAvdApCommThymeC1EPvP14CAvdRegisterIO
- __ZN15CAvdApCommThymeC2EPvP14CAvdRegisterIO
- __ZN15CAvdApCommThymeD0Ev
- __ZN15CAvdApCommThymeD1Ev
- __ZN15CAvdApCommThymeD2Ev
- __ZN17CAvdWrapCtrlThyme10DeviceInitEPv
- __ZN17CAvdWrapCtrlThyme11DevicePwrOnEPv
- __ZN17CAvdWrapCtrlThyme11triggerDKeyEv
- __ZN17CAvdWrapCtrlThyme12DevicePwrOffEPv
- __ZN17CAvdWrapCtrlThyme12getAdsStatusEPjS0_S0_S0_
- __ZN17CAvdWrapCtrlThyme13StatusLoggingEi
- __ZN17CAvdWrapCtrlThyme14ReadRegister32Ej
- __ZN17CAvdWrapCtrlThyme15CheckDartStatusEb
- __ZN17CAvdWrapCtrlThyme15CheckMctlStatusEv
- __ZN17CAvdWrapCtrlThyme15WriteRegister32Ejj
- __ZN17CAvdWrapCtrlThyme15getAdsDeviceIdsEPyPtPj
- __ZN17CAvdWrapCtrlThyme16enableMCDataStrmEj
- __ZN17CAvdWrapCtrlThyme17disableMCDataStrmEv
- __ZN17CAvdWrapCtrlThyme32waitForOutstandingAXITransactionEv
- __ZN17CAvdWrapCtrlThyme4IdleEb
- __ZN17CAvdWrapCtrlThyme6HResetEv
- __ZN17CAvdWrapCtrlThyme7getDSIDEv
- __ZN17CAvdWrapCtrlThyme8PwmResetEv
- __ZN17CAvdWrapCtrlThyme9getPmuGTBEPjS0_
- __ZN17CAvdWrapCtrlThyme9getPmuRTCEPjS0_
- __ZN17CAvdWrapCtrlThymeC1EPjP9IOServiceP7AVDDartjy
- __ZN17CAvdWrapCtrlThymeC2EPjP9IOServiceP7AVDDartjy
- __ZN17CAvdWrapCtrlThymeD0Ev
- __ZN17CAvdWrapCtrlThymeD1Ev
- __ZN17CAvdWrapCtrlThymeD2Ev
- __ZN19CPriorityQueueThyme18createApCommObjectEPvP14CAvdRegisterIO
- __ZN19CPriorityQueueThyme25isVPAvailableForDecodeCmdEPhjj
- __ZN19CPriorityQueueThymeC1EPvP14CAvdRegisterIO
- __ZN19CPriorityQueueThymeC2EPvP14CAvdRegisterIO
- __ZN19CPriorityQueueThymeD0Ev
- __ZN19CPriorityQueueThymeD1Ev
- __ZTV13CAvdMcpuThyme
- __ZTV15CAvdApCommThyme
- __ZTV17CAvdWrapCtrlThyme
- __ZTV19CPriorityQueueThyme
- __ZZN13CAvdMcpuThymeC1EvE11_os_log_fmt
- __ZZN13CAvdMcpuThymedlEPvmE20kalloc_type_view_522
- __ZZN13CAvdMcpuThymenwEmE20kalloc_type_view_522
- __ZZN15CAvdApCommThyme10sendAvdCmdEP10uCAvdCmd20jE11_os_log_fmt
- __ZZN15CAvdApCommThyme11initAvdWrapEvE11_os_log_fmt
- __ZZN15CAvdApCommThyme15mcpuSaveContextEvE11_os_log_fmt
- __ZZN15CAvdApCommThyme17validateAvcFieldsEPhE11_os_log_fmt
- __ZZN15CAvdApCommThyme17validateAvcFieldsEPhE11_os_log_fmt_0
- __ZZN15CAvdApCommThyme17validateAvcFieldsEPhE11_os_log_fmt_1
- __ZZN15CAvdApCommThyme17validateAvxFieldsEPhE11_os_log_fmt
- __ZZN15CAvdApCommThyme17validateAvxFieldsEPhE11_os_log_fmt_0
- __ZZN15CAvdApCommThyme17validateAvxFieldsEPhE11_os_log_fmt_1
- __ZZN15CAvdApCommThyme17validateAvxFieldsEPhE11_os_log_fmt_2
- __ZZN15CAvdApCommThyme17validateLghFieldsEPhE11_os_log_fmt
- __ZZN15CAvdApCommThyme17validateLghFieldsEPhE11_os_log_fmt_0
- __ZZN15CAvdApCommThyme17validateLghFieldsEPhE11_os_log_fmt_1
- __ZZN15CAvdApCommThyme18ConfigurePioHdrAvxEvE11_os_log_fmt
- __ZZN15CAvdApCommThyme18validateHevcFieldsEPhE11_os_log_fmt
- __ZZN15CAvdApCommThyme18validateHevcFieldsEPhE11_os_log_fmt_0
- __ZZN15CAvdApCommThyme18validateHevcFieldsEPhE11_os_log_fmt_1
- __ZZN15CAvdApCommThyme18validateHevcFieldsEPhE11_os_log_fmt_2
- __ZZN15CAvdApCommThyme18validateHevcFieldsEPhE11_os_log_fmt_3
- __ZZN15CAvdApCommThyme18validateHevcFieldsEPhE11_os_log_fmt_4
- __ZZN15CAvdApCommThyme19ConfigurePioHdrHevcEvE11_os_log_fmt
- __ZZN15CAvdApCommThyme25PrepareM3DecodeCommandAvxEvE11_os_log_fmt
- __ZZN15CAvdApCommThyme25allocateAPCommFrameParamsEvE11_os_log_fmt
- __ZZN15CAvdApCommThyme26PrepareM3DecodeCommandHevcEvE11_os_log_fmt
- __ZZN15CAvdApCommThyme26waitValidADSStatusWithMaskEjE11_os_log_fmt
- __ZZN15CAvdApCommThyme26waitValidADSStatusWithMaskEjE11_os_log_fmt_0
- __ZZN15CAvdApCommThyme26waitValidADSStatusWithMaskEjE11_os_log_fmt_1
- __ZZN15CAvdApCommThyme26waitValidADSStatusWithMaskEjE11_os_log_fmt_2
- __ZZN15CAvdApCommThyme26waitValidADSStatusWithMaskEjE11_os_log_fmt_3
- __ZZN15CAvdApCommThymeC1EPvP14CAvdRegisterIOE11_os_log_fmt
- __ZZN15CAvdApCommThymeC1EPvP14CAvdRegisterIOE11_os_log_fmt_0
- __ZZN15CAvdApCommThymeC1EPvP14CAvdRegisterIOE11_os_log_fmt_1
- __ZZN15CAvdApCommThymeC1EPvP14CAvdRegisterIOE19kalloc_type_view_78
- __ZZN15CAvdApCommThymedlEPvmE21kalloc_type_view_1336
- __ZZN15CAvdApCommThymenwEmE21kalloc_type_view_1336
- __ZZN17CAvdWrapCtrlThyme13StatusLoggingEiE11_os_log_fmt
- __ZZN17CAvdWrapCtrlThyme13StatusLoggingEiE11_os_log_fmt_0
- __ZZN17CAvdWrapCtrlThyme13StatusLoggingEiE11_os_log_fmt_1
- __ZZN17CAvdWrapCtrlThyme13StatusLoggingEiE11_os_log_fmt_2
- __ZZN17CAvdWrapCtrlThyme13StatusLoggingEiE11_os_log_fmt_3
- __ZZN17CAvdWrapCtrlThyme15CheckMctlStatusEvE11_os_log_fmt
- __ZZN17CAvdWrapCtrlThyme15getAdsDeviceIdsEPyPtPjE11_os_log_fmt
- __ZZN17CAvdWrapCtrlThyme16enableMCDataStrmEjE11_os_log_fmt
- __ZZN17CAvdWrapCtrlThyme16enableMCDataStrmEjE11_os_log_fmt_0
- __ZZN17CAvdWrapCtrlThyme16enableMCDataStrmEjE11_os_log_fmt_1
- __ZZN17CAvdWrapCtrlThyme16enableMCDataStrmEjE11_os_log_fmt_2
- __ZZN17CAvdWrapCtrlThyme16enableMCDataStrmEjE11_os_log_fmt_3
- __ZZN17CAvdWrapCtrlThyme16enableMCDataStrmEjE11_os_log_fmt_4
- __ZZN17CAvdWrapCtrlThyme16enableMCDataStrmEjE11_os_log_fmt_5
- __ZZN17CAvdWrapCtrlThyme17disableMCDataStrmEvE11_os_log_fmt
- __ZZN17CAvdWrapCtrlThyme8PwmResetEvE11_os_log_fmt
- __ZZN17CAvdWrapCtrlThyme9getPmuGTBEPjS0_E11_os_log_fmt
- __ZZN17CAvdWrapCtrlThyme9getPmuRTCEPjS0_E11_os_log_fmt
- __ZZN17CAvdWrapCtrlThymeC1EPjP9IOServiceP7AVDDartjyE11_os_log_fmt
- __ZZN17CAvdWrapCtrlThymeC1EPjP9IOServiceP7AVDDartjyE11_os_log_fmt_0
- __ZZN17CAvdWrapCtrlThymedlEPvmE20kalloc_type_view_948
- __ZZN17CAvdWrapCtrlThymenwEmE20kalloc_type_view_948
- __ZZN19CPriorityQueueThymedlEPvmE20kalloc_type_view_480
- __ZZN19CPriorityQueueThymenwEmE20kalloc_type_view_480
- __ZZN8AppleAVD5startEP9IOServiceE11_os_log_fmt__66_
CStrings:
- "CAvdApCommThyme"
- "CAvdMcpuThyme"
- "CAvdWrapCtrlThyme"
- "site.CAvdApCommThyme"
- "site.CAvdMcpuThyme"
- "site.CPriorityQueueThyme"

```

>  `com.apple.driver.AppleBCMWLANCore`

```diff

-1425.41.0.0.0
+1425.42.0.0.0
   __TEXT.__os_log: 0x74ef
-  __TEXT.__const: 0x2486
-  __TEXT.__cstring: 0x6b744
-  __TEXT_EXEC.__text: 0x22eb98
+  __TEXT.__const: 0x2496
+  __TEXT.__cstring: 0x6b944
+  __TEXT_EXEC.__text: 0x22eeb4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x492
   __DATA.__common: 0x478

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x208
   __DATA_CONST.__mod_term_func: 0x1f8
-  __DATA_CONST.__const: 0x1e820
+  __DATA_CONST.__const: 0x1e830
   __DATA_CONST.__kalloc_type: 0x4440
   __DATA_CONST.__kalloc_var: 0x230
   Functions: 4258
   Symbols:   8270
-  CStrings:  11182
+  CStrings:  11188
 
Symbols:
+ .str.2752
+ .str.2753
+ .str.2754
+ .str.2823
+ .str.3124
+ .str.3137
+ .str.3138
+ .str.3139
+ .str.3209
+ .str.3220
+ .str.3242
+ .str.3305
+ .str.3320
+ .str.3362
+ .str.3378
+ .str.3387
+ .str.3388
+ .str.3428
+ .str.3429
+ .str.3430
+ .str.3431
+ .str.460
+ .str.461
+ __ZZN16AppleBCMWLANCore17configureLPASModeEjE22kalloc_type_view_50440
+ __ZZN16AppleBCMWLANCore17configureLPASModeEjE22kalloc_type_view_50451
+ __ZZN30AppleBCMWLANCoreFirmwareLoader16initWithProviderEP9IOServiceE22kalloc_type_view_60274
+ __ZZN30AppleBCMWLANCoreFirmwareLoader4freeEvE22kalloc_type_view_60362
+ __block_descriptor_tmp.2384
+ __block_descriptor_tmp.2420
+ __block_descriptor_tmp.2788
+ __block_descriptor_tmp.3315
+ __block_literal_global.2386
+ __block_literal_global.2422
- .str.2748
- .str.2749
- .str.2750
- .str.2819
- .str.3120
- .str.3133
- .str.3134
- .str.3135
- .str.3205
- .str.3216
- .str.3238
- .str.3301
- .str.3316
- .str.3358
- .str.3374
- .str.3383
- .str.3384
- .str.3417
- .str.3418
- .str.3419
- .str.3420
- __ZZN16AppleBCMWLANCore17configureLPASModeEjE22kalloc_type_view_50430
- __ZZN16AppleBCMWLANCore17configureLPASModeEjE22kalloc_type_view_50441
- __ZZN30AppleBCMWLANCoreFirmwareLoader16initWithProviderEP9IOServiceE22kalloc_type_view_60264
- __ZZN30AppleBCMWLANCoreFirmwareLoader4freeEvE22kalloc_type_view_60352
- __block_descriptor_tmp.2380
- __block_descriptor_tmp.2416
- __block_descriptor_tmp.2784
- __block_descriptor_tmp.3311
- __block_literal_global.2382
- __block_literal_global.2418
CStrings:
+ "\"AppleBCMWLANV3_Drivers-1425.42\""
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/IOKit/apple80211/IO80211Util.h"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLAN11beAdapter.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANBSSBeacon.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANBssManager.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCommandMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCommander.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCore.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCoreDbg.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANIOReportingPerSlice.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANJoinAdapter.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANLQM.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANNANInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANPowerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANProximityInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANScanAdapter.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANTimeSyncEngine.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANTxPowerManager.cpp"
+ "AppleBCMWLANV3_Drivers-1425.42"
+ "LinkLoss"
+ "LinkTestFailure"
+ "Mar 26 2025 22:12:29"
+ "[ik] %s@%d:Exiting setRESET_CHIP after calling FaultReport with kFaultActionFullCapture"
+ "[ik] %s@%d:This call to setRESET_CHIP will not actually reset the chip nor collect CoreCapture! Forwarding to dbgTriggerWatchdog()"
+ "[ik] %s@%d:This call to setRESET_CHIP will not actually reset the chip nor collect CoreCapture! returning ENODEV, calling message %s"
+ "[ik] %s@%d:This call to setRESET_CHIP will not actually reset the chip! isTrap=%u, isUserspaceReset=%u, calling message %s"
+ "[ik] %s@%d:isTrap=%u, isUserspaceReset=%u, trap reason %u, message: %s"
- "\"AppleBCMWLANV3_Drivers-1425.41\""
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/IOKit/apple80211/IO80211Util.h"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLAN11beAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANBSSBeacon.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANBssManager.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCommandMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCommander.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCore.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCoreDbg.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANIOReportingPerSlice.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANJoinAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANLQM.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANNANInterface.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANPowerManager.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANProximityInterface.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANScanAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANTimeSyncEngine.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANTxPowerManager.cpp"
- "AppleBCMWLANV3_Drivers-1425.41"
- "Mar 19 2025 21:13:19"
- "[ik] %s@%d:isTrap=%u, isUserspaceReset=%u, trap reason %u\n"

```

>  `com.apple.driver.AppleConvergedIPCOLYBTControl`

```diff

-126.0.0.0.0
-  __TEXT.__cstring: 0x8008
+150.0.0.0.0
+  __TEXT.__cstring: 0x8095
   __TEXT.__const: 0x90
-  __TEXT_EXEC.__text: 0x49184
+  __TEXT_EXEC.__text: 0x49acc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1f0

   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__mod_init_func: 0x58
   __DATA_CONST.__mod_term_func: 0x58
-  __DATA_CONST.__const: 0x7298
+  __DATA_CONST.__const: 0x72e8
   __DATA_CONST.__kalloc_type: 0xc40
   __DATA_CONST.__kalloc_var: 0x500
-  Functions: 968
-  Symbols:   1727
-  CStrings:  1001
+  Functions: 975
+  Symbols:   1737
+  CStrings:  1007
 
Symbols:
+ __ZN12ACIPCControl15setDARBasedTrapEb
+ __ZN12ACIPCControl19setChipInaccessibleEb
+ __ZN12ACIPCControl7getChipEv
+ __ZN14ACIPCBTIDevice15setDARBasedTrapEb
+ __ZN14ACIPCBTIDevice18isChipInaccessibleEv
+ __ZN14ACIPCBTIDevice19setChipInaccessibleEb
+ __ZN14ACIPCRTIDevice15setDARBasedTrapEb
+ __ZN14ACIPCRTIDevice18isChipInaccessibleEv
+ __ZN14ACIPCRTIDevice19setChipInaccessibleEb
+ __ZN14ACIPCRTIDevice21updateDARTrapDoorbellE26acipcOLYBTDARDoorvellValue
+ __ZZN14ACIPCRTIDevice10initializeEP20acipcRTIDeviceParamsE20kalloc_type_view_413
+ __ZZN14ACIPCRTIDevice10initializeEP20acipcRTIDeviceParamsE20kalloc_type_view_421
+ __ZZN14ACIPCRTIDevice10initializeEP20acipcRTIDeviceParamsE20kalloc_type_view_437
+ __ZZN14ACIPCRTIDevice10initializeEP20acipcRTIDeviceParamsE20kalloc_type_view_468
+ __ZZN14ACIPCRTIDevice9terminateEvE20kalloc_type_view_523
+ __ZZN14ACIPCRTIDevice9terminateEvE20kalloc_type_view_529
+ __ZZN14ACIPCRTIDevice9terminateEvE20kalloc_type_view_535
+ __ZZN14ACIPCRTIDevice9terminateEvE20kalloc_type_view_543
+ __ZZN17ACIPCOLYBTControldlEPvmE19kalloc_type_view_54
+ __ZZN17ACIPCOLYBTControlnwEmE19kalloc_type_view_54
- __ZZN14ACIPCRTIDevice10initializeEP20acipcRTIDeviceParamsE20kalloc_type_view_404
- __ZZN14ACIPCRTIDevice10initializeEP20acipcRTIDeviceParamsE20kalloc_type_view_412
- __ZZN14ACIPCRTIDevice10initializeEP20acipcRTIDeviceParamsE20kalloc_type_view_428
- __ZZN14ACIPCRTIDevice10initializeEP20acipcRTIDeviceParamsE20kalloc_type_view_459
- __ZZN14ACIPCRTIDevice9terminateEvE20kalloc_type_view_514
- __ZZN14ACIPCRTIDevice9terminateEvE20kalloc_type_view_520
- __ZZN14ACIPCRTIDevice9terminateEvE20kalloc_type_view_526
- __ZZN14ACIPCRTIDevice9terminateEvE20kalloc_type_view_534
- __ZZN17ACIPCOLYBTControldlEPvmE19kalloc_type_view_49
- __ZZN17ACIPCOLYBTControlnwEmE19kalloc_type_view_49
CStrings:
+ "%s::%s: Chip is inaccessible \n"
+ "%s::%s: trigger DAR based trap\n"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCBTIDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCBTIInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCOLYBTControl.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCOLYBTControlReporter.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCRTIDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCRTIInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCOLYBTDebug/AppleConvergedIPCOLYBTCoreDumpProvider.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCOLYBTDebug/AppleConvergedIPCOLYBTLogProvider.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCBTIDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCBTIPipe.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCOLYBTControl.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCRTIDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCRTIPipe.cpp"
+ "12222221221121212122212222222211111222222222112211111111111111111222222"
+ "isChipInaccessible"
+ "setChipInaccessible"
+ "setDARBasedTrap"
+ "updateDARTrapDoorbell"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCDevice.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCBTIDevice.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCBTIInterface.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCOLYBTControl.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCOLYBTControlReporter.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCRTIDevice.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCRTIInterface.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCOLYBTDebug/AppleConvergedIPCOLYBTCoreDumpProvider.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCOLYBTDebug/AppleConvergedIPCOLYBTLogProvider.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCBTIDevice.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCBTIPipe.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCOLYBTControl.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCRTIDevice.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCRTIPipe.cpp"
- "1222222122112121212221222222221111122222222211221111111111111111122222"

```

>  `com.apple.driver.AppleConvergedPCI`

```diff

-126.0.0.0.0
+150.0.0.0.0
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x707c
-  __TEXT_EXEC.__text: 0x40098
+  __TEXT.__cstring: 0x70b3
+  __TEXT_EXEC.__text: 0x4047c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x2d0

   __DATA_CONST.__got: 0x108
   __DATA_CONST.__mod_init_func: 0x68
   __DATA_CONST.__mod_term_func: 0x68
-  __DATA_CONST.__const: 0x6eb8
+  __DATA_CONST.__const: 0x6ee8
   __DATA_CONST.__kalloc_type: 0x1380
-  Functions: 1076
-  Symbols:   1742
-  CStrings:  898
+  Functions: 1082
+  Symbols:   1748
+  CStrings:  901
 
Symbols:
+ __ZN12ACIPCControl15setDARBasedTrapEb
+ __ZN12ACIPCControl19setChipInaccessibleEb
+ __ZN12ACIPCControl7getChipEv
+ __ZN15ACIPCNullDevice15setDARBasedTrapEb
+ __ZN15ACIPCNullDevice18isChipInaccessibleEv
+ __ZN15ACIPCNullDevice19setChipInaccessibleEb
+ __ZZN15ACIPCNullDevicedlEPvmE19kalloc_type_view_49
+ __ZZN15ACIPCNullDevicenwEmE19kalloc_type_view_49
+ __ZZN24AppleConvergedIPCControl16handlePCIMessageEjE21kalloc_type_view_2752
+ __ZZN24AppleConvergedIPCControl16handlePCIMessageEjE21kalloc_type_view_2776
+ __ZZN24AppleConvergedIPCControl20pciMessageThreadCallEPvS0_E21kalloc_type_view_2793
- __ZZN15ACIPCNullDevicedlEPvmE19kalloc_type_view_46
- __ZZN15ACIPCNullDevicenwEmE19kalloc_type_view_46
- __ZZN24AppleConvergedIPCControl16handlePCIMessageEjE21kalloc_type_view_2747
- __ZZN24AppleConvergedIPCControl16handlePCIMessageEjE21kalloc_type_view_2771
- __ZZN24AppleConvergedIPCControl20pciMessageThreadCallEPvS0_E21kalloc_type_view_2788
CStrings:
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCControl.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCLogger.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCIOCommand.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCMemoryCommand.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCMemoryPolicy.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCRequest.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/UserClient/AppleConvergedIPCControlUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/UserClient/AppleConvergedIPCUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedPCI/AppleConvergedPCI.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/ACIPCChip.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/ACIPCControl.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/ACIPCPort.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/Chips/ACIPCChip4388.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/Chips/ACIPCChip4399.cpp"
+ "isChipInaccessible"
+ "setChipInaccessible"
+ "setDARBasedTrap"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCControl.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCInterface.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCLogger.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCIOCommand.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCMemoryCommand.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCMemoryPolicy.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCRequest.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/UserClient/AppleConvergedIPCControlUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/UserClient/AppleConvergedIPCUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedPCI/AppleConvergedPCI.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/ACIPCChip.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/ACIPCControl.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/ACIPCPort.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/Chips/ACIPCChip4388.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/Chips/ACIPCChip4399.cpp"

```

>  `com.apple.driver.AppleGPIOICController`

```diff

-57.0.0.0.0
+59.0.0.0.0
   __TEXT.__const: 0x150
   __TEXT.__cstring: 0xe10
-  __TEXT_EXEC.__text: 0xb350
+  __TEXT_EXEC.__text: 0xb3a8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x128

   __DATA_CONST.__kalloc_type: 0x1c0
   __DATA_CONST.__kalloc_var: 0xf0
   Functions: 260
-  Symbols:   1111
+  Symbols:   1115
   CStrings:  91
 
Symbols:
+ _ZN16AppleT8101GPIOIC17initPinsAndGroupsEjj.cold.11
+ _ZN16AppleT8101GPIOIC17initPinsAndGroupsEjj.cold.12
+ _ZN16AppleT8101GPIOIC17initPinsAndGroupsEjj.cold.13
+ _ZN16AppleT8101GPIOIC17initPinsAndGroupsEjj.cold.14

```

>  `com.apple.driver.AppleM2ScalerCSCDriver`

```diff

-149.28.4.0.0
+149.28.3.0.0
   __TEXT.__const: 0x64dc0
-  __TEXT.__cstring: 0x1b660
-  __TEXT_EXEC.__text: 0x11264c
+  __TEXT.__cstring: 0x1ba94
+  __TEXT_EXEC.__text: 0x11320c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1ff00
-  __DATA.__common: 0x22f0
+  __DATA.__common: 0x22f8
   __DATA.__bss: 0x1170
   __DATA_CONST.__auth_got: 0x570
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__auth_ptr: 0x88
   __DATA_CONST.__mod_init_func: 0x5c8
   __DATA_CONST.__mod_term_func: 0x5a0
-  __DATA_CONST.__const: 0x34c28
+  __DATA_CONST.__const: 0x34c58
   __DATA_CONST.__kalloc_type: 0x4580
   __DATA_CONST.__kalloc_var: 0x780
-  Functions: 7848
-  Symbols:   11340
-  CStrings:  2773
+  Functions: 7869
+  Symbols:   11361
+  CStrings:  2790
 
Symbols:
+ _ZN30MSR23BackwardsCompatibleFilter22checkCoefficientsValidEj20VerticalOrHorizontal.cold.1
+ _ZN30MSR23BackwardsCompatibleFilter22checkCoefficientsValidEj20VerticalOrHorizontal.cold.2
+ _ZN30MSR23BackwardsCompatibleFilter22checkCoefficientsValidEj20VerticalOrHorizontal.cold.3
+ _ZN30MSR23BackwardsCompatibleFilter22checkCoefficientsValidEj20VerticalOrHorizontal.cold.4
+ _ZN30MSR23BackwardsCompatibleFilter22checkCoefficientsValidEj20VerticalOrHorizontal.cold.5
+ _ZN30MSR23BackwardsCompatibleFilter22checkCoefficientsValidEj20VerticalOrHorizontal.cold.6
+ _ZN30MSR23BackwardsCompatibleFilter22checkCoefficientsValidEj20VerticalOrHorizontal.cold.7
+ _ZN30MSR23BackwardsCompatibleFilter22checkCoefficientsValidEj20VerticalOrHorizontal.cold.8
+ _ZN30MSR23BackwardsCompatibleFilter22checkCoefficientsValidEj20VerticalOrHorizontal.cold.9
+ _ZN30MSR23BackwardsCompatibleFilter22updateWithCoefficientsEj20VerticalOrHorizontal17ChromaLumaOrAlphaPjS2_b.cold.5
+ _ZN30MSR23BackwardsCompatibleFilter8allocateE22ScalerSupportedFiltersjjjjPK25SCALER_PROPERTIES_EXTENTSPK22AppleM2ScalerCSCDriver.cold.1
+ _ZN33IosaPolyphaseScalingPipeUnitMSR2314prepareFiltersEP16pipeUnitExchangeb20VerticalOrHorizontal.cold.4
+ _ZNK19AppleM2ScalerCSCHal20computeChromaDDAinitEP18M2ScalerCSCRequest20VerticalOrHorizontal.cold.1
+ __ZN29AppleM2ScalerCSCDriverFilters22getCoefficientsShiftedEj20VerticalOrHorizontal
+ __ZN30MSR23BackwardsCompatibleFilter22checkCoefficientsValidEj20VerticalOrHorizontal
+ __ZN30MSR23BackwardsCompatibleFilter22getCoefficientsShiftedEj20VerticalOrHorizontal
+ __ZN30MSR23BackwardsCompatibleFilter8allocateE22ScalerSupportedFiltersjjjjPK25SCALER_PROPERTIES_EXTENTSPK22AppleM2ScalerCSCDriver
+ __ZZL15logFailedClientP26IOSurfaceAcceleratorClientP4taskP18M2ScalerCSCRequestE21kalloc_type_view_2654
+ __ZZL22notify_signal_callbackP8OSObjectP20IOSurfaceSharedEventyyE21kalloc_type_view_2540
+ __ZZN19AppleM2ScalerCSCHal22clearShadowMapperCacheEvE21kalloc_type_view_9655
+ __ZZN19AppleM2ScalerCSCHal37addSurfaceIntoShadowMapperCache_gatedEP9IOSurfaceE21kalloc_type_view_9594
+ __ZZN19AppleM2ScalerCSCHal37addSurfaceIntoShadowMapperCache_gatedEP9IOSurfaceE21kalloc_type_view_9616
+ __ZZN19AppleM2ScalerCSCHal40removeSurfaceFromShadowMapperCache_gatedEP9IOSurfaceE21kalloc_type_view_9640
+ __ZZN22AppleM2ScalerCSCDriver12notify_eventEP20IOSurfaceSharedEventyyE21kalloc_type_view_2495
+ __ZZN22AppleM2ScalerCSCDriver21isSharedEventWaitDoneEP18M2ScalerCSCRequestP9IOSurfacebE21kalloc_type_view_3658
+ __ZZN22AppleM2ScalerCSCDriver24executeSharedEventSignalEP18M2ScalerCSCRequestP9IOSurfacebE21kalloc_type_view_3714
+ __ZZN22AppleM2ScalerCSCDriver34setStatTransformEvent_gatedContextEP18M2ScalerCSCRequest14TransformEventE21kalloc_type_view_5443
+ __ZZN22AppleM2ScalerCSCDriver36pruneTransformStatQueue_gatedContextEvE21kalloc_type_view_5422
+ __ZZN22AppleM2ScalerCSCDriver4stopEP9IOServiceE21kalloc_type_view_1512
+ __ZZN22AppleM2ScalerCSCDriver4stopEP9IOServiceE21kalloc_type_view_1519
+ __ZZN33IosaPolyphaseScalingPipeUnitMSR2314prepareFiltersEP16pipeUnitExchangeb20VerticalOrHorizontalENK3$_0clEv
- _ZN30MSR23BackwardsCompatibleFilter8allocateE22ScalerSupportedFiltersjjjjPK25SCALER_PROPERTIES_EXTENTS.cold.1
- __ZN30MSR23BackwardsCompatibleFilter8allocateE22ScalerSupportedFiltersjjjjPK25SCALER_PROPERTIES_EXTENTS
- __ZZL15logFailedClientP26IOSurfaceAcceleratorClientP4taskP18M2ScalerCSCRequestE21kalloc_type_view_2653
- __ZZL22notify_signal_callbackP8OSObjectP20IOSurfaceSharedEventyyE21kalloc_type_view_2539
- __ZZN19AppleM2ScalerCSCHal22clearShadowMapperCacheEvE21kalloc_type_view_9646
- __ZZN19AppleM2ScalerCSCHal37addSurfaceIntoShadowMapperCache_gatedEP9IOSurfaceE21kalloc_type_view_9585
- __ZZN19AppleM2ScalerCSCHal37addSurfaceIntoShadowMapperCache_gatedEP9IOSurfaceE21kalloc_type_view_9607
- __ZZN19AppleM2ScalerCSCHal40removeSurfaceFromShadowMapperCache_gatedEP9IOSurfaceE21kalloc_type_view_9631
- __ZZN22AppleM2ScalerCSCDriver12notify_eventEP20IOSurfaceSharedEventyyE21kalloc_type_view_2494
- __ZZN22AppleM2ScalerCSCDriver21isSharedEventWaitDoneEP18M2ScalerCSCRequestP9IOSurfacebE21kalloc_type_view_3657
- __ZZN22AppleM2ScalerCSCDriver24executeSharedEventSignalEP18M2ScalerCSCRequestP9IOSurfacebE21kalloc_type_view_3713
- __ZZN22AppleM2ScalerCSCDriver34setStatTransformEvent_gatedContextEP18M2ScalerCSCRequest14TransformEventE21kalloc_type_view_5442
- __ZZN22AppleM2ScalerCSCDriver36pruneTransformStatQueue_gatedContextEvE21kalloc_type_view_5421
- __ZZN22AppleM2ScalerCSCDriver4stopEP9IOServiceE21kalloc_type_view_1511
- __ZZN22AppleM2ScalerCSCDriver4stopEP9IOServiceE21kalloc_type_view_1518
CStrings:
+ "%d %s %s got null for pcoeffs\n"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AXI2AFControl/IosaAxi2AfControl.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriver.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriverFilters.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriverFilters.h"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHal.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR10j.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR11.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR15.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR16.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR2.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR21.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR22.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR24.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR25.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR4.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR6.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR7.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR9.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR16.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR17.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR21.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR22.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DisplayScalerFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DitherControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DriverCommonFunctions.h"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23Dv.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23Rtk.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FrameDescriptorRing.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FrameDescriptorRingMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IOAsynchronousScheduler.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IOSurfaceAcceleratorClient.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IOSurfaceAcceleratorPreparator.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR15.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR18.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR4.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaFilmGrainControlMSR16.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaFilmGrainControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPowerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPrescalerControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControl.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR18.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaTiledCompressedMemMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaWdmaControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/K2KTests.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControl.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControl.h"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR4.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControl.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControl.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR6.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControl.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR22.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR4.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MSR23BackwardsCompatibleFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MSR23ChromaDownsampleFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MSR23DefaultFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MailBox.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MailBoxMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/ModularDefaultFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStream.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStreamMSR15.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStreamMSR19.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrBlockDescriptorRegisterStream.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrBlockDescriptorRegisterStreamMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrRegisterStream.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/Request.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/RingBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/Shared/Utility/IOFBSAGammaLUT.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/SpillBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/SpillBufferMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/StatusDescriptorRing.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/StatusDescriptorRingMSR23.cpp"
+ "122222121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212121112222222222"
+ "Custom Filter Shift has been detected.\n"
+ "Custom Filter does not follow odd symmetry in phase 0\n"
+ "Falling back to default filters, skipping custom filters\n"
+ "Found phase %d that has taps around middle tap with closer values\n"
+ "IOSurfaceAcceleratorCapabilitiesVariableRateDirectionalScaling"
+ "Skipping coefficients are shifted checks\n"
+ "Skipping complete even symmetry check. Custom Filter is not shifted.\n"
+ "Using custom threshold for filter checks 0x%x\n"
+ "[%s][%s]Detected coefficient shift in custom filters bin %d\n"
+ "[SYM] Skipping CHDDAInit subsample adjustment\n"
+ "cannot get bootargs for checking shifted coefficients\n"
+ "checkCoefficientsValid"
+ "computeChromaDDAinit"
+ "msr_coefficient_checks"
+ "tap %d and tap %d are not close in value as expected\n"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AXI2AFControl/IosaAxi2AfControl.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriver.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriverFilters.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriverFilters.h"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHal.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR10j.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR11.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR15.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR16.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR2.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR21.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR22.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR24.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR25.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR4.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR6.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR7.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR9.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR16.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR17.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR21.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR22.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DisplayScalerFilter.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DitherControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DriverCommonFunctions.h"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23Dv.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23Rtk.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FrameDescriptorRing.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FrameDescriptorRingMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IOAsynchronousScheduler.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IOSurfaceAcceleratorClient.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IOSurfaceAcceleratorPreparator.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR15.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR18.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR4.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaFilmGrainControlMSR16.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaFilmGrainControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPowerManager.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPrescalerControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControl.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR18.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaTiledCompressedMemMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaWdmaControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/K2KTests.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControl.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControl.h"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR4.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControl.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControl.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR6.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControl.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR22.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR4.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MSR23BackwardsCompatibleFilter.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MSR23ChromaDownsampleFilter.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MSR23DefaultFilter.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MailBox.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MailBoxMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/ModularDefaultFilter.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStream.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStreamMSR15.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStreamMSR19.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrBlockDescriptorRegisterStream.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrBlockDescriptorRegisterStreamMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrRegisterStream.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/Request.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/RingBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/Shared/Utility/IOFBSAGammaLUT.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/SpillBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/SpillBufferMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/StatusDescriptorRing.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/StatusDescriptorRingMSR23.cpp"

```

>  `com.apple.driver.AppleMobileDispH13G-DFR`

```diff

-399.26.7.0.0
+399.27.2.0.0
   __TEXT.__const: 0x4a50
   __TEXT.__cstring: 0xd33f
   __TEXT.__ustring: 0x12
-  __TEXT_EXEC.__text: 0x522cc
+  __TEXT_EXEC.__text: 0x522c8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1a00
   __DATA.__common: 0x750
Symbols:
+ __ZN25IOMobileFramebufferLegacy22dropAbortedSwaps_gatedEv
- __ZN25IOMobileFramebufferLegacy22dropAbortedSwaps_gatedEb

```

>  `com.apple.driver.AppleMobileFileIntegrity`

```diff

-938.101.1.0.0
+938.120.9.0.1
   __TEXT.__cstring: 0x1aa1e
-  __TEXT.__const: 0x1b50
+  __TEXT.__const: 0x1b70
   __TEXT.__os_log: 0x47a
-  __TEXT_EXEC.__text: 0x3353c
+  __TEXT_EXEC.__text: 0x33594
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x81a
   __DATA.__common: 0xb0
CStrings:
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/CommonMem.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
+ "22:10:23"
+ "Mar 26 2025"
+ "cmd = (acm_command_t *)({ size_t sizeVal = (cmdSize); void *ptr = acm_mem_alloc_data(sizeVal); acm_mem_alloc_info(\"<data>\", ptr, sizeVal, \"/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c\", 22, __func__); ptr; })"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/CommonMem.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
- "21:11:26"
- "Mar 19 2025"
- "cmd = (acm_command_t *)({ size_t sizeVal = (cmdSize); void *ptr = acm_mem_alloc_data(sizeVal); acm_mem_alloc_info(\"<data>\", ptr, sizeVal, \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c\", 22, __func__); ptr; })"

```

>  `com.apple.driver.AppleOLYHAL`

```diff

 400.20.0.0.0
   __TEXT.__const: 0x798
   __TEXT.__cstring: 0x472a
-  __TEXT_EXEC.__text: 0x1de48
+  __TEXT_EXEC.__text: 0x1de38
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x18c
   __DATA.__common: 0x170

```

>  `com.apple.driver.AppleRSMChannel`

```diff

-205.0.0.0.0
-  __TEXT.__cstring: 0x4a4
+208.120.5.0.0
+  __TEXT.__cstring: 0x4f0
   __TEXT.__os_log: 0x173
-  __TEXT_EXEC.__text: 0xea2c
+  __TEXT_EXEC.__text: 0xeb04
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1e8
   __DATA.__common: 0x100

   __DATA_CONST.__kalloc_type: 0x180
   Functions: 565
   Symbols:   1101
-  CStrings:  58
+  CStrings:  60
 
Symbols:
+ __block_descriptor_tmp.12
+ __block_descriptor_tmp.13
- __block_descriptor_tmp.10
- __block_descriptor_tmp.9
CStrings:
+ "AppleRSMChannelControllerMajorVersion"
+ "AppleRSMChannelControllerMinorVersion"

```

>  `com.apple.driver.AppleSEPKeyStore`

```diff

-1827.100.156.0.0
-  __TEXT.__cstring: 0x3d1f
+1827.120.2.0.0
+  __TEXT.__cstring: 0x3d1d
   __TEXT.__const: 0x874
   __TEXT_EXEC.__text: 0x3cdac
   __TEXT_EXEC.__auth_stubs: 0x0
CStrings:
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_SEP_kexts/AppleKeyStore.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_SEP_kexts/ipc.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_SEP_kexts/msg.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_SEP_kexts/platform/platform.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_SEP_kexts/platform/platform_kernel.c"
+ "1827.120.2"
+ "22:12:19"
+ "Mar 26 2025"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_SEP_kexts/AppleKeyStore.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_SEP_kexts/ipc.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_SEP_kexts/msg.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_SEP_kexts/platform/platform.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_SEP_kexts/platform/platform_kernel.c"
- "1827.100.156"
- "21:12:30"
- "Mar 19 2025"

```

>  `com.apple.driver.AppleT8103CLPCv3`

```diff

-1175.100.103.0.0
-  __TEXT.__cstring: 0x31d0
-  __TEXT.__const: 0x970
-  __TEXT_EXEC.__text: 0x4edb4
+1175.120.17.0.0
+  __TEXT.__cstring: 0x3200
+  __TEXT.__const: 0x9a0
+  __TEXT_EXEC.__text: 0x5063c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x9378
-  __DATA.__common: 0x8f80
-  __DATA.__bss: 0x268
+  __DATA.__data: 0x93b8
+  __DATA.__common: 0x9100
+  __DATA.__bss: 0x278
   __DATA_CONST.__auth_got: 0x460
   __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__mod_init_func: 0x110
+  __DATA_CONST.__mod_init_func: 0x118
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x52a8
+  __DATA_CONST.__const: 0x52c0
   __DATA_CONST.__kalloc_type: 0x300
   __DATA_CONST.__kalloc_var: 0x2d0
-  Functions: 1128
-  Symbols:   1883
-  CStrings:  457
+  Functions: 1130
+  Symbols:   1889
+  CStrings:  459
 
Symbols:
+ _GLOBAL__sub_I_aon_ptd_power_interface.cpp
+ __ZN4clpc20AonPtdPowerInterfaceINS_5power11T8103ConfigENS_4priv9PMGRAdminENS3_6SystemEE16initWithProviderEP9IOService
+ __ZN4clpc20AonPtdPowerInterfaceINS_5power11T8103ConfigENS_4priv9PMGRAdminENS3_6SystemEE6enableEb
+ __ZN4clpc20AonPtdPowerInterfaceINS_5power11T8103ConfigENS_4priv9PMGRAdminENS3_6SystemEE6updateEv
+ __ZN4clpc4CLPC20setSlowThermalBudgetEjNS_6shared9TimescaleENS_14PowerInterfaceENS1_6report8LostPerf10ReasonCodeE
+ __ZN4clpc4CLPC22setDiscretionaryBudgetEjNS_6shared9TimescaleENS_14PowerInterfaceENS1_6report8LostPerf10ReasonCodeE
+ __ZN4clpc4tgrp8DeadlineINS0_17NormalThreadGroupEE23calculateCPUBoostEffortEfffff
+ __ZN4clpc5power19CPUWorkloadPowerMap4initERKNS_10CPUPerfMapILm256ELNS_25PerfMapConstructionMethodE0ENS_19CPUPerfMapPolicyLUTILm15ELm256EEEEERKNS_5arrayINS0_15CPUCorePowerMapELm2EEE
+ __ZN9AppleCLPC15setPowerBudgetsERKN20ApplePPMKernelClient18PowerBudgetUpdatesEN4clpc14PowerInterfaceE
+ __ZNK4clpc20AonPtdPowerInterfaceINS_5power11T8103ConfigENS_4priv9PMGRAdminENS3_6SystemEE14num_interruptsEv
+ __ZNK4clpc20AonPtdPowerInterfaceINS_5power11T8103ConfigENS_4priv9PMGRAdminENS3_6SystemEE14supports_entryENS_19PowerBudgetPtdEntryE
+ __ZNK4clpc20AonPtdPowerInterfaceINS_5power11T8103ConfigENS_4priv9PMGRAdminENS3_6SystemEE15first_interruptEv
- __ZN4clpc4CLPC20setSlowThermalBudgetEjNS_6shared9TimescaleE
- __ZN4clpc4CLPC22setDiscretionaryBudgetEjNS_6shared9TimescaleE
- __ZN4clpc4CLPC34setAonPtdInterruptsOffsetAndLengthEjj
- __ZN4clpc4tgrp8DeadlineINS0_17NormalThreadGroupEE18calculateCPUEffortEffff
- __ZN4clpc5power19CPUWorkloadPowerMap4initERKNS_10CPUPerfMapILm256ENS_19CPUPerfMapPolicyLUTILm15ELm256EEEEERKNS_5arrayINS0_15CPUCorePowerMapELm2EEE
- __ZN4clpc6shared6report8LostPerf10ReasonCode16legacyTraceValueINS_5power11T8103ConfigEEEhv
- __ZN9AppleCLPC15setPowerBudgetsERKN20ApplePPMKernelClient18PowerBudgetUpdatesE
CStrings:
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/ane_perf_sampler_impl.hpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/ane_topology.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/apple_clpc.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/clpc.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/clpc.hpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_cluster_perf_sampler.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_core_memstall_sampler.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_core_perf_sampler.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_dvfm_table_impl.hpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_sched_interface.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_temperature_sampler.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_timer.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_topology.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_uncore_perf_sampler.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/fabric_dvfm_table.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/gpu_dvfm_table.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/perf_map_impl.hpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/power_map.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/power_telemetry_pusher_impl.hpp"
+ "2025-03-26T22:19:15-07:00"
+ "AppleCLPC-1175.120.17"
+ "OperatingStates"
+ "map_perf_scores[type][base_index] >= bottom_first"
+ "setBudgetToAGXFunction"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/ane_perf_sampler_impl.hpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/ane_topology.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/apple_clpc.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/clpc.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/clpc.hpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_cluster_perf_sampler.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_core_memstall_sampler.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_core_perf_sampler.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_dvfm_table_impl.hpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_sched_interface.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_temperature_sampler.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_timer.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_topology.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_uncore_perf_sampler.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/fabric_dvfm_table.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/gpu_dvfm_table.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/perf_map_impl.hpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/power_map.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/power_telemetry_pusher_impl.hpp"
- "2025-03-19T21:14:49-07:00"
- "AppleCLPC-1175.100.103"
- "perf_scores[type][base] >= bottom_first"

```

>  `com.apple.filesystems.afpfs`

```diff

-695.0.0.0.0
-  __TEXT.__cstring: 0xc339
+697.0.0.0.0
+  __TEXT.__cstring: 0xc295
   __TEXT.__const: 0x410
-  __TEXT_EXEC.__text: 0x39bf4
+  __TEXT_EXEC.__text: 0x39b38
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2e90
   __DATA.__common: 0xe8

   __DATA_CONST.__const: 0x138
   __DATA_CONST.__kalloc_type: 0x1fc0
   __DATA_CONST.__kalloc_var: 0x460
-  Functions: 765
-  Symbols:   1316
-  CStrings:  1219
+  Functions: 762
+  Symbols:   1313
+  CStrings:  1216
 
Symbols:
- afpfs_vnop_getxattr.cold.1
- afpfs_vnop_listxattr.cold.1
- afpfs_vnop_setxattr.cold.1
CStrings:
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/LogMessage.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bio.subproj/bio_lib.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_add.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_blind.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_div.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_exp.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_exp2.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_gcd.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_lib.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_mont.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_mpi.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_print.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_rand.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_recp.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/buffer.subproj/buffer.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/cryptlib.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/err.subproj/err.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/ex_data.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/lhash.subproj/lhash.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/rand.subproj/md_rand.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/stack.subproj/stack.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_catalog.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_encodings.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_reconnect.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_request.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_search.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_vfsops.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_vfsutils.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_vhash.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_vnops.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/encrypt_random.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/recon1.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/LogMessage.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bio.subproj/bio_lib.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_add.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_blind.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_div.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_exp.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_exp2.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_gcd.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_lib.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_mont.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_mpi.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_print.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_rand.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_recp.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/buffer.subproj/buffer.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/cryptlib.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/err.subproj/err.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/ex_data.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/lhash.subproj/lhash.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/rand.subproj/md_rand.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/stack.subproj/stack.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_catalog.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_encodings.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_reconnect.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_request.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_search.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_vfsops.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_vfsutils.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_vhash.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_vnops.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_xattr.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/encrypt_random.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/recon1.c"
- "afpfs_xattr.c"
- "datap != NULL"

```

>  `com.apple.filesystems.apfs`

```diff

-2332.101.1.0.0
+2332.120.27.0.0
   __TEXT.__const: 0xaf8
-  __TEXT.__cstring: 0x574f5
-  __TEXT_EXEC.__text: 0x1843d0
+  __TEXT.__cstring: 0x5771a
+  __TEXT_EXEC.__text: 0x18464c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xd48
-  __DATA.__bss: 0xb10
+  __DATA.__data: 0xd50
+  __DATA.__bss: 0xb08
   __DATA_CONST.__auth_got: 0x12e0
   __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__auth_ptr: 0x8

   __DATA_CONST.__assert: 0x294
   Functions: 2629
   Symbols:   4777
-  CStrings:  7500
+  CStrings:  7510
 
Symbols:
+ _GLOBAL__D_a.1778
+ _ZN18APFSOSNumberAtomic10withNumberEx.1730
+ __ZZ21delta_teardown_threadPviE22kalloc_type_view_10217
+ __ZZL23apfs_keycache_operationPKh13apfs_key_typeiPP3cpxbE22kalloc_type_view_13404
+ __ZZL23apfs_keycache_operationPKh13apfs_key_typeiPP3cpxbE22kalloc_type_view_13414
+ __ZZL23apfs_keycache_operationPKh13apfs_key_typeiPP3cpxbE22kalloc_type_view_13435
+ __ZZN15AppleAPFSVolume15asyncCryptoReadEP18AppleAPFSContaineryyPyaybE21kalloc_type_view_9156
+ __ZZN15AppleAPFSVolume15asyncCryptoReadEP18AppleAPFSContaineryyPyaybE21kalloc_type_view_9243
+ __ZZN15AppleAPFSVolume27asyncCryptoReadFinishHelperEP24multikey_crypto_io_entryPyE21kalloc_type_view_9275
+ __ZZN18AppleAPFSContainer16lockerDataGetSetEb9klckr_ctxPhyP4taskE22kalloc_type_view_15002
+ __ZZN18AppleAPFSContainer16lockerDataGetSetEb9klckr_ctxPhyP4taskE22kalloc_type_view_15005
+ __ZZN18AppleAPFSContainer19deltaCreateTeardownEP18delta_create_ctx_tE21kalloc_type_view_8129
+ __ZZN18AppleAPFSContainer20deltaRestoreTeardownEP19delta_restore_ctx_tE21kalloc_type_view_8323
+ __ZZN18AppleAPFSContainer27containerGetKeyLockerRangesEjj9klckr_ctxyPjP20vol_keylocker_rangesE22kalloc_type_view_14823
+ __ZZN18AppleAPFSContainer27containerGetKeyLockerRangesEjj9klckr_ctxyPjP20vol_keylocker_rangesE22kalloc_type_view_14854
+ __ZZN19AppleAPFSUserClient24methodDeltaCreatePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11488
+ __ZZN19AppleAPFSUserClient24methodDeltaCreatePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11512
+ __ZZN19AppleAPFSUserClient25methodDeltaRestorePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11614
+ __ZZN19AppleAPFSUserClient25methodDeltaRestorePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11643
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10847
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10855
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10856
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10857
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10922
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10925
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10934
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10937
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10945
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10948
+ __ZZN19AppleAPFSUserClient4stopEP9IOServiceE22kalloc_type_view_10231
+ __ZZN19AppleAPFSUserClient4stopEP9IOServiceE22kalloc_type_view_10241
+ ek_to_crypto_state.kalloc_type_view_32689
+ legacy_get_ek.kalloc_type_view_34171
+ nx_unmount_internal.kalloc_type_view_1995
+ purge_files_with_ino.kalloc_type_view_7063
+ purge_files_with_ino.kalloc_type_view_7267
+ purge_single_file.kalloc_type_view_9268
+ purge_single_file.kalloc_type_view_9272
+ purge_single_file.kalloc_type_view_9274
+ purge_single_file.kalloc_type_view_9300
+ purge_single_file.kalloc_type_view_9301
+ xattr_ek_to_crypto_state.kalloc_type_view_33364
- _GLOBAL__D_a.1777
- _ZN18APFSOSNumberAtomic10withNumberEx.1729
- __ZZ21delta_teardown_threadPviE22kalloc_type_view_10210
- __ZZL23apfs_keycache_operationPKh13apfs_key_typeiPP3cpxbE22kalloc_type_view_13397
- __ZZL23apfs_keycache_operationPKh13apfs_key_typeiPP3cpxbE22kalloc_type_view_13407
- __ZZL23apfs_keycache_operationPKh13apfs_key_typeiPP3cpxbE22kalloc_type_view_13428
- __ZZN15AppleAPFSVolume15asyncCryptoReadEP18AppleAPFSContaineryyPyaybE21kalloc_type_view_9149
- __ZZN15AppleAPFSVolume15asyncCryptoReadEP18AppleAPFSContaineryyPyaybE21kalloc_type_view_9236
- __ZZN15AppleAPFSVolume27asyncCryptoReadFinishHelperEP24multikey_crypto_io_entryPyE21kalloc_type_view_9268
- __ZZN18AppleAPFSContainer16lockerDataGetSetEb9klckr_ctxPhyP4taskE22kalloc_type_view_14995
- __ZZN18AppleAPFSContainer16lockerDataGetSetEb9klckr_ctxPhyP4taskE22kalloc_type_view_14998
- __ZZN18AppleAPFSContainer19deltaCreateTeardownEP18delta_create_ctx_tE21kalloc_type_view_8123
- __ZZN18AppleAPFSContainer20deltaRestoreTeardownEP19delta_restore_ctx_tE21kalloc_type_view_8316
- __ZZN18AppleAPFSContainer27containerGetKeyLockerRangesEjj9klckr_ctxyPjP20vol_keylocker_rangesE22kalloc_type_view_14816
- __ZZN18AppleAPFSContainer27containerGetKeyLockerRangesEjj9klckr_ctxyPjP20vol_keylocker_rangesE22kalloc_type_view_14847
- __ZZN19AppleAPFSUserClient24methodDeltaCreatePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11481
- __ZZN19AppleAPFSUserClient24methodDeltaCreatePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11505
- __ZZN19AppleAPFSUserClient25methodDeltaRestorePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11607
- __ZZN19AppleAPFSUserClient25methodDeltaRestorePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11636
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10840
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10841
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10842
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10850
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10915
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10918
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10927
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10930
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10938
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10941
- __ZZN19AppleAPFSUserClient4stopEP9IOServiceE22kalloc_type_view_10224
- __ZZN19AppleAPFSUserClient4stopEP9IOServiceE22kalloc_type_view_10234
- ek_to_crypto_state.kalloc_type_view_32686
- legacy_get_ek.kalloc_type_view_34168
- nx_unmount_internal.kalloc_type_view_1994
- purge_files_with_ino.kalloc_type_view_7052
- purge_files_with_ino.kalloc_type_view_7256
- purge_single_file.kalloc_type_view_9257
- purge_single_file.kalloc_type_view_9261
- purge_single_file.kalloc_type_view_9263
- purge_single_file.kalloc_type_view_9289
- purge_single_file.kalloc_type_view_9290
- xattr_ek_to_crypto_state.kalloc_type_view_33361
CStrings:
+ "%s:%d: %s Deleting incompatible volume %s\n"
+ "%s:%d: %s Deleting volume %s, volume index %u\n"
+ "%s:%d: %s Request to delete volume %u was denied, nx is read only\n"
+ "%s:%d: %s Request to delete volume %u was denied, user not authorized to delete the volume\n"
+ "%s:%d: %s Request to delete volume %u was denied, volume is still open\n"
+ "%s:%d: %s Request to delete volume %u was denied, wrong volume index\n"
+ "%s:%d: %s Request to delete volume index %u, made by process %s (pid %d)\n"
+ "%s:%d: %s can't mark compressed inode as a purgeable fault\n"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apfs/kext/apfs_filter.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apfs/kext/apfs_ioctls.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apfs/kext/apfs_vnops.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apfs/nx/jobj.c"
+ "2025/03/26"
+ "22:13:31"
+ "22:13:32"
+ "2332.120.27"
+ "Mar 26 2025"
+ "apfs-2332.120.27"
+ "volumeDelete"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/apfs/kext/apfs_filter.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/apfs/kext/apfs_ioctls.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/apfs/kext/apfs_vnops.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/apfs/nx/jobj.c"
- "2025/03/19"
- "21:14:54"
- "2332.101.1"
- "Mar 19 2025"
- "apfs-2332.101.1"

```

>  `com.apple.iokit.IO80211Family`

```diff

-1475.34.0.0.0
+1475.36.0.0.0
   __TEXT.__const: 0x12ef0
   __TEXT.__os_log: 0x9251
-  __TEXT.__cstring: 0x8bdd2
-  __TEXT_EXEC.__text: 0x255980
+  __TEXT.__cstring: 0x8bdd9
+  __TEXT_EXEC.__text: 0x255b28
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x5100
   __DATA.__common: 0x23e0

   __DATA_CONST.__kalloc_type: 0x9b00
   __DATA_CONST.__kalloc_var: 0x7d0
   Functions: 12189
-  Symbols:   19160
-  CStrings:  13949
+  Symbols:   19162
+  CStrings:  13950
 
Symbols:
+ __ZL13_channel6Info
+ __ZZN14IO80211NANPeer23lowlatencyGetStatisticsEP11IO80211PeerE21kalloc_type_view_1741
+ __ZZN14IO80211NANPeer23lowlatencyGetStatisticsEP11IO80211PeerE21kalloc_type_view_1759
- __ZZN14IO80211NANPeer23lowlatencyGetStatisticsEP11IO80211PeerE21kalloc_type_view_1738
- __ZZN14IO80211NANPeer23lowlatencyGetStatisticsEP11IO80211PeerE21kalloc_type_view_1756
CStrings:
+ "\"IO80211_kexts-1475.36\""
+ "%s: ALERT: WiFi infra ASSOC failed with status code %d, reason %d, lasted for %d msecs\n"
+ "%s: ALERT: WiFi infra AUTH failed with status code %d, reason %d, lasted for %d msecs\n"
+ "%s: Peer %02X:%02X:%02X:%02X:%02X:%02X has no NDP established, not creating flow queue"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLMulticastPeer.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeer.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PDataPathManager.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSteeringManager.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSupervisor.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211ServiceRequestDescriptor.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211DynamicBufferPool.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211StaticBufferPool.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211Controller.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211ControllerMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211InfraInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211InterfaceMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211PacketDescriptor.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211Peer.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211PeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211PeerMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211SkywalkInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211VirtualInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Infra/IO80211LinkRecovery.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Infra/IO80211ScanManager.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathInitiator.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathManager.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/DiscoveryEngine/IO80211NANDiscoveryEngine.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/Miscellaneous/IO80211NANUtils.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANDataInterfacePeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeer.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceDescriptor.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceManager.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/SynchronizationEngine/IO80211NANSyncEngine.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/UserClients/IO80211AsyncUserClientParameters.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211CommandQueue.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211FlowQueueDatabase.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.h"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_get_handlersLegacy.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlers.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlersLegacy.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Scan/IO80211ScanCacheStore.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211WCL/WCLDeauthDisassoc.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211WCL/WCLJoin/WCLJoinManager.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211WCL/WCLNearbyDeviceDiscoveryManager.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211WCL/WCLNetManager.cpp"
+ "IO80211_kexts-1475.36"
+ "Mar 26 2025 22:13:27"
- "\"IO80211_kexts-1475.34\""
- "%s: WiFi infra ASSOC failed with status code %d, reason %d, removing slots reserved for infra association, lasted for %d msecs\n"
- "%s: WiFi infra AUTH failed with status code %d, reason %d, removing slots reserved for infra association, lasted for %d msecs\n"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLMulticastPeer.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeer.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PDataPathManager.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSteeringManager.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSupervisor.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211ServiceRequestDescriptor.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211DynamicBufferPool.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211StaticBufferPool.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211Controller.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211ControllerMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211InfraInterface.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211InterfaceMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211PacketDescriptor.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211Peer.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211PeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211PeerMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211SkywalkInterface.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211VirtualInterface.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Infra/IO80211LinkRecovery.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Infra/IO80211ScanManager.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathInitiator.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathManager.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/DiscoveryEngine/IO80211NANDiscoveryEngine.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/Miscellaneous/IO80211NANUtils.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANDataInterfacePeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeer.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceDescriptor.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceManager.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/SynchronizationEngine/IO80211NANSyncEngine.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/UserClients/IO80211AsyncUserClientParameters.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211CommandQueue.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211FlowQueueDatabase.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.h"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_get_handlersLegacy.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlers.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlersLegacy.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Scan/IO80211ScanCacheStore.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211WCL/WCLDeauthDisassoc.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211WCL/WCLJoin/WCLJoinManager.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211WCL/WCLNearbyDeviceDiscoveryManager.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211WCL/WCLNetManager.cpp"
- "IO80211_kexts-1475.34"
- "Mar 19 2025 21:15:45"

```

>  `com.apple.iokit.IODisplayPortFamily`

```diff

-739.101.1.0.0
-  __TEXT.__cstring: 0x7cb6
+739.120.3.0.0
+  __TEXT.__cstring: 0x7d78
   __TEXT.__os_log: 0x950b
-  __TEXT.__const: 0x300
-  __TEXT_EXEC.__text: 0x5c8c0
+  __TEXT.__const: 0x440
+  __TEXT_EXEC.__text: 0x5cc64
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x550
   __DATA.__bss: 0x10
-  __DATA_CONST.__auth_got: 0x538
+  __DATA_CONST.__auth_got: 0x540
   __DATA_CONST.__got: 0x170
   __DATA_CONST.__mod_init_func: 0x110
   __DATA_CONST.__mod_term_func: 0x108
   __DATA_CONST.__const: 0x15c88
   __DATA_CONST.__kalloc_type: 0x840
   __DATA_CONST.__kalloc_var: 0x280
-  Functions: 2353
-  Symbols:   4369
-  CStrings:  1520
+  Functions: 2355
+  Symbols:   4373
+  CStrings:  1525
 
Symbols:
+ __ZN18IODPServiceAUXOnly11handleStartEP9IOService
+ __ZN18IODPServiceAUXOnly17enumerateElementsEv
+ __ZZN18IODPServiceAUXOnly17enumerateElementsEvE18BaobabDisplayHints
+ _strcmp
CStrings:
+ "121111121222121211122222111111111122212222212222222122222122222122222222222222222222222222222222222222222222222222211111111121111111122221111112222222222222222222211"
+ "A44602"
+ "A44606"
+ "A44610"
+ "D1baba"

```

>  `com.apple.iokit.IOMobileGraphicsFamily`

```diff

-399.26.7.0.0
+399.27.2.0.0
   __TEXT.__cstring: 0x827d
   __TEXT.__const: 0xa64
-  __TEXT_EXEC.__text: 0x229cc
+  __TEXT_EXEC.__text: 0x229c8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2900
   __DATA.__common: 0x1c92c
Symbols:
+ __ZN25IOMobileFramebufferLegacy22dropAbortedSwaps_gatedEv
- __ZN25IOMobileFramebufferLegacy22dropAbortedSwaps_gatedEb
CStrings:
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOMobileFramebuffer/Kernel/AppleDisplayPipe/DriverCommonFunctions.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOMobileFramebuffer/Kernel/AppleDisplayPipe/DriverCommonFunctions.cpp"

```

>  `com.apple.iokit.IONVMeFamily`

```diff

-775.100.17.0.0
+775.120.7.0.0
   __TEXT.__const: 0x708
-  __TEXT.__cstring: 0x10165
-  __TEXT_EXEC.__text: 0x61248
+  __TEXT.__cstring: 0x10369
+  __TEXT_EXEC.__text: 0x61a3c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4e4
   __DATA.__common: 0x528
   __DATA.__bss: 0x10
   __DATA_CONST.__auth_got: 0x688
-  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__got: 0x188
   __DATA_CONST.__mod_init_func: 0x100
   __DATA_CONST.__mod_term_func: 0x100
-  __DATA_CONST.__const: 0x13730
+  __DATA_CONST.__const: 0x13758
   __DATA_CONST.__kalloc_type: 0x7c0
   __DATA_CONST.__kalloc_var: 0x550
-  Functions: 3169
-  Symbols:   4283
-  CStrings:  1710
+  Functions: 3183
+  Symbols:   4298
+  CStrings:  1718
 
Symbols:
+ _ZN23AppleANS2NVMeController22SetupANS2SleepNotifierEv.cold.1
+ _ZN23AppleANS2NVMeController26SendSleepNotificationToANSEjPb.cold.1
+ _ZN23AppleANS2NVMeController26SendSleepNotificationToANSEjPb.cold.2
+ _ZN23AppleANS2NVMeController26SendSleepNotificationToANSEjPb.cold.3
+ _ZN23AppleANS2NVMeController26SendSleepNotificationToANSEjPb.cold.4
+ _ZN23AppleANS2NVMeController26SendSleepNotificationToANSEjPb.cold.5
+ _ZN23AppleANS2NVMeController5startEP9IOService.cold.30
+ __ZN23AppleANS2NVMeController17systemPowerChangeEPvjP9IOServiceS0_m
+ __ZN23AppleANS2NVMeController17systemPowerChangeEPvjP9IOServiceS0_m_vfpthunk_
+ __ZN23AppleANS2NVMeController22SetupANS2SleepNotifierEv
+ __ZN23AppleANS2NVMeController26SendSleepNotificationToANSEjPb
+ _gIOGeneralInterest
CStrings:
+ "%s::%d:Sleep Notification Tunnel for msg type %u took %llu us\n"
+ "%s::%d:cancelling S2R IDLE Sleep\n"
+ "%s::%d:nvme: ANS Sleep Notification with Opcode %lu failed with ASP status 0x%x\n"
+ "%s::%d:nvme: ANS Sleep Notification with Opcode %lu failed with status 0x%x\n"
+ "%s::%d:received systemPowerChange 0x%x\n"
+ "( 0 != fSystemPowerNotifier )"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Common/AppleNVMeBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Common/AppleNVMeController.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Common/AppleNVMeRequest.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Common/AppleNVMeRequestPool.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Common/AppleNVMeRequestPoolTagReserve.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Common/AppleNVMeRequestTimer.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Common/AppleNVMeSMARTUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Common/AppleNVMeWorkLoop.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Common/IONVMeBlockStorageDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Common/IONVMeController.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Common/IONVMeControllerPolledAdapter.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleANS2CGNVMeController.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleANS2CGv2Controller.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleANS2NVMeController.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleANS3CGv2Controller.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleANS3NVMeController.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeController.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeDiagnostics.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeNVRAM.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeTemperatureSensor.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleNVMeEAN.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleNVMeEANUC.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleNVMeFWNamespaceDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleNVMeFWNamespaceUC.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleNVMeNamespaceDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleNVMeNamespaceUC.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleNVMeUpdateUC.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/IOEmbeddedNVMeBlockDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/IONVMeEffaceableDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/IONVMeLifeboatBlockDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/NVMeSEPNotifier.cpp"
+ "121111121222121211211111111221222111111111112222112122222222222121111111222221122221211111111111111111111111111111111222122212211111111111221112111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222112122112111111111111111112111112111121121121111111111111112212122"
+ "12111112122212121121111111122122211111111111222211212222222222212111111122222112222121111111111111111111111111111111122212221221111111111122111211111111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222211212211211111111111111111211111211112112112111111111111111221212212"
+ "IOReturn AppleANS2NVMeController::SendSleepNotificationToANS(uint32_t, bool *)"
+ "virtual IOReturn AppleANS2NVMeController::systemPowerChange(void *, UInt32, IOService *, void *, vm_size_t)"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Common/AppleNVMeBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Common/AppleNVMeController.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Common/AppleNVMeRequest.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Common/AppleNVMeRequestPool.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Common/AppleNVMeRequestPoolTagReserve.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Common/AppleNVMeRequestTimer.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Common/AppleNVMeSMARTUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Common/AppleNVMeWorkLoop.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Common/IONVMeBlockStorageDevice.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Common/IONVMeController.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Common/IONVMeControllerPolledAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleANS2CGNVMeController.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleANS2CGv2Controller.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleANS2NVMeController.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleANS3CGv2Controller.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleANS3NVMeController.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeController.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeDiagnostics.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeNVRAM.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeTemperatureSensor.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleNVMeEAN.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleNVMeEANUC.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleNVMeFWNamespaceDevice.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleNVMeFWNamespaceUC.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleNVMeNamespaceDevice.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleNVMeNamespaceUC.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/AppleNVMeUpdateUC.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/IOEmbeddedNVMeBlockDevice.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/IONVMeEffaceableDevice.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/IONVMeLifeboatBlockDevice.cpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IONVMeFamily/Embedded/NVMeSEPNotifier.cpp"
- "1211111212221212112111111112212221111111111122221121222222222221211111112222211222212111111111111111111111111111111112221222122111111111112211121111111111111111111111111111111111111111111111111111111111111111222222222222222222222222222222222221121221121111111111111111121111121111211211211111111111111122122"
- "121111121222121211211111111221222111111111112222112122222222222121111111222221122221211111111111111111111111111111111222122212211111111111221112111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222112122112111111111111111112111112111121121121111111111111112212212"

```

>  `com.apple.iokit.IOSCSIArchitectureModelFamily`

```diff

-500.101.1.0.0
+500.120.1.0.0
   __TEXT.__cstring: 0x1676
   __TEXT.__const: 0x18
-  __TEXT_EXEC.__text: 0x1b378
+  __TEXT_EXEC.__text: 0x1b2e8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x468
   __DATA.__common: 0x1f0
Symbols:
+ __ZZN18IOSCSITargetDevice17CreateLogicalUnitEPhE21kalloc_type_view_2854
+ __ZZN18IOSCSITargetDevice17CreateLogicalUnitEPhE21kalloc_type_view_2901
+ __ZZN18IOSCSITargetDevice17PerformREPORTLUNSEvE21kalloc_type_view_1053
+ __ZZN18IOSCSITargetDevice17PerformREPORTLUNSEvE21kalloc_type_view_1102
+ __ZZN18IOSCSITargetDevice19ScanForLogicalUnitsEvE21kalloc_type_view_1012
+ __ZZN18IOSCSITargetDevice32PublishDefaultINQUIRYInformationEvE21kalloc_type_view_1882
+ __ZZN18IOSCSITargetDevice32PublishDefaultINQUIRYInformationEvE21kalloc_type_view_1930
+ __ZZN18IOSCSITargetDevice32PublishDefaultINQUIRYInformationEvE21kalloc_type_view_1942
- __ZZN18IOSCSITargetDevice17CreateLogicalUnitEPhE21kalloc_type_view_2872
- __ZZN18IOSCSITargetDevice17CreateLogicalUnitEPhE21kalloc_type_view_2919
- __ZZN18IOSCSITargetDevice17PerformREPORTLUNSEvE21kalloc_type_view_1071
- __ZZN18IOSCSITargetDevice17PerformREPORTLUNSEvE21kalloc_type_view_1120
- __ZZN18IOSCSITargetDevice19ScanForLogicalUnitsEvE21kalloc_type_view_1030
- __ZZN18IOSCSITargetDevice32PublishDefaultINQUIRYInformationEvE21kalloc_type_view_1900
- __ZZN18IOSCSITargetDevice32PublishDefaultINQUIRYInformationEvE21kalloc_type_view_1948
- __ZZN18IOSCSITargetDevice32PublishDefaultINQUIRYInformationEvE21kalloc_type_view_1960

```

>  `com.apple.iokit.IOSCSIBlockCommandsDevice`

```diff

-500.101.1.0.0
+500.120.1.0.0
   __TEXT.__const: 0x1c0
   __TEXT.__cstring: 0xc1f
-  __TEXT_EXEC.__text: 0x14e68
+  __TEXT_EXEC.__text: 0x14e1c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2a8
   __DATA.__common: 0x160
   __DATA.__bss: 0x4
-  __DATA_CONST.__auth_got: 0x3e0
+  __DATA_CONST.__auth_got: 0x3d8
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__mod_init_func: 0x40
   __DATA_CONST.__mod_term_func: 0x40

   __DATA_CONST.__kalloc_type: 0x580
   __LINKINFO.__symbolsets: 0x4ba4
   Functions: 505
-  Symbols:   1228
+  Symbols:   1227
   CStrings:  123
 
Symbols:
- __ZN27IOSCSIPrimaryCommandsDevice23IsDeviceAccessSuspendedEv

```

>  `com.apple.kernel`

```diff

-11417.101.15.0.0
-  __TEXT.__const: 0x36330
+11417.120.80.501.1
+  __TEXT.__const: 0x362f0
   __TEXT.__copyio_vectors: 0x120
-  __TEXT.__cstring: 0x98dce
-  __TEXT.__os_log: 0x2a769
+  __TEXT.__cstring: 0x98f96
+  __TEXT.__os_log: 0x2a7b5
   __TEXT.__thread_starts: 0x0
   __TEXT.__eh_frame: 0x4e0
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__mod_init_func: 0x2d8
-  __DATA_CONST.__const: 0x177e88
+  __DATA_CONST.__const: 0x177e38
   __DATA_CONST.__hib_const: 0x6b8
-  __DATA_CONST.__sdt_cstring: 0x6ab5
-  __DATA_CONST.__sdt: 0x111a8
+  __DATA_CONST.__sdt_cstring: 0x6acc
+  __DATA_CONST.__sdt: 0x11010
   __DATA_CONST.__kalloc_type: 0x16940
   __DATA_CONST.__kalloc_var: 0x82f0
-  __DATA_CONST.__assert: 0xf0
-  __DATA_CONST.__brk_desc: 0x60
+  __DATA_CONST.__assert: 0x1cc
+  __DATA_CONST.__brk_desc: 0x78
   __TEXT_EXEC.__hib_text: 0x3f88
-  __TEXT_EXEC.__text: 0x9074b4
+  __TEXT_EXEC.__text: 0x904790
   __TEXT_EXEC.__commpage_text: 0x2dc
   __KLD.__text: 0xb0d8
   __PPLTEXT.__text: 0x2bc88

   __DATA.__data: 0x20781
   __DATA.__lock_grp: 0x15dc8
   __DATA.__percpu: 0x3a50
-  __DATA.__common: 0x7e888
+  __DATA.__common: 0x7e868
   __DATA.__bss: 0x399a8
   __HIBDATA.__data: 0x31
   __HIBDATA.__common: 0x120
   __HIBDATA.__bss: 0x660
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__init: 0x5ba58
-  __BOOTDATA.__init_entry_set: 0x119d0
+  __BOOTDATA.__init: 0x5ba60
+  __BOOTDATA.__init_entry_set: 0x119e8
   __BOOTDATA.__static_ifinit: 0x8
   __BOOTDATA.__static_if: 0x0
   __PRELINK_TEXT.__text: 0x0

   __PLK_DATA_CONST.__data: 0x0
   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
-  __LINKINFO.__symbolsets: 0x4e10e
+  __LINKINFO.__symbolsets: 0x4e13a
   __CTF.__ctf: 0x0
-  Functions: 21763
-  Symbols:   6756
-  CStrings:  23476
+  Functions: 21777
+  Symbols:   6757
+  CStrings:  23482
 
Symbols:
+ _exclaves_sensor_tick_rate
CStrings:
+ "!os_add_overflow(*__counter, 1, __counter)"
+ "!os_sub_overflow(*__counter, 1, __counter)"
+ "!os_sub_overflow(*__counter, list.vmpl_count, __counter)"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/xnu/install/TempContent/Objects/EXPORT_HDRS/bsd/skywalk/nexus_common.h"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/xnu/install/TempContent/Objects/EXPORT_HDRS/bsd/skywalk/packet_common.h"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/dev/dtrace/dtrace.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kern_control.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kern_event.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kpi_mbuf.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kpi_socket.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kpi_socketfilter.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/socket_flows.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/subr_eventhandler.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/sys_domain.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/tracker.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_domain.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_mbuf.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_mbuf2.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_proto.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_socket.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_socket2.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_syscalls.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_usrreq.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/vsock_domain.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/bpf.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/classq/classq.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/classq/classq_fq_codel.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/classq/classq_subr.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/content_filter.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/dlil.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/dlil_ctl.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/dlil_input.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/dlil_output.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/dlil_subr.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/droptap.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/flowadv.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_bond.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_bridge.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_fake.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_ipsec.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_llreach.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_loop.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_ports_used.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_redirect.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_utun.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_vlan.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/iptap.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/kpi_interface.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/mblist.h"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/nat464_utils.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/ndrv.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/necp_client.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/net_thread_marks.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/network_agent.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/ntstat.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/nwk_wq.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_if.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_ioctl.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_norm.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_pbuf.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_table.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktap.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktsched/pktsched.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktsched/pktsched_fq_codel.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktsched/pktsched_netem.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/route.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/rtsock.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/flow_divert.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/igmp.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_arp.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_mcast.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_pcb.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_proto.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_rmx.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_tclass.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_dummynet.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_encap.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_icmp.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_input.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_output.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/kpi_ipfilter.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mp_pcb.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mp_pcb.h"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mp_proto.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_opt.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_subr.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_timer.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_usrreq.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_var.h"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/raw_ip.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_cache.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_cubic.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_input.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_ledbat.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_output.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_prague.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_sack.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_subr.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_timer.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_usrreq.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/udp_usrreq.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ah_core.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ah_input.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ah_output.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_chachapoly.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_core.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_input.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_output.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_rijndael.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/frag6.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/icmp6.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_cga.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_ifattach.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_mcast.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_pcb.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_proto.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_rmx.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_src.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_forward.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_id.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_input.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_output.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ipsec.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ipsec.h"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/mld6.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_nbr.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_prproxy.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_rti.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_rtr.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_send.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/scope6.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/udp6_output.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netkey/key.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netkey/keysock.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel_kern.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel_ring.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel_syscalls.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/core/skywalk.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/lib/net_filter_event.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_arena.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_cache.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_cache_var.h"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_region.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_slab.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/namespace/flowidns.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/namespace/netns.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/namespace/protons.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_agg.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_classifier.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_entry.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_manager.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_owner.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_route.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_stats.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_track.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_var.h"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_classq.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_dp.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_ethernet.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_ip_frag.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_vp.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/nx_flowswitch.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/kpipe/nx_kernel_pipe.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/monitor/nx_monitor.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_compat.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_compat.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_native.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_vp.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_flow.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_gso.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_host.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_llink.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_mit.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_poll.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_util.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_vp.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_adapter.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_adapter.h"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_kern.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_mbq.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_mbq.h"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_pktq.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_pktq.h"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_traffic_rule.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/upipe/nx_user_pipe.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/packet_copy.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/packet_kern.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/pbufpool.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/pbufpool_kern.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/xnu/iokit/Kernel/IODeviceTreeSupport.cpp"
+ "B16@?0^{task={lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}[4^{ipc_port}]^{ipc_port}^{ipc_port}[14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^vQQC{?=QQAQQ}BB^Q^Q^Q^Q^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQIBBBBb4b4b4b4CCCCB*^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b17}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b29}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27b1b1b1b1b28^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}b16b1b1b1b1b1b1b1[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]Q^vIQ{queue_entry=^{queue_entry}^{queue_entry}}iIQ[16C]Q^{_vmobject_list_output_}Q^{vm_deferred_reclamation_metadata_s}Q{task_security_config=(?={?=b1b1b1}C)}}8"
+ "Failed to add the security config string with error %d\n"
+ "Failed to set up ktriage for VM sanitization. @%s:%d"
+ "com.apple.private.enable-coredump-on-panic-seed-privacy-approved"
+ "memorystatus_kill_on_zone_map_exhaustion: failed to allocate jetsam reason\n"
+ "qset__not__initialized"
+ "security_config="
+ "security_config=0x%x"
+ "should not modify CPU free_pages while hibernating @%s:%d"
+ "should not modify cpu->free_pages while hibernating @%s:%d"
+ "stackshot_te_flags_mask"
+ "thread_group_clear_flags: Invalid flags %u @%s:%d"
+ "v16@?0^{vm_page=(?={vm_page_packed_queue_entry=II}^{vm_page}){vm_page_packed_queue_entry=II}{vm_page_packed_queue_entry=II}IIQ(?=SS){?=b4b2b1b1}{?=b1b1b1b1b1b1b1b1}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b4b4b4b1b1}8"
+ "vm_sanitize_telemetry.c"
- "%s: disallowing arm64e binary with invalid RO range\n"
- "%s: disallowing arm64e binary with invalid dynlinker RO range\n"
- "%s: entitlement is not OSBoolean @%s:%d"
- "%s:%d should not modify cpu->free_pages while hibernating @%s:%d"
- "(u_int)off <= pbuf->pb_packet_len"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/xnu/install/TempContent/Objects/EXPORT_HDRS/bsd/skywalk/nexus_common.h"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/xnu/install/TempContent/Objects/EXPORT_HDRS/bsd/skywalk/packet_common.h"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/dev/dtrace/dtrace.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kern_control.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kern_event.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kpi_mbuf.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kpi_socket.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kpi_socketfilter.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/socket_flows.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/subr_eventhandler.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/sys_domain.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/tracker.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_domain.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_mbuf.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_mbuf2.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_proto.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_socket.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_socket2.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_syscalls.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_usrreq.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/vsock_domain.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/bpf.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/classq/classq.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/classq/classq_fq_codel.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/classq/classq_subr.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/content_filter.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/dlil.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/dlil_ctl.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/dlil_input.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/dlil_output.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/dlil_subr.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/droptap.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/flowadv.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_bond.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_bridge.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_fake.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_ipsec.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_llreach.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_loop.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_ports_used.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_redirect.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_utun.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_vlan.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/iptap.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/kpi_interface.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/mblist.h"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/nat464_utils.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/ndrv.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/necp_client.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/net_thread_marks.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/network_agent.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/ntstat.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/nwk_wq.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_if.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_ioctl.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_norm.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_pbuf.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_table.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktap.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktsched/pktsched.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktsched/pktsched_fq_codel.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktsched/pktsched_netem.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/route.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/rtsock.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/flow_divert.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/igmp.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_arp.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_mcast.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_pcb.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_proto.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_rmx.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_tclass.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_dummynet.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_encap.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_icmp.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_input.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_output.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/kpi_ipfilter.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mp_pcb.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mp_pcb.h"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mp_proto.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_opt.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_subr.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_timer.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_usrreq.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_var.h"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/raw_ip.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_cache.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_cubic.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_input.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_ledbat.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_output.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_prague.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_sack.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_subr.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_timer.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_usrreq.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/udp_usrreq.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ah_core.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ah_input.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ah_output.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_chachapoly.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_core.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_input.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_output.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_rijndael.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/frag6.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/icmp6.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_cga.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_ifattach.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_mcast.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_pcb.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_proto.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_rmx.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_src.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_forward.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_id.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_input.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_output.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ipsec.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ipsec.h"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/mld6.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_nbr.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_prproxy.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_rti.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_rtr.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_send.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/scope6.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/udp6_output.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netkey/key.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netkey/keysock.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel_kern.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel_ring.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel_syscalls.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/core/skywalk.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/lib/net_filter_event.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_arena.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_cache.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_cache_var.h"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_region.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_slab.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/namespace/flowidns.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/namespace/netns.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/namespace/protons.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_agg.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_classifier.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_entry.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_manager.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_owner.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_route.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_stats.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_track.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_var.h"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_classq.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_dp.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_ethernet.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_ip_frag.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_vp.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/nx_flowswitch.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/kpipe/nx_kernel_pipe.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/monitor/nx_monitor.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_compat.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_compat.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_native.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_vp.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_flow.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_gso.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_host.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_llink.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_mit.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_poll.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_util.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_vp.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_adapter.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_adapter.h"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_kern.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_mbq.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_mbq.h"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_pktq.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_pktq.h"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_traffic_rule.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/upipe/nx_user_pipe.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/packet_copy.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/packet_kern.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/pbufpool.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/pbufpool_kern.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/iokit/Kernel/IODeviceTreeSupport.cpp"
- "B16@?0^{task={lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}[4^{ipc_port}]^{ipc_port}^{ipc_port}[14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^vQQC{?=QQAQQ}BB^Q^Q^Q^Q^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQIBBBBb4b4b4b4CCCCB*^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b17}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b29}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27b1b1b1b1b28^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}b16b1b1b1b1b1b1b1[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]Q^vIQ{queue_entry=^{queue_entry}^{queue_entry}}iIQ[16C]Q^{_vmobject_list_output_}Q^{vm_deferred_reclamation_metadata_s}Q}8"
- "Failed to add hardened heap string with error %d\n"
- "IN_ARE_ADDR_EQUAL(&odst->natv4addr, &iph2->ip_src)"
- "IOVnodeGetBooleanEntitlement"
- "available"
- "hardened_heap=1"
- "vm_page_grab_options_internal"

```

>  `com.apple.security.sandbox`

```diff

-2401.101.1.0.0
+2401.120.9.0.0
   __TEXT.__os_log: 0x1d47
-  __TEXT.__const: 0x1e5a3
+  __TEXT.__const: 0x1ef5f
   __TEXT.__cstring: 0x7626
   __TEXT_EXEC.__text: 0x45244
   __TEXT_EXEC.__auth_stubs: 0x0

```

</details>

## MachO

### 🆕 NEW (8)

- `/System/Library/CoreServices/Apple Diagnostics.app/Contents/MacOS/Apple Diagnostics`
- `/System/Library/CoreServices/diagnosticservicesd`
- `/System/Library/ExtensionKit/Extensions/MessageCenterApplicationServiceDiscoveryExtension.appex/Contents/MacOS/MessageCenterApplicationServiceDiscoveryExtension`
- `/System/Library/ExtensionKit/Extensions/PRIMLCKPreemptivePing.appex/Contents/MacOS/PRIMLCKPreemptivePing`
- `/System/Library/ExtensionKit/Extensions/ZeoliteEvalExtension.appex/Contents/MacOS/ZeoliteEvalExtension`
- `/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorBundlore`
- `/usr/libexec/diagnosticspushd`
- `/usr/libexec/memoryanalyticsd`

### ❌ Removed (2)

- `/System/Library/ExtensionKit/Extensions/IEMetricsWorker.appex/Contents/MacOS/IEMetricsWorker`
- `/System/Library/ExtensionKit/Extensions/ZeoliteExtension.appex/Contents/MacOS/ZeoliteExtension`

### ⬆️ Updated (490)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Applications/App Store.app/Contents/MacOS/App Store](MACHOS/App_Store.md)
- [/System/Applications/Books.app/Contents/Frameworks/AEBookPlugins.framework/Versions/A/AEBookPlugins](MACHOS/AEBookPlugins.md)
- [/System/Applications/Books.app/Contents/Frameworks/BlissReader.framework/Versions/A/BlissReader](MACHOS/BlissReader.md)
- [/System/Applications/Books.app/Contents/Frameworks/BookCore.framework/Versions/A/BookCore](MACHOS/BookCore.md)
- [/System/Applications/Books.app/Contents/Frameworks/BookEPUB.framework/Versions/A/BookEPUB](MACHOS/BookEPUB.md)
- [/System/Applications/Books.app/Contents/Frameworks/BookStoreUI.framework/Versions/A/BookStoreUI](MACHOS/BookStoreUI.md)
- [/System/Applications/Books.app/Contents/Frameworks/BooksPersonalization.framework/Versions/A/BooksPersonalization](MACHOS/BooksPersonalization.md)
- [/System/Applications/Books.app/Contents/Frameworks/BooksUI.framework/Versions/A/BooksUI](MACHOS/BooksUI.md)
- [/System/Applications/Books.app/Contents/MacOS/Books](MACHOS/Books.md)
- [/System/Applications/Books.app/Contents/PlugIns/AppKitUtilities.bundle/Contents/MacOS/AppKitUtilities](MACHOS/AppKitUtilities.md)
- [/System/Applications/Calculator.app/Contents/MacOS/Calculator](MACHOS/Calculator.md)
- [/System/Applications/Calendar.app/Contents/MacOS/Calendar](MACHOS/Calendar.md)
- [/System/Applications/Clock.app/Contents/PlugIns/WorldClockWidget.appex/Contents/MacOS/WorldClockWidget](MACHOS/WorldClockWidget.md)
- [/System/Applications/FaceTime.app/Contents/Frameworks/FaceTimeSettingsUI.framework/Versions/A/FaceTimeSettingsUI](MACHOS/FaceTimeSettingsUI.md)
- [/System/Applications/FaceTime.app/Contents/MacOS/FaceTime](MACHOS/FaceTime.md)
- [/System/Applications/FindMy.app/Contents/Frameworks/FindMyAppCore.framework/Versions/A/FindMyAppCore](MACHOS/FindMyAppCore.md)
- [/System/Applications/FindMy.app/Contents/MacOS/FindMy](MACHOS/FindMy.md)
- [/System/Applications/FindMy.app/Contents/PlugIns/FindMyNotificationsService.appex/Contents/MacOS/FindMyNotificationsService](MACHOS/FindMyNotificationsService.md)
- [/System/Applications/FindMy.app/Contents/PlugIns/FindMyWidgetItems.appex/Contents/MacOS/FindMyWidgetItems](MACHOS/FindMyWidgetItems.md)
- [/System/Applications/FindMy.app/Contents/PlugIns/FindMyWidgetPeople.appex/Contents/MacOS/FindMyWidgetPeople](MACHOS/FindMyWidgetPeople.md)
- [/System/Applications/Font Book.app/Contents/MacOS/Font Book](MACHOS/Font_Book.md)
- [/System/Applications/Freeform.app/Contents/MacOS/Freeform](MACHOS/Freeform.md)
- [/System/Applications/Freeform.app/Contents/PlugIns/FreeformSharingExtension.appex/Contents/MacOS/FreeformSharingExtension](MACHOS/FreeformSharingExtension.md)
- [/System/Applications/Home.app/Contents/PlugIns/HomeEnergyWidgetsExtension.appex/Contents/MacOS/HomeEnergyWidgetsExtension](MACHOS/HomeEnergyWidgetsExtension.md)
- [/System/Applications/Maps.app/Contents/MacOS/Maps](MACHOS/Maps.md)
- [/System/Applications/Music.app/Contents/MacOS/Music](MACHOS/Music.md)
- [/System/Applications/Music.app/Contents/PlugIns/MusicCacheExtension.appex/Contents/MacOS/MusicCacheExtension](MACHOS/MusicCacheExtension.md)
- [/System/Applications/Music.app/Contents/PlugIns/MusicStorageExtension.appex/Contents/MacOS/MusicStorageExtension](MACHOS/MusicStorageExtension.md)
- [/System/Applications/Music.app/Contents/PlugIns/com.apple.Music.web.bundle/Contents/MacOS/com.apple.Music.web](MACHOS/com.apple.Music.web.md)
- [/System/Applications/News.app/Contents/MacOS/News](MACHOS/News.md)
- [/System/Applications/News.app/Contents/PlugIns/NewsTodayIntents.appex/Contents/MacOS/NewsTodayIntents](MACHOS/NewsTodayIntents.md)
- [/System/Applications/Notes.app/Contents/MacOS/Notes](MACHOS/Notes.md)
- [/System/Applications/Notes.app/Contents/PlugIns/com.apple.Notes.QuickLookExtension.appex/Contents/MacOS/com.apple.Notes.QuickLookExtension](MACHOS/com.apple.Notes.QuickLookExtension.md)
- [/System/Applications/Notes.app/Contents/PlugIns/com.apple.Notes.WidgetExtension.appex/Contents/MacOS/com.apple.Notes.WidgetExtension](MACHOS/com.apple.Notes.WidgetExtension.md)
- [/System/Applications/Photos.app/Contents/MacOS/Photos](MACHOS/Photos.md)
- [/System/Applications/Photos.app/Contents/PlugIns/PhotosReliveWidget.appex/Contents/MacOS/PhotosReliveWidget](MACHOS/PhotosReliveWidget.md)
- [/System/Applications/Podcasts.app/Contents/Frameworks/NowPlayingUI.framework/Versions/A/NowPlayingUI](MACHOS/NowPlayingUI.md)
- [/System/Applications/Podcasts.app/Contents/Frameworks/ShelfKit.framework/Versions/A/ShelfKit](MACHOS/ShelfKit.md)
- [/System/Applications/Podcasts.app/Contents/Frameworks/ShelfKitCollectionViews.framework/Versions/A/ShelfKitCollectionViews](MACHOS/ShelfKitCollectionViews.md)
- [/System/Applications/Podcasts.app/Contents/MacOS/Podcasts](MACHOS/Podcasts.md)
- [/System/Applications/Preview.app/Contents/MacOS/Preview](MACHOS/Preview.md)
- [/System/Applications/Reminders.app/Contents/MacOS/Reminders](MACHOS/Reminders.md)
- [/System/Applications/Reminders.app/Contents/PlugIns/RemindersIntentsExtension.appex/Contents/MacOS/RemindersIntentsExtension](MACHOS/RemindersIntentsExtension.md)
- [/System/Applications/Reminders.app/Contents/PlugIns/RemindersWidgetExtension.appex/Contents/MacOS/RemindersWidgetExtension](MACHOS/RemindersWidgetExtension.md)
- [/System/Applications/Shortcuts.app/Contents/MacOS/Shortcuts](MACHOS/Shortcuts.md)
- [/System/Applications/Shortcuts.app/Contents/PlugIns/ShortcutsWidgetExtension.appex/Contents/MacOS/ShortcutsWidgetExtension](MACHOS/ShortcutsWidgetExtension.md)
- [/System/Applications/Stocks.app/Contents/MacOS/Stocks](MACHOS/Stocks.md)
- [/System/Applications/System Settings.app/Contents/MacOS/System Settings](MACHOS/System_Settings.md)
- [/System/Applications/System Settings.app/Contents/PlugIns/csimporter.appex/Contents/MacOS/csimporter](MACHOS/csimporter.md)
- [/System/Applications/TV.app/Contents/MacOS/TV](MACHOS/TV.md)
- [/System/Applications/TV.app/Contents/PlugIns/TVCacheExtension.appex/Contents/MacOS/TVCacheExtension](MACHOS/TVCacheExtension.md)
- [/System/Applications/TV.app/Contents/PlugIns/TVStorageExtension.appex/Contents/MacOS/TVStorageExtension](MACHOS/TVStorageExtension.md)
- [/System/Applications/TV.app/Contents/PlugIns/com.apple.TV.web.bundle/Contents/MacOS/com.apple.TV.web](MACHOS/com.apple.TV.web.md)
- [/System/Applications/Tips.app/Contents/MacOS/Tips](MACHOS/Tips.md)
- [/System/Applications/Utilities/Boot Camp Assistant.app/Contents/MacOS/Boot Camp Assistant](MACHOS/Boot_Camp_Assistant.md)
- [/System/Applications/Utilities/Console.app/Contents/MacOS/Console](MACHOS/Console.md)
- [/System/Applications/Utilities/Print Center.app/Contents/MacOS/Print Center](MACHOS/Print_Center.md)
- [/System/Applications/Utilities/Screen Sharing.app/Contents/MacOS/Screen Sharing](MACHOS/Screen_Sharing.md)
- [/System/Applications/Utilities/VoiceOver Utility.app/Contents/MacOS/VoiceOver Utility](MACHOS/VoiceOver_Utility.md)
- [/System/Applications/Utilities/VoiceOver Utility.app/Contents/OtherBinaries/VoiceOverUtilityCacheBuilder.app/Contents/MacOS/VoiceOver Utility](MACHOS/VoiceOver_Utility.md)
- [/System/Applications/VoiceMemos.app/Contents/MacOS/VoiceMemos](MACHOS/VoiceMemos.md)
- [/System/Applications/Weather.app/Contents/Library/LoginItems/WeatherMenu.app/Contents/MacOS/WeatherMenu](MACHOS/WeatherMenu.md)
- [/System/Applications/Weather.app/Contents/MacOS/Weather](MACHOS/Weather.md)
- [/System/Applications/Weather.app/Contents/PlugIns/WeatherWidget.appex/Contents/MacOS/WeatherWidget](MACHOS/WeatherWidget.md)
- [/System/Applications/iPhone Mirroring.app/Contents/Frameworks/ScreenContinuityUI.framework/Versions/A/ScreenContinuityUI](MACHOS/ScreenContinuityUI.md)
- [/System/Library/Accounts/SwiftUI/iCloudSwiftUIPlugin.bundle/Contents/MacOS/iCloudSwiftUIPlugin](MACHOS/iCloudSwiftUIPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/CoreDynamicUIPlugin.bundle/Contents/MacOS/CoreDynamicUIPlugin](MACHOS/CoreDynamicUIPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/Contents/MacOS/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/iCloudDynamicUIPlugin.bundle/Contents/MacOS/iCloudDynamicUIPlugin](MACHOS/iCloudDynamicUIPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/MacOS/AudioFlowDelegatePlugin](MACHOS/AudioFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/DailyBriefingFlowPlugin.bundle/Contents/MacOS/DailyBriefingFlowPlugin](MACHOS/DailyBriefingFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EmergencyFlowPlugin.bundle/Contents/MacOS/EmergencyFlowPlugin](MACHOS/EmergencyFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HealthFlowDelegatePlugin.bundle/Contents/MacOS/HealthFlowDelegatePlugin](MACHOS/HealthFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/MacOS/IFFlowPlugin](MACHOS/IFFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/MacOS/InformationFlowPlugin](MACHOS/InformationFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PCSReadingFlowDelegatePlugin.bundle/Contents/MacOS/PCSReadingFlowDelegatePlugin](MACHOS/PCSReadingFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Contents/MacOS/PhoneCallFlowDelegatePlugin](MACHOS/PhoneCallFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SettingsFlowDelegatePlugin.bundle/Contents/MacOS/SettingsFlowDelegatePlugin](MACHOS/SettingsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriLinkFlowPlugin.bundle/Contents/MacOS/SiriLinkFlowPlugin](MACHOS/SiriLinkFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Contents/MacOS/SocialConversationFlowDelegatePlugin](MACHOS/SocialConversationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/TimerFlowDelegatePlugin.bundle/Contents/MacOS/TimerFlowDelegatePlugin](MACHOS/TimerFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Contents/MacOS/WellnessFlowPlugin](MACHOS/WellnessFlowPlugin.md)
- [/System/Library/Assistant/Plugins/activity.assistantBundle/Contents/MacOS/activity](MACHOS/activity.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningInferencePlugin.bundle/Contents/MacOS/SiriPrivateLearningInferencePlugin](MACHOS/SiriPrivateLearningInferencePlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningPatternExtractionPlugin.bundle/Contents/MacOS/SiriPrivateLearningPatternExtractionPlugin](MACHOS/SiriPrivateLearningPatternExtractionPlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningTTSMispronunciationPlugin.bundle/Contents/MacOS/SiriPrivateLearningTTSMispronunciationPlugin](MACHOS/SiriPrivateLearningTTSMispronunciationPlugin.md)
- [/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/Contents/MacOS/AVCHalogen](MACHOS/AVCHalogen.md)
- [/System/Library/Audio/Plug-Ins/HAL/AirPlay.driver/Contents/MacOS/AirPlay](MACHOS/AirPlay.md)
- [/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/Contents/MacOS/BTAudioHALPlugin](MACHOS/BTAudioHALPlugin.md)
- [/System/Library/Audio/Plug-Ins/HAL/ContinuityCaptureAudioPlugin.driver/Contents/MacOS/ContinuityCaptureAudioPlugin](MACHOS/ContinuityCaptureAudioPlugin.md)
- [/System/Library/Audio/Plug-Ins/HAL/MacAudio.driver/Contents/MacOS/MacAudio](MACHOS/MacAudio.md)
- [/System/Library/Components/AudioDSP.component/Contents/MacOS/AudioDSP](MACHOS/AudioDSP.md)
- [/System/Library/Components/CoreAudio.component/Contents/MacOS/CoreAudio](MACHOS/CoreAudio.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/Contents/MacOS/IOAccessoryManager](MACHOS/IOAccessoryManager.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/Contents/MacOS/USBHost](MACHOS/USBHost.md)
- [/System/Library/CoreImage/CIInpainting.cifilter/Contents/MacOS/CIInpainting](MACHOS/CIInpainting.md)
- [/System/Library/CoreServices/Applications/Desk View.app/Contents/MacOS/Desk View](MACHOS/Desk_View.md)
- [/System/Library/CoreServices/ControlCenter.app/Contents/MacOS/ControlCenter](MACHOS/ControlCenter.md)
- [/System/Library/CoreServices/ControlStrip.app/Contents/MacOS/ControlStrip](MACHOS/ControlStrip.md)
- [/System/Library/CoreServices/CoreServicesUIAgent.app/Contents/MacOS/CoreServicesUIAgent](MACHOS/CoreServicesUIAgent.md)
- [/System/Library/CoreServices/Coverage Details.app/Contents/MacOS/Coverage Details](MACHOS/Coverage_Details.md)
- [/System/Library/CoreServices/Diagnostics Reporter.app/Contents/MacOS/Diagnostics Reporter](MACHOS/Diagnostics_Reporter.md)
- [/System/Library/CoreServices/Dock.app/Contents/MacOS/Dock](MACHOS/Dock.md)
- [/System/Library/CoreServices/Enhanced Logging.app/Contents/MacOS/Enhanced Logging](MACHOS/Enhanced_Logging.md)
- [/System/Library/CoreServices/FileProvider-Feedback.app/Contents/MacOS/FileProvider-Feedback](MACHOS/FileProvider-Feedback.md)
- [/System/Library/CoreServices/Finder.app/Contents/MacOS/Finder](MACHOS/Finder.md)
- [/System/Library/CoreServices/KeyboardSetupAssistant.app/Contents/MacOS/KeyboardSetupAssistant](MACHOS/KeyboardSetupAssistant.md)
- [/System/Library/CoreServices/Keychain Circle Notification.app/Contents/MacOS/Keychain Circle Notification](MACHOS/Keychain_Circle_Notification.md)
- [/System/Library/CoreServices/MTLReplayer.app/Contents/Frameworks/MTLReplayController.framework/Versions/A/MTLReplayController](MACHOS/MTLReplayController.md)
- [/System/Library/CoreServices/Menu Extras/TimeMachine.menu/Contents/MacOS/TimeMachine](MACHOS/TimeMachine.md)
- [/System/Library/CoreServices/NotificationCenter.app/Contents/MacOS/NotificationCenter](MACHOS/NotificationCenter.md)
- [/System/Library/CoreServices/PIPAgent.app/Contents/MacOS/PIPAgent](MACHOS/PIPAgent.md)
- [/System/Library/CoreServices/PeopleMessageService.app/Contents/PlugIns/PeopleMessagesScreenTime.appex/Contents/MacOS/PeopleMessagesScreenTime](MACHOS/PeopleMessagesScreenTime.md)
- [/System/Library/CoreServices/PeopleViewService.app/Contents/MacOS/PeopleViewService](MACHOS/PeopleViewService.md)
- [/System/Library/CoreServices/PeopleViewService.app/Contents/PlugIns/PeopleWidget_macOSExtension.appex/Contents/MacOS/PeopleWidget_macOSExtension](MACHOS/PeopleWidget_macOSExtension.md)
- [/System/Library/CoreServices/ReportCrash](MACHOS/ReportCrash.md)
- [/System/Library/CoreServices/Screen Time.app/Contents/PlugIns/ScreenTimeWidgetExtension.appex/Contents/MacOS/ScreenTimeWidgetExtension](MACHOS/ScreenTimeWidgetExtension.md)
- [/System/Library/CoreServices/SecurityAgentPlugins/LocalAuthentication.bundle/Contents/MacOS/LocalAuthentication](MACHOS/LocalAuthentication.md)
- [/System/Library/CoreServices/Setup Assistant.app/Contents/MacOS/Setup Assistant](MACHOS/Setup_Assistant.md)
- [/System/Library/CoreServices/Spotlight.app/Contents/Extensions/SpotlightPreferenceExtension.appex/Contents/MacOS/SpotlightPreferenceExtension](MACHOS/SpotlightPreferenceExtension.md)
- [/System/Library/CoreServices/TimeMachine/backupd](MACHOS/backupd.md)
- [/System/Library/CoreServices/UAUPlugins/ScreenTimeUAU.bundle/Contents/MacOS/ScreenTimeUAU](MACHOS/ScreenTimeUAU.md)
- [/System/Library/CoreServices/UAUPlugins/SettingsUAUPlugin.bundle/Contents/Resources/IndexSettings](MACHOS/IndexSettings.md)
- [/System/Library/CoreServices/WidgetKit Simulator.app/Contents/MacOS/WidgetKit Simulator](MACHOS/WidgetKit_Simulator.md)
- [/System/Library/CoreServices/WindowManager.app/Contents/MacOS/WindowManager](MACHOS/WindowManager.md)
- [/System/Library/CoreServices/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/System/Library/CoreServices/loginwindow.app/Contents/MacOS/loginwindow](MACHOS/loginwindow.md)
- [/System/Library/CoreServices/powerd.bundle/powerd](MACHOS/powerd.md)
- [/System/Library/CoreServices/screencaptureui.app/Contents/MacOS/screencaptureui](MACHOS/screencaptureui.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-IOUserDockChannelSerial.dext/com.apple.DriverKit-IOUserDockChannelSerial](MACHOS/com.apple.DriverKit-IOUserDockChannelSerial.md)
- [/System/Library/ExtensionKit/Extensions/AccessibilitySettingsExtension.appex/Contents/MacOS/AccessibilitySettingsExtension](MACHOS/AccessibilitySettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/AirDropHandoffExtension.appex/Contents/MacOS/AirDropHandoffExtension](MACHOS/AirDropHandoffExtension.md)
- [/System/Library/ExtensionKit/Extensions/Appearance.appex/Contents/MacOS/Appearance](MACHOS/Appearance.md)
- [/System/Library/ExtensionKit/Extensions/AppleAccountIntents_macOS.appex/Contents/MacOS/AppleAccountIntents_macOS](MACHOS/AppleAccountIntents_macOS.md)
- [/System/Library/ExtensionKit/Extensions/AppleIDSettings.appex/Contents/MacOS/AppleIDSettings](MACHOS/AppleIDSettings.md)
- [/System/Library/ExtensionKit/Extensions/BiomeSELFIngestor.appex/Contents/MacOS/BiomeSELFIngestor](MACHOS/BiomeSELFIngestor.md)
- [/System/Library/ExtensionKit/Extensions/CDs & DVDs Settings Extension.appex/Contents/MacOS/CDs & DVDs Settings Extension](MACHOS/CDs_&_DVDs_Settings_Extension.md)
- [/System/Library/ExtensionKit/Extensions/ClassKitSettings.appex/Contents/MacOS/ClassKitSettings](MACHOS/ClassKitSettings.md)
- [/System/Library/ExtensionKit/Extensions/ControlCenterSettings.appex/Contents/MacOS/ControlCenterSettings](MACHOS/ControlCenterSettings.md)
- [/System/Library/ExtensionKit/Extensions/ControlCenterSettingsIntents.appex/Contents/MacOS/ControlCenterSettingsIntents](MACHOS/ControlCenterSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/CoverageSettings.appex/Contents/MacOS/CoverageSettings](MACHOS/CoverageSettings.md)
- [/System/Library/ExtensionKit/Extensions/DateAndTime Extension.appex/Contents/MacOS/DateAndTime Extension](MACHOS/DateAndTime_Extension.md)
- [/System/Library/ExtensionKit/Extensions/DesktopSettings.appex/Contents/MacOS/DesktopSettings](MACHOS/DesktopSettings.md)
- [/System/Library/ExtensionKit/Extensions/DesktopSettings.appex/Contents/Resources/DesktopSettingsScripting.scripting/Contents/MacOS/DesktopSettingsScripting](MACHOS/DesktopSettingsScripting.md)
- [/System/Library/ExtensionKit/Extensions/DisplaysExt.appex/Contents/MacOS/DisplaysExt](MACHOS/DisplaysExt.md)
- [/System/Library/ExtensionKit/Extensions/Drift.appex/Contents/MacOS/Drift](MACHOS/Drift.md)
- [/System/Library/ExtensionKit/Extensions/EventKitUIRemoteUIExtension.appex/Contents/MacOS/EventKitUIRemoteUIExtension](MACHOS/EventKitUIRemoteUIExtension.md)
- [/System/Library/ExtensionKit/Extensions/FedStatsMLHostPlugin.appex/Contents/MacOS/FedStatsMLHostPlugin](MACHOS/FedStatsMLHostPlugin.md)
- [/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassA.appex/Contents/MacOS/FedStatsMLHostPluginClassA](MACHOS/FedStatsMLHostPluginClassA.md)
- [/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassB.appex/Contents/MacOS/FedStatsMLHostPluginClassB](MACHOS/FedStatsMLHostPluginClassB.md)
- [/System/Library/ExtensionKit/Extensions/GMSSELFIngestor.appex/Contents/MacOS/GMSSELFIngestor](MACHOS/GMSSELFIngestor.md)
- [/System/Library/ExtensionKit/Extensions/GameControllerMacSettings.appex/Contents/MacOS/GameControllerMacSettings](MACHOS/GameControllerMacSettings.md)
- [/System/Library/ExtensionKit/Extensions/GenerativeAssistantExtension.appex/Contents/MacOS/GenerativeAssistantExtension](MACHOS/GenerativeAssistantExtension.md)
- [/System/Library/ExtensionKit/Extensions/GenerativeAssistantSettingsExtension.appex/Contents/MacOS/GenerativeAssistantSettingsExtension](MACHOS/GenerativeAssistantSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/HeadphoneSettingsExtension.appex/Contents/MacOS/HeadphoneSettingsExtension](MACHOS/HeadphoneSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/KeyboardSettings.appex/Contents/MacOS/KeyboardSettings](MACHOS/KeyboardSettings.md)
- [/System/Library/ExtensionKit/Extensions/Localization.appex/Contents/MacOS/Localization](MACHOS/Localization.md)
- [/System/Library/ExtensionKit/Extensions/LockScreen.appex/Contents/MacOS/LockScreen](MACHOS/LockScreen.md)
- [/System/Library/ExtensionKit/Extensions/LoginItemsIntentsExtension.appex/Contents/MacOS/LoginItemsIntentsExtension](MACHOS/LoginItemsIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MouseExtension.appex/Contents/MacOS/MouseExtension](MACHOS/MouseExtension.md)
- [/System/Library/ExtensionKit/Extensions/Network.appex/Contents/MacOS/Network](MACHOS/Network.md)
- [/System/Library/ExtensionKit/Extensions/NewDeviceOutreachIntents_macOS.appex/Contents/MacOS/NewDeviceOutreachIntents_macOS](MACHOS/NewDeviceOutreachIntents_macOS.md)
- [/System/Library/ExtensionKit/Extensions/NotificationsSettings.appex/Contents/MacOS/NotificationsSettings](MACHOS/NotificationsSettings.md)
- [/System/Library/ExtensionKit/Extensions/NotificationsSettingsIntents.appex/Contents/MacOS/NotificationsSettingsIntents](MACHOS/NotificationsSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/ODDIPoirotMetricsExtension.appex/Contents/MacOS/ODDIPoirotMetricsExtension](MACHOS/ODDIPoirotMetricsExtension.md)
- [/System/Library/ExtensionKit/Extensions/PowerPreferences.appex/Contents/MacOS/PowerPreferences](MACHOS/PowerPreferences.md)
- [/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/Contents/MacOS/PrivateEvolutionPlugin](MACHOS/PrivateEvolutionPlugin.md)
- [/System/Library/ExtensionKit/Extensions/RepackagingWorker.appex/Contents/MacOS/RepackagingWorker](MACHOS/RepackagingWorker.md)
- [/System/Library/ExtensionKit/Extensions/SafariAssistantWorker.appex/Contents/MacOS/SafariAssistantWorker](MACHOS/SafariAssistantWorker.md)
- [/System/Library/ExtensionKit/Extensions/Screen Saver.appex/Contents/MacOS/Screen Saver](MACHOS/Screen_Saver.md)
- [/System/Library/ExtensionKit/Extensions/ScreenTimePreferencesExtension.appex/Contents/MacOS/ScreenTimePreferencesExtension](MACHOS/ScreenTimePreferencesExtension.md)
- [/System/Library/ExtensionKit/Extensions/SecurityPrivacyExtension.appex/Contents/MacOS/SecurityPrivacyExtension](MACHOS/SecurityPrivacyExtension.md)
- [/System/Library/ExtensionKit/Extensions/Sharing.appex/Contents/MacOS/Sharing](MACHOS/Sharing.md)
- [/System/Library/ExtensionKit/Extensions/SiriPreferenceExtension.appex/Contents/MacOS/SiriPreferenceExtension](MACHOS/SiriPreferenceExtension.md)
- [/System/Library/ExtensionKit/Extensions/SoftwareUpdateSettingsExtension.appex/Contents/MacOS/SoftwareUpdateSettingsExtension](MACHOS/SoftwareUpdateSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/SpotlightPreferenceExtension.appex/Contents/MacOS/SpotlightPreferenceExtension](MACHOS/SpotlightPreferenceExtension.md)
- [/System/Library/ExtensionKit/Extensions/Storage.appex/Contents/MacOS/Storage](MACHOS/Storage.md)
- [/System/Library/ExtensionKit/Extensions/TimeMachineSettings.appex/Contents/MacOS/TimeMachineSettings](MACHOS/TimeMachineSettings.md)
- [/System/Library/ExtensionKit/Extensions/Touch ID & Password.appex/Contents/MacOS/Touch ID & Password](MACHOS/Touch_ID_&_Password.md)
- [/System/Library/ExtensionKit/Extensions/TrackpadExtension.appex/Contents/MacOS/TrackpadExtension](MACHOS/TrackpadExtension.md)
- [/System/Library/ExtensionKit/Extensions/TrackpadIntentsExtension.appex/Contents/MacOS/TrackpadIntentsExtension](MACHOS/TrackpadIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/UsersGroups.appex/Contents/MacOS/UsersGroups](MACHOS/UsersGroups.md)
- [/System/Library/ExtensionKit/Extensions/UsersGroupsIntentsExtension.appex/Contents/MacOS/UsersGroupsIntentsExtension](MACHOS/UsersGroupsIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/VPN.appex/Contents/MacOS/VPN](MACHOS/VPN.md)
- [/System/Library/ExtensionKit/Extensions/Wallpaper.appex/Contents/MacOS/Wallpaper](MACHOS/Wallpaper.md)
- [/System/Library/ExtensionKit/Extensions/Wi-Fi.appex/Contents/MacOS/Wi-Fi](MACHOS/Wi-Fi.md)
- [/System/Library/Extensions/AppleIntelGraphicsShared.bundle/Contents/MacOS/libigc.dylib](MACHOS/libigc.dylib.md)
- [/System/Library/Extensions/AppleIntelICLGraphicsGLDriver.bundle/Contents/MacOS/AppleIntelICLGraphicsGLDriver](MACHOS/AppleIntelICLGraphicsGLDriver.md)
- [/System/Library/Extensions/AppleIntelKBLGraphicsGLDriver.bundle/Contents/MacOS/AppleIntelKBLGraphicsGLDriver](MACHOS/AppleIntelKBLGraphicsGLDriver.md)
- [/System/Library/Filesystems/AppleShare/afpLoad](MACHOS/afpLoad.md)
- [/System/Library/Filesystems/AppleShare/check_afp.app/Contents/MacOS/check_afp](MACHOS/check_afp.md)
- [/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_condenser](MACHOS/apfs_condenser.md)
- [/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_invert](MACHOS/apfs_invert.md)
- [/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_prepare_cryptex](MACHOS/apfs_prepare_cryptex.md)
- [/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_vol_converter](MACHOS/apfs_vol_converter.md)
- [/System/Library/Filesystems/apfs.fs/Contents/Resources/fsck_apfs](MACHOS/fsck_apfs.md)
- [/System/Library/Filesystems/apfs.fs/Contents/Resources/hfs_convert](MACHOS/hfs_convert.md)
- [/System/Library/Filesystems/apfs.fs/Contents/Resources/newfs_apfs](MACHOS/newfs_apfs.md)
- [/System/Library/Frameworks/AppKit.framework/Versions/C/XPCServices/TrustedUIService.xpc/Contents/MacOS/TrustedUIService](MACHOS/TrustedUIService.md)
- [/System/Library/Frameworks/CFNetwork.framework/Versions/A/Support/AuthBrokerAgent](MACHOS/AuthBrokerAgent.md)
- [/System/Library/Frameworks/CoreMediaIO.framework/Versions/A/Resources/BaseUnits/CMIOBaseUnits.bundle/Contents/MacOS/CMIOBaseUnits](MACHOS/CMIOBaseUnits.md)
- [/System/Library/Frameworks/CoreMediaIO.framework/Versions/A/Resources/CinematicFramingOnboardingUI.app/Contents/MacOS/CinematicFramingOnboardingUI](MACHOS/CinematicFramingOnboardingUI.md)
- [/System/Library/Frameworks/CoreMediaIO.framework/Versions/A/Resources/ContinuityCaptureOnboardingUI.app/Contents/MacOS/ContinuityCaptureOnboardingUI](MACHOS/ContinuityCaptureOnboardingUI.md)
- [/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/coreimportd](MACHOS/coreimportd.md)
- [/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/corespotlightd](MACHOS/corespotlightd.md)
- [/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/managedcorespotlightd](MACHOS/managedcorespotlightd.md)
- [/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mdbulkimport](MACHOS/mdbulkimport.md)
- [/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mds](MACHOS/mds.md)
- [/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mdsync](MACHOS/mdsync.md)
- [/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mdworker](MACHOS/mdworker.md)
- [/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mdworker_shared](MACHOS/mdworker_shared.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged](MACHOS/spotlightknowledged.md)
- [/System/Library/Frameworks/CreateML.framework/Versions/A/CreateML](MACHOS/CreateML.md)
- [/System/Library/Frameworks/FamilyControls.framework/Versions/A/FamilyControlsAgent](MACHOS/FamilyControlsAgent.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechTouchId.bundle/Contents/MacOS/MechTouchId](MACHOS/MechTouchId.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd](MACHOS/coreauthd.md)
- [/System/Library/Frameworks/ManagedSettings.framework/Versions/A/ManagedSettingsAgent](MACHOS/ManagedSettingsAgent.md)
- [/System/Library/Frameworks/MediaExtension.framework/Versions/A/XPCServices/com.apple.MEValidationService.xpc/Contents/MacOS/com.apple.MEValidationService](MACHOS/com.apple.MEValidationService.md)
- [/System/Library/Frameworks/MediaToolbox.framework/Versions/A/XPCServices/MTPluginFormatReader.xpc/Contents/MacOS/MTPluginFormatReader](MACHOS/MTPluginFormatReader.md)
- [/System/Library/Frameworks/MediaToolbox.framework/Versions/A/XPCServices/MTPluginFormatReaderZonto.xpc/Contents/MacOS/MTPluginFormatReaderZonto](MACHOS/MTPluginFormatReaderZonto.md)
- [/System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/3425AMD/libLLVMContainer.dylib](MACHOS/libLLVMContainer.dylib.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitagent](MACHOS/storekitagent.md)
- [/System/Library/Frameworks/SystemExtensions.framework/Versions/A/Helpers/sysextd](MACHOS/sysextd.md)
- [/System/Library/Frameworks/WeatherKit.framework/Versions/A/XPCServices/com.apple.weatherkit.authservice.xpc/Contents/MacOS/com.apple.weatherkit.authservice](MACHOS/com.apple.weatherkit.authservice.md)
- [/System/Library/HIDPlugins/ServiceFilters/UniversalControlServiceFilter.plugin/Contents/MacOS/UniversalControlServiceFilter](MACHOS/UniversalControlServiceFilter.md)
- [/System/Library/Kernels/kernel](MACHOS/kernel.md)
- [/System/Library/Kernels/kernel.release.t6000](MACHOS/kernel.release.t6000.md)
- [/System/Library/Kernels/kernel.release.t6020](MACHOS/kernel.release.t6020.md)
- [/System/Library/Kernels/kernel.release.t6030](MACHOS/kernel.release.t6030.md)
- [/System/Library/Kernels/kernel.release.t6031](MACHOS/kernel.release.t6031.md)
- [/System/Library/Kernels/kernel.release.t6041](MACHOS/kernel.release.t6041.md)
- [/System/Library/Kernels/kernel.release.t8103](MACHOS/kernel.release.t8103.md)
- [/System/Library/Kernels/kernel.release.t8112](MACHOS/kernel.release.t8112.md)
- [/System/Library/Kernels/kernel.release.t8122](MACHOS/kernel.release.t8122.md)
- [/System/Library/Kernels/kernel.release.t8132](MACHOS/kernel.release.t8132.md)
- [/System/Library/Kernels/kernel.release.vmapple](MACHOS/kernel.release.vmapple.md)
- [/System/Library/Messages/PlugIns/iMessage.imservice/Contents/MacOS/iMessage](MACHOS/iMessage.md)
- [/System/Library/PreferenceBundles/AccountSettings/icloudMailSettings_macOS.bundle/Contents/MacOS/icloudMailSettings_macOS](MACHOS/icloudMailSettings_macOS.md)
- [/System/Library/PrivateFrameworks/AACCore.framework/Versions/A/XPCServices/AssessmentUIService.xpc/Contents/MacOS/AssessmentUIService](MACHOS/AssessmentUIService.md)
- [/System/Library/PrivateFrameworks/AMPDevices.framework/Versions/A/Support/AMPDeviceDiscoveryAgent](MACHOS/AMPDeviceDiscoveryAgent.md)
- [/System/Library/PrivateFrameworks/AMPDevices.framework/Versions/A/Support/AMPDevicesAgent](MACHOS/AMPDevicesAgent.md)
- [/System/Library/PrivateFrameworks/AMPDevices.framework/Versions/A/XPCServices/com.apple.amp.devicesui.xpc/Contents/MacOS/com.apple.amp.devicesui](MACHOS/com.apple.amp.devicesui.md)
- [/System/Library/PrivateFrameworks/AMPLibrary.framework/Versions/A/Support/AMPArtworkAgent](MACHOS/AMPArtworkAgent.md)
- [/System/Library/PrivateFrameworks/AMPLibrary.framework/Versions/A/Support/AMPLibraryAgent](MACHOS/AMPLibraryAgent.md)
- [/System/Library/PrivateFrameworks/AMPSharing.framework/Versions/A/PlugIns/SharingPrefsExtension.appex/Contents/MacOS/SharingPrefsExtension](MACHOS/SharingPrefsExtension.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/Versions/A/XPCServices/ASOctaneSupportXPCService.xpc/Contents/MacOS/ASOctaneSupportXPCService](MACHOS/ASOctaneSupportXPCService.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd](MACHOS/appstorecomponentsd.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstoreagent](MACHOS/appstoreagent.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/Versions/A/Resources/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/UtilityExtension.appex/Contents/MacOS/UtilityExtension](MACHOS/UtilityExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/Versions/A/AppleMediaServicesUIDynamic](MACHOS/AppleMediaServicesUIDynamic.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/PlugIns/RAQLPreviewExtension.appex/Contents/MacOS/RAQLPreviewExtension](MACHOS/RAQLPreviewExtension.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/Versions/A/XPCServices/RAQL-Inline-Service.xpc/Contents/MacOS/RAQL-Inline-Service](MACHOS/RAQL-Inline-Service.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/Support/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/Bootability.framework/Versions/A/XPCServices/BootabilityService.xpc/Contents/MacOS/BootabilityService](MACHOS/BootabilityService.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted_helper](MACHOS/deleted_helper.md)
- [/System/Library/PrivateFrameworks/CloudSharing.framework/Versions/A/XPCServices/SPIHelper.xpc/Contents/MacOS/SPIHelper](MACHOS/SPIHelper.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/Versions/A/PlugIns/CloudSharingUISKExtension.appex/Contents/MacOS/CloudSharingUISKExtension](MACHOS/CloudSharingUISKExtension.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/Versions/A/XPCServices/ManageViewService.xpc/Contents/MacOS/ManageViewService](MACHOS/ManageViewService.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/Versions/A/XPCServices/com.apple.CloudSharingUI.AddParticipants.xpc/Contents/MacOS/com.apple.CloudSharingUI.AddParticipants](MACHOS/com.apple.CloudSharingUI.AddParticipants.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/Versions/A/XPCServices/CloudTelemetryService.xpc/Contents/MacOS/CloudTelemetryService](MACHOS/CloudTelemetryService.md)
- [/System/Library/PrivateFrameworks/CommerceKit.framework/Versions/A/Resources/storeuid.app/Contents/MacOS/storeuid](MACHOS/storeuid.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd](MACHOS/accessoryd.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/Versions/A/XPCServices/ACCHWComponentAuthService.xpc/Contents/MacOS/ACCHWComponentAuthService](MACHOS/ACCHWComponentAuthService.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/Versions/A/XPCServices/com.apple.siri.embeddedspeech.xpc/Contents/MacOS/com.apple.siri.embeddedspeech](MACHOS/com.apple.siri.embeddedspeech.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf](MACHOS/parsec-fbf.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd](MACHOS/corespeechd.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd_system](MACHOS/corespeechd_system.md)
- [/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced](MACHOS/CoreThreadCommissionerServiced.md)
- [/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod](MACHOS/threadradiod.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.sysdiagnose.appex/Contents/MacOS/com.apple.DiagnosticExtensions.sysdiagnose](MACHOS/com.apple.DiagnosticExtensions.sysdiagnose.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/osx-spotlight.appex/Contents/MacOS/osx-spotlight](MACHOS/osx-spotlight.md)
- [/System/Library/PrivateFrameworks/DiagnosticsSessionAvailability.framework/Versions/A/XPCServices/DiagnosticsSessionAvailabilityService.xpc/Contents/MacOS/DiagnosticsSessionAvailabilityService](MACHOS/DiagnosticsSessionAvailabilityService.md)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/catutil](MACHOS/catutil.md)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/XPCServices/DPSubmissionService.xpc/Contents/MacOS/DPSubmissionService](MACHOS/DPSubmissionService.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/Versions/A/XPCServices/diskimagescontroller.xpc/Contents/MacOS/diskimagescontroller](MACHOS/diskimagescontroller.md)
- [/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/Support/ecosystemanalyticsd](MACHOS/ecosystemanalyticsd.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/Versions/A/Resources/familycircled](MACHOS/familycircled.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/PlugIns/DraftingExtension-macOS.appex/Contents/MacOS/DraftingExtension-macOS](MACHOS/DraftingExtension-macOS.md)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/PlugIns/FileProviderDiagnosticExtension.appex/Contents/MacOS/FileProviderDiagnosticExtension](MACHOS/FileProviderDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceEraseXPCService.xpc/Contents/MacOS/FindMyDeviceEraseXPCService](MACHOS/FindMyDeviceEraseXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceIdentityXPCService.xpc/Contents/MacOS/FindMyDeviceIdentityXPCService](MACHOS/FindMyDeviceIdentityXPCService.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/Versions/A/Resources/TypographyPanel.bundle/Contents/MacOS/TypographyPanel](MACHOS/TypographyPanel.md)
- [/System/Library/PrivateFrameworks/GPUToolsCapture.framework/Versions/A/GPUToolsCapture](MACHOS/GPUToolsCapture.md)
- [/System/Library/PrivateFrameworks/GameCenterUICore.framework/XPCServices/com.apple.gamecenter.GameCenterUIService.xpc/Contents/MacOS/com.apple.gamecenter.GameCenterUIService](MACHOS/com.apple.gamecenter.GameCenterUIService.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/Versions/A/HomeKitDaemonLegacy](MACHOS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/Contents/MacOS/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/Versions/A/XPCServices/IDSBlastDoorService.xpc/Contents/MacOS/IDSBlastDoorService](MACHOS/IDSBlastDoorService.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/Contents/MacOS/imagent](MACHOS/imagent.md)
- [/System/Library/PrivateFrameworks/IPConfiguration.framework/Versions/A/XPCServices/IPConfigurationHelper.xpc/Contents/MacOS/IPConfigurationHelper](MACHOS/IPConfigurationHelper.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/Versions/A/IntelligenceFlowDiagnostics.appex/Contents/MacOS/IntelligenceFlowDiagnostics](MACHOS/IntelligenceFlowDiagnostics.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/Versions/A/intelligenceflowd](MACHOS/intelligenceflowd.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/PlugIns/DiagnosticExtension.appex/Contents/MacOS/DiagnosticExtension](MACHOS/DiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/MFAAuthentication.framework/Versions/A/XPCServices/MFAANetwork.xpc/Contents/MacOS/MFAANetwork](MACHOS/MFAANetwork.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted](MACHOS/mediaremoted.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/Versions/A/XPCServices/MessagesBlastDoorService.xpc/Contents/MacOS/MessagesBlastDoorService](MACHOS/MessagesBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd](MACHOS/accessoryupdaterd.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/Contents/MacOS/EAUpdaterService](MACHOS/EAUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/Contents/MacOS/UARPUpdaterServiceLegacyAudio](MACHOS/UARPUpdaterServiceLegacyAudio.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/Support/softwareupdated](MACHOS/softwareupdated.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/Versions/A/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/Contents/MacOS/com.apple.MobileSoftwareUpdate.CleanupPreparePathService](MACHOS/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/Versions/A/XPCServices/com.apple.MobileSoftwareUpdate.CryptegraftService.xpc/Contents/MacOS/com.apple.MobileSoftwareUpdate.CryptegraftService](MACHOS/com.apple.MobileSoftwareUpdate.CryptegraftService.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/PlugIns/NewDeviceOutreachMacExtension.appex/Contents/MacOS/NewDeviceOutreachMacExtension](MACHOS/NewDeviceOutreachMacExtension.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent](MACHOS/ndoagent.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorage.framework/Support/amsondevicestoraged](MACHOS/amsondevicestoraged.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/Contents/LinkedNotesUIService.app/Contents/MacOS/LinkedNotesUIService](MACHOS/LinkedNotesUIService.md)
- [/System/Library/PrivateFrameworks/People.framework/peopled](MACHOS/peopled.md)
- [/System/Library/PrivateFrameworks/PodcastServices.framework/XPCServices/PodcastContentService.xpc/Contents/MacOS/PodcastContentService](MACHOS/PodcastContentService.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Support/previewsd](MACHOS/previewsd.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/Contents/MacOS/privatecloudcomputed](MACHOS/privatecloudcomputed.md)
- [/System/Library/PrivateFrameworks/RemotePairingDevice.framework/Versions/A/RemotePairingDevice](MACHOS/RemotePairingDevice.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/Versions/A/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/ScreenTimeServiceUI.framework/Versions/A/XPCServices/ScreenTimeViewService.xpc/Contents/MacOS/ScreenTimeViewService](MACHOS/ScreenTimeViewService.md)
- [/System/Library/PrivateFrameworks/ShareKit.framework/Versions/A/PlugIns/ShareSheetUI.appex/Contents/MacOS/ShareSheetUI](MACHOS/ShareSheetUI.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd](MACHOS/sirittsd.md)
- [/System/Library/PrivateFrameworks/SiriVOX.framework/SiriHeadlessService](MACHOS/SiriHeadlessService.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/PlugIns/VideoIntentExtension.appex/Contents/MacOS/VideoIntentExtension](MACHOS/VideoIntentExtension.md)
- [/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond](MACHOS/spaceattributiond.md)
- [/System/Library/PrivateFrameworks/SystemStatusServer.framework/Support/systemstatusd](MACHOS/systemstatusd.md)
- [/System/Library/PrivateFrameworks/TCC.framework/Support/tccd](MACHOS/tccd.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FTLivePhotoService.xpc/Contents/MacOS/com.apple.FTLivePhotoService](MACHOS/com.apple.FTLivePhotoService.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/TimelineUI.framework/Versions/A/TimelineUI](MACHOS/TimelineUI.md)
- [/System/Library/PrivateFrameworks/UIKitMacHelper.framework/Versions/A/XPCServices/UIKitMacHelperSystemPreferencesViewService.xpc/Contents/MacOS/UIKitMacHelperSystemPreferencesViewService](MACHOS/UIKitMacHelperSystemPreferencesViewService.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/Contents/MacOS/BackgroundShortcutRunner](MACHOS/BackgroundShortcutRunner.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/ShortcutsViewService.xpc/Contents/MacOS/ShortcutsViewService](MACHOS/ShortcutsViewService.md)
- [/System/Library/PrivateFrameworks/WorkflowUIServices.framework/XPCServices/FocusConfigurationXPCServiceMac.xpc/Contents/MacOS/FocusConfigurationXPCServiceMac](MACHOS/FocusConfigurationXPCServiceMac.md)
- [/System/Library/PrivateFrameworks/WritingToolsUI.framework/Versions/A/XPCServices/WritingToolsViewService.xpc/Contents/MacOS/WritingToolsViewService](MACHOS/WritingToolsViewService.md)
- [/System/Library/PrivateFrameworks/iCloudNotification.framework/iCloudNotificationAgent](MACHOS/iCloudNotificationAgent.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd](MACHOS/itunescloudd.md)
- [/System/Library/ScreenReader/BrailleTables/Rhine.brailletable/Contents/MacOS/Rhine](MACHOS/Rhine.md)
- [/System/Library/SecurityResearch/usr/bin/pccvre](MACHOS/pccvre.md)
- [/System/Library/SecurityResearch/usr/bin/vrevm](MACHOS/vrevm.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/Contents/MacOS/AudioSuggestionsPlugin](MACHOS/AudioSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/HomeAutomationSiriSuggestions.bundle/Contents/MacOS/HomeAutomationSiriSuggestions](MACHOS/HomeAutomationSiriSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriLinkSuggestionsPlugin.bundle/Contents/MacOS/SiriLinkSuggestionsPlugin](MACHOS/SiriLinkSuggestionsPlugin.md)
- [/System/Library/Snippets/UIPlugins/AudioUIPlugin.bundle/Contents/MacOS/AudioUIPlugin](MACHOS/AudioUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/PhoneUIPlugin.bundle/Contents/MacOS/PhoneUIPlugin](MACHOS/PhoneUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/ResponseGenerationUIPlugin.bundle/Contents/MacOS/ResponseGenerationUIPlugin](MACHOS/ResponseGenerationUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SearchToolUIPlugin.bundle/Contents/MacOS/SearchToolUIPlugin](MACHOS/SearchToolUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriInformationUIPlugin.bundle/Contents/MacOS/SiriInformationUIPlugin](MACHOS/SiriInformationUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SystemPlugin.bundle/Contents/MacOS/SystemPlugin](MACHOS/SystemPlugin.md)
- [/System/Library/Spotlight/Application.mdimporter/Contents/MacOS/Application](MACHOS/Application.md)
- [/System/Library/SystemConfiguration/CaptiveNetworkSupport.bundle/Contents/MacOS/CaptiveNetworkSupport](MACHOS/CaptiveNetworkSupport.md)
- [/System/Library/SystemConfiguration/EAPOLController.bundle/Contents/MacOS/EAPOLController](MACHOS/EAPOLController.md)
- [/System/Library/SystemConfiguration/EAPOLController.bundle/Contents/Resources/eapolclient](MACHOS/eapolclient.md)
- [/System/Library/SystemConfiguration/IPConfiguration.bundle/Contents/MacOS/IPConfiguration](MACHOS/IPConfiguration.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtect](MACHOS/XProtect.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorAdload](MACHOS/XProtectRemediatorAdload.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorDolittle](MACHOS/XProtectRemediatorDolittle.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorGreenAcre](MACHOS/XProtectRemediatorGreenAcre.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorPirrit](MACHOS/XProtectRemediatorPirrit.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/XPCServices/XProtectPluginService.xpc/Contents/MacOS/XProtectPluginService](MACHOS/XProtectPluginService.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/DeviceInterface.framework/Support/deviceinterfaced](MACHOS/deviceinterfaced.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/DeviceInterface.framework/Versions/A/DeviceInterface](MACHOS/DeviceInterface.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/DeviceInterfaceClient.framework/Versions/A/DeviceInterfaceClient](MACHOS/DeviceInterfaceClient.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/MobileDevice.framework/Versions/A/AppleMobileDeviceHelper.app/Contents/Resources/AppleMobileBackup](MACHOS/AppleMobileBackup.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/MobileDevice.framework/Versions/A/MobileDevice](MACHOS/MobileDevice.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/RemotePairing.framework/Versions/A/RemotePairing](MACHOS/RemotePairing.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/RemotePairing.framework/Versions/A/XPCServices/remotepairingd.xpc/Contents/MacOS/remotepairingd](MACHOS/remotepairingd.md)
- [/System/Library/Templates/Data/Library/Frameworks/CoreRepairCore.framework/Versions/A/CoreRepairCore](MACHOS/CoreRepairCore.md)
- [/System/Library/UserEventPlugins/EAPOLMonitor.plugin/Contents/MacOS/EAPOLMonitor](MACHOS/EAPOLMonitor.md)
- [/System/Library/UserEventPlugins/PerfPowerServicesEventListenerPlugin.plugin/Contents/MacOS/PerfPowerServicesEventListenerPlugin](MACHOS/PerfPowerServicesEventListenerPlugin.md)
- [/System/Library/UserEventPlugins/com.apple.cts.plugin/Contents/MacOS/com.apple.cts](MACHOS/com.apple.cts.md)
- [/System/Library/UserEventPlugins/com.apple.nsurlsessiond.plugin/Contents/MacOS/com.apple.nsurlsessiond](MACHOS/com.apple.nsurlsessiond.md)
- [/System/Library/Video/Plug-Ins/AppleVideoDecoder.bundle/Contents/MacOS/AppleVideoDecoder](MACHOS/AppleVideoDecoder.md)
- [/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/Contents/MacOS/AppleVideoEncoder](MACHOS/AppleVideoEncoder.md)
- [/System/Library/Video/Plug-Ins/JPEGVideoDecoder.bundle/Contents/MacOS/JPEGVideoDecoder](MACHOS/JPEGVideoDecoder.md)
- [/System/Library/Video/Plug-Ins/JPEGVideoEncoder.bundle/Contents/MacOS/JPEGVideoEncoder](MACHOS/JPEGVideoEncoder.md)
- [/System/Library/Video/Plug-Ins/VCPHEVC.bundle/Contents/MacOS/VCPHEVC](MACHOS/VCPHEVC.md)
- [/System/Library/Video/Professional Video Workflow Plug-Ins/ExtensionShim.bundle/Contents/MacOS/ExtensionShim](MACHOS/ExtensionShim.md)
- [/System/Library/VideoProcessors/BarcodeScanner.videoprocessor](MACHOS/BarcodeScanner.videoprocessor.md)
- [/System/Library/iCloudSettings/Messages.bundle/Contents/MacOS/Messages](MACHOS/Messages.md)
- [/System/iOSSupport/System/Library/AppleMediaServices/DynamicUI/PlugIns/CoreDynamicUIPlugin.bundle/Contents/MacOS/CoreDynamicUIPlugin](MACHOS/CoreDynamicUIPlugin.md)
- [/System/iOSSupport/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/Contents/MacOS/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/iOSSupport/System/Library/Frameworks/ScreenTime.framework/Versions/A/PlugIns/ScreenTimeWebExtension.appex/Contents/MacOS/ScreenTimeWebExtension](MACHOS/ScreenTimeWebExtension.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/UtilityExtension.appex/Contents/MacOS/UtilityExtension](MACHOS/UtilityExtension.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/AvatarUI.framework/PlugIns/StickersUltraExtension.appex/Contents/MacOS/StickersUltraExtension](MACHOS/StickersUltraExtension.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterMessageExtension.appex/Contents/MacOS/GameCenterMessageExtension](MACHOS/GameCenterMessageExtension.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/UIKitCore.framework/Versions/A/Resources/TextEffectsCatalog.bundle/Contents/MacOS/TextEffectsCatalog](MACHOS/TextEffectsCatalog.md)
- [/bin/launchctl](MACHOS/launchctl.md)
- [/sbin/launchd](MACHOS/launchd.md)
- [/sbin/mount_afp](MACHOS/mount_afp.md)
- [/usr/bin/avmediainfo](MACHOS/avmediainfo.md)
- [/usr/bin/bsdtar](MACHOS/bsdtar.md)
- [/usr/bin/kmutil](MACHOS/kmutil.md)
- [/usr/bin/ktrace](MACHOS/ktrace.md)
- [/usr/bin/mddiagnose](MACHOS/mddiagnose.md)
- [/usr/bin/patch](MACHOS/patch.md)
- [/usr/bin/rsync](MACHOS/rsync.md)
- [/usr/bin/shazam](MACHOS/shazam.md)
- [/usr/bin/ssh](MACHOS/ssh.md)
- [/usr/bin/swift-inspect](MACHOS/swift-inspect.md)
- [/usr/lib/dyld](MACHOS/dyld.md)
- [/usr/lib/libmobileassetd.dylib](MACHOS/libmobileassetd.dylib.md)
- [/usr/lib/pam/pam_krb5.so.2](MACHOS/pam_krb5.so.2.md)
- [/usr/lib/pam/pam_mount.so.2](MACHOS/pam_mount.so.2.md)
- [/usr/lib/pam/pam_ntlm.so.2](MACHOS/pam_ntlm.so.2.md)
- [/usr/lib/pam/pam_opendirectory.so.2](MACHOS/pam_opendirectory.so.2.md)
- [/usr/lib/pam/pam_smartcard.so.2](MACHOS/pam_smartcard.so.2.md)
- [/usr/lib/system/libsystem_kernel.dylib](MACHOS/libsystem_kernel.dylib.md)
- [/usr/libexec/ASPCarryLog](MACHOS/ASPCarryLog.md)
- [/usr/libexec/ApplicationFirewall/socketfilterfw](MACHOS/socketfilterfw.md)
- [/usr/libexec/DumpPanic](MACHOS/DumpPanic.md)
- [/usr/libexec/NANDTaskScheduler](MACHOS/NANDTaskScheduler.md)
- [/usr/libexec/ReportMemoryException](MACHOS/ReportMemoryException.md)
- [/usr/libexec/TouchBarServer](MACHOS/TouchBarServer.md)
- [/usr/libexec/airportd](MACHOS/airportd.md)
- [/usr/libexec/apfsd](MACHOS/apfsd.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/assessmentagent](MACHOS/assessmentagent.md)
- [/usr/libexec/audioanalyticsd](MACHOS/audioanalyticsd.md)
- [/usr/libexec/biomesyncd](MACHOS/biomesyncd.md)
- [/usr/libexec/biometrickitd](MACHOS/biometrickitd.md)
- [/usr/libexec/bluetoothuserd](MACHOS/bluetoothuserd.md)
- [/usr/libexec/bootinstalld](MACHOS/bootinstalld.md)
- [/usr/libexec/bootpd](MACHOS/bootpd.md)
- [/usr/libexec/captiveagent](MACHOS/captiveagent.md)
- [/usr/libexec/companiond](MACHOS/companiond.md)
- [/usr/libexec/dasd](MACHOS/dasd.md)
- [/usr/libexec/dhcp6d](MACHOS/dhcp6d.md)
- [/usr/libexec/diskimagesiod](MACHOS/diskimagesiod.md)
- [/usr/libexec/eligibilityd](MACHOS/eligibilityd.md)
- [/usr/libexec/feedbackd](MACHOS/feedbackd.md)
- [/usr/libexec/findmydevice-user-agent](MACHOS/findmydevice-user-agent.md)
- [/usr/libexec/findmydeviced](MACHOS/findmydeviced.md)
- [/usr/libexec/findmylocateagent](MACHOS/findmylocateagent.md)
- [/usr/libexec/gamepolicyd](MACHOS/gamepolicyd.md)
- [/usr/libexec/kernelmanager_helper](MACHOS/kernelmanager_helper.md)
- [/usr/libexec/kernelmanagerd](MACHOS/kernelmanagerd.md)
- [/usr/libexec/locationd](MACHOS/locationd.md)
- [/usr/libexec/logd](MACHOS/logd.md)
- [/usr/libexec/logd_reporter](MACHOS/logd_reporter.md)
- [/usr/libexec/loginitemregisterd](MACHOS/loginitemregisterd.md)
- [/usr/libexec/mlhostd](MACHOS/mlhostd.md)
- [/usr/libexec/mobileactivationd](MACHOS/mobileactivationd.md)
- [/usr/libexec/mobileassetd](MACHOS/mobileassetd.md)
- [/usr/libexec/modelmanagerd](MACHOS/modelmanagerd.md)
- [/usr/libexec/nearbyd](MACHOS/nearbyd.md)
- [/usr/libexec/nesessionmanager](MACHOS/nesessionmanager.md)
- [/usr/libexec/networkserviceproxy](MACHOS/networkserviceproxy.md)
- [/usr/libexec/nfcd](MACHOS/nfcd.md)
- [/usr/libexec/nsurlsessiond](MACHOS/nsurlsessiond.md)
- [/usr/libexec/otherbsd](MACHOS/otherbsd.md)
- [/usr/libexec/proactiveeventtrackerd](MACHOS/proactiveeventtrackerd.md)
- [/usr/libexec/promotedcontentd](MACHOS/promotedcontentd.md)
- [/usr/libexec/rapportd](MACHOS/rapportd.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/replayd](MACHOS/replayd.md)
- [/usr/libexec/rtcreportingd](MACHOS/rtcreportingd.md)
- [/usr/libexec/sandboxd](MACHOS/sandboxd.md)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd.md)
- [/usr/libexec/searchpartyuseragent](MACHOS/searchpartyuseragent.md)
- [/usr/libexec/secd](MACHOS/secd.md)
- [/usr/libexec/security-sysdiagnose](MACHOS/security-sysdiagnose.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/sharingd](MACHOS/sharingd.md)
- [/usr/libexec/signpost_reporter](MACHOS/signpost_reporter.md)
- [/usr/libexec/slapconfig-keygen](MACHOS/slapconfig-keygen.md)
- [/usr/libexec/smd](MACHOS/smd.md)
- [/usr/libexec/sportsd](MACHOS/sportsd.md)
- [/usr/libexec/ssh-apple-pkcs11](MACHOS/ssh-apple-pkcs11.md)
- [/usr/libexec/ssh-pkcs11-helper](MACHOS/ssh-pkcs11-helper.md)
- [/usr/libexec/sshd-keygen-wrapper](MACHOS/sshd-keygen-wrapper.md)
- [/usr/libexec/swtransparencyd](MACHOS/swtransparencyd.md)
- [/usr/libexec/sysdiagnose_helper](MACHOS/sysdiagnose_helper.md)
- [/usr/libexec/sysdiagnosed](MACHOS/sysdiagnosed.md)
- [/usr/libexec/systemservicemonitord](MACHOS/systemservicemonitord.md)
- [/usr/libexec/testmanagerd](MACHOS/testmanagerd.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/tzd](MACHOS/tzd.md)
- [/usr/libexec/wifip2pd](MACHOS/wifip2pd.md)
- [/usr/libexec/wifivelocityd](MACHOS/wifivelocityd.md)
- [/usr/libexec/xpcproxy](MACHOS/xpcproxy.md)
- [/usr/libexec/xpcroleaccountd](MACHOS/xpcroleaccountd.md)
- [/usr/sbin/WirelessRadioManagerd](MACHOS/WirelessRadioManagerd.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/diskutil](MACHOS/diskutil.md)
- [/usr/sbin/mDNSResponder](MACHOS/mDNSResponder.md)
- [/usr/sbin/mtree](MACHOS/mtree.md)
- [/usr/sbin/screencapture](MACHOS/screencapture.md)
- [/usr/sbin/spindump](MACHOS/spindump.md)
- [/usr/sbin/sshd](MACHOS/sshd.md)
- [/usr/sbin/systemsoundserverd](MACHOS/systemsoundserverd.md)
- [/usr/sbin/usernoted](MACHOS/usernoted.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (81)

<details>
  <summary><i>View Updated</i></summary>

- [adc-eris-j129.im4p](FIRMWARE/adc-eris-j129.im4p.md)
- [adc-nyx-bc6x.im4p](FIRMWARE/adc-nyx-bc6x.im4p.md)
- [agx_a000](FIRMWARE/agx_a000.md)
- [agx_b000](FIRMWARE/agx_b000.md)
- [agx_b100](FIRMWARE/agx_b100.md)
- [agx_c000](FIRMWARE/agx_c000.md)
- [ansf.t6000.release.im4p](FIRMWARE/ansf.t6000.release.im4p.md)
- [ansf.t6020.release.im4p](FIRMWARE/ansf.t6020.release.im4p.md)
- [ansf.t6030.release.im4p](FIRMWARE/ansf.t6030.release.im4p.md)
- [ansf.t603x.release.im4p](FIRMWARE/ansf.t603x.release.im4p.md)
- [ansf.t603x_ASP3.release.im4p](FIRMWARE/ansf.t603x_ASP3.release.im4p.md)
- [ansf.t604x.release.im4p](FIRMWARE/ansf.t604x.release.im4p.md)
- [ansf.t8103.release.im4p](FIRMWARE/ansf.t8103.release.im4p.md)
- [ansf.t8112.release.im4p](FIRMWARE/ansf.t8112.release.im4p.md)
- [ansf.t8122.release.im4p](FIRMWARE/ansf.t8122.release.im4p.md)
- [ansf.t8132_ASP3.release.im4p](FIRMWARE/ansf.t8132_ASP3.release.im4p.md)
- [aopfw-j773gaop.RELEASE.im4p](FIRMWARE/aopfw-j773gaop.RELEASE.im4p.md)
- [aopfw-mac13gaop.RELEASE.im4p](FIRMWARE/aopfw-mac13gaop.RELEASE.im4p.md)
- [aopfw-mac13jaop.RELEASE.im4p](FIRMWARE/aopfw-mac13jaop.RELEASE.im4p.md)
- [aopfw-mac14gaop.RELEASE.im4p](FIRMWARE/aopfw-mac14gaop.RELEASE.im4p.md)
- [aopfw-mac14jaop.RELEASE.im4p](FIRMWARE/aopfw-mac14jaop.RELEASE.im4p.md)
- [aopfw-mac15gaop.RELEASE.im4p](FIRMWARE/aopfw-mac15gaop.RELEASE.im4p.md)
- [aopfw-mac15jaop.RELEASE.im4p](FIRMWARE/aopfw-mac15jaop.RELEASE.im4p.md)
- [aopfw-mac15saop.RELEASE.im4p](FIRMWARE/aopfw-mac15saop.RELEASE.im4p.md)
- [aopfw-mac16gaop.RELEASE.im4p](FIRMWARE/aopfw-mac16gaop.RELEASE.im4p.md)
- [aopfw-mac16gaop_l4.RELEASE.im4p](FIRMWARE/aopfw-mac16gaop_l4.RELEASE.im4p.md)
- [aopfw-mac16jaop.RELEASE.im4p](FIRMWARE/aopfw-mac16jaop.RELEASE.im4p.md)
- [ipad13dcp.im4p](FIRMWARE/ipad13dcp.im4p.md)
- [ipad13dcp_restore.im4p](FIRMWARE/ipad13dcp_restore.im4p.md)
- [ipad14dcp.im4p](FIRMWARE/ipad14dcp.im4p.md)
- [ipad14dcp_restore.im4p](FIRMWARE/ipad14dcp_restore.im4p.md)
- [rans.t6000.release.im4p](FIRMWARE/rans.t6000.release.im4p.md)
- [rans.t6020.release.im4p](FIRMWARE/rans.t6020.release.im4p.md)
- [rans.t6030.release.im4p](FIRMWARE/rans.t6030.release.im4p.md)
- [rans.t603x.release.im4p](FIRMWARE/rans.t603x.release.im4p.md)
- [rans.t603x_ASP3.release.im4p](FIRMWARE/rans.t603x_ASP3.release.im4p.md)
- [rans.t604x.release.im4p](FIRMWARE/rans.t604x.release.im4p.md)
- [rans.t8103.release.im4p](FIRMWARE/rans.t8103.release.im4p.md)
- [rans.t8112.release.im4p](FIRMWARE/rans.t8112.release.im4p.md)
- [rans.t8122.release.im4p](FIRMWARE/rans.t8122.release.im4p.md)
- [rans.t8132_ASP3.release.im4p](FIRMWARE/rans.t8132_ASP3.release.im4p.md)
- [sptm.t6041.release.im4p](FIRMWARE/sptm.t6041.release.im4p.md)
- [sptm.t8112.release.im4p](FIRMWARE/sptm.t8112.release.im4p.md)
- [sptm.t8132.release.im4p](FIRMWARE/sptm.t8132.release.im4p.md)
- [t6000ciofw.im4p](FIRMWARE/t6000ciofw.im4p.md)
- [t6001ciofw.im4p](FIRMWARE/t6001ciofw.im4p.md)
- [t6002ciofw.im4p](FIRMWARE/t6002ciofw.im4p.md)
- [t600xdcp.im4p](FIRMWARE/t600xdcp.im4p.md)
- [t600xdcp_restore.im4p](FIRMWARE/t600xdcp_restore.im4p.md)
- [t6020ciofw.im4p](FIRMWARE/t6020ciofw.im4p.md)
- [t6021ciofw.im4p](FIRMWARE/t6021ciofw.im4p.md)
- [t6022ciofw.im4p](FIRMWARE/t6022ciofw.im4p.md)
- [t602xdcp.im4p](FIRMWARE/t602xdcp.im4p.md)
- [t602xdcp_restore.im4p](FIRMWARE/t602xdcp_restore.im4p.md)
- [t602xscodec.im4p](FIRMWARE/t602xscodec.im4p.md)
- [t6030ciofw.im4p](FIRMWARE/t6030ciofw.im4p.md)
- [t6030dcp.im4p](FIRMWARE/t6030dcp.im4p.md)
- [t6030dcp_restore.im4p](FIRMWARE/t6030dcp_restore.im4p.md)
- [t6031ciofw.im4p](FIRMWARE/t6031ciofw.im4p.md)
- [t6032ciofw.im4p](FIRMWARE/t6032ciofw.im4p.md)
- [t6032cphyfw.im4p](FIRMWARE/t6032cphyfw.im4p.md)
- [t6034ciofw.im4p](FIRMWARE/t6034ciofw.im4p.md)
- [t603xdcp.im4p](FIRMWARE/t603xdcp.im4p.md)
- [t603xdcp_restore.im4p](FIRMWARE/t603xdcp_restore.im4p.md)
- [t6040ciofw.im4p](FIRMWARE/t6040ciofw.im4p.md)
- [t6040cphyfw.im4p](FIRMWARE/t6040cphyfw.im4p.md)
- [t6041ciofw.im4p](FIRMWARE/t6041ciofw.im4p.md)
- [t6041cphyfw.im4p](FIRMWARE/t6041cphyfw.im4p.md)
- [t6041pmp.im4p](FIRMWARE/t6041pmp.im4p.md)
- [t604xdcp.im4p](FIRMWARE/t604xdcp.im4p.md)
- [t604xdcp_restore.im4p](FIRMWARE/t604xdcp_restore.im4p.md)
- [t8103ciofw.im4p](FIRMWARE/t8103ciofw.im4p.md)
- [t8112ciofw.im4p](FIRMWARE/t8112ciofw.im4p.md)
- [t8112scodec.im4p](FIRMWARE/t8112scodec.im4p.md)
- [t8122ciofw.im4p](FIRMWARE/t8122ciofw.im4p.md)
- [t8122dcp.im4p](FIRMWARE/t8122dcp.im4p.md)
- [t8122dcp_restore.im4p](FIRMWARE/t8122dcp_restore.im4p.md)
- [t8132ciofw.im4p](FIRMWARE/t8132ciofw.im4p.md)
- [t8132dcp.im4p](FIRMWARE/t8132dcp.im4p.md)
- [t8132dcp_restore.im4p](FIRMWARE/t8132dcp_restore.im4p.md)
- [t8132pmp.im4p](FIRMWARE/t8132pmp.im4p.md)

</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 15.4 *(24E248)* | 621.1.15.11.10 |
| 15.5 *(24F5042g)* | 621.2.1.11.5 |

### Dylibs

#### 🆕 NEW (6)

- `/System/Library/PrivateFrameworks/CodableSwiftUICore.framework/Versions/A/CodableSwiftUICore`
- `/System/Library/PrivateFrameworks/NDOAPI.framework/Versions/A/NDOAPI`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/NDOUI`
- `/System/Library/PrivateFrameworks/SUDocAssetCore.framework/Versions/A/SUDocAssetCore`
- `/System/Library/PrivateFrameworks/SensorAccess.framework/Versions/A/SensorAccess`
- `/System/Library/PrivateFrameworks/SiriLocalization.framework/Versions/A/SiriLocalization`

#### ⬆️ Updated (850)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/Assistant/UIPlugins/SiriFindMyUIPlugin.siriUIBundle/Contents/Frameworks/SiriFindMyUI.framework/Versions/A/SiriFindMyUI](DYLIBS/SiriFindMyUI.md)
- [/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vImage.framework/Versions/A/vImage](DYLIBS/vImage.md)
- [/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libBLAS.dylib](DYLIBS/libBLAS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libBNNS.dylib](DYLIBS/libBNNS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libLAPACK.dylib](DYLIBS/libLAPACK.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libSparse.dylib](DYLIBS/libSparse.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libSparseBLAS.dylib](DYLIBS/libSparseBLAS.dylib.md)
- [/System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/AppKit.framework/Versions/C/AppKit](DYLIBS/AppKit.md)
- [/System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AuthenticationServices.framework/Versions/A/AuthenticationServices](DYLIBS/AuthenticationServices.md)
- [/System/Library/Frameworks/BrowserEngineKit.framework/Versions/A/BrowserEngineKit](DYLIBS/BrowserEngineKit.md)
- [/System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork](DYLIBS/CFNetwork.md)
- [/System/Library/Frameworks/Charts.framework/Versions/A/Charts](DYLIBS/Charts.md)
- [/System/Library/Frameworks/Combine.framework/Versions/A/Combine](DYLIBS/Combine.md)
- [/System/Library/Frameworks/ContactProvider.framework/Versions/A/ContactProvider](DYLIBS/ContactProvider.md)
- [/System/Library/Frameworks/Contacts.framework/Versions/A/Contacts](DYLIBS/Contacts.md)
- [/System/Library/Frameworks/ContactsUI.framework/Versions/A/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio](DYLIBS/CoreAudio.md)
- [/System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth](DYLIBS/CoreBluetooth.md)
- [/System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics](DYLIBS/CoreGraphics.md)
- [/System/Library/Frameworks/CoreImage.framework/Versions/A/CoreImage](DYLIBS/CoreImage.md)
- [/System/Library/Frameworks/CoreML.framework/Versions/A/CoreML](DYLIBS/CoreML.md)
- [/System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreMediaIO.framework/Versions/A/CoreMediaIO](DYLIBS/CoreMediaIO.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/Versions/A/CoreSpotlight](DYLIBS/CoreSpotlight.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib](DYLIBS/libCommCenterBase.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Versions/A/CoreTelephony](DYLIBS/CoreTelephony.md)
- [/System/Library/Frameworks/CoreTransferable.framework/Versions/A/CoreTransferable](DYLIBS/CoreTransferable.md)
- [/System/Library/Frameworks/CreateMLComponents.framework/Versions/A/CreateMLComponents](DYLIBS/CreateMLComponents.md)
- [/System/Library/Frameworks/CryptoKit.framework/Versions/A/CryptoKit](DYLIBS/CryptoKit.md)
- [/System/Library/Frameworks/DVDPlayback.framework/Versions/A/DVDPlayback](DYLIBS/DVDPlayback.md)
- [/System/Library/Frameworks/DeveloperToolsSupport.framework/Versions/A/DeveloperToolsSupport](DYLIBS/DeveloperToolsSupport.md)
- [/System/Library/Frameworks/EventKit.framework/Versions/A/EventKit](DYLIBS/EventKit.md)
- [/System/Library/Frameworks/ExtensionFoundation.framework/Versions/A/ExtensionFoundation](DYLIBS/ExtensionFoundation.md)
- [/System/Library/Frameworks/FSKit.framework/Versions/A/FSKit](DYLIBS/FSKit.md)
- [/System/Library/Frameworks/FileProvider.framework/Versions/A/FileProvider](DYLIBS/FileProvider.md)
- [/System/Library/Frameworks/FinanceKit.framework/Versions/A/FinanceKit](DYLIBS/FinanceKit.md)
- [/System/Library/Frameworks/FinanceKitUI.framework/Versions/A/FinanceKitUI](DYLIBS/FinanceKitUI.md)
- [/System/Library/Frameworks/Foundation.framework/Versions/C/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/HealthKit.framework/Versions/A/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit](DYLIBS/IOKit.md)
- [/System/Library/Frameworks/Intents.framework/Versions/A/Intents](DYLIBS/Intents.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/LightweightCodeRequirements.framework/Versions/A/LightweightCodeRequirements](DYLIBS/LightweightCodeRequirements.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/Versions/A/DaemonUtils](DYLIBS/DaemonUtils.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/ModuleBase.framework/Versions/A/ModuleBase](DYLIBS/ModuleBase.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/Versions/A/SharedUtils](DYLIBS/SharedUtils.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Versions/A/ManagedAppDistribution](DYLIBS/ManagedAppDistribution.md)
- [/System/Library/Frameworks/Matter.framework/Versions/A/Matter](DYLIBS/Matter.md)
- [/System/Library/Frameworks/MediaExtension.framework/Versions/A/MediaExtension](DYLIBS/MediaExtension.md)
- [/System/Library/Frameworks/MediaPlayer.framework/Versions/A/MediaPlayer](DYLIBS/MediaPlayer.md)
- [/System/Library/Frameworks/MediaToolbox.framework/Versions/A/MediaToolbox](DYLIBS/MediaToolbox.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Versions/A/Frameworks/MPSNDArray.framework/Versions/A/MPSNDArray](DYLIBS/MPSNDArray.md)
- [/System/Library/Frameworks/MusicKit.framework/Versions/A/MusicKit](DYLIBS/MusicKit.md)
- [/System/Library/Frameworks/Network.framework/Versions/A/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/NetworkExtension.framework/Versions/A/NetworkExtension](DYLIBS/NetworkExtension.md)
- [/System/Library/Frameworks/OSLog.framework/Versions/A/OSLog](DYLIBS/OSLog.md)
- [/System/Library/Frameworks/PhotosUI.framework/Versions/A/PhotosUI](DYLIBS/PhotosUI.md)
- [/System/Library/Frameworks/PushKit.framework/Versions/A/PushKit](DYLIBS/PushKit.md)
- [/System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/RealityFoundation.framework/Versions/A/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/Library/Frameworks/RealityKit.framework/Versions/A/RealityKit](DYLIBS/RealityKit.md)
- [/System/Library/Frameworks/SceneKit.framework/Versions/A/SceneKit](DYLIBS/SceneKit.md)
- [/System/Library/Frameworks/Security.framework/Versions/A/Security](DYLIBS/Security.md)
- [/System/Library/Frameworks/SecurityInterface.framework/Versions/A/SecurityInterface](DYLIBS/SecurityInterface.md)
- [/System/Library/Frameworks/SoundAnalysis.framework/Versions/A/SoundAnalysis](DYLIBS/SoundAnalysis.md)
- [/System/Library/Frameworks/Speech.framework/Versions/A/Speech](DYLIBS/Speech.md)
- [/System/Library/Frameworks/StickerKit.framework/Versions/A/StickerKit](DYLIBS/StickerKit.md)
- [/System/Library/Frameworks/StoreKit.framework/Versions/A/StoreKit](DYLIBS/StoreKit.md)
- [/System/Library/Frameworks/SwiftData.framework/Versions/A/SwiftData](DYLIBS/SwiftData.md)
- [/System/Library/Frameworks/SwiftUI.framework/Versions/A/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/Frameworks/SwiftUICore.framework/Versions/A/SwiftUICore](DYLIBS/SwiftUICore.md)
- [/System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration](DYLIBS/SystemConfiguration.md)
- [/System/Library/Frameworks/TabularData.framework/Versions/A/TabularData](DYLIBS/TabularData.md)
- [/System/Library/Frameworks/TipKit.framework/Versions/A/TipKit](DYLIBS/TipKit.md)
- [/System/Library/Frameworks/VideoToolbox.framework/Versions/A/VideoToolbox](DYLIBS/VideoToolbox.md)
- [/System/Library/Frameworks/Vision.framework/Versions/A/Vision](DYLIBS/Vision.md)
- [/System/Library/Frameworks/WeatherKit.framework/Versions/A/WeatherKit](DYLIBS/WeatherKit.md)
- [/System/Library/Frameworks/WebKit.framework/Versions/A/Frameworks/WebCore.framework/Versions/A/Frameworks/libANGLE-shared.dylib](DYLIBS/libANGLE-shared.dylib.md)
- [/System/Library/Frameworks/WebKit.framework/Versions/A/Frameworks/WebCore.framework/Versions/A/WebCore](DYLIBS/WebCore.md)
- [/System/Library/Frameworks/WebKit.framework/Versions/A/Frameworks/libWebKitSwift.dylib](DYLIBS/libWebKitSwift.dylib.md)
- [/System/Library/Frameworks/WebKit.framework/Versions/A/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Frameworks/WidgetKit.framework/Versions/A/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/Library/Frameworks/WorkoutKit.framework/Versions/A/WorkoutKit](DYLIBS/WorkoutKit.md)
- [/System/Library/Frameworks/_AppIntents_AppKit.framework/Versions/A/_AppIntents_AppKit](DYLIBS/_AppIntents_AppKit.md)
- [/System/Library/Frameworks/_AppIntents_SwiftUI.framework/Versions/A/_AppIntents_SwiftUI](DYLIBS/_AppIntents_SwiftUI.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/Versions/A/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/Frameworks/_StoreKit_SwiftUI.framework/Versions/A/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI.md)
- [/System/Library/Frameworks/iTunesLibrary.framework/Versions/A/iTunesLibrary](DYLIBS/iTunesLibrary.md)
- [/System/Library/MediaCapture/H16ISP.mediacapture](DYLIBS/H16ISP.mediacapture.md)
- [/System/Library/PrivateFrameworks/AIMLInstrumentationStreams.framework/Versions/A/AIMLInstrumentationStreams](DYLIBS/AIMLInstrumentationStreams.md)
- [/System/Library/PrivateFrameworks/AMPDesktopUI.framework/Versions/A/AMPDesktopUI](DYLIBS/AMPDesktopUI.md)
- [/System/Library/PrivateFrameworks/ANECompiler.framework/Versions/A/ANECompiler](DYLIBS/ANECompiler.md)
- [/System/Library/PrivateFrameworks/AOSUI.framework/Versions/A/AOSUI](DYLIBS/AOSUI.md)
- [/System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS](DYLIBS/APFS.md)
- [/System/Library/PrivateFrameworks/APTransport.framework/Versions/A/APTransport](DYLIBS/APTransport.md)
- [/System/Library/PrivateFrameworks/ASEProcessing.framework/Versions/A/ASEProcessing](DYLIBS/ASEProcessing.md)
- [/System/Library/PrivateFrameworks/ASRBridge.framework/Versions/A/ASRBridge](DYLIBS/ASRBridge.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/Versions/A/ViceroyTrace](DYLIBS/ViceroyTrace.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Versions/A/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVFCapture.framework/Versions/A/AVFCapture](DYLIBS/AVFCapture.md)
- [/System/Library/PrivateFrameworks/AVFCore.framework/Versions/A/AVFCore](DYLIBS/AVFCore.md)
- [/System/Library/PrivateFrameworks/AVFoundationCF.framework/Versions/A/AVFoundationCF](DYLIBS/AVFoundationCF.md)
- [/System/Library/PrivateFrameworks/AVKitCore.framework/Versions/A/AVKitCore](DYLIBS/AVKitCore.md)
- [/System/Library/PrivateFrameworks/AccessibilitySettingsUI.framework/Versions/A/AccessibilitySettingsUI](DYLIBS/AccessibilitySettingsUI.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/Versions/A/AccessibilitySharedSupport](DYLIBS/AccessibilitySharedSupport.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/Versions/A/AccessibilitySharedUISupport](DYLIBS/AccessibilitySharedUISupport.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/Versions/A/AccessibilityUtilities](DYLIBS/AccessibilityUtilities.md)
- [/System/Library/PrivateFrameworks/AccountsUISettings.framework/Versions/A/AccountsUISettings](DYLIBS/AccountsUISettings.md)
- [/System/Library/PrivateFrameworks/ActionKit.framework/Versions/A/ActionKit](DYLIBS/ActionKit.md)
- [/System/Library/PrivateFrameworks/AdPlatformsCommon.framework/Versions/A/AdPlatformsCommon](DYLIBS/AdPlatformsCommon.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiver.framework/Versions/A/AirPlayReceiver](DYLIBS/AirPlayReceiver.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiverKit.framework/Versions/A/AirPlayReceiverKit](DYLIBS/AirPlayReceiverKit.md)
- [/System/Library/PrivateFrameworks/AirPlaySender.framework/Versions/A/AirPlaySender](DYLIBS/AirPlaySender.md)
- [/System/Library/PrivateFrameworks/AirPlaySupport.framework/Versions/A/AirPlaySupport](DYLIBS/AirPlaySupport.md)
- [/System/Library/PrivateFrameworks/Anvil.framework/Versions/A/Anvil](DYLIBS/Anvil.md)
- [/System/Library/PrivateFrameworks/AppAnalytics.framework/Versions/A/AppAnalytics](DYLIBS/AppAnalytics.md)
- [/System/Library/PrivateFrameworks/AppAttestInternal.framework/Versions/A/AppAttestInternal](DYLIBS/AppAttestInternal.md)
- [/System/Library/PrivateFrameworks/AppIntentSchemas.framework/Versions/A/AppIntentSchemas](DYLIBS/AppIntentSchemas.md)
- [/System/Library/PrivateFrameworks/AppIntentsServices.framework/Versions/A/AppIntentsServices](DYLIBS/AppIntentsServices.md)
- [/System/Library/PrivateFrameworks/AppPlaceholderSync.framework/Versions/A/AppPlaceholderSync](DYLIBS/AppPlaceholderSync.md)
- [/System/Library/PrivateFrameworks/AppState.framework/Versions/A/AppState](DYLIBS/AppState.md)
- [/System/Library/PrivateFrameworks/AppStoreKit.framework/Versions/A/AppStoreKit](DYLIBS/AppStoreKit.md)
- [/System/Library/PrivateFrameworks/AppleAccount.framework/Versions/A/AppleAccount](DYLIBS/AppleAccount.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/Versions/A/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/Versions/A/AppleDeviceQuerySupport](DYLIBS/AppleDeviceQuerySupport.md)
- [/System/Library/PrivateFrameworks/AppleIDSetup.framework/Versions/A/AppleIDSetup](DYLIBS/AppleIDSetup.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupDaemon.framework/Versions/A/AppleIDSetupDaemon](DYLIBS/AppleIDSetupDaemon.md)
- [/System/Library/PrivateFrameworks/AppleJPEG.framework/Versions/A/AppleJPEG](DYLIBS/AppleJPEG.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/Versions/A/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesKitInternal.framework/Versions/A/AppleMediaServicesKitInternal](DYLIBS/AppleMediaServicesKitInternal.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Versions/A/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AppleServiceToolkit.framework/Versions/A/AppleServiceToolkit](DYLIBS/AppleServiceToolkit.md)
- [/System/Library/PrivateFrameworks/ArgumentParserInternal.framework/Versions/A/ArgumentParserInternal](DYLIBS/ArgumentParserInternal.md)
- [/System/Library/PrivateFrameworks/AskPermission.framework/Versions/A/AskPermission](DYLIBS/AskPermission.md)
- [/System/Library/PrivateFrameworks/AskToDaemon.framework/Versions/A/AskToDaemon](DYLIBS/AskToDaemon.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/PrivateFrameworks/AttributeGraph.framework/Versions/A/AttributeGraph](DYLIBS/AttributeGraph.md)
- [/System/Library/PrivateFrameworks/AudioAnalytics.framework/Versions/A/AudioAnalytics](DYLIBS/AudioAnalytics.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/Versions/A/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsExternal.framework/Versions/A/AudioAnalyticsExternal](DYLIBS/AudioAnalyticsExternal.md)
- [/System/Library/PrivateFrameworks/AudioDSPManager.framework/Versions/A/AudioDSPManager](DYLIBS/AudioDSPManager.md)
- [/System/Library/PrivateFrameworks/AudioServerDriver.framework/Versions/A/AudioServerDriver](DYLIBS/AudioServerDriver.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_Base.framework/Versions/A/AudioServerDriverTransports_Base](DYLIBS/AudioServerDriverTransports_Base.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOA2.framework/Versions/A/AudioServerDriverTransports_IOA2](DYLIBS/AudioServerDriverTransports_IOA2.md)
- [/System/Library/PrivateFrameworks/AudioSession.framework/Versions/A/AudioSession](DYLIBS/AudioSession.md)
- [/System/Library/PrivateFrameworks/AudioToolboxCore.framework/Versions/A/AudioToolboxCore](DYLIBS/AudioToolboxCore.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/AvatarKit.framework/Versions/A/AvatarKit](DYLIBS/AvatarKit.md)
- [/System/Library/PrivateFrameworks/Backup.framework/Versions/A/Backup](DYLIBS/Backup.md)
- [/System/Library/PrivateFrameworks/BatteryCenterUI.framework/Versions/A/BatteryCenterUI](DYLIBS/BatteryCenterUI.md)
- [/System/Library/PrivateFrameworks/BiomeFlexibleStorage.framework/Versions/A/BiomeFlexibleStorage](DYLIBS/BiomeFlexibleStorage.md)
- [/System/Library/PrivateFrameworks/BiomeFoundation.framework/Versions/A/BiomeFoundation](DYLIBS/BiomeFoundation.md)
- [/System/Library/PrivateFrameworks/BiomeLibrary.framework/Versions/A/BiomeLibrary](DYLIBS/BiomeLibrary.md)
- [/System/Library/PrivateFrameworks/BiomeStorage.framework/Versions/A/BiomeStorage](DYLIBS/BiomeStorage.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams](DYLIBS/BiomeStreams.md)
- [/System/Library/PrivateFrameworks/BlastDoor.framework/Versions/A/BlastDoor](DYLIBS/BlastDoor.md)
- [/System/Library/PrivateFrameworks/Bom.framework/Versions/A/Bom](DYLIBS/Bom.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/Versions/A/BookDataStore](DYLIBS/BookDataStore.md)
- [/System/Library/PrivateFrameworks/BookFoundation.framework/Versions/A/BookFoundation](DYLIBS/BookFoundation.md)
- [/System/Library/PrivateFrameworks/Bootability.framework/Versions/A/Frameworks/BootabilityBrain.framework/Versions/A/BootabilityBrain](DYLIBS/BootabilityBrain.md)
- [/System/Library/PrivateFrameworks/BusinessServices.framework/Versions/A/BusinessServices](DYLIBS/BusinessServices.md)
- [/System/Library/PrivateFrameworks/CDMFoundation.framework/Versions/A/CDMFoundation](DYLIBS/CDMFoundation.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/Versions/A/CMCapture](DYLIBS/CMCapture.md)
- [/System/Library/PrivateFrameworks/CMCaptureCore.framework/Versions/A/CMCaptureCore](DYLIBS/CMCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/Versions/A/CMContinuityCaptureCore](DYLIBS/CMContinuityCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMImaging.framework/Versions/A/CMImaging](DYLIBS/CMImaging.md)
- [/System/Library/PrivateFrameworks/CTBlastDoorSupport.framework/Versions/A/CTBlastDoorSupport](DYLIBS/CTBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/CTLazuliSupport.framework/Versions/A/CTLazuliSupport](DYLIBS/CTLazuliSupport.md)
- [/System/Library/PrivateFrameworks/Calculate.framework/Versions/A/Calculate](DYLIBS/Calculate.md)
- [/System/Library/PrivateFrameworks/CalculateUI.framework/Versions/A/CalculateUI](DYLIBS/CalculateUI.md)
- [/System/Library/PrivateFrameworks/CalendarDaemon.framework/Versions/A/CalendarDaemon](DYLIBS/CalendarDaemon.md)
- [/System/Library/PrivateFrameworks/CalendarDatabase.framework/Versions/A/CalendarDatabase](DYLIBS/CalendarDatabase.md)
- [/System/Library/PrivateFrameworks/CalendarLink.framework/Versions/A/CalendarLink](DYLIBS/CalendarLink.md)
- [/System/Library/PrivateFrameworks/CalendarUIKit.framework/Versions/A/CalendarUIKit](DYLIBS/CalendarUIKit.md)
- [/System/Library/PrivateFrameworks/CalendarWidget.framework/Versions/A/CalendarWidget](DYLIBS/CalendarWidget.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/Versions/A/CallHistory](DYLIBS/CallHistory.md)
- [/System/Library/PrivateFrameworks/CameraColorProcessing.framework/Versions/A/CameraColorProcessing](DYLIBS/CameraColorProcessing.md)
- [/System/Library/PrivateFrameworks/CascadeEngine.framework/Versions/A/CascadeEngine](DYLIBS/CascadeEngine.md)
- [/System/Library/PrivateFrameworks/CascadeSets.framework/Versions/A/CascadeSets](DYLIBS/CascadeSets.md)
- [/System/Library/PrivateFrameworks/Chirp.framework/Versions/A/Chirp](DYLIBS/Chirp.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/Versions/A/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/PrivateFrameworks/ChronoKit.framework/Versions/A/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/Library/PrivateFrameworks/ChronoServices.framework/Versions/A/ChronoServices](DYLIBS/ChronoServices.md)
- [/System/Library/PrivateFrameworks/ChronoUIServices.framework/Versions/A/ChronoUIServices](DYLIBS/ChronoUIServices.md)
- [/System/Library/PrivateFrameworks/CinematicFraming.framework/Versions/A/CinematicFraming](DYLIBS/CinematicFraming.md)
- [/System/Library/PrivateFrameworks/CipherML.framework/Versions/A/CipherML](DYLIBS/CipherML.md)
- [/System/Library/PrivateFrameworks/ClassKitUI.framework/Versions/A/ClassKitUI](DYLIBS/ClassKitUI.md)
- [/System/Library/PrivateFrameworks/CloudAssetDaemon.framework/Versions/A/CloudAssetDaemon](DYLIBS/CloudAssetDaemon.md)
- [/System/Library/PrivateFrameworks/CloudAssets.framework/Versions/A/CloudAssets](DYLIBS/CloudAssets.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/Versions/A/CloudSharingUI](DYLIBS/CloudSharingUI.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/Versions/A/CloudSubscriptionFeatures](DYLIBS/CloudSubscriptionFeatures.md)
- [/System/Library/PrivateFrameworks/CloudTelemetryTools.framework/Versions/A/CloudTelemetryTools](DYLIBS/CloudTelemetryTools.md)
- [/System/Library/PrivateFrameworks/Coherence.framework/Versions/A/Coherence](DYLIBS/Coherence.md)
- [/System/Library/PrivateFrameworks/CollectionsInternal.framework/Versions/A/CollectionsInternal](DYLIBS/CollectionsInternal.md)
- [/System/Library/PrivateFrameworks/ContactsAutocomplete.framework/Versions/A/ContactsAutocomplete](DYLIBS/ContactsAutocomplete.md)
- [/System/Library/PrivateFrameworks/ContactsUICore.framework/Versions/A/ContactsUICore](DYLIBS/ContactsUICore.md)
- [/System/Library/PrivateFrameworks/ContentKit.framework/Versions/A/ContentKit](DYLIBS/ContentKit.md)
- [/System/Library/PrivateFrameworks/ContextualUnderstanding.framework/Versions/A/ContextualUnderstanding](DYLIBS/ContextualUnderstanding.md)
- [/System/Library/PrivateFrameworks/ConversationKit.framework/Versions/A/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/PrivateFrameworks/CoordinationCore.framework/Versions/A/CoordinationCore](DYLIBS/CoordinationCore.md)
- [/System/Library/PrivateFrameworks/CoreAccessibility.framework/Versions/A/CoreAccessibility](DYLIBS/CoreAccessibility.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/Versions/A/CoreAccessories](DYLIBS/CoreAccessories.md)
- [/System/Library/PrivateFrameworks/CoreAppleCVA.framework/Versions/A/CoreAppleCVA](DYLIBS/CoreAppleCVA.md)
- [/System/Library/PrivateFrameworks/CoreAudioOrchestration.framework/Versions/A/CoreAudioOrchestration](DYLIBS/CoreAudioOrchestration.md)
- [/System/Library/PrivateFrameworks/CoreBrightness.framework/Versions/A/CoreBrightness](DYLIBS/CoreBrightness.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/Versions/A/CoreCDPUI](DYLIBS/CoreCDPUI.md)
- [/System/Library/PrivateFrameworks/CoreDiagnostics.framework/Versions/A/CoreDiagnostics](DYLIBS/CoreDiagnostics.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/Versions/A/CoreEmbeddedSpeechRecognition](DYLIBS/CoreEmbeddedSpeechRecognition.md)
- [/System/Library/PrivateFrameworks/CoreFollowUp.framework/Versions/A/CoreFollowUp](DYLIBS/CoreFollowUp.md)
- [/System/Library/PrivateFrameworks/CoreHAP.framework/Versions/A/CoreHAP](DYLIBS/CoreHAP.md)
- [/System/Library/PrivateFrameworks/CoreHapticsTools.framework/Versions/A/CoreHapticsTools](DYLIBS/CoreHapticsTools.md)
- [/System/Library/PrivateFrameworks/CoreKnowledge.framework/Versions/A/CoreKnowledge](DYLIBS/CoreKnowledge.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/Versions/A/CoreParsec](DYLIBS/CoreParsec.md)
- [/System/Library/PrivateFrameworks/CorePhotogrammetry.framework/Versions/A/CorePhotogrammetry](DYLIBS/CorePhotogrammetry.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/Versions/A/CoreSpeech](DYLIBS/CoreSpeech.md)
- [/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/Versions/A/CoreSpeechExclave](DYLIBS/CoreSpeechExclave.md)
- [/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/Versions/A/CoreSpeechFoundation](DYLIBS/CoreSpeechFoundation.md)
- [/System/Library/PrivateFrameworks/CoreSpeechUtils.framework/Versions/A/CoreSpeechUtils](DYLIBS/CoreSpeechUtils.md)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/Versions/A/CoreSuggestions](DYLIBS/CoreSuggestions.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsInternals.framework/Versions/A/CoreSuggestionsInternals](DYLIBS/CoreSuggestionsInternals.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsUI.framework/Versions/A/CoreSuggestionsUI](DYLIBS/CoreSuggestionsUI.md)
- [/System/Library/PrivateFrameworks/CoreThreadRadio.framework/Versions/A/CoreThreadRadio](DYLIBS/CoreThreadRadio.md)
- [/System/Library/PrivateFrameworks/CoreUARP.framework/Versions/A/CoreUARP](DYLIBS/CoreUARP.md)
- [/System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils](DYLIBS/CoreUtils.md)
- [/System/Library/PrivateFrameworks/CoreUtilsExtras.framework/Versions/A/CoreUtilsExtras](DYLIBS/CoreUtilsExtras.md)
- [/System/Library/PrivateFrameworks/CoreUtilsSwift.framework/Versions/A/CoreUtilsSwift](DYLIBS/CoreUtilsSwift.md)
- [/System/Library/PrivateFrameworks/CoreWiFi.framework/Versions/A/CoreWiFi](DYLIBS/CoreWiFi.md)
- [/System/Library/PrivateFrameworks/Cosmo.framework/Versions/A/Cosmo](DYLIBS/Cosmo.md)
- [/System/Library/PrivateFrameworks/CryptexServer.framework/Versions/A/CryptexServer](DYLIBS/CryptexServer.md)
- [/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/Versions/A/CryptoKitPrivate](DYLIBS/CryptoKitPrivate.md)
- [/System/Library/PrivateFrameworks/DailyBriefingCommon.framework/Versions/A/DailyBriefingCommon](DYLIBS/DailyBriefingCommon.md)
- [/System/Library/PrivateFrameworks/DarwinDirectory.framework/Versions/A/DarwinDirectory](DYLIBS/DarwinDirectory.md)
- [/System/Library/PrivateFrameworks/DeepThoughtBiomeFoundation.framework/Versions/A/DeepThoughtBiomeFoundation](DYLIBS/DeepThoughtBiomeFoundation.md)
- [/System/Library/PrivateFrameworks/Dendrite.framework/Versions/A/Dendrite](DYLIBS/Dendrite.md)
- [/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Versions/A/DeviceExpertIntents](DYLIBS/DeviceExpertIntents.md)
- [/System/Library/PrivateFrameworks/DeviceExpertUI.framework/Versions/A/DeviceExpertUI](DYLIBS/DeviceExpertUI.md)
- [/System/Library/PrivateFrameworks/DeviceIdentity.framework/Versions/A/DeviceIdentity](DYLIBS/DeviceIdentity.md)
- [/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/Versions/A/DiagnosticRequestService](DYLIBS/DiagnosticRequestService.md)
- [/System/Library/PrivateFrameworks/DiagnosticsSessionAvailability.framework/Versions/A/DiagnosticsSessionAvailability](DYLIBS/DiagnosticsSessionAvailability.md)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/Versions/A/DialogEngine](DYLIBS/DialogEngine.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/Versions/A/DiskImages2](DYLIBS/DiskImages2.md)
- [/System/Library/PrivateFrameworks/DistributedTimers.framework/Versions/A/DistributedTimers](DYLIBS/DistributedTimers.md)
- [/System/Library/PrivateFrameworks/DistributedTimersDaemon.framework/Versions/A/DistributedTimersDaemon](DYLIBS/DistributedTimersDaemon.md)
- [/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/Versions/A/DoNotDisturbServer](DYLIBS/DoNotDisturbServer.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/Versions/A/DocumentUnderstanding](DYLIBS/DocumentUnderstanding.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstandingClient.framework/Versions/A/DocumentUnderstandingClient](DYLIBS/DocumentUnderstandingClient.md)
- [/System/Library/PrivateFrameworks/Dyld.framework/Versions/A/Dyld](DYLIBS/Dyld.md)
- [/System/Library/PrivateFrameworks/EAP8021X.framework/Versions/A/EAP8021X](DYLIBS/EAP8021X.md)
- [/System/Library/PrivateFrameworks/EXDisplayPipe.framework/Versions/A/EXDisplayPipe](DYLIBS/EXDisplayPipe.md)
- [/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/Versions/A/EcosystemAnalytics](DYLIBS/EcosystemAnalytics.md)
- [/System/Library/PrivateFrameworks/Email.framework/Versions/A/Email](DYLIBS/Email.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/Versions/A/EmailDaemon](DYLIBS/EmailDaemon.md)
- [/System/Library/PrivateFrameworks/EmailFoundation.framework/Versions/A/EmailFoundation](DYLIBS/EmailFoundation.md)
- [/System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/Versions/A/EmbeddedAcousticRecognition](DYLIBS/EmbeddedAcousticRecognition.md)
- [/System/Library/PrivateFrameworks/EmojiFoundation.framework/Versions/A/EmojiFoundation](DYLIBS/EmojiFoundation.md)
- [/System/Library/PrivateFrameworks/Espresso.framework/Versions/A/Espresso](DYLIBS/Espresso.md)
- [/System/Library/PrivateFrameworks/ExtensionKitSettings.framework/Versions/A/ExtensionKitSettings](DYLIBS/ExtensionKitSettings.md)
- [/System/Library/PrivateFrameworks/FMFCore.framework/Versions/A/FMFCore](DYLIBS/FMFCore.md)
- [/System/Library/PrivateFrameworks/FMIPCore.framework/Versions/A/FMIPCore](DYLIBS/FMIPCore.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/Versions/A/FaceTimeMessageStore](DYLIBS/FaceTimeMessageStore.md)
- [/System/Library/PrivateFrameworks/FaceTimeNotificationCore.framework/Versions/A/FaceTimeNotificationCore](DYLIBS/FaceTimeNotificationCore.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/Versions/A/FamilyCircle](DYLIBS/FamilyCircle.md)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/Versions/A/FamilyCircleUI](DYLIBS/FamilyCircleUI.md)
- [/System/Library/PrivateFrameworks/FeatureStore.framework/Versions/A/FeatureStore](DYLIBS/FeatureStore.md)
- [/System/Library/PrivateFrameworks/FedStats.framework/Versions/A/FedStats](DYLIBS/FedStats.md)
- [/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/Versions/A/FedStatsPluginCore](DYLIBS/FedStatsPluginCore.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/Versions/A/Feedback](DYLIBS/Feedback.md)
- [/System/Library/PrivateFrameworks/FeedbackCore.framework/Versions/A/FeedbackCore](DYLIBS/FeedbackCore.md)
- [/System/Library/PrivateFrameworks/FeedbackService.framework/Versions/A/FeedbackService](DYLIBS/FeedbackService.md)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/Versions/A/FileProviderDaemon](DYLIBS/FileProviderDaemon.md)
- [/System/Library/PrivateFrameworks/FinanceDaemon.framework/Versions/A/FinanceDaemon](DYLIBS/FinanceDaemon.md)
- [/System/Library/PrivateFrameworks/FindMyBase.framework/Versions/A/FindMyBase](DYLIBS/FindMyBase.md)
- [/System/Library/PrivateFrameworks/FindMyBluetooth.framework/Versions/A/FindMyBluetooth](DYLIBS/FindMyBluetooth.md)
- [/System/Library/PrivateFrameworks/FindMyCore.framework/Versions/A/FindMyCore](DYLIBS/FindMyCore.md)
- [/System/Library/PrivateFrameworks/FindMyDaemonSupport.framework/Versions/A/FindMyDaemonSupport](DYLIBS/FindMyDaemonSupport.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/Versions/A/FindMyDevice](DYLIBS/FindMyDevice.md)
- [/System/Library/PrivateFrameworks/FindMyLocate.framework/Versions/A/FindMyLocate](DYLIBS/FindMyLocate.md)
- [/System/Library/PrivateFrameworks/FindMyServerInteraction.framework/Versions/A/FindMyServerInteraction](DYLIBS/FindMyServerInteraction.md)
- [/System/Library/PrivateFrameworks/FocusSettingsUI.framework/Versions/A/FocusSettingsUI](DYLIBS/FocusSettingsUI.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib](DYLIBS/libFontParser.dylib.md)
- [/System/Library/PrivateFrameworks/FoundInAppsPlugins.framework/Versions/A/FoundInAppsPlugins](DYLIBS/FoundInAppsPlugins.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libLLVM.dylib](DYLIBS/libLLVM.dylib.md)
- [/System/Library/PrivateFrameworks/GRDBInternal.framework/Versions/A/GRDBInternal](DYLIBS/GRDBInternal.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/Versions/A/GameCenterUI](DYLIBS/GameCenterUI.md)
- [/System/Library/PrivateFrameworks/GameServicesCore.framework/Versions/A/GameServicesCore](DYLIBS/GameServicesCore.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/GenerativeAssistantActions](DYLIBS/GenerativeAssistantActions.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantCommon.framework/Versions/A/GenerativeAssistantCommon](DYLIBS/GenerativeAssistantCommon.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantSettings.framework/Versions/A/GenerativeAssistantSettings](DYLIBS/GenerativeAssistantSettings.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantUI.framework/Versions/A/GenerativeAssistantUI](DYLIBS/GenerativeAssistantUI.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiences.framework/Versions/A/GenerativeExperiences](DYLIBS/GenerativeExperiences.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/Versions/A/GenerativeExperiencesRuntime](DYLIBS/GenerativeExperiencesRuntime.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesUI.framework/Versions/A/GenerativeExperiencesUI](DYLIBS/GenerativeExperiencesUI.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/Versions/A/GenerativeFunctionsFoundation](DYLIBS/GenerativeFunctionsFoundation.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/Versions/A/GenerativeFunctionsInstrumentation](DYLIBS/GenerativeFunctionsInstrumentation.md)
- [/System/Library/PrivateFrameworks/GenerativeModels.framework/Versions/A/GenerativeModels](DYLIBS/GenerativeModels.md)
- [/System/Library/PrivateFrameworks/GenerativeModelsFoundation.framework/Versions/A/GenerativeModelsFoundation](DYLIBS/GenerativeModelsFoundation.md)
- [/System/Library/PrivateFrameworks/Geometry.framework/Versions/A/Geometry](DYLIBS/Geometry.md)
- [/System/Library/PrivateFrameworks/GroupKitCrypto.framework/Versions/A/GroupKitCrypto](DYLIBS/GroupKitCrypto.md)
- [/System/Library/PrivateFrameworks/HDRProcessing.framework/Versions/A/HDRProcessing](DYLIBS/HDRProcessing.md)
- [/System/Library/PrivateFrameworks/HIDRMKit.framework/Versions/A/HIDRMKit](DYLIBS/HIDRMKit.md)
- [/System/Library/PrivateFrameworks/HMFoundation.framework/Versions/A/HMFoundation](DYLIBS/HMFoundation.md)
- [/System/Library/PrivateFrameworks/HeadGestures.framework/Versions/A/HeadGestures](DYLIBS/HeadGestures.md)
- [/System/Library/PrivateFrameworks/HealthDomainsTools.framework/Versions/A/HealthDomainsTools](DYLIBS/HealthDomainsTools.md)
- [/System/Library/PrivateFrameworks/HelpData.framework/Versions/A/HelpData](DYLIBS/HelpData.md)
- [/System/Library/PrivateFrameworks/HomeAI.framework/Versions/A/HomeAI](DYLIBS/HomeAI.md)
- [/System/Library/PrivateFrameworks/HomeAppIntents.framework/Versions/A/HomeAppIntents](DYLIBS/HomeAppIntents.md)
- [/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Versions/A/HomeAutomationInternal](DYLIBS/HomeAutomationInternal.md)
- [/System/Library/PrivateFrameworks/HomeAutomationUIFramework.framework/Versions/A/HomeAutomationUIFramework](DYLIBS/HomeAutomationUIFramework.md)
- [/System/Library/PrivateFrameworks/HomeDataModel.framework/Versions/A/HomeDataModel](DYLIBS/HomeDataModel.md)
- [/System/Library/PrivateFrameworks/HomeKit.framework/Versions/A/HomeKit](DYLIBS/HomeKit.md)
- [/System/Library/PrivateFrameworks/HomeKitCore.framework/Versions/A/HomeKitCore](DYLIBS/HomeKitCore.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Versions/A/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonFoundation.framework/Versions/A/HomeKitDaemonFoundation](DYLIBS/HomeKitDaemonFoundation.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/Versions/A/HomeKitEvents](DYLIBS/HomeKitEvents.md)
- [/System/Library/PrivateFrameworks/HomeKitMatter.framework/Versions/A/HomeKitMatter](DYLIBS/HomeKitMatter.md)
- [/System/Library/PrivateFrameworks/HomeKitMetrics.framework/Versions/A/HomeKitMetrics](DYLIBS/HomeKitMetrics.md)
- [/System/Library/PrivateFrameworks/Human.framework/Versions/A/Human](DYLIBS/Human.md)
- [/System/Library/PrivateFrameworks/HumanUI.framework/Versions/A/HumanUI](DYLIBS/HumanUI.md)
- [/System/Library/PrivateFrameworks/HumanUnderstandingEvidence.framework/Versions/A/HumanUnderstandingEvidence](DYLIBS/HumanUnderstandingEvidence.md)
- [/System/Library/PrivateFrameworks/IASUtilities.framework/Versions/A/IASUtilities](DYLIBS/IASUtilities.md)
- [/System/Library/PrivateFrameworks/IASUtilitiesCore.framework/Versions/A/IASUtilitiesCore](DYLIBS/IASUtilitiesCore.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/Versions/A/IDSFoundation](DYLIBS/IDSFoundation.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/Versions/A/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/Versions/A/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/Versions/A/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/Versions/A/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib](DYLIBS/libIPTelephony.dylib.md)
- [/System/Library/PrivateFrameworks/ISPExclaveKitServices.framework/Versions/A/ISPExclaveKitServices](DYLIBS/ISPExclaveKitServices.md)
- [/System/Library/PrivateFrameworks/ImagePlaygroundInternal.framework/Versions/A/ImagePlaygroundInternal](DYLIBS/ImagePlaygroundInternal.md)
- [/System/Library/PrivateFrameworks/InertiaCam.framework/Versions/A/InertiaCam](DYLIBS/InertiaCam.md)
- [/System/Library/PrivateFrameworks/InputAnalytics.framework/Versions/A/InputAnalytics](DYLIBS/InputAnalytics.md)
- [/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/Versions/A/InputAnalyticsServer](DYLIBS/InputAnalyticsServer.md)
- [/System/Library/PrivateFrameworks/IntelligenceEngine.framework/Versions/A/IntelligenceEngine](DYLIBS/IntelligenceEngine.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlow.framework/Versions/A/IntelligenceFlow](DYLIBS/IntelligenceFlow.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContext.framework/Versions/A/IntelligenceFlowContext](DYLIBS/IntelligenceFlowContext.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/Versions/A/IntelligenceFlowContextRuntime](DYLIBS/IntelligenceFlowContextRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowFeedbackDataCollector.framework/Versions/A/IntelligenceFlowFeedbackDataCollector](DYLIBS/IntelligenceFlowFeedbackDataCollector.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/IntelligenceFlowPlannerRuntime](DYLIBS/IntelligenceFlowPlannerRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/Versions/A/IntelligenceFlowPlannerSupport](DYLIBS/IntelligenceFlowPlannerSupport.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/Versions/A/IntelligenceFlowRuntime](DYLIBS/IntelligenceFlowRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowShared.framework/Versions/A/IntelligenceFlowShared](DYLIBS/IntelligenceFlowShared.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/Versions/A/IntelligencePlatform](DYLIBS/IntelligencePlatform.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/Versions/A/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/Versions/A/IntelligencePlatformLibrary](DYLIBS/IntelligencePlatformLibrary.md)
- [/System/Library/PrivateFrameworks/IntentsCore.framework/Versions/A/IntentsCore](DYLIBS/IntentsCore.md)
- [/System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/Versions/A/InternalSwiftProtobuf](DYLIBS/InternalSwiftProtobuf.md)
- [/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/Versions/A/IsolatedCoreAudioClient](DYLIBS/IsolatedCoreAudioClient.md)
- [/System/Library/PrivateFrameworks/JetCore.framework/Versions/A/JetCore](DYLIBS/JetCore.md)
- [/System/Library/PrivateFrameworks/JetEngine.framework/Versions/A/JetEngine](DYLIBS/JetEngine.md)
- [/System/Library/PrivateFrameworks/JetUI.framework/Versions/A/JetUI](DYLIBS/JetUI.md)
- [/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/Versions/A/KnowledgeGraphKit](DYLIBS/KnowledgeGraphKit.md)
- [/System/Library/PrivateFrameworks/LearnedFeatures.framework/Versions/A/LearnedFeatures](DYLIBS/LearnedFeatures.md)
- [/System/Library/PrivateFrameworks/LiftUI.framework/Versions/A/LiftUI](DYLIBS/LiftUI.md)
- [/System/Library/PrivateFrameworks/LighthouseBackground.framework/Versions/A/LighthouseBackground](DYLIBS/LighthouseBackground.md)
- [/System/Library/PrivateFrameworks/LighthouseDataProcessor.framework/Versions/A/LighthouseDataProcessor](DYLIBS/LighthouseDataProcessor.md)
- [/System/Library/PrivateFrameworks/LinkMetadata.framework/Versions/A/LinkMetadata](DYLIBS/LinkMetadata.md)
- [/System/Library/PrivateFrameworks/LinkPresentationStyleSheetParsing.framework/Versions/A/LinkPresentationStyleSheetParsing](DYLIBS/LinkPresentationStyleSheetParsing.md)
- [/System/Library/PrivateFrameworks/LinkServices.framework/Versions/A/LinkServices](DYLIBS/LinkServices.md)
- [/System/Library/PrivateFrameworks/LiveExecutionResultsProbe.framework/Versions/A/LiveExecutionResultsProbe](DYLIBS/LiveExecutionResultsProbe.md)
- [/System/Library/PrivateFrameworks/MFAAuthentication.framework/Versions/A/MFAAuthentication](DYLIBS/MFAAuthentication.md)
- [/System/Library/PrivateFrameworks/MLModelSpecification.framework/Versions/A/MLModelSpecification](DYLIBS/MLModelSpecification.md)
- [/System/Library/PrivateFrameworks/Mail.framework/Versions/A/Mail](DYLIBS/Mail.md)
- [/System/Library/PrivateFrameworks/MailCore.framework/Versions/A/MailCore](DYLIBS/MailCore.md)
- [/System/Library/PrivateFrameworks/MailSupport.framework/Versions/A/MailSupport](DYLIBS/MailSupport.md)
- [/System/Library/PrivateFrameworks/MailUI.framework/Versions/A/MailUI](DYLIBS/MailUI.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/Versions/A/MapsSync](DYLIBS/MapsSync.md)
- [/System/Library/PrivateFrameworks/MatterPlugin.framework/Versions/A/MatterPlugin](DYLIBS/MatterPlugin.md)
- [/System/Library/PrivateFrameworks/MediaControlSender.framework/Versions/A/MediaControlSender](DYLIBS/MediaControlSender.md)
- [/System/Library/PrivateFrameworks/MediaCoreUI.framework/Versions/A/MediaCoreUI](DYLIBS/MediaCoreUI.md)
- [/System/Library/PrivateFrameworks/MediaExperience.framework/Versions/A/MediaExperience](DYLIBS/MediaExperience.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/Versions/A/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Versions/A/MediaRemote](DYLIBS/MediaRemote.md)
- [/System/Library/PrivateFrameworks/MessageProtection.framework/Versions/A/MessageProtection](DYLIBS/MessageProtection.md)
- [/System/Library/PrivateFrameworks/MessagesCloudSync.framework/Versions/A/MessagesCloudSync](DYLIBS/MessagesCloudSync.md)
- [/System/Library/PrivateFrameworks/MetadataUtilities.framework/Versions/A/MetadataUtilities](DYLIBS/MetadataUtilities.md)
- [/System/Library/PrivateFrameworks/MetricsFramework.framework/Versions/A/MetricsFramework](DYLIBS/MetricsFramework.md)
- [/System/Library/PrivateFrameworks/MicroLocation.framework/Versions/A/MicroLocation](DYLIBS/MicroLocation.md)
- [/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/Versions/A/MicroLocationDaemon](DYLIBS/MicroLocationDaemon.md)
- [/System/Library/PrivateFrameworks/MobileActivationMacOS.framework/Versions/A/MobileActivationMacOS](DYLIBS/MobileActivationMacOS.md)
- [/System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset](DYLIBS/MobileAsset.md)
- [/System/Library/PrivateFrameworks/MobileAssetExclaveServices.framework/Versions/A/MobileAssetExclaveServices](DYLIBS/MobileAssetExclaveServices.md)
- [/System/Library/PrivateFrameworks/ModelCatalog.framework/Versions/A/ModelCatalog](DYLIBS/ModelCatalog.md)
- [/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/Versions/A/ModelCatalogRuntime](DYLIBS/ModelCatalogRuntime.md)
- [/System/Library/PrivateFrameworks/ModelManagerServices.framework/Versions/A/ModelManagerServices](DYLIBS/ModelManagerServices.md)
- [/System/Library/PrivateFrameworks/Morpheus.framework/Versions/A/Morpheus](DYLIBS/Morpheus.md)
- [/System/Library/PrivateFrameworks/MorpheusExtensions.framework/Versions/A/MorpheusExtensions](DYLIBS/MorpheusExtensions.md)
- [/System/Library/PrivateFrameworks/MusicKitInternal.framework/Versions/A/MusicKitInternal](DYLIBS/MusicKitInternal.md)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/Versions/A/MusicLibrary](DYLIBS/MusicLibrary.md)
- [/System/Library/PrivateFrameworks/MusicUI.framework/Versions/A/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/PrivateFrameworks/NearField.framework/Versions/A/NearField](DYLIBS/NearField.md)
- [/System/Library/PrivateFrameworks/NetworkInfo.framework/Versions/A/NetworkInfo](DYLIBS/NetworkInfo.md)
- [/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/Versions/A/NetworkServiceProxy](DYLIBS/NetworkServiceProxy.md)
- [/System/Library/PrivateFrameworks/NetworkStatistics.framework/Versions/A/NetworkStatistics](DYLIBS/NetworkStatistics.md)
- [/System/Library/PrivateFrameworks/NeuralNetworks.framework/Versions/A/NeuralNetworks](DYLIBS/NeuralNetworks.md)
- [/System/Library/PrivateFrameworks/NeutrinoCore.framework/Versions/A/NeutrinoCore](DYLIBS/NeutrinoCore.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/Versions/A/NewDeviceOutreach](DYLIBS/NewDeviceOutreach.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreachMacUI.framework/Versions/A/NewDeviceOutreachMacUI](DYLIBS/NewDeviceOutreachMacUI.md)
- [/System/Library/PrivateFrameworks/NewsCore.framework/Versions/A/NewsCore](DYLIBS/NewsCore.md)
- [/System/Library/PrivateFrameworks/NewsToday.framework/Versions/A/NewsToday](DYLIBS/NewsToday.md)
- [/System/Library/PrivateFrameworks/NewsTransport.framework/Versions/A/NewsTransport](DYLIBS/NewsTransport.md)
- [/System/Library/PrivateFrameworks/Nexus.framework/Versions/A/Nexus](DYLIBS/Nexus.md)
- [/System/Library/PrivateFrameworks/NexusDaemon.framework/Versions/A/NexusDaemon](DYLIBS/NexusDaemon.md)
- [/System/Library/PrivateFrameworks/NotesEditor.framework/Versions/A/NotesEditor](DYLIBS/NotesEditor.md)
- [/System/Library/PrivateFrameworks/NotesHTML.framework/Versions/A/NotesHTML](DYLIBS/NotesHTML.md)
- [/System/Library/PrivateFrameworks/NotesShared.framework/Versions/A/NotesShared](DYLIBS/NotesShared.md)
- [/System/Library/PrivateFrameworks/NotesSupport.framework/Versions/A/NotesSupport](DYLIBS/NotesSupport.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/Versions/A/NotesUI](DYLIBS/NotesUI.md)
- [/System/Library/PrivateFrameworks/OAHSoftwareUpdate.framework/Versions/A/OAHSoftwareUpdate](DYLIBS/OAHSoftwareUpdate.md)
- [/System/Library/PrivateFrameworks/ODDIFramework.framework/Versions/A/ODDIFramework](DYLIBS/ODDIFramework.md)
- [/System/Library/PrivateFrameworks/OSAnalytics.framework/Versions/A/OSAnalytics](DYLIBS/OSAnalytics.md)
- [/System/Library/PrivateFrameworks/OSEligibility.framework/Versions/A/OSEligibility](DYLIBS/OSEligibility.md)
- [/System/Library/PrivateFrameworks/OSInstaller.framework/Versions/A/OSInstaller](DYLIBS/OSInstaller.md)
- [/System/Library/PrivateFrameworks/OSUpdate.framework/Versions/A/OSUpdate](DYLIBS/OSUpdate.md)
- [/System/Library/PrivateFrameworks/OmniSearch.framework/Versions/A/OmniSearch](DYLIBS/OmniSearch.md)
- [/System/Library/PrivateFrameworks/OmniSearchTypes.framework/Versions/A/OmniSearchTypes](DYLIBS/OmniSearchTypes.md)
- [/System/Library/PrivateFrameworks/OnBoardingKit.framework/Versions/A/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/PrivateFrameworks/OnDeviceEvalRuntime.framework/Versions/A/OnDeviceEvalRuntime](DYLIBS/OnDeviceEvalRuntime.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorageCore.framework/Versions/A/OnDeviceStorageCore](DYLIBS/OnDeviceStorageCore.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorageInternal.framework/Versions/A/OnDeviceStorageInternal](DYLIBS/OnDeviceStorageInternal.md)
- [/System/Library/PrivateFrameworks/OpenAPIURLSessionInternal.framework/Versions/A/OpenAPIURLSessionInternal](DYLIBS/OpenAPIURLSessionInternal.md)
- [/System/Library/PrivateFrameworks/PackageKit.framework/Versions/A/PackageKit](DYLIBS/PackageKit.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/Versions/A/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/PrivateFrameworks/ParsecSubscriptionServiceSupport.framework/Versions/A/ParsecSubscriptionServiceSupport](DYLIBS/ParsecSubscriptionServiceSupport.md)
- [/System/Library/PrivateFrameworks/PassKitMacHelper.framework/Versions/A/PassKitMacHelper](DYLIBS/PassKitMacHelper.md)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/Versions/A/PasswordManagerUI](DYLIBS/PasswordManagerUI.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/Versions/A/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PegasusKit.framework/Versions/A/PegasusKit](DYLIBS/PegasusKit.md)
- [/System/Library/PrivateFrameworks/PegasusPersistence.framework/Versions/A/PegasusPersistence](DYLIBS/PegasusPersistence.md)
- [/System/Library/PrivateFrameworks/PerformanceControlKit.framework/Versions/A/PerformanceControlKit](DYLIBS/PerformanceControlKit.md)
- [/System/Library/PrivateFrameworks/PersonalizationPortraitInternals.framework/Versions/A/PersonalizationPortraitInternals](DYLIBS/PersonalizationPortraitInternals.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/Versions/A/PersonalizedSensing](DYLIBS/PersonalizedSensing.md)
- [/System/Library/PrivateFrameworks/PhoneSnippetUI.framework/Versions/A/PhoneSnippetUI](DYLIBS/PhoneSnippetUI.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Versions/A/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotoImaging.framework/Versions/A/PhotoImaging](DYLIBS/PhotoImaging.md)
- [/System/Library/PrivateFrameworks/PhotosGraph.framework/Versions/A/PhotosGraph](DYLIBS/PhotosGraph.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/Versions/A/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/Versions/A/PhotosSwiftUICore](DYLIBS/PhotosSwiftUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/Versions/A/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIEdit.framework/Versions/A/PhotosUIEdit](DYLIBS/PhotosUIEdit.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/Versions/A/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PnROnDeviceFramework.framework/Versions/A/PnROnDeviceFramework](DYLIBS/PnROnDeviceFramework.md)
- [/System/Library/PrivateFrameworks/PodcastsFoundation.framework/Versions/A/PodcastsFoundation](DYLIBS/PodcastsFoundation.md)
- [/System/Library/PrivateFrameworks/PodcastsKit.framework/Versions/A/PodcastsKit](DYLIBS/PodcastsKit.md)
- [/System/Library/PrivateFrameworks/PoirotBlocks.framework/Versions/A/PoirotBlocks](DYLIBS/PoirotBlocks.md)
- [/System/Library/PrivateFrameworks/PoirotSchematizer.framework/Versions/A/PoirotSchematizer](DYLIBS/PoirotSchematizer.md)
- [/System/Library/PrivateFrameworks/PoirotUDFs.framework/Versions/A/PoirotUDFs](DYLIBS/PoirotUDFs.md)
- [/System/Library/PrivateFrameworks/PowerUI.framework/Versions/A/PowerUI](DYLIBS/PowerUI.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/Versions/A/PowerlogCore](DYLIBS/PowerlogCore.md)
- [/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/Versions/A/PowerlogFullOperators](DYLIBS/PowerlogFullOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/Versions/A/PowerlogHelperdOperators](DYLIBS/PowerlogHelperdOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/Versions/A/PowerlogLiteOperators](DYLIBS/PowerlogLiteOperators.md)
- [/System/Library/PrivateFrameworks/PreviewShellKit.framework/Versions/A/PreviewShellKit](DYLIBS/PreviewShellKit.md)
- [/System/Library/PrivateFrameworks/PreviewsFoundationOS.framework/Versions/A/PreviewsFoundationOS](DYLIBS/PreviewsFoundationOS.md)
- [/System/Library/PrivateFrameworks/PreviewsInjection.framework/Versions/A/PreviewsInjection](DYLIBS/PreviewsInjection.md)
- [/System/Library/PrivateFrameworks/PreviewsMessagingOS.framework/Versions/A/PreviewsMessagingOS](DYLIBS/PreviewsMessagingOS.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Versions/A/PreviewsOSSupport](DYLIBS/PreviewsOSSupport.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/Versions/A/PrivateCloudCompute](DYLIBS/PrivateCloudCompute.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/Versions/A/PrivateFederatedLearning](DYLIBS/PrivateFederatedLearning.md)
- [/System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/Versions/A/ProactiveDaemonSupport](DYLIBS/ProactiveDaemonSupport.md)
- [/System/Library/PrivateFrameworks/ProactiveHarvesting.framework/Versions/A/ProactiveHarvesting](DYLIBS/ProactiveHarvesting.md)
- [/System/Library/PrivateFrameworks/ProactiveInputPredictionsInternals.framework/Versions/A/ProactiveInputPredictionsInternals](DYLIBS/ProactiveInputPredictionsInternals.md)
- [/System/Library/PrivateFrameworks/ProactiveML.framework/Versions/A/ProactiveML](DYLIBS/ProactiveML.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarization.framework/Versions/A/ProactiveSummarization](DYLIBS/ProactiveSummarization.md)
- [/System/Library/PrivateFrameworks/ProductKit.framework/Versions/A/ProductKit](DYLIBS/ProductKit.md)
- [/System/Library/PrivateFrameworks/PromotedContentJetClient.framework/Versions/A/PromotedContentJetClient](DYLIBS/PromotedContentJetClient.md)
- [/System/Library/PrivateFrameworks/ProtoDataExtractor.framework/Versions/A/ProtoDataExtractor](DYLIBS/ProtoDataExtractor.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetupUI.framework/Versions/A/ProximityAppleIDSetupUI](DYLIBS/ProximityAppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/QOSToolkit.framework/Versions/A/QOSToolkit](DYLIBS/QOSToolkit.md)
- [/System/Library/PrivateFrameworks/QueryParser.framework/Versions/A/QueryParser](DYLIBS/QueryParser.md)
- [/System/Library/PrivateFrameworks/RTTUtilities.framework/Versions/A/RTTUtilities](DYLIBS/RTTUtilities.md)
- [/System/Library/PrivateFrameworks/RapidResourceDelivery.framework/Versions/A/RapidResourceDelivery](DYLIBS/RapidResourceDelivery.md)
- [/System/Library/PrivateFrameworks/Rapport.framework/Versions/A/Rapport](DYLIBS/Rapport.md)
- [/System/Library/PrivateFrameworks/RealityIO.framework/Versions/A/RealityIO](DYLIBS/RealityIO.md)
- [/System/Library/PrivateFrameworks/Recount.framework/Versions/A/Recount](DYLIBS/Recount.md)
- [/System/Library/PrivateFrameworks/ReminderKitInternal.framework/Versions/A/ReminderKitInternal](DYLIBS/ReminderKitInternal.md)
- [/System/Library/PrivateFrameworks/RemindersAppIntents.framework/Versions/A/RemindersAppIntents](DYLIBS/RemindersAppIntents.md)
- [/System/Library/PrivateFrameworks/RemindersIntentsFramework.framework/Versions/A/RemindersIntentsFramework](DYLIBS/RemindersIntentsFramework.md)
- [/System/Library/PrivateFrameworks/RemindersUICore.framework/Versions/A/RemindersUICore](DYLIBS/RemindersUICore.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/Versions/A/RemoteManagement](DYLIBS/RemoteManagement.md)
- [/System/Library/PrivateFrameworks/RemoteUI.framework/Versions/A/RemoteUI](DYLIBS/RemoteUI.md)
- [/System/Library/PrivateFrameworks/RenderBox.framework/Versions/A/RenderBox](DYLIBS/RenderBox.md)
- [/System/Library/PrivateFrameworks/ReplicatorCore.framework/Versions/A/ReplicatorCore](DYLIBS/ReplicatorCore.md)
- [/System/Library/PrivateFrameworks/ReplicatorEngine.framework/Versions/A/ReplicatorEngine](DYLIBS/ReplicatorEngine.md)
- [/System/Library/PrivateFrameworks/RequestDispatcherBridges.framework/Versions/A/RequestDispatcherBridges](DYLIBS/RequestDispatcherBridges.md)
- [/System/Library/PrivateFrameworks/ResponseUI.framework/Versions/A/ResponseUI](DYLIBS/ResponseUI.md)
- [/System/Library/PrivateFrameworks/SAObjects.framework/Versions/A/SAObjects](DYLIBS/SAObjects.md)
- [/System/Library/PrivateFrameworks/SPOwner.framework/Versions/A/SPOwner](DYLIBS/SPOwner.md)
- [/System/Library/PrivateFrameworks/Safari.framework/Versions/A/Safari](DYLIBS/Safari.md)
- [/System/Library/PrivateFrameworks/SafariCore.framework/Versions/A/SafariCore](DYLIBS/SafariCore.md)
- [/System/Library/PrivateFrameworks/SafariShared.framework/Versions/A/SafariShared](DYLIBS/SafariShared.md)
- [/System/Library/PrivateFrameworks/SafariSharedUI.framework/Versions/A/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/Library/PrivateFrameworks/SafariSwift.framework/Versions/A/SafariSwift](DYLIBS/SafariSwift.md)
- [/System/Library/PrivateFrameworks/SampleAnalysis.framework/Versions/A/SampleAnalysis](DYLIBS/SampleAnalysis.md)
- [/System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/Frameworks/ScreenReaderOutput.framework/Versions/A/ScreenReaderOutput](DYLIBS/ScreenReaderOutput.md)
- [/System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/ScreenReader](DYLIBS/ScreenReader.md)
- [/System/Library/PrivateFrameworks/ScreenSharing.framework/Versions/A/Frameworks/ScreenSharingUI.framework/Versions/A/ScreenSharingUI](DYLIBS/ScreenSharingUI.md)
- [/System/Library/PrivateFrameworks/ScreenSharingKit.framework/Versions/A/ScreenSharingKit](DYLIBS/ScreenSharingKit.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/Versions/A/ScreenTimeCore](DYLIBS/ScreenTimeCore.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/Versions/A/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUI.framework/Versions/A/ScreenTimeUI](DYLIBS/ScreenTimeUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/Versions/A/ScreenTimeUICore](DYLIBS/ScreenTimeUICore.md)
- [/System/Library/PrivateFrameworks/SearchAds.framework/Versions/A/SearchAds](DYLIBS/SearchAds.md)
- [/System/Library/PrivateFrameworks/SearchAssets.framework/Versions/A/SearchAssets](DYLIBS/SearchAssets.md)
- [/System/Library/PrivateFrameworks/SearchFoundation.framework/Versions/A/SearchFoundation](DYLIBS/SearchFoundation.md)
- [/System/Library/PrivateFrameworks/SearchUI.framework/Versions/A/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisUI.framework/Versions/A/SensitiveContentAnalysisUI](DYLIBS/SensitiveContentAnalysisUI.md)
- [/System/Library/PrivateFrameworks/Sentry.framework/Versions/A/Sentry](DYLIBS/Sentry.md)
- [/System/Library/PrivateFrameworks/Settings.framework/Versions/A/Settings](DYLIBS/Settings.md)
- [/System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/Versions/A/SetupAssistantSupportUI](DYLIBS/SetupAssistantSupportUI.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/Versions/A/Sharing](DYLIBS/Sharing.md)
- [/System/Library/PrivateFrameworks/SharingXPCServices.framework/Versions/A/SharingXPCServices](DYLIBS/SharingXPCServices.md)
- [/System/Library/PrivateFrameworks/ShazamEvents.framework/Versions/A/ShazamEvents](DYLIBS/ShazamEvents.md)
- [/System/Library/PrivateFrameworks/ShazamKitUI.framework/Versions/A/ShazamKitUI](DYLIBS/ShazamKitUI.md)
- [/System/Library/PrivateFrameworks/ShimGameServices.framework/Versions/A/ShimGameServices](DYLIBS/ShimGameServices.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/Versions/A/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/Versions/A/SiriAppLaunchIntents](DYLIBS/SiriAppLaunchIntents.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchUIFramework.framework/Versions/A/SiriAppLaunchUIFramework](DYLIBS/SiriAppLaunchUIFramework.md)
- [/System/Library/PrivateFrameworks/SiriAudioInternal.framework/Versions/A/SiriAudioInternal](DYLIBS/SiriAudioInternal.md)
- [/System/Library/PrivateFrameworks/SiriAudioSupport.framework/Versions/A/SiriAudioSupport](DYLIBS/SiriAudioSupport.md)
- [/System/Library/PrivateFrameworks/SiriAutoComplete.framework/Versions/A/SiriAutoComplete](DYLIBS/SiriAutoComplete.md)
- [/System/Library/PrivateFrameworks/SiriCalendarIntents.framework/Versions/A/SiriCalendarIntents](DYLIBS/SiriCalendarIntents.md)
- [/System/Library/PrivateFrameworks/SiriCalendarUI.framework/Versions/A/SiriCalendarUI](DYLIBS/SiriCalendarUI.md)
- [/System/Library/PrivateFrameworks/SiriCam.framework/Versions/A/SiriCam](DYLIBS/SiriCam.md)
- [/System/Library/PrivateFrameworks/SiriContactsIntents.framework/Versions/A/SiriContactsIntents](DYLIBS/SiriContactsIntents.md)
- [/System/Library/PrivateFrameworks/SiriContactsUI.framework/Versions/A/SiriContactsUI](DYLIBS/SiriContactsUI.md)
- [/System/Library/PrivateFrameworks/SiriCore.framework/Versions/A/SiriCore](DYLIBS/SiriCore.md)
- [/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/Versions/A/SiriCrossDeviceArbitration](DYLIBS/SiriCrossDeviceArbitration.md)
- [/System/Library/PrivateFrameworks/SiriDialogEngine.framework/Versions/A/SiriDialogEngine](DYLIBS/SiriDialogEngine.md)
- [/System/Library/PrivateFrameworks/SiriFindMy.framework/Versions/A/SiriFindMy](DYLIBS/SiriFindMy.md)
- [/System/Library/PrivateFrameworks/SiriFlowEnvironment.framework/Versions/A/SiriFlowEnvironment](DYLIBS/SiriFlowEnvironment.md)
- [/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/SiriIdentityInternal](DYLIBS/SiriIdentityInternal.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/Versions/A/SiriInference](DYLIBS/SiriInference.md)
- [/System/Library/PrivateFrameworks/SiriInferenceFlow.framework/Versions/A/SiriInferenceFlow](DYLIBS/SiriInferenceFlow.md)
- [/System/Library/PrivateFrameworks/SiriInformationSearch.framework/Versions/A/SiriInformationSearch](DYLIBS/SiriInformationSearch.md)
- [/System/Library/PrivateFrameworks/SiriInstrumentation.framework/Versions/A/SiriInstrumentation](DYLIBS/SiriInstrumentation.md)
- [/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/SiriKitFlow](DYLIBS/SiriKitFlow.md)
- [/System/Library/PrivateFrameworks/SiriKitRuntime.framework/Versions/A/SiriKitRuntime](DYLIBS/SiriKitRuntime.md)
- [/System/Library/PrivateFrameworks/SiriMailInternal.framework/Versions/A/SiriMailInternal](DYLIBS/SiriMailInternal.md)
- [/System/Library/PrivateFrameworks/SiriMailUI.framework/Versions/A/SiriMailUI](DYLIBS/SiriMailUI.md)
- [/System/Library/PrivateFrameworks/SiriMessageBus.framework/Versions/A/SiriMessageBus](DYLIBS/SiriMessageBus.md)
- [/System/Library/PrivateFrameworks/SiriMessageTypes.framework/Versions/A/SiriMessageTypes](DYLIBS/SiriMessageTypes.md)
- [/System/Library/PrivateFrameworks/SiriMessagesCommon.framework/Versions/A/SiriMessagesCommon](DYLIBS/SiriMessagesCommon.md)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/Versions/A/SiriMessagesFlow](DYLIBS/SiriMessagesFlow.md)
- [/System/Library/PrivateFrameworks/SiriMessagesUI.framework/Versions/A/SiriMessagesUI](DYLIBS/SiriMessagesUI.md)
- [/System/Library/PrivateFrameworks/SiriNLUTypes.framework/Versions/A/SiriNLUTypes](DYLIBS/SiriNLUTypes.md)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageGeneration.framework/Versions/A/SiriNaturalLanguageGeneration](DYLIBS/SiriNaturalLanguageGeneration.md)
- [/System/Library/PrivateFrameworks/SiriNetwork.framework/Versions/A/SiriNetwork](DYLIBS/SiriNetwork.md)
- [/System/Library/PrivateFrameworks/SiriNotebook.framework/Versions/A/SiriNotebook](DYLIBS/SiriNotebook.md)
- [/System/Library/PrivateFrameworks/SiriNotebookUI.framework/Versions/A/SiriNotebookUI](DYLIBS/SiriNotebookUI.md)
- [/System/Library/PrivateFrameworks/SiriNotificationsIntents.framework/Versions/A/SiriNotificationsIntents](DYLIBS/SiriNotificationsIntents.md)
- [/System/Library/PrivateFrameworks/SiriOntology.framework/Versions/A/SiriOntology](DYLIBS/SiriOntology.md)
- [/System/Library/PrivateFrameworks/SiriOntologyProtobuf.framework/Versions/A/SiriOntologyProtobuf](DYLIBS/SiriOntologyProtobuf.md)
- [/System/Library/PrivateFrameworks/SiriPaymentsIntents.framework/Versions/A/SiriPaymentsIntents](DYLIBS/SiriPaymentsIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/SiriPlaybackControlIntents](DYLIBS/SiriPlaybackControlIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlSupport.framework/Versions/A/SiriPlaybackControlSupport](DYLIBS/SiriPlaybackControlSupport.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/Versions/A/SiriPrivateLearningAnalytics](DYLIBS/SiriPrivateLearningAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningInference.framework/Versions/A/SiriPrivateLearningInference](DYLIBS/SiriPrivateLearningInference.md)
- [/System/Library/PrivateFrameworks/SiriRemembers.framework/Versions/A/SiriRemembers](DYLIBS/SiriRemembers.md)
- [/System/Library/PrivateFrameworks/SiriRequestDispatcher.framework/Versions/A/SiriRequestDispatcher](DYLIBS/SiriRequestDispatcher.md)
- [/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/Versions/A/SiriSettingsIntents](DYLIBS/SiriSettingsIntents.md)
- [/System/Library/PrivateFrameworks/SiriSetup.framework/Versions/A/SiriSetup](DYLIBS/SiriSetup.md)
- [/System/Library/PrivateFrameworks/SiriSharedUI.framework/Versions/A/SiriSharedUI](DYLIBS/SiriSharedUI.md)
- [/System/Library/PrivateFrameworks/SiriSignals.framework/Versions/A/SiriSignals](DYLIBS/SiriSignals.md)
- [/System/Library/PrivateFrameworks/SiriSuggestions.framework/Versions/A/SiriSuggestions](DYLIBS/SiriSuggestions.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsIntelligence.framework/Versions/A/SiriSuggestionsIntelligence](DYLIBS/SiriSuggestionsIntelligence.md)
- [/System/Library/PrivateFrameworks/SiriTTS.framework/Versions/A/SiriTTS](DYLIBS/SiriTTS.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/Versions/A/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SiriTranslationIntents.framework/Versions/A/SiriTranslationIntents](DYLIBS/SiriTranslationIntents.md)
- [/System/Library/PrivateFrameworks/SiriUI.framework/Versions/A/SiriUI](DYLIBS/SiriUI.md)
- [/System/Library/PrivateFrameworks/SiriUICore.framework/Versions/A/SiriUICore](DYLIBS/SiriUICore.md)
- [/System/Library/PrivateFrameworks/SiriUIFoundation.framework/Versions/A/SiriUIFoundation](DYLIBS/SiriUIFoundation.md)
- [/System/Library/PrivateFrameworks/SiriVOX.framework/Versions/A/SiriVOX](DYLIBS/SiriVOX.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/Versions/A/SiriVideoIntents](DYLIBS/SiriVideoIntents.md)
- [/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/SkyLight](DYLIBS/SkyLight.md)
- [/System/Library/PrivateFrameworks/SnippetKit.framework/Versions/A/SnippetKit](DYLIBS/SnippetKit.md)
- [/System/Library/PrivateFrameworks/SnippetUI.framework/Versions/A/SnippetUI](DYLIBS/SnippetUI.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/Versions/A/SoftwareUpdateCore](DYLIBS/SoftwareUpdateCore.md)
- [/System/Library/PrivateFrameworks/SonicFoundation.framework/Versions/A/SonicFoundation](DYLIBS/SonicFoundation.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/Versions/A/SonicKit](DYLIBS/SonicKit.md)
- [/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/SpeakerRecognition](DYLIBS/SpeakerRecognition.md)
- [/System/Library/PrivateFrameworks/SportsKit.framework/Versions/A/SportsKit](DYLIBS/SportsKit.md)
- [/System/Library/PrivateFrameworks/Spotlight.framework/Versions/A/Spotlight](DYLIBS/Spotlight.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/Versions/A/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
- [/System/Library/PrivateFrameworks/SpotlightEmbedding.framework/Versions/A/SpotlightEmbedding](DYLIBS/SpotlightEmbedding.md)
- [/System/Library/PrivateFrameworks/SpotlightFoundation.framework/Versions/A/SpotlightFoundation](DYLIBS/SpotlightFoundation.md)
- [/System/Library/PrivateFrameworks/SpotlightIndex.framework/Versions/A/SpotlightIndex](DYLIBS/SpotlightIndex.md)
- [/System/Library/PrivateFrameworks/SpotlightKnowledge.framework/Versions/A/SpotlightKnowledge](DYLIBS/SpotlightKnowledge.md)
- [/System/Library/PrivateFrameworks/SpotlightLinguistics.framework/Versions/A/SpotlightLinguistics](DYLIBS/SpotlightLinguistics.md)
- [/System/Library/PrivateFrameworks/SpotlightResources.framework/Versions/A/SpotlightResources](DYLIBS/SpotlightResources.md)
- [/System/Library/PrivateFrameworks/SpotlightServices.framework/Versions/A/SpotlightServices](DYLIBS/SpotlightServices.md)
- [/System/Library/PrivateFrameworks/StocksCore.framework/Versions/A/StocksCore](DYLIBS/StocksCore.md)
- [/System/Library/PrivateFrameworks/SuggestionsSpotlightMetrics.framework/Versions/A/SuggestionsSpotlightMetrics](DYLIBS/SuggestionsSpotlightMetrics.md)
- [/System/Library/PrivateFrameworks/SummarizationKit.framework/Versions/A/SummarizationKit](DYLIBS/SummarizationKit.md)
- [/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/Versions/A/SymptomDiagnosticReporter](DYLIBS/SymptomDiagnosticReporter.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Versions/A/Frameworks/SymptomEvaluator.framework/Versions/A/SymptomEvaluator](DYLIBS/SymptomEvaluator.md)
- [/System/Library/PrivateFrameworks/SyncedDefaultsDaemon.framework/Versions/A/SyncedDefaultsDaemon](DYLIBS/SyncedDefaultsDaemon.md)
- [/System/Library/PrivateFrameworks/SyncedModels.framework/Versions/A/SyncedModels](DYLIBS/SyncedModels.md)
- [/System/Library/PrivateFrameworks/SystemAdministrationInterface.framework/Versions/A/SystemAdministrationInterface](DYLIBS/SystemAdministrationInterface.md)
- [/System/Library/PrivateFrameworks/SystemServiceMonitor.framework/Versions/A/SystemServiceMonitor](DYLIBS/SystemServiceMonitor.md)
- [/System/Library/PrivateFrameworks/SystemStatus.framework/Versions/A/SystemStatus](DYLIBS/SystemStatus.md)
- [/System/Library/PrivateFrameworks/SystemStatusServer.framework/Versions/A/SystemStatusServer](DYLIBS/SystemStatusServer.md)
- [/System/Library/PrivateFrameworks/SystemStatusUI.framework/Versions/A/SystemStatusUI](DYLIBS/SystemStatusUI.md)
- [/System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC](DYLIBS/TCC.md)
- [/System/Library/PrivateFrameworks/TVPlayback.framework/Versions/A/TVPlayback](DYLIBS/TVPlayback.md)
- [/System/Library/PrivateFrameworks/TVRemoteCore.framework/Versions/A/TVRemoteCore](DYLIBS/TVRemoteCore.md)
- [/System/Library/PrivateFrameworks/TeaFoundation.framework/Versions/A/TeaFoundation](DYLIBS/TeaFoundation.md)
- [/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/Versions/A/TelephonyBlastDoorSupport](DYLIBS/TelephonyBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/Versions/A/TelephonyUtilities](DYLIBS/TelephonyUtilities.md)
- [/System/Library/PrivateFrameworks/TextComposer.framework/Versions/A/TextComposer](DYLIBS/TextComposer.md)
- [/System/Library/PrivateFrameworks/TextInputCore.framework/Versions/A/TextInputCore](DYLIBS/TextInputCore.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingUI.framework/Versions/A/TextToSpeechVoiceBankingUI](DYLIBS/TextToSpeechVoiceBankingUI.md)
- [/System/Library/PrivateFrameworks/TimeMachine.framework/Versions/A/TimeMachine](DYLIBS/TimeMachine.md)
- [/System/Library/PrivateFrameworks/TimeMachinePrivate.framework/Versions/A/TimeMachinePrivate](DYLIBS/TimeMachinePrivate.md)
- [/System/Library/PrivateFrameworks/TipKitCore.framework/Versions/A/TipKitCore](DYLIBS/TipKitCore.md)
- [/System/Library/PrivateFrameworks/TipsCore.framework/Versions/A/TipsCore](DYLIBS/TipsCore.md)
- [/System/Library/PrivateFrameworks/TipsDaemon.framework/Versions/A/TipsDaemon](DYLIBS/TipsDaemon.md)
- [/System/Library/PrivateFrameworks/TokenGeneration.framework/Versions/A/TokenGeneration](DYLIBS/TokenGeneration.md)
- [/System/Library/PrivateFrameworks/TokenGenerationCore.framework/Versions/A/TokenGenerationCore](DYLIBS/TokenGenerationCore.md)
- [/System/Library/PrivateFrameworks/TokenGenerationInference.framework/Versions/A/TokenGenerationInference](DYLIBS/TokenGenerationInference.md)
- [/System/Library/PrivateFrameworks/ToolKit.framework/Versions/A/ToolKit](DYLIBS/ToolKit.md)
- [/System/Library/PrivateFrameworks/TranslationDaemon.framework/Versions/A/TranslationDaemon](DYLIBS/TranslationDaemon.md)
- [/System/Library/PrivateFrameworks/TransparencyUI.framework/Versions/A/TransparencyUI](DYLIBS/TransparencyUI.md)
- [/System/Library/PrivateFrameworks/Trial.framework/Versions/A/Trial](DYLIBS/Trial.md)
- [/System/Library/PrivateFrameworks/TrialServer.framework/Versions/A/TrialServer](DYLIBS/TrialServer.md)
- [/System/Library/PrivateFrameworks/TypistFramework.framework/Versions/A/TypistFramework](DYLIBS/TypistFramework.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceIntents.framework/Versions/A/UIIntelligenceIntents](DYLIBS/UIIntelligenceIntents.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupport.framework/Versions/A/UIIntelligenceSupport](DYLIBS/UIIntelligenceSupport.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupportAgent.framework/Versions/A/UIIntelligenceSupportAgent](DYLIBS/UIIntelligenceSupportAgent.md)
- [/System/Library/PrivateFrameworks/UIKitMacHelper.framework/Versions/A/UIKitMacHelper](DYLIBS/UIKitMacHelper.md)
- [/System/Library/PrivateFrameworks/UIKitServices.framework/Versions/A/UIKitServices](DYLIBS/UIKitServices.md)
- [/System/Library/PrivateFrameworks/USTBridge.framework/Versions/A/USTBridge](DYLIBS/USTBridge.md)
- [/System/Library/PrivateFrameworks/USTBridgeConnection.framework/Versions/A/USTBridgeConnection](DYLIBS/USTBridgeConnection.md)
- [/System/Library/PrivateFrameworks/UVCFamily.framework/Versions/A/UVCFamily](DYLIBS/UVCFamily.md)
- [/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/Versions/A/UnifiedAssetFramework](DYLIBS/UnifiedAssetFramework.md)
- [/System/Library/PrivateFrameworks/UnifiedMessagingKit.framework/Versions/A/UnifiedMessagingKit](DYLIBS/UnifiedMessagingKit.md)
- [/System/Library/PrivateFrameworks/UniversalControl.framework/Versions/A/UniversalControl](DYLIBS/UniversalControl.md)
- [/System/Library/PrivateFrameworks/UniversalDrag.framework/Versions/A/UniversalDrag](DYLIBS/UniversalDrag.md)
- [/System/Library/PrivateFrameworks/UniversalHID.framework/Versions/A/UniversalHID](DYLIBS/UniversalHID.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Versions/A/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsKit.framework/Versions/A/UserNotificationsKit](DYLIBS/UserNotificationsKit.md)
- [/System/Library/PrivateFrameworks/VFX.framework/Versions/A/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/Versions/A/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/PrivateFrameworks/VectorSearch.framework/Versions/A/VectorSearch](DYLIBS/VectorSearch.md)
- [/System/Library/PrivateFrameworks/VideoProcessing.framework/Versions/A/VideoProcessing](DYLIBS/VideoProcessing.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/Versions/A/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VisualGeneration.framework/Versions/A/VisualGeneration](DYLIBS/VisualGeneration.md)
- [/System/Library/PrivateFrameworks/VisualIntelligence.framework/Versions/A/VisualIntelligence](DYLIBS/VisualIntelligence.md)
- [/System/Library/PrivateFrameworks/VisualPairing.framework/Versions/A/VisualPairing](DYLIBS/VisualPairing.md)
- [/System/Library/PrivateFrameworks/VoiceActions.framework/Versions/A/VoiceActions](DYLIBS/VoiceActions.md)
- [/System/Library/PrivateFrameworks/VoiceControlUI.framework/Versions/A/VoiceControlUI](DYLIBS/VoiceControlUI.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Versions/A/VoiceShortcuts](DYLIBS/VoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/Versions/A/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/Wallpaper.framework/Versions/A/Wallpaper](DYLIBS/Wallpaper.md)
- [/System/Library/PrivateFrameworks/WallpaperFoundation.framework/Versions/A/WallpaperFoundation](DYLIBS/WallpaperFoundation.md)
- [/System/Library/PrivateFrameworks/WatchListKit.framework/Versions/A/WatchListKit](DYLIBS/WatchListKit.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/Versions/A/WeatherDaemon](DYLIBS/WeatherDaemon.md)
- [/System/Library/PrivateFrameworks/WebBookmarks.framework/Versions/A/WebBookmarks](DYLIBS/WebBookmarks.md)
- [/System/Library/PrivateFrameworks/WebDriver.framework/Versions/A/WebDriver](DYLIBS/WebDriver.md)
- [/System/Library/PrivateFrameworks/WebInspector.framework/Versions/A/WebInspector](DYLIBS/WebInspector.md)
- [/System/Library/PrivateFrameworks/WiFiAnalytics.framework/Versions/A/WiFiAnalytics](DYLIBS/WiFiAnalytics.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/Versions/A/WiFiPolicy](DYLIBS/WiFiPolicy.md)
- [/System/Library/PrivateFrameworks/WindowManager.framework/Versions/A/WindowManager](DYLIBS/WindowManager.md)
- [/System/Library/PrivateFrameworks/WirelessProximity.framework/Versions/A/WirelessProximity](DYLIBS/WirelessProximity.md)
- [/System/Library/PrivateFrameworks/WorkflowEditor.framework/Versions/A/WorkflowEditor](DYLIBS/WorkflowEditor.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/Versions/A/WorkflowKit](DYLIBS/WorkflowKit.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/Versions/A/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/PrivateFrameworks/WorkflowUICore.framework/Versions/A/WorkflowUICore](DYLIBS/WorkflowUICore.md)
- [/System/Library/PrivateFrameworks/WritingToolsUI.framework/Versions/A/WritingToolsUI](DYLIBS/WritingToolsUI.md)
- [/System/Library/PrivateFrameworks/XOJIT.framework/Versions/A/XOJIT](DYLIBS/XOJIT.md)
- [/System/Library/PrivateFrameworks/ZeoliteFramework.framework/Versions/A/ZeoliteFramework](DYLIBS/ZeoliteFramework.md)
- [/System/Library/PrivateFrameworks/ZeoliteLanguage.framework/Versions/A/ZeoliteLanguage](DYLIBS/ZeoliteLanguage.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/Versions/A/ZhuGeSupport](DYLIBS/ZhuGeSupport.md)
- [/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/Versions/A/_JetEngine_SwiftUI](DYLIBS/_JetEngine_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/Versions/A/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_SonicKit_MusicKit.framework/Versions/A/_SonicKit_MusicKit](DYLIBS/_SonicKit_MusicKit.md)
- [/System/Library/PrivateFrameworks/iCloudDriveCore.framework/Versions/A/iCloudDriveCore](DYLIBS/iCloudDriveCore.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/Versions/A/iCloudQuotaUI](DYLIBS/iCloudQuotaUI.md)
- [/System/Library/PrivateFrameworks/ktrace.framework/Versions/A/ktrace](DYLIBS/ktrace.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/MobileSafariUI.axbundle/Contents/MacOS/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/Podcasts.axbundle/Contents/MacOS/Podcasts](DYLIBS/Podcasts.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/SwiftUI.axbundle/Contents/MacOS/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/UIKit.axbundle/Contents/MacOS/UIKit](DYLIBS/UIKit.md)
- [/System/iOSSupport/System/Library/Frameworks/Assignables.framework/Versions/A/Assignables](DYLIBS/Assignables.md)
- [/System/iOSSupport/System/Library/Frameworks/AuthenticationServices.framework/Versions/A/AuthenticationServices](DYLIBS/AuthenticationServices.md)
- [/System/iOSSupport/System/Library/Frameworks/CarPlay.framework/Versions/A/CarPlay](DYLIBS/CarPlay.md)
- [/System/iOSSupport/System/Library/Frameworks/Charts.framework/Versions/A/Charts](DYLIBS/Charts.md)
- [/System/iOSSupport/System/Library/Frameworks/ContactsUI.framework/Versions/A/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/iOSSupport/System/Library/Frameworks/CoreAudioKit.framework/Versions/A/CoreAudioKit](DYLIBS/CoreAudioKit.md)
- [/System/iOSSupport/System/Library/Frameworks/EventKitUI.framework/Versions/A/EventKitUI](DYLIBS/EventKitUI.md)
- [/System/iOSSupport/System/Library/Frameworks/HomeKit.framework/Versions/A/HomeKit](DYLIBS/HomeKit.md)
- [/System/iOSSupport/System/Library/Frameworks/ImagePlayground.framework/Versions/A/ImagePlayground](DYLIBS/ImagePlayground.md)
- [/System/iOSSupport/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/iOSSupport/System/Library/Frameworks/LiveCommunicationKit.framework/Versions/A/LiveCommunicationKit](DYLIBS/LiveCommunicationKit.md)
- [/System/iOSSupport/System/Library/Frameworks/MediaPlayer.framework/Versions/A/MediaPlayer](DYLIBS/MediaPlayer.md)
- [/System/iOSSupport/System/Library/Frameworks/PencilKit.framework/Versions/A/PencilKit](DYLIBS/PencilKit.md)
- [/System/iOSSupport/System/Library/Frameworks/PhotosUI.framework/Versions/A/PhotosUI](DYLIBS/PhotosUI.md)
- [/System/iOSSupport/System/Library/Frameworks/ProximityReader.framework/Versions/A/ProximityReader](DYLIBS/ProximityReader.md)
- [/System/iOSSupport/System/Library/Frameworks/RealityFoundation.framework/Versions/A/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/iOSSupport/System/Library/Frameworks/RealityKit.framework/Versions/A/RealityKit](DYLIBS/RealityKit.md)
- [/System/iOSSupport/System/Library/Frameworks/RoomPlan.framework/Versions/A/RoomPlan](DYLIBS/RoomPlan.md)
- [/System/iOSSupport/System/Library/Frameworks/SceneKit.framework/Versions/A/SceneKit](DYLIBS/SceneKit.md)
- [/System/iOSSupport/System/Library/Frameworks/StoreKit.framework/Versions/A/StoreKit](DYLIBS/StoreKit.md)
- [/System/iOSSupport/System/Library/Frameworks/SwiftUI.framework/Versions/A/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/iOSSupport/System/Library/Frameworks/TipKit.framework/Versions/A/TipKit](DYLIBS/TipKit.md)
- [/System/iOSSupport/System/Library/Frameworks/UIKit.framework/Versions/A/UIKit](DYLIBS/UIKit.md)
- [/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/WebKit](DYLIBS/WebKit.md)
- [/System/iOSSupport/System/Library/Frameworks/WidgetKit.framework/Versions/A/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/iOSSupport/System/Library/Frameworks/_AppIntents_SwiftUI.framework/Versions/A/_AppIntents_SwiftUI](DYLIBS/_AppIntents_SwiftUI.md)
- [/System/iOSSupport/System/Library/Frameworks/_AppIntents_UIKit.framework/Versions/A/_AppIntents_UIKit](DYLIBS/_AppIntents_UIKit.md)
- [/System/iOSSupport/System/Library/Frameworks/_GroupActivities_UIKit.framework/Versions/A/_GroupActivities_UIKit](DYLIBS/_GroupActivities_UIKit.md)
- [/System/iOSSupport/System/Library/Frameworks/_MapKit_SwiftUI.framework/Versions/A/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/iOSSupport/System/Library/Frameworks/_StoreKit_SwiftUI.framework/Versions/A/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/AccessibilityUIService.framework/Versions/A/AccessibilityUIService](DYLIBS/AccessibilityUIService.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ActionKit.framework/Versions/A/ActionKit](DYLIBS/ActionKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Versions/A/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/Versions/A/AppleMediaServicesUIDynamic](DYLIBS/AppleMediaServicesUIDynamic.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/AvatarKit.framework/Versions/A/AvatarKit](DYLIBS/AvatarKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/BatteryCenterUI.framework/Versions/A/BatteryCenterUI](DYLIBS/BatteryCenterUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/CalculateUI.framework/Versions/A/CalculateUI](DYLIBS/CalculateUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/CalendarUIKit.framework/Versions/A/CalendarUIKit](DYLIBS/CalendarUIKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ChatKit.framework/Versions/A/ChatKit](DYLIBS/ChatKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ChronoKit.framework/Versions/A/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ChronoUIServices.framework/Versions/A/ChronoUIServices](DYLIBS/ChronoUIServices.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/CommunicationsUI.framework/Versions/A/CommunicationsUI](DYLIBS/CommunicationsUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ContactsAutocompleteUI.framework/Versions/A/ContactsAutocompleteUI](DYLIBS/ContactsAutocompleteUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ConversationKit.framework/Versions/A/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/CoreHapticsTools.framework/Versions/A/CoreHapticsTools](DYLIBS/CoreHapticsTools.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/CoreSuggestionsUI.framework/Versions/A/CoreSuggestionsUI](DYLIBS/CoreSuggestionsUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/FaceTimeNotificationUI.framework/Versions/A/FaceTimeNotificationUI](DYLIBS/FaceTimeNotificationUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/FindMyUICore.framework/Versions/A/FindMyUICore](DYLIBS/FindMyUICore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/GenerativeAssistantCommon.framework/Versions/A/GenerativeAssistantCommon](DYLIBS/GenerativeAssistantCommon.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/GenerativeAssistantSettings.framework/Versions/A/GenerativeAssistantSettings](DYLIBS/GenerativeAssistantSettings.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/GenerativeExperiencesUI.framework/Versions/A/GenerativeExperiencesUI](DYLIBS/GenerativeExperiencesUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/HelpKit.framework/Versions/A/HelpKit](DYLIBS/HelpKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/Home.framework/Versions/A/Home](DYLIBS/Home.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/Versions/A/HomeAccessoryControlUI](DYLIBS/HomeAccessoryControlUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/HomeAppIntents.framework/Versions/A/HomeAppIntents](DYLIBS/HomeAppIntents.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/HomeDataModel.framework/Versions/A/HomeDataModel](DYLIBS/HomeDataModel.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/Versions/A/HomeEnergyDaemon](DYLIBS/HomeEnergyDaemon.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/HomeEnergyUI.framework/Versions/A/HomeEnergyUI](DYLIBS/HomeEnergyUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/HomeUI.framework/Versions/A/HomeUI](DYLIBS/HomeUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/HomeUI2.framework/Versions/A/HomeUI2](DYLIBS/HomeUI2.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/IMCore.framework/Versions/A/IMCore](DYLIBS/IMCore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/IMDPersistence.framework/Versions/A/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/IMSharedUtilities.framework/Versions/A/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ImagePlaygroundInternal.framework/Versions/A/ImagePlaygroundInternal](DYLIBS/ImagePlaygroundInternal.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/IntlPreferences.framework/Versions/A/IntlPreferences](DYLIBS/IntlPreferences.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/JetEngine.framework/Versions/A/JetEngine](DYLIBS/JetEngine.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/JetUI.framework/Versions/A/JetUI](DYLIBS/JetUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/MapsUI.framework/Versions/A/MapsUI](DYLIBS/MapsUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/MediaCoreUI.framework/Versions/A/MediaCoreUI](DYLIBS/MediaCoreUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/Versions/A/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/MessagesSupport.framework/Versions/A/MessagesSupport](DYLIBS/MessagesSupport.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/NewsArticles.framework/Versions/A/NewsArticles](DYLIBS/NewsArticles.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/NewsEngagement.framework/Versions/A/NewsEngagement](DYLIBS/NewsEngagement.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/NewsFeed.framework/Versions/A/NewsFeed](DYLIBS/NewsFeed.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/NewsLiveActivitiesCore.framework/Versions/A/NewsLiveActivitiesCore](DYLIBS/NewsLiveActivitiesCore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/NewsPersonalization.framework/Versions/A/NewsPersonalization](DYLIBS/NewsPersonalization.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/NewsSubscription.framework/Versions/A/NewsSubscription](DYLIBS/NewsSubscription.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/NewsUI.framework/Versions/A/NewsUI](DYLIBS/NewsUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/NewsUI2.framework/Versions/A/NewsUI2](DYLIBS/NewsUI2.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/OnBoardingKit.framework/Versions/A/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PaperKit.framework/Versions/A/PaperKit](DYLIBS/PaperKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PassKitUI.framework/Versions/A/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/Versions/A/PhotosSwiftUICore](DYLIBS/PhotosSwiftUICore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PhotosUICore.framework/Versions/A/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PhotosUIFoundation.framework/Versions/A/PhotosUIFoundation](DYLIBS/PhotosUIFoundation.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PodcastsUI.framework/Versions/A/PodcastsUI](DYLIBS/PodcastsUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PreviewShellKit.framework/Versions/A/PreviewShellKit](DYLIBS/PreviewShellKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PreviewsInjection.framework/Versions/A/PreviewsInjection](DYLIBS/PreviewsInjection.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PreviewsOSSupportUI.framework/Versions/A/PreviewsOSSupportUI](DYLIBS/PreviewsOSSupportUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PromotedContent.framework/Versions/A/PromotedContent](DYLIBS/PromotedContent.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PromotedContentUI.framework/Versions/A/PromotedContentUI](DYLIBS/PromotedContentUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ProximityReaderCore.framework/Versions/A/ProximityReaderCore](DYLIBS/ProximityReaderCore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/RealityIO.framework/Versions/A/RealityIO](DYLIBS/RealityIO.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/SafariShared.framework/Versions/A/SafariShared](DYLIBS/SafariShared.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/SafariSharedUI.framework/Versions/A/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/Versions/A/SafetyMonitorUI](DYLIBS/SafetyMonitorUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/SensitiveContentAnalysisUI.framework/Versions/A/SensitiveContentAnalysisUI](DYLIBS/SensitiveContentAnalysisUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ShareSheet.framework/Versions/A/ShareSheet](DYLIBS/ShareSheet.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ShazamKitUI.framework/Versions/A/ShazamKitUI](DYLIBS/ShazamKitUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/Silex.framework/Versions/A/Silex](DYLIBS/Silex.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/SocialLayer.framework/Versions/A/SocialLayer](DYLIBS/SocialLayer.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/StocksPersonalization.framework/Versions/A/StocksPersonalization](DYLIBS/StocksPersonalization.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/StocksUI.framework/Versions/A/StocksUI](DYLIBS/StocksUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/TeaBreeze.framework/Versions/A/TeaBreeze](DYLIBS/TeaBreeze.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/TeaUI.framework/Versions/A/TeaUI](DYLIBS/TeaUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/TelephonyUI.framework/Versions/A/TelephonyUI](DYLIBS/TelephonyUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/TextInputUI.framework/Versions/A/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/UIAccessibility.framework/Versions/A/UIAccessibility](DYLIBS/UIAccessibility.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/UIKitCore.framework/Versions/A/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/UserNotificationsKit.framework/Versions/A/UserNotificationsKit](DYLIBS/UserNotificationsKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/VFX.framework/Versions/A/VFX](DYLIBS/VFX.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/VisionKitInternal.framework/Versions/A/VisionKitInternal](DYLIBS/VisionKitInternal.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/VisualPairing.framework/Versions/A/VisualPairing](DYLIBS/VisualPairing.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Versions/A/VoiceShortcuts](DYLIBS/VoiceShortcuts.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/WeatherMaps.framework/Versions/A/WeatherMaps](DYLIBS/WeatherMaps.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/WeatherUI.framework/Versions/A/WeatherUI](DYLIBS/WeatherUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/WebCore.framework/Versions/A/Frameworks/libANGLE-shared.dylib](DYLIBS/libANGLE-shared.dylib.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/WebCore.framework/Versions/A/WebCore](DYLIBS/WebCore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/WorkflowEditor.framework/Versions/A/WorkflowEditor](DYLIBS/WorkflowEditor.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/WorkflowKit.framework/Versions/A/WorkflowKit](DYLIBS/WorkflowKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/WorkflowUI.framework/Versions/A/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/WorkflowUICore.framework/Versions/A/WorkflowUICore](DYLIBS/WorkflowUICore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/Versions/A/_JetEngine_SwiftUI](DYLIBS/_JetEngine_SwiftUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/Versions/A/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI.md)
- [/System/iOSSupport/usr/lib/swift/libswiftUIKit.dylib](DYLIBS/libswiftUIKit.dylib.md)
- [/usr/lib/dyld](DYLIBS/dyld.md)
- [/usr/lib/libAppletTranslationLibrary.dylib](DYLIBS/libAppletTranslationLibrary.dylib.md)
- [/usr/lib/libAudioIssueDetector.dylib](DYLIBS/libAudioIssueDetector.dylib.md)
- [/usr/lib/libFDR.dylib](DYLIBS/libFDR.dylib.md)
- [/usr/lib/libKernelCollectionBuilder.dylib](DYLIBS/libKernelCollectionBuilder.dylib.md)
- [/usr/lib/libMemoryResourceException.dylib](DYLIBS/libMemoryResourceException.dylib.md)
- [/usr/lib/libMobileGestalt.dylib](DYLIBS/libMobileGestalt.dylib.md)
- [/usr/lib/libPN548_API.dylib](DYLIBS/libPN548_API.dylib.md)
- [/usr/lib/libSecureMAHelper.dylib](DYLIBS/libSecureMAHelper.dylib.md)
- [/usr/lib/libTelephonyCapabilities.dylib](DYLIBS/libTelephonyCapabilities.dylib.md)
- [/usr/lib/libTelephonyUtilDynamic.dylib](DYLIBS/libTelephonyUtilDynamic.dylib.md)
- [/usr/lib/libUSBCfwflasher.dylib](DYLIBS/libUSBCfwflasher.dylib.md)
- [/usr/lib/libauthinstall.dylib](DYLIBS/libauthinstall.dylib.md)
- [/usr/lib/libcryptex.dylib](DYLIBS/libcryptex.dylib.md)
- [/usr/lib/libcryptex_core.dylib](DYLIBS/libcryptex_core.dylib.md)
- [/usr/lib/libcryptex_interface.dylib](DYLIBS/libcryptex_interface.dylib.md)
- [/usr/lib/libcryptex_trampoline.dylib](DYLIBS/libcryptex_trampoline.dylib.md)
- [/usr/lib/libmdns.dylib](DYLIBS/libmdns.dylib.md)
- [/usr/lib/libnetquality.dylib](DYLIBS/libnetquality.dylib.md)
- [/usr/lib/libnetworkextension.dylib](DYLIBS/libnetworkextension.dylib.md)
- [/usr/lib/libramrod.dylib](DYLIBS/libramrod.dylib.md)
- [/usr/lib/libsandbox.1.dylib](DYLIBS/libsandbox.1.dylib.md)
- [/usr/lib/libspindump.dylib](DYLIBS/libspindump.dylib.md)
- [/usr/lib/libtailspin.dylib](DYLIBS/libtailspin.dylib.md)
- [/usr/lib/libtidy.A.dylib](DYLIBS/libtidy.A.dylib.md)
- [/usr/lib/swift/libswiftAccelerate.dylib](DYLIBS/libswiftAccelerate.dylib.md)
- [/usr/lib/swift/libswiftCoreAudio.dylib](DYLIBS/libswiftCoreAudio.dylib.md)
- [/usr/lib/swift/libswiftCoreMedia.dylib](DYLIBS/libswiftCoreMedia.dylib.md)
- [/usr/lib/swift/libswiftNaturalLanguage.dylib](DYLIBS/libswiftNaturalLanguage.dylib.md)
- [/usr/lib/swift/libswiftSpatial.dylib](DYLIBS/libswiftSpatial.dylib.md)
- [/usr/lib/swift/libswiftSystem.dylib](DYLIBS/libswiftSystem.dylib.md)
- [/usr/lib/swift/libswiftXPC.dylib](DYLIBS/libswiftXPC.dylib.md)
- [/usr/lib/system/libdyld.dylib](DYLIBS/libdyld.dylib.md)
- [/usr/lib/system/liblaunch.dylib](DYLIBS/liblaunch.dylib.md)
- [/usr/lib/system/libsystem_dnssd.dylib](DYLIBS/libsystem_dnssd.dylib.md)
- [/usr/lib/system/libsystem_eligibility.dylib](DYLIBS/libsystem_eligibility.dylib.md)
- [/usr/lib/system/libsystem_kernel.dylib](DYLIBS/libsystem_kernel.dylib.md)
- [/usr/lib/system/libsystem_malloc.dylib](DYLIBS/libsystem_malloc.dylib.md)
- [/usr/lib/system/libsystem_sanitizers.dylib](DYLIBS/libsystem_sanitizers.dylib.md)
- [/usr/lib/system/libsystem_trace.dylib](DYLIBS/libsystem_trace.dylib.md)
- [/usr/lib/usd/libusd_ms.dylib](DYLIBS/libusd_ms.dylib.md)

</details>

### Feature Flags

#### 🆕 NEW (2)

<details>
  <summary><i>View New</i></summary>

#### MemoryTelemetry.plist

>  `Domain/MemoryTelemetry.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict/>
</plist>

```
#### MobileAsset.plist

>  `Domain/MobileAsset.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>LiveStorageExclaveNonce</key>
	<dict>
		<key>DevelopmentPhase</key>
		<string>FeatureComplete</string>
	</dict>
	<key>com_apple_mobileassetd_conclave</key>
	<dict>
		<key>DevelopmentPhase</key>
		<string>FeatureComplete</string>
	</dict>
</dict>
</plist>

```

</details>

#### ⬆️ Updated (15)

<details>
  <summary><i>View Updated</i></summary>

#### AppleIDSetup.plist

>  `Domain/AppleIDSetup.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>AgeAttestationSettings</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>ChildSetupSignIn</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### AudioSession.plist

>  `Domain/AudioSession.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>EnableSecureSessionOnMacOS</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>OffloadActivationOffACQ</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### CompanionServices.plist

>  `Domain/CompanionServices.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>AdditionalSiriDialogue</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 	<key>AppleMusic</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### Home.plist

>  `Domain/Home.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>RapportoverBLE</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>ResidentSelection</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### MediaExperience.plist

>  `Domain/MediaExperience.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>StravinskyOrchestration</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>SystemRemoteDisplay</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### MediaRemote.plist

>  `Domain/MediaRemote.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
-	<key>rapport_remote_control_transport</key>
-	<dict>
-		<key>Enabled</key>
-		<true/>
-	</dict>
 	<key>session_based_lock_screen_platter</key>
 	<dict>
 		<key>Enabled</key>

```

#### OmniSearch.plist

>  `Domain/OmniSearch.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>preExtractedIDs</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>reflectionToken</key>
 	<dict>
 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
-	<key>urgentPCCPrewarm</key>
+	<key>searchInAppRows</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>shortCircuitMusicSearch</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>shortCircuitPhotoSearch</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>showInternalErrorInfo</key>
 	<dict>
 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>

```

#### Oneness.plist

>  `Domain/Oneness.plist`

```diff

 		<key>DisclosureRequired</key>
 		<string>8f6f8e85-8d9d-8330-8c15-a603765b90f3</string>
 	</dict>
+	<key>RemoteTextInput</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>Shell</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### PrivateCloudCompute.plist

>  `Domain/PrivateCloudCompute.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>enforceEnvironment</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
-	<key>productionEnvironmentAvailable</key>
+	<key>trustedProxyProtocol</key>
 	<dict>
 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>

```

#### ScreenTime.plist

>  `Domain/ScreenTime.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>passcode_activity</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 </dict>
 </plist>
 

```

#### Spotlight.plist

>  `Domain/Spotlight.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
-	<key>SearchToolAllBundles</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
-	<key>SearchToolCleanSlateDenseRetrieval</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 	<key>SearchToolLLMQueryUnderstanding</key>
 	<dict>
 		<key>DevelopmentPhase</key>

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
-	<key>SearchToolRanking</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 	<key>SearchToolRetrievalSparseScoringV2</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### Summarization.plist

>  `Domain/Summarization.plist`

```diff

 <?xml version="1.0" encoding="UTF-8"?>
 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
-<dict/>
+<dict>
+	<key>FactualConsistencyClassifier</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+</dict>
 </plist>
 

```

#### TV.plist

>  `Domain/TV.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>interstitials</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>subtitlesOnLanguageMismatch</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### TelephonyUtilities.plist

>  `Domain/TelephonyUtilities.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>CallEndSpamUIEnhancement</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>CallManagerEnabled</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### GlobalDisclosures.plist

>  `GlobalDisclosures.plist`

```diff

 		<key>Disclosed</key>
 		<true/>
 	</dict>
-	<key>1b3196a9-6a20-4559-60fd-bb3743219ab3</key>
-	<dict>
-		<key>Disclosed</key>
-		<true/>
-	</dict>
 	<key>2298f8e4-f510-4776-b2c1-a85ea314b1f8</key>
 	<dict>
 		<key>Disclosed</key>

```


</details>

### Files

#### 🆕 New

##### IPSW (6)

- `Firmware/022-19067-017.dmg.aea.x86.trustcache`
- `Firmware/043-10808-017.dmg.x86.trustcache`
- `Firmware/043-10814-017.dmg.x86.trustcache`
- `Firmware/043-10843-015.dmg.aea.x86.mtree`
- `Firmware/043-10843-015.dmg.aea.x86.root_hash`
- `Firmware/043-10843-015.dmg.aea.x86.trustcache`

##### filesystem (686)

<details>
  <summary><i>View Files</i></summary>

- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/ar.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/da.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/de.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/en-au.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/en-ca.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/en-gb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/en.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/es.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/fi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/fr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/he.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/hi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/it.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/ja.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/ko.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/ms.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/nb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/nl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/pt.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/ru.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/sv.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/th.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/tr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/vi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/yue.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/zh-cn.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/zh-hk.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/zh-tw.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/CAMRootFlowPlugin.bundle/Contents/Resources/Templates/dialog/UserSession.catfamily/ActiveSessionUserNotRecognized.cat/en-za.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/DialogAssetDelivery.plist`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/ar.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/da.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/de-ch.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/de.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/en-au.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/en-ca.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/en-gb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/en.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/es-cl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/es.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/fi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/fr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/he.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/it.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/ja.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/ko.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/ms.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/nb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/nl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/pt.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/ru.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/sv.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/tr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/vi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/yue.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/zh-cn.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/zh-hk.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/CommonErrors.catfamily/GenericError.cat/zh-tw.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/IFFlow.catfamily/UserLocationUnknown.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/IFFlow.catfamily/UserLocationUnknown.cat/en.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/ar.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/da.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/de.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/en-au.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/en-ca.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/en-gb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/en.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/es-us.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/es.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/fi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/fr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/he.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/it.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/ja.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/ko.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/ms.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/nb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/nl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/pt.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/ru.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/sv.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/th.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/tr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/vi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/yue.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/zh-cn.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/zh-hk.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/zh-tw.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/ar.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/da.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/de.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/en-au.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/en-ca.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/en-gb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/en.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/es.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/fi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/fr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/he.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/it.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/ja.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/ko.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/ms.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/nb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/nl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/pt.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/ru.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/sv.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/th.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/tr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/vi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/yue.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/zh-cn.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/zh-hk.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/zh-tw.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/ar.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/da.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/de-ch.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/de.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/en-au.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/en-ca.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/en-gb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/en-za.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/en.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/es-cl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/es.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/fi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/fr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/he.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/it.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/ja.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/ko.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/ms.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/nb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/nl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/pt.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/ru.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/sv.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/th.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/tr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/vi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/yue.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/zh-cn.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/zh-hk.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Contents/Resources/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/zh-tw.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/_params.cat.xml`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/ar.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/da.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/de.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/en-au.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/en-ca.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/en.cat.xml`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/es.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/fr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/it.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/ja.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/ko.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/ms.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/nb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/nl-be.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/nl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/pt.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/ru.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/sv.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/tr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/vi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/zh-cn.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/zh-hk.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/zh-tw.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/_params.cat.xml`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/ar.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/da.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/de.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/en-au.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/en-ca.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/en-gb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/en.cat.xml`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/es.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/fr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/he.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/it.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/ja.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/ko.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/ms.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/nb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/nl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/pt.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/sv.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/tr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/vi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/zh-cn.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/zh-hk.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/zh-tw.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/_params.cat.xml`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/ar.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/da.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/de.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/en-au.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/en-ca.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/en-gb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/en.cat.xml`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/es.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/fr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/he.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/it.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/ja.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/ko.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/ms.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/nb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/nl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/pt.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/sv.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/tr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/vi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/zh-cn.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/zh-hk.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/Resources/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/zh-tw.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/SearchCallHistory.catfamily/IntentHandledResponse.cat/en-ie.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/SearchCallHistory.catfamily/IntentHandledResponse.cat/en-sg.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/SearchCallHistory.catfamily/IntentHandledResponse.cat/en-za.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/SearchCallHistory.catfamily/IntentHandledResponseMissedCall.cat/en-ie.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/SearchCallHistory.catfamily/IntentHandledResponseMissedCall.cat/en-sg.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/SearchCallHistory.catfamily/IntentHandledResponseMissedCall.cat/en-za.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/StartCall.catfamily/IntentConfirmationEmergency.cat/en-ie.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/StartCall.catfamily/IntentConfirmationEmergency.cat/en-in.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/StartCall.catfamily/IntentConfirmationEmergency.cat/en-sg.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/StartCall.catfamily/IntentConfirmationEmergency.cat/en-za.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/StartCall.catfamily/IntentConfirmationEmergency.cat/es-cl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/UnsupportedFlow.catfamily/StartCallEmergency.cat/en-ie.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/UnsupportedFlow.catfamily/StartCallEmergency.cat/en-in.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/UnsupportedFlow.catfamily/StartCallEmergency.cat/en-sg.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/UnsupportedFlow.catfamily/StartCallEmergency.cat/en-za.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/TimerFlowDelegatePlugin.bundle/Contents/Resources/Templates/dialog/createTimer.catfamily/errorWithCode.cat/de-ch.cat.bin`
- `/System/Library/CoreServices/Apple Diagnostics.app/Contents/Info.plist`
- `/System/Library/CoreServices/Apple Diagnostics.app/Contents/MacOS/Apple Diagnostics`
- `/System/Library/CoreServices/Apple Diagnostics.app/Contents/PkgInfo`
- `/System/Library/CoreServices/Apple Diagnostics.app/Contents/Resources/AppIcon.icns`
- `/System/Library/CoreServices/Apple Diagnostics.app/Contents/Resources/Assets.car`
- `/System/Library/CoreServices/Apple Diagnostics.app/Contents/Resources/Base.lproj/MainMenu.nib`
- `/System/Library/CoreServices/Apple Diagnostics.app/Contents/Resources/InfoPlist.loctable`
- `/System/Library/CoreServices/Apple Diagnostics.app/Contents/Resources/Localizable.loctable`
- `/System/Library/CoreServices/Apple Diagnostics.app/Contents/_CodeSignature/CodeResources`
- `/System/Library/CoreServices/Apple Diagnostics.app/Contents/version.plist`
- `/System/Library/CoreServices/diagnosticservicesd`
- `/System/Library/ExtensionKit/Extensions/MessageCenterApplicationServiceDiscoveryExtension.appex/Contents/Info.plist`
- `/System/Library/ExtensionKit/Extensions/MessageCenterApplicationServiceDiscoveryExtension.appex/Contents/MacOS/MessageCenterApplicationServiceDiscoveryExtension`
- `/System/Library/ExtensionKit/Extensions/MessageCenterApplicationServiceDiscoveryExtension.appex/Contents/_CodeSignature/CodeResources`
- `/System/Library/ExtensionKit/Extensions/MessageCenterApplicationServiceDiscoveryExtension.appex/Contents/version.plist`
- `/System/Library/ExtensionKit/Extensions/PRIMLCKPreemptivePing.appex/Contents/Info.plist`
- `/System/Library/ExtensionKit/Extensions/PRIMLCKPreemptivePing.appex/Contents/MacOS/PRIMLCKPreemptivePing`
- `/System/Library/ExtensionKit/Extensions/PRIMLCKPreemptivePing.appex/Contents/_CodeSignature/CodeResources`
- `/System/Library/ExtensionKit/Extensions/PRIMLCKPreemptivePing.appex/Contents/version.plist`
- `/System/Library/ExtensionKit/Extensions/ZeoliteEvalExtension.appex/Contents/Info.plist`
- `/System/Library/ExtensionKit/Extensions/ZeoliteEvalExtension.appex/Contents/MacOS/ZeoliteEvalExtension`
- `/System/Library/ExtensionKit/Extensions/ZeoliteEvalExtension.appex/Contents/_CodeSignature/CodeResources`
- `/System/Library/ExtensionKit/Extensions/ZeoliteEvalExtension.appex/Contents/version.plist`
- `/System/Library/FeatureFlags/Domain/MemoryTelemetry.plist`
- `/System/Library/FeatureFlags/Domain/MobileAsset.plist`
- `/System/Library/LaunchAgents/com.apple.diagnosticspushd.plist`
- `/System/Library/LaunchDaemons/com.apple.diagnosticservicesd.plist`
- `/System/Library/LaunchDaemons/com.apple.memoryanalyticsd.plist`
- `/System/Library/MLHost/StaticTasks/com.apple.priml.PRIMLCKPreemptivePing.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.FaceTime.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.IDS.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.Messages.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.MessagesEvents.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.Registration.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.StatusKit.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.Transport.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.apsd.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.calldirectory.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.callkit.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.callservicesd.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.conversationkit.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.facetime.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.incallservice.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.mobilephone.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.telephonyui.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.telephonyutilities.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.findmy.framework.FindMyServerInteraction.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.memoryanalyticsd.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.podcasts.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.voicemail.plist`
- `/System/Library/PrivateFrameworks/CodableSwiftUICore.framework/Versions/A`
- `/System/Library/PrivateFrameworks/CodableSwiftUICore.framework/Versions/A/Resources`
- `/System/Library/PrivateFrameworks/CodableSwiftUICore.framework/Versions/A/Resources/Info.plist`
- `/System/Library/PrivateFrameworks/CodableSwiftUICore.framework/Versions/A/Resources/version.plist`
- `/System/Library/PrivateFrameworks/CodableSwiftUICore.framework/Versions/A/_CodeSignature`
- `/System/Library/PrivateFrameworks/CodableSwiftUICore.framework/Versions/A/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPlugin.appex/Contents/Resources/FedStatsCohortValueAllowList.plist`
- `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPlugin.appex/Contents/Resources/FedStatsCohortValueBlockList.plist`
- `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginClassB.appex/Contents/Resources/FedStatsCohortValueAllowList.plist`
- `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginClassB.appex/Contents/Resources/FedStatsCohortValueBlockList.plist`
- `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginNonDnU.appex/Contents/Resources/FedStatsCohortValueAllowList.plist`
- `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginNonDnU.appex/Contents/Resources/FedStatsCohortValueBlockList.plist`
- `/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/Versions/A/Resources/FedStatsCohortValueAllowList.plist`
- `/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/Versions/A/Resources/FedStatsCohortValueBlockList.plist`
- `/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/Versions/A/Resources/FedStatsPluginCoreConsentConfiguration.plist`
- `/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/Versions/A/Resources/FedStatsPluginPrunableStreams.plist`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/1608RXJ7CAICP`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/1608RXJ7CAICP/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/1X6RPS1E589UO`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/1X6RPS1E589UO/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/1XD5UFKJNG8K8`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/1XD5UFKJNG8K8/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/2FH6OVNN7CUU0`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/2FH6OVNN7CUU0/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/2G15UZZ6RRUR1`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/2G15UZZ6RRUR1/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/2OAA7FD4C156R`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/2OAA7FD4C156R/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/34U0VVJ18ZAW0`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/34U0VVJ18ZAW0/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/3H7B9J7Q0HHC2`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/3H7B9J7Q0HHC2/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/3U2D281TLBOZN`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/3U2D281TLBOZN/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/3UL2FGQD9MNT6`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/3UL2FGQD9MNT6/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/LG28XMTP5CPS`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/LG28XMTP5CPS/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Versions/A/Resources/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Versions/A/Resources/Templates/dialog/HomeAutomation.catfamily/BlockMulticardinalRequests.cat/es-cl.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Versions/A/Resources/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Versions/A/Resources/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Versions/A/Resources/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Versions/A/Resources/Templates/schema/homeAutomation.AbstractMeasurements.catschema.bin`
- `/System/Library/PrivateFrameworks/InputAccessoriesSettings.framework/Versions/A/Resources/sl.lproj`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Metadata.generativefunctions/-Ct5aF7INvkwygqcxVy0urnCJVg.`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Metadata.generativefunctions/8wlV3JjCjJ6-OBHCd-Ffo-aCUo0.`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Metadata.generativefunctions/OWs1BM2VPV56LUF6803Ztuz8sO0.`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/Versions/A/Resources/ToolBoxAllowList.plist`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/Versions/A/Resources/ToolPromptOverride.json`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/Versions/A/Resources/ToolRetrievalContextAllowList.plist`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/Versions/A/Resources/spiece_mmap.model`
- `/System/Library/PrivateFrameworks/NDOAPI.framework/Versions/A`
- `/System/Library/PrivateFrameworks/NDOAPI.framework/Versions/A/Resources`
- `/System/Library/PrivateFrameworks/NDOAPI.framework/Versions/A/Resources/Info.plist`
- `/System/Library/PrivateFrameworks/NDOAPI.framework/Versions/A/Resources/version.plist`
- `/System/Library/PrivateFrameworks/NDOAPI.framework/Versions/A/_CodeSignature`
- `/System/Library/PrivateFrameworks/NDOAPI.framework/Versions/A/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/Assets.car`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/Info.plist`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/Localizable.loctable`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/ar.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/ca.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/cs.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/da.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/de.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/el.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/en.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/en_AU.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/en_GB.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/es.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/es_419.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/fi.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/fr.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/fr_CA.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/he.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/hi.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/hr.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/hu.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/id.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/it.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/ja.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/ko.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/ms.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/nl.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/no.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/pl.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/pt_BR.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/pt_PT.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/ro.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/ru.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/sk.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/sl.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/sv.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/th.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/tr.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/uk.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/version.plist`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/vi.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/zh_CN.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/zh_HK.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/Resources/zh_TW.lproj`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/_CodeSignature`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Versions/A/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/OmniSearch.framework/Versions/A/Resources/NamespaceDescriptor.SEARCH_TOOL_ANSWER_SYNTHESIS.plist`
- `/System/Library/PrivateFrameworks/OmniSearch.framework/Versions/A/Resources/default_factors_SEARCH_TOOL_ANSWER_SYNTHESIS.pb`
- `/System/Library/PrivateFrameworks/PodcastsFoundation.framework/Versions/A/Resources/com.apple.podcasts.plist`
- `/System/Library/PrivateFrameworks/SUDocAssetCore.framework/Versions/A`
- `/System/Library/PrivateFrameworks/SUDocAssetCore.framework/Versions/A/Resources`
- `/System/Library/PrivateFrameworks/SUDocAssetCore.framework/Versions/A/Resources/Info.plist`
- `/System/Library/PrivateFrameworks/SUDocAssetCore.framework/Versions/A/Resources/version.plist`
- `/System/Library/PrivateFrameworks/SUDocAssetCore.framework/Versions/A/_CodeSignature`
- `/System/Library/PrivateFrameworks/SUDocAssetCore.framework/Versions/A/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/ScreenTimeServiceUI.framework/Versions/A/XPCServices/ScreenTimeViewService.xpc/Contents/Resources/InfoPlist.loctable`
- `/System/Library/PrivateFrameworks/SensorAccess.framework/Versions/A`
- `/System/Library/PrivateFrameworks/SensorAccess.framework/Versions/A/Resources`
- `/System/Library/PrivateFrameworks/SensorAccess.framework/Versions/A/Resources/Info.plist`
- `/System/Library/PrivateFrameworks/SensorAccess.framework/Versions/A/Resources/version.plist`
- `/System/Library/PrivateFrameworks/SensorAccess.framework/Versions/A/_CodeSignature`
- `/System/Library/PrivateFrameworks/SensorAccess.framework/Versions/A/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/SiriContactsIntents.framework/Versions/A/Resources/Templates/dialog/GetContactAttribute.catfamily/IntentHandledShowAddress.cat/vi_VN_u_sd_vnct.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/AlreadyActive.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/AlreadyActive.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/AnswerWhoAmI.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/AnswerWhoAmI.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/CannotSwitchForSingleProfile.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/CannotSwitchForSingleProfile.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/ConfirmRemotePlay.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/ConfirmRemotePlay.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/ConfirmationCancelled.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/ConfirmationCancelled.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/EstablishMultiUser.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/EstablishMultiUser.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/EstablishSingleUser.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/EstablishSingleUser.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/HomeUserAccountDoesNotExist.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/HomeUserAccountDoesNotExist.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/Identify.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/Identify.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/MissingMeCardData.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/MissingMeCardData.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/MultiUserUnavailable.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/MultiUserUnavailable.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/PartialMeCardData.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/PartialMeCardData.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/ProfileSelectPrompt.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/ProfileSelectPrompt.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/RemoteDeviceNotFound.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/RemoteDeviceNotFound.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/RemotePlayDisambiguateResults.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/RemotePlayDisambiguateResults.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/RemotePlayDisambiguateResultsDisplay.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/RemotePlayDisambiguateResultsDisplay.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/Unrecognized.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/Unrecognized.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/UnrecognizedAmbiguous.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/UnrecognizedAmbiguous.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/UnrecognizedOfferVoiceId.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/UnrecognizedOfferVoiceId.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/Unsupported.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/Unsupported.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/UserUnknown.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/UserUnknown.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/VoiceNotRecognizedButOneAccount.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/VoiceNotRecognizedButOneAccount.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/HandoffErrors.catfamily/CompanionLanguageMismatch.cat/es-us.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnrecognizedSpeaker.cat/de-ch.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/es-cl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/SiriLocalization.framework/Versions/A`
- `/System/Library/PrivateFrameworks/SiriLocalization.framework/Versions/A/Resources`
- `/System/Library/PrivateFrameworks/SiriLocalization.framework/Versions/A/Resources/Info.plist`
- `/System/Library/PrivateFrameworks/SiriLocalization.framework/Versions/A/Resources/version.plist`
- `/System/Library/PrivateFrameworks/SiriLocalization.framework/Versions/A/_CodeSignature`
- `/System/Library/PrivateFrameworks/SiriLocalization.framework/Versions/A/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/Versions/A/Resources/Templates/dialog/SearchForMessages.catfamily/OfferSendMessageIntent.cat/en-za.cat.bin`
- `/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/Versions/A/Resources/Templates/dialog/SearchForMessages.catfamily/OfferSendMessageIntent.cat/vi_VN_u_sd_vnct.cat.bin`
- `/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/Versions/A/Resources/Templates/dialog/SearchForMessages.catfamily/ReadSpokenGenericCountableComponent.cat/it-ch.cat.bin`
- `/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/Versions/A/Resources/Templates/dialog/SendMessage.catfamily/FailureCantMessage.cat/nl-be.cat.bin`
- `/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/Versions/A/Resources/Templates/dialog/SendMessage.catfamily/HoldSend.cat/en-in.cat.bin`
- `/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/Versions/A/Resources/Templates/dialog/SendMessage.catfamily/HoldSend.cat/es-us.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/de-ch.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/es-cl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/nl-be.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/Localizable.loctable`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/ar.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/ca.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/cs.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/da.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/de.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/el.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/en.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/en_AU.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/en_GB.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/es.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/es_419.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/fi.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/fr.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/fr_CA.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/he.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/hi.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/hr.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/hu.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/id.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/it.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/ja.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/ko.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/ms.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/nl.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/no.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/pl.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/pt_BR.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/pt_PT.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/ro.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/ru.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/sk.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/sl.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/sv.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/th.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/tr.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/uk.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/vi.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/zh_CN.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/zh_HK.lproj`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/Resources/zh_TW.lproj`
- `/System/Library/SESStorage/Asset/DCK/XPEV.plist`
- `/System/Library/Sandbox/Profiles/com.apple.diagnosticservicesd.sb`
- `/System/Library/Security/Certificates.bundle/Contents/Resources/Anchors/B296DC3BCF451217D7AD4F84FB8EE25CC92FC659CAFA0EB4A8B5B4DB3D0215C2.cer`
- `/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/Contents/Resources/Templates/dialog/AudioSuggestions.catfamily/PlayPlaylist.cat/fr-be.cat.bin`
- `/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/Contents/Resources/Templates/dialog/AudioSuggestions.catfamily/PlayPlaylist.cat/fr-ch.cat.bin`
- `/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/Contents/Resources/Templates/dialog/AudioSuggestions.catfamily/PlayPlaylist.cat/vi_VN_u_sd_vnct.cat.bin`
- `/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorBundlore`
- `/System/Library/Templates/Data/Library/Developer/CommandLineTools/.beta`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.AIRPLAY.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.BATTERYINTELLIGENCE_BATTERY_ANALYSIS.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.COREOS_PERFPOWER_IDLE_REAPER.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.COREOS_XNU_LATENCY_GUARDS.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.ENHANCED_DEBUGGING_LIBSANITIZERS.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.MAPS_SRP_AUTOCOMPLETE.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.MEDIAEXPERIENCE.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.POWER_EXCEPTIONS_MITIGATIONS.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.RULES_ENGINE_ENABLED_MIGRATION.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.SEARCH_TOOL_ANSWER_SYNTHESIS.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.SIML_ADM_PERSONALIZATION.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.SMS_FILTER_FELIS.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.SMS_FILTER_KYOTO.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.TELEPHONY_WIFI_CELLULAR_HANDOVER_POLICY.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.WEBKIT_LIBPAS_PGM.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.WEBKIT_PROBABILISTIC_GUARD_MALLOC.plist`
- `/System/Library/UnifiedAssetFramework/AssetSets/com.apple.MobileAsset.CN.Guardrail.plist`
- `/System/Library/UnifiedAssetFramework/UsageAliases/com.apple.Siri.Planner.migration.18.4.plist`
- `/System/Library/UnifiedAssetFramework/UsageAliases/safety.chinaGuardrail.migration.18.4.plist`
- `/System/Library/UnifiedAssetFramework/UsageAliases/safety.chinaGuardrail.plist`
- `/System/Library/UserNotifications/Bundles/com.apple.NewDeviceOutreach.UserNotificationsBundle.bundle/Contents/Info.plist`
- `/System/Library/UserNotifications/Bundles/com.apple.NewDeviceOutreach.UserNotificationsBundle.bundle/Contents/Resources/Assets.car`
- `/System/Library/UserNotifications/Bundles/com.apple.NewDeviceOutreach.UserNotificationsBundle.bundle/Contents/Resources/InfoPlist.strings`
- `/System/Library/UserNotifications/Bundles/com.apple.NewDeviceOutreach.UserNotificationsBundle.bundle/Contents/_CodeSignature/CodeDirectory`
- `/System/Library/UserNotifications/Bundles/com.apple.NewDeviceOutreach.UserNotificationsBundle.bundle/Contents/_CodeSignature/CodeRequirements`
- `/System/Library/UserNotifications/Bundles/com.apple.NewDeviceOutreach.UserNotificationsBundle.bundle/Contents/_CodeSignature/CodeResources`
- `/System/Library/UserNotifications/Bundles/com.apple.NewDeviceOutreach.UserNotificationsBundle.bundle/Contents/_CodeSignature/CodeSignature`
- `/System/Library/UserNotifications/Bundles/com.apple.NewDeviceOutreach.UserNotificationsBundle.bundle/Contents/version.plist`
- `/System/iOSSupport/System/Library/PrivateFrameworks/FindMyUICore.framework/Versions/A/Resources/TNLLocalized.loctable`
- `/usr/libexec/diagnosticspushd`
- `/usr/libexec/memoryanalyticsd`
- `/usr/share/man/man8/diagnosticservicesd.8`
- `/usr/standalone/firmware/t303/bfh_ofw.t303.ofw.toshiba_qlc_3d_g8_4p_1024gb.bin`

</details>

#### ❌ Removed

##### IPSW (6)

- `Firmware/022-16698-347.dmg.aea.x86.trustcache`
- `Firmware/090-49019-359.dmg.x86.trustcache`
- `Firmware/090-49050-328.dmg.aea.x86.mtree`
- `Firmware/090-49050-328.dmg.aea.x86.root_hash`
- `Firmware/090-49050-328.dmg.aea.x86.trustcache`
- `Firmware/090-49128-358.dmg.x86.trustcache`

##### filesystem (985)

<details>
  <summary><i>View Files</i></summary>

- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Contents/Resources/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Contents/Resources/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/ar.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Contents/Resources/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/de.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Contents/Resources/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/en-au.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Contents/Resources/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/en-gb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Contents/Resources/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/en.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Contents/Resources/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/it-ch.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Contents/Resources/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/ja.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Contents/Resources/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/nl-be.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Contents/Resources/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/tr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Contents/Resources/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/yue.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Contents/Resources/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/zh-hk.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Contents/Resources/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/zh-tw.cat.bin`
- `/System/Library/CoreServices/BluetoothUIService.app/Contents/Resources/Banner-PID-8218-Seed/Banner-PID-8218-6-Seed.png`
- `/System/Library/CoreServices/BluetoothUIService.app/Contents/Resources/Banner-PID-8218-Seed/Banner-PID-8218-7-Seed.png`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/ar.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/ca.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/cs.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/da.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/de.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/el.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/es.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/fi.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/fr.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/he.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/hr.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/hu.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/id.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/it.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/ja.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/ko.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/ms.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/nl.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/no.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/pl.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/pt.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/pt_PT.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/ro.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/ru.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/sk.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/sv.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/th.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/tr.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/uk.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/vi.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/zh_CN.lproj/License.rtf`
- `/System/Library/CoreServices/Install Command Line Developer Tools.app/Contents/Resources/zh_TW.lproj/License.rtf`
- `/System/Library/CoreServices/Setup Assistant.app/Contents/Resources/bg.lproj/OSXSoftwareLicense.html`
- `/System/Library/CoreServices/Setup Assistant.app/Contents/Resources/bg.lproj/OSXSoftwareLicense.rtf`
- `/System/Library/CoreServices/Setup Assistant.app/Contents/Resources/kk.lproj/OSXSoftwareLicense.html`
- `/System/Library/CoreServices/Setup Assistant.app/Contents/Resources/kk.lproj/OSXSoftwareLicense.rtf`
- `/System/Library/ExtensionKit/Extensions/IEMetricsWorker.appex/Contents/Info.plist`
- `/System/Library/ExtensionKit/Extensions/IEMetricsWorker.appex/Contents/MacOS/IEMetricsWorker`
- `/System/Library/ExtensionKit/Extensions/IEMetricsWorker.appex/Contents/_CodeSignature/CodeResources`
- `/System/Library/ExtensionKit/Extensions/IEMetricsWorker.appex/Contents/version.plist`
- `/System/Library/ExtensionKit/Extensions/ZeoliteExtension.appex/Contents/Info.plist`
- `/System/Library/ExtensionKit/Extensions/ZeoliteExtension.appex/Contents/MacOS/ZeoliteExtension`
- `/System/Library/ExtensionKit/Extensions/ZeoliteExtension.appex/Contents/_CodeSignature/CodeResources`
- `/System/Library/ExtensionKit/Extensions/ZeoliteExtension.appex/Contents/version.plist`
- `/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/Versions/A/Resources/AssetPaths-Seed.plist`
- `/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/Versions/A/Resources/B453-4-Moon.icns`
- `/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/Versions/A/Resources/B453-5-Dune.icns`
- `/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/Versions/A/Resources/B453-6-Earth.icns`
- `/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/Versions/A/Resources/B487-6-Mushroom.icns`
- `/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/Versions/A/Resources/B487-7-Graphite.icns`
- `/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/Versions/A/Resources/B607-3-CosmicSilver.icns`
- `/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/Versions/A/Resources/B607-4-CosmicPink.icns`
- `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/Versions/A/Resources/BCM4388C2_MangosteenA_154_FINALv1_OS_STATS_20240625.ptb`
- `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/Versions/A/Resources/BCM4388C2_MangosteenA_154_FINALv1_OS_USI_20240625.ptb`
- `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/Versions/A/Resources/BCM4399C2_Audreyii_154_FINALv1_OS_STATS_20240727.ptb`
- `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/Versions/A/Resources/BCM4399C2_Audreyii_154_FINALv1_OS_USI_20240727.ptb`
- `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/Versions/A/Resources/BCM4399C2_Cephalotus_154_FINALv1_OS_STATS_20240708.ptb`
- `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/Versions/A/Resources/BCM4399C2_Cephalotus_154_FINALv1_OS_USI_20240708.ptb`
- `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/Versions/A/Resources/BCM4399C2_Nepenthes_154_FINALv1_OS_STATS_20240726.ptb`
- `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/Versions/A/Resources/BCM4399C2_Nepenthes_154_FINALv1_OS_USI_20240726.ptb`
- `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/Versions/A/Resources/BCM4399C2_Sundew_154_FINALv1_OS_STATS_20240704.ptb`
- `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/Versions/A/Resources/BCM4399C2_Sundew_154_FINALv1_OS_USI_20240704.ptb`
- `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginClassB.appex/Contents/Resources/assets_1546/recipe.json`
- `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginClassB.appex/Contents/Resources/default_factors_1546.pb`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/1B5UFAMA91W15`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/1B5UFAMA91W15/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/1N09X1DVWRHMC`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/1N09X1DVWRHMC/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/2BYVNAQRA1AT5`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/2BYVNAQRA1AT5/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/2MVZ1CSFZEOBU`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/2MVZ1CSFZEOBU/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/2N3HF6P44BTFB`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/2N3HF6P44BTFB/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/2XG14TQY5V6FH`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/2XG14TQY5V6FH/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/36CEXTF0IB7W0`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/36CEXTF0IB7W0/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/3B9VBUV6L861C`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/3B9VBUV6L861C/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/3EO6E4F0HE2ZU`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/3EO6E4F0HE2ZU/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/3F4NVGLUL1GVG`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/3F4NVGLUL1GVG/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/3GIMOQYB0CUB6`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/3GIMOQYB0CUB6/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Metadata.generativefunctions/DcOJ-FWQMD-aA7pq_XOiZhJ8IWY.`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Metadata.generativefunctions/HlrafOOIrVhnS2vlnrbNsA3Effw.`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Metadata.generativefunctions/UQRDb-9XZO8ErFlJAoiZJiGfvRM.`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/actionConfirmation.cat`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/actionConfirmation.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/actionConfirmation.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/actionFailure.cat`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/actionFailure.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/actionFailure.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/actionRequirement.cat`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/actionRequirement.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/actionRequirement.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/actionSuccess.cat`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/actionSuccess.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/actionSuccess.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/actionUndo.cat`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/actionUndo.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/actionUndo.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/conjunction.cat`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/conjunction.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/conjunction.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/continueOnDevice.cat`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/continueOnDevice.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/continueOnDevice.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/error.cat`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/error.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/error.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/labels.cat`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/labels.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/labels.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/parameterConfirmation.cat`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/parameterConfirmation.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/parameterConfirmation.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/parameterDisambiguation.cat`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/parameterDisambiguation.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/parameterDisambiguation.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/parameterNeedsValue.cat`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/parameterNeedsValue.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/parameterNeedsValue.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/parameterNotAllowed.cat`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/parameterNotAllowed.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/dialog/responseGeneration.catfamily/parameterNotAllowed.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/schema`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/schema/responseGeneration.ResponseDialog.catschema.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/Resources/Templates/schema/responseGeneration.Value.catschema.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/Versions/A/Resources/ToolBoxAllowList-CrystalE.plist`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/Versions/A/Resources/spiece.model`
- `/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/Versions/A/Resources/Assets.car`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/AlreadyActive.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/AlreadyActive.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/AnswerWhoAmI.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/AnswerWhoAmI.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/CannotSwitchForSingleProfile.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/CannotSwitchForSingleProfile.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/ConfirmRemotePlay.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/ConfirmRemotePlay.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/ConfirmationCancelled.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/ConfirmationCancelled.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/EstablishMultiUser.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/EstablishMultiUser.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/EstablishSingleUser.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/EstablishSingleUser.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/HomeUserAccountDoesNotExist.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/HomeUserAccountDoesNotExist.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/Identify.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/Identify.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/MissingMeCardData.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/MissingMeCardData.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/MultiUserUnavailable.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/MultiUserUnavailable.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/PartialMeCardData.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/PartialMeCardData.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/ProfileSelectPrompt.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/ProfileSelectPrompt.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/RemoteDeviceNotFound.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/RemoteDeviceNotFound.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/RemotePlayDisambiguateResults.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/RemotePlayDisambiguateResults.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/RemotePlayDisambiguateResultsDisplay.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/RemotePlayDisambiguateResultsDisplay.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/Unrecognized.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/Unrecognized.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/UnrecognizedAmbiguous.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/UnrecognizedAmbiguous.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/UnrecognizedOfferVoiceId.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/UnrecognizedOfferVoiceId.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/Unsupported.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/Unsupported.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/UserUnknown.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/UserUnknown.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/VoiceNotRecognizedButOneAccount.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Versions/A/Resources/Templates/dialog/Identity.catfamily/VoiceNotRecognizedButOneAccount.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/Resources/Templates/dialog/HandoffErrors.catfamily/CompanionLanguageMismatch.cat/en-ie.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/es-cl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/es-us.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/de-ch.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/es-cl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Versions/A/Resources/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalCompletion.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalCompletion.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalCompletion.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalCompletion.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/es-us.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/nl-be.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/de-ch.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/nl-be.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/en-za.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/de-ch.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableTime.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableTime.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableTime.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableTime.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutResumed.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutResumed.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutResumed.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutResumed.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/workoutResumed.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredNonPace.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredNonPace.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredNonPace.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredNonPace.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredNonPace.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredNonPace.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredNonPace.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredNonPace.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredNonPace.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredNonPace.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredNonPace.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredNonPace.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/de-ch.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/de-ch.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveSpeed.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveSpeed.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveSpeed.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveSpeed.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveSpeed.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/de-ch.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Versions/A/Resources/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/zh-tw.cat.bin`
- `/System/Library/Templates/Data/Library/Documentation/License.lpdf/Contents/Resources/bg.lproj/License.html`
- `/System/Library/Templates/Data/Library/Documentation/License.lpdf/Contents/Resources/bg.lproj/License.pdf`
- `/System/Library/Templates/Data/Library/Documentation/License.lpdf/Contents/Resources/kk.lproj/License.html`
- `/System/Library/Templates/Data/Library/Documentation/License.lpdf/Contents/Resources/kk.lproj/License.pdf`
- `/System/Library/Trial/NamespaceDescriptors/com.apple.Trial.NamespaceDescriptor.1546.plist`

</details>

## EOF
