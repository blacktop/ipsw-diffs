# 15.0 (24A5279h) .vs 15.0 (24A5289g)

## IPSWs

- `UniversalMac_15.0_24A5279h_Restore.ipsw`
- `UniversalMac_15.0_24A5289g_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 15.0 *(24A5279h)* | 24.0.0 | 11215.0.115.501.3~1 | Thu, 20Jun2024 20:36:19 PDT |
| 15.0 *(24A5289g)* | 24.0.0 | 11215.0.132.501.1~1 | Mon, 01Jul2024 21:55:30 PDT |

### Kexts

#### ⬆️ Updated (45)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.driver.AppleOLYHAL`

```diff

-326.24.0.0.0
+326.26.0.0.0
   __TEXT.__const: 0x7a8
-  __TEXT.__cstring: 0x495c
-  __TEXT_EXEC.__text: 0x1d78c
+  __TEXT.__cstring: 0x486f
+  __TEXT_EXEC.__text: 0x1d830
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x18c
   __DATA.__common: 0x170

   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__mod_init_func: 0x38
   __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x1fd8
+  __DATA_CONST.__const: 0x2018
   __DATA_CONST.__kalloc_type: 0x640
-  Functions: 549
-  Symbols:   1069
-  CStrings:  507
+  Functions: 550
+  Symbols:   1071
+  CStrings:  506
 
Symbols:
+ __ZN28AppleOLYHALPortInterfacePCIe19isFLRRecoveryFailedEv
+ __ZN32AppleOLYHALPortInterfacePCIeAMFM19isFLRRecoveryFailedEv
+ __ZZN32AppleOLYHALPortInterfacePCIeAMFM21triggerAsyncResetWorkE34AppleOLYHALPortInterfaceActionTypePvmE20kalloc_type_view_442
+ __ZZN32AppleOLYHALPortInterfacePCIeAMFM21triggerAsyncResetWorkE34AppleOLYHALPortInterfaceActionTypePvmE20kalloc_type_view_475
+ __ZZN32AppleOLYHALPortInterfacePCIeAMFM21triggerAsyncResetWorkE34AppleOLYHALPortInterfaceActionTypePvmE20kalloc_type_view_478
+ __ZZN32AppleOLYHALPortInterfacePCIeAMFM23processAMFMMessageGatedEjPvmE21kalloc_type_view_1246
+ __ZZN32AppleOLYHALPortInterfacePCIeAMFM9resetCallEPvS0_E20kalloc_type_view_499
+ __ZZN32AppleOLYHALPortInterfacePCIeAMFM9resetCallEPvS0_E20kalloc_type_view_501
+ ____ZN32AppleOLYHALPortInterfacePCIeAMFM19isFLRRecoveryFailedEv_block_invoke
+ __block_descriptor_tmp.40
- _ZN32AppleOLYHALPortInterfacePCIeAMFM23processAMFMMessageGatedEjPvm.cold.25
- _ZN32AppleOLYHALPortInterfacePCIeAMFM23processAMFMMessageGatedEjPvm.cold.26
- __ZZN32AppleOLYHALPortInterfacePCIeAMFM21triggerAsyncResetWorkE34AppleOLYHALPortInterfaceActionTypePvmE20kalloc_type_view_425
- __ZZN32AppleOLYHALPortInterfacePCIeAMFM21triggerAsyncResetWorkE34AppleOLYHALPortInterfaceActionTypePvmE20kalloc_type_view_458
- __ZZN32AppleOLYHALPortInterfacePCIeAMFM21triggerAsyncResetWorkE34AppleOLYHALPortInterfaceActionTypePvmE20kalloc_type_view_461
- __ZZN32AppleOLYHALPortInterfacePCIeAMFM23processAMFMMessageGatedEjPvmE21kalloc_type_view_1235
- __ZZN32AppleOLYHALPortInterfacePCIeAMFM9resetCallEPvS0_E20kalloc_type_view_482
- __ZZN32AppleOLYHALPortInterfacePCIeAMFM9resetCallEPvS0_E20kalloc_type_view_484
CStrings:
+ "\"Dext relaunched with unexpected status %u\" @%s:%d"
+ "\"WiFi Dext Crash Recovery during PowerCycle %u\" @%s:%d"
- "\"%s:%u:\" \"(fClientStatus == kClientFLRRecoveryFailed || fClientStatus == kClientPowerCycleRecoveryComplete || fClientStatus == kClientFLRRecoverySuccessful)\" @%s:%d"
- "\"%s:%u:\" \"(fClientStatus == kClientFLRRecoverySuccessful) || (fClientStatus == kClientPowerCycleRecoveryComplete)\" @%s:%d"
- "\"%s:%u:\" \"fResetProgress == kResetStepRequested\" @%s:%d"

```

>  `com.apple.driver.AppleSPU`

```diff

-1014.0.1.0.0
+1014.0.1.501.1
   __TEXT.__cstring: 0x4b22
   __TEXT.__os_log: 0x77f
   __TEXT.__const: 0x248
-  __TEXT_EXEC.__text: 0x426cc
+  __TEXT_EXEC.__text: 0x426d4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x788
   __DATA.__common: 0x8a8
   __DATA.__bss: 0x540
-  __DATA_CONST.__auth_got: 0x5b8
+  __DATA_CONST.__auth_got: 0x5c0
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x158

   __DATA_CONST.__kalloc_type: 0xd80
   __DATA_CONST.__kalloc_var: 0x320
   Functions: 1875
-  Symbols:   3010
+  Symbols:   3011
   CStrings:  794
 
Symbols:
+ _ml_get_conttime_offset

```

>  `com.apple.driver.AppleT8122TypeCPhy`

```diff

-239.0.0.0.0
+239.0.1.0.0
   __TEXT.__const: 0x48
   __TEXT.__cstring: 0x83ef
   __TEXT.__os_log: 0xefff
-  __TEXT_EXEC.__text: 0x4dacc
+  __TEXT_EXEC.__text: 0x4dae0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x488
   __DATA.__common: 0x38

   __DATA_CONST.__got: 0x30
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
-  __DATA_CONST.__const: 0xbe8
+  __DATA_CONST.__const: 0xbf8
   __DATA_CONST.__kalloc_type: 0x40
-  Functions: 125
-  Symbols:   1213
+  Functions: 127
+  Symbols:   1215
   CStrings:  432
 
Symbols:
+ __ZN13AppleTypeCPhy15supportS2RtoOffEv
+ __ZN13AppleTypeCPhy20shutdownACIOS2RtoOffENS_12tACIOPhyModeE

```

>  `com.apple.iokit.EndpointSecurity`

```diff

-511.0.14.0.0
-  __TEXT.__const: 0x228
-  __TEXT.__cstring: 0x843f
-  __TEXT.__os_log: 0x3c6e
-  __TEXT_EXEC.__text: 0x95750
+511.0.18.0.0
+  __TEXT.__const: 0x218
+  __TEXT.__cstring: 0x83c1
+  __TEXT.__os_log: 0x3cea
+  __TEXT_EXEC.__text: 0x95884
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x228
   __DATA.__common: 0xc4
-  __DATA.__bss: 0x140
-  __DATA_CONST.__auth_got: 0x560
-  __DATA_CONST.__got: 0x90
+  __DATA.__bss: 0x70
+  __DATA_CONST.__auth_got: 0x568
+  __DATA_CONST.__got: 0x98
   __DATA_CONST.__mod_init_func: 0x30
   __DATA_CONST.__mod_term_func: 0x40
   __DATA_CONST.__const: 0x6940
   __DATA_CONST.__kalloc_var: 0x19a0
   __DATA_CONST.__kalloc_type: 0x1380
   Functions: 2859
-  Symbols:   4436
-  CStrings:  576
+  Symbols:   4437
+  CStrings:  572
 
Symbols:
+ __ZN22EndpointSecurityDriver17systemPowerChangeEPvS0_jP9IOServiceS0_m
+ __ZN9IOService15getPMRootDomainEv
+ __ZNK4spar14PowerStateGate4openEv
+ __ZZN22EndpointSecurityDriver17systemPowerChangeEPvS0_jP9IOServiceS0_mE11_os_log_fmt
+ __ZZN22EndpointSecurityDriver17systemPowerChangeEPvS0_jP9IOServiceS0_mE11_os_log_fmt_0
+ __ZZN22EndpointSecurityDriver17systemPowerChangeEPvS0_jP9IOServiceS0_mE11_os_log_fmt_1
+ __ZZN4spar10GatedTimer12unsafeDeleteEvE20kalloc_type_view_302
+ __ZZN4spar10GatedTimer12unsafeDeleteEvE20kalloc_type_view_302
+ __ZZN4spar10GatedTimer12unsafeDeleteEvE20kalloc_type_view_302
+ __ZZN4spar10GatedTimer12unsafeDeleteEvE20kalloc_type_view_302
+ _gIOPriorityPowerStateInterest
- __ZN22EndpointSecurityDriver13setPowerStateEmP9IOService
- __ZN22EndpointSecurityDriver18systemWillShutdownEj
- __ZZN22EndpointSecurityDriver13setPowerStateEmP9IOServiceE11_os_log_fmt
- __ZZN22EndpointSecurityDriver13setPowerStateEmP9IOServiceE11_os_log_fmt_0
- __ZZN22EndpointSecurityDriver18systemWillShutdownEjE11_os_log_fmt
- __ZZN22EndpointSecurityDriver5startEP9IOServiceE11powerStates
- __ZZN4spar10GatedTimer12unsafeDeleteEvE20kalloc_type_view_299
- __ZZN4spar10GatedTimer12unsafeDeleteEvE20kalloc_type_view_299
- __ZZN4spar10GatedTimer12unsafeDeleteEvE20kalloc_type_view_299
- __ZZN4spar10GatedTimer12unsafeDeleteEvE20kalloc_type_view_299
CStrings:
- "\"setPowerState: unknown power state %lu\" @%s:%d"
- "\"systemWillShutdown: unknown shutdown specifier %llu\" @%s:%d"
- "PowerOff"
- "Restart"

```

>  `com.apple.security.quarantine`

```diff

-181.0.3.0.1
-  __TEXT.__const: 0x61
-  __TEXT.__cstring: 0x5e6
+181.0.5.0.0
+  __TEXT.__const: 0x71
+  __TEXT.__cstring: 0x5e7
   __TEXT.__os_log: 0x2a7
-  __TEXT_EXEC.__text: 0x9190
+  __TEXT_EXEC.__text: 0x92a8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcc3
   __DATA.__common: 0x24
   __DATA.__bss: 0x28
-  __DATA_CONST.__auth_got: 0x418
+  __DATA_CONST.__auth_got: 0x420
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0xc8
   __DATA_CONST.__kalloc_type: 0x280
-  Functions: 181
-  Symbols:   375
+  Functions: 182
+  Symbols:   377
   CStrings:  65
 
Symbols:
+ _responsibility_identity_get_binary_vnode
+ _vfs_getbyid
+ cred_label_alloc.kalloc_type_view_876
+ cred_label_destroy.kalloc_type_view_963
+ responsibility_alloc.kalloc_type_view_767
+ responsibility_destroy.kalloc_type_view_838
- cred_label_alloc.kalloc_type_view_861
- cred_label_destroy.kalloc_type_view_948
- responsibility_alloc.kalloc_type_view_752
- responsibility_destroy.kalloc_type_view_823
CStrings:
+ "2222221111122211222"
- "111111122222222222"

```

>  `com.apple.driver.AppleConvergedPCI`

```diff

-106.0.0.0.0
+107.0.0.0.0
   __TEXT.__const: 0x1b0
   __TEXT.__cstring: 0x6f75
-  __TEXT_EXEC.__text: 0x3f1a8
+  __TEXT_EXEC.__text: 0x3f1e4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x2d0

   __DATA_CONST.__got: 0x108
   __DATA_CONST.__mod_init_func: 0x68
   __DATA_CONST.__mod_term_func: 0x68
-  __DATA_CONST.__const: 0x6da8
+  __DATA_CONST.__const: 0x6db8
   __DATA_CONST.__kalloc_type: 0x1300
-  Functions: 1067
-  Symbols:   1724
+  Functions: 1069
+  Symbols:   1726
   CStrings:  891
 
Symbols:
+ __ZN12ACIPCControl10deviceDeadEv
+ __ZN15ACIPCNullDevice10deviceDeadEv
+ __ZZN15ACIPCNullDevicedlEPvmE19kalloc_type_view_45
+ __ZZN15ACIPCNullDevicenwEmE19kalloc_type_view_45
- __ZZN15ACIPCNullDevicedlEPvmE19kalloc_type_view_44
- __ZZN15ACIPCNullDevicenwEmE19kalloc_type_view_44
CStrings:
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCControl.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCLogger.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCIOCommand.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCMemoryCommand.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCMemoryPolicy.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCRequest.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/UserClient/AppleConvergedIPCControlUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/UserClient/AppleConvergedIPCUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedPCI/AppleConvergedPCI.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/ACIPCChip.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/ACIPCControl.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/ACIPCPort.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/Chips/ACIPCChip4388.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCControl.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCInterface.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCLogger.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCIOCommand.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCMemoryCommand.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCMemoryPolicy.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCRequest.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/UserClient/AppleConvergedIPCControlUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/UserClient/AppleConvergedIPCUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedPCI/AppleConvergedPCI.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/ACIPCChip.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/ACIPCControl.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/ACIPCPort.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/Chips/ACIPCChip4388.cpp"

```

>  `com.apple.driver.AppleH13CameraInterface`

```diff

-9.4.0.0.0
+9.5.0.0.0
   __TEXT.__const: 0x94c
-  __TEXT.__cstring: 0x7394
+  __TEXT.__cstring: 0x74ed
   __TEXT.__os_log: 0xd3df
   __TEXT.__ustring: 0x40
-  __TEXT_EXEC.__text: 0x573bc
+  __TEXT_EXEC.__text: 0x5743c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x288

   __DATA_CONST.__const: 0xfc38
   __DATA_CONST.__kalloc_type: 0xc40
   __DATA_CONST.__kalloc_var: 0xd70
-  Functions: 1107
-  Symbols:   2763
-  CStrings:  924
+  Functions: 1108
+  Symbols:   2764
+  CStrings:  925
 
Symbols:
+ _ZN13AppleH13CamIn23EnableISPClocksAndPowerEv.cold.2
+ __ZZL10ffw_callocmmE22kalloc_type_view_24801
+ __ZZL37H13CamInChannelSACParams_replaceListsP24H13CamInChannelSACParamsjE22kalloc_type_view_20792
+ __ZZL37H13CamInChannelSACParams_replaceListsP24H13CamInChannelSACParamsjE22kalloc_type_view_20793
+ __ZZL37H13CamInChannelSACParams_replaceListsP24H13CamInChannelSACParamsjE22kalloc_type_view_20794
+ __ZZL37H13CamInChannelSACParams_replaceListsP24H13CamInChannelSACParamsjE22kalloc_type_view_20797
+ __ZZL37H13CamInChannelSACParams_replaceListsP24H13CamInChannelSACParamsjE22kalloc_type_view_20798
+ __ZZL37H13CamInChannelSACParams_replaceListsP24H13CamInChannelSACParamsjE22kalloc_type_view_20799
+ __ZZL37H13CamInChannelSACParams_replaceListsP24H13CamInChannelSACParamsjE22kalloc_type_view_20805
+ __ZZL37H13CamInChannelSACParams_replaceListsP24H13CamInChannelSACParamsjE22kalloc_type_view_20806
+ __ZZL37H13CamInChannelSACParams_replaceListsP24H13CamInChannelSACParamsjE22kalloc_type_view_20807
+ __ZZL8ffw_freePvE22kalloc_type_view_24806
+ __ZZN13AppleH13CamIn22SendBCARDataToFirmwareEjE22kalloc_type_view_24916
+ __ZZN13AppleH13CamIn22SendBCARDataToFirmwareEjE22kalloc_type_view_24926
+ __ZZN13AppleH13CamIn22SendBCTRDataToFirmwareEjE22kalloc_type_view_24881
+ __ZZN13AppleH13CamIn22SendBCTRDataToFirmwareEjE22kalloc_type_view_24890
+ __ZZN13AppleH13CamIn26ISP_InitialSensorDetectionEvE22kalloc_type_view_21987
+ __ZZN13AppleH13CamIn26ISP_InitialSensorDetectionEvE22kalloc_type_view_22205
+ __ZZN13AppleH13CamIn26ISP_InitialSensorDetectionEvE22kalloc_type_view_22238
+ __ZZN13AppleH13CamIn26ISP_InitialSensorDetectionEvE22kalloc_type_view_22358
+ __ZZN13AppleH13CamIn26ISP_InitialSensorDetectionEvE22kalloc_type_view_22391
+ __ZZN13AppleH13CamIn26ISP_InitialSensorDetectionEvE22kalloc_type_view_22415
+ __ZZN13AppleH13CamIn26ISP_InitialSensorDetectionEvE22kalloc_type_view_22428
+ __ZZN13AppleH13CamIn26ISP_InitialSensorDetectionEvE22kalloc_type_view_22444
+ __ZZN13AppleH13CamIn26ISP_InitialSensorDetectionEvE22kalloc_type_view_22465
+ __ZZN13AppleH13CamIn27SendStrobeCalDataToFirmwareEjE22kalloc_type_view_24845
+ __ZZN13AppleH13CamIn27SendStrobeCalDataToFirmwareEjE22kalloc_type_view_24855
+ __ZZN13AppleH13CamIn32SendLPDPRxPhyEfuseDataToFirmwareEjE22kalloc_type_view_24987
+ __ZZN13AppleH13CamIn32SendLPDPRxPhyEfuseDataToFirmwareEjE22kalloc_type_view_25005
+ __ZZN13AppleH13CamIn39SendSphereExtendedStrokeRangeToFirmwareEjE22kalloc_type_view_25039
+ __ZZN13AppleH13CamIn39SendSphereExtendedStrokeRangeToFirmwareEjE22kalloc_type_view_25047
+ __cxx_global_var_init.1278
- __ZZL10ffw_callocmmE22kalloc_type_view_24769
- __ZZL37H13CamInChannelSACParams_replaceListsP24H13CamInChannelSACParamsjE22kalloc_type_view_20760
- __ZZL37H13CamInChannelSACParams_replaceListsP24H13CamInChannelSACParamsjE22kalloc_type_view_20761
- __ZZL37H13CamInChannelSACParams_replaceListsP24H13CamInChannelSACParamsjE22kalloc_type_view_20762
- __ZZL37H13CamInChannelSACParams_replaceListsP24H13CamInChannelSACParamsjE22kalloc_type_view_20765
- __ZZL37H13CamInChannelSACParams_replaceListsP24H13CamInChannelSACParamsjE22kalloc_type_view_20766
- __ZZL37H13CamInChannelSACParams_replaceListsP24H13CamInChannelSACParamsjE22kalloc_type_view_20767
- __ZZL37H13CamInChannelSACParams_replaceListsP24H13CamInChannelSACParamsjE22kalloc_type_view_20773
- __ZZL37H13CamInChannelSACParams_replaceListsP24H13CamInChannelSACParamsjE22kalloc_type_view_20774
- __ZZL37H13CamInChannelSACParams_replaceListsP24H13CamInChannelSACParamsjE22kalloc_type_view_20775
- __ZZL8ffw_freePvE22kalloc_type_view_24774
- __ZZN13AppleH13CamIn22SendBCARDataToFirmwareEjE22kalloc_type_view_24884
- __ZZN13AppleH13CamIn22SendBCARDataToFirmwareEjE22kalloc_type_view_24894
- __ZZN13AppleH13CamIn22SendBCTRDataToFirmwareEjE22kalloc_type_view_24849
- __ZZN13AppleH13CamIn22SendBCTRDataToFirmwareEjE22kalloc_type_view_24858
- __ZZN13AppleH13CamIn26ISP_InitialSensorDetectionEvE22kalloc_type_view_21955
- __ZZN13AppleH13CamIn26ISP_InitialSensorDetectionEvE22kalloc_type_view_22173
- __ZZN13AppleH13CamIn26ISP_InitialSensorDetectionEvE22kalloc_type_view_22206
- __ZZN13AppleH13CamIn26ISP_InitialSensorDetectionEvE22kalloc_type_view_22326
- __ZZN13AppleH13CamIn26ISP_InitialSensorDetectionEvE22kalloc_type_view_22359
- __ZZN13AppleH13CamIn26ISP_InitialSensorDetectionEvE22kalloc_type_view_22383
- __ZZN13AppleH13CamIn26ISP_InitialSensorDetectionEvE22kalloc_type_view_22396
- __ZZN13AppleH13CamIn26ISP_InitialSensorDetectionEvE22kalloc_type_view_22412
- __ZZN13AppleH13CamIn26ISP_InitialSensorDetectionEvE22kalloc_type_view_22433
- __ZZN13AppleH13CamIn27SendStrobeCalDataToFirmwareEjE22kalloc_type_view_24813
- __ZZN13AppleH13CamIn27SendStrobeCalDataToFirmwareEjE22kalloc_type_view_24823
- __ZZN13AppleH13CamIn32SendLPDPRxPhyEfuseDataToFirmwareEjE22kalloc_type_view_24955
- __ZZN13AppleH13CamIn32SendLPDPRxPhyEfuseDataToFirmwareEjE22kalloc_type_view_24973
- __ZZN13AppleH13CamIn39SendSphereExtendedStrokeRangeToFirmwareEjE22kalloc_type_view_25007
- __ZZN13AppleH13CamIn39SendSphereExtendedStrokeRangeToFirmwareEjE22kalloc_type_view_25015
- __cxx_global_var_init.1272
CStrings:
+ "\"Could not power up the ISP, PS regs: \" \" RMX_PS = 0x%x \" \" ISP_SYS_PS = 0x%x \" \" ISP_CPU_PS = 0x%x \" \" ISP_CPU_CORE0_PS = 0x%x \" \" ISP_CPU_CORE1_PS = 0x%x \" \" ISP_DPRX_PS = 0x%x \" \" ISP_STS0_PS = 0x%x \" \" ISP_STS1_PS = 0x%x \" \" ISP_VIS_PS = 0x%x \" \" ISP_BE_PS = 0x%x \" \" ISP_PEARL_PS = 0x%x \" \" ISP_CLR_PS = 0x%x \" \" ISP_RAW_PS = 0x%x \" @%s:%d"

```

>  `com.apple.driver.AppleHPM`

```diff

-570.0.0.0.0
-  __TEXT.__cstring: 0x10466
+570.0.1.0.0
+  __TEXT.__cstring: 0x10481
   __TEXT.__const: 0xb0
   __TEXT.__os_log: 0x1e8
-  __TEXT_EXEC.__text: 0x502e8
+  __TEXT_EXEC.__text: 0x50344
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6c9
   __DATA.__common: 0x540
   __DATA.__bss: 0x4
-  __DATA_CONST.__auth_got: 0x450
+  __DATA_CONST.__auth_got: 0x458
   __DATA_CONST.__got: 0x108
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__mod_init_func: 0x100

   __DATA_CONST.__const: 0x19e70
   __DATA_CONST.__kalloc_type: 0xa40
   Functions: 1392
-  Symbols:   2227
-  CStrings:  925
+  Symbols:   2228
+  CStrings:  926
 
Symbols:
+ __ZN9OSBoolean11withBooleanEb
CStrings:
+ "AsymmetricModeSupportedBit"

```

>  `com.apple.driver.AppleMesaSEPDriver`

```diff

-10185.0.2.501.1
+10185.0.6.0.0
   __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x58b0
-  __TEXT.__os_log: 0x2abe
-  __TEXT_EXEC.__text: 0x2df6c
+  __TEXT.__cstring: 0x58ba
+  __TEXT.__os_log: 0x2b06
+  __TEXT_EXEC.__text: 0x2dea0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcc
   __DATA.__common: 0x278
   __DATA.__bss: 0x18
-  __DATA_CONST.__auth_got: 0x370
+  __DATA_CONST.__auth_got: 0x358
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__mod_init_func: 0x30
   __DATA_CONST.__mod_term_func: 0x30
-  __DATA_CONST.__const: 0x4420
+  __DATA_CONST.__const: 0x4428
   __DATA_CONST.__kalloc_type: 0x580
   __DATA_CONST.__kalloc_var: 0x140
   Functions: 518
-  Symbols:   1458
-  CStrings:  728
+  Symbols:   1456
+  CStrings:  727
 
Symbols:
+ __ZN18AppleMesaSEPDriver13sensorDisableEbb
+ __ZZN18AppleMesaSEPDriver11handleMatchEbP17IOMesaCaptureDatabPbhE21kalloc_type_view_7893
+ __ZZN18AppleMesaSEPDriver11handleMatchEbP17IOMesaCaptureDatabPbhE21kalloc_type_view_8222
+ __ZZN18AppleMesaSEPDriver13sensorDisableEbbE11_os_log_fmt
+ __ZZN18AppleMesaSEPDriver13sensorDisableEbbE11_os_log_fmt_0
+ __ZZN18AppleMesaSEPDriver13sensorDisableEbbE11_os_log_fmt_1
+ __ZZN18AppleMesaSEPDriver13sensorDisableEbbE11_os_log_fmt_2
+ __ZZN18AppleMesaSEPDriver16sendEnrollResultEP16enroll_result_v2E21kalloc_type_view_6687
+ __ZZN18AppleMesaSEPDriver16sendEnrollResultEP16enroll_result_v2E21kalloc_type_view_6696
+ __ZZN18AppleMesaSEPDriver19applyPostponedMatchEP24postponed_match_result_tbE21kalloc_type_view_9868
+ __ZZN18AppleMesaSEPDriver19applyPostponedMatchEP24postponed_match_result_tbE21kalloc_type_view_9920
+ __ZZN18AppleMesaSEPDriver26sendTemplateListUpdatedMsgEP25template_update_info_v2_tE21kalloc_type_view_6757
+ __ZZN18AppleMesaSEPDriver26sendTemplateListUpdatedMsgEP25template_update_info_v2_tE21kalloc_type_view_6766
+ __ZZN18AppleMesaSEPDriver29sendTemplateListNotUpdatedMsgEP17bgops_result_v2_tE21kalloc_type_view_6789
+ __ZZN18AppleMesaSEPDriver29sendTemplateListNotUpdatedMsgEP17bgops_result_v2_tE21kalloc_type_view_6798
+ __ZZN18AppleMesaSEPDriver31sendEnrollProgresWithEnrollInfoEhP20enrollment_info_v2_tE21kalloc_type_view_6657
+ __ZZN18AppleMesaSEPDriver31sendEnrollProgresWithEnrollInfoEhP20enrollment_info_v2_tE21kalloc_type_view_6666
+ __block_descriptor_tmp.374
+ __block_descriptor_tmp.385
+ __block_descriptor_tmp.387
- __ZN12OSDictionary12withCapacityEj
- __ZN12OSDictionary9setObjectEPKcRK11OSSharedPtrIK15OSMetaClassBaseE
- __ZN18AppleMesaSEPDriver13sensorDisableEb
- __ZN8OSNumber10withNumberEyj
- __ZZN18AppleMesaSEPDriver11handleMatchEbP17IOMesaCaptureDatabPbhE21kalloc_type_view_7889
- __ZZN18AppleMesaSEPDriver11handleMatchEbP17IOMesaCaptureDatabPbhE21kalloc_type_view_8218
- __ZZN18AppleMesaSEPDriver13sensorDisableEbE11_os_log_fmt
- __ZZN18AppleMesaSEPDriver13sensorDisableEbE11_os_log_fmt_0
- __ZZN18AppleMesaSEPDriver13sensorDisableEbE11_os_log_fmt_1
- __ZZN18AppleMesaSEPDriver16sendEnrollResultEP16enroll_result_v2E21kalloc_type_view_6683
- __ZZN18AppleMesaSEPDriver16sendEnrollResultEP16enroll_result_v2E21kalloc_type_view_6692
- __ZZN18AppleMesaSEPDriver19applyPostponedMatchEP24postponed_match_result_tbE21kalloc_type_view_9864
- __ZZN18AppleMesaSEPDriver19applyPostponedMatchEP24postponed_match_result_tbE21kalloc_type_view_9916
- __ZZN18AppleMesaSEPDriver26sendTemplateListUpdatedMsgEP25template_update_info_v2_tE21kalloc_type_view_6753
- __ZZN18AppleMesaSEPDriver26sendTemplateListUpdatedMsgEP25template_update_info_v2_tE21kalloc_type_view_6762
- __ZZN18AppleMesaSEPDriver29sendTemplateListNotUpdatedMsgEP17bgops_result_v2_tE21kalloc_type_view_6785
- __ZZN18AppleMesaSEPDriver29sendTemplateListNotUpdatedMsgEP17bgops_result_v2_tE21kalloc_type_view_6794
- __ZZN18AppleMesaSEPDriver31sendEnrollProgresWithEnrollInfoEhP20enrollment_info_v2_tE21kalloc_type_view_6653
- __ZZN18AppleMesaSEPDriver31sendEnrollProgresWithEnrollInfoEhP20enrollment_info_v2_tE21kalloc_type_view_6662
- __block_descriptor_tmp.377
- __block_descriptor_tmp.390
- __block_descriptor_tmp.391
CStrings:
+ "!factoryOptionsOnly || _sensorType == kSensorTypeTritonA2"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaAccessory/AppleMesaAccessory.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaAccessory/MesaAccessoryIntReports.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaAccessory/MesaAccessoryManager.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaSEPDriver.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/IOMesaCaptureDataQueue.cpp"
+ "1211111212221212112121111111111111111111112112112222222212211122222222222222222222222222222222222222222222222222222221112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222122221211212222211122222221221212121222222222222222222121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111111"
+ "kSetSensorPowerCommand"
- "/AppleInternal/Library/BuildRoots/c78ea4c7-2fc7-11ef-9487-e2437461156c/Library/Caches/com.apple.xbs/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaAccessory/AppleMesaAccessory.cpp"
- "/AppleInternal/Library/BuildRoots/c78ea4c7-2fc7-11ef-9487-e2437461156c/Library/Caches/com.apple.xbs/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaAccessory/MesaAccessoryIntReports.cpp"
- "/AppleInternal/Library/BuildRoots/c78ea4c7-2fc7-11ef-9487-e2437461156c/Library/Caches/com.apple.xbs/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaAccessory/MesaAccessoryManager.cpp"
- "/AppleInternal/Library/BuildRoots/c78ea4c7-2fc7-11ef-9487-e2437461156c/Library/Caches/com.apple.xbs/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaSEPDriver.cpp"
- "/AppleInternal/Library/BuildRoots/c78ea4c7-2fc7-11ef-9487-e2437461156c/Library/Caches/com.apple.xbs/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/IOMesaCaptureDataQueue.cpp"
- "121111121222121211212111111111111111111111211211222222221221112222222222222222222222222222222222222222222222222222222111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222121121222221112222222122121212122222222222222222212122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111111"
- "dictionary"
- "dictionary->setObject(\"wakeOnMenuPin\", number)"
- "wakeOnMenuPin"

```

>  `com.apple.driver.AppleSEPKeyStore`

```diff

-1827.0.41.0.1
-  __TEXT.__cstring: 0x3d0c
+1827.0.50.0.0
+  __TEXT.__cstring: 0x3d08
   __TEXT.__const: 0x864
   __TEXT_EXEC.__text: 0x3e984
   __TEXT_EXEC.__auth_stubs: 0x0
CStrings:
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_SEP_kexts/AppleKeyStore.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_SEP_kexts/ipc.c"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_SEP_kexts/msg.c"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_SEP_kexts/platform/platform.c"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_SEP_kexts/platform/platform_kernel.c"
+ "1827.0.50"
+ "20:02:59"
+ "Jul  3 2024"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_SEP_kexts/AppleKeyStore.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_SEP_kexts/ipc.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_SEP_kexts/msg.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_SEP_kexts/platform/platform.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_SEP_kexts/platform/platform_kernel.c"
- "1827.0.41.0.1"
- "20:29:54"
- "Jun 20 2024"

```

>  `com.apple.driver.AppleSmartBatteryManager`

```diff

-1730.0.0.0.2
-  __TEXT.__const: 0x1558
-  __TEXT.__cstring: 0x290f
+1735.0.0.0.0
+  __TEXT.__const: 0x1588
+  __TEXT.__cstring: 0x2933
   __TEXT.__os_log: 0x232c
-  __TEXT_EXEC.__text: 0x1ae7c
+  __TEXT_EXEC.__text: 0x1aef0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x208
   __DATA.__common: 0xd8
-  __DATA.__bss: 0x3110
+  __DATA.__bss: 0x3170
   __DATA_CONST.__auth_got: 0x338
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__mod_init_func: 0x28

   __DATA_CONST.__const: 0x2c00
   __DATA_CONST.__kalloc_type: 0x200
   Functions: 242
-  Symbols:   1493
-  CStrings:  550
+  Symbols:   1496
+  CStrings:  553
 
Symbols:
+ __ZL15_kCommStatusSym
+ __ZL24_kGGCalculatedMaxWRdcSym
+ __ZL29_kGGCalculatedNccPFilteredSym
+ __ZZN17AppleSmartBattery17removeClientGatedEP29AppleSmartBatteryHFDataClientP5OSSetE21kalloc_type_view_6557
+ __ZZN17AppleSmartBattery18initializeCommandsEvE21kalloc_type_view_3003
+ __ZZN17AppleSmartBattery20startCollectionGatedEP12OSDictionaryP29AppleSmartBatteryHFDataClientE21kalloc_type_view_6102
- __ZZN17AppleSmartBattery17removeClientGatedEP29AppleSmartBatteryHFDataClientP5OSSetE21kalloc_type_view_6551
- __ZZN17AppleSmartBattery18initializeCommandsEvE21kalloc_type_view_2998
- __ZZN17AppleSmartBattery20startCollectionGatedEP12OSDictionaryP29AppleSmartBatteryHFDataClientE21kalloc_type_view_6096
CStrings:
+ "CommStatus"
+ "MaximumWRdc"
+ "NccpFiltered"

```

>  `com.apple.driver.AppleStockholmControl`

```diff

-350.26.1.0.0
-  __TEXT.__cstring: 0x3d2b
+350.28.0.0.0
+  __TEXT.__cstring: 0x3e5b
   __TEXT.__const: 0x30
-  __TEXT_EXEC.__text: 0x12ae8
+  __TEXT_EXEC.__text: 0x12dfc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x219
   __DATA.__common: 0x17e

   __DATA_CONST.__kalloc_type: 0x180
   Functions: 231
   Symbols:   735
-  CStrings:  409
+  CStrings:  414
 
CStrings:
+ "ERR: %s::%s:%d Error : Pending flag is false !\n"
+ "ERR: %s::%s:%d data ready but unable to send to client - drop\n"
+ "[%llu] %s::%s:%d data ready but unable to send to client - enqueuing."
+ "[%llu] ERR: %s::%s:%d Error : Pending flag is false !"
+ "[%llu] ERR: %s::%s:%d data ready but unable to send to client - drop"

```

>  `com.apple.filesystems.smbfs`

```diff

-484.0.0.0.0
+488.0.0.0.0
   __TEXT.__const: 0xb55
-  __TEXT.__cstring: 0x4567
-  __TEXT.__os_log: 0x1590d
-  __TEXT_EXEC.__text: 0x7d04c
+  __TEXT.__cstring: 0x4555
+  __TEXT.__os_log: 0x1588d
+  __TEXT_EXEC.__text: 0x7ceec
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xdf8
   __DATA.__bss: 0x1194

   __DATA_CONST.__const: 0x78
   __DATA_CONST.__kalloc_type: 0x4d40
   __DATA_CONST.__kalloc_var: 0x3c0
-  Functions: 812
-  Symbols:   3710
-  CStrings:  936
+  Functions: 811
+  Symbols:   3706
+  CStrings:  935
 
Symbols:
+ AddRemoveByteRangeLockEntry._os_log_fmt.131
+ AddRemoveByteRangeLockEntry._os_log_fmt.134
+ AddRemoveByteRangeLockEntry._os_log_fmt.135
+ AddRemoveByteRangeLockEntry.kalloc_type_view_6159
+ AddRemoveByteRangeLockEntry.kalloc_type_view_6197
+ AddRemoveByteRangeLockEntry.kalloc_type_view_6208
+ CheckByteRangeLockEntry._os_log_fmt.136
+ CheckByteRangeLockEntry._os_log_fmt.137
+ CloseDeferredFileRefs._os_log_fmt.58
+ CloseDeferredFileRefs._os_log_fmt.59
+ FindByteRangeLockEntry._os_log_fmt.139
+ FindFileRef._os_log_fmt.140
+ FindFileRef._os_log_fmt.141
+ FindFileRef._os_log_fmt.144
+ FindFileRef._os_log_fmt.145
+ nsmb_dev_load.kalloc_type_view_1828
+ nsmb_dev_load.kalloc_type_view_1836
+ smb2_dur_handle_init._os_log_fmt.68
+ smb2_lease_init._os_log_fmt.69
+ smb2_lease_init._os_log_fmt.70
+ smb2_mc_add_new_interface_info_to_list.kalloc_type_view_1466
+ smb2_mc_query_info_response_event.kalloc_type_view_787
+ smb2_mc_query_info_response_event.kalloc_type_view_862
+ smb2_mc_release_connection_list.kalloc_type_view_1798
+ smb2_mc_release_interface.kalloc_type_view_1812
+ smb2_mc_release_interface.kalloc_type_view_1827
+ smb2_mc_remove_nic_if_unused.kalloc_type_view_969
+ smb2_mc_update_con_list.kalloc_type_view_1635
+ smb2_mc_update_info_with_ip.kalloc_type_view_1974
+ smb2_mc_update_info_with_ip.kalloc_type_view_1982
+ smb2fs_reconnect._os_log_fmt.41
+ smb2fs_reconnect._os_log_fmt.42
+ smb2fs_reconnect._os_log_fmt.48
+ smb2fs_reconnect._os_log_fmt.56
+ smb2fs_reconnect.kalloc_type_view_3800
+ smb2fs_reconnect.kalloc_type_view_4344
+ smb2fs_reconnect_dur_handle._os_log_fmt.29
+ smb2fs_reconnect_dur_handle._os_log_fmt.32
+ smb2fs_reconnect_dur_handle._os_log_fmt.33
+ smb2fs_reconnect_dur_handle._os_log_fmt.36
+ smb2fs_reconnect_dur_handle._os_log_fmt.40
+ smb2fs_reconnect_dur_handle.kalloc_type_view_3562
+ smb2fs_reconnect_dur_handle.kalloc_type_view_3718
+ smb2fs_smb_query_network_interface_info.kalloc_type_view_11027
+ smb_check_for_windows_symlink._os_log_fmt.175
+ smb_hashget._os_log_fmt.171
+ smb_hashget._os_log_fmt.172
+ smb_iod_create.kalloc_type_view_4167
+ smb_iod_create.kalloc_type_view_4185
+ smb_iod_create.kalloc_type_view_4213
+ smb_iod_destroy.kalloc_type_view_4283
+ smb_iod_destroy.kalloc_type_view_4287
+ smb_iod_destroy.kalloc_type_view_4314
+ smb_iod_lease_dequeue.kalloc_type_view_4763
+ smb_iod_lease_enqueue.kalloc_type_view_4063
+ smb_iod_main.kalloc_type_view_3866
+ smb_iod_thread.kalloc_type_view_3969
+ smb_session_lease_thread.kalloc_type_view_2234
+ smb_share_create.kalloc_type_view_1493
+ smb_share_create.kalloc_type_view_1499
+ smb_share_free.kalloc_type_view_1454
+ smbfs_CloseChildren._os_log_fmt.24
+ smbfs_CloseChildren._os_log_fmt.25
+ smbfs_CloseChildren._os_log_fmt.28
+ smbfs_CloseChildren.kalloc_type_view_3353
+ smbfs_add_update_lease._os_log_fmt.72
+ smbfs_add_update_lease._os_log_fmt.73
+ smbfs_build_path._os_log_fmt.187
+ smbfs_clear_lockEntries.kalloc_type_view_6570
+ smbfs_clear_lockEntries.kalloc_type_view_6600
+ smbfs_close.kalloc_type_view_1257
+ smbfs_close.kalloc_type_view_1607
+ smbfs_close_fid.kalloc_type_view_877
+ smbfs_create_open.kalloc_type_view_2223
+ smbfs_create_open.kalloc_type_view_2242
+ smbfs_do_strategy.kalloc_type_view_6689
+ smbfs_do_strategy.kalloc_type_view_6828
+ smbfs_find_lockEntry._os_log_fmt.151
+ smbfs_free_locks_on_close._os_log_fmt.152
+ smbfs_free_locks_on_close._os_log_fmt.153
+ smbfs_free_locks_on_close._os_log_fmt.160
+ smbfs_free_locks_on_close.kalloc_type_view_6752
+ smbfs_get_lockEntry._os_log_fmt.165
+ smbfs_get_lockEntry._os_log_fmt.166
+ smbfs_get_lockEntry.kalloc_type_view_6959
+ smbfs_get_lockEntry.kalloc_type_view_7048
+ smbfs_getattr.kalloc_type_view_4926
+ smbfs_handle_dir_lease_break._os_log_fmt.100
+ smbfs_handle_dir_lease_break._os_log_fmt.99
+ smbfs_handle_lease_break._os_log_fmt.104
+ smbfs_handle_lease_break._os_log_fmt.105
+ smbfs_handle_lease_break._os_log_fmt.114
+ smbfs_lease_hash_add.kalloc_type_view_6011
+ smbfs_lease_hash_remove.kalloc_type_view_6111
+ smbfs_open.kalloc_type_view_2300
+ smbfs_open.kalloc_type_view_2947
+ smbfs_trigger_get_mount_args._os_log_fmt.181
+ smbfs_trigger_get_mount_args._os_log_fmt.182
+ smbfs_vnop_advlock.kalloc_type_view_10927
+ smbfs_vnop_advlock.kalloc_type_view_11016
+ smbfs_vnop_compound_open.kalloc_type_view_3331
+ smbfs_vnop_compound_open.kalloc_type_view_3732
+ smbfs_vnop_getxattr.kalloc_type_view_12680
+ smbfs_vnop_getxattr.kalloc_type_view_12697
+ smbfs_vnop_reclaim.kalloc_type_view_4347
+ smbfs_vnop_reclaim.kalloc_type_view_4374
+ smbfs_vnop_rename.kalloc_type_view_9086
+ smbfs_vnop_strategy.kalloc_type_view_6872
- AddRemoveByteRangeLockEntry._os_log_fmt.133
- AddRemoveByteRangeLockEntry._os_log_fmt.136
- AddRemoveByteRangeLockEntry._os_log_fmt.137
- AddRemoveByteRangeLockEntry.kalloc_type_view_6237
- AddRemoveByteRangeLockEntry.kalloc_type_view_6275
- AddRemoveByteRangeLockEntry.kalloc_type_view_6286
- CheckByteRangeLockEntry._os_log_fmt.139
- CheckByteRangeLockEntry._os_log_fmt.140
- CloseDeferredFileRefs._os_log_fmt.68
- CloseDeferredFileRefs._os_log_fmt.69
- FindByteRangeLockEntry._os_log_fmt.141
- FindFileRef._os_log_fmt.142
- FindFileRef._os_log_fmt.143
- FindFileRef._os_log_fmt.151
- FindFileRef._os_log_fmt.152
- _smbfs_ClearChildren
- nsmb_dev_load.kalloc_type_view_1827
- nsmb_dev_load.kalloc_type_view_1835
- smb2_dur_handle_init._os_log_fmt.70
- smb2_lease_init._os_log_fmt.72
- smb2_lease_init._os_log_fmt.73
- smb2_mc_add_new_interface_info_to_list.kalloc_type_view_1460
- smb2_mc_query_info_response_event.kalloc_type_view_784
- smb2_mc_query_info_response_event.kalloc_type_view_859
- smb2_mc_release_connection_list.kalloc_type_view_1792
- smb2_mc_release_interface.kalloc_type_view_1806
- smb2_mc_release_interface.kalloc_type_view_1821
- smb2_mc_remove_nic_if_unused.kalloc_type_view_966
- smb2_mc_update_con_list.kalloc_type_view_1629
- smb2_mc_update_info_with_ip.kalloc_type_view_1968
- smb2_mc_update_info_with_ip.kalloc_type_view_1976
- smb2fs_reconnect._os_log_fmt.46
- smb2fs_reconnect._os_log_fmt.54
- smb2fs_reconnect._os_log_fmt.58
- smb2fs_reconnect._os_log_fmt.59
- smb2fs_reconnect.kalloc_type_view_3878
- smb2fs_reconnect.kalloc_type_view_4422
- smb2fs_reconnect_dur_handle._os_log_fmt.31
- smb2fs_reconnect_dur_handle._os_log_fmt.34
- smb2fs_reconnect_dur_handle._os_log_fmt.38
- smb2fs_reconnect_dur_handle._os_log_fmt.41
- smb2fs_reconnect_dur_handle._os_log_fmt.42
- smb2fs_reconnect_dur_handle.kalloc_type_view_3640
- smb2fs_reconnect_dur_handle.kalloc_type_view_3796
- smb2fs_smb_query_network_interface_info.kalloc_type_view_11026
- smb_check_for_windows_symlink._os_log_fmt.179
- smb_hashget._os_log_fmt.173
- smb_hashget._os_log_fmt.174
- smb_iod_create.kalloc_type_view_4168
- smb_iod_create.kalloc_type_view_4186
- smb_iod_create.kalloc_type_view_4214
- smb_iod_destroy.kalloc_type_view_4284
- smb_iod_destroy.kalloc_type_view_4288
- smb_iod_destroy.kalloc_type_view_4315
- smb_iod_lease_dequeue.kalloc_type_view_4764
- smb_iod_lease_enqueue.kalloc_type_view_4064
- smb_iod_main.kalloc_type_view_3867
- smb_iod_thread.kalloc_type_view_3970
- smb_session_lease_thread.kalloc_type_view_2232
- smb_share_create.kalloc_type_view_1491
- smb_share_create.kalloc_type_view_1497
- smb_share_free.kalloc_type_view_1452
- smbfs_ClearChildren._os_log_fmt
- smbfs_ClearChildren._os_log_fmt.24
- smbfs_ClearChildren._os_log_fmt.25
- smbfs_CloseChildren._os_log_fmt.26
- smbfs_CloseChildren._os_log_fmt.27
- smbfs_CloseChildren._os_log_fmt.30
- smbfs_CloseChildren.kalloc_type_view_3431
- smbfs_add_update_lease._os_log_fmt.100
- smbfs_add_update_lease._os_log_fmt.99
- smbfs_build_path._os_log_fmt.189
- smbfs_clear_lockEntries.kalloc_type_view_6648
- smbfs_clear_lockEntries.kalloc_type_view_6678
- smbfs_close.kalloc_type_view_1254
- smbfs_close.kalloc_type_view_1604
- smbfs_close_fid.kalloc_type_view_874
- smbfs_create_open.kalloc_type_view_2220
- smbfs_create_open.kalloc_type_view_2239
- smbfs_do_strategy.kalloc_type_view_6694
- smbfs_do_strategy.kalloc_type_view_6833
- smbfs_find_lockEntry._os_log_fmt.153
- smbfs_free_locks_on_close._os_log_fmt.156
- smbfs_free_locks_on_close._os_log_fmt.165
- smbfs_free_locks_on_close._os_log_fmt.166
- smbfs_free_locks_on_close.kalloc_type_view_6830
- smbfs_get_lockEntry._os_log_fmt.169
- smbfs_get_lockEntry._os_log_fmt.172
- smbfs_get_lockEntry.kalloc_type_view_7037
- smbfs_get_lockEntry.kalloc_type_view_7126
- smbfs_getattr.kalloc_type_view_4931
- smbfs_handle_dir_lease_break._os_log_fmt.104
- smbfs_handle_dir_lease_break._os_log_fmt.105
- smbfs_handle_lease_break._os_log_fmt.112
- smbfs_handle_lease_break._os_log_fmt.126
- smbfs_handle_lease_break._os_log_fmt.129
- smbfs_lease_hash_add.kalloc_type_view_6089
- smbfs_lease_hash_remove.kalloc_type_view_6189
- smbfs_open.kalloc_type_view_2297
- smbfs_open.kalloc_type_view_2944
- smbfs_trigger_get_mount_args._os_log_fmt.184
- smbfs_trigger_get_mount_args._os_log_fmt.185
- smbfs_vnop_advlock.kalloc_type_view_10932
- smbfs_vnop_advlock.kalloc_type_view_11021
- smbfs_vnop_compound_open.kalloc_type_view_3328
- smbfs_vnop_compound_open.kalloc_type_view_3729
- smbfs_vnop_getxattr.kalloc_type_view_12685
- smbfs_vnop_getxattr.kalloc_type_view_12702
- smbfs_vnop_reclaim.kalloc_type_view_4352
- smbfs_vnop_reclaim.kalloc_type_view_4379
- smbfs_vnop_rename.kalloc_type_view_9091
- smbfs_vnop_strategy.kalloc_type_view_6877
CStrings:
+ "2112222111111122222222111122222222222222222222211222121222222222222222222222222222222222222222222222222111222222222222222212222222222222222212222111222222222222222211211221222112112211222222222222222222222222222"
- "21122221111111222222221111222222222222222222222112221212222222222222222222222222222222222222222222222221112222222222222222122222222222222222122221112222222222222221121121222112112211222222222222222222222222222"
- "smbfs_ClearChildren"

```

>  `com.apple.kec.corecrypto`

```diff

-1736.0.27.0.1
-  __TEXT.__cstring: 0x46c7
-  __TEXT.__const: 0x144a0
+1736.0.36.0.0
+  __TEXT.__cstring: 0x46eb
+  __TEXT.__const: 0x14480
   __TEXT.__fips_hmacs: 0x20
-  __TEXT_EXEC.__text: 0x549f8
+  __TEXT_EXEC.__text: 0x58bec
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2df0
-  __DATA.__bss: 0x2960
-  __DATA.__common: 0x138
+  __DATA.__bss: 0x2980
+  __DATA.__common: 0x140
   __DATA_CONST.__auth_got: 0x120
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x128
-  __DATA_CONST.__const: 0x2ba8
-  Functions: 1303
-  Symbols:   1744
-  CStrings:  543
+  __DATA_CONST.__const: 0x2c90
+  Functions: 1313
+  Symbols:   1760
+  CStrings:  545
 
Symbols:
+ _cc_cpu_feat_initialized
+ _cc_init_feature_bits
+ _ccec_sign_composite_msg_ws
+ _ccec_verify_composite_digest_ws
+ _ccec_verify_composite_msg_ws
+ _ccrsa_eme_pkcs1v15_decode_internal_ws
+ _ccrsa_sign_pkcs1v15_msg_blinded_ws
+ _ccrsa_verify_pkcs1v15_msg_ws
+ _ccsha384_vng_arm_hw_compress
+ _ccsha384_vng_arm_hw_di
+ _ccsha512_256_vng_arm_hw_compress
+ _ccsha512_256_vng_arm_hw_di
+ _ccsha512_vng_arm_hw_compress
+ _ccsha512_vng_arm_hw_di
+ _cpu_feature_bits
+ ccrsa_eme_pkcs1v15_decode.entropy
+ ccrsa_eme_pkcs1v15_decode.entropy_init
CStrings:
+ "SHA384_VNG_ARM_HW"
+ "SHA512_VNG_ARM_HW"

```

>  `com.apple.driver.AppleCallbackPowerSource`

```diff

-1730.0.0.0.2
-  __TEXT.__cstring: 0xf76
+1735.0.0.0.0
+  __TEXT.__cstring: 0xf8f
   __TEXT.__os_log: 0x76
-  __TEXT_EXEC.__text: 0x4c7c
+  __TEXT_EXEC.__text: 0x4cc4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd0
   __DATA.__common: 0x190
-  __DATA.__bss: 0x1408
+  __DATA.__bss: 0x1438
   __DATA_CONST.__auth_got: 0x150
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__mod_init_func: 0x10

   __DATA_CONST.__const: 0x1380
   __DATA_CONST.__kalloc_type: 0x80
   Functions: 63
-  Symbols:   670
-  CStrings:  235
+  Symbols:   672
+  CStrings:  237
 
Symbols:
+ __ZL24_kGGCalculatedMaxWRdcSym
+ __ZL29_kGGCalculatedNccPFilteredSym
CStrings:
+ "MaximumWRdc"
+ "NccpFiltered"

```

>  `com.apple.driver.ApplePMGR`

```diff

-1555.0.15.0.0
+1555.0.17.0.0
   __TEXT.__const: 0x258
   __TEXT.__cstring: 0xe858
-  __TEXT_EXEC.__text: 0x53bf0
+  __TEXT_EXEC.__text: 0x53bec
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x100
   __DATA.__common: 0x420
Symbols:
+ __ZZN28ApplePMGRFunctionISPRefClock27initWithTargetDataAndSymbolEP9IOServicePK6OSDataPK8OSSymbolE22kalloc_type_view_15385
+ __ZZN9ApplePMGR10_initPMPv2EvE21kalloc_type_view_9705
+ __ZZN9ApplePMGR10_initPMPv2EvE21kalloc_type_view_9778
+ __ZZN9ApplePMGR15_initGenericPTDEvE21kalloc_type_view_9659
+ __ZZN9ApplePMGR19_initPerfCountersV1EP9IOServiceE22kalloc_type_view_16737
+ __ZZN9ApplePMGR19_initPerfCountersV1EP9IOServiceE22kalloc_type_view_16765
+ __ZZN9ApplePMGR19_initPerfCountersV1EP9IOServiceE22kalloc_type_view_16808
+ __ZZN9ApplePMGR19_initPerfCountersV1EP9IOServiceE22kalloc_type_view_16872
+ __ZZN9ApplePMGR19_initPerfCountersV2EP9IOServiceE22kalloc_type_view_17512
+ __ZZN9ApplePMGR19_initPerfCountersV2EP9IOServiceE22kalloc_type_view_17529
+ __ZZN9ApplePMGR32_pmpWriteDashBoardSetDeviceStateEtjjE22kalloc_type_view_10025
- __ZZN28ApplePMGRFunctionISPRefClock27initWithTargetDataAndSymbolEP9IOServicePK6OSDataPK8OSSymbolE22kalloc_type_view_15386
- __ZZN9ApplePMGR10_initPMPv2EvE21kalloc_type_view_9706
- __ZZN9ApplePMGR10_initPMPv2EvE21kalloc_type_view_9779
- __ZZN9ApplePMGR15_initGenericPTDEvE21kalloc_type_view_9660
- __ZZN9ApplePMGR19_initPerfCountersV1EP9IOServiceE22kalloc_type_view_16738
- __ZZN9ApplePMGR19_initPerfCountersV1EP9IOServiceE22kalloc_type_view_16766
- __ZZN9ApplePMGR19_initPerfCountersV1EP9IOServiceE22kalloc_type_view_16809
- __ZZN9ApplePMGR19_initPerfCountersV1EP9IOServiceE22kalloc_type_view_16873
- __ZZN9ApplePMGR19_initPerfCountersV2EP9IOServiceE22kalloc_type_view_17513
- __ZZN9ApplePMGR19_initPerfCountersV2EP9IOServiceE22kalloc_type_view_17530
- __ZZN9ApplePMGR32_pmpWriteDashBoardSetDeviceStateEtjjE22kalloc_type_view_10026

```

>  `com.apple.AGXG15G`

```diff

-320.18.0.0.0
+320.23.0.0.0
   __TEXT.__const: 0x31fc
-  __TEXT.__cstring: 0xcd7f
+  __TEXT.__cstring: 0xcd83
   __TEXT.__os_log: 0x32f
-  __TEXT_EXEC.__text: 0xb35b8
+  __TEXT_EXEC.__text: 0xb3bb8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1408
   __DATA.__common: 0x10
Symbols:
+ _GLOBAL__D_a.3607
+ _GLOBAL__D_a.4023
+ _GLOBAL__D_a.4441
+ _GLOBAL__D_a.4859
+ _GLOBAL__D_a.5184
+ _GLOBAL__D_a.5268
+ _GLOBAL__D_a.5354
+ _GLOBAL__D_a.5510
+ _ZL18gAGXSetGameModeKey.3226
+ _ZL18gAGXSetGameModeKey.3287
+ _ZL18gAGXSetGameModeKey.3604
+ _ZL18gAGXSetGameModeKey.4020
+ _ZL18gAGXSetGameModeKey.4438
+ _ZL18gAGXSetGameModeKey.4856
+ _ZL18gAGXSetGameModeKey.5181
+ _ZL18gAGXSetGameModeKey.5265
+ _ZL18gAGXSetGameModeKey.5351
+ _ZL18gAGXSetGameModeKey.5375
+ _ZL18gAGXSetGameModeKey.5390
+ _ZL18gAGXSetGameModeKey.5505
+ _ZL26gAGXGetCLPCStandbyCountKey.3218
+ _ZL26gAGXGetCLPCStandbyCountKey.3279
+ _ZL26gAGXGetCLPCStandbyCountKey.3567
+ _ZL26gAGXGetCLPCStandbyCountKey.4012
+ _ZL26gAGXGetCLPCStandbyCountKey.4430
+ _ZL26gAGXGetCLPCStandbyCountKey.4848
+ _ZL26gAGXGetCLPCStandbyCountKey.5173
+ _ZL26gAGXGetCLPCStandbyCountKey.5257
+ _ZL26gAGXGetCLPCStandbyCountKey.5343
+ _ZL26gAGXGetCLPCStandbyCountKey.5367
+ _ZL26gAGXGetCLPCStandbyCountKey.5382
+ _ZL26gAGXGetCLPCStandbyCountKey.5497
+ _ZL28gAGXGetCLPCPerfCtrlTargetKey.3224
+ _ZL28gAGXGetCLPCPerfCtrlTargetKey.3285
+ _ZL28gAGXGetCLPCPerfCtrlTargetKey.3570
+ _ZL28gAGXGetCLPCPerfCtrlTargetKey.4018
+ _ZL28gAGXGetCLPCPerfCtrlTargetKey.4436
+ _ZL28gAGXGetCLPCPerfCtrlTargetKey.4854
+ _ZL28gAGXGetCLPCPerfCtrlTargetKey.5179
+ _ZL28gAGXGetCLPCPerfCtrlTargetKey.5263
+ _ZL28gAGXGetCLPCPerfCtrlTargetKey.5349
+ _ZL28gAGXGetCLPCPerfCtrlTargetKey.5373
+ _ZL28gAGXGetCLPCPerfCtrlTargetKey.5388
+ _ZL28gAGXGetCLPCPerfCtrlTargetKey.5503
+ _ZL29gAGXGetCLPCStandbyDurationKey.3220
+ _ZL29gAGXGetCLPCStandbyDurationKey.3281
+ _ZL29gAGXGetCLPCStandbyDurationKey.3568
+ _ZL29gAGXGetCLPCStandbyDurationKey.4014
+ _ZL29gAGXGetCLPCStandbyDurationKey.4432
+ _ZL29gAGXGetCLPCStandbyDurationKey.4850
+ _ZL29gAGXGetCLPCStandbyDurationKey.5175
+ _ZL29gAGXGetCLPCStandbyDurationKey.5259
+ _ZL29gAGXGetCLPCStandbyDurationKey.5345
+ _ZL29gAGXGetCLPCStandbyDurationKey.5369
+ _ZL29gAGXGetCLPCStandbyDurationKey.5384
+ _ZL29gAGXGetCLPCStandbyDurationKey.5499
+ _ZL31gAGXGetCLPCPowerSamplePeriodKey.3222
+ _ZL31gAGXGetCLPCPowerSamplePeriodKey.3283
+ _ZL31gAGXGetCLPCPowerSamplePeriodKey.3569
+ _ZL31gAGXGetCLPCPowerSamplePeriodKey.4016
+ _ZL31gAGXGetCLPCPowerSamplePeriodKey.4434
+ _ZL31gAGXGetCLPCPowerSamplePeriodKey.4852
+ _ZL31gAGXGetCLPCPowerSamplePeriodKey.5177
+ _ZL31gAGXGetCLPCPowerSamplePeriodKey.5261
+ _ZL31gAGXGetCLPCPowerSamplePeriodKey.5347
+ _ZL31gAGXGetCLPCPowerSamplePeriodKey.5371
+ _ZL31gAGXGetCLPCPowerSamplePeriodKey.5386
+ _ZL31gAGXGetCLPCPowerSamplePeriodKey.5501
+ _ZL34gAGXGetFilteredGPUPowerFunctionKey.3214
+ _ZL34gAGXGetFilteredGPUPowerFunctionKey.3275
+ _ZL34gAGXGetFilteredGPUPowerFunctionKey.3597
+ _ZL34gAGXGetFilteredGPUPowerFunctionKey.4008
+ _ZL34gAGXGetFilteredGPUPowerFunctionKey.4426
+ _ZL34gAGXGetFilteredGPUPowerFunctionKey.4844
+ _ZL34gAGXGetFilteredGPUPowerFunctionKey.5169
+ _ZL34gAGXGetFilteredGPUPowerFunctionKey.5253
+ _ZL34gAGXGetFilteredGPUPowerFunctionKey.5339
+ _ZL34gAGXGetFilteredGPUPowerFunctionKey.5363
+ _ZL34gAGXGetFilteredGPUPowerFunctionKey.5378
+ _ZL34gAGXGetFilteredGPUPowerFunctionKey.5493
+ _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.3216
+ _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.3277
+ _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.3427
+ _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.4010
+ _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.4428
+ _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.4846
+ _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.5171
+ _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.5255
+ _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.5341
+ _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.5365
+ _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.5380
+ _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.5495
+ _ZN10AGXChannel24encodeInvalidatePDSCacheE19_AGFIDataMasterType.5459
+ _ZN10AGXChannel28encodeInvalidateUSCInstCacheEv.5461
+ _ZN10AGXChannel32markCommandsSubmittedToAccelRingEv.5458
+ _ZN10AGXChannel34unmarkCommandsSubmittedToAccelRingEv.5457
+ _ZN10AGXChannel36encodeInvalidateDynamicConstantCacheEv.5460
+ _ZN11AGXFirmware14getGPUMaxPowerEv.3430
+ _ZN11AGXFirmware14getGPUMaxPowerEv.3970
+ _ZN11AGXFirmware14getGPUMaxPowerEv.4388
+ _ZN11AGXFirmware14getGPUMaxPowerEv.4806
+ _ZN11AGXFirmware17isWaitingForKicksEv.3432
+ _ZN11AGXFirmware17isWaitingForKicksEv.3972
+ _ZN11AGXFirmware17isWaitingForKicksEv.4390
+ _ZN11AGXFirmware17isWaitingForKicksEv.4808
+ _ZN11AGXFirmware18setPropertyQoSModeEyy.3410
+ _ZN11AGXFirmware18setPropertyQoSModeEyy.3958
+ _ZN11AGXFirmware18setPropertyQoSModeEyy.4375
+ _ZN11AGXFirmware18setPropertyQoSModeEyy.4793
+ _ZN11AGXFirmware21isFirmwareInitialisedEv.3433
+ _ZN11AGXFirmware21isFirmwareInitialisedEv.3973
+ _ZN11AGXFirmware21isFirmwareInitialisedEv.4391
+ _ZN11AGXFirmware21isFirmwareInitialisedEv.4809
+ _ZN11AGXFirmware22isFirmwareColdBootDoneEv.3566
+ _ZN11AGXFirmware22isFirmwareColdBootDoneEv.3976
+ _ZN11AGXFirmware22isFirmwareColdBootDoneEv.4394
+ _ZN11AGXFirmware22isFirmwareColdBootDoneEv.4812
+ _ZN11AGXFirmware24completeFirmwareColdBootE16AGFIFirmwareRole.3565
+ _ZN11AGXFirmware24completeFirmwareColdBootE16AGFIFirmwareRole.3975
+ _ZN11AGXFirmware24completeFirmwareColdBootE16AGFIFirmwareRole.4393
+ _ZN11AGXFirmware24completeFirmwareColdBootE16AGFIFirmwareRole.4811
+ _ZN11AGXFirmware24updateMRCConfigOverridesEP12OSDictionary.3367
+ _ZN11AGXFirmware24updateMRCConfigOverridesEP12OSDictionary.3943
+ _ZN11AGXFirmware24updateMRCConfigOverridesEP12OSDictionary.4360
+ _ZN11AGXFirmware24updateMRCConfigOverridesEP12OSDictionary.4778
+ _ZN11AGXFirmware26getUVWarnCounterDictionaryEv.3425
+ _ZN11AGXFirmware26getUVWarnCounterDictionaryEv.3964
+ _ZN11AGXFirmware26getUVWarnCounterDictionaryEv.4381
+ _ZN11AGXFirmware26getUVWarnCounterDictionaryEv.4799
+ _ZN11AGXFirmware26resetKSMDynamicPowerGatingEv.3400
+ _ZN11AGXFirmware26resetKSMDynamicPowerGatingEv.3956
+ _ZN11AGXFirmware26resetKSMDynamicPowerGatingEv.4373
+ _ZN11AGXFirmware26resetKSMDynamicPowerGatingEv.4791
+ _ZN11AGXFirmware31snapshotInspectionCriticalStateEv.3434
+ _ZN11AGXFirmware31snapshotInspectionCriticalStateEv.3974
+ _ZN11AGXFirmware31snapshotInspectionCriticalStateEv.4392
+ _ZN11AGXFirmware31snapshotInspectionCriticalStateEv.4810
+ _ZN11AGXFirmware33setKSMDynamicPowerGatingOverridesEP33AGFKSMDynamicPowerGatingOverrides.3401
+ _ZN11AGXFirmware33setKSMDynamicPowerGatingOverridesEP33AGFKSMDynamicPowerGatingOverrides.3957
+ _ZN11AGXFirmware33setKSMDynamicPowerGatingOverridesEP33AGFKSMDynamicPowerGatingOverrides.4374
+ _ZN11AGXFirmware33setKSMDynamicPowerGatingOverridesEP33AGFKSMDynamicPowerGatingOverrides.4792
+ _ZN11AGXFirmware37updateDeadlineAwareControllerOverrideEP12OSDictionary.3393
+ _ZN11AGXFirmware37updateDeadlineAwareControllerOverrideEP12OSDictionary.3944
+ _ZN11AGXFirmware37updateDeadlineAwareControllerOverrideEP12OSDictionary.4361
+ _ZN11AGXFirmware37updateDeadlineAwareControllerOverrideEP12OSDictionary.4779
+ _ZN14AGXAccelerator14enableGameModeEb.6038
+ _ZN14AGXAccelerator14isPIOSupportedEv.6061
+ _ZN14AGXAccelerator15forceIPPBarrierE12AGXWalkOrderj.6052
+ _ZN14AGXAccelerator15getDPEACWinInfoEP13AGFDPEPPTInfoty.6027
+ _ZN14AGXAccelerator15getSamplePeriodEv.5993
+ _ZN14AGXAccelerator15updateG9GConfigEj.6043
+ _ZN14AGXAccelerator16getDPEACDthrInfoEP13AGFDPEPPTInfoty.6028
+ _ZN14AGXAccelerator16getDPEDCDthrInfoEP13AGFDPEPPTInfoty.6024
+ _ZN14AGXAccelerator16getUMAesPageSizeER13AGXUMADescRecb.5997
+ _ZN14AGXAccelerator16postBootFirmwareEv.6053
+ _ZN14AGXAccelerator17getDPEACDshftInfoEP13AGFDPEPPTInfoty.6029
+ _ZN14AGXAccelerator17getDPEDCDshftInfoEP13AGFDPEPPTInfoty.6025
+ _ZN14AGXAccelerator17isHWDSIDAvailableEh.5988
+ _ZN14AGXAccelerator18getDPEImaxDthrInfoEP13AGFDPEPPTInfoty.6022
+ _ZN14AGXAccelerator18getDPEImaxWin1InfoEP13AGFDPEPPTInfoty.6020
+ _ZN14AGXAccelerator18getDPEImaxWin2InfoEP13AGFDPEPPTInfoty.6019
+ _ZN14AGXAccelerator18setPropertyQoSModeEP12OSDictionaryP8OSObject.5965
+ _ZN14AGXAccelerator19computeDPEPPTValuesEP19AGFDPEPPTConfigDataf.6007
+ _ZN14AGXAccelerator19getDPEImaxDshftInfoEP13AGFDPEPPTInfoty.6023
+ _ZN14AGXAccelerator19getKernelGMMUTablesEv.5967
+ _ZN14AGXAccelerator19handleSAPTInterruptEv.6039
+ _ZN14AGXAccelerator19isPowerManagedInAGXEv.6060
+ _ZN14AGXAccelerator19isQOSBillingEnabledEv.5996
+ _ZN14AGXAccelerator19setKernelGMMUTablesEPv.5968
+ _ZN14AGXAccelerator19supportsMTRSecurityEv.6058
+ _ZN14AGXAccelerator20getDPEImaxBudgetInfoEP13AGFDPEPPTInfoty.6021
+ _ZN14AGXAccelerator20isMTRScalerSupportedEv.6059
+ _ZN14AGXAccelerator21getGPUMemoryThresholdEv.6037
+ _ZN14AGXAccelerator21getGPUPhysicalAddressEv.6057
+ _ZN14AGXAccelerator21populateCSCAllocationEv.5991
+ _ZN14AGXAccelerator21use16kPageSizeDefaultEv.6044
+ _ZN14AGXAccelerator22getDPEDCCompCondBudgetEP13AGFDPEPPTInfoty.6010
+ _ZN14AGXAccelerator22getDPEDCCondBudgetInfoEP13AGFDPEPPTInfoty.6026
+ _ZN14AGXAccelerator22getDPEImaxPredWin1InfoEP13AGFDPEPPTInfoty.6017
+ _ZN14AGXAccelerator22getDPEImaxPredWin2InfoEP13AGFDPEPPTInfoty.6016
+ _ZN14AGXAccelerator23getDPEImaxReactWin1InfoEP13AGFDPEPPTInfoty.6013
+ _ZN14AGXAccelerator23getDPEImaxReactWin2InfoEP13AGFDPEPPTInfoty.6012
+ _ZN14AGXAccelerator23getUMAMaxActiveGTPKicksEv.6002
+ _ZN14AGXAccelerator23populateStaticPowerDataEv.6036
+ _ZN14AGXAccelerator24getDPEDCCompDshiftThreshEP13AGFDPEPPTInfoty.6009
+ _ZN14AGXAccelerator24getDPEImaxPredBudgetInfoEP13AGFDPEPPTInfoty.6018
+ _ZN14AGXAccelerator24getFenceBufferGPUAddressEv.6003
+ _ZN14AGXAccelerator24getFenderPhysicalAddressEv.6056
+ _ZN14AGXAccelerator24getPMGRServiceDictionaryEv.6031
+ _ZN14AGXAccelerator24getSamplePeriodAICClocksEv.5992
+ _ZN14AGXAccelerator24getUVWarnPhysicalAddressEv.6055
+ _ZN14AGXAccelerator24halNewSpillBufferManagerEv.6048
+ _ZN14AGXAccelerator24updateImaxReactiveBudgetEv.6006
+ _ZN14AGXAccelerator25getDPECurrentDefaultLimitEv.6008
+ _ZN14AGXAccelerator25getDPEImaxReactBudgetInfoEP13AGFDPEPPTInfoty.6014
+ _ZN14AGXAccelerator25halGetDefaultMcacheWritesEv.5987
+ _ZN14AGXAccelerator25halWaitForFenderPowerGateEv.5969
+ _ZN14AGXAccelerator26halGetSmallestUMABlockSizeEv.5999
+ _ZN14AGXAccelerator26populateSRAMPowerScaleDataEv.6034
+ _ZN14AGXAccelerator28getDPEImaxPredTrigThreshInfoEP13AGFDPEPPTInfoty.6015
+ _ZN14AGXAccelerator28setPropertyDefaultQoSTargetsEP12OSDictionaryP8OSObject.5963
+ _ZN14AGXAccelerator29getBorderColorTableGPUAddressEv.6004
+ _ZN14AGXAccelerator29getDPEImaxReactTrigThreshInfoEP13AGFDPEPPTInfoty.6011
+ _ZN14AGXAccelerator29supportsOptimizedUMASharedMinEv.5998
+ _ZN14AGXAccelerator30getUMAMaxActiveCDMKicksPerMGPUEb.6000
+ _ZN14AGXAccelerator30getUMAMaxActiveFRGKicksPerMGPUEb.6001
+ _ZN14AGXAccelerator30populateDPEAdjustmentCoEffDataEv.6035
+ _ZN14AGXAccelerator30populateDPELeakageUpdateConfigEP25AGXDPELeakageUpdateConfig.6032
+ _ZN14AGXAccelerator30populateDefaultSRAMVoltageDataER13PerfStateInfoILj16ELj8EE.6033
+ _ZN14AGXAccelerator33populateMaximumPerformancePowerCSEv.5989
+ _ZN14AGXAccelerator34updateImaxReactiveTriggerThresholdEv.6005
+ _ZN14AGXAccelerator47setPropertyNoiseSuppressionGPUIdlePowerOffStateEP12OSDictionaryP8OSObject.5964
+ _ZN14AGXArmFirmware11isGFXBootedEPy.3953
+ _ZN14AGXArmFirmware11isGFXBootedEPy.4370
+ _ZN14AGXArmFirmware11isGFXBootedEPy.4788
+ _ZN14AGXArmFirmware12setInitReg32Etjh.3968
+ _ZN14AGXArmFirmware12setInitReg32Etjh.4386
+ _ZN14AGXArmFirmware12setInitReg32Etjh.4804
+ _ZN14AGXArmFirmware12setInitReg64Etyh.3967
+ _ZN14AGXArmFirmware12setInitReg64Etyh.4385
+ _ZN14AGXArmFirmware12setInitReg64Etyh.4803
+ _ZN14AGXArmFirmware14setInitReg64PAEtyjh.3966
+ _ZN14AGXArmFirmware14setInitReg64PAEtyjh.4384
+ _ZN14AGXArmFirmware14setInitReg64PAEtyjh.4802
+ _ZN14AGXArmFirmware19getFSTPOverrideMaskE19_AGFIDataMasterTypeb.3946
+ _ZN14AGXArmFirmware19getFSTPOverrideMaskE19_AGFIDataMasterTypeb.4363
+ _ZN14AGXArmFirmware19getFSTPOverrideMaskE19_AGFIDataMasterTypeb.4781
+ _ZN14AGXArmFirmware21initSoftFaultSettingsEb.3949
+ _ZN14AGXArmFirmware21initSoftFaultSettingsEb.4366
+ _ZN14AGXArmFirmware21initSoftFaultSettingsEb.4784
+ _ZN14AGXArmFirmware21isFSTPOverrideEnabledEv.3947
+ _ZN14AGXArmFirmware21isFSTPOverrideEnabledEv.4364
+ _ZN14AGXArmFirmware21isFSTPOverrideEnabledEv.4782
+ _ZN14AGXArmFirmware22getDPEImaxCurrentLimitEv.3971
+ _ZN14AGXArmFirmware22getDPEImaxCurrentLimitEv.4389
+ _ZN14AGXArmFirmware22getDPEImaxCurrentLimitEv.4807
+ _ZN14AGXArmFirmware23updateSoftFaultSettingsEb.3948
+ _ZN14AGXArmFirmware23updateSoftFaultSettingsEb.4365
+ _ZN14AGXArmFirmware23updateSoftFaultSettingsEb.4783
+ _ZN14AGXArmFirmware24isForceGTPDiscardEnabledEv.3942
+ _ZN14AGXArmFirmware24isForceGTPDiscardEnabledEv.4359
+ _ZN14AGXArmFirmware24isForceGTPDiscardEnabledEv.4777
+ _ZN14AGXArmFirmware24resetFirmwareForRecoveryEv.3963
+ _ZN14AGXArmFirmware24resetFirmwareForRecoveryEv.4380
+ _ZN14AGXArmFirmware24resetFirmwareForRecoveryEv.4798
+ _ZN14AGXArmFirmware27setCommandSubmissionEnabledEb.3969
+ _ZN14AGXArmFirmware27setCommandSubmissionEnabledEb.4387
+ _ZN14AGXArmFirmware27setCommandSubmissionEnabledEb.4805
+ _ZN14AGXArmFirmware28getDefaultCLKillTimeoutLimitEv.3960
+ _ZN14AGXArmFirmware28getDefaultCLKillTimeoutLimitEv.4377
+ _ZN14AGXArmFirmware28getDefaultCLKillTimeoutLimitEv.4795
+ _ZN14AGXArmFirmware29getMCacheRegistersBaseAddressEv.3952
+ _ZN14AGXArmFirmware29getMCacheRegistersBaseAddressEv.4369
+ _ZN14AGXArmFirmware29getMCacheRegistersBaseAddressEv.4787
+ _ZN14AGXArmFirmware32getDefaultCDMBackoffTimeoutLimitEv.3959
+ _ZN14AGXArmFirmware32getDefaultCDMBackoffTimeoutLimitEv.4376
+ _ZN14AGXArmFirmware32getDefaultCDMBackoffTimeoutLimitEv.4794
+ _ZN14AGXArmFirmware34clearOutstandingFirmwareInterruptsEv.3945
+ _ZN14AGXArmFirmware34clearOutstandingFirmwareInterruptsEv.4362
+ _ZN14AGXArmFirmware34clearOutstandingFirmwareInterruptsEv.4780
+ _ZN14AGXArmFirmware35isSystemSleepNotificationInProgressEv.3954
+ _ZN14AGXArmFirmware35isSystemSleepNotificationInProgressEv.4371
+ _ZN14AGXArmFirmware35isSystemSleepNotificationInProgressEv.4789
+ _ZN14AGXArmFirmware36setSystemSleepNotificationInProgressEb.3955
+ _ZN14AGXArmFirmware36setSystemSleepNotificationInProgressEb.4372
+ _ZN14AGXArmFirmware36setSystemSleepNotificationInProgressEb.4790
+ _ZN14AGXArmFirmware37getDefaultCLContextSwitchTimeoutLimitEv.3962
+ _ZN14AGXArmFirmware37getDefaultCLContextSwitchTimeoutLimitEv.4379
+ _ZN14AGXArmFirmware37getDefaultCLContextSwitchTimeoutLimitEv.4797
+ _ZN14AGXArmFirmware39getDefaultRelaxedCLContextSwitchTimeoutEv.3961
+ _ZN14AGXArmFirmware39getDefaultRelaxedCLContextSwitchTimeoutEv.4378
+ _ZN14AGXArmFirmware39getDefaultRelaxedCLContextSwitchTimeoutEv.4796
+ _ZN20AGXFamilyAccelerator21parsePerfStateMapRegsEv.5960
+ _ZN9os_detail21panic_trapping_policy4trapEPKc.3051
+ _ZN9os_detail21panic_trapping_policy4trapEPKc.3411
+ _ZNK11AGXFirmware14getFWPageShiftEv.3428
+ _ZNK12AGX3DChannel15getGuiltyDMTypeEv.5456
+ _ZNK14AGXAccelerator20getChecksumRegistersER22_AGXSChecksumRegisters.6054
+ _ZNK14AGXAccelerator22halMCacheApertureSetupEPvhiy18_AGXWriteRangeSizet.5990
+ _ZNK14AGXAccelerator23halGetMaxFencesShiftMaxEv.5976
+ _ZNK14AGXAccelerator23halGetMaxFencesShiftMinEv.5977
+ _ZNK14AGXAccelerator23halGetSegmentIdRangeMaxEv.5982
+ _ZNK14AGXAccelerator23halGetSegmentIdRangeMinEv.5983
+ _ZNK14AGXAccelerator24halIsSmartidleOffEnabledEv.6047
+ _ZNK14AGXAccelerator25halGetMaxFencesShiftResetEv.5978
+ _ZNK14AGXAccelerator25halGetSegmentIdRangeResetEv.5984
+ _ZNK14AGXAccelerator26halGetMergeLastCmdBufEventEv.6030
+ _ZNK14AGXAccelerator32halGetDefaultSplHeuristicEnabledEv.5985
+ _ZNK14AGXAccelerator33halGetComplexPrimThreshAlignShiftEv.5975
+ _ZNK14AGXAccelerator34halGetComplexPrimThreshShiftCapMaxEv.5972
+ _ZNK14AGXAccelerator34halGetComplexPrimThreshShiftCapMinEv.5973
+ _ZNK14AGXAccelerator35halGetDefaultParameterBufferSizeMaxEy.5986
+ _ZNK14AGXAccelerator36halGetComplexPrimThreshShiftCapResetEv.5974
+ _ZNK14AGXAccelerator41halGetGtpScalingSegmentIdRangeMaxSegmentsEv.5981
+ _ZNK14AGXAccelerator43halGetDefaultParameterBufferSizeMaxOverrideEv.5979
+ _ZNK14AGXAccelerator43halGetDefaultParameterBufferSizeMinOverrideEv.5980
+ _ZNK14AGXAccelerator47getPropertyNoiseSuppressionGPUIdlePowerOffStateEv.5966
+ _ZNK14AGXArmFirmware30isFenderPowerManagementEnabledEv.3965
+ _ZNK14AGXArmFirmware30isFenderPowerManagementEnabledEv.4382
+ _ZNK14AGXArmFirmware30isFenderPowerManagementEnabledEv.4800
+ _ZNK14AGXArmFirmware31getConsistentGPUPerfStatePStateEv.3950
+ _ZNK14AGXArmFirmware31getConsistentGPUPerfStatePStateEv.4367
+ _ZNK14AGXArmFirmware31getConsistentGPUPerfStatePStateEv.4785
+ _ZNK14AGXArmFirmware31isConsistentGPUPerfStateEnabledEv.3951
+ _ZNK14AGXArmFirmware31isConsistentGPUPerfStateEnabledEv.4368
+ _ZNK14AGXArmFirmware31isConsistentGPUPerfStateEnabledEv.4786
+ _ZNK27AGXArmFirmwareChinookCommon14getFWPageShiftEv.4383
+ _ZNK27AGXArmFirmwareChinookCommon14getFWPageShiftEv.4801
+ __ZZN10AGXChannel4freeEvE20kalloc_type_view_338
+ __ZZN10AGXChannel4initEPK15AGXCommandQueueP12AGXWorkQueueiiy19_AGFIDataMasterTypeE20kalloc_type_view_104
+ __ZZN10AGXChannel4initEPK15AGXCommandQueueP12AGXWorkQueueiiy19_AGFIDataMasterTypeE20kalloc_type_view_273
+ __block_descriptor_tmp.3431
+ __block_descriptor_tmp.5356
- _GLOBAL__D_a.3609
- _GLOBAL__D_a.4025
- _GLOBAL__D_a.4443
- _GLOBAL__D_a.4861
- _GLOBAL__D_a.5186
- _GLOBAL__D_a.5270
- _GLOBAL__D_a.5356
- _GLOBAL__D_a.5512
- _ZL18gAGXSetGameModeKey.3227
- _ZL18gAGXSetGameModeKey.3289
- _ZL18gAGXSetGameModeKey.3606
- _ZL18gAGXSetGameModeKey.4022
- _ZL18gAGXSetGameModeKey.4440
- _ZL18gAGXSetGameModeKey.4858
- _ZL18gAGXSetGameModeKey.5183
- _ZL18gAGXSetGameModeKey.5267
- _ZL18gAGXSetGameModeKey.5353
- _ZL18gAGXSetGameModeKey.5377
- _ZL18gAGXSetGameModeKey.5392
- _ZL18gAGXSetGameModeKey.5507
- _ZL26gAGXGetCLPCStandbyCountKey.3219
- _ZL26gAGXGetCLPCStandbyCountKey.3281
- _ZL26gAGXGetCLPCStandbyCountKey.3569
- _ZL26gAGXGetCLPCStandbyCountKey.4014
- _ZL26gAGXGetCLPCStandbyCountKey.4432
- _ZL26gAGXGetCLPCStandbyCountKey.4850
- _ZL26gAGXGetCLPCStandbyCountKey.5175
- _ZL26gAGXGetCLPCStandbyCountKey.5259
- _ZL26gAGXGetCLPCStandbyCountKey.5345
- _ZL26gAGXGetCLPCStandbyCountKey.5369
- _ZL26gAGXGetCLPCStandbyCountKey.5384
- _ZL26gAGXGetCLPCStandbyCountKey.5499
- _ZL28gAGXGetCLPCPerfCtrlTargetKey.3225
- _ZL28gAGXGetCLPCPerfCtrlTargetKey.3287
- _ZL28gAGXGetCLPCPerfCtrlTargetKey.3572
- _ZL28gAGXGetCLPCPerfCtrlTargetKey.4020
- _ZL28gAGXGetCLPCPerfCtrlTargetKey.4438
- _ZL28gAGXGetCLPCPerfCtrlTargetKey.4856
- _ZL28gAGXGetCLPCPerfCtrlTargetKey.5181
- _ZL28gAGXGetCLPCPerfCtrlTargetKey.5265
- _ZL28gAGXGetCLPCPerfCtrlTargetKey.5351
- _ZL28gAGXGetCLPCPerfCtrlTargetKey.5375
- _ZL28gAGXGetCLPCPerfCtrlTargetKey.5390
- _ZL28gAGXGetCLPCPerfCtrlTargetKey.5505
- _ZL29gAGXGetCLPCStandbyDurationKey.3221
- _ZL29gAGXGetCLPCStandbyDurationKey.3283
- _ZL29gAGXGetCLPCStandbyDurationKey.3570
- _ZL29gAGXGetCLPCStandbyDurationKey.4016
- _ZL29gAGXGetCLPCStandbyDurationKey.4434
- _ZL29gAGXGetCLPCStandbyDurationKey.4852
- _ZL29gAGXGetCLPCStandbyDurationKey.5177
- _ZL29gAGXGetCLPCStandbyDurationKey.5261
- _ZL29gAGXGetCLPCStandbyDurationKey.5347
- _ZL29gAGXGetCLPCStandbyDurationKey.5371
- _ZL29gAGXGetCLPCStandbyDurationKey.5386
- _ZL29gAGXGetCLPCStandbyDurationKey.5501
- _ZL31gAGXGetCLPCPowerSamplePeriodKey.3223
- _ZL31gAGXGetCLPCPowerSamplePeriodKey.3285
- _ZL31gAGXGetCLPCPowerSamplePeriodKey.3571
- _ZL31gAGXGetCLPCPowerSamplePeriodKey.4018
- _ZL31gAGXGetCLPCPowerSamplePeriodKey.4436
- _ZL31gAGXGetCLPCPowerSamplePeriodKey.4854
- _ZL31gAGXGetCLPCPowerSamplePeriodKey.5179
- _ZL31gAGXGetCLPCPowerSamplePeriodKey.5263
- _ZL31gAGXGetCLPCPowerSamplePeriodKey.5349
- _ZL31gAGXGetCLPCPowerSamplePeriodKey.5373
- _ZL31gAGXGetCLPCPowerSamplePeriodKey.5388
- _ZL31gAGXGetCLPCPowerSamplePeriodKey.5503
- _ZL34gAGXGetFilteredGPUPowerFunctionKey.3215
- _ZL34gAGXGetFilteredGPUPowerFunctionKey.3277
- _ZL34gAGXGetFilteredGPUPowerFunctionKey.3599
- _ZL34gAGXGetFilteredGPUPowerFunctionKey.4010
- _ZL34gAGXGetFilteredGPUPowerFunctionKey.4428
- _ZL34gAGXGetFilteredGPUPowerFunctionKey.4846
- _ZL34gAGXGetFilteredGPUPowerFunctionKey.5171
- _ZL34gAGXGetFilteredGPUPowerFunctionKey.5255
- _ZL34gAGXGetFilteredGPUPowerFunctionKey.5341
- _ZL34gAGXGetFilteredGPUPowerFunctionKey.5365
- _ZL34gAGXGetFilteredGPUPowerFunctionKey.5380
- _ZL34gAGXGetFilteredGPUPowerFunctionKey.5495
- _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.3217
- _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.3279
- _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.3429
- _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.4012
- _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.4430
- _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.4848
- _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.5173
- _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.5257
- _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.5343
- _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.5367
- _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.5382
- _ZL35gAGXGetCLPCDynamicSplitRatioDictKey.5497
- _ZN10AGXChannel24encodeInvalidatePDSCacheE19_AGFIDataMasterType.5461
- _ZN10AGXChannel28encodeInvalidateUSCInstCacheEv.5463
- _ZN10AGXChannel32markCommandsSubmittedToAccelRingEv.5460
- _ZN10AGXChannel34unmarkCommandsSubmittedToAccelRingEv.5459
- _ZN10AGXChannel36encodeInvalidateDynamicConstantCacheEv.5462
- _ZN11AGXFirmware14getGPUMaxPowerEv.3432
- _ZN11AGXFirmware14getGPUMaxPowerEv.3972
- _ZN11AGXFirmware14getGPUMaxPowerEv.4390
- _ZN11AGXFirmware14getGPUMaxPowerEv.4808
- _ZN11AGXFirmware17isWaitingForKicksEv.3434
- _ZN11AGXFirmware17isWaitingForKicksEv.3974
- _ZN11AGXFirmware17isWaitingForKicksEv.4392
- _ZN11AGXFirmware17isWaitingForKicksEv.4810
- _ZN11AGXFirmware18setPropertyQoSModeEyy.3412
- _ZN11AGXFirmware18setPropertyQoSModeEyy.3960
- _ZN11AGXFirmware18setPropertyQoSModeEyy.4377
- _ZN11AGXFirmware18setPropertyQoSModeEyy.4795
- _ZN11AGXFirmware21isFirmwareInitialisedEv.3435
- _ZN11AGXFirmware21isFirmwareInitialisedEv.3975
- _ZN11AGXFirmware21isFirmwareInitialisedEv.4393
- _ZN11AGXFirmware21isFirmwareInitialisedEv.4811
- _ZN11AGXFirmware22isFirmwareColdBootDoneEv.3568
- _ZN11AGXFirmware22isFirmwareColdBootDoneEv.3978
- _ZN11AGXFirmware22isFirmwareColdBootDoneEv.4396
- _ZN11AGXFirmware22isFirmwareColdBootDoneEv.4814
- _ZN11AGXFirmware24completeFirmwareColdBootE16AGFIFirmwareRole.3567
- _ZN11AGXFirmware24completeFirmwareColdBootE16AGFIFirmwareRole.3977
- _ZN11AGXFirmware24completeFirmwareColdBootE16AGFIFirmwareRole.4395
- _ZN11AGXFirmware24completeFirmwareColdBootE16AGFIFirmwareRole.4813
- _ZN11AGXFirmware24updateMRCConfigOverridesEP12OSDictionary.3369
- _ZN11AGXFirmware24updateMRCConfigOverridesEP12OSDictionary.3945
- _ZN11AGXFirmware24updateMRCConfigOverridesEP12OSDictionary.4362
- _ZN11AGXFirmware24updateMRCConfigOverridesEP12OSDictionary.4780
- _ZN11AGXFirmware26getUVWarnCounterDictionaryEv.3427
- _ZN11AGXFirmware26getUVWarnCounterDictionaryEv.3966
- _ZN11AGXFirmware26getUVWarnCounterDictionaryEv.4383
- _ZN11AGXFirmware26getUVWarnCounterDictionaryEv.4801
- _ZN11AGXFirmware26resetKSMDynamicPowerGatingEv.3402
- _ZN11AGXFirmware26resetKSMDynamicPowerGatingEv.3958
- _ZN11AGXFirmware26resetKSMDynamicPowerGatingEv.4375
- _ZN11AGXFirmware26resetKSMDynamicPowerGatingEv.4793
- _ZN11AGXFirmware31snapshotInspectionCriticalStateEv.3436
- _ZN11AGXFirmware31snapshotInspectionCriticalStateEv.3976
- _ZN11AGXFirmware31snapshotInspectionCriticalStateEv.4394
- _ZN11AGXFirmware31snapshotInspectionCriticalStateEv.4812
- _ZN11AGXFirmware33setKSMDynamicPowerGatingOverridesEP33AGFKSMDynamicPowerGatingOverrides.3403
- _ZN11AGXFirmware33setKSMDynamicPowerGatingOverridesEP33AGFKSMDynamicPowerGatingOverrides.3959
- _ZN11AGXFirmware33setKSMDynamicPowerGatingOverridesEP33AGFKSMDynamicPowerGatingOverrides.4376
- _ZN11AGXFirmware33setKSMDynamicPowerGatingOverridesEP33AGFKSMDynamicPowerGatingOverrides.4794
- _ZN11AGXFirmware37updateDeadlineAwareControllerOverrideEP12OSDictionary.3395
- _ZN11AGXFirmware37updateDeadlineAwareControllerOverrideEP12OSDictionary.3946
- _ZN11AGXFirmware37updateDeadlineAwareControllerOverrideEP12OSDictionary.4363
- _ZN11AGXFirmware37updateDeadlineAwareControllerOverrideEP12OSDictionary.4781
- _ZN14AGXAccelerator14enableGameModeEb.6040
- _ZN14AGXAccelerator14isPIOSupportedEv.6063
- _ZN14AGXAccelerator15forceIPPBarrierE12AGXWalkOrderj.6054
- _ZN14AGXAccelerator15getDPEACWinInfoEP13AGFDPEPPTInfoty.6029
- _ZN14AGXAccelerator15getSamplePeriodEv.5995
- _ZN14AGXAccelerator15updateG9GConfigEj.6045
- _ZN14AGXAccelerator16getDPEACDthrInfoEP13AGFDPEPPTInfoty.6030
- _ZN14AGXAccelerator16getDPEDCDthrInfoEP13AGFDPEPPTInfoty.6026
- _ZN14AGXAccelerator16getUMAesPageSizeER13AGXUMADescRecb.5999
- _ZN14AGXAccelerator16postBootFirmwareEv.6055
- _ZN14AGXAccelerator17getDPEACDshftInfoEP13AGFDPEPPTInfoty.6031
- _ZN14AGXAccelerator17getDPEDCDshftInfoEP13AGFDPEPPTInfoty.6027
- _ZN14AGXAccelerator17isHWDSIDAvailableEh.5990
- _ZN14AGXAccelerator18getDPEImaxDthrInfoEP13AGFDPEPPTInfoty.6024
- _ZN14AGXAccelerator18getDPEImaxWin1InfoEP13AGFDPEPPTInfoty.6022
- _ZN14AGXAccelerator18getDPEImaxWin2InfoEP13AGFDPEPPTInfoty.6021
- _ZN14AGXAccelerator18setPropertyQoSModeEP12OSDictionaryP8OSObject.5967
- _ZN14AGXAccelerator19computeDPEPPTValuesEP19AGFDPEPPTConfigDataf.6009
- _ZN14AGXAccelerator19getDPEImaxDshftInfoEP13AGFDPEPPTInfoty.6025
- _ZN14AGXAccelerator19getKernelGMMUTablesEv.5969
- _ZN14AGXAccelerator19handleSAPTInterruptEv.6041
- _ZN14AGXAccelerator19isPowerManagedInAGXEv.6062
- _ZN14AGXAccelerator19isQOSBillingEnabledEv.5998
- _ZN14AGXAccelerator19setKernelGMMUTablesEPv.5970
- _ZN14AGXAccelerator19supportsMTRSecurityEv.6060
- _ZN14AGXAccelerator20getDPEImaxBudgetInfoEP13AGFDPEPPTInfoty.6023
- _ZN14AGXAccelerator20isMTRScalerSupportedEv.6061
- _ZN14AGXAccelerator21getGPUMemoryThresholdEv.6039
- _ZN14AGXAccelerator21getGPUPhysicalAddressEv.6059
- _ZN14AGXAccelerator21populateCSCAllocationEv.5993
- _ZN14AGXAccelerator21use16kPageSizeDefaultEv.6046
- _ZN14AGXAccelerator22getDPEDCCompCondBudgetEP13AGFDPEPPTInfoty.6012
- _ZN14AGXAccelerator22getDPEDCCondBudgetInfoEP13AGFDPEPPTInfoty.6028
- _ZN14AGXAccelerator22getDPEImaxPredWin1InfoEP13AGFDPEPPTInfoty.6019
- _ZN14AGXAccelerator22getDPEImaxPredWin2InfoEP13AGFDPEPPTInfoty.6018
- _ZN14AGXAccelerator23getDPEImaxReactWin1InfoEP13AGFDPEPPTInfoty.6015
- _ZN14AGXAccelerator23getDPEImaxReactWin2InfoEP13AGFDPEPPTInfoty.6014
- _ZN14AGXAccelerator23getUMAMaxActiveGTPKicksEv.6004
- _ZN14AGXAccelerator23populateStaticPowerDataEv.6038
- _ZN14AGXAccelerator24getDPEDCCompDshiftThreshEP13AGFDPEPPTInfoty.6011
- _ZN14AGXAccelerator24getDPEImaxPredBudgetInfoEP13AGFDPEPPTInfoty.6020
- _ZN14AGXAccelerator24getFenceBufferGPUAddressEv.6005
- _ZN14AGXAccelerator24getFenderPhysicalAddressEv.6058
- _ZN14AGXAccelerator24getPMGRServiceDictionaryEv.6033
- _ZN14AGXAccelerator24getSamplePeriodAICClocksEv.5994
- _ZN14AGXAccelerator24getUVWarnPhysicalAddressEv.6057
- _ZN14AGXAccelerator24halNewSpillBufferManagerEv.6050
- _ZN14AGXAccelerator24updateImaxReactiveBudgetEv.6008
- _ZN14AGXAccelerator25getDPECurrentDefaultLimitEv.6010
- _ZN14AGXAccelerator25getDPEImaxReactBudgetInfoEP13AGFDPEPPTInfoty.6016
- _ZN14AGXAccelerator25halGetDefaultMcacheWritesEv.5989
- _ZN14AGXAccelerator25halWaitForFenderPowerGateEv.5971
- _ZN14AGXAccelerator26halGetSmallestUMABlockSizeEv.6001
- _ZN14AGXAccelerator26populateSRAMPowerScaleDataEv.6036
- _ZN14AGXAccelerator28getDPEImaxPredTrigThreshInfoEP13AGFDPEPPTInfoty.6017
- _ZN14AGXAccelerator28setPropertyDefaultQoSTargetsEP12OSDictionaryP8OSObject.5965
- _ZN14AGXAccelerator29getBorderColorTableGPUAddressEv.6006
- _ZN14AGXAccelerator29getDPEImaxReactTrigThreshInfoEP13AGFDPEPPTInfoty.6013
- _ZN14AGXAccelerator29supportsOptimizedUMASharedMinEv.6000
- _ZN14AGXAccelerator30getUMAMaxActiveCDMKicksPerMGPUEb.6002
- _ZN14AGXAccelerator30getUMAMaxActiveFRGKicksPerMGPUEb.6003
- _ZN14AGXAccelerator30populateDPEAdjustmentCoEffDataEv.6037
- _ZN14AGXAccelerator30populateDPELeakageUpdateConfigEP25AGXDPELeakageUpdateConfig.6034
- _ZN14AGXAccelerator30populateDefaultSRAMVoltageDataER13PerfStateInfoILj16ELj8EE.6035
- _ZN14AGXAccelerator33populateMaximumPerformancePowerCSEv.5991
- _ZN14AGXAccelerator34updateImaxReactiveTriggerThresholdEv.6007
- _ZN14AGXAccelerator47setPropertyNoiseSuppressionGPUIdlePowerOffStateEP12OSDictionaryP8OSObject.5966
- _ZN14AGXArmFirmware11isGFXBootedEPy.3955
- _ZN14AGXArmFirmware11isGFXBootedEPy.4372
- _ZN14AGXArmFirmware11isGFXBootedEPy.4790
- _ZN14AGXArmFirmware12setInitReg32Etjh.3970
- _ZN14AGXArmFirmware12setInitReg32Etjh.4388
- _ZN14AGXArmFirmware12setInitReg32Etjh.4806
- _ZN14AGXArmFirmware12setInitReg64Etyh.3969
- _ZN14AGXArmFirmware12setInitReg64Etyh.4387
- _ZN14AGXArmFirmware12setInitReg64Etyh.4805
- _ZN14AGXArmFirmware14setInitReg64PAEtyjh.3968
- _ZN14AGXArmFirmware14setInitReg64PAEtyjh.4386
- _ZN14AGXArmFirmware14setInitReg64PAEtyjh.4804
- _ZN14AGXArmFirmware19getFSTPOverrideMaskE19_AGFIDataMasterTypeb.3948
- _ZN14AGXArmFirmware19getFSTPOverrideMaskE19_AGFIDataMasterTypeb.4365
- _ZN14AGXArmFirmware19getFSTPOverrideMaskE19_AGFIDataMasterTypeb.4783
- _ZN14AGXArmFirmware21initSoftFaultSettingsEb.3951
- _ZN14AGXArmFirmware21initSoftFaultSettingsEb.4368
- _ZN14AGXArmFirmware21initSoftFaultSettingsEb.4786
- _ZN14AGXArmFirmware21isFSTPOverrideEnabledEv.3949
- _ZN14AGXArmFirmware21isFSTPOverrideEnabledEv.4366
- _ZN14AGXArmFirmware21isFSTPOverrideEnabledEv.4784
- _ZN14AGXArmFirmware22getDPEImaxCurrentLimitEv.3973
- _ZN14AGXArmFirmware22getDPEImaxCurrentLimitEv.4391
- _ZN14AGXArmFirmware22getDPEImaxCurrentLimitEv.4809
- _ZN14AGXArmFirmware23updateSoftFaultSettingsEb.3950
- _ZN14AGXArmFirmware23updateSoftFaultSettingsEb.4367
- _ZN14AGXArmFirmware23updateSoftFaultSettingsEb.4785
- _ZN14AGXArmFirmware24isForceGTPDiscardEnabledEv.3944
- _ZN14AGXArmFirmware24isForceGTPDiscardEnabledEv.4361
- _ZN14AGXArmFirmware24isForceGTPDiscardEnabledEv.4779
- _ZN14AGXArmFirmware24resetFirmwareForRecoveryEv.3965
- _ZN14AGXArmFirmware24resetFirmwareForRecoveryEv.4382
- _ZN14AGXArmFirmware24resetFirmwareForRecoveryEv.4800
- _ZN14AGXArmFirmware27setCommandSubmissionEnabledEb.3971
- _ZN14AGXArmFirmware27setCommandSubmissionEnabledEb.4389
- _ZN14AGXArmFirmware27setCommandSubmissionEnabledEb.4807
- _ZN14AGXArmFirmware28getDefaultCLKillTimeoutLimitEv.3962
- _ZN14AGXArmFirmware28getDefaultCLKillTimeoutLimitEv.4379
- _ZN14AGXArmFirmware28getDefaultCLKillTimeoutLimitEv.4797
- _ZN14AGXArmFirmware29getMCacheRegistersBaseAddressEv.3954
- _ZN14AGXArmFirmware29getMCacheRegistersBaseAddressEv.4371
- _ZN14AGXArmFirmware29getMCacheRegistersBaseAddressEv.4789
- _ZN14AGXArmFirmware32getDefaultCDMBackoffTimeoutLimitEv.3961
- _ZN14AGXArmFirmware32getDefaultCDMBackoffTimeoutLimitEv.4378
- _ZN14AGXArmFirmware32getDefaultCDMBackoffTimeoutLimitEv.4796
- _ZN14AGXArmFirmware34clearOutstandingFirmwareInterruptsEv.3947
- _ZN14AGXArmFirmware34clearOutstandingFirmwareInterruptsEv.4364
- _ZN14AGXArmFirmware34clearOutstandingFirmwareInterruptsEv.4782
- _ZN14AGXArmFirmware35isSystemSleepNotificationInProgressEv.3956
- _ZN14AGXArmFirmware35isSystemSleepNotificationInProgressEv.4373
- _ZN14AGXArmFirmware35isSystemSleepNotificationInProgressEv.4791
- _ZN14AGXArmFirmware36setSystemSleepNotificationInProgressEb.3957
- _ZN14AGXArmFirmware36setSystemSleepNotificationInProgressEb.4374
- _ZN14AGXArmFirmware36setSystemSleepNotificationInProgressEb.4792
- _ZN14AGXArmFirmware37getDefaultCLContextSwitchTimeoutLimitEv.3964
- _ZN14AGXArmFirmware37getDefaultCLContextSwitchTimeoutLimitEv.4381
- _ZN14AGXArmFirmware37getDefaultCLContextSwitchTimeoutLimitEv.4799
- _ZN14AGXArmFirmware39getDefaultRelaxedCLContextSwitchTimeoutEv.3963
- _ZN14AGXArmFirmware39getDefaultRelaxedCLContextSwitchTimeoutEv.4380
- _ZN14AGXArmFirmware39getDefaultRelaxedCLContextSwitchTimeoutEv.4798
- _ZN20AGXFamilyAccelerator21parsePerfStateMapRegsEv.5962
- _ZN9os_detail21panic_trapping_policy4trapEPKc.3052
- _ZN9os_detail21panic_trapping_policy4trapEPKc.3413
- _ZNK11AGXFirmware14getFWPageShiftEv.3430
- _ZNK12AGX3DChannel15getGuiltyDMTypeEv.5458
- _ZNK14AGXAccelerator20getChecksumRegistersER22_AGXSChecksumRegisters.6056
- _ZNK14AGXAccelerator22halMCacheApertureSetupEPvhiy18_AGXWriteRangeSizet.5992
- _ZNK14AGXAccelerator23halGetMaxFencesShiftMaxEv.5978
- _ZNK14AGXAccelerator23halGetMaxFencesShiftMinEv.5979
- _ZNK14AGXAccelerator23halGetSegmentIdRangeMaxEv.5984
- _ZNK14AGXAccelerator23halGetSegmentIdRangeMinEv.5985
- _ZNK14AGXAccelerator24halIsSmartidleOffEnabledEv.6049
- _ZNK14AGXAccelerator25halGetMaxFencesShiftResetEv.5980
- _ZNK14AGXAccelerator25halGetSegmentIdRangeResetEv.5986
- _ZNK14AGXAccelerator26halGetMergeLastCmdBufEventEv.6032
- _ZNK14AGXAccelerator32halGetDefaultSplHeuristicEnabledEv.5987
- _ZNK14AGXAccelerator33halGetComplexPrimThreshAlignShiftEv.5977
- _ZNK14AGXAccelerator34halGetComplexPrimThreshShiftCapMaxEv.5974
- _ZNK14AGXAccelerator34halGetComplexPrimThreshShiftCapMinEv.5975
- _ZNK14AGXAccelerator35halGetDefaultParameterBufferSizeMaxEy.5988
- _ZNK14AGXAccelerator36halGetComplexPrimThreshShiftCapResetEv.5976
- _ZNK14AGXAccelerator41halGetGtpScalingSegmentIdRangeMaxSegmentsEv.5983
- _ZNK14AGXAccelerator43halGetDefaultParameterBufferSizeMaxOverrideEv.5981
- _ZNK14AGXAccelerator43halGetDefaultParameterBufferSizeMinOverrideEv.5982
- _ZNK14AGXAccelerator47getPropertyNoiseSuppressionGPUIdlePowerOffStateEv.5968
- _ZNK14AGXArmFirmware30isFenderPowerManagementEnabledEv.3967
- _ZNK14AGXArmFirmware30isFenderPowerManagementEnabledEv.4384
- _ZNK14AGXArmFirmware30isFenderPowerManagementEnabledEv.4802
- _ZNK14AGXArmFirmware31getConsistentGPUPerfStatePStateEv.3952
- _ZNK14AGXArmFirmware31getConsistentGPUPerfStatePStateEv.4369
- _ZNK14AGXArmFirmware31getConsistentGPUPerfStatePStateEv.4787
- _ZNK14AGXArmFirmware31isConsistentGPUPerfStateEnabledEv.3953
- _ZNK14AGXArmFirmware31isConsistentGPUPerfStateEnabledEv.4370
- _ZNK14AGXArmFirmware31isConsistentGPUPerfStateEnabledEv.4788
- _ZNK27AGXArmFirmwareChinookCommon14getFWPageShiftEv.4385
- _ZNK27AGXArmFirmwareChinookCommon14getFWPageShiftEv.4803
- __ZZN10AGXChannel4freeEvE20kalloc_type_view_334
- __ZZN10AGXChannel4initEPK15AGXCommandQueueP12AGXWorkQueueiiy19_AGFIDataMasterTypeE20kalloc_type_view_100
- __ZZN10AGXChannel4initEPK15AGXCommandQueueP12AGXWorkQueueiiy19_AGFIDataMasterTypeE20kalloc_type_view_269
- __block_descriptor_tmp.3433
- __block_descriptor_tmp.5358
CStrings:
+ "121111112112222122111111211222212211111121122221221222222222221122111111112222222211111212112121121211212112121121211212112121121211212112121121211212111111111222111222111222111222111222111222111222111222111222111222111222222211112212112121111111122222222221211222222222222222222222222222222222222222222222222222222222222222222222222121121122222222222222222222222222222222222222222222222222222222222222222111111221212222222221222221111122121222222222122222111112212122222222212222211111221212222222221222221111122121222222222122222111112212122222222212222211111222111111222111111222111111222111111222111111222111111222111111222111111222112111112211111111221122111111111111111111111111111111111112222222222222222221111112212122222222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111112222222"
+ "12112121112211222222222"
+ "1212222222222222222222111222122122222222222"
+ "Jul  1 2024 22:20:26"
- "1211111121122221221111112112222122111111211222212212222222222211221111111122222222111112121121211212112121121211212112121121211212112121121211212112121111111112221112221112221112221112221112221112221112221112221112221112222222111122121121211111111222222222212112222222222222222222222222222222222222222222222222222222222222222222222221211211222222222222222222222222222222222222222222222222222222222222222221111112212122222222212222211111221212222222221222221111122121222222222122222111112212122222222212222211111221212222222221222221111122121222222222122222111112221111112221111112221111112221111112221111112221111112221111112221111112221121111122111111112211221111111111111111111111111111111111222222222222222221111112212122222222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111112222222"
- "1211212111221122222222"
- "121222222222222222222211122212212222222222"
- "Jun 20 2024 20:41:37"

```

>  `com.apple.driver.AppleCredentialManager`

```diff

-758.0.14.0.0
-  __TEXT.__cstring: 0x168b9
+758.0.16.0.0
+  __TEXT.__cstring: 0x1692b
   __TEXT.__const: 0x378
-  __TEXT_EXEC.__text: 0x67724
+  __TEXT_EXEC.__text: 0x677e4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x34c1
   __DATA.__common: 0x1d8

   __DATA_CONST.__const: 0x2de8
   __DATA_CONST.__kalloc_type: 0x780
   __DATA_CONST.__kalloc_var: 0x1450
-  Functions: 1124
-  Symbols:   1849
-  CStrings:  2434
+  Functions: 1126
+  Symbols:   1851
+  CStrings:  2439
 
Symbols:
+ _ZN30ACMRestrictedModeKernelService19updateKeybagTrackerERNS_13KeybagTracker7TrackerEib.cold.1
+ __ZN30ACMRestrictedModeKernelService19searchKeybagTrackerERNS_13KeybagTracker7TrackerEi
+ __ZN30ACMRestrictedModeKernelService19updateKeybagTrackerERNS_13KeybagTracker7TrackerEib
- __ZN30ACMRestrictedModeKernelService25searchUnlockedUserKeybagsEi
CStrings:
+ "\"ACM: %s keybag=%d cannot be added, no space!\" @%s:%d"
+ "%s: %s: %s keybag=%d added.\n"
+ "%s: %s: %s keybag=%d already added.\n"
+ "%s: %s: %s keybag=%d cannot be added, no space!.\n"
+ "%s: %s: %s keybag=%d not found.\n"
+ "%s: %s: %s keybag=%d removed.\n"
+ "%s: %s: keybag=%d kbLockState=%s(%u) | useUserKeybag=%s unlocked=%u locked=%u => deviceLockState=%s(%u) was=%s(%u).\n"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/ACMKernelUtils.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManager.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManagerShared.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManagerUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMAccessoryCacheKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMBridgeKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMFirstResponderKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMKeybagKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMLockdownModeKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMPersistentStoreKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeAnalyticsKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CommonMem.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CommonTRMLegacy.h"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreAuthMethod.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreCmd.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreCred.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreCredSet.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreDER.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreEnv.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreExec.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CorePrague.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreReqAlgo.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreSEPControl.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreStorage.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreTRMAccCache.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreTRMMultiState.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreTimer.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreUserIntent.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreUtil.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CredUtil.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/Credentials.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/LibSerialization.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelLib.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
+ "12111111222212232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323231111111211111111112212222222222222222122222222222222222222222222222222222222"
+ "ACMRestrictedModeKernelService.cpp"
+ "Jul  1 2024, 22:03:18"
+ "L"
+ "U"
+ "cmd = (acm_command_t *)({ size_t sizeVal = (cmdSize); void *ptr = acm_mem_alloc_data(sizeVal); acm_mem_alloc_info(\"<data>\", ptr, sizeVal, \"/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c\", 22, __func__); ptr; })"
+ "updateKeybagTracker"
- "%s: %s: keybag=%d added (%u).\n"
- "%s: %s: keybag=%d already added (%u).\n"
- "%s: %s: keybag=%d cannot be added, no space! (%u).\n"
- "%s: %s: keybag=%d kbLockState=%s(%u) | users=%u(%u) lockingLastUser=%s | deviceLockState=%s(%u) was=%s(%u).\n"
- "%s: %s: keybag=%d not found (%u).\n"
- "%s: %s: keybag=%d removed (%u).\n"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelLib.cpp"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/ACMKernelUtils.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManager.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManagerShared.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManagerUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMAccessoryCacheKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMBridgeKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMFirstResponderKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMKeybagKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMLockdownModeKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMPersistentStoreKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeAnalyticsKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CommonMem.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CommonTRMLegacy.h"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreAuthMethod.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreCmd.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreCred.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreCredSet.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreDER.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreEnv.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreExec.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CorePrague.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreReqAlgo.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreSEPControl.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreStorage.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreTRMAccCache.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreTRMMultiState.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreTimer.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreUserIntent.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreUtil.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CredUtil.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/Credentials.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/LibSerialization.c"
- "12111111222212232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323231111111211111111112222222222222222222222222222222222222222222222222222222"
- "Jun 20 2024, 20:39:09"
- "cmd = (acm_command_t *)({ size_t sizeVal = (cmdSize); void *ptr = acm_mem_alloc_data(sizeVal); acm_mem_alloc_info(\"<data>\", ptr, sizeVal, \"/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c\", 22, __func__); ptr; })"

```

>  `com.apple.driver.AppleJPEGDriver`

```diff

-7.1.3.0.0
-  __TEXT.__os_log: 0xa0b6
-  __TEXT.__cstring: 0x2dc4
+7.1.4.0.0
+  __TEXT.__os_log: 0xa158
+  __TEXT.__cstring: 0x30ba
   __TEXT.__const: 0x3b26
-  __TEXT_EXEC.__text: 0x2be38
+  __TEXT_EXEC.__text: 0x2c694
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6f88
   __DATA.__common: 0x218
   __DATA.__bss: 0x1
-  __DATA_CONST.__auth_got: 0x340
+  __DATA_CONST.__auth_got: 0x348
   __DATA_CONST.__got: 0x98
   __DATA_CONST.__mod_init_func: 0x68
   __DATA_CONST.__mod_term_func: 0x68
   __DATA_CONST.__const: 0x35a0
   __DATA_CONST.__kalloc_type: 0x900
   Functions: 942
-  Symbols:   2096
-  CStrings:  244
+  Symbols:   2099
+  CStrings:  266
 
Symbols:
+ __ZN15AppleJPEGDriver15showRequestInfoEP11JpegRequest
+ __ZNK9IOSurface14getBytesPerRowEv
+ __ZZN15AppleJPEGDriver13newUserClientEP4taskPvjP12OSDictionaryPP12IOUserClientE11_os_log_fmt_2
+ __ZZN15AppleJPEGDriver15finish_io_gatedEP11JpegRequestijbE21kalloc_type_view_3502
+ __ZZN15AppleJPEGDriver15showRequestInfoEP11JpegRequestE11_os_log_fmt
+ __ZZN15AppleJPEGDriver15showRequestInfoEP11JpegRequestE11_os_log_fmt_0
+ __ZZN15AppleJPEGDriver15showRequestInfoEP11JpegRequestE11_os_log_fmt_1
+ __ZZN15AppleJPEGDriver17clientClosedGatedEP25AppleJPEGDriverUserClientE11_os_log_fmt
+ __ZZN15AppleJPEGHalV1418finishEncode_gatedEP11JpegRequestE11_os_log_fmt_4
- _ZN15AppleJPEGHalV1418finishEncode_gatedEP11JpegRequest.cold.5
- __ZZN15AppleJPEGDriver11jpegProfileEP11JpegRequestE11_os_log_fmt_0
- __ZZN15AppleJPEGDriver11jpegProfileEP11JpegRequestE11_os_log_fmt_1
- __ZZN15AppleJPEGDriver11jpegProfileEP11JpegRequestE11_os_log_fmt_2
- __ZZN15AppleJPEGDriver11jpegProfileEP11JpegRequestE11_os_log_fmt_3
- __ZZN15AppleJPEGDriver15finish_io_gatedEP11JpegRequestijbE21kalloc_type_view_3498
CStrings:
+ "22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111"
+ "format_400_10bit_linear_count"
+ "format_400_10bit_packed_count"
+ "format_400_10bit_tiled_count"
+ "format_400_12bit_linear_count"
+ "format_400_8bit_linear_count"
+ "format_400_8bit_tiled_count"
+ "format_420_10bit_linear_count"
+ "format_420_10bit_packed_count"
+ "format_420_10bit_tiled_count"
+ "format_420_12bit_linear_count"
+ "format_422_10bit_linear_count"
+ "format_422_10bit_packed_count"
+ "format_422_10bit_tiled_count"
+ "format_422_12bit_linear_count"
+ "format_444_10bit_linear_count"
+ "format_444_10bit_packed_count"
+ "format_444_10bit_tiled_count"
+ "format_444_12bit_linear_count"
+ "format_argb_10bit_linear_count"
+ "format_argb_10bit_tiled_count"
+ "format_argb_12bit_linear_count"
+ "format_argb_12bit_tiled_count"
+ "virtual void AppleJPEGDriver::clientClosedGated(AppleJPEGDriverUserClient *)"
+ "void AppleJPEGDriver::showRequestInfo(JpegRequest *)"
- "\"%s: codec=%d, encode AXI bus error triggered\\n\" @%s:%d"
- "222222222222222222222222222222222222222222222111"
- "Encode_V14.cpp"

```

>  `com.apple.driver.AppleTypeCPhy`

```diff

-239.0.0.0.0
+239.0.1.0.0
   __TEXT.__cstring: 0x1651
   __TEXT.__const: 0x24
   __TEXT.__os_log: 0x114c
-  __TEXT_EXEC.__text: 0x1296c
+  __TEXT_EXEC.__text: 0x129a4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xd8

   __DATA_CONST.__got: 0x78
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
-  __DATA_CONST.__const: 0x1b00
+  __DATA_CONST.__const: 0x1b10
   __DATA_CONST.__kalloc_type: 0x140
-  Functions: 243
-  Symbols:   727
+  Functions: 245
+  Symbols:   729
   CStrings:  160
 
Symbols:
+ __ZN13AppleTypeCPhy15supportS2RtoOffEv
+ __ZN13AppleTypeCPhy20shutdownACIOS2RtoOffENS_12tACIOPhyModeE

```

>  `com.apple.driver.AppleUIO`

```diff

-65.0.0.0.0
-  __TEXT.__cstring: 0x92e
+68.0.0.0.0
+  __TEXT.__cstring: 0x948
   __TEXT.__const: 0x10
-  __TEXT_EXEC.__text: 0x2ba0
+  __TEXT_EXEC.__text: 0x2b84
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0xf8
-  __DATA.__bss: 0x8
-  __DATA_CONST.__auth_got: 0x140
+  __DATA.__common: 0x100
+  __DATA.__bss: 0x4
+  __DATA_CONST.__auth_got: 0x150
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x2dd0
   __DATA_CONST.__kalloc_type: 0x140
   Functions: 121
-  Symbols:   542
+  Symbols:   544
   CStrings:  77
 
Symbols:
+ __ZN11AppleUIOMem17allocateUIOMemoryEv
+ __ZN11AppleUIOMem8fMemSizeE
+ _sysctlbyname
- __ZZL13getUIOMemSizevE7memSize
CStrings:
+ "22:05:08"
+ "Jul  1 2024"
+ "UIO: %-30s IOBufferMemoryDescriptor::withOptions(%d) failed\n"
+ "UIO: %-30s vmm_present=1 requesting contiguous memory\n"
+ "allocateUIOMemory"
+ "kern.hv_vmm_present"
- "20:38:40"
- "Jun 20 2024"
- "UIO: %-30s IOBufferMemoryDescriptor::inTaskWithPhysicalMask failed\n"
- "UIO: %-30s UIO memory size: %u\n"
- "copyUIOMemory"
- "getUIOMemSize"

```

>  `com.apple.filesystems.apfs`

```diff

-2309.0.0.0.3
+2310.0.0.0.0
   __TEXT.__const: 0x918
-  __TEXT.__cstring: 0x55946
-  __TEXT_EXEC.__text: 0x16f08c
+  __TEXT.__cstring: 0x5592b
+  __TEXT_EXEC.__text: 0x16efb0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd40
   __DATA.__bss: 0xac0

   __DATA_CONST.__const: 0x9190
   __DATA_CONST.__kalloc_type: 0x5f40
   __DATA_CONST.__kalloc_var: 0x30c0
-  Functions: 2631
-  Symbols:   4625
+  Functions: 2632
+  Symbols:   4626
   CStrings:  7352
 
Symbols:
+ _GLOBAL__D_a.1759
+ _ZN18APFSOSNumberAtomic10withNumberEx.1711
+ __ZZ21delta_teardown_threadPviE21kalloc_type_view_9999
+ __ZZL23apfs_keycache_operationPKh13apfs_key_typeiPP3cpxbE22kalloc_type_view_13069
+ __ZZL23apfs_keycache_operationPKh13apfs_key_typeiPP3cpxbE22kalloc_type_view_13079
+ __ZZL23apfs_keycache_operationPKh13apfs_key_typeiPP3cpxbE22kalloc_type_view_13100
+ __ZZN15AppleAPFSVolume15asyncCryptoReadEP18AppleAPFSContaineryyPyaybE21kalloc_type_view_8980
+ __ZZN15AppleAPFSVolume15asyncCryptoReadEP18AppleAPFSContaineryyPyaybE21kalloc_type_view_9067
+ __ZZN15AppleAPFSVolume27asyncCryptoReadFinishHelperEP24multikey_crypto_io_entryPyE21kalloc_type_view_9099
+ __ZZN18AppleAPFSContainer16lockerDataGetSetEb9klckr_ctxPhyP4taskE22kalloc_type_view_14629
+ __ZZN18AppleAPFSContainer16lockerDataGetSetEb9klckr_ctxPhyP4taskE22kalloc_type_view_14632
+ __ZZN18AppleAPFSContainer19deltaCreateTeardownEP18delta_create_ctx_tE21kalloc_type_view_7998
+ __ZZN18AppleAPFSContainer20deltaRestoreTeardownEP19delta_restore_ctx_tE21kalloc_type_view_8191
+ __ZZN18AppleAPFSContainer27containerGetKeyLockerRangesEjj9klckr_ctxyPjP20vol_keylocker_rangesE22kalloc_type_view_14450
+ __ZZN18AppleAPFSContainer27containerGetKeyLockerRangesEjj9klckr_ctxyPjP20vol_keylocker_rangesE22kalloc_type_view_14481
+ __ZZN19AppleAPFSUserClient24methodDeltaCreatePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11270
+ __ZZN19AppleAPFSUserClient24methodDeltaCreatePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11294
+ __ZZN19AppleAPFSUserClient25methodDeltaRestorePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11396
+ __ZZN19AppleAPFSUserClient25methodDeltaRestorePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11425
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10630
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10631
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10638
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10639
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10704
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10707
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10716
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10719
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10727
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10730
+ __ZZN19AppleAPFSUserClient4stopEP9IOServiceE22kalloc_type_view_10013
+ __ZZN19AppleAPFSUserClient4stopEP9IOServiceE22kalloc_type_view_10023
+ _apfs_is_task_dataless_manipulator_internal
+ _fs_add_xattr.kalloc_type_view_22578
+ _fs_add_xattr.kalloc_type_view_22584
+ _fs_add_xattr.kalloc_type_view_22587
+ _fs_add_xattr.kalloc_type_view_22641
+ _fs_add_xattr.kalloc_type_view_22642
+ apfs_drop_allocated_unwritten_ranges.kalloc_type_view_15821
+ apfs_drop_rangelist_entries.kalloc_type_view_8920
+ apfs_drop_rangelist_entry.kalloc_type_view_8867
+ apfs_find_gaps_in_rangelist.kalloc_type_view_11675
+ apfs_flush_allocated_unwritten_ranges.kalloc_type_view_13249
+ apfs_flush_allocated_unwritten_ranges.kalloc_type_view_13307
+ apfs_io_common.kalloc_type_view_18009
+ apfs_io_common.kalloc_type_view_18047
+ apfs_io_common.kalloc_type_view_18058
+ apfs_io_common.kalloc_type_view_18076
+ apfs_io_common.kalloc_type_view_18094
+ apfs_io_common.kalloc_type_view_18110
+ apfs_io_common.kalloc_type_view_18134
+ apfs_io_common.kalloc_type_view_18217
+ apfs_io_common.kalloc_type_view_18238
+ apfs_io_common.kalloc_type_view_18249
+ apfs_io_common.kalloc_type_view_18267
+ apfs_io_common.kalloc_type_view_18286
+ apfs_io_common.kalloc_type_view_18299
+ apfs_io_common.kalloc_type_view_18320
+ apfs_io_common.kalloc_type_view_18339
+ apfs_iodone.kalloc_type_view_17471
+ apfs_iodone.kalloc_type_view_17510
+ apfs_punch_out_ranges_in_fext.kalloc_type_view_20905
+ apfs_punch_out_ranges_in_fext.kalloc_type_view_20912
+ apfs_record_intention_to_allocate.kalloc_type_view_8802
+ apfs_release_all_reserved_space.kalloc_type_view_4440
+ apfs_release_io_context.kalloc_type_view_17709
+ apfs_release_io_context.kalloc_type_view_17718
+ apfs_trim_ranges_in_region.kalloc_type_view_16534
+ apfs_update_ranges_on_allocation.kalloc_type_view_16625
+ apfs_update_reserved_ranges.kalloc_type_view_21053
+ apfs_update_reserved_ranges.kalloc_type_view_21058
+ apfs_vnop_blockmap.kalloc_type_view_17045
+ apfs_vnop_blockmap.kalloc_type_view_17393
+ apfs_vnop_getattrlistbulk.kalloc_type_view_19082
+ apfs_vnop_getattrlistbulk.kalloc_type_view_19089
+ apfs_vnop_getattrlistbulk.kalloc_type_view_19156
+ apfs_vnop_getattrlistbulk.kalloc_type_view_19180
+ apfs_vnop_readdir.kalloc_type_view_15426
+ apfs_vnop_readdir.kalloc_type_view_15442
+ apfs_vnop_readdir.kalloc_type_view_15561
+ apfs_vnop_readdir.kalloc_type_view_15571
+ apfs_vnop_readdir.kalloc_type_view_15592
+ arle_alloc_pending_entry.kalloc_type_view_20485
+ change_crypto_id_prot_class.kalloc_type_view_9747
+ change_crypto_id_prot_class.kalloc_type_view_9813
+ clone_fexts_.kalloc_type_view_13851
+ clone_fexts_.kalloc_type_view_13864
+ clone_fexts_.kalloc_type_view_13922
+ create_sibling_link.kalloc_type_view_11291
+ create_sibling_link.kalloc_type_view_11307
+ dir_rec_alloc_with_hash.kalloc_type_view_10951
+ dir_rec_alloc_with_hash.kalloc_type_view_10957
+ dir_rec_alloc_with_hash.kalloc_type_view_10981
+ dump_extents_of_stream.kalloc_type_view_17929
+ ek_to_crypto_state.kalloc_type_view_32380
+ extent_evict_range.kalloc_type_view_25164
+ extent_evict_range.kalloc_type_view_25257
+ fext_collector.kalloc_type_view_13615
+ fext_collector.kalloc_type_view_13615.216
+ fext_collector.kalloc_type_view_13622
+ fext_collector_cleanup.kalloc_type_view_13597
+ fext_collector_reset.kalloc_type_view_13586
+ free_linkids.kalloc_type_view_11483
+ fs_get_xattr_in_snap.kalloc_type_view_22676
+ fs_get_xattr_in_snap.kalloc_type_view_22695
+ fs_init_bootcache_inodes_dstreams_info.kalloc_type_view_27074
+ fs_init_bootcache_inodes_dstreams_info.kalloc_type_view_27074.334
+ fs_iterate_snapshots.kalloc_type_view_26308
+ fs_iterate_snapshots.kalloc_type_view_26355
+ fs_map_file_offset_ext.kalloc_type_view_21465
+ fs_map_file_offset_ext.kalloc_type_view_21497
+ fs_map_file_offset_ext.kalloc_type_view_21535
+ fs_map_file_offset_ext.kalloc_type_view_21558
+ fs_remove_xattr_with_nstream_inode.kalloc_type_view_22790
+ fs_remove_xattr_with_nstream_inode.kalloc_type_view_22806
+ fs_remove_xattr_with_nstream_inode.kalloc_type_view_22827
+ fs_remove_xattr_with_nstream_inode.kalloc_type_view_22944
+ handle_fusion_debug.kalloc_type_view_10969
+ handle_fusion_debug.kalloc_type_view_10988
+ handle_snapshot_lookup.kalloc_type_view_12167
+ handle_xdstream_obj_id.kalloc_type_view_15726
+ handle_xdstream_obj_id.kalloc_type_view_15749
+ ier_alloc_tls.kalloc_type_view_27742
+ ier_alloc_tls.kalloc_type_view_27788
+ ier_free_tls.kalloc_type_view_27821
+ ier_ierso_free.kalloc_type_view_26910
+ ier_ierso_load.kalloc_type_view_26924
+ ier_ierso_new.kalloc_type_view_26619
+ ier_ierso_new.kalloc_type_view_26652
+ ier_ierto_free.kalloc_type_view_24514
+ ier_ierto_new.kalloc_type_view_24500
+ insert_linkid.kalloc_type_view_11431
+ legacy_get_ek.kalloc_type_view_33825
+ lookup_unfoldable_name_iterator.kalloc_type_view_17313
+ lookup_unfoldable_name_iterator.kalloc_type_view_17319
+ lookup_unfoldable_name_iterator.kalloc_type_view_17327
+ nx_fusion_find_lba_owner_checkForNewEntry.kalloc_type_view_10461
+ nx_fusion_find_lba_owner_cleanup.kalloc_type_view_10713
+ nx_fusion_find_lba_owner_scanInodes.kalloc_type_view_10656
+ nx_fusion_find_lba_owner_scanInodes.kalloc_type_view_10674
+ pfkur_pfkurso_free.kalloc_type_view_35974
+ pfkur_pfkurso_new.kalloc_type_view_34374
+ simple_remove_xattr.kalloc_type_view_22714
+ simple_remove_xattr.kalloc_type_view_22727
+ update_parent_xattr.kalloc_type_view_20286
+ update_parent_xattr.kalloc_type_view_20416
+ xattr_cloner.kalloc_type_view_16080
+ xattr_cloner.kalloc_type_view_16122
+ xattr_ek_to_crypto_state.kalloc_type_view_33010
- _GLOBAL__D_a.1760
- _ZN18APFSOSNumberAtomic10withNumberEx.1712
- __ZZ21delta_teardown_threadPviE21kalloc_type_view_9997
- __ZZL23apfs_keycache_operationPKh13apfs_key_typeiPP3cpxbE22kalloc_type_view_13067
- __ZZL23apfs_keycache_operationPKh13apfs_key_typeiPP3cpxbE22kalloc_type_view_13077
- __ZZL23apfs_keycache_operationPKh13apfs_key_typeiPP3cpxbE22kalloc_type_view_13098
- __ZZN15AppleAPFSVolume15asyncCryptoReadEP18AppleAPFSContaineryyPyaybE21kalloc_type_view_8978
- __ZZN15AppleAPFSVolume15asyncCryptoReadEP18AppleAPFSContaineryyPyaybE21kalloc_type_view_9065
- __ZZN15AppleAPFSVolume27asyncCryptoReadFinishHelperEP24multikey_crypto_io_entryPyE21kalloc_type_view_9097
- __ZZN18AppleAPFSContainer16lockerDataGetSetEb9klckr_ctxPhyP4taskE22kalloc_type_view_14627
- __ZZN18AppleAPFSContainer16lockerDataGetSetEb9klckr_ctxPhyP4taskE22kalloc_type_view_14630
- __ZZN18AppleAPFSContainer19deltaCreateTeardownEP18delta_create_ctx_tE21kalloc_type_view_7996
- __ZZN18AppleAPFSContainer20deltaRestoreTeardownEP19delta_restore_ctx_tE21kalloc_type_view_8189
- __ZZN18AppleAPFSContainer27containerGetKeyLockerRangesEjj9klckr_ctxyPjP20vol_keylocker_rangesE22kalloc_type_view_14448
- __ZZN18AppleAPFSContainer27containerGetKeyLockerRangesEjj9klckr_ctxyPjP20vol_keylocker_rangesE22kalloc_type_view_14479
- __ZZN19AppleAPFSUserClient24methodDeltaCreatePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11268
- __ZZN19AppleAPFSUserClient24methodDeltaCreatePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11292
- __ZZN19AppleAPFSUserClient25methodDeltaRestorePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11394
- __ZZN19AppleAPFSUserClient25methodDeltaRestorePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11423
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10627
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10628
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10635
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10636
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10702
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10705
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10714
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10717
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10725
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10728
- __ZZN19AppleAPFSUserClient4stopEP9IOServiceE22kalloc_type_view_10011
- __ZZN19AppleAPFSUserClient4stopEP9IOServiceE22kalloc_type_view_10021
- _fs_add_xattr.kalloc_type_view_22596
- _fs_add_xattr.kalloc_type_view_22602
- _fs_add_xattr.kalloc_type_view_22605
- _fs_add_xattr.kalloc_type_view_22659
- _fs_add_xattr.kalloc_type_view_22660
- apfs_drop_allocated_unwritten_ranges.kalloc_type_view_15833
- apfs_drop_rangelist_entries.kalloc_type_view_8932
- apfs_drop_rangelist_entry.kalloc_type_view_8879
- apfs_find_gaps_in_rangelist.kalloc_type_view_11687
- apfs_flush_allocated_unwritten_ranges.kalloc_type_view_13261
- apfs_flush_allocated_unwritten_ranges.kalloc_type_view_13319
- apfs_io_common.kalloc_type_view_18021
- apfs_io_common.kalloc_type_view_18059
- apfs_io_common.kalloc_type_view_18070
- apfs_io_common.kalloc_type_view_18088
- apfs_io_common.kalloc_type_view_18106
- apfs_io_common.kalloc_type_view_18122
- apfs_io_common.kalloc_type_view_18146
- apfs_io_common.kalloc_type_view_18229
- apfs_io_common.kalloc_type_view_18250
- apfs_io_common.kalloc_type_view_18261
- apfs_io_common.kalloc_type_view_18279
- apfs_io_common.kalloc_type_view_18298
- apfs_io_common.kalloc_type_view_18311
- apfs_io_common.kalloc_type_view_18344
- apfs_io_common.kalloc_type_view_18351
- apfs_iodone.kalloc_type_view_17483
- apfs_iodone.kalloc_type_view_17522
- apfs_punch_out_ranges_in_fext.kalloc_type_view_20923
- apfs_punch_out_ranges_in_fext.kalloc_type_view_20930
- apfs_record_intention_to_allocate.kalloc_type_view_8814
- apfs_release_all_reserved_space.kalloc_type_view_4448
- apfs_release_io_context.kalloc_type_view_17721
- apfs_release_io_context.kalloc_type_view_17730
- apfs_trim_ranges_in_region.kalloc_type_view_16546
- apfs_update_ranges_on_allocation.kalloc_type_view_16637
- apfs_update_reserved_ranges.kalloc_type_view_21071
- apfs_update_reserved_ranges.kalloc_type_view_21076
- apfs_vnop_blockmap.kalloc_type_view_17057
- apfs_vnop_blockmap.kalloc_type_view_17405
- apfs_vnop_getattrlistbulk.kalloc_type_view_19094
- apfs_vnop_getattrlistbulk.kalloc_type_view_19101
- apfs_vnop_getattrlistbulk.kalloc_type_view_19168
- apfs_vnop_getattrlistbulk.kalloc_type_view_19192
- apfs_vnop_readdir.kalloc_type_view_15438
- apfs_vnop_readdir.kalloc_type_view_15454
- apfs_vnop_readdir.kalloc_type_view_15573
- apfs_vnop_readdir.kalloc_type_view_15583
- apfs_vnop_readdir.kalloc_type_view_15604
- arle_alloc_pending_entry.kalloc_type_view_20503
- change_crypto_id_prot_class.kalloc_type_view_9767
- change_crypto_id_prot_class.kalloc_type_view_9833
- clone_fexts_.kalloc_type_view_13871
- clone_fexts_.kalloc_type_view_13884
- clone_fexts_.kalloc_type_view_13942
- create_sibling_link.kalloc_type_view_11311
- create_sibling_link.kalloc_type_view_11327
- dir_rec_alloc_with_hash.kalloc_type_view_10971
- dir_rec_alloc_with_hash.kalloc_type_view_10977
- dir_rec_alloc_with_hash.kalloc_type_view_11001
- dump_extents_of_stream.kalloc_type_view_17947
- ek_to_crypto_state.kalloc_type_view_32398
- extent_evict_range.kalloc_type_view_25182
- extent_evict_range.kalloc_type_view_25275
- fext_collector.kalloc_type_view_13635
- fext_collector.kalloc_type_view_13635.216
- fext_collector.kalloc_type_view_13642
- fext_collector_cleanup.kalloc_type_view_13617
- fext_collector_reset.kalloc_type_view_13606
- free_linkids.kalloc_type_view_11503
- fs_get_xattr_in_snap.kalloc_type_view_22694
- fs_get_xattr_in_snap.kalloc_type_view_22713
- fs_init_bootcache_inodes_dstreams_info.kalloc_type_view_27092
- fs_init_bootcache_inodes_dstreams_info.kalloc_type_view_27092.334
- fs_iterate_snapshots.kalloc_type_view_26326
- fs_iterate_snapshots.kalloc_type_view_26373
- fs_map_file_offset_ext.kalloc_type_view_21483
- fs_map_file_offset_ext.kalloc_type_view_21515
- fs_map_file_offset_ext.kalloc_type_view_21553
- fs_map_file_offset_ext.kalloc_type_view_21576
- fs_remove_xattr_with_nstream_inode.kalloc_type_view_22808
- fs_remove_xattr_with_nstream_inode.kalloc_type_view_22824
- fs_remove_xattr_with_nstream_inode.kalloc_type_view_22845
- fs_remove_xattr_with_nstream_inode.kalloc_type_view_22962
- handle_fusion_debug.kalloc_type_view_10970
- handle_fusion_debug.kalloc_type_view_10989
- handle_snapshot_lookup.kalloc_type_view_12168
- handle_xdstream_obj_id.kalloc_type_view_15731
- handle_xdstream_obj_id.kalloc_type_view_15754
- ier_alloc_tls.kalloc_type_view_27754
- ier_alloc_tls.kalloc_type_view_27800
- ier_free_tls.kalloc_type_view_27833
- ier_ierso_free.kalloc_type_view_26922
- ier_ierso_load.kalloc_type_view_26948
- ier_ierso_new.kalloc_type_view_26631
- ier_ierso_new.kalloc_type_view_26664
- ier_ierto_free.kalloc_type_view_24526
- ier_ierto_new.kalloc_type_view_24512
- insert_linkid.kalloc_type_view_11451
- legacy_get_ek.kalloc_type_view_33843
- lookup_unfoldable_name_iterator.kalloc_type_view_17333
- lookup_unfoldable_name_iterator.kalloc_type_view_17339
- lookup_unfoldable_name_iterator.kalloc_type_view_17347
- nx_fusion_find_lba_owner_checkForNewEntry.kalloc_type_view_10462
- nx_fusion_find_lba_owner_cleanup.kalloc_type_view_10714
- nx_fusion_find_lba_owner_scanInodes.kalloc_type_view_10657
- nx_fusion_find_lba_owner_scanInodes.kalloc_type_view_10675
- pfkur_pfkurso_free.kalloc_type_view_35986
- pfkur_pfkurso_new.kalloc_type_view_34386
- simple_remove_xattr.kalloc_type_view_22732
- simple_remove_xattr.kalloc_type_view_22745
- update_parent_xattr.kalloc_type_view_20298
- update_parent_xattr.kalloc_type_view_20428
- xattr_cloner.kalloc_type_view_16100
- xattr_cloner.kalloc_type_view_16142
- xattr_ek_to_crypto_state.kalloc_type_view_33028
CStrings:
+ "%s:%d: This operation needs dataless manipulation entitlement, detected in %s: %u\n"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/apfs/kext/apfs_filter.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/apfs/kext/apfs_ioctls.c"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/apfs/kext/apfs_rangelist.c"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/apfs/kext/apfs_vnops.c"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/apfs/nx/jobj.c"
+ "2024/07/03"
+ "20:04:18"
+ "20:04:19"
+ "2310"
+ "Jul  3 2024"
+ "apfs-2310"
+ "apfs_is_task_dataless_manipulator_internal"
- "%s:%d: %s dst (ino %llu) is a dataless file, and the caller is unprivileged\n"
- "%s:%d: %s file is dataless, and the caller is unprivileged\n"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/apfs/kext/apfs_filter.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/apfs/kext/apfs_ioctls.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/apfs/kext/apfs_rangelist.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/apfs/kext/apfs_vnops.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/apfs/nx/jobj.c"
- "2024/06/20"
- "20:32:41"
- "20:32:42"
- "2309.0.0.0.3"
- "Jun 20 2024"
- "apfs-2309.0.0.0.3"

```

>  `com.apple.iokit.IO80211Family`

```diff

-1302.61.0.0.0
-  __TEXT.__const: 0xf9f0
-  __TEXT.__cstring: 0x88c18
-  __TEXT.__os_log: 0x8c3d
-  __TEXT_EXEC.__text: 0x23950c
+1302.63.0.0.0
+  __TEXT.__const: 0xfa30
+  __TEXT.__cstring: 0x88d74
+  __TEXT.__os_log: 0x8d1b
+  __TEXT_EXEC.__text: 0x23a074
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4f48
   __DATA.__common: 0x2360

   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__mod_init_func: 0x518
   __DATA_CONST.__mod_term_func: 0x518
-  __DATA_CONST.__const: 0x36c50
+  __DATA_CONST.__const: 0x36ce0
   __DATA_CONST.__kalloc_type: 0x98c0
   __DATA_CONST.__kalloc_var: 0x7d0
-  Functions: 11991
-  Symbols:   18645
-  CStrings:  13381
+  Functions: 12004
+  Symbols:   18667
+  CStrings:  13394
 
Symbols:
+ .str.1183
+ .str.1184
+ __FUNCTION__._ZN15IO80211AWDLPeer13isPeerTypeSetE11rtgPeerType
+ __Z29apple80211getMANUFACTURE_DATEP23IO80211SkywalkInterfaceP27apple80211_manufacture_date
+ __Z29apple80211setMANUFACTURE_DATEP23IO80211SkywalkInterfaceP27apple80211_manufacture_date
+ __Z36apple80211getFIRST_BOOT_COUNTRY_CODEP23IO80211SkywalkInterfaceP28apple80211_country_code_data
+ __Z36apple80211setFIRST_BOOT_COUNTRY_CODEP23IO80211SkywalkInterfaceP28apple80211_country_code_data
+ __ZL19setMANUFACTURE_DATEP17IO80211ControllerP23IO80211SkywalkInterfaceP13apple80211req
+ __ZL21_logTimeCommandHelperPKcS0_jjyyy
+ __ZL26setFIRST_BOOT_COUNTRY_CODEP17IO80211ControllerP23IO80211SkywalkInterfaceP13apple80211req
+ __ZL27_logTimeIfThresholdExceededPKcS0_jjyyy
+ __ZN14WCLJoinRequest18addAssocCandidatesEP16WCLJoinCandidateP25apple80211AssocCandidates
+ __ZN15IO80211AWDLPeer13isPeerTypeSetE11rtgPeerType
+ __ZN16WCLJoinCandidate14updateTryCountEv
+ __ZN16WCLJoinCandidate16isRetryExhaustedEv
+ __ZN16WCLJoinCandidate18getCurrentTryCountEv
+ __ZN18IO80211ScanRequest15getMinTimestampEv
+ __ZN22IO80211AWDLPeerManager20getRemoteScreenStateEv
+ __ZN22WCLDeviceConfiguration29isLinkRecommendationSupportedEv
+ __ZNK16IO80211BSSBeacon12getTimestampEv
+ __ZZL10setNAN_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP13apple80211reqE21kalloc_type_view_1861
+ __ZZL10setNAN_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP13apple80211reqE21kalloc_type_view_1909
+ __ZZL11setAWDL_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP13apple80211reqE21kalloc_type_view_1085
+ __ZZL11setAWDL_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP13apple80211reqE21kalloc_type_view_1133
+ __ZZL16setRANGING_STARTP17IO80211ControllerP23IO80211SkywalkInterfaceP13apple80211reqE21kalloc_type_view_1518
+ __ZZL16setRANGING_STARTP17IO80211ControllerP23IO80211SkywalkInterfaceP13apple80211reqE21kalloc_type_view_1544
+ __ZZL17setRANGING_ENABLEP17IO80211ControllerP23IO80211SkywalkInterfaceP13apple80211reqE21kalloc_type_view_1488
+ __ZZL17setRANGING_ENABLEP17IO80211ControllerP23IO80211SkywalkInterfaceP13apple80211reqE21kalloc_type_view_1507
+ __ZZL21_logTimeCommandHelperPKcS0_jjyyyE11_os_log_fmt
+ __ZZL27_logTimeIfThresholdExceededPKcS0_jjyyyE11_os_log_fmt
+ __ZZN14WCLJoinRequest18initWCLJoinRequestEP21apple80211_assoc_dataP11CCLogStreamE20kalloc_type_view_704
+ __ZZN14WCLJoinRequest4freeEvE19kalloc_type_view_86
+ __ZZN14WCLScanRequest18initWCLScanRequestEP20apple80211_scan_dataR17scanRequestParamsE20kalloc_type_view_325
+ __ZZN16WCLBGScanManager15initWithOptionsEP13WCLControllerP16WCLBulletinBoardE20kalloc_type_view_121
+ __ZZN16WCLBGScanManager4freeEvE20kalloc_type_view_100
+ __ZZN16WCLJoinCandidate20initWCLJoinCandidateEP12WCLBSSBeaconE20kalloc_type_view_264
+ __ZZN16WCLJoinCandidate4freeEvE19kalloc_type_view_84
+ __ZZN18IO80211PeerManager17initWithInterfaceEP23IO80211VirtualInterfaceP23IO80211SkywalkInterfaceE21kalloc_type_view_1133
+ __ZZN18IO80211PeerManager4freeEvE21kalloc_type_view_1806
+ __ZZN18IO80211RoamProfile15initWithOptionsER25IO80211RoamProfileOptionsE20kalloc_type_view_115
+ __ZZN18IO80211RoamProfile4freeEvE20kalloc_type_view_100
+ __ZZN18IO80211ScanRequest22initIO80211ScanRequestEP20apple80211_scan_data8scanTypeE20kalloc_type_view_401
+ __ZZN20IO80211APIUserClient12initWithTaskEP4taskPvjP12OSDictionaryE20kalloc_type_view_152
+ __ZZN20IO80211APIUserClient4freeEvE20kalloc_type_view_479
+ __ZZN22IO80211AWDLPeerManager28freeAwdlPacketDescriptorPoolEvE22kalloc_type_view_37793
+ __ZZN22IO80211AWDLPeerManager28initAwdlPacketDescriptorPoolEjE22kalloc_type_view_37777
+ __ZZN22IO80211AWDLPeerManager33realTimeStatsGetSkywalkStatisticsEvE22kalloc_type_view_29388
+ __ZZN22IO80211AWDLPeerManager33realTimeStatsGetSkywalkStatisticsEvE22kalloc_type_view_29411
+ ___ZN20IO80211APIUserClient23reportUnentitledProcessEP12OSDictionary_block_invoke.28
+ ___ZN20IO80211APIUserClient23reportUnentitledProcessEP12OSDictionary_block_invoke_2.30
+ __block_descriptor_tmp.27
+ __block_descriptor_tmp.44
+ __block_descriptor_tmp.49
+ __block_descriptor_tmp.58
- __ZN14WCLJoinRequest18addAssocCandidatesEP16WCLJoinCandidateP25apple80211AssocCandidatesb
- __ZN16WCLJoinCandidate14updateTryCountEb
- __ZN16WCLJoinCandidate16isRetryExhaustedEb
- __ZN16WCLJoinCandidate18getCurrentTryCountEb
- __ZZL10setNAN_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP13apple80211reqE21kalloc_type_view_1851
- __ZZL10setNAN_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP13apple80211reqE21kalloc_type_view_1899
- __ZZL11setAWDL_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP13apple80211reqE21kalloc_type_view_1075
- __ZZL11setAWDL_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP13apple80211reqE21kalloc_type_view_1123
- __ZZL16setRANGING_STARTP17IO80211ControllerP23IO80211SkywalkInterfaceP13apple80211reqE21kalloc_type_view_1508
- __ZZL16setRANGING_STARTP17IO80211ControllerP23IO80211SkywalkInterfaceP13apple80211reqE21kalloc_type_view_1534
- __ZZL17setRANGING_ENABLEP17IO80211ControllerP23IO80211SkywalkInterfaceP13apple80211reqE21kalloc_type_view_1478
- __ZZL17setRANGING_ENABLEP17IO80211ControllerP23IO80211SkywalkInterfaceP13apple80211reqE21kalloc_type_view_1497
- __ZZN14WCLJoinRequest18initWCLJoinRequestEP21apple80211_assoc_dataP11CCLogStreamE20kalloc_type_view_760
- __ZZN14WCLJoinRequest4freeEvE19kalloc_type_view_87
- __ZZN14WCLScanRequest18initWCLScanRequestEP20apple80211_scan_dataR17scanRequestParamsE20kalloc_type_view_317
- __ZZN16WCLBGScanManager15initWithOptionsEP13WCLControllerP16WCLBulletinBoardE20kalloc_type_view_119
- __ZZN16WCLBGScanManager4freeEvE19kalloc_type_view_98
- __ZZN16WCLJoinCandidate20initWCLJoinCandidateEP12WCLBSSBeaconE20kalloc_type_view_292
- __ZZN16WCLJoinCandidate4freeEvE19kalloc_type_view_88
- __ZZN18IO80211PeerManager17initWithInterfaceEP23IO80211VirtualInterfaceP23IO80211SkywalkInterfaceE21kalloc_type_view_1127
- __ZZN18IO80211PeerManager4freeEvE21kalloc_type_view_1800
- __ZZN18IO80211RoamProfile15initWithOptionsER25IO80211RoamProfileOptionsE20kalloc_type_view_117
- __ZZN18IO80211RoamProfile4freeEvE20kalloc_type_view_102
- __ZZN18IO80211ScanRequest22initIO80211ScanRequestEP20apple80211_scan_data8scanTypeE20kalloc_type_view_395
- __ZZN20IO80211APIUserClient12initWithTaskEP4taskPvjP12OSDictionaryE20kalloc_type_view_116
- __ZZN20IO80211APIUserClient4freeEvE20kalloc_type_view_425
- __ZZN22IO80211AWDLPeerManager28freeAwdlPacketDescriptorPoolEvE22kalloc_type_view_37782
- __ZZN22IO80211AWDLPeerManager28initAwdlPacketDescriptorPoolEjE22kalloc_type_view_37766
- __ZZN22IO80211AWDLPeerManager33realTimeStatsGetSkywalkStatisticsEvE22kalloc_type_view_29378
- __ZZN22IO80211AWDLPeerManager33realTimeStatsGetSkywalkStatisticsEvE22kalloc_type_view_29401
- ___ZN20IO80211APIUserClient23reportUnentitledProcessEP12OSDictionary_block_invoke.27
- ___ZN20IO80211APIUserClient23reportUnentitledProcessEP12OSDictionary_block_invoke_2.29
- __block_descriptor_tmp.45
- __block_descriptor_tmp.55
CStrings:
+ " _runDriverCommandHelper"
+ " _runLargeBufferCommandHelper"
+ "\"IO80211_kexts-1302.63\""
+ "%s[%d]: peer type of %02X:%02X:%02X:%02X:%02X:%02X (%d) %s set \n"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLMulticastPeer.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeer.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PDataPathManager.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSteeringManager.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSupervisor.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211ServiceRequestDescriptor.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211DynamicBufferPool.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211StaticBufferPool.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211Controller.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211ControllerMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211GASFsm.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211InfraInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211InterfaceMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211PacketDescriptor.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211Peer.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211PeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211PeerMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211SkywalkInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211VirtualInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Infra/IO80211LinkRecovery.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Infra/IO80211ScanManager.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathInitiator.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathManager.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/DiscoveryEngine/IO80211NANDiscoveryEngine.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/Miscellaneous/IO80211NANUtils.c"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANDataInterfacePeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeer.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceDescriptor.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceManager.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/SynchronizationEngine/IO80211NANSyncEngine.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/UserClients/IO80211AsyncUserClientParameters.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211CommandQueue.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211FlowQueueDatabase.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.h"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_get_handlersLegacy.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlers.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlersLegacy.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211WCL/WCLDeauthDisassoc.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211WCL/WCLNearbyDeviceDiscoveryManager.cpp"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211WCL/WCLNetManager.cpp"
+ "1111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
+ "1111222222222222222222222222222222222111111111212122"
+ "11222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211"
+ "12222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111112"
+ "222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222121"
+ "APPLE80211_IOC_FIRST_BOOT_COUNTRY_CODE"
+ "APPLE80211_IOC_MANUFACTURE_DATE"
+ "IO80211_kexts-1302.63"
+ "Jul  2 2024 21:35:57"
+ "WCLBGScanManager Failed to init BssManager\n"
+ "[ik] %s@%d:Received BTM Request frame: Category Code = %d Action Code = %d dialogToken = %d Request Mode =(Pref Candidate List = %d Abridged = %d disassoc_Imminent = %d bss_term = %d ess_term = %d link_remove=%d) DisassocTimeout = %d Validity Interval = %d\n"
+ "[wcl] %s@%d:Exhausted join candidate list: Current index %d\n"
+ "[wcl] %s@%d:mode<%s>, allowSleepConnected<%d> ipv4<%d> ipv6<%d> assoc<%d> assocAdhoc<%d> AssociOS<%d> isSapUp<%d> lphs<%d> IPLeaseWakeEventScheduled<%d> denyListed<%d> lpasAllowed<%d> phInWoW<%d>\n"
+ "_logTimeCommandHelper"
+ "_logTimeIfThresholdExceeded"
+ "iouc.logThresholdMS"
+ "is"
+ "is not"
+ "isPeerTypeSet"
- "\"IO80211_kexts-1302.61\""
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLMulticastPeer.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeer.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PDataPathManager.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSteeringManager.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSupervisor.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211ServiceRequestDescriptor.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211DynamicBufferPool.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211StaticBufferPool.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211Controller.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211ControllerMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211GASFsm.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211InfraInterface.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211InterfaceMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211PacketDescriptor.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211Peer.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211PeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211PeerMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211SkywalkInterface.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211VirtualInterface.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Infra/IO80211LinkRecovery.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Infra/IO80211ScanManager.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathInitiator.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathManager.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/DiscoveryEngine/IO80211NANDiscoveryEngine.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/Miscellaneous/IO80211NANUtils.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANDataInterfacePeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeer.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceDescriptor.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceManager.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/SynchronizationEngine/IO80211NANSyncEngine.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/UserClients/IO80211AsyncUserClientParameters.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211CommandQueue.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211FlowQueueDatabase.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.h"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_get_handlersLegacy.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlers.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlersLegacy.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211WCL/WCLDeauthDisassoc.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211WCL/WCLNearbyDeviceDiscoveryManager.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211WCL/WCLNetManager.cpp"
- "111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
- "111122222222222222222222222222222222211111111121212"
- "112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211"
- "1222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111112"
- "22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222121"
- "IO80211_kexts-1302.61"
- "Jun 20 2024 20:32:12"
- "[ik] %s@%d:Received BTM Request frame: Category Code = %d Action Code = %d dialogToken = %d Request Mode =(Pref Candidate List = %d Abridged = %d disassoc_Imminent = %d bss_term = %d ess_term = %d) DisassocTimeout = %d Validity Interval = %d\n"
- "[wcl] %s@%d:mode<%s>, allowSleepConnected<%d> ipv4<%d> ipv6<%d> assoc<%d> assocAdhoc<%d> AssociOS<%d> isSapUp<%d> assocLPHSiOSHotspot<%d> IPLeaseWakeEventScheduled<%d> denyListed<%d> lpasAllowed<%d>\n"

```

>  `com.apple.iokit.IOGPUFamily`

```diff

-104.0.5.0.0
+104.0.6.0.0
   __TEXT.__cstring: 0x5706
   __TEXT.__os_log: 0x3c15
   __TEXT.__const: 0xd4
-  __TEXT_EXEC.__text: 0x3dc30
+  __TEXT_EXEC.__text: 0x3dd98
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4b0
   __DATA.__common: 0x7d0

```

>  `com.apple.kernel`

```diff

-11215.0.115.501.3
-  __TEXT.__const: 0x35d50
+11215.0.132.501.1
+  __TEXT.__const: 0x35d60
   __TEXT.__copyio_vectors: 0x120
-  __TEXT.__cstring: 0x99c78
+  __TEXT.__cstring: 0x99c4b
   __TEXT.__os_log: 0x26fe1
   __TEXT.__thread_starts: 0x0
   __TEXT.__eh_frame: 0x478

   __DATA_CONST.__kalloc_var: 0x8110
   __DATA_CONST.__brk_desc: 0x78
   __TEXT_EXEC.__hib_text: 0x3ab4
-  __TEXT_EXEC.__text: 0x8f79ec
+  __TEXT_EXEC.__text: 0x8f8e58
   __TEXT_EXEC.__commpage_text: 0x2dc
   __KLD.__text: 0x4ef0
   __PPLTEXT.__text: 0x2b6cc

   __LAST.__last: 0x0
   __PPLDATA.__data: 0x4c98
   __KLDDATA.__cstring: 0x71f
-  __KLDDATA.__const: 0x7f30
+  __KLDDATA.__const: 0x7f60
   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
   __DATA.__data: 0x203e1
   __DATA.__lock_grp: 0x15f10
   __DATA.__percpu: 0x30d8
-  __DATA.__common: 0x7b1a0
-  __DATA.__bss: 0x454b0
+  __DATA.__common: 0x7b1c0
+  __DATA.__bss: 0x455f0
   __HIBDATA.__data: 0x31
   __HIBDATA.__common: 0x120
-  __HIBDATA.__bss: 0x608
+  __HIBDATA.__bss: 0x618
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__init: 0x5bad0
-  __BOOTDATA.__init_entry_set: 0x113e8
+  __BOOTDATA.__init_entry_set: 0x11400
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0
   __PLK_TEXT_EXEC.__text: 0x0

   __PLK_DATA_CONST.__data: 0x0
   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
-  __LINKINFO.__symbolsets: 0x4ce0b
+  __LINKINFO.__symbolsets: 0x4ce8c
   __CTF.__ctf: 0x0
-  Functions: 22033
-  Symbols:   6651
+  Functions: 22040
+  Symbols:   6655
   CStrings:  19680
 
Symbols:
+ __vfs_smr
+ _apfs_smr
+ _smr_hash_init_empty
+ _smr_hash_is_empty_initialized
CStrings:
+ "%s : Number of retries for syncing first or last page reached %d\n"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Binaries/xnu/install/TempContent/Objects/EXPORT_HDRS/bsd/skywalk/nexus_common.h"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Binaries/xnu/install/TempContent/Objects/EXPORT_HDRS/bsd/skywalk/packet_common.h"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/dev/dtrace/dtrace.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kern_control.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kern_event.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kpi_mbuf.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kpi_socket.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kpi_socketfilter.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/socket_flows.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/subr_eventhandler.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/sys_domain.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/tracker.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_domain.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_mbuf.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_mbuf2.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_proto.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_socket.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_socket2.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_syscalls.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_usrreq.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/vsock_domain.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/bpf.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/classq/classq.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/classq/classq_fq_codel.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/classq/classq_subr.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/content_filter.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/dlil.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/droptap.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/flowadv.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_bond.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_bridge.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_fake.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_ipsec.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_llreach.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_loop.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_ports_used.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_redirect.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_utun.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_vlan.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/iptap.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/kpi_interface.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/mblist.h"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/nat464_utils.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/ndrv.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/necp_client.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/network_agent.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/ntstat.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/nwk_wq.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_if.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_ioctl.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_norm.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_pbuf.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_table.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktap.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktsched/pktsched.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktsched/pktsched_fq_codel.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktsched/pktsched_netem.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/route.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/rtsock.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/flow_divert.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/igmp.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_arp.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_mcast.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_pcb.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_proto.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_rmx.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_tclass.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_dummynet.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_encap.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_icmp.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_input.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_output.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/kpi_ipfilter.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mp_pcb.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mp_pcb.h"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mp_proto.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_opt.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_subr.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_timer.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_usrreq.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_var.h"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/raw_ip.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_cache.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_cubic.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_input.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_ledbat.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_output.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_prague.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_sack.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_subr.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_timer.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_usrreq.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/udp_usrreq.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ah_core.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ah_input.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ah_output.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_chachapoly.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_core.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_input.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_output.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_rijndael.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/frag6.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/icmp6.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_cga.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_ifattach.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_mcast.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_pcb.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_proto.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_rmx.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_src.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_forward.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_id.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_input.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_output.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ipsec.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ipsec.h"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/mld6.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_nbr.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_prproxy.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_rti.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_rtr.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_send.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/scope6.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/udp6_output.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netkey/key.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netkey/keysock.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel_kern.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel_ring.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel_syscalls.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/core/skywalk.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/lib/net_filter_event.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_arena.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_cache.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_cache_var.h"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_region.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_slab.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/namespace/flowidns.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/namespace/netns.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/namespace/protons.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_agg.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_classifier.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_entry.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_manager.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_owner.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_route.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_stats.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_track.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_var.h"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_classq.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_dp.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_ethernet.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_ip_frag.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_vp.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/nx_flowswitch.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/kpipe/nx_kernel_pipe.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/monitor/nx_monitor.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_compat.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_compat.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_native.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_vp.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_flow.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_gso.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_host.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_llink.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_mit.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_poll.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_util.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_vp.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_adapter.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_adapter.h"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_kern.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_mbq.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_mbq.h"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_pktq.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_pktq.h"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_traffic_rule.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/upipe/nx_user_pipe.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/packet_copy.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/packet_kern.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/pbufpool.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/pbufpool_kern.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/xnu/iokit/Kernel/IODeviceTreeSupport.cpp"
+ "cluster_verify_thread"
+ "verify_in_flight underflow @%s:%d"
- "%s:%d pageout of unaligned first page offset = %lld, size = %d  returned %d,\n"
- "%s:%d pageout of unaligned last page offset = %lld, size = %d  returned %d,\n"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Binaries/xnu/install/TempContent/Objects/EXPORT_HDRS/bsd/skywalk/nexus_common.h"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Binaries/xnu/install/TempContent/Objects/EXPORT_HDRS/bsd/skywalk/packet_common.h"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/dev/dtrace/dtrace.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kern_control.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kern_event.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kpi_mbuf.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kpi_socket.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kpi_socketfilter.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/socket_flows.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/subr_eventhandler.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/sys_domain.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/tracker.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_domain.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_mbuf.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_mbuf2.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_proto.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_socket.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_socket2.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_syscalls.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_usrreq.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/vsock_domain.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/bpf.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/classq/classq.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/classq/classq_fq_codel.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/classq/classq_subr.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/content_filter.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/dlil.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/droptap.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/flowadv.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_bond.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_bridge.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_fake.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_ipsec.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_llreach.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_loop.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_ports_used.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_redirect.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_utun.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_vlan.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/iptap.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/kpi_interface.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/mblist.h"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/nat464_utils.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/ndrv.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/necp_client.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/network_agent.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/ntstat.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/nwk_wq.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_if.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_ioctl.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_norm.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_pbuf.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_table.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktap.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktsched/pktsched.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktsched/pktsched_fq_codel.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktsched/pktsched_netem.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/route.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/rtsock.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/flow_divert.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/igmp.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_arp.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_mcast.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_pcb.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_proto.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_rmx.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_tclass.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_dummynet.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_encap.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_icmp.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_input.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_output.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/kpi_ipfilter.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mp_pcb.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mp_pcb.h"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mp_proto.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_opt.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_subr.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_timer.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_usrreq.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_var.h"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/raw_ip.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_cache.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_cubic.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_input.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_ledbat.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_output.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_prague.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_sack.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_subr.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_timer.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_usrreq.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/udp_usrreq.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ah_core.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ah_input.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ah_output.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_chachapoly.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_core.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_input.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_output.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_rijndael.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/frag6.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/icmp6.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_cga.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_ifattach.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_mcast.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_pcb.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_proto.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_rmx.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_src.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_forward.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_id.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_input.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_output.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ipsec.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ipsec.h"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/mld6.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_nbr.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_prproxy.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_rti.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_rtr.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_send.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/scope6.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/udp6_output.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netkey/key.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netkey/keysock.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel_kern.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel_ring.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel_syscalls.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/core/skywalk.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/lib/net_filter_event.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_arena.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_cache.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_cache_var.h"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_region.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_slab.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/namespace/flowidns.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/namespace/netns.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/namespace/protons.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_agg.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_classifier.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_entry.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_manager.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_owner.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_route.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_stats.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_track.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_var.h"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_classq.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_dp.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_ethernet.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_ip_frag.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_vp.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/nx_flowswitch.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/kpipe/nx_kernel_pipe.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/monitor/nx_monitor.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_compat.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_compat.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_native.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_vp.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_flow.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_gso.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_host.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_llink.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_mit.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_poll.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_util.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_vp.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_adapter.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_adapter.h"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_kern.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_mbq.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_mbq.h"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_pktq.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_pktq.h"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_traffic_rule.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/upipe/nx_user_pipe.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/packet_copy.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/packet_kern.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/pbufpool.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/pbufpool_kern.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/xnu/iokit/Kernel/IODeviceTreeSupport.cpp"
- "darwin-init"

```

>  `com.apple.driver.AppleConvergedIPCOLYBTControl`

```diff

-106.0.0.0.0
-  __TEXT.__cstring: 0x7f01
+107.0.0.0.0
+  __TEXT.__cstring: 0x7f7d
   __TEXT.__const: 0x98
-  __TEXT_EXEC.__text: 0x48410
+  __TEXT_EXEC.__text: 0x48570
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1f0

   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__mod_init_func: 0x58
   __DATA_CONST.__mod_term_func: 0x58
-  __DATA_CONST.__const: 0x7230
+  __DATA_CONST.__const: 0x7248
   __DATA_CONST.__kalloc_type: 0xc40
   __DATA_CONST.__kalloc_var: 0x500
-  Functions: 969
-  Symbols:   1717
-  CStrings:  993
+  Functions: 971
+  Symbols:   1720
+  CStrings:  996
 
Symbols:
+ __ZN12ACIPCControl10deviceDeadEv
+ __ZN14ACIPCBTIDevice10deviceDeadEv
+ __ZN14ACIPCRTIDevice10deviceDeadEv
CStrings:
+ "%s::%s: PMNI AON APB wrapper reg : offset : 0x%lx  0x%x\n"
+ "%s::%s: PMNI BT APB wrapper reg : offset : 0x%lx  0x%x\n"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCBTIDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCBTIInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCOLYBTControl.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCOLYBTControlReporter.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCRTIDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCRTIInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCOLYBTDebug/AppleConvergedIPCOLYBTCoreDumpProvider.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCOLYBTDebug/AppleConvergedIPCOLYBTLogProvider.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCBTIDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCBTIPipe.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCOLYBTControl.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCRTIDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCRTIPipe.cpp"
+ "deviceDead"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCDevice.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCBTIDevice.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCBTIInterface.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCOLYBTControl.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCOLYBTControlReporter.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCRTIDevice.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCRTIInterface.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCOLYBTDebug/AppleConvergedIPCOLYBTCoreDumpProvider.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCOLYBTDebug/AppleConvergedIPCOLYBTLogProvider.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCBTIDevice.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCBTIPipe.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCOLYBTControl.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCRTIDevice.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCRTIPipe.cpp"

```

>  `com.apple.driver.AppleFirmwareKit`

```diff

-531.0.4.0.0
-  __TEXT.__cstring: 0x20e6
+531.0.7.0.0
+  __TEXT.__cstring: 0x3650
   __TEXT.__os_log: 0xc73
   __TEXT.__const: 0xa8
-  __TEXT_EXEC.__text: 0x2dcb8
+  __TEXT_EXEC.__text: 0x314d4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3f8
   __DATA.__common: 0x548
   __DATA.__bss: 0xc8
-  __DATA_CONST.__auth_got: 0x3c0
-  __DATA_CONST.__got: 0x118
+  __DATA_CONST.__auth_got: 0x3b8
+  __DATA_CONST.__got: 0x110
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__mod_init_func: 0xb8
   __DATA_CONST.__mod_term_func: 0xb8
-  __DATA_CONST.__const: 0xfa28
+  __DATA_CONST.__const: 0xf9f8
   __DATA_CONST.__kalloc_type: 0x15c0
-  Functions: 1337
-  Symbols:   2417
-  CStrings:  316
+  Functions: 1598
+  Symbols:   2675
+  CStrings:  469
 
Symbols:
+ _ZL19rtbuddy_free_memoryP9rtbuddy_sP23rtbuddy_memory_buffer_t12alloc_type_t.cold.1
+ _ZL19rtbuddy_free_memoryP9rtbuddy_sP23rtbuddy_memory_buffer_t12alloc_type_t.cold.2
+ _ZN11AFKEPKextV214powerStateDoneEPv.cold.1
+ _ZN11AFKEPKextV215incrementClientEb.cold.1
+ _ZN11AFKEPKextV215incrementClientEb.cold.2
+ _ZN11AFKEPKextV215incrementClientEb.cold.3
+ _ZN11AFKEPKextV218systemWillShutdownEj.cold.1
+ _ZN11AFKEPKextV222initPowerConfigurationEv.cold.1
+ _ZN11AFKEPKextV222initPowerConfigurationEv.cold.2
+ _ZN11AFKEPKextV24stopEP9IOService.cold.1
+ _ZN11AFKEPKextV25startEP9IOService.cold.1
+ _ZN11AFKEPKextV25startEP9IOService.cold.2
+ _ZN11AFKEPKextV25startEP9IOService.cold.3
+ _ZN11AFKEPKextV25startEP9IOService.cold.4
+ _ZN11AFKEPKextV25startEP9IOService.cold.5
+ _ZN11AFKEPKextV25startEP9IOService.cold.6
+ _ZN11AFKEPKextV28initIOPMEv.cold.1
+ _ZN16AFKEPInterfaceV210handleOpenEv.cold.1
+ _ZN16AFKEPInterfaceV210handleOpenEv.cold.2
+ _ZN16AFKEPInterfaceV211findCommandEh.cold.1
+ _ZN16AFKEPInterfaceV211handleCloseEv.cold.1
+ _ZN16AFKEPInterfaceV212handlePacketEPKN5AFKEP11MessageInfoEPKNS0_7MessageEm.cold.1
+ _ZN16AFKEPInterfaceV212handlePacketEPKN5AFKEP11MessageInfoEPKNS0_7MessageEm.cold.2
+ _ZN16AFKEPInterfaceV212handlePacketEPKN5AFKEP11MessageInfoEPKNS0_7MessageEm.cold.3
+ _ZN16AFKEPInterfaceV212handlePacketEPKN5AFKEP11MessageInfoEPKNS0_7MessageEm.cold.4
+ _ZN16AFKEPInterfaceV213enqueueReportEhyPN5AFKEP7MessageEmPK16AFKEPSendOptions.cold.1
+ _ZN16AFKEPInterfaceV213handleMessageEPKN5AFKEP11MessageInfoEPKNS0_7MessageEm.cold.1
+ _ZN16AFKEPInterfaceV213handleMessageEPKN5AFKEP11MessageInfoEPKNS0_7MessageEm.cold.2
+ _ZN16AFKEPInterfaceV213handleMessageEPKN5AFKEP11MessageInfoEPKNS0_7MessageEm.cold.3
+ _ZN16AFKEPInterfaceV213handleMessageEPKN5AFKEP11MessageInfoEPKNS0_7MessageEm.cold.4
+ _ZN16AFKEPInterfaceV213handleMessageEPKN5AFKEP11MessageInfoEPKNS0_7MessageEm.cold.5
+ _ZN16AFKEPInterfaceV213handleUnknownEP23AFKEPInterfaceServiceV2PKN5AFKEP11MessageInfoEPKNS2_7MessageEm.cold.1
+ _ZN16AFKEPInterfaceV213handleUnknownEP23AFKEPInterfaceServiceV2PKN5AFKEP11MessageInfoEPKNS2_7MessageEm.cold.2
+ _ZN16AFKEPInterfaceV213handleUnknownEP23AFKEPInterfaceServiceV2PKN5AFKEP11MessageInfoEPKNS2_7MessageEm.cold.3
+ _ZN16AFKEPInterfaceV214acquireCommandEv.cold.1
+ _ZN16AFKEPInterfaceV214enqueueCommandEPvhyPN5AFKEP7MessageEmS0_jPK16AFKEPSendOptions.cold.1
+ _ZN16AFKEPInterfaceV214enqueueCommandEPvhyPN5AFKEP7MessageEmS0_jPK16AFKEPSendOptions.cold.2
+ _ZN16AFKEPInterfaceV214releaseCommandEv.cold.1
+ _ZN16AFKEPInterfaceV215enqueueResponseEPviyPN5AFKEP7MessageEmPK16AFKEPSendOptions.cold.1
+ _ZN16AFKEPInterfaceV218handleNotificationEN5AFKEP12NotificationEPU7_Atomich.cold.1
+ _ZN16AFKEPInterfaceV219deliverNotificationEN5AFKEP12NotificationEPU7_Atomich.cold.1
+ _ZN16AFKEPInterfaceV219deliverNotificationEN5AFKEP12NotificationEPU7_Atomich.cold.2
+ _ZN16AFKEPInterfaceV219handleClientCommandEyhPvj.cold.1
+ _ZN16AFKEPInterfaceV220cleanupRemoteContextEv.cold.1
+ _ZN16AFKEPInterfaceV220createErrorResponsesEv.cold.1
+ _ZN16AFKEPInterfaceV220handleClientResponseEyhPvj.cold.1
+ _ZN16AFKEPInterfaceV220handleClientResponseEyhPvj.cold.2
+ _ZN17AFKEPCommandLocal13getCmdHeadersEPN5AFKEP7MessageEjPm.cold.1
+ _ZN17AFKEPCommandLocal13getCmdHeadersEPN5AFKEP7MessageEjPm.cold.2
+ _ZN17AFKEPCommandLocal13getCmdHeadersEPN5AFKEP7MessageEjPm.cold.3
+ _ZN17AFKEPCommandLocal13getCmdHeadersEPN5AFKEP7MessageEjPm.cold.4
+ _ZN17AFKEPCommandLocal13parseResponseEPvj.cold.1
+ _ZN17AFKEPCommandLocal13parseResponseEPvj.cold.2
+ _ZN17AFKEPCommandLocal23createAFKEPCommandLocalEP9rtbuddy_sPvjjPK16AFKEPSendOptionsS2_hPN5AFKEP7MessageEm.cold.1
+ _ZN17AFKEPCommandLocal23createAFKEPCommandLocalEP9rtbuddy_sPvjjPK16AFKEPSendOptionsS2_hPN5AFKEP7MessageEm.cold.2
+ _ZN17AFKEPV2MessHelper7stateCBEPv14MessengerState.cold.1
+ _ZN18AFKEPCommandRemote13getRspHeadersEPN5AFKEP7MessageES2_miPm.cold.1
+ _ZN18AFKEPCommandRemote13getRspHeadersEPN5AFKEP7MessageES2_miPm.cold.2
+ _ZN18AFKEPCommandRemote24createAFKEPCommandRemoteEP9rtbuddy_shPvj.cold.1
+ _ZN18AFKEPCommandRemote24createAFKEPCommandRemoteEP9rtbuddy_shPvj.cold.2
+ _ZN18AFKIOServiceClient13handleCommandEPN20AFKEndpointInterface14CommandContextEjyP9AFK_iovecmj.cold.1
+ _ZN18AFKIOServiceClient4stopEP9IOService.cold.1
+ _ZN18AFKIOServiceClient4stopEP9IOService.cold.2
+ _ZN19AFKMemoryDescriptor10writeBytesEmPKvm.cold.1
+ _ZN19AFKMemoryDescriptor11assertPowerEb.cold.1
+ _ZN19AFKMemoryDescriptor13assumeControlEv.cold.1
+ _ZN19AFKMemoryDescriptor14releaseControlEb.cold.1
+ _ZN19AFKMemoryDescriptor14retainInternalEv.cold.1
+ _ZN19AFKMemoryDescriptor15releaseInternalEv.cold.1
+ _ZN19AFKMemoryDescriptor4freeEv.cold.1
+ _ZN19AFKMemoryDescriptor8setInUseEb.cold.1
+ _ZN19AFKMemoryDescriptor8setInUseEb.cold.2
+ _ZN19AFKMemoryDescriptor9setLengthEm.cold.1
+ _ZN20AFKEPInterfaceKextV211closeHelperEv.cold.1
+ _ZN20AFKEPInterfaceKextV211handleCloseEP9IOServicej.cold.1
+ _ZN20AFKEPInterfaceKextV213handleUnknownEP27AFKEPInterfaceServiceKextV2PKN5AFKEP11MessageInfoEPKNS2_7MessageEm.cold.1
+ _ZN20AFKEPInterfaceKextV213handleUnknownEP27AFKEPInterfaceServiceKextV2PKN5AFKEP11MessageInfoEPKNS2_7MessageEm.cold.2
+ _ZN20AFKEPInterfaceKextV213handleUnknownEP27AFKEPInterfaceServiceKextV2PKN5AFKEP11MessageInfoEPKNS2_7MessageEm.cold.3
+ _ZN20AFKEPInterfaceKextV214sendOpenReportEv.cold.1
+ _ZN20AFKEPInterfaceKextV216assertPowerStateEv.cold.1
+ _ZN20AFKEPInterfaceKextV217enqueueDescriptorEjyP19AFKMemoryDescriptorjP9IOService.cold.1
+ _ZN20AFKEPInterfaceKextV217enqueueDescriptorEjyP19AFKMemoryDescriptorjP9IOService.cold.2
+ _ZN20AFKEPInterfaceKextV217enqueueDescriptorEjyP19AFKMemoryDescriptorjP9IOService.cold.3
+ _ZN20AFKEPInterfaceKextV217withPublishReportEPK13PublishReportmP9IOServiceP9rtbuddy_st.cold.1
+ _ZN20AFKEPInterfaceKextV218deassertPowerStateEv.cold.1
+ _ZN20AFKEPInterfaceKextV218deassertPowerStateEv.cold.2
+ _ZN20AFKEPInterfaceKextV223deliverDescriptorReportEPvj.cold.1
+ _ZN20AFKEPInterfaceKextV24initEP12OSDictionaryP9IOService.cold.1
+ _ZN20AFKEPInterfaceKextV24initEP12OSDictionaryP9IOService.cold.2
+ _ZN20AFKEPInterfaceKextV24stopEP9IOService.cold.1
+ _ZN20AFKEPInterfaceKextV24stopEP9IOService.cold.2
+ _ZN20AFKEPInterfaceKextV24stopEP9IOService.cold.3
+ _ZN20AFKEPInterfaceKextV24stopEP9IOService.cold.4
+ _ZN20AFKEPInterfaceKextV24stopEP9IOService.cold.5
+ _ZN20AFKEPInterfaceKextV25startEP9IOService.cold.1
+ _ZN20AFKEPInterfaceKextV25startEP9IOService.cold.10
+ _ZN20AFKEPInterfaceKextV25startEP9IOService.cold.2
+ _ZN20AFKEPInterfaceKextV25startEP9IOService.cold.3
+ _ZN20AFKEPInterfaceKextV25startEP9IOService.cold.4
+ _ZN20AFKEPInterfaceKextV25startEP9IOService.cold.5
+ _ZN20AFKEPInterfaceKextV25startEP9IOService.cold.6
+ _ZN20AFKEPInterfaceKextV25startEP9IOService.cold.7
+ _ZN20AFKEPInterfaceKextV25startEP9IOService.cold.8
+ _ZN20AFKEPInterfaceKextV25startEP9IOService.cold.9
+ _ZN20AFKEPInterfaceKextV28openImplEP9IOService.cold.1
+ _ZN20AFKEndpointInterface4initEP12OSDictionary.cold.1
+ _ZN20AFKTightbeamEndpoint10sendReportEPhm.cold.1
+ _ZN20AFKTightbeamEndpoint11sendCommandEPhmPS0_Pm.cold.1
+ _ZN20AFKTightbeamEndpoint11sendCommandEPhmPS0_Pm.cold.2
+ _ZN20AFKTightbeamEndpoint12sendResponseEPviPhm.cold.1
+ _ZN20AFKTightbeamEndpoint5startEP9IOService.cold.1
+ _ZN22AFKIOServiceClientBase15enqueueResponseEPN20AFKEndpointInterface14CommandContextEiyP9AFK_iovecmj.cold.2
+ _ZN23AFKMemoryDescriptorImpl11appendBytesEPKvm.cold.1
+ _ZN23AFKMemoryDescriptorImpl11assertPowerEb.cold.1
+ _ZN23AFKMemoryDescriptorImpl13assumeControlEmm.cold.1
+ _ZN23AFKMemoryDescriptorImpl14releaseControlEmmb.cold.1
+ _ZN23AFKMemoryDescriptorImpl4initEv.cold.1
+ _ZN23AFKMemoryDescriptorImpl9initAcipcEy.cold.1
+ _ZN23AFKMemoryDescriptorImpl9setLengthEm.cold.1
+ _ZN23AFKMemoryDescriptorImplD1Ev.cold.1
+ _ZN25AFKBufferMemoryDescriptor11appendBytesEPKvm.cold.1
+ _ZN25AFKBufferMemoryDescriptor13assumeControlEmm.cold.1
+ _ZN25AFKBufferMemoryDescriptor14releaseControlEmmb.cold.1
+ _ZN25AFKEndpointInterfaceRelay11memDescCopyEP19AFKMemoryDescriptorS1_.cold.1
+ _ZN25AFKEndpointInterfaceRelay13enqueueReportEP20AFKEndpointInterfacejyPKvmj.cold.1
+ _ZN25AFKEndpointInterfaceRelay14enqueueCommandEP20AFKEndpointInterfacePNS0_14CommandContextEjyPKvmmj.cold.1
+ _ZN25AFKEndpointInterfaceRelay15enqueueResponseEP20AFKEndpointInterfacePNS_19AsyncCommandContextEiyPKvmj.cold.1
+ _ZN25AFKEndpointInterfaceRelay17enqueueDescriptorEP20AFKEndpointInterfacejyP19AFKMemoryDescriptorj.cold.1
+ _ZN27AFKEPInterfaceEventSourceV214dispatchReportEjyPvj.cold.1
+ _ZN27AFKEPInterfaceEventSourceV214dispatchReportEjyPvj.cold.2
+ _ZN27AFKEPInterfaceEventSourceV215dispatchCommandEPvjyhS0_j.cold.1
+ _ZN27AFKEPInterfaceEventSourceV215dispatchCommandEPvjyhS0_j.cold.2
+ _ZN27AFKEPInterfaceEventSourceV216dispatchResponseEPviyS0_j.cold.1
+ _ZN27AFKEPInterfaceEventSourceV216dispatchResponseEPviyS0_j.cold.2
+ _ZN27AFKEPInterfaceEventSourceV217stateCompleteImplEv.cold.1
+ _ZN27AFKEPInterfaceEventSourceV220dispatchNotificationEN5AFKEP12NotificationEPU7_Atomich.cold.1
+ _ZN27AFKEPInterfaceEventSourceV24freeEv.cold.1
+ _ZN27AFKEPInterfaceEventSourceV24freeEv.cold.2
+ _ZN27AFKEPInterfaceEventSourceV24initEP16AFKEPInterfaceV2.cold.1
+ _ZN27AFKEPInterfaceEventSourceV24initEP16AFKEPInterfaceV2.cold.2
+ _ZN27AFKEPInterfaceEventSourceV26doTaskEv.cold.1
+ _ZN27AFKEPInterfaceServiceKextV213handleMessageEPKN5AFKEP11MessageInfoEPKNS0_7MessageEm.cold.1
+ _ZN27AFKEPInterfaceServiceKextV216eventQThreadCallEPS_.cold.1
+ _ZN27AFKEPInterfaceServiceKextV218handleNotificationEN5AFKEP12NotificationE.cold.1
+ _ZN27AFKEPInterfaceServiceKextV218handlePublishEventEPNS_12PublishEventE.cold.1
+ _ZN27AFKEPInterfaceServiceKextV218handlePublishEventEPNS_12PublishEventE.cold.2
+ _ZN27AFKEPInterfaceServiceKextV218handlePublishEventEPNS_12PublishEventE.cold.3
+ _ZN27AFKEPInterfaceServiceKextV218handlePublishEventEPNS_12PublishEventE.cold.4
+ _ZN27AFKEPInterfaceServiceKextV219enqueuePublishEventEPvmt.cold.1
+ _ZN27AFKEPInterfaceServiceKextV221enqueueTerminateEventEt.cold.1
+ _ZN27AFKEPInterfaceServiceKextV224enqueueTerminateAllEventEv.cold.1
+ _ZN27AFKEPInterfaceServiceKextV25startEP9IOService.cold.1
+ _ZN30AFKEndpointInterfaceUserClient10closeGatedEPvP25IOExternalMethodArguments.cold.1
+ _ZN30AFKEndpointInterfaceUserClient12handleReportEP20AFKEndpointInterfacejyPKvmj.cold.1
+ _ZN30AFKEndpointInterfaceUserClient16handleDescriptorEP20AFKEndpointInterfacejyP19AFKMemoryDescriptorj.cold.1
+ _ZN30AFKEndpointInterfaceUserClient16handleDescriptorEP20AFKEndpointInterfacejyP19AFKMemoryDescriptorj.cold.2
+ _ZN30AFKEndpointInterfaceUserClient19saveQueueToWaitListEP18AFKSharedDataQueue.cold.1
+ _ZN30AFKEndpointInterfaceUserClient28dataQueueSpaceAvailableGatedEPvP25IOExternalMethodArguments.cold.1
+ _ZN30AFKMemoryDescriptorManagerBase12handleReportEP20AFKEndpointInterfacejyPKvmj.cold.1
+ _ZN30AFKMemoryDescriptorManagerBase17enqueueFreeReportEy.cold.1
+ _ZN30AFKMemoryDescriptorManagerBase23handleDescriptorReleaseEPK19AFKMemoryDescriptor.cold.1
+ _ZN30AFKMemoryDescriptorManagerBase5startEP9IOService.cold.1
+ _ZN30AFKMemoryDescriptorManagerBase5startEP9IOService.cold.2
+ _ZN30AFKMemoryDescriptorManagerBase5startEP9IOService.cold.3
+ _ZN30AFKMemoryDescriptorManagerBase5startEP9IOService.cold.4
+ _ZN30AFKMemoryDescriptorManagerBase5startEP9IOService.cold.5
+ _ZN30AFKMemoryDescriptorManagerBase5startEP9IOService.cold.6
+ _ZN31AFKACIPCMemoryDescriptorManager14handleResponseEP20AFKEndpointInterfacePviyPKvm.cold.1
+ _ZN31AFKACIPCMemoryDescriptorManager14handleResponseEP20AFKEndpointInterfacePviyPKvm.cold.2
+ _ZN31AFKACIPCMemoryDescriptorManager21createDescriptorGatedEmNS_6MDTypeE.cold.1
+ _ZN31AFKACIPCMemoryDescriptorManager21createDescriptorGatedEmNS_6MDTypeE.cold.2
+ _ZN31AFKLocalMemoryDescriptorManager13handleCommandEP20AFKEndpointInterfacePNS0_14CommandContextEjyPKvmj.cold.1
+ _ZN31AFKLocalMemoryDescriptorManager13handleCommandEP20AFKEndpointInterfacePNS0_14CommandContextEjyPKvmj.cold.2
+ _ZN31AFKLocalMemoryDescriptorManager13handleCommandEP20AFKEndpointInterfacePNS0_14CommandContextEjyPKvmj.cold.3
+ _ZN5AFKEP10handleOpenEP12AFKEPServicej.cold.1
+ _ZN5AFKEP11handleCloseEP12AFKEPService.cold.1
+ _ZN5AFKEP11handleStartEv.cold.1
+ _ZN7AFKEPV210handleOpenEP12AFKEPServicej.cold.1
+ _ZN7AFKEPV211handleStartEv.cold.1
+ _ZN7AFKEPV211handleStartEv.cold.2
+ _ZN7AFKEPV211handleStartEv.cold.3
+ _ZN7AFKEPV212handlePacketEPvj.cold.1
+ _ZN7AFKEPV212handlePacketEPvj.cold.2
+ _ZN7AFKEPV212handleQSpaceEPvj.cold.1
+ _ZN7AFKEPV213sendPauseDoneEPv.cold.1
+ _ZN7AFKEPV214handleSetStateEN5AFKEP5StateE.cold.1
+ _ZN7AFKEPV215getDesiredStateEPN5AFKEP12NotificationEPb.cold.1
+ _ZN7AFKEPV215runStateMachineEv.cold.1
+ _ZN7AFKEPV215runStateMachineEv.cold.2
+ _ZN7AFKEPV215runStateMachineEv.cold.3
+ _ZN7AFKEPV215runStateMachineEv.cold.4
+ _ZN7AFKEPV217handleSendMessageEPKN5AFKEP11MessageInfoEPKNS0_7MessageEmPK16AFKEPSendOptions.cold.1
+ _ZN7AFKEPV217handleSendMessageEPKN5AFKEP11MessageInfoEPKNS0_7MessageEmPK16AFKEPSendOptions.cold.2
+ _ZN7AFKEPV217handleSendMessageEPKN5AFKEP11MessageInfoEPKNS0_7MessageEmPK16AFKEPSendOptions.cold.3
+ _ZN7AFKEPV218sendInternalPacketEj.cold.1
+ _ZN7AFKEPV218sendInternalPacketEj.cold.2
+ _ZN7AFKEPV220handleInternalPacketEPKN5AFKEP7MessageEm.cold.1
+ _ZN7AFKEPV220handleInternalPacketEPKN5AFKEP7MessageEm.cold.2
+ _ZN7AFKEPV220handleInternalPacketEPKN5AFKEP7MessageEm.cold.3
+ _ZN7AFKEPV220handleInternalPacketEPKN5AFKEP7MessageEm.cold.4
+ _ZN7AFKEPV221mailboxMessageHandlerEP21AFKMailboxEventSourceyPv.cold.1
+ _ZN7AFKEPV222notificationCompletionEPv.cold.1
+ _ZN7AFKEPV222notificationCompletionEPv.cold.2
+ _ZN7AFKEPV229invokeNotificationCompletionsEv.cold.1
+ _ZN7AFKEPV29reconnectEPv.cold.1
+ _ZNK19AFKMemoryDescriptor5bytesEv.cold.1
+ _ZNK19AFKMemoryDescriptor9getLengthEv.cold.1
+ _ZNK19AFKMemoryDescriptor9readBytesEmPvm.cold.1
+ _ZNK23AFKMemoryDescriptorImpl14getBytesNoCopyEmm.cold.1
+ _ZNK23AFKMemoryDescriptorImpl14getBytesNoCopyEmm.cold.2
+ _ZNK25AFKBufferMemoryDescriptor14getBytesNoCopyEmm.cold.1
+ __ZN16AFKACIPCEndpoint4initEP12OSDictionary
+ __ZNK11AFKEPKextV219useIOPMStateControlEv
+ ___ZN11AFKEPKextV214handleSetStateEN5AFKEP5StateE_block_invoke.cold.1
+ ___ZN11AFKEPKextV214handleSetStateEN5AFKEP5StateE_block_invoke.cold.2
+ ___ZN11AFKEPKextV214handleSetStateEN5AFKEP5StateE_block_invoke.cold.3
+ ___ZN11AFKEPKextV216stateMachineInitEv_block_invoke_2.cold.1
+ ___ZN20AFKEPInterfaceKextV214enqueueCommandEPvjyPKvmmjP9IOService_block_invoke.57
+ ___ZN20AFKEPInterfaceKextV214enqueueCommandEPvjyPKvmmjP9IOService_block_invoke.60
+ ___ZN20AFKEPInterfaceKextV214enqueueCommandEPvjyPKvmmjP9IOService_block_invoke.60.cold.1
+ ___ZN20AFKEPInterfaceKextV214enqueueCommandEPvjyPKvmmjP9IOService_block_invoke.60.cold.2
+ ___ZN20AFKEPInterfaceKextV214enqueueCommandEPvjyPKvmmjP9IOService_block_invoke.60.cold.3
+ ___ZN20AFKEPInterfaceKextV214enqueueCommandEPvjyPKvmmjP9IOService_block_invoke.66
+ ___ZN20AFKEPInterfaceKextV215enqueueResponseEPN20AFKEndpointInterface14CommandContextEiyPKvmj_block_invoke.cold.1
+ ___ZN20AFKEPInterfaceKextV219enqueueReportHelperEjyPKvmj_block_invoke.186
+ ___ZN20AFKEPInterfaceKextV219enqueueReportHelperEjyPKvmj_block_invoke.186.cold.1
+ ___ZN20AFKEPInterfaceKextV219enqueueReportHelperEjyPKvmj_block_invoke.190
+ ___ZN20AFKEPInterfaceKextV25startEP9IOService_block_invoke_2.cold.1
+ ___ZN22AFKIOServiceClientBase21handleServiceInternalEP9IOService_block_invoke.12
+ ___ZN25AFKEndpointInterfaceRelay5startEP9IOService_block_invoke_2.cold.1
+ ___ZN30AFKEndpointInterfaceUserClient12handleReportEP20AFKEndpointInterfacejyPKvmj_block_invoke.72
+ ___ZN30AFKEndpointInterfaceUserClient16handleDescriptorEP20AFKEndpointInterfacejyP19AFKMemoryDescriptorj_block_invoke.79
+ ___ZN30AFKEndpointInterfaceUserClient16handleDescriptorEP20AFKEndpointInterfacejyP19AFKMemoryDescriptorj_block_invoke.cold.1
+ ___ZN30AFKEndpointInterfaceUserClient22enqueueDescriptorGatedEPvP25IOExternalMethodArguments_block_invoke.cold.1
+ ___ZN30AFKMemoryDescriptorManagerBase22copyReceivedDescriptorEy_block_invoke.23
+ ___ZN30AFKMemoryDescriptorManagerBase22copyReceivedDescriptorEy_block_invoke.23.cold.1
+ ___ZN30AFKMemoryDescriptorManagerBase5startEP9IOService_block_invoke_2.cold.1
+ ___ZN31AFKLocalMemoryDescriptorManager20createDescriptorImplEmNS_6MDTypeEbb_block_invoke.cold.1
+ __block_descriptor_tmp.17
+ __block_descriptor_tmp.185
+ __block_descriptor_tmp.189
+ __block_descriptor_tmp.191
+ __block_descriptor_tmp.23
+ __block_descriptor_tmp.26
+ __block_descriptor_tmp.42
+ __block_descriptor_tmp.51
+ __block_descriptor_tmp.68
+ __block_descriptor_tmp.68
+ __block_descriptor_tmp.70
+ __block_descriptor_tmp.70
+ __block_descriptor_tmp.71
+ __block_descriptor_tmp.71
+ __block_descriptor_tmp.73
+ __block_descriptor_tmp.73
+ __block_descriptor_tmp.77
+ __block_descriptor_tmp.78
+ __block_descriptor_tmp.79
+ __block_descriptor_tmp.80
+ __block_descriptor_tmp.80
+ __block_descriptor_tmp.83
+ __block_descriptor_tmp.95
+ __block_descriptor_tmp.96
+ afk_msgr_after_ready_ack.cold.1
+ afk_msgr_enqueue.cold.1
+ afk_msgr_enqueue.cold.2
+ afk_msgr_handle_command._os_log_fmt.5
+ afk_msgr_handle_command._os_log_fmt.6
+ afk_msgr_handle_command.cold.1
+ afk_msgr_handle_here_buf_addr.cold.1
+ afk_msgr_handle_q_full.cold.1
+ afk_msgr_init.cold.1
+ afk_msgr_init.cold.2
+ afk_msgr_init.cold.3
+ afk_msgr_msg_recv_cb.cold.1
+ afk_msgr_msg_send.cold.1
+ afk_msgr_ringbuffer_assume_subrange_cb.cold.1
+ afk_msgr_ringbuffer_release_subrange_cb.cold.1
+ handle_here_buf.cold.1
+ handle_here_buf_acipc.cold.1
+ handle_req_buf.cold.1
+ handle_req_buf.cold.2
+ handle_req_buf.cold.3
+ handle_req_buf_acipc.cold.1
+ handle_req_buf_acipc.cold.2
+ handle_req_buf_acipc.cold.3
+ handler_ready_acipc.cold.1
+ handler_ready_ack_acipc.cold.1
+ rtbuddy_allocate_shared_memory_buffer.cold.3
+ rtbuddy_assume_control.cold.1
+ rtbuddy_assume_control.cold.2
+ rtbuddy_assume_control.cold.3
+ rtbuddy_make_memory_visible.cold.3
+ rtbuddy_make_memory_visible.cold.4
+ rtbuddy_release_control.cold.1
+ rtbuddy_release_control.cold.2
+ rtbuddy_release_control.cold.3
+ rtbuddy_release_free_visible_memory.cold.1
+ rtbuddy_send_message.cold.1
- _Assert
- __ZNK11AFKEPKextV222useRTBuddyPowerActionsEv
- __ZNK16AFKACIPCEndpoint22useRTBuddyPowerActionsEv
- ___ZN20AFKEPInterfaceKextV214enqueueCommandEPvjyPKvmmjP9IOService_block_invoke.39
- ___ZN20AFKEPInterfaceKextV214enqueueCommandEPvjyPKvmmjP9IOService_block_invoke.42
- ___ZN20AFKEPInterfaceKextV214enqueueCommandEPvjyPKvmmjP9IOService_block_invoke.46
- ___ZN20AFKEPInterfaceKextV219enqueueReportHelperEjyPKvmj_block_invoke.156
- ___ZN20AFKEPInterfaceKextV219enqueueReportHelperEjyPKvmj_block_invoke.160
- ___ZN22AFKIOServiceClientBase21handleServiceInternalEP9IOService_block_invoke.10
- ___ZN30AFKEndpointInterfaceUserClient12handleReportEP20AFKEndpointInterfacejyPKvmj_block_invoke.68
- ___ZN30AFKEndpointInterfaceUserClient16handleDescriptorEP20AFKEndpointInterfacejyP19AFKMemoryDescriptorj_block_invoke.73
- ___ZN30AFKMemoryDescriptorManagerBase22copyReceivedDescriptorEy_block_invoke.15
- __block_descriptor_tmp.1
- __block_descriptor_tmp.155
- __block_descriptor_tmp.159
- __block_descriptor_tmp.161
- __block_descriptor_tmp.32
- __block_descriptor_tmp.35
- __block_descriptor_tmp.4
- __block_descriptor_tmp.53
- __block_descriptor_tmp.54
- __block_descriptor_tmp.54
- __block_descriptor_tmp.54
- __block_descriptor_tmp.55
- __block_descriptor_tmp.55
- __block_descriptor_tmp.57
- __block_descriptor_tmp.60
- __block_descriptor_tmp.61
- __block_descriptor_tmp.63
- __block_descriptor_tmp.74
- __block_descriptor_tmp.8
- __block_descriptor_tmp.8
- _kext_assertions_enable
- afk_msgr_handle_command._os_log_fmt.1
- afk_msgr_handle_command._os_log_fmt.2
CStrings:
+ "\"!__os_warn_unused(__builtin_add_overflow((offset), (numBytes), (&endRange))) && endRange <= _length\" @%s:%d"
+ "\"!__os_warn_unused(__builtin_add_overflow((offset), (numBytes), (&endRange)))\" @%s:%d"
+ "\"!_inUse\" @%s:%d"
+ "\"!_internalRetain\" @%s:%d"
+ "\"!copyReceivedDescriptor(getMDImpl(md)->getToken())\" @%s:%d"
+ "\"!descriptor->_impl->getAssertPower()\" @%s:%d"
+ "\"!fail\" @%s:%d"
+ "\"!iObject->isEqualTo(jObject)\" @%s:%d"
+ "\"!isInactive()\" @%s:%d"
+ "\"!overflow && newLength <= _capacity\" @%s:%d"
+ "\"!overflow\" @%s:%d"
+ "\"!pending\" @%s:%d"
+ "\"!this->_config.size || this->_config.txQueueLen+this->_config.rxQueueLen == this->_config.size\" @%s:%d"
+ "\"!this->_endpointWL->inGate()\" @%s:%d"
+ "\"!this->_endpointWL->onThread()\" @%s:%d"
+ "\"!this->_published && !this->_openSent\" @%s:%d"
+ "\"(((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x2c2) != rv\" @%s:%d"
+ "\"((void*)0) != (void*)messenger->buffer.remote_addr\" @%s:%d"
+ "\"(bool)this->_config.size == (bool)this->_config.buffer\" @%s:%d"
+ "\"0 != messenger->buffer.size && ((void*)0) != (void*)messenger->buffer.remote_addr\" @%s:%d"
+ "\"0 == _assertionCount && 0 == _assertionWaitCount\" @%s:%d"
+ "\"0 == _sessionCount\" @%s:%d"
+ "\"0 == platStatus\" @%s:%d"
+ "\"0 == result && shmem_info->memory\" @%s:%d"
+ "\"0 == result\" @%s:%d"
+ "\"0 == ret\" @%s:%d"
+ "\"0 == status || (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x2d7) == status || (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x2e3) == status\" @%s:%d"
+ "\"0 == status || (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x2d7) == status\" @%s:%d"
+ "\"0 == status\" @%s:%d"
+ "\"1 == messageCount\" @%s:%d"
+ "\"AFKEP::Message::TypeBuffer == messages[0].type\" @%s:%d"
+ "\"NULL != mess\" @%s:%d"
+ "\"RTBUDDY_STATUS_OK == status\" @%s:%d"
+ "\"STAILQ_EMPTY(&this->_taskQ)\" @%s:%d"
+ "\"__builtin_bswap32('IOP ') == magic\" @%s:%d"
+ "\"_assertCnt\" @%s:%d"
+ "\"_assertPowerTimer\" @%s:%d"
+ "\"_assertionCount\" @%s:%d"
+ "\"_asycRequestES\" @%s:%d"
+ "\"_asyncES\" @%s:%d"
+ "\"_clientCount < 4294967295U\" @%s:%d"
+ "\"_clientCount > 0\" @%s:%d"
+ "\"_commandGate\" @%s:%d"
+ "\"_endpoint\" @%s:%d"
+ "\"_endpointWL->inGate()\" @%s:%d"
+ "\"_epi\" @%s:%d"
+ "\"_epicArr\" @%s:%d"
+ "\"_impl\" @%s:%d"
+ "\"_impl->getUsable()\" @%s:%d"
+ "\"_inUse != enable\" @%s:%d"
+ "\"_interface\" @%s:%d"
+ "\"_interfaces\" @%s:%d"
+ "\"_internalRetain\" @%s:%d"
+ "\"_lockAsyncRequests\" @%s:%d"
+ "\"_mdMgr\" @%s:%d"
+ "\"_mdMgrNotify\" @%s:%d"
+ "\"_provider\" @%s:%d"
+ "\"_secMemory\" @%s:%d"
+ "\"_workloop->inGate()\" @%s:%d"
+ "\"add <= shmem_info->memory->getBuffer()->getLength()\" @%s:%d"
+ "\"availableSpace >= payload->size\" @%s:%d"
+ "\"buffer->remote_addr == shmem_info->memory->getSlaveAddress()\" @%s:%d"
+ "\"bufferLen >= capacity * AFK_TAGGED_BUFFER_SIZE_SCALE\" @%s:%d"
+ "\"capacity\" @%s:%d"
+ "\"client\" @%s:%d"
+ "\"cmdCtx\" @%s:%d"
+ "\"command && commandLength && respBuffer && respBufferLength\" @%s:%d"
+ "\"command\" @%s:%d"
+ "\"count >= 1 + this->_inMsgsCnt\" @%s:%d"
+ "\"count >= 1\" @%s:%d"
+ "\"count >= 2 + this->_inMsgsCnt\" @%s:%d"
+ "\"count >= 2\" @%s:%d"
+ "\"counterIdx < (sizeof(this->_counters)/sizeof(this->_counters[0]))\" @%s:%d"
+ "\"d->notification != AFKEP::NotificationSendPossible\" @%s:%d"
+ "\"d->self->_endpointWL->inGate()\" @%s:%d"
+ "\"descriptor->_impl->getUsable()\" @%s:%d"
+ "\"endRange <= _length\" @%s:%d"
+ "\"endpointService\" @%s:%d"
+ "\"entry\" @%s:%d"
+ "\"epic\" @%s:%d"
+ "\"event->packetSize >= sizeof(PublishReport)\" @%s:%d"
+ "\"false\" @%s:%d"
+ "\"found\" @%s:%d"
+ "\"interface\" @%s:%d"
+ "\"length <= _capacity\" @%s:%d"
+ "\"lock\" @%s:%d"
+ "\"managerRole->isEqualTo(thisRole.get())\" @%s:%d"
+ "\"md\" @%s:%d"
+ "\"md->getRetainCount() > 1\" @%s:%d"
+ "\"messages[0].buffer.size >= sizeof(*header)\" @%s:%d"
+ "\"messenger->config.allocator\" @%s:%d"
+ "\"messenger->config.rxQueueLen && messenger->config.txQueueLen\" @%s:%d"
+ "\"messenger->state == handlers[i].startState\" @%s:%d"
+ "\"msgsIn[0].buffer.size - sizeof(*header) >= sizeof(*commHeader)\" @%s:%d"
+ "\"msgsIn[0].buffer.size >= sizeof(*header)\" @%s:%d"
+ "\"notification > AFKEP::NotificationInvalid && notification < AFKEP::NotificationCount\" @%s:%d"
+ "\"nullptr != client\" @%s:%d"
+ "\"nullptr != command\" @%s:%d"
+ "\"nullptr != properties\" @%s:%d"
+ "\"nullptr != task\" @%s:%d"
+ "\"nullptr != task->pkt\" @%s:%d"
+ "\"nullptr != this->_rles\" @%s:%d"
+ "\"nullptr == this->_client\" @%s:%d"
+ "\"nullptr == this->_out\" @%s:%d"
+ "\"num\" @%s:%d"
+ "\"numBytes <= dst->getCapacity()\" @%s:%d"
+ "\"ok\" @%s:%d"
+ "\"options & (1 << 13)\" @%s:%d"
+ "\"payloadSize == sizeof(AFKMDManagerCreateCommand)\" @%s:%d"
+ "\"payloadSize == sizeof(AFKMDManagerCreateResponse)\" @%s:%d"
+ "\"pktLen >= sizeof(*header)\" @%s:%d"
+ "\"pktLen >= sizeof(*respHeader)\" @%s:%d"
+ "\"pktLen >= sizeof(rv->_commandHeader) + sizeof(rv->_oobHdr)\" @%s:%d"
+ "\"pktLen >= sizeof(rv->_commandHeader)\" @%s:%d"
+ "\"processor\" @%s:%d"
+ "\"prop\" @%s:%d"
+ "\"propStr\" @%s:%d"
+ "\"queueDesc\" @%s:%d"
+ "\"ret\" @%s:%d"
+ "\"role\" @%s:%d"
+ "\"rspSize <= this->_oobHdr.rspSize\" @%s:%d"
+ "\"rtbuddy->platformParams->isACIPC\" @%s:%d"
+ "\"self->_endpointWL->inGate()\" @%s:%d"
+ "\"shmem_info\" @%s:%d"
+ "\"shmem_info->memory\" @%s:%d"
+ "\"shmem_info->memory->getBuffer()->getLength() >= size\" @%s:%d"
+ "\"status\" @%s:%d"
+ "\"this->_client == forClient\" @%s:%d"
+ "\"this->_clientWL\" @%s:%d"
+ "\"this->_clientWL->inGate()\" @%s:%d"
+ "\"this->_endpointWL->inGate()\" @%s:%d"
+ "\"this->_openSent\" @%s:%d"
+ "\"this->_pendingOffset + pktLen <= this->_pendingSize\" @%s:%d"
+ "\"this->_pendingStatesLock\" @%s:%d"
+ "\"this->_queueLock\" @%s:%d"
+ "\"this->_rspPayload.remote_addr == oobHdr->rspAddress\" @%s:%d"
+ "\"threadCall\" @%s:%d"
+ "\"token\" @%s:%d"
+ "\"total_offset >= static_offset\" @%s:%d"
+ "\"type == shmem_info->alloc_type\" @%s:%d"
+ "\"uc\" @%s:%d"
+ "\"valid && pktLen <= 4294967295U\" @%s:%d"
+ "\"valid && size <= 4294967295U\" @%s:%d"
+ "\"valid\" @%s:%d"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleFirmwareKit_kext/src/Kext/AFKFirmwareService.cpp"
+ "AFKACIPCMemoryDescriptorManager.cpp"
+ "AFKEP.cpp"
+ "AFKEPCommandContext.cpp"
+ "AFKEPInterfaceEventSourceV2.cpp"
+ "AFKEPInterfaceKextV2.cpp"
+ "AFKEPInterfaceServiceKextV2.cpp"
+ "AFKEPInterfaceV2.cpp"
+ "AFKEPKextV2.cpp"
+ "AFKEPV2.cpp"
+ "AFKEndpointInterface.cpp"
+ "AFKEndpointInterfaceRelay.cpp"
+ "AFKEndpointInterfaceUserClient.cpp"
+ "AFKIOServiceClient.cpp"
+ "AFKIOServiceClientBase.cpp"
+ "AFKLocalMemoryDescriptorManager.cpp"
+ "AFKMemoryDescriptor.cpp"
+ "AFKMemoryDescriptorImpl.cpp"
+ "AFKMemoryDescriptorManagerBase.cpp"
+ "AFKTightbeamEndpoint.cpp"
+ "Messenger.c"
+ "MessengerACIPC.c"
+ "MessengerStandard.c"
+ "UseIOPMStateControl"
- "!fail"
- "%s:%d Assertion failed: %s : 0x%lx 0x%lx "
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleFirmwareKit_kext/src/Kext/AFKFirmwareService.cpp"
- "0 == result && shmem_info->memory"
- "0 == ret"
- "add <= shmem_info->memory->getBuffer()->getLength()"
- "buffer->remote_addr == shmem_info->memory->getSlaveAddress()"
- "found"
- "lock"
- "processor"
- "rtbuddy->platformParams->isACIPC"
- "shmem_info"
- "shmem_info->memory"
- "shmem_info->memory->getBuffer()->getLength() >= size"
- "type == shmem_info->alloc_type"

```

>  `com.apple.driver.AppleSCDriver`

```diff

-20.139.0.0.0
-  __TEXT.__cstring: 0x3f9a
-  __TEXT.__os_log: 0x6188
+20.140.0.0.0
+  __TEXT.__cstring: 0x3f91
+  __TEXT.__os_log: 0x61a2
   __TEXT.__const: 0x190
-  __TEXT_EXEC.__text: 0x20f78
+  __TEXT_EXEC.__text: 0x2103c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x22c8
   __DATA.__common: 0x15a0

   __DATA_CONST.__const: 0x3b60
   __DATA_CONST.__kalloc_type: 0x340
   __DATA_CONST.__kalloc_var: 0xf0
-  Functions: 516
-  Symbols:   1465
-  CStrings:  583
+  Functions: 515
+  Symbols:   1464
+  CStrings:  582
 
Symbols:
+ __ZZN10SCodecHost36handleSessionsDemandCountChangeGatedEvE11_os_log_fmt_1
+ __ZZN10SCodecHost36handleSessionsDemandCountChangeGatedEvE11_os_log_fmt_2
+ __ZZN6SCodec31waitForStreamPreconditionsGatedEPhPjE11_os_log_fmt_2
- __ZN10SCodecHost11releaseCoreEv
- __ZZN10SCodecHost11releaseCoreEvE11_os_log_fmt
- __ZZN10SCodecHost11releaseCoreEvE11_os_log_fmt_0
- __ZZN10SCodecHost11releaseCoreEvE11_os_log_fmt_1
CStrings:
+ "1211111212221212122111111111111111111111111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222222222211111122221122222222222222222222222222222222222222222222222222222222222222222122222211"
+ "1211111212221212122111111111111111111111111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222222222211111122221122222222222222222222222222222222222222222222222222222222222222222122222211111211111111111111211211111111211112221212211222212"
+ "20:03:05"
+ "20:03:16"
+ "Jul  3 2024"
- "121111121222121212211111111111111111111111111111111111111111111111111111111111111111111111111111111222222222222222222222222222222222222222221111112222112222222222222222222222222222222222222222222222222222222222222222122222211"
- "12111112122212121221111111111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222222222111111222211222222222222222222222222222222222222222222222222222222222222222212222221111121111111111111121121111111121111222121221122221"
- "20:39:42"
- "20:39:53"
- "Jun 20 2024"
- "releaseCore"

```

>  `com.apple.driver.AppleT8110DART`

```diff

-452.0.1.0.0
+452.0.2.0.0
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x27f7
-  __TEXT_EXEC.__text: 0xd71c
+  __TEXT.__cstring: 0x2840
+  __TEXT_EXEC.__text: 0xd7e4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38

   __DATA_CONST.__const: 0xb18
   __DATA_CONST.__kalloc_type: 0x2c0
   __DATA_CONST.__kalloc_var: 0x410
-  Functions: 148
-  Symbols:   535
-  CStrings:  215
+  Functions: 149
+  Symbols:   536
+  CStrings:  217
 
Symbols:
+ _ZN14AppleT8110DART6_setupER19t8110dart_init_data.cold.5
+ __ZN14AppleT8110DART20_prepareForPowerDownEbb
+ __ZZN14AppleT8110DART10_dartSetupER19t8110dart_init_dataE21kalloc_type_view_3605
+ __ZZN14AppleT8110DART10_dartSetupER19t8110dart_init_dataE21kalloc_type_view_3650
+ __ZZN14AppleT8110DART10_dartSetupER19t8110dart_init_dataE21kalloc_type_view_3726
+ __ZZN14AppleT8110DART10_dartSetupER19t8110dart_init_dataE21kalloc_type_view_3836
+ __ZZN14AppleT8110DART17_apfSetupInstanceEjjPKNS_10instance_tER19t8110dart_init_dataE21kalloc_type_view_4637
+ __ZZN14AppleT8110DART17_apfSetupInstanceEjjPKNS_10instance_tER19t8110dart_init_dataE21kalloc_type_view_4641
+ __ZZN14AppleT8110DART17_apfSetupInstanceEjjPKNS_10instance_tER19t8110dart_init_dataE21kalloc_type_view_4796
+ __ZZN14AppleT8110DART21_dartAssignDynamicSIDEPjE21kalloc_type_view_4211
+ __ZZN14AppleT8110DART22_dartReleaseDynamicSIDEjE21kalloc_type_view_4260
+ __ZZN14AppleT8110DART26_apfInitializeStateCaptureEjE21kalloc_type_view_4841
+ __ZZN14AppleT8110DART27_dartInitializeStateCaptureEjE21kalloc_type_view_4294
+ __ZZN14AppleT8110DART27_dartInitializeStateCaptureEjE21kalloc_type_view_4303
+ __ZZN14AppleT8110DART27_smmuInitializeStateCaptureEjE21kalloc_type_view_4957
+ __ZZN14AppleT8110DART27_smmuInitializeStateCaptureEjE21kalloc_type_view_4975
+ __ZZN14AppleT8110DART27_smmuInitializeStateCaptureEjE21kalloc_type_view_4978
- __ZN14AppleT8110DART20_prepareForPowerDownEb
- __ZZN14AppleT8110DART10_dartSetupER19t8110dart_init_dataE21kalloc_type_view_3600
- __ZZN14AppleT8110DART10_dartSetupER19t8110dart_init_dataE21kalloc_type_view_3645
- __ZZN14AppleT8110DART10_dartSetupER19t8110dart_init_dataE21kalloc_type_view_3721
- __ZZN14AppleT8110DART10_dartSetupER19t8110dart_init_dataE21kalloc_type_view_3831
- __ZZN14AppleT8110DART17_apfSetupInstanceEjjPKNS_10instance_tER19t8110dart_init_dataE21kalloc_type_view_4632
- __ZZN14AppleT8110DART17_apfSetupInstanceEjjPKNS_10instance_tER19t8110dart_init_dataE21kalloc_type_view_4636
- __ZZN14AppleT8110DART17_apfSetupInstanceEjjPKNS_10instance_tER19t8110dart_init_dataE21kalloc_type_view_4791
- __ZZN14AppleT8110DART21_dartAssignDynamicSIDEPjE21kalloc_type_view_4206
- __ZZN14AppleT8110DART22_dartReleaseDynamicSIDEjE21kalloc_type_view_4255
- __ZZN14AppleT8110DART26_apfInitializeStateCaptureEjE21kalloc_type_view_4836
- __ZZN14AppleT8110DART27_dartInitializeStateCaptureEjE21kalloc_type_view_4289
- __ZZN14AppleT8110DART27_dartInitializeStateCaptureEjE21kalloc_type_view_4293
- __ZZN14AppleT8110DART27_smmuInitializeStateCaptureEjE21kalloc_type_view_4952
- __ZZN14AppleT8110DART27_smmuInitializeStateCaptureEjE21kalloc_type_view_4970
- __ZZN14AppleT8110DART27_smmuInitializeStateCaptureEjE21kalloc_type_view_4973
CStrings:
+ "\"%s requires the SPTM and is mutually exclusive with %s\" @%s:%d"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleHxDART/AppleT8110DART.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleHxDART/AppleT8110DART.h"
+ "no-sleep"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleHxDART/AppleT8110DART.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleHxDART/AppleT8110DART.h"

```

>  `com.apple.driver.AppleThunderboltUTDM`

```diff

-317.0.0.0.0
+318.0.0.0.0
   __TEXT.__cstring: 0xd48
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x12c3c
+  __TEXT_EXEC.__text: 0x12c38
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x118
   __DATA.__common: 0xe8

```

>  `com.apple.iokit.IOMobileGraphicsFamily`

```diff

-395.18.1.1.0
+395.23.1.0.0
   __TEXT.__cstring: 0x81dc
   __TEXT.__const: 0x800
-  __TEXT_EXEC.__text: 0x22f4c
+  __TEXT_EXEC.__text: 0x22f90
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2900
   __DATA.__common: 0x1c924
Symbols:
+ __ZN25IOMobileFramebufferLegacy29get_programfifo_blocked_stateEv
+ __ZN25IOMobileFramebufferLegacy29set_programfifo_blocked_stateEb
+ __ZZN25IOMobileFramebufferLegacy22record_swap_info_gatedEP18IOMFBSwapIORequest24IOMFBSwapCompletionStateE21kalloc_type_view_6539
- __ZN25IOMobileFramebufferLegacy27get_swap_wait_blocked_stateEv
- __ZN25IOMobileFramebufferLegacy27set_swap_wait_blocked_stateEb
- __ZZN25IOMobileFramebufferLegacy22record_swap_info_gatedEP18IOMFBSwapIORequest24IOMFBSwapCompletionStateE21kalloc_type_view_6533
CStrings:
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOMobileFramebuffer/Kernel/AppleDisplayPipe/DriverCommonFunctions.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOMobileFramebuffer/Kernel/AppleDisplayPipe/DriverCommonFunctions.cpp"

```

>  `com.apple.iokit.IOThunderboltFamily`

```diff

-6767.0.0.0.0
-  __TEXT.__cstring: 0x32b4d
+6769.0.0.0.0
+  __TEXT.__cstring: 0x32b4e
   __TEXT.__os_log: 0x2db0c
   __TEXT.__const: 0x7e4
-  __TEXT_EXEC.__text: 0x19c4f0
+  __TEXT_EXEC.__text: 0x19c654
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xb1a
   __DATA.__common: 0x1238

   __DATA_CONST.__got: 0x150
   __DATA_CONST.__mod_init_func: 0x3a0
   __DATA_CONST.__mod_term_func: 0x3a0
-  __DATA_CONST.__const: 0x334e8
+  __DATA_CONST.__const: 0x334f8
   __DATA_CONST.__kalloc_type: 0x1d40
   __DATA_CONST.__kalloc_var: 0xaf0
-  Functions: 6230
-  Symbols:   9863
+  Functions: 6232
+  Symbols:   9865
   CStrings:  2779
 
Symbols:
+ __ZN23IOThunderboltCableState20setIsCableAsymmetricEb
+ __ZNK23IOThunderboltCableState17isCableAsymmetricEv
CStrings:
+ "1212222221"
+ "20:04:28"
+ "Jul  3 2024"
- "121222221"
- "20:34:11"
- "Jun 20 2024"

```

>  `com.apple.plugin.IOAVBDiscoveryPlugin`

```diff

-1300.21.0.0.0
-  __TEXT.__cstring: 0x799
+1300.22.0.0.0
+  __TEXT.__cstring: 0x7b1
   __TEXT.__os_log: 0x1abb
   __TEXT.__const: 0x66
-  __TEXT_EXEC.__text: 0x7834
+  __TEXT_EXEC.__text: 0x7898
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x100
-  __DATA_CONST.__auth_got: 0x168
+  __DATA_CONST.__auth_got: 0x170
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__mod_init_func: 0x30
   __DATA_CONST.__mod_term_func: 0x30
-  __DATA_CONST.__const: 0x3430
+  __DATA_CONST.__const: 0x3470
   __DATA_CONST.__kalloc_type: 0x180
-  Functions: 161
-  Symbols:   699
-  CStrings:  71
+  Functions: 163
+  Symbols:   705
+  CStrings:  72
 
Symbols:
+ __NSConcreteGlobalBlock
+ __ZN12OSCollection14iterateObjectsEU13block_pointerFbP8OSObjectE
+ __ZN21IOAVB17221LocalEntity19resetAvailableIndexEv
+ ____ZN25IOAVB17221EntityDiscovery14cableRepluggedEv_block_invoke
+ ___block_descriptor_tmp
+ ___block_literal_global
CStrings:
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBDiscoveryPlugin/IOAVB17221Entity.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBDiscoveryPlugin/IOAVB17221EntityDiscovery.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBDiscoveryPlugin/IOAVB17221EntityDiscoveryUserClient.cpp"
+ "B16@?0^{OSObject=^^?i}8"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBDiscoveryPlugin/IOAVB17221Entity.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBDiscoveryPlugin/IOAVB17221EntityDiscovery.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBDiscoveryPlugin/IOAVB17221EntityDiscoveryUserClient.cpp"

```

>  `com.apple.driver.AppleAVE2`

```diff

-802.37.1.0.0
-  __TEXT.__const: 0x28bb0
-  __TEXT.__cstring: 0x332fd
-  __TEXT.__os_log: 0x3ca20
-  __TEXT_EXEC.__text: 0x131ffc
+802.61.1.0.0
+  __TEXT.__const: 0x2e8b0
+  __TEXT.__cstring: 0x34a98
+  __TEXT.__os_log: 0x3f635
+  __TEXT_EXEC.__text: 0x13e708
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x288
-  __DATA.__common: 0x108
-  __DATA.__bss: 0x300
+  __DATA.__data: 0x290
+  __DATA.__common: 0x130
+  __DATA.__bss: 0x560
   __DATA_CONST.__auth_got: 0x3e0
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__mod_init_func: 0x30
-  __DATA_CONST.__mod_term_func: 0x30
-  __DATA_CONST.__const: 0x6960
-  __DATA_CONST.__kalloc_type: 0x1e80
-  __DATA_CONST.__kalloc_var: 0x1310
-  Functions: 2344
-  Symbols:   7961
-  CStrings:  4330
+  __DATA_CONST.__mod_init_func: 0x38
+  __DATA_CONST.__mod_term_func: 0x38
+  __DATA_CONST.__const: 0x70e8
+  __DATA_CONST.__kalloc_type: 0x1f40
+  __DATA_CONST.__kalloc_var: 0x1090
+  Functions: 2431
+  Symbols:   8304
+  CStrings:  4463
 
Symbols:
+ _GLOBAL__sub_I_AVE_Thread.cpp
+ _Z22AVE_AXI2AF_GetTunables12_E_AVE_DevIDjiPPK17_S_AVE_AXI2AF_Cfg.cold.46
+ _Z22AVE_AXI2AF_GetTunables12_E_AVE_DevIDjiPPK17_S_AVE_AXI2AF_Cfg.cold.47
+ _Z23AVE_TaskCmd_GOPDecisionPvS_Pii.cold.1
+ _ZN7AVE_Drv22AdjustClientByPriorityEP13_S_AVE_Client.cold.2
+ __Z12AVE_EUID2IdxP12_S_AVE_EUMapPii
+ __Z13AVE_Log_CheckP10_S_AVE_Log
+ __Z13AVE_SortEUMapP12_S_AVE_EUMap
+ __Z14AVE_CheckEUMap12_E_AVE_DevIDiP12_S_AVE_EUMap
+ __Z15AVE_CheckDLBCfg12_E_AVE_DevIDP14_S_AVE_DLB_Cfg
+ __Z15AVE_CheckDPMCfgP14_S_AVE_DPM_Cfg
+ __Z16AVE_CheckQualitydi
+ __Z17AVE_CheckDPMRangeP16_S_AVE_DPM_Range
+ __Z17AVE_Client_ConfigP13_S_AVE_ClientP21_S_AVE_SurfaceIDInSet
+ __Z17AVE_Client_InitPSP13_S_AVE_Clienti
+ __Z17AVE_Client_SetDLBP13_S_AVE_Clienti
+ __Z17AVE_DLB_AllocUnitP10_S_AVE_DLBP15_S_AVE_DLB_Unit
+ __Z17AVE_DLB_CleanInfoP10_S_AVE_DLBP15_S_AVE_DLB_Info
+ __Z17AVE_DLB_CleanUnitP10_S_AVE_DLBP15_S_AVE_DLB_Unit
+ __Z17AVE_DLB_PrintUnitP15_S_AVE_DLB_UnitjiPKci
+ __Z17AVE_Pipeline_InitP15_S_AVE_PipelineyPv
+ __Z18AVE_DLB_AllocEUNumP10_S_AVE_DLBiP13_S_AVE_DLNode
+ __Z18AVE_DLB_AssignUnitP10_S_AVE_DLBP15_S_AVE_DLB_Unit15_E_AVE_WorkTypeii
+ __Z18AVE_DLB_SelectUnitP10_S_AVE_DLBP18_S_AVE_DLB_UnitCfgP15_S_AVE_DLB_Unit
+ __Z18AVE_TaskCmd_CreatePviS_j
+ __Z19AVE_CheckDLBUnitCfg12_E_AVE_DevIDP18_S_AVE_DLB_UnitCfg
+ __Z19AVE_Client_AssignEUP13_S_AVE_ClientP15_S_AVE_DLB_Info
+ __Z19AVE_DLB_ApplyStaticP10_S_AVE_DLBP13_S_AVE_ClientP15_S_AVE_DLB_Info
+ __Z19AVE_Pipeline_ConfigP15_S_AVE_Pipeline
+ __Z19AVE_SVESched_ConfigP15_S_AVE_SVESchediP12_S_AVE_EUMapi
+ __Z19AVE_TaskCmd_DestroyP14_S_AVE_TaskCmd
+ __Z20AVE_CHM_CalcDPMStatsP10_S_AVE_CHMP20_S_AVE_DPM_ThresholdP15_S_AVE_DPMStats
+ __Z20AVE_Client_ConfigDLBP13_S_AVE_Client
+ __Z20AVE_Client_PreUpdateP13_S_AVE_ClientP18_S_AVE_ClientStatsP16_S_AVE_FrameInfo
+ __Z20AVE_ComposeStr_EUMapP12_S_AVE_EUMapPci
+ __Z20AVE_DLB_ApplyDynamicP10_S_AVE_DLBP13_S_AVE_DLNode
+ __Z20AVE_IOP_Start_ErebusP7AVE_Reg
+ __Z20AVE_UCCmd_CheckParam12_E_AVE_DevID17_E_AVE_ClientTypeP16_S_AVE_UCInParam
+ __Z21AVE_Client_PostUpdateP13_S_AVE_ClientP16_S_AVE_FrameInfo
+ __Z21AVE_IOP_Config_ErebusP7AVE_Regy
+ __Z21AVE_Pipeline_DestructP15_S_AVE_Pipeline
+ __Z21AVE_Pipeline_GetMDNumP15_S_AVE_Pipelinej
+ __Z21AVE_Pipeline_PrintAllP15_S_AVE_PipelinejiPKci
+ __Z22AVE_Pipeline_AssignEUCP15_S_AVE_PipelineP15_S_AVE_DLB_Info
+ __Z22AVE_Pipeline_ConstructP15_S_AVE_Pipeline15_E_AVE_Pipeline
+ __Z22AVE_Pipeline_PreUpdateP15_S_AVE_PipelineP16_S_AVE_FrameInfo
+ __Z22AVE_Pipeline_PrintCmdsP15_S_AVE_PipelinejiPKci
+ __Z22AVE_Work_Enc_ConfigDLBP13_S_AVE_ClientP18_S_AVE_DLB_UnitCfgS2_P15_S_AVE_DLB_Unit
+ __Z22AVE_Work_Enc_PreUpdateP13_S_AVE_ClientP15_S_AVE_DLB_UnitP16_S_AVE_FrameInfo
+ __Z23AVE_CalcBufNumOfMBStatsbiiiiiibb16_E_AVE_MCTF_Modei13_E_AVE_RCModei
+ __Z23AVE_CalcNumOfInputQueue17_E_AVE_ClientTypeiiiiiiibb16_E_AVE_MCTF_Modei13_E_AVE_RCModei
+ __Z23AVE_DLB_CompStr_EUStatsPP18_S_AVE_DLB_EUStatsiPci
+ __Z23AVE_GOPDecision_PrepareP10_S_AVE_CHMP15AVE_GOPDecisionP10FrameStatsP12AVE_KeyFramejiiP26_S_AVE_TaskCmd_GOPDecisionPA4_P10_S_AVE_CmdPP16_S_AVE_FrameInfoPiPA3_iPA2_iSK_SI_
+ __Z23AVE_Pipeline_PostUpdateP15_S_AVE_PipelineP16_S_AVE_FrameInfo
+ __Z23AVE_PrintClientSurfacesP23_S_AVE_ClientSurfaceSetji
+ __Z23AVE_TaskCmd_GOPDecisionPvS_Pii
+ __Z23AVE_Work_Enc_CalcRefNumP13_S_AVE_Clienti
+ __Z23AVE_Work_Enc_PostUpdateP13_S_AVE_ClientP16_S_AVE_FrameInfo
+ __Z23AVE_Work_LRME_ConfigDLBP13_S_AVE_ClientP18_S_AVE_DLB_UnitCfgS2_P15_S_AVE_DLB_Unit
+ __Z23AVE_Work_LRME_PreUpdateP13_S_AVE_ClientP16_S_AVE_FrameInfo
+ __Z23AVE_Work_MCTF_ConfigDLBP13_S_AVE_ClientP18_S_AVE_DLB_UnitCfgS2_P15_S_AVE_DLB_Unit
+ __Z23AVE_Work_MCTF_PreUpdateP13_S_AVE_ClientP16_S_AVE_FrameInfo
+ __Z24AVE_IOP_CheckIdle_ErebusP7AVE_Reg
+ __Z24AVE_Pipeline_DropAllCmdsP15_S_AVE_Pipelinejj
+ __Z24AVE_Pipeline_PrintStatusP15_S_AVE_PipelinejiPKci
+ __Z24AVE_Work_Enc_ConfigEUMapP13_S_AVE_ClientP11AVE_DevInfoP18_S_AVE_DLB_UnitCfgS4_P15_S_AVE_DLB_Unit
+ __Z24AVE_Work_LAGOP_ConfigDLBP18_S_AVE_DLB_UnitCfgS0_P15_S_AVE_DLB_Unit
+ __Z24AVE_Work_LRME_CalcRefNumP13_S_AVE_Clienti
+ __Z24AVE_Work_LRME_PostUpdateP13_S_AVE_ClientP16_S_AVE_FrameInfoP14CODED_DATA_HDR
+ __Z24AVE_Work_MCTF_CalcRefNumP13_S_AVE_Clienti
+ __Z24AVE_Work_MCTF_PostUpdateP13_S_AVE_ClientP16_S_AVE_FrameInfoP14CODED_DATA_HDR
+ __Z25AVE_CHM_PrintCmdsInStagesP10_S_AVE_CHMjjji
+ __Z25AVE_CalcBufNumOfCodedDataiiiiiibb16_E_AVE_MCTF_Modei13_E_AVE_RCModei
+ __Z25AVE_UCCmd_CheckParam_Open12_E_AVE_DevID17_E_AVE_ClientTypeP20S_AVE_UCInParam_Open
+ __Z25AVE_UCCmd_CheckParam_Stop12_E_AVE_DevID17_E_AVE_ClientTypeP20S_AVE_UCInParam_Stop
+ __Z25AVE_Work_LRME_ConfigEUMapP13_S_AVE_ClientP11AVE_DevInfoP18_S_AVE_DLB_UnitCfgS4_P15_S_AVE_DLB_Unit
+ __Z25AVE_Work_MCTF_ConfigEUMapP13_S_AVE_ClientP11AVE_DevInfoP18_S_AVE_DLB_UnitCfgS4_P15_S_AVE_DLB_Unit
+ __Z26AVE_CreateExternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceIDInSetP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSet
+ __Z26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSet
+ __Z26AVE_IOP_GetCurrTime_ErebusP7AVE_Reg
+ __Z26AVE_Pipeline_PrintCmdStatsP15_S_AVE_PipelinejiPKci
+ __Z26AVE_TaskCmd_IntraInterCostPvS_Pii
+ __Z26AVE_UCCmd_CheckParam_Close12_E_AVE_DevID17_E_AVE_ClientTypeP21S_AVE_UCInParam_Close
+ __Z26AVE_UCCmd_CheckParam_Flush12_E_AVE_DevID17_E_AVE_ClientTypeP21S_AVE_UCInParam_Flush
+ __Z26AVE_UCCmd_CheckParam_Reset12_E_AVE_DevID17_E_AVE_ClientTypeP21S_AVE_UCInParam_Reset
+ __Z26AVE_UCCmd_CheckParam_Start12_E_AVE_DevID17_E_AVE_ClientTypeP21S_AVE_UCInParam_Start
+ __Z26AVE_Work_Enc_ConfigDLBFlagP13_S_AVE_ClientP18_S_AVE_DLB_UnitCfgS2_P15_S_AVE_DLB_Unit
+ __Z26AVE_Work_Enc_DecideDLBFlagP13_S_AVE_ClientP18_S_AVE_DLB_UnitCfg
+ __Z26AVE_Work_LAGOP_ConfigEUMapP18_S_AVE_DLB_UnitCfgS0_P15_S_AVE_DLB_Unit
+ __Z27AVE_CalcBufNumOfCodedHeader17_E_AVE_ClientTypeiiiiiibb16_E_AVE_MCTF_Modei13_E_AVE_RCModei
+ __Z27AVE_CalcBufNumOfSliceHeader16_E_AVE_CodecTypeiiiiiibb16_E_AVE_MCTF_Modei13_E_AVE_RCModei
+ __Z27AVE_CheckExternalInSurfacesP17_S_AVE_SurfaceSetP21_S_AVE_SurfaceInfoSety
+ __Z27AVE_ClientList_CalcDLBStatsP13_S_AVE_DLNodeP16_S_AVE_DLB_Stats
+ __Z27AVE_Client_CalcPerfNumOfCHMP13_S_AVE_Clienti15_E_AVE_WorkTypePi
+ __Z27AVE_Pipeline_CreateSurfacesP15_S_AVE_PipelineP21_S_AVE_SurfaceIDInSet
+ __Z27AVE_Pipeline_GetCmdCntInAllP15_S_AVE_Pipelinej
+ __Z27AVE_UCCmd_CheckParam_Config12_E_AVE_DevID17_E_AVE_ClientTypeP22S_AVE_UCInParam_Config
+ __Z27AVE_Work_Enc_CalcRefNum_ExtP13_S_AVE_Clienti
+ __Z27AVE_Work_LRME_ConfigDLBFlagP13_S_AVE_ClientP18_S_AVE_DLB_UnitCfgS2_P15_S_AVE_DLB_Unit
+ __Z27AVE_Work_LRME_DecideDLBFlagP18_S_AVE_DLB_UnitCfgi
+ __Z27AVE_Work_MCTF_ConfigDLBFlagP13_S_AVE_ClientP18_S_AVE_DLB_UnitCfgS2_P15_S_AVE_DLB_Unit
+ __Z27AVE_Work_MCTF_DecideDLBFlagP18_S_AVE_DLB_UnitCfgi
+ __Z28AVE_Client_AddDLBStatsPerCHMP13_S_AVE_Clientj15_E_AVE_WorkTypeP12_S_AVE_EUMapP18_S_AVE_DLB_EUStats
+ __Z28AVE_Client_ConfigSurfacePoolP13_S_AVE_Client
+ __Z28AVE_Client_SubDLBStatsPerCHMP13_S_AVE_Clientj15_E_AVE_WorkTypeP12_S_AVE_EUMapP18_S_AVE_DLB_EUStats
+ __Z28AVE_CreateExternalInSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceIDInSetyP17_S_AVE_SurfaceSet
+ __Z28AVE_Pipeline_CalcSurfaceInfoP15_S_AVE_Pipeline
+ __Z28AVE_Pipeline_DARTMapSurfacesP15_S_AVE_Pipeline
+ __Z28AVE_Pipeline_DestroySurfacesP15_S_AVE_Pipeline
+ __Z28AVE_TaskCmd_GOPDecision_InitP15AVE_GOPDecisionjiiiPiPxP26_S_AVE_TaskCmd_GOPDecision
+ __Z28AVE_UCCmd_CheckParam_Prepare12_E_AVE_DevID17_E_AVE_ClientTypeP23S_AVE_UCInParam_Prepare
+ __Z28AVE_UCCmd_CheckParam_Process12_E_AVE_DevID17_E_AVE_ClientTypeP23S_AVE_UCInParam_Process
+ __Z28AVE_Work_Enc_CalcSurfaceInfoP13_S_AVE_ClientP15_S_AVE_DLB_UnitP21_S_AVE_SurfaceInfoSet
+ __Z28AVE_Work_IntraPred_ConfigDLBP18_S_AVE_DLB_UnitCfgS0_P15_S_AVE_DLB_Unit
+ __Z28AVE_Work_LAGOP_ConfigDLBFlagP18_S_AVE_DLB_UnitCfgS0_P15_S_AVE_DLB_Unit
+ __Z28AVE_Work_LAGOP_DecideDLBFlagP18_S_AVE_DLB_UnitCfg
+ __Z29AVE_CalcBufNumOfProtectedDatabiiiiiibb16_E_AVE_MCTF_Modei13_E_AVE_RCModei
+ __Z29AVE_CalcBufTypeNumOfLowResRefb
+ __Z29AVE_CreateExternalOutSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSet
+ __Z29AVE_Pipeline_GetCmdCntInInputP15_S_AVE_Pipelinej
+ __Z29AVE_Pipeline_GetCmdCntInStageP15_S_AVE_Pipeline15_E_AVE_MD_Stagej
+ __Z29AVE_UCCmd_CheckParam_Complete12_E_AVE_DevID17_E_AVE_ClientTypeP24S_AVE_UCInParam_Complete
+ __Z29AVE_Work_Enc_CalcDPMThresholdiibbP20_S_AVE_DPM_Threshold
+ __Z29AVE_Work_LRME_CalcSurfaceInfoP13_S_AVE_ClientP15_S_AVE_DLB_UnitP21_S_AVE_SurfaceInfoSet
+ __Z29AVE_Work_MCTF_CalcSurfaceInfoP13_S_AVE_ClientP15_S_AVE_DLB_UnitP21_S_AVE_SurfaceInfoSet
+ __Z30AVE_Pipeline_CalcInputQueueNumP15_S_AVE_Pipelinei
+ __Z30AVE_Pipeline_DARTUnmapSurfacesP15_S_AVE_PipelinePy
+ __Z30AVE_Pipeline_GetAdaptBPOCDelayP15_S_AVE_Pipeline
+ __Z30AVE_Pipeline_GetCmdCntInOutputP15_S_AVE_Pipelinej
+ __Z30AVE_Pipeline_GetCmdCntInStagesP15_S_AVE_Pipelinejj
+ __Z30AVE_TaskCmd_GOPDecision_UninitP26_S_AVE_TaskCmd_GOPDecision
+ __Z30AVE_Work_IntraPred_ConfigEUMapP18_S_AVE_DLB_UnitCfgS0_P15_S_AVE_DLB_Unit
+ __Z30AVE_Work_LRME_CalcDPMThresholdiP20_S_AVE_DPM_Threshold
+ __Z30AVE_Work_MCTF_CalcDPMThresholdiP20_S_AVE_DPM_Threshold
+ __Z31AVE_CalcBufNumOfLowResRefChromav
+ __Z31AVE_TaskCmd_IntraInterCost_InitP15AVE_GOPDecisionP13AVE_IntraPrediPiPxP29_S_AVE_TaskCmd_IntraInterCost
+ __Z31AVE_Work_Enc_CalcNumOfInputDataiiiiiibb16_E_AVE_MCTF_Modei13_E_AVE_RCModeii
+ __Z32AVE_CalcBufSizeOfLowResRefChromav
+ __Z32AVE_CalcBufSizeOfSrcNeighborData14_E_AVE_DevType16_E_AVE_CodecTypei
+ __Z32AVE_CalcBufTypeNumOfLowResResultb
+ __Z32AVE_Work_IntraPred_ConfigDLBFlagP18_S_AVE_DLB_UnitCfgS0_P15_S_AVE_DLB_Unit
+ __Z32AVE_Work_IntraPred_DecideDLBFlagP18_S_AVE_DLB_UnitCfg
+ __Z32AVE_Work_LRME_CalcNumOfInputDatai
+ __Z32AVE_Work_MCTF_CalcNumOfInputDatai16_E_AVE_MCTF_Mode
+ __Z33AVE_TaskCmd_IntraInterCost_UninitP29_S_AVE_TaskCmd_IntraInterCost
+ __Z33AVE_Work_LAGOP_CalcNumOfInputDatav
+ __Z34AVE_CalcBufTypeNumOfLowResRCResultb
+ __Z35AVE_Analytics_CollectThroughputModeP16_S_AVE_Analytics21_E_AVE_ThroughputMode
+ __Z35AVE_CalcBufNumOfEntropyCodingHeader14_E_AVE_DevType
+ __Z35AVE_CalcBufNumOfLowResRefLumaHeader14_E_AVE_DevType17_E_AVE_ClientTypeiiibbib
+ __Z35AVE_TaskCmd_IntraInterCost_SetInputP29_S_AVE_TaskCmd_IntraInterCostP15AVE_GOPDecisionP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoyi
+ __Z36AVE_CalcBufSizeOfEntropyCodingHeaderi
+ __Z36AVE_CalcBufSizeOfLowResRefLumaHeader14_E_AVE_DevType17_E_AVE_ClientType16_E_AVE_CodecTypeii
+ __Z37AVE_CalcBufNumOfLowResRefChromaHeaderv
+ __Z37AVE_Work_Enc_UpdateFrameInfoFromStatsP13_S_AVE_ClientP16_S_AVE_FrameInfoP20S_AVE_DRC_FrameStats
+ __Z37AVE_Work_IntraPred_CalcNumOfInputDatav
+ __Z38AVE_CalcBufSizeOfLowResRefChromaHeaderv
+ __Z38AVE_Pipeline_GetExternalOutSurfacesSetP15_S_AVE_PipelinePP17_S_AVE_SurfaceSet
+ __Z42AVE_Work_Enc_UpdateFrameInfoFromOutputDataP13_S_AVE_ClientiP16_S_AVE_FrameInfoP14CODED_DATA_HDR
+ __ZL14AVE_Thread_ktv
+ __ZL17gsc_faAVE_TaskCmd
+ __ZL23AVE_SwC_CalcTaskBufSizePK13_S_AVE_Client
+ __ZL27gsc_sAVE_DevCap_CEntry_8150
+ __ZL29gsc_sAVE_DPE_CfgSet_Upis_8142
+ __ZL31gsc_sAVE_DPE_CfgSet_Erebus_8150
+ __ZL31gsc_sAVE_DevCap_SEntry_AVC_8150
+ __ZL31gsc_sAVE_DevCap_SEntry_GGM_8150
+ __ZL32gsc_sAVE_DevCap_SEntry_HEVC_8150
+ __ZL32gsc_sAVE_DevCap_SEntry_LRME_8150
+ __ZL32gsc_sAVE_DevCap_SEntry_MCTF_8150
+ __ZL32gsc_sAVE_DevCfg_Entry_AVC_Erebus
+ __ZL32gsc_saAVE_AXI2AF_Cfg_Erebus_8150
+ __ZL39gsc_saAVE_DPE_RegCfg_CAC_8bit_Upis_8142
+ __ZL39gsc_saAVE_DPE_RegCfg_CAT_8bit_Upis_8142
+ __ZL40gsc_saAVE_DPE_RegCfg_CAC_10bit_Upis_8142
+ __ZL40gsc_saAVE_DPE_RegCfg_CAT_10bit_Upis_8142
+ __ZL41gsc_saAVE_DPE_RegCfg_CAC_8bit_Erebus_8150
+ __ZL41gsc_saAVE_DPE_RegCfg_CAT_8bit_Erebus_8150
+ __ZL42gsc_saAVE_DPE_RegCfg_CAC_10bit_Erebus_8150
+ __ZL42gsc_saAVE_DPE_RegCfg_CAC_Default_Upis_8142
+ __ZL42gsc_saAVE_DPE_RegCfg_CAT_10bit_Erebus_8150
+ __ZL42gsc_saAVE_DPE_RegCfg_CAT_Default_Upis_8142
+ __ZL43gsc_saAVE_AXI2AF_RegCfg_Default_Erebus_8150
+ __ZL44gsc_saAVE_DPE_RegCfg_CAC_Default_Erebus_8150
+ __ZL44gsc_saAVE_DPE_RegCfg_CAT_Default_Erebus_8150
+ __ZN10AVE_MD_SVE10PostUpdateEP16_S_AVE_FrameInfo
+ __ZN10AVE_MD_SVE15CalcSurfaceInfoEv
+ __ZN10AVE_MD_SVE15GetOutputBufNumEv
+ __ZN10AVE_MD_SVE16AcquireOutputBufEP10_S_AVE_Cmdi
+ __ZN10AVE_MD_SVE16ReleaseOutputBufEP10_S_AVE_Cmdi
+ __ZN10AVE_MD_SVE17CalcInputQueueNumEv
+ __ZN10AVE_MD_SVE20CheckOutputBuf_QuotaEi
+ __ZN10AVE_MD_SVE22CreateExternalSurfacesEP21_S_AVE_SurfaceIDInSet
+ __ZN10AVE_MD_SVE22CreateInternalSurfacesEv
+ __ZN10AVE_MD_SVE22UpdateOutputBuf_StatusEi
+ __ZN10AVE_MD_SVE23DARTMapExternalSurfacesEv
+ __ZN10AVE_MD_SVE23DARTMapInternalSurfacesEv
+ __ZN10AVE_MD_SVE23DestroyExternalSurfacesEv
+ __ZN10AVE_MD_SVE23DestroyInternalSurfacesEv
+ __ZN10AVE_MD_SVE24CheckOutputBuf_AvailableEi
+ __ZN10AVE_MD_SVE25DARTUnmapExternalSurfacesEy
+ __ZN10AVE_MD_SVE25DARTUnmapInternalSurfacesEy
+ __ZN10AVE_MD_SVE8PrintAllEjiPKci
+ __ZN10AVE_MD_SVE9ConfigDLBEv
+ __ZN10AVE_MD_SVE9PreUpdateEP16_S_AVE_FrameInfo
+ __ZN10AVE_SVEDPB4InitEjiiiiPA2_A17_P11AVE_SurfacePS1_S5_S5_S5_PA2_A10_S1_S8_
+ __ZN10AVE_Thread10CondSignalEPv
+ __ZN10AVE_Thread10gMetaClassE
+ __ZN10AVE_Thread10superClassE
+ __ZN10AVE_Thread13CondTimedWaitEPvS0_jj
+ __ZN10AVE_Thread18ProcessTerminationEv
+ __ZN10AVE_Thread4InitEj
+ __ZN10AVE_Thread5ResetEv
+ __ZN10AVE_Thread6ThreadEv
+ __ZN10AVE_Thread6UninitEv
+ __ZN10AVE_Thread8CondWaitEPvS0_
+ __ZN10AVE_Thread9MetaClassC1Ev
+ __ZN10AVE_Thread9MetaClassC2Ev
+ __ZN10AVE_Thread9MetaClassD0Ev
+ __ZN10AVE_Thread9MetaClassD1Ev
+ __ZN10AVE_Thread9metaClassE
+ __ZN10AVE_ThreadC2EPK11OSMetaClass
+ __ZN10AVE_ThreadD0Ev
+ __ZN10AVE_ThreadD1Ev
+ __ZN10AVE_ThreadD2Ev
+ __ZN10AVE_ThreaddlEPvm
+ __ZN10AVE_ThreadnwEm
+ __ZN12AVE_MD_LAGOP17CalcInputQueueNumEv
+ __ZN12AVE_MD_LAGOP8PrintAllEjiPKci
+ __ZN12AVE_MD_LAGOP9ConfigDLBEv
+ __ZN12AVE_WorkPool11CheckCmdCntEv
+ __ZN12AVE_WorkPool11MarkSkipCmdEP14_S_AVE_TaskCmd
+ __ZN12AVE_WorkPool12CreateThreadEi
+ __ZN12AVE_WorkPool12ProcessSleepEv
+ __ZN12AVE_WorkPool13NotifyCmdDoneEP14_S_AVE_TaskCmd
+ __ZN12AVE_WorkPool13ProcessNewCmdEv
+ __ZN12AVE_WorkPool14ClearCmdInTaskEP11_S_AVE_Task
+ __ZN12AVE_WorkPool14RequestTaskCmdEP14_S_AVE_WPParamiP11_S_AVE_Task
+ __ZN12AVE_WorkPool14WaitThreadIdleEj
+ __ZN12AVE_WorkPool15CheckTaskCmdCntEPK11_S_AVE_Task
+ __ZN12AVE_WorkPool15ProcessInputCmdEv
+ __ZN12AVE_WorkPool16ProcessOutputCmdEv
+ __ZN12AVE_WorkPool17GetIdleThreadInfoEPiS0_
+ __ZN12AVE_WorkPool18ClearCmdInPriorityEP13_S_AVE_DLNode
+ __ZN12AVE_WorkPool21ProcessInputCmdInTaskEP11_S_AVE_Task
+ __ZN12AVE_WorkPool22ProcessOutputCmdInTaskEP11_S_AVE_Task
+ __ZN12AVE_WorkPool25ProcessInputCmdInPriorityEP13_S_AVE_DLNode
+ __ZN12AVE_WorkPool26ProcessOutputCmdInPriorityEP13_S_AVE_DLNode
+ __ZN12AVE_WorkPool6ThreadEv
+ __ZN12AVE_WorkPool7MoveCmdEP14_S_AVE_TaskCmd15_E_AVE_WP_StageS2_
+ __ZN12AVE_WorkPool7SkipCmdEP14_S_AVE_TaskCmd
+ __ZN12AVE_WorkPool8ClearCmdEv
+ __ZN12AVE_WorkPool8OpenTaskEPK20S_AVE_WPInParam_OpenPP11_S_AVE_Task
+ __ZN12AVE_WorkPool9NotifyCmdEP14_S_AVE_TaskCmdi
+ __ZN12AVE_WorkPool9WaitEventEv
+ __ZN14AVE_WorkThread10ProcessCmdEv
+ __ZN14AVE_WorkThread12ProcessEventEv
+ __ZN14AVE_WorkThread6ThreadEv
+ __ZN14AVE_WorkThread9NotifyCmdEP14_S_AVE_TaskCmd
+ __ZN14AVE_WorkThread9WaitEventEv
+ __ZN15AVE_GOPDecision15MiniGOPDecisionEPA3_KiS2_PS0_PA2_S0_S5_PK19_S_AVE_KeyFrameHintiiiii
+ __ZN15AVE_GOPDecision17ScenecutDetectionEPA3_KiPA2_S0_PS0_i
+ __ZN16AVE_MD_IntraPred14PrepareTaskCmdEP14_S_AVE_CmdInfoP16_S_AVE_FrameInfo
+ __ZN16AVE_MD_IntraPred17CalcInputQueueNumEv
+ __ZN16AVE_MD_IntraPred8PrintAllEjiPKci
+ __ZN16AVE_MD_IntraPred9ConfigDLBEv
+ __ZN6AVE_MD10PostUpdateEP16_S_AVE_FrameInfo
+ __ZN6AVE_MD10ProcessRunEv
+ __ZN6AVE_MD11PrintStatusEjiPKci
+ __ZN6AVE_MD12ProcessReadyEv
+ __ZN6AVE_MD13PrintCmdStatsEjjiPKci
+ __ZN6AVE_MD14GetCmdCntInRunEj
+ __ZN6AVE_MD16GetCmdCntInReadyEj
+ __ZN6AVE_MD17CalcInputQueueNumEv
+ __ZN6AVE_MD17PrintCmdsInStagesEjjji
+ __ZN6AVE_MD8PrintAllEjiPKci
+ __ZN6AVE_MD9AssignEUCEP15_S_AVE_DLB_Unit
+ __ZN6AVE_MD9AttachEUCEv
+ __ZN6AVE_MD9ConfigDLBEv
+ __ZN6AVE_MD9DetachEUCEv
+ __ZN6AVE_MD9PreUpdateEP16_S_AVE_FrameInfo
+ __ZN7AVE_DPM4InitEP11AVE_DevInfoPK10_S_AVE_CfgjP8AVE_PMGR
+ __ZN8Analyzer13storeLRMECostEPA3_KiiPA4_i
+ __ZN8Analyzer15miniGopDecisionEPA3_KiS2_PS0_PA2_S0_S5_PK19_S_AVE_KeyFrameHintiiiiibi
+ __ZN8Analyzer17scenecutDetectionEjPKiPA3_S0_PA2_S0_S1_j
+ __ZNK10AVE_Thread12getMetaClassEv
+ __ZNK10AVE_Thread9MetaClass5allocEv
+ __ZTV10AVE_Thread
+ __ZTVN10AVE_Thread9MetaClassE
+ __ZZ13AVE_DLB_CleanP10_S_AVE_DLBP13_S_AVE_DLNodeE11_os_log_fmt_0
+ __ZZ16AVE_CHM_SetFwBufP10_S_AVE_CHMP17_S_AVE_SurfaceSetP21_S_AVE_SurfaceInfoSetP16AVE_VIDEO_PARAMSE11_os_log_fmt__28_
+ __ZZ16AVE_CHM_SetFwBufP10_S_AVE_CHMP17_S_AVE_SurfaceSetP21_S_AVE_SurfaceInfoSetP16AVE_VIDEO_PARAMSE11_os_log_fmt__29_
+ __ZZ16AVE_CHM_SetFwBufP10_S_AVE_CHMP17_S_AVE_SurfaceSetP21_S_AVE_SurfaceInfoSetP16AVE_VIDEO_PARAMSE11_os_log_fmt__30_
+ __ZZ16AVE_CHM_SetFwBufP10_S_AVE_CHMP17_S_AVE_SurfaceSetP21_S_AVE_SurfaceInfoSetP16AVE_VIDEO_PARAMSE11_os_log_fmt__31_
+ __ZZ16AVE_CHM_SetFwBufP10_S_AVE_CHMP17_S_AVE_SurfaceSetP21_S_AVE_SurfaceInfoSetP16AVE_VIDEO_PARAMSE11_os_log_fmt__32_
+ __ZZ16AVE_Client_PrintP13_S_AVE_ClientjiPKciE11_os_log_fmt_7
+ __ZZ16AVE_Client_PrintP13_S_AVE_ClientjiPKciE11_os_log_fmt_8
+ __ZZ16AVE_Client_StartP13_S_AVE_ClientP14_S_AVE_TimeOutiP21_S_AVE_SurfaceIDInSetP35AVE_SessionSettings_UserKernel_DataPKcE11_os_log_fmt_7
+ __ZZ16AVE_Client_StartP13_S_AVE_ClientP14_S_AVE_TimeOutiP21_S_AVE_SurfaceIDInSetP35AVE_SessionSettings_UserKernel_DataPKcE11_os_log_fmt__12_
+ __ZZ17AVE_Client_ConfigP13_S_AVE_ClientP21_S_AVE_SurfaceIDInSetE11_os_log_fmt
+ __ZZ17AVE_Client_ConfigP13_S_AVE_ClientP21_S_AVE_SurfaceIDInSetE11_os_log_fmt_0
+ __ZZ17AVE_Client_ConfigP13_S_AVE_ClientP21_S_AVE_SurfaceIDInSetE11_os_log_fmt_1
+ __ZZ17AVE_Client_ConfigP13_S_AVE_ClientP21_S_AVE_SurfaceIDInSetE11_os_log_fmt_2
+ __ZZ17AVE_Client_ConfigP13_S_AVE_ClientP21_S_AVE_SurfaceIDInSetE11_os_log_fmt_3
+ __ZZ17AVE_Client_InitPSP13_S_AVE_ClientiE11_os_log_fmt
+ __ZZ17AVE_Client_InitPSP13_S_AVE_ClientiE11_os_log_fmt_0
+ __ZZ17AVE_Client_InitPSP13_S_AVE_ClientiE11_os_log_fmt_1
+ __ZZ17AVE_Client_InitPSP13_S_AVE_ClientiE11_os_log_fmt_2
+ __ZZ17AVE_Client_InitPSP13_S_AVE_ClientiE11_os_log_fmt_3
+ __ZZ17AVE_Client_InitPSP13_S_AVE_ClientiE11_os_log_fmt_4
+ __ZZ17AVE_Client_InitPSP13_S_AVE_ClientiE11_os_log_fmt_5
+ __ZZ17AVE_Client_InitPSP13_S_AVE_ClientiE11_os_log_fmt_6
+ __ZZ17AVE_Client_InitPSP13_S_AVE_ClientiE11_os_log_fmt_7
+ __ZZ17AVE_Client_InitPSP13_S_AVE_ClientiE11_os_log_fmt_8
+ __ZZ17AVE_Client_InitPSP13_S_AVE_ClientiE11_os_log_fmt_9
+ __ZZ17AVE_Client_InitPSP13_S_AVE_ClientiE11_os_log_fmt__10_
+ __ZZ17AVE_Client_InitPSP13_S_AVE_ClientiE11_os_log_fmt__11_
+ __ZZ17AVE_Client_InitPSP13_S_AVE_ClientiE11_os_log_fmt__12_
+ __ZZ17AVE_DLB_AllocUnitP10_S_AVE_DLBP15_S_AVE_DLB_UnitE11_os_log_fmt
+ __ZZ17AVE_DLB_AllocUnitP10_S_AVE_DLBP15_S_AVE_DLB_UnitE11_os_log_fmt_0
+ __ZZ17AVE_DLB_AllocUnitP10_S_AVE_DLBP15_S_AVE_DLB_UnitE11_os_log_fmt_1
+ __ZZ17AVE_DLB_CleanUnitP10_S_AVE_DLBP15_S_AVE_DLB_UnitE11_os_log_fmt
+ __ZZ17AVE_DLB_PrintUnitP15_S_AVE_DLB_UnitjiPKciE11_os_log_fmt
+ __ZZ17AVE_DLB_PrintUnitP15_S_AVE_DLB_UnitjiPKciE11_os_log_fmt_0
+ __ZZ17AVE_Pipeline_InitP15_S_AVE_PipelineyPvE11_os_log_fmt
+ __ZZ17AVE_Pipeline_InitP15_S_AVE_PipelineyPvE11_os_log_fmt_0
+ __ZZ17AVE_Pipeline_InitP15_S_AVE_PipelineyPvE11_os_log_fmt_1
+ __ZZ17AVE_Pipeline_InitP15_S_AVE_PipelineyPvE11_os_log_fmt_2
+ __ZZ18AVE_Client_PrepareP13_S_AVE_ClientP14_S_AVE_TimeOutiP21_S_AVE_SurfaceIDInSetP35AVE_SessionSettings_UserKernel_DataPKcE11_os_log_fmt_6
+ __ZZ18AVE_Client_PrepareP13_S_AVE_ClientP14_S_AVE_TimeOutiP21_S_AVE_SurfaceIDInSetP35AVE_SessionSettings_UserKernel_DataPKcE11_os_log_fmt__11_
+ __ZZ18AVE_DLB_AllocEUNumP10_S_AVE_DLBiP13_S_AVE_DLNodeE11_os_log_fmt
+ __ZZ18AVE_DLB_AllocEUNumP10_S_AVE_DLBiP13_S_AVE_DLNodeE11_os_log_fmt_0
+ __ZZ18AVE_DLB_AllocEUNumP10_S_AVE_DLBiP13_S_AVE_DLNodeE11_os_log_fmt_1
+ __ZZ18AVE_DLB_AllocEUNumP10_S_AVE_DLBiP13_S_AVE_DLNodeE11_os_log_fmt_2
+ __ZZ18AVE_DLB_AssignUnitP10_S_AVE_DLBP15_S_AVE_DLB_Unit15_E_AVE_WorkTypeiiE11_os_log_fmt
+ __ZZ18AVE_DLB_AssignUnitP10_S_AVE_DLBP15_S_AVE_DLB_Unit15_E_AVE_WorkTypeiiE11_os_log_fmt_0
+ __ZZ18AVE_DLB_AssignUnitP10_S_AVE_DLBP15_S_AVE_DLB_Unit15_E_AVE_WorkTypeiiE11_os_log_fmt_1
+ __ZZ18AVE_DLB_SelectUnitP10_S_AVE_DLBP18_S_AVE_DLB_UnitCfgP15_S_AVE_DLB_UnitE11_os_log_fmt
+ __ZZ18AVE_DLB_SelectUnitP10_S_AVE_DLBP18_S_AVE_DLB_UnitCfgP15_S_AVE_DLB_UnitE11_os_log_fmt_0
+ __ZZ18AVE_DLB_SelectUnitP10_S_AVE_DLBP18_S_AVE_DLB_UnitCfgP15_S_AVE_DLB_UnitE11_os_log_fmt_1
+ __ZZ18AVE_DLB_SelectUnitP10_S_AVE_DLBP18_S_AVE_DLB_UnitCfgP15_S_AVE_DLB_UnitE11_os_log_fmt_2
+ __ZZ18AVE_TaskCmd_CreatePviS_jE11_os_log_fmt
+ __ZZ18AVE_TaskCmd_CreatePviS_jE11_os_log_fmt_0
+ __ZZ18AVE_TaskCmd_CreatePviS_jE11_os_log_fmt_1
+ __ZZ18AVE_TaskCmd_CreatePviS_jE11_os_log_fmt_2
+ __ZZ18AVE_TaskCmd_CreatePviS_jE11_os_log_fmt_3
+ __ZZ18AVE_TaskCmd_CreatePviS_jE11_os_log_fmt_4
+ __ZZ19AVE_Client_AssignEUP13_S_AVE_ClientP15_S_AVE_DLB_InfoE11_os_log_fmt
+ __ZZ19AVE_DLB_ApplyStaticP10_S_AVE_DLBP13_S_AVE_ClientP15_S_AVE_DLB_InfoE11_os_log_fmt
+ __ZZ19AVE_DLB_ApplyStaticP10_S_AVE_DLBP13_S_AVE_ClientP15_S_AVE_DLB_InfoE11_os_log_fmt_0
+ __ZZ19AVE_DLB_ApplyStaticP10_S_AVE_DLBP13_S_AVE_ClientP15_S_AVE_DLB_InfoE11_os_log_fmt_1
+ __ZZ19AVE_Pipeline_ConfigP15_S_AVE_PipelineE11_os_log_fmt
+ __ZZ19AVE_SVESched_ConfigP15_S_AVE_SVESchediP12_S_AVE_EUMapiE11_os_log_fmt
+ __ZZ19AVE_SVESched_ConfigP15_S_AVE_SVESchediP12_S_AVE_EUMapiE11_os_log_fmt_0
+ __ZZ19AVE_SVESched_ConfigP15_S_AVE_SVESchediP12_S_AVE_EUMapiE11_os_log_fmt_1
+ __ZZ19AVE_SVESched_ConfigP15_S_AVE_SVESchediP12_S_AVE_EUMapiE11_os_log_fmt_2
+ __ZZ19AVE_SVESched_ConfigP15_S_AVE_SVESchediP12_S_AVE_EUMapiE11_os_log_fmt_3
+ __ZZ19AVE_SVESched_ConfigP15_S_AVE_SVESchediP12_S_AVE_EUMapiE11_os_log_fmt_4
+ __ZZ20AVE_Client_PreUpdateP13_S_AVE_ClientP18_S_AVE_ClientStatsP16_S_AVE_FrameInfoE11_os_log_fmt
+ __ZZ20AVE_DLB_ApplyDynamicP10_S_AVE_DLBP13_S_AVE_DLNodeE11_os_log_fmt
+ __ZZ20AVE_DLB_ApplyDynamicP10_S_AVE_DLBP13_S_AVE_DLNodeE11_os_log_fmt_0
+ __ZZ20AVE_DLB_ApplyDynamicP10_S_AVE_DLBP13_S_AVE_DLNodeE11_os_log_fmt_1
+ __ZZ20AVE_IOP_Start_ErebusP7AVE_RegE11_os_log_fmt
+ __ZZ20AVE_IOP_Start_ErebusP7AVE_RegE11_os_log_fmt_0
+ __ZZ20AVE_UCCmd_CheckParam12_E_AVE_DevID17_E_AVE_ClientTypeP16_S_AVE_UCInParamE11_os_log_fmt
+ __ZZ20AVE_UCCmd_CheckParam12_E_AVE_DevID17_E_AVE_ClientTypeP16_S_AVE_UCInParamE11_os_log_fmt_0
+ __ZZ21AVE_IOP_Config_ErebusP7AVE_RegyE11_os_log_fmt
+ __ZZ21AVE_IOP_Config_ErebusP7AVE_RegyE11_os_log_fmt_0
+ __ZZ21AVE_IOP_Config_ErebusP7AVE_RegyE11_os_log_fmt_1
+ __ZZ21AVE_Pipeline_DestructP15_S_AVE_PipelineE11_os_log_fmt
+ __ZZ21AVE_Pipeline_DestructP15_S_AVE_PipelineE11_os_log_fmt_0
+ __ZZ21AVE_Pipeline_DestructP15_S_AVE_PipelineE11_os_log_fmt_1
+ __ZZ21AVE_Pipeline_PrintAllP15_S_AVE_PipelinejiPKciE11_os_log_fmt
+ __ZZ21AVE_Pipeline_PrintAllP15_S_AVE_PipelinejiPKciE11_os_log_fmt_0
+ __ZZ22AVE_Pipeline_AssignEUCP15_S_AVE_PipelineP15_S_AVE_DLB_InfoE11_os_log_fmt
+ __ZZ22AVE_Pipeline_AssignEUCP15_S_AVE_PipelineP15_S_AVE_DLB_InfoE11_os_log_fmt_0
+ __ZZ22AVE_Pipeline_AssignEUCP15_S_AVE_PipelineP15_S_AVE_DLB_InfoE11_os_log_fmt_1
+ __ZZ22AVE_Pipeline_ConstructP15_S_AVE_Pipeline15_E_AVE_PipelineE11_os_log_fmt
+ __ZZ22AVE_Pipeline_ConstructP15_S_AVE_Pipeline15_E_AVE_PipelineE11_os_log_fmt_0
+ __ZZ22AVE_Pipeline_ConstructP15_S_AVE_Pipeline15_E_AVE_PipelineE11_os_log_fmt_1
+ __ZZ22AVE_Pipeline_ConstructP15_S_AVE_Pipeline15_E_AVE_PipelineE11_os_log_fmt_2
+ __ZZ22AVE_Pipeline_ConstructP15_S_AVE_Pipeline15_E_AVE_PipelineE11_os_log_fmt_3
+ __ZZ22AVE_Pipeline_ConstructP15_S_AVE_Pipeline15_E_AVE_PipelineE11_os_log_fmt_4
+ __ZZ22AVE_Pipeline_ConstructP15_S_AVE_Pipeline15_E_AVE_PipelineE11_os_log_fmt_5
+ __ZZ22AVE_Pipeline_ConstructP15_S_AVE_Pipeline15_E_AVE_PipelineE11_os_log_fmt_6
+ __ZZ22AVE_Pipeline_ConstructP15_S_AVE_Pipeline15_E_AVE_PipelineE11_os_log_fmt_7
+ __ZZ22AVE_Pipeline_PreUpdateP15_S_AVE_PipelineP16_S_AVE_FrameInfoE11_os_log_fmt
+ __ZZ22AVE_Pipeline_PreUpdateP15_S_AVE_PipelineP16_S_AVE_FrameInfoE11_os_log_fmt_0
+ __ZZ22AVE_Pipeline_PreUpdateP15_S_AVE_PipelineP16_S_AVE_FrameInfoE11_os_log_fmt_1
+ __ZZ23AVE_Analytics_SendEventP16_S_AVE_AnalyticsiE11_os_log_fmt__39_
+ __ZZ23AVE_Analytics_SendEventP16_S_AVE_AnalyticsiE11_os_log_fmt__40_
+ __ZZ23AVE_GOPDecision_PrepareP10_S_AVE_CHMP15AVE_GOPDecisionP10FrameStatsP12AVE_KeyFramejiiP26_S_AVE_TaskCmd_GOPDecisionPA4_P10_S_AVE_CmdPP16_S_AVE_FrameInfoPiPA3_iPA2_iSK_SI_E11_os_log_fmt
+ __ZZ23AVE_GOPDecision_PrepareP10_S_AVE_CHMP15AVE_GOPDecisionP10FrameStatsP12AVE_KeyFramejiiP26_S_AVE_TaskCmd_GOPDecisionPA4_P10_S_AVE_CmdPP16_S_AVE_FrameInfoPiPA3_iPA2_iSK_SI_E11_os_log_fmt_0
+ __ZZ23AVE_GOPDecision_PrepareP10_S_AVE_CHMP15AVE_GOPDecisionP10FrameStatsP12AVE_KeyFramejiiP26_S_AVE_TaskCmd_GOPDecisionPA4_P10_S_AVE_CmdPP16_S_AVE_FrameInfoPiPA3_iPA2_iSK_SI_E11_os_log_fmt_1
+ __ZZ23AVE_GOPDecision_PrepareP10_S_AVE_CHMP15AVE_GOPDecisionP10FrameStatsP12AVE_KeyFramejiiP26_S_AVE_TaskCmd_GOPDecisionPA4_P10_S_AVE_CmdPP16_S_AVE_FrameInfoPiPA3_iPA2_iSK_SI_E11_os_log_fmt_2
+ __ZZ23AVE_GOPDecision_PrepareP10_S_AVE_CHMP15AVE_GOPDecisionP10FrameStatsP12AVE_KeyFramejiiP26_S_AVE_TaskCmd_GOPDecisionPA4_P10_S_AVE_CmdPP16_S_AVE_FrameInfoPiPA3_iPA2_iSK_SI_E11_os_log_fmt_4
+ __ZZ23AVE_GOPDecision_PrepareP10_S_AVE_CHMP15AVE_GOPDecisionP10FrameStatsP12AVE_KeyFramejiiP26_S_AVE_TaskCmd_GOPDecisionPA4_P10_S_AVE_CmdPP16_S_AVE_FrameInfoPiPA3_iPA2_iSK_SI_E11_os_log_fmt_5
+ __ZZ23AVE_Pipeline_PostUpdateP15_S_AVE_PipelineP16_S_AVE_FrameInfoE11_os_log_fmt
+ __ZZ23AVE_Pipeline_PostUpdateP15_S_AVE_PipelineP16_S_AVE_FrameInfoE11_os_log_fmt_0
+ __ZZ23AVE_Pipeline_PostUpdateP15_S_AVE_PipelineP16_S_AVE_FrameInfoE11_os_log_fmt_1
+ __ZZ23AVE_PrintClientSurfacesP23_S_AVE_ClientSurfaceSetjiE11_os_log_fmt
+ __ZZ23AVE_PrintSurfaceInfoSetP21_S_AVE_SurfaceInfoSetjiE11_os_log_fmt__48_
+ __ZZ23AVE_PrintSurfaceInfoSetP21_S_AVE_SurfaceInfoSetjiE11_os_log_fmt__49_
+ __ZZ23AVE_PrintSurfaceInfoSetP21_S_AVE_SurfaceInfoSetjiE11_os_log_fmt__50_
+ __ZZ23AVE_PrintSurfaceInfoSetP21_S_AVE_SurfaceInfoSetjiE11_os_log_fmt__51_
+ __ZZ23AVE_PrintSurfaceInfoSetP21_S_AVE_SurfaceInfoSetjiE11_os_log_fmt__52_
+ __ZZ23AVE_PrintSurfaceInfoSetP21_S_AVE_SurfaceInfoSetjiE11_os_log_fmt__53_
+ __ZZ23AVE_PrintSurfaceInfoSetP21_S_AVE_SurfaceInfoSetjiE11_os_log_fmt__54_
+ __ZZ23AVE_PrintSurfaceInfoSetP21_S_AVE_SurfaceInfoSetjiE11_os_log_fmt__55_
+ __ZZ23AVE_TaskCmd_GOPDecisionPvS_PiiE11_os_log_fmt
+ __ZZ23AVE_TaskCmd_GOPDecisionPvS_PiiE11_os_log_fmt_0
+ __ZZ23AVE_TaskCmd_GOPDecisionPvS_PiiE11_os_log_fmt_1
+ __ZZ24AVE_IOP_CheckIdle_ErebusP7AVE_RegE11_os_log_fmt
+ __ZZ24AVE_IOP_CheckIdle_ErebusP7AVE_RegE11_os_log_fmt_0
+ __ZZ24AVE_Work_LRME_PostUpdateP13_S_AVE_ClientP16_S_AVE_FrameInfoP14CODED_DATA_HDRE11_os_log_fmt
+ __ZZ24AVE_Work_LRME_PostUpdateP13_S_AVE_ClientP16_S_AVE_FrameInfoP14CODED_DATA_HDRE11_os_log_fmt_0
+ __ZZ24AVE_Work_MCTF_PostUpdateP13_S_AVE_ClientP16_S_AVE_FrameInfoP14CODED_DATA_HDRE11_os_log_fmt
+ __ZZ24AVE_Work_MCTF_PostUpdateP13_S_AVE_ClientP16_S_AVE_FrameInfoP14CODED_DATA_HDRE11_os_log_fmt_0
+ __ZZ25AVE_CHM_SetDataInfo_FwBufP10_S_AVE_CHMP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoP14_S_AVE_DPB_SetP18AVE_PICMGMT_PARAMSE11_os_log_fmt__44_
+ __ZZ25AVE_CHM_SetDataInfo_FwBufP10_S_AVE_CHMP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoP14_S_AVE_DPB_SetP18AVE_PICMGMT_PARAMSE11_os_log_fmt__45_
+ __ZZ25AVE_CHM_SetDataInfo_FwBufP10_S_AVE_CHMP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoP14_S_AVE_DPB_SetP18AVE_PICMGMT_PARAMSE11_os_log_fmt__46_
+ __ZZ25AVE_CHM_SetDataInfo_FwBufP10_S_AVE_CHMP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoP14_S_AVE_DPB_SetP18AVE_PICMGMT_PARAMSE11_os_log_fmt__47_
+ __ZZ25AVE_CHM_SetDataInfo_FwBufP10_S_AVE_CHMP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoP14_S_AVE_DPB_SetP18AVE_PICMGMT_PARAMSE11_os_log_fmt__48_
+ __ZZ25AVE_CHM_SetDataInfo_FwBufP10_S_AVE_CHMP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoP14_S_AVE_DPB_SetP18AVE_PICMGMT_PARAMSE11_os_log_fmt__49_
+ __ZZ25AVE_CHM_SetDataInfo_FwBufP10_S_AVE_CHMP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoP14_S_AVE_DPB_SetP18AVE_PICMGMT_PARAMSE11_os_log_fmt__50_
+ __ZZ25AVE_CHM_SetDataInfo_FwBufP10_S_AVE_CHMP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoP14_S_AVE_DPB_SetP18AVE_PICMGMT_PARAMSE11_os_log_fmt__51_
+ __ZZ25AVE_CHM_SetDataInfo_FwBufP10_S_AVE_CHMP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoP14_S_AVE_DPB_SetP18AVE_PICMGMT_PARAMSE11_os_log_fmt__52_
+ __ZZ25AVE_CHM_SetDataInfo_FwBufP10_S_AVE_CHMP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoP14_S_AVE_DPB_SetP18AVE_PICMGMT_PARAMSE11_os_log_fmt__53_
+ __ZZ25AVE_CHM_SetDataInfo_FwBufP10_S_AVE_CHMP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoP14_S_AVE_DPB_SetP18AVE_PICMGMT_PARAMSE11_os_log_fmt__54_
+ __ZZ25AVE_Client_SetSliceHeaderP13_S_AVE_ClientyP16_S_AVE_FrameInfobE11_os_log_fmt_2
+ __ZZ25AVE_UCCmd_CheckParam_Open12_E_AVE_DevID17_E_AVE_ClientTypeP20S_AVE_UCInParam_OpenE11_os_log_fmt
+ __ZZ25AVE_UCCmd_CheckParam_Open12_E_AVE_DevID17_E_AVE_ClientTypeP20S_AVE_UCInParam_OpenE11_os_log_fmt_0
+ __ZZ25AVE_UCCmd_CheckParam_Open12_E_AVE_DevID17_E_AVE_ClientTypeP20S_AVE_UCInParam_OpenE11_os_log_fmt_1
+ __ZZ25AVE_UCCmd_CheckParam_Open12_E_AVE_DevID17_E_AVE_ClientTypeP20S_AVE_UCInParam_OpenE11_os_log_fmt_2
+ __ZZ25AVE_UCCmd_CheckParam_Open12_E_AVE_DevID17_E_AVE_ClientTypeP20S_AVE_UCInParam_OpenE11_os_log_fmt_3
+ __ZZ25AVE_UCCmd_CheckParam_Open12_E_AVE_DevID17_E_AVE_ClientTypeP20S_AVE_UCInParam_OpenE11_os_log_fmt_4
+ __ZZ25AVE_UCCmd_CheckParam_Open12_E_AVE_DevID17_E_AVE_ClientTypeP20S_AVE_UCInParam_OpenE11_os_log_fmt_5
+ __ZZ25AVE_UCCmd_CheckParam_Open12_E_AVE_DevID17_E_AVE_ClientTypeP20S_AVE_UCInParam_OpenE11_os_log_fmt_6
+ __ZZ25AVE_UCCmd_CheckParam_Stop12_E_AVE_DevID17_E_AVE_ClientTypeP20S_AVE_UCInParam_StopE11_os_log_fmt
+ __ZZ25AVE_UCCmd_CheckParam_Stop12_E_AVE_DevID17_E_AVE_ClientTypeP20S_AVE_UCInParam_StopE11_os_log_fmt_0
+ __ZZ25AVE_UCCmd_CheckParam_Stop12_E_AVE_DevID17_E_AVE_ClientTypeP20S_AVE_UCInParam_StopE11_os_log_fmt_1
+ __ZZ26AVE_Client_CheckCommonInfoP13_S_AVE_ClientbP35AVE_SessionSettings_UserKernel_DataE11_os_log_fmt__10_
+ __ZZ26AVE_Client_UpdateOutputBufP13_S_AVE_ClientP16_S_AVE_FrameInfoE11_os_log_fmt
+ __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt
+ __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt_0
+ __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt_1
+ __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt_2
+ __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt_3
+ __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt_4
+ __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt_5
+ __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt_6
+ __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt_7
+ __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt_8
+ __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt_9
+ __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt__10_
+ __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt__11_
+ __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt__12_
+ __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt__13_
+ __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt__14_
+ __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt__15_
+ __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt__16_
+ __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt__17_
+ __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt__18_
+ __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt__19_
+ __ZZ26AVE_IOP_GetCurrTime_ErebusP7AVE_RegE11_os_log_fmt
+ __ZZ26AVE_IOP_GetCurrTime_ErebusP7AVE_RegE11_os_log_fmt_0
+ __ZZ26AVE_TaskCmd_IntraInterCostPvS_PiiE11_os_log_fmt
+ __ZZ26AVE_TaskCmd_IntraInterCostPvS_PiiE11_os_log_fmt_0
+ __ZZ26AVE_TaskCmd_IntraInterCostPvS_PiiE11_os_log_fmt_1
+ __ZZ26AVE_TaskCmd_IntraInterCostPvS_PiiE11_os_log_fmt_2
+ __ZZ26AVE_TaskCmd_IntraInterCostPvS_PiiE11_os_log_fmt_3
+ __ZZ26AVE_UCCmd_CheckParam_Close12_E_AVE_DevID17_E_AVE_ClientTypeP21S_AVE_UCInParam_CloseE11_os_log_fmt
+ __ZZ26AVE_UCCmd_CheckParam_Close12_E_AVE_DevID17_E_AVE_ClientTypeP21S_AVE_UCInParam_CloseE11_os_log_fmt_0
+ __ZZ26AVE_UCCmd_CheckParam_Flush12_E_AVE_DevID17_E_AVE_ClientTypeP21S_AVE_UCInParam_FlushE11_os_log_fmt
+ __ZZ26AVE_UCCmd_CheckParam_Flush12_E_AVE_DevID17_E_AVE_ClientTypeP21S_AVE_UCInParam_FlushE11_os_log_fmt_0
+ __ZZ26AVE_UCCmd_CheckParam_Flush12_E_AVE_DevID17_E_AVE_ClientTypeP21S_AVE_UCInParam_FlushE11_os_log_fmt_1
+ __ZZ26AVE_UCCmd_CheckParam_Reset12_E_AVE_DevID17_E_AVE_ClientTypeP21S_AVE_UCInParam_ResetE11_os_log_fmt
+ __ZZ26AVE_UCCmd_CheckParam_Reset12_E_AVE_DevID17_E_AVE_ClientTypeP21S_AVE_UCInParam_ResetE11_os_log_fmt_0
+ __ZZ26AVE_UCCmd_CheckParam_Reset12_E_AVE_DevID17_E_AVE_ClientTypeP21S_AVE_UCInParam_ResetE11_os_log_fmt_1
+ __ZZ26AVE_UCCmd_CheckParam_Start12_E_AVE_DevID17_E_AVE_ClientTypeP21S_AVE_UCInParam_StartE11_os_log_fmt
+ __ZZ26AVE_UCCmd_CheckParam_Start12_E_AVE_DevID17_E_AVE_ClientTypeP21S_AVE_UCInParam_StartE11_os_log_fmt_0
+ __ZZ26AVE_UCCmd_CheckParam_Start12_E_AVE_DevID17_E_AVE_ClientTypeP21S_AVE_UCInParam_StartE11_os_log_fmt_1
+ __ZZ26AVE_UCCmd_CheckParam_Start12_E_AVE_DevID17_E_AVE_ClientTypeP21S_AVE_UCInParam_StartE11_os_log_fmt_2
+ __ZZ27AVE_CheckExternalInSurfacesP17_S_AVE_SurfaceSetP21_S_AVE_SurfaceInfoSetyE11_os_log_fmt
+ __ZZ27AVE_CheckExternalInSurfacesP17_S_AVE_SurfaceSetP21_S_AVE_SurfaceInfoSetyE11_os_log_fmt_0
+ __ZZ27AVE_CheckExternalInSurfacesP17_S_AVE_SurfaceSetP21_S_AVE_SurfaceInfoSetyE11_os_log_fmt_1
+ __ZZ27AVE_CheckExternalInSurfacesP17_S_AVE_SurfaceSetP21_S_AVE_SurfaceInfoSetyE11_os_log_fmt_2
+ __ZZ27AVE_DARTMapInternalSurfacesP14AVE_SurfaceMgrP17_S_AVE_SurfaceSetjE11_os_log_fmt__16_
+ __ZZ27AVE_DARTMapInternalSurfacesP14AVE_SurfaceMgrP17_S_AVE_SurfaceSetjE11_os_log_fmt__17_
+ __ZZ27AVE_DARTMapInternalSurfacesP14AVE_SurfaceMgrP17_S_AVE_SurfaceSetjE11_os_log_fmt__18_
+ __ZZ27AVE_DARTMapInternalSurfacesP14AVE_SurfaceMgrP17_S_AVE_SurfaceSetjE11_os_log_fmt__19_
+ __ZZ27AVE_Pipeline_CreateSurfacesP15_S_AVE_PipelineP21_S_AVE_SurfaceIDInSetE11_os_log_fmt
+ __ZZ27AVE_Pipeline_CreateSurfacesP15_S_AVE_PipelineP21_S_AVE_SurfaceIDInSetE11_os_log_fmt_0
+ __ZZ27AVE_UCCmd_CheckParam_Config12_E_AVE_DevID17_E_AVE_ClientTypeP22S_AVE_UCInParam_ConfigE11_os_log_fmt
+ __ZZ27AVE_UCCmd_CheckParam_Config12_E_AVE_DevID17_E_AVE_ClientTypeP22S_AVE_UCInParam_ConfigE11_os_log_fmt_0
+ __ZZ27AVE_UCCmd_CheckParam_Config12_E_AVE_DevID17_E_AVE_ClientTypeP22S_AVE_UCInParam_ConfigE11_os_log_fmt_1
+ __ZZ28AVE_Client_ConfigSurfacePoolP13_S_AVE_ClientE11_os_log_fmt
+ __ZZ28AVE_Client_ConfigSurfacePoolP13_S_AVE_ClientE11_os_log_fmt_0
+ __ZZ28AVE_Client_ConfigSurfacePoolP13_S_AVE_ClientE11_os_log_fmt_1
+ __ZZ28AVE_Client_ConfigSurfacePoolP13_S_AVE_ClientE11_os_log_fmt_2
+ __ZZ28AVE_Client_ConfigSurfacePoolP13_S_AVE_ClientE11_os_log_fmt_3
+ __ZZ28AVE_Client_ConfigSurfacePoolP13_S_AVE_ClientE11_os_log_fmt_4
+ __ZZ28AVE_Client_ConfigSurfacePoolP13_S_AVE_ClientE11_os_log_fmt_5
+ __ZZ28AVE_Client_ConfigSurfacePoolP13_S_AVE_ClientE11_os_log_fmt_6
+ __ZZ28AVE_CreateExternalInSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceIDInSetyP17_S_AVE_SurfaceSetE11_os_log_fmt
+ __ZZ28AVE_CreateExternalInSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceIDInSetyP17_S_AVE_SurfaceSetE11_os_log_fmt_0
+ __ZZ28AVE_Pipeline_CalcSurfaceInfoP15_S_AVE_PipelineE11_os_log_fmt
+ __ZZ28AVE_Pipeline_CalcSurfaceInfoP15_S_AVE_PipelineE11_os_log_fmt_0
+ __ZZ28AVE_Pipeline_CalcSurfaceInfoP15_S_AVE_PipelineE11_os_log_fmt_1
+ __ZZ28AVE_Pipeline_DARTMapSurfacesP15_S_AVE_PipelineE11_os_log_fmt
+ __ZZ28AVE_Pipeline_DARTMapSurfacesP15_S_AVE_PipelineE11_os_log_fmt_0
+ __ZZ28AVE_Pipeline_DestroySurfacesP15_S_AVE_PipelineE11_os_log_fmt
+ __ZZ28AVE_Pipeline_DestroySurfacesP15_S_AVE_PipelineE11_os_log_fmt_0
+ __ZZ28AVE_TaskCmd_GOPDecision_InitP15AVE_GOPDecisionjiiiPiPxP26_S_AVE_TaskCmd_GOPDecisionE11_os_log_fmt
+ __ZZ28AVE_TaskCmd_GOPDecision_InitP15AVE_GOPDecisionjiiiPiPxP26_S_AVE_TaskCmd_GOPDecisionE11_os_log_fmt_0
+ __ZZ28AVE_UCCmd_CheckParam_Prepare12_E_AVE_DevID17_E_AVE_ClientTypeP23S_AVE_UCInParam_PrepareE11_os_log_fmt
+ __ZZ28AVE_UCCmd_CheckParam_Prepare12_E_AVE_DevID17_E_AVE_ClientTypeP23S_AVE_UCInParam_PrepareE11_os_log_fmt_0
+ __ZZ28AVE_UCCmd_CheckParam_Prepare12_E_AVE_DevID17_E_AVE_ClientTypeP23S_AVE_UCInParam_PrepareE11_os_log_fmt_1
+ __ZZ28AVE_UCCmd_CheckParam_Prepare12_E_AVE_DevID17_E_AVE_ClientTypeP23S_AVE_UCInParam_PrepareE11_os_log_fmt_2
+ __ZZ28AVE_UCCmd_CheckParam_Process12_E_AVE_DevID17_E_AVE_ClientTypeP23S_AVE_UCInParam_ProcessE11_os_log_fmt
+ __ZZ28AVE_UCCmd_CheckParam_Process12_E_AVE_DevID17_E_AVE_ClientTypeP23S_AVE_UCInParam_ProcessE11_os_log_fmt_0
+ __ZZ28AVE_UCCmd_CheckParam_Process12_E_AVE_DevID17_E_AVE_ClientTypeP23S_AVE_UCInParam_ProcessE11_os_log_fmt_1
+ __ZZ29AVE_CreateExternalOutSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt
+ __ZZ29AVE_CreateExternalOutSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt_0
+ __ZZ29AVE_CreateExternalOutSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt_1
+ __ZZ29AVE_CreateExternalOutSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt_2
+ __ZZ29AVE_CreateExternalOutSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt_3
+ __ZZ29AVE_CreateExternalOutSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt_4
+ __ZZ29AVE_CreateExternalOutSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt_5
+ __ZZ29AVE_CreateExternalOutSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt_6
+ __ZZ29AVE_CreateExternalOutSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyyP17_S_AVE_SurfaceSetE11_os_log_fmt_7
+ __ZZ29AVE_UCCmd_CheckParam_Complete12_E_AVE_DevID17_E_AVE_ClientTypeP24S_AVE_UCInParam_CompleteE11_os_log_fmt
+ __ZZ29AVE_UCCmd_CheckParam_Complete12_E_AVE_DevID17_E_AVE_ClientTypeP24S_AVE_UCInParam_CompleteE11_os_log_fmt_0
+ __ZZ29AVE_UCCmd_CheckParam_Complete12_E_AVE_DevID17_E_AVE_ClientTypeP24S_AVE_UCInParam_CompleteE11_os_log_fmt_1
+ __ZZ30AVE_Pipeline_CalcInputQueueNumP15_S_AVE_PipelineiE11_os_log_fmt
+ __ZZ30AVE_Pipeline_CalcInputQueueNumP15_S_AVE_PipelineiE11_os_log_fmt_0
+ __ZZ30AVE_Pipeline_CalcInputQueueNumP15_S_AVE_PipelineiE11_os_log_fmt_1
+ __ZZ30AVE_Pipeline_CalcInputQueueNumP15_S_AVE_PipelineiE11_os_log_fmt_2
+ __ZZ30AVE_Pipeline_DARTUnmapSurfacesP15_S_AVE_PipelinePyE11_os_log_fmt
+ __ZZ30AVE_Pipeline_DARTUnmapSurfacesP15_S_AVE_PipelinePyE11_os_log_fmt_0
+ __ZZ30AVE_TaskCmd_GOPDecision_UninitP26_S_AVE_TaskCmd_GOPDecisionE11_os_log_fmt
+ __ZZ31AVE_TaskCmd_IntraInterCost_InitP15AVE_GOPDecisionP13AVE_IntraPrediPiPxP29_S_AVE_TaskCmd_IntraInterCostE11_os_log_fmt
+ __ZZ33AVE_TaskCmd_IntraInterCost_UninitP29_S_AVE_TaskCmd_IntraInterCostE11_os_log_fmt
+ __ZZ35AVE_Analytics_CollectThroughputModeP16_S_AVE_Analytics21_E_AVE_ThroughputModeE11_os_log_fmt
+ __ZZ35AVE_TaskCmd_IntraInterCost_SetInputP29_S_AVE_TaskCmd_IntraInterCostP15AVE_GOPDecisionP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoyiE11_os_log_fmt
+ __ZZ42AVE_Work_Enc_UpdateFrameInfoFromOutputDataP13_S_AVE_ClientiP16_S_AVE_FrameInfoP14CODED_DATA_HDRE11_os_log_fmt
+ __ZZ42AVE_Work_Enc_UpdateFrameInfoFromOutputDataP13_S_AVE_ClientiP16_S_AVE_FrameInfoP14CODED_DATA_HDRE11_os_log_fmt_0
+ __ZZL23AVE_SwC_CalcTaskBufSizePK13_S_AVE_ClientE11_os_log_fmt
+ __ZZL23AVE_SwC_CalcTaskBufSizePK13_S_AVE_ClientE11_os_log_fmt_0
+ __ZZL23AVE_SwC_CalcTaskBufSizePK13_S_AVE_ClientE11_os_log_fmt_1
+ __ZZL23AVE_SwC_CalcTaskBufSizePK13_S_AVE_ClientE11_os_log_fmt_2
+ __ZZL27AVE_SVESched_GenerateSVEMapP15_S_AVE_SVESchedPK12_S_AVE_EUMapE11_os_log_fmt
+ __ZZL27AVE_SVESched_GenerateSVEMapP15_S_AVE_SVESchedPK12_S_AVE_EUMapE11_os_log_fmt_1
+ __ZZL27AVE_SVESched_GenerateSVEMapP15_S_AVE_SVESchedPK12_S_AVE_EUMapE11_os_log_fmt_2
+ __ZZL27AVE_SVESched_GenerateSVEMapP15_S_AVE_SVESchedPK12_S_AVE_EUMapE11_os_log_fmt_3
+ __ZZL35AVE_Pipeline_CreateExternalSurfacesP15_S_AVE_PipelineP21_S_AVE_SurfaceIDInSetE11_os_log_fmt
+ __ZZL35AVE_Pipeline_CreateExternalSurfacesP15_S_AVE_PipelineP21_S_AVE_SurfaceIDInSetE11_os_log_fmt_0
+ __ZZL35AVE_Pipeline_CreateExternalSurfacesP15_S_AVE_PipelineP21_S_AVE_SurfaceIDInSetE11_os_log_fmt_1
+ __ZZL35AVE_Pipeline_CreateInternalSurfacesP15_S_AVE_PipelineE11_os_log_fmt
+ __ZZL35AVE_Pipeline_CreateInternalSurfacesP15_S_AVE_PipelineE11_os_log_fmt_0
+ __ZZL35AVE_Pipeline_CreateInternalSurfacesP15_S_AVE_PipelineE11_os_log_fmt_1
+ __ZZL36AVE_Pipeline_DARTMapExternalSurfacesP15_S_AVE_PipelineE11_os_log_fmt
+ __ZZL36AVE_Pipeline_DARTMapInternalSurfacesP15_S_AVE_PipelineE11_os_log_fmt
+ __ZZL36AVE_Pipeline_DestroyExternalSurfacesP15_S_AVE_PipelineE11_os_log_fmt
+ __ZZL36AVE_Pipeline_DestroyExternalSurfacesP15_S_AVE_PipelineE11_os_log_fmt_0
+ __ZZL36AVE_Pipeline_DestroyInternalSurfacesP15_S_AVE_PipelineE11_os_log_fmt
+ __ZZL36AVE_Pipeline_DestroyInternalSurfacesP15_S_AVE_PipelineE11_os_log_fmt_0
+ __ZZN10AVE_MD_SVE10PostUpdateEP16_S_AVE_FrameInfoE11_os_log_fmt
+ __ZZN10AVE_MD_SVE10PostUpdateEP16_S_AVE_FrameInfoE11_os_log_fmt_1
+ __ZZN10AVE_MD_SVE15CalcSurfaceInfoEvE11_os_log_fmt
+ __ZZN10AVE_MD_SVE15CalcSurfaceInfoEvE11_os_log_fmt_0
+ __ZZN10AVE_MD_SVE15CalcSurfaceInfoEvE11_os_log_fmt_1
+ __ZZN10AVE_MD_SVE15CalcSurfaceInfoEvE11_os_log_fmt_2
+ __ZZN10AVE_MD_SVE16AcquireOutputBufEP10_S_AVE_CmdiE11_os_log_fmt
+ __ZZN10AVE_MD_SVE16AcquireOutputBufEP10_S_AVE_CmdiE11_os_log_fmt_0
+ __ZZN10AVE_MD_SVE16AcquireOutputBufEP10_S_AVE_CmdiE11_os_log_fmt_1
+ __ZZN10AVE_MD_SVE16AcquireOutputBufEP10_S_AVE_CmdiE11_os_log_fmt_2
+ __ZZN10AVE_MD_SVE16AcquireOutputBufEP10_S_AVE_CmdiE11_os_log_fmt_3
+ __ZZN10AVE_MD_SVE16ReleaseOutputBufEP10_S_AVE_CmdiE11_os_log_fmt
+ __ZZN10AVE_MD_SVE16ReleaseOutputBufEP10_S_AVE_CmdiE11_os_log_fmt_0
+ __ZZN10AVE_MD_SVE16ReleaseOutputBufEP10_S_AVE_CmdiE11_os_log_fmt_1
+ __ZZN10AVE_MD_SVE17CalcInputQueueNumEvE11_os_log_fmt
+ __ZZN10AVE_MD_SVE17CalcInputQueueNumEvE11_os_log_fmt_0
+ __ZZN10AVE_MD_SVE20CheckOutputBuf_QuotaEiE11_os_log_fmt
+ __ZZN10AVE_MD_SVE22CreateExternalSurfacesEP21_S_AVE_SurfaceIDInSetE11_os_log_fmt
+ __ZZN10AVE_MD_SVE22CreateExternalSurfacesEP21_S_AVE_SurfaceIDInSetE11_os_log_fmt_0
+ __ZZN10AVE_MD_SVE22CreateExternalSurfacesEP21_S_AVE_SurfaceIDInSetE11_os_log_fmt_1
+ __ZZN10AVE_MD_SVE22CreateExternalSurfacesEP21_S_AVE_SurfaceIDInSetE11_os_log_fmt_2
+ __ZZN10AVE_MD_SVE22CreateExternalSurfacesEP21_S_AVE_SurfaceIDInSetE11_os_log_fmt_3
+ __ZZN10AVE_MD_SVE22CreateInternalSurfacesEvE11_os_log_fmt
+ __ZZN10AVE_MD_SVE22CreateInternalSurfacesEvE11_os_log_fmt_0
+ __ZZN10AVE_MD_SVE22CreateInternalSurfacesEvE11_os_log_fmt_1
+ __ZZN10AVE_MD_SVE22UpdateOutputBuf_StatusEiE11_os_log_fmt
+ __ZZN10AVE_MD_SVE22UpdateOutputBuf_StatusEiE11_os_log_fmt_0
+ __ZZN10AVE_MD_SVE22UpdateOutputBuf_StatusEiE11_os_log_fmt_1
+ __ZZN10AVE_MD_SVE22UpdateOutputBuf_StatusEiE11_os_log_fmt_2
+ __ZZN10AVE_MD_SVE23DARTMapExternalSurfacesEvE11_os_log_fmt
+ __ZZN10AVE_MD_SVE23DARTMapExternalSurfacesEvE11_os_log_fmt_0
+ __ZZN10AVE_MD_SVE23DARTMapExternalSurfacesEvE11_os_log_fmt_1
+ __ZZN10AVE_MD_SVE23DARTMapInternalSurfacesEvE11_os_log_fmt
+ __ZZN10AVE_MD_SVE23DARTMapInternalSurfacesEvE11_os_log_fmt_0
+ __ZZN10AVE_MD_SVE23DARTMapInternalSurfacesEvE11_os_log_fmt_1
+ __ZZN10AVE_MD_SVE23DestroyExternalSurfacesEvE11_os_log_fmt
+ __ZZN10AVE_MD_SVE23DestroyExternalSurfacesEvE11_os_log_fmt_0
+ __ZZN10AVE_MD_SVE23DestroyExternalSurfacesEvE11_os_log_fmt_1
+ __ZZN10AVE_MD_SVE23DestroyInternalSurfacesEvE11_os_log_fmt
+ __ZZN10AVE_MD_SVE23DestroyInternalSurfacesEvE11_os_log_fmt_0
+ __ZZN10AVE_MD_SVE23DestroyInternalSurfacesEvE11_os_log_fmt_1
+ __ZZN10AVE_MD_SVE25DARTUnmapExternalSurfacesEyE11_os_log_fmt
+ __ZZN10AVE_MD_SVE25DARTUnmapExternalSurfacesEyE11_os_log_fmt_0
+ __ZZN10AVE_MD_SVE25DARTUnmapExternalSurfacesEyE11_os_log_fmt_1
+ __ZZN10AVE_MD_SVE25DARTUnmapInternalSurfacesEyE11_os_log_fmt
+ __ZZN10AVE_MD_SVE25DARTUnmapInternalSurfacesEyE11_os_log_fmt_0
+ __ZZN10AVE_MD_SVE25DARTUnmapInternalSurfacesEyE11_os_log_fmt_1
+ __ZZN10AVE_MD_SVE6ConfigEvE11_os_log_fmt_1
+ __ZZN10AVE_MD_SVE6ConfigEvE11_os_log_fmt_2
+ __ZZN10AVE_MD_SVE8PrintAllEjiPKciE11_os_log_fmt
+ __ZZN10AVE_MD_SVE8PrintAllEjiPKciE11_os_log_fmt_0
+ __ZZN10AVE_MD_SVE9ConfigDLBEvE11_os_log_fmt
+ __ZZN10AVE_MD_SVE9ConfigDLBEvE11_os_log_fmt_0
+ __ZZN10AVE_MD_SVE9PreUpdateEP16_S_AVE_FrameInfoE11_os_log_fmt
+ __ZZN10AVE_MD_SVE9PreUpdateEP16_S_AVE_FrameInfoE11_os_log_fmt_1
+ __ZZN10AVE_SVEDPB4InitEjiiiiPA2_A17_P11AVE_SurfacePS1_S5_S5_S5_PA2_A10_S1_S8_E11_os_log_fmt
+ __ZZN10AVE_SVEDPB4InitEjiiiiPA2_A17_P11AVE_SurfacePS1_S5_S5_S5_PA2_A10_S1_S8_E11_os_log_fmt_0
+ __ZZN10AVE_SVEDPB4InitEjiiiiPA2_A17_P11AVE_SurfacePS1_S5_S5_S5_PA2_A10_S1_S8_E11_os_log_fmt_1
+ __ZZN10AVE_SVEDPB4InitEjiiiiPA2_A17_P11AVE_SurfacePS1_S5_S5_S5_PA2_A10_S1_S8_E11_os_log_fmt_2
+ __ZZN10AVE_SVEDPB4InitEjiiiiPA2_A17_P11AVE_SurfacePS1_S5_S5_S5_PA2_A10_S1_S8_E11_os_log_fmt_3
+ __ZZN10AVE_SVEDPB4InitEjiiiiPA2_A17_P11AVE_SurfacePS1_S5_S5_S5_PA2_A10_S1_S8_E11_os_log_fmt_4
+ __ZZN10AVE_SVEDPB4InitEjiiiiPA2_A17_P11AVE_SurfacePS1_S5_S5_S5_PA2_A10_S1_S8_E11_os_log_fmt_6
+ __ZZN10AVE_SVEDPBdlEPvmE19kalloc_type_view_86
+ __ZZN10AVE_SVEDPBnwEmE19kalloc_type_view_86
+ __ZZN10AVE_Thread10CondSignalEPvE11_os_log_fmt
+ __ZZN10AVE_Thread10CondSignalEPvE11_os_log_fmt_0
+ __ZZN10AVE_Thread13CondTimedWaitEPvS0_jjE11_os_log_fmt
+ __ZZN10AVE_Thread13CondTimedWaitEPvS0_jjE11_os_log_fmt_0
+ __ZZN10AVE_Thread13CondTimedWaitEPvS0_jjE11_os_log_fmt_2
+ __ZZN10AVE_Thread13CondTimedWaitEPvS0_jjE11_os_log_fmt_3
+ __ZZN10AVE_Thread18ProcessTerminationEvE11_os_log_fmt
+ __ZZN10AVE_Thread18ProcessTerminationEvE11_os_log_fmt_0
+ __ZZN10AVE_Thread18ProcessTerminationEvE11_os_log_fmt_1
+ __ZZN10AVE_Thread4InitEjE11_os_log_fmt
+ __ZZN10AVE_Thread4InitEjE11_os_log_fmt_0
+ __ZZN10AVE_Thread4InitEjE11_os_log_fmt_1
+ __ZZN10AVE_Thread6ThreadEvE11_os_log_fmt
+ __ZZN10AVE_Thread6ThreadEvE11_os_log_fmt_0
+ __ZZN10AVE_Thread6UninitEvE11_os_log_fmt
+ __ZZN10AVE_Thread6UninitEvE11_os_log_fmt_0
+ __ZZN10AVE_Thread8CondWaitEPvS0_E11_os_log_fmt
+ __ZZN10AVE_Thread8CondWaitEPvS0_E11_os_log_fmt_0
+ __ZZN10AVE_Thread8CondWaitEPvS0_E11_os_log_fmt_1
+ __ZZN12AVE_MD_LAGOP17CalcInputQueueNumEvE11_os_log_fmt
+ __ZZN12AVE_MD_LAGOP17CalcInputQueueNumEvE11_os_log_fmt_0
+ __ZZN12AVE_MD_LAGOP8PrintAllEjiPKciE11_os_log_fmt
+ __ZZN12AVE_MD_LAGOP8PrintAllEjiPKciE11_os_log_fmt_0
+ __ZZN12AVE_MD_LAGOP9ConfigDLBEvE11_os_log_fmt
+ __ZZN12AVE_MD_LAGOP9ConfigDLBEvE11_os_log_fmt_0
+ __ZZN12AVE_MD_LAGOPdlEPvmE19kalloc_type_view_20
+ __ZZN12AVE_MD_LAGOPnwEmE19kalloc_type_view_20
+ __ZZN12AVE_WorkPool11CheckCmdCntEvE11_os_log_fmt
+ __ZZN12AVE_WorkPool11CheckCmdCntEvE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool11CheckCmdCntEvE11_os_log_fmt_1
+ __ZZN12AVE_WorkPool11MarkSkipCmdEP14_S_AVE_TaskCmdE11_os_log_fmt
+ __ZZN12AVE_WorkPool11MarkSkipCmdEP14_S_AVE_TaskCmdE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool11MarkSkipCmdEP14_S_AVE_TaskCmdE11_os_log_fmt_1
+ __ZZN12AVE_WorkPool12CreateThreadEiE11_os_log_fmt
+ __ZZN12AVE_WorkPool12CreateThreadEiE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool12CreateThreadEiE11_os_log_fmt_1
+ __ZZN12AVE_WorkPool12ProcessSleepEvE11_os_log_fmt
+ __ZZN12AVE_WorkPool12ProcessSleepEvE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool13NotifyCmdDoneEP14_S_AVE_TaskCmdE11_os_log_fmt
+ __ZZN12AVE_WorkPool13NotifyCmdDoneEP14_S_AVE_TaskCmdE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool13NotifyCmdDoneEP14_S_AVE_TaskCmdE11_os_log_fmt_1
+ __ZZN12AVE_WorkPool13ProcessNewCmdEvE11_os_log_fmt
+ __ZZN12AVE_WorkPool13ProcessNewCmdEvE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool14ClearCmdInTaskEP11_S_AVE_TaskE11_os_log_fmt
+ __ZZN12AVE_WorkPool14ClearCmdInTaskEP11_S_AVE_TaskE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool14ClearCmdInTaskEP11_S_AVE_TaskE11_os_log_fmt_1
+ __ZZN12AVE_WorkPool14ClearCmdInTaskEP11_S_AVE_TaskE11_os_log_fmt_2
+ __ZZN12AVE_WorkPool14ClearCmdInTaskEP11_S_AVE_TaskE11_os_log_fmt_3
+ __ZZN12AVE_WorkPool14ClearCmdInTaskEP11_S_AVE_TaskE11_os_log_fmt_4
+ __ZZN12AVE_WorkPool14ClearCmdInTaskEP11_S_AVE_TaskE11_os_log_fmt_5
+ __ZZN12AVE_WorkPool14RequestTaskCmdEP14_S_AVE_WPParamiP11_S_AVE_TaskE11_os_log_fmt
+ __ZZN12AVE_WorkPool14RequestTaskCmdEP14_S_AVE_WPParamiP11_S_AVE_TaskE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool14RequestTaskCmdEP14_S_AVE_WPParamiP11_S_AVE_TaskE11_os_log_fmt_1
+ __ZZN12AVE_WorkPool14RequestTaskCmdEP14_S_AVE_WPParamiP11_S_AVE_TaskE11_os_log_fmt_2
+ __ZZN12AVE_WorkPool14RequestTaskCmdEP14_S_AVE_WPParamiP11_S_AVE_TaskE11_os_log_fmt_3
+ __ZZN12AVE_WorkPool14RequestTaskCmdEP14_S_AVE_WPParamiP11_S_AVE_TaskE11_os_log_fmt_4
+ __ZZN12AVE_WorkPool14WaitThreadIdleEjE11_os_log_fmt
+ __ZZN12AVE_WorkPool14WaitThreadIdleEjE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool14WaitThreadIdleEjE11_os_log_fmt_1
+ __ZZN12AVE_WorkPool14WaitThreadIdleEjE11_os_log_fmt_2
+ __ZZN12AVE_WorkPool15CheckTaskCmdCntEPK11_S_AVE_TaskE11_os_log_fmt
+ __ZZN12AVE_WorkPool15CheckTaskCmdCntEPK11_S_AVE_TaskE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool15CheckTaskCmdCntEPK11_S_AVE_TaskE11_os_log_fmt_1
+ __ZZN12AVE_WorkPool15ProcessInputCmdEvE11_os_log_fmt
+ __ZZN12AVE_WorkPool15ProcessInputCmdEvE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool15ProcessInputCmdEvE11_os_log_fmt_1
+ __ZZN12AVE_WorkPool15WaitThreadsIdleEvE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool16ProcessOutputCmdEvE11_os_log_fmt
+ __ZZN12AVE_WorkPool16ProcessOutputCmdEvE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool16ProcessOutputCmdEvE11_os_log_fmt_1
+ __ZZN12AVE_WorkPool16ProcessOutputCmdEvE11_os_log_fmt_2
+ __ZZN12AVE_WorkPool17WaitCloseTaskDoneEP11_S_AVE_TaskE21kalloc_type_view_2124
+ __ZZN12AVE_WorkPool18ClearCmdInPriorityEP13_S_AVE_DLNodeE11_os_log_fmt
+ __ZZN12AVE_WorkPool18ClearCmdInPriorityEP13_S_AVE_DLNodeE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool18ProcessNewCmd_OpenEP14_S_AVE_WPParamiE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool18ProcessNewCmd_OpenEP14_S_AVE_WPParamiE11_os_log_fmt_2
+ __ZZN12AVE_WorkPool19ClearTaskInPriorityEP13_S_AVE_DLNodeE21kalloc_type_view_1528
+ __ZZN12AVE_WorkPool19ProcessNewCmd_StartEP14_S_AVE_WPParamiP11_S_AVE_TaskE11_os_log_fmt_1
+ __ZZN12AVE_WorkPool21ProcessInputCmdInTaskEP11_S_AVE_TaskE11_os_log_fmt
+ __ZZN12AVE_WorkPool21ProcessInputCmdInTaskEP11_S_AVE_TaskE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool21ProcessInputCmdInTaskEP11_S_AVE_TaskE11_os_log_fmt_1
+ __ZZN12AVE_WorkPool22ProcessOutputCmdInTaskEP11_S_AVE_TaskE11_os_log_fmt
+ __ZZN12AVE_WorkPool22ProcessOutputCmdInTaskEP11_S_AVE_TaskE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool22ProcessOutputCmdInTaskEP11_S_AVE_TaskE11_os_log_fmt_1
+ __ZZN12AVE_WorkPool22ProcessOutputCmdInTaskEP11_S_AVE_TaskE11_os_log_fmt_2
+ __ZZN12AVE_WorkPool25ProcessInputCmdInPriorityEP13_S_AVE_DLNodeE11_os_log_fmt
+ __ZZN12AVE_WorkPool26ProcessOutputCmdInPriorityEP13_S_AVE_DLNodeE11_os_log_fmt
+ __ZZN12AVE_WorkPool26ProcessOutputCmdInPriorityEP13_S_AVE_DLNodeE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool6ThreadEvE11_os_log_fmt
+ __ZZN12AVE_WorkPool6ThreadEvE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool7MoveCmdEP14_S_AVE_TaskCmd15_E_AVE_WP_StageS2_E11_os_log_fmt
+ __ZZN12AVE_WorkPool7MoveCmdEP14_S_AVE_TaskCmd15_E_AVE_WP_StageS2_E11_os_log_fmt_0
+ __ZZN12AVE_WorkPool7MoveCmdEP14_S_AVE_TaskCmd15_E_AVE_WP_StageS2_E11_os_log_fmt_1
+ __ZZN12AVE_WorkPool7MoveCmdEP14_S_AVE_TaskCmd15_E_AVE_WP_StageS2_E11_os_log_fmt_2
+ __ZZN12AVE_WorkPool7MoveCmdEP14_S_AVE_TaskCmd15_E_AVE_WP_StageS2_E11_os_log_fmt_3
+ __ZZN12AVE_WorkPool7MoveCmdEP14_S_AVE_TaskCmd15_E_AVE_WP_StageS2_E11_os_log_fmt_4
+ __ZZN12AVE_WorkPool7SkipCmdEP14_S_AVE_TaskCmdE11_os_log_fmt
+ __ZZN12AVE_WorkPool7SkipCmdEP14_S_AVE_TaskCmdE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool8ClearCmdEvE11_os_log_fmt
+ __ZZN12AVE_WorkPool8ClearCmdEvE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool8ClearCmdEvE11_os_log_fmt_1
+ __ZZN12AVE_WorkPool8ClearCmdEvE11_os_log_fmt_2
+ __ZZN12AVE_WorkPool8ClearCmdEvE11_os_log_fmt_3
+ __ZZN12AVE_WorkPool8OpenTaskEPK20S_AVE_WPInParam_OpenPP11_S_AVE_TaskE11_os_log_fmt
+ __ZZN12AVE_WorkPool8OpenTaskEPK20S_AVE_WPInParam_OpenPP11_S_AVE_TaskE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool8OpenTaskEPK20S_AVE_WPInParam_OpenPP11_S_AVE_TaskE11_os_log_fmt_1
+ __ZZN12AVE_WorkPool8OpenTaskEPK20S_AVE_WPInParam_OpenPP11_S_AVE_TaskE11_os_log_fmt_2
+ __ZZN12AVE_WorkPool8OpenTaskEPK20S_AVE_WPInParam_OpenPP11_S_AVE_TaskE11_os_log_fmt_3
+ __ZZN12AVE_WorkPool8OpenTaskEPK20S_AVE_WPInParam_OpenPP11_S_AVE_TaskE11_os_log_fmt_4
+ __ZZN12AVE_WorkPool8OpenTaskEPK20S_AVE_WPInParam_OpenPP11_S_AVE_TaskE20kalloc_type_view_238
+ __ZZN12AVE_WorkPool8OpenTaskEPK20S_AVE_WPInParam_OpenPP11_S_AVE_TaskE20kalloc_type_view_281
+ __ZZN12AVE_WorkPool9CloseTaskEyiE20kalloc_type_view_353
+ __ZZN12AVE_WorkPool9CloseTaskEyiE20kalloc_type_view_360
+ __ZZN12AVE_WorkPool9NotifyCmdEP14_S_AVE_TaskCmdiE11_os_log_fmt
+ __ZZN12AVE_WorkPool9NotifyCmdEP14_S_AVE_TaskCmdiE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool9NotifyCmdEP14_S_AVE_TaskCmdiE11_os_log_fmt_1
+ __ZZN12AVE_WorkPool9NotifyCmdEP14_S_AVE_TaskCmdiE11_os_log_fmt_2
+ __ZZN12AVE_WorkPool9WaitEventEvE11_os_log_fmt
+ __ZZN12AVE_WorkPool9WaitEventEvE11_os_log_fmt_0
+ __ZZN12AVE_WorkPool9WaitEventEvE11_os_log_fmt_1
+ __ZZN14AVE_WorkThread10ProcessCmdEvE11_os_log_fmt
+ __ZZN14AVE_WorkThread10ProcessCmdEvE11_os_log_fmt_0
+ __ZZN14AVE_WorkThread10ProcessCmdEvE11_os_log_fmt_1
+ __ZZN14AVE_WorkThread10ProcessCmdEvE11_os_log_fmt_2
+ __ZZN14AVE_WorkThread10ProcessCmdEvE11_os_log_fmt_3
+ __ZZN14AVE_WorkThread10ProcessCmdEvE11_os_log_fmt_4
+ __ZZN14AVE_WorkThread12ProcessEventEvE11_os_log_fmt
+ __ZZN14AVE_WorkThread12ProcessEventEvE11_os_log_fmt_0
+ __ZZN14AVE_WorkThread6ThreadEvE11_os_log_fmt
+ __ZZN14AVE_WorkThread6ThreadEvE11_os_log_fmt_0
+ __ZZN14AVE_WorkThread9NotifyCmdEP14_S_AVE_TaskCmdE11_os_log_fmt
+ __ZZN14AVE_WorkThread9NotifyCmdEP14_S_AVE_TaskCmdE11_os_log_fmt_0
+ __ZZN14AVE_WorkThread9NotifyCmdEP14_S_AVE_TaskCmdE11_os_log_fmt_1
+ __ZZN14AVE_WorkThread9NotifyCmdEP14_S_AVE_TaskCmdE11_os_log_fmt_2
+ __ZZN14AVE_WorkThread9WaitEventEvE11_os_log_fmt
+ __ZZN14AVE_WorkThread9WaitEventEvE11_os_log_fmt_0
+ __ZZN14AVE_WorkThread9WaitEventEvE11_os_log_fmt_1
+ __ZZN16AVE_MD_IntraPred14PrepareTaskCmdEP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoE11_os_log_fmt
+ __ZZN16AVE_MD_IntraPred14PrepareTaskCmdEP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoE11_os_log_fmt_0
+ __ZZN16AVE_MD_IntraPred14PrepareTaskCmdEP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoE11_os_log_fmt_1
+ __ZZN16AVE_MD_IntraPred14PrepareTaskCmdEP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoE11_os_log_fmt_2
+ __ZZN16AVE_MD_IntraPred17CalcInputQueueNumEvE11_os_log_fmt
+ __ZZN16AVE_MD_IntraPred17CalcInputQueueNumEvE11_os_log_fmt_0
+ __ZZN16AVE_MD_IntraPred8PrintAllEjiPKciE11_os_log_fmt
+ __ZZN16AVE_MD_IntraPred8PrintAllEjiPKciE11_os_log_fmt_0
+ __ZZN16AVE_MD_IntraPred9ConfigDLBEvE11_os_log_fmt
+ __ZZN16AVE_MD_IntraPred9ConfigDLBEvE11_os_log_fmt_0
+ __ZZN19AppleAVE2UserClient4OpenEP20S_AVE_UCInParam_OpenP21S_AVE_UCOutParam_OpenE11_os_log_fmt_4
+ __ZZN19AppleAVE2UserClient4OpenEP20S_AVE_UCInParam_OpenP21S_AVE_UCOutParam_OpenE11_os_log_fmt_7
+ __ZZN19AppleAVE2UserClient4StopEP20S_AVE_UCInParam_StopP21S_AVE_UCOutParam_StopE11_os_log_fmt_2
+ __ZZN19AppleAVE2UserClient4StopEP20S_AVE_UCInParam_StopP21S_AVE_UCOutParam_StopE11_os_log_fmt_4
+ __ZZN19AppleAVE2UserClient5CloseEP21S_AVE_UCInParam_CloseP22S_AVE_UCOutParam_CloseE11_os_log_fmt_2
+ __ZZN19AppleAVE2UserClient5CloseEP21S_AVE_UCInParam_CloseP22S_AVE_UCOutParam_CloseE11_os_log_fmt_4
+ __ZZN19AppleAVE2UserClient5FlushEP21S_AVE_UCInParam_FlushP22S_AVE_UCOutParam_FlushE11_os_log_fmt_2
+ __ZZN19AppleAVE2UserClient5FlushEP21S_AVE_UCInParam_FlushP22S_AVE_UCOutParam_FlushE11_os_log_fmt_4
+ __ZZN19AppleAVE2UserClient5ResetEP21S_AVE_UCInParam_ResetP22S_AVE_UCOutParam_ResetE11_os_log_fmt_2
+ __ZZN19AppleAVE2UserClient5ResetEP21S_AVE_UCInParam_ResetP22S_AVE_UCOutParam_ResetE11_os_log_fmt_4
+ __ZZN19AppleAVE2UserClient5StartEP21S_AVE_UCInParam_StartP22S_AVE_UCOutParam_StartE11_os_log_fmt_2
+ __ZZN19AppleAVE2UserClient5StartEP21S_AVE_UCInParam_StartP22S_AVE_UCOutParam_StartE11_os_log_fmt_4
+ __ZZN19AppleAVE2UserClient7PrepareEP23S_AVE_UCInParam_PrepareP24S_AVE_UCOutParam_PrepareE11_os_log_fmt_2
+ __ZZN19AppleAVE2UserClient7PrepareEP23S_AVE_UCInParam_PrepareP24S_AVE_UCOutParam_PrepareE11_os_log_fmt_4
+ __ZZN19AppleAVE2UserClient7ProcessEP23S_AVE_UCInParam_ProcessP24S_AVE_UCOutParam_ProcessE11_os_log_fmt_2
+ __ZZN19AppleAVE2UserClient7ProcessEP23S_AVE_UCInParam_ProcessP24S_AVE_UCOutParam_ProcessE11_os_log_fmt_4
+ __ZZN19AppleAVE2UserClient8CompleteEP24S_AVE_UCInParam_CompleteP25S_AVE_UCOutParam_CompleteE11_os_log_fmt_2
+ __ZZN19AppleAVE2UserClient8CompleteEP24S_AVE_UCInParam_CompleteP25S_AVE_UCOutParam_CompleteE11_os_log_fmt_4
+ __ZZN25_S_AVE_SVESched_TimingMgrdlEPvmE19kalloc_type_view_52
+ __ZZN25_S_AVE_SVESched_TimingMgrnwEmE19kalloc_type_view_52
+ __ZZN6AVE_MD10PostUpdateEP16_S_AVE_FrameInfoE11_os_log_fmt
+ __ZZN6AVE_MD10PostUpdateEP16_S_AVE_FrameInfoE11_os_log_fmt_1
+ __ZZN6AVE_MD11PrintStatusEjiPKciE11_os_log_fmt
+ __ZZN6AVE_MD11PrintStatusEjiPKciE11_os_log_fmt_0
+ __ZZN6AVE_MD13PrintCmdStatsEjjiPKciE11_os_log_fmt
+ __ZZN6AVE_MD13PrintCmdStatsEjjiPKciE11_os_log_fmt_0
+ __ZZN6AVE_MD17CalcInputQueueNumEvE11_os_log_fmt
+ __ZZN6AVE_MD17CalcInputQueueNumEvE11_os_log_fmt_0
+ __ZZN6AVE_MD9AssignEUCEP15_S_AVE_DLB_UnitE11_os_log_fmt
+ __ZZN6AVE_MD9AssignEUCEP15_S_AVE_DLB_UnitE11_os_log_fmt_0
+ __ZZN6AVE_MD9AssignEUCEP15_S_AVE_DLB_UnitE11_os_log_fmt_1
+ __ZZN6AVE_MD9AttachEUCEvE11_os_log_fmt
+ __ZZN6AVE_MD9AttachEUCEvE11_os_log_fmt_0
+ __ZZN6AVE_MD9ConfigDLBEvE11_os_log_fmt
+ __ZZN6AVE_MD9ConfigDLBEvE11_os_log_fmt_0
+ __ZZN6AVE_MD9DetachEUCEvE11_os_log_fmt
+ __ZZN6AVE_MD9DetachEUCEvE11_os_log_fmt_0
+ __ZZN6AVE_MD9PreUpdateEP16_S_AVE_FrameInfoE11_os_log_fmt
+ __ZZN6AVE_MD9PreUpdateEP16_S_AVE_FrameInfoE11_os_log_fmt_1
+ __ZZN6AVE_MDdlEPvmE19kalloc_type_view_30
+ __ZZN7AVE_DPM4InitEP11AVE_DevInfoPK10_S_AVE_CfgjP8AVE_PMGRE11_os_log_fmt
+ __ZZN7AVE_DPM4InitEP11AVE_DevInfoPK10_S_AVE_CfgjP8AVE_PMGRE11_os_log_fmt_0
+ __ZZN7AVE_DPM4InitEP11AVE_DevInfoPK10_S_AVE_CfgjP8AVE_PMGRE11_os_log_fmt_1
+ __ZZN8Analyzer13storeLRMECostEPA3_KiiPA4_iE11_os_log_fmt
+ __ZZN8Analyzer15miniGopDecisionEPA3_KiS2_PS0_PA2_S0_S5_PK19_S_AVE_KeyFrameHintiiiiibiE11_os_log_fmt
+ __ZZN8Analyzer17scenecutDetectionEjPKiPA3_S0_PA2_S0_S1_jE11_os_log_fmt
+ __ZZN8Analyzer17scenecutDetectionEjPKiPA3_S0_PA2_S0_S1_jE11_os_log_fmt_0
+ __ZZN9AVE_SVERC4InitEji14_E_AVE_GOPModeiiPiiE11_os_log_fmt_3
+ __ZZN9AVE_SVERC4InitEji14_E_AVE_GOPModeiiPiiE11_os_log_fmt_4
+ ___cxa_pure_virtual
+ _gc_sAVE_DevCap_PDMap_Erebus
+ _gc_sAVE_DevCap_Perf_AVC_Erebus
+ _gc_sAVE_DevCap_Perf_GGM_Erebus
+ _gc_sAVE_DevCap_Perf_HEVC_Erebus
+ _gc_sAVE_DevCap_Perf_LRME_Erebus
+ _gc_sAVE_DevCap_PixelFmt_AVC_Erebus
+ _gc_sAVE_DevCap_PixelFmt_GGM_Erebus
+ _gc_sAVE_DevCap_PixelFmt_HEVC_Erebus
+ _gc_sAVE_DevCap_PixelFmt_MCTF_Erebus
+ _gc_sAVE_DevCap_Resolution_AVC_Erebus
+ _gc_sAVE_DevCap_Resolution_GGM_Erebus
+ _gc_sAVE_DevCap_Resolution_HEVC_Erebus
+ _gc_sAVE_DevCap_Resolution_LRME_Erebus
+ _gc_sAVE_DevCap_Resolution_MCTF_Erebus
+ _gc_sAVE_DevCap_SearchRange_AVC_Erebus
+ _gc_sAVE_DevCap_SearchRange_GGM_Erebus
+ _gc_sAVE_DevCap_SearchRange_HEVC_Erebus
+ _gc_sAVE_DevCap_SearchRange_LRME_Erebus
+ _gc_sAVE_DevCap_SearchRange_MCTF_Erebus
- _Z19AVE_DevCap_FindPerf12_E_AVE_DevID17_E_AVE_ClientType16_E_AVE_CodecType.cold.1
- _Z19AVE_Job_GOPDecisionPv.cold.1
- _Z20AVE_DevCap_FindpDMap12_E_AVE_DevID.cold.1
- _Z23AVE_DevCap_FindPixelFmt12_E_AVE_DevID17_E_AVE_ClientType16_E_AVE_CodecType.cold.1
- _Z25AVE_DevCap_FindResolution12_E_AVE_DevID17_E_AVE_ClientType16_E_AVE_CodecType.cold.1
- _Z26AVE_DevCap_FindSearchRange12_E_AVE_DevID17_E_AVE_ClientType16_E_AVE_CodecType.cold.1
- _ZN12AVE_WorkPool11ClearAllJobEv.cold.1
- _ZN12AVE_WorkPool14CheckSleepDoneEv.cold.1
- _ZN12AVE_WorkPool14ClearJobInTaskEP11_S_AVE_Task.cold.1
- _ZN12AVE_WorkPool14ClearJobInTaskEP11_S_AVE_Task.cold.2
- _ZN12AVE_WorkPool14WaitThreadIdleEji.cold.1
- _ZN12AVE_WorkPool14WaitThreadIdleEji.cold.2
- _ZN12AVE_WorkPool15CheckJobCounterEv.cold.1
- _ZN12AVE_WorkPool15CheckJobCounterEv.cold.2
- _ZN12AVE_WorkPool15CheckJobCounterEv.cold.3
- _ZN12AVE_WorkPool15GetIdleThreadIDEv.cold.1
- _ZN12AVE_WorkPool17WaitCloseTaskDoneEP11_S_AVE_Task.cold.1
- _ZN12AVE_WorkPool18ProcessNewCmd_OpenEP14_S_AVE_WPParami.cold.1
- _ZN12AVE_WorkPool18ProcessNewCmd_OpenEP14_S_AVE_WPParami.cold.2
- _ZN12AVE_WorkPool19CheckTaskJobCounterEPK11_S_AVE_Task.cold.1
- _ZN12AVE_WorkPool19CheckTaskJobCounterEPK11_S_AVE_Task.cold.2
- _ZN12AVE_WorkPool19CheckTaskJobCounterEPK11_S_AVE_Task.cold.3
- _ZN12AVE_WorkPool19ProcessAllOutputJobEv.cold.1
- _ZN12AVE_WorkPool19ProcessNewCmd_StartEP14_S_AVE_WPParamiP11_S_AVE_Task.cold.1
- _ZN12AVE_WorkPool19ProcessNewCmd_StartEP14_S_AVE_WPParamiP11_S_AVE_Task.cold.2
- _ZN12AVE_WorkPool22ProcessOutputJobInTaskEP11_S_AVE_Task.cold.1
- _ZN12AVE_WorkPool7MoveJobEP10_S_AVE_Job15_E_AVE_WP_StageS2_.cold.1
- _ZN12AVE_WorkPool7MoveJobEP10_S_AVE_Job15_E_AVE_WP_StageS2_.cold.2
- _ZN12AVE_WorkPool7MoveJobEP10_S_AVE_Job15_E_AVE_WP_StageS2_.cold.3
- _ZN12AVE_WorkPool8WorkPoolEv.cold.1
- _ZN14AVE_WorkThread10ProcessJobEv.cold.1
- _ZN14AVE_WorkThread9NotifyJobEP10_S_AVE_Job.cold.1
- _ZN14AVE_WorkThread9NotifyJobEP10_S_AVE_Job.cold.2
- _ZN8Analyzer15miniGopDecisionEPA2_KiPS0_S2_S2_PK19_S_AVE_KeyFrameHintiiiiibi.cold.1
- _ZN8Analyzer15miniGopDecisionEPA2_KiPS0_S2_S2_PK19_S_AVE_KeyFrameHintiiiiibi.cold.2
- __Z13AVE_DLB_AllocP10_S_AVE_DLBP15_S_AVE_DLB_Info17_E_AVE_ClientTypeid16_E_AVE_CodecType
- __Z13AVE_DLB_ApplyP10_S_AVE_DLBP13_S_AVE_DLNode
- __Z14AVE_DLB_AssignP10_S_AVE_DLBP15_S_AVE_DLB_Infoii17_E_AVE_ClientTypeid16_E_AVE_CodecType
- __Z14AVE_DLB_SelectP10_S_AVE_DLBP15_S_AVE_DLB_InfoP13_S_AVE_SVEMap
- __Z14AVE_Job_CreatePviS_j
- __Z14AVE_SortSVEMapP13_S_AVE_SVEMap
- __Z15AVE_CheckSVEMap12_E_AVE_DevIDP13_S_AVE_SVEMap
- __Z15AVE_Job_DestroyP10_S_AVE_Job
- __Z16AVE_CheckQualityii
- __Z17AVE_Client_ConfigP13_S_AVE_Client
- __Z17AVE_Client_InitPSP13_S_AVE_Client
- __Z17AVE_Client_UpdateP13_S_AVE_ClientP18_S_AVE_ClientStatsP16_S_AVE_FrameInfo
- __Z17AVE_Pipeline_InitP15_S_AVE_Pipeliney
- __Z18AVE_Pipeline_MDNumP15_S_AVE_Pipelinej
- __Z19AVE_DLB_AllocSVENumP10_S_AVE_DLBP13_S_AVE_DLNode
- __Z19AVE_Job_GOPDecisionPv
- __Z19AVE_Pipeline_ConfigP15_S_AVE_Pipeline15_E_AVE_Pipeline17_E_AVE_ClientType
- __Z19AVE_SVESched_ConfigP15_S_AVE_SVESchedP13_S_AVE_SVEMapi
- __Z20AVE_CHM_CalcDPMStatsP10_S_AVE_CHMP15_S_AVE_DPMStats
- __Z20AVE_CHM_PrintAllCmdsP10_S_AVE_CHMjjji
- __Z20AVE_Client_AssignHwCP13_S_AVE_ClientP13_S_AVE_SVEMap
- __Z20AVE_Client_ConfigDLBP13_S_AVE_Clienti
- __Z21AVE_Client_CalcSVEMaxP13_S_AVE_Clienti
- __Z21AVE_Client_CalcSVENumP13_S_AVE_Clienti
- __Z21AVE_Pipeline_ConfigMDP15_S_AVE_Pipeline
- __Z22AVE_Job_IntraInterCostPv
- __Z23AVE_CalcBufNumOfMBStatsbiiiiiiibb16_E_AVE_MCTF_Modei13_E_AVE_RCModei
- __Z23AVE_CalcNumOfInputQueue17_E_AVE_ClientTypeiiiiiiiibb16_E_AVE_MCTF_Modei13_E_AVE_RCModei
- __Z23AVE_GOPDecision_PrepareP10_S_AVE_CHMP15AVE_GOPDecisionP10FrameStatsP12AVE_KeyFramejiiP22_S_AVE_Job_GOPDecisionPA4_P10_S_AVE_CmdPP16_S_AVE_FrameInfoPiPA2_iSI_SI_
- __Z23AVE_Pipeline_PrintStateP15_S_AVE_PipelinejiPKci
- __Z23AVE_Work_Enc_CalcRefNumP13_S_AVE_Client
- __Z24AVE_DLB_CompStr_SVEStatsPP18_S_AVE_DLB_EUStatsiPci
- __Z24AVE_Job_GOPDecision_InitP15AVE_GOPDecisionjiiiPiPyP22_S_AVE_Job_GOPDecision
- __Z24AVE_Work_LRME_CalcRefNumP13_S_AVE_Client
- __Z24AVE_Work_MCTF_CalcRefNumP13_S_AVE_Client
- __Z25AVE_CalcBufNumOfCodedDataiiiiiiibb16_E_AVE_MCTF_Modei13_E_AVE_RCModei
- __Z25AVE_Client_Enc_CalcRefNumP13_S_AVE_Client
- __Z26AVE_Client_DecideSchedModeP13_S_AVE_Client
- __Z26AVE_Client_LRME_CalcRefNumP13_S_AVE_Client
- __Z26AVE_Client_MCTF_CalcRefNumP13_S_AVE_Client
- __Z26AVE_Client_UpdateFrameInfoP13_S_AVE_ClientP16_S_AVE_FrameInfo
- __Z26AVE_CreateExternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceIDInSetP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSet
- __Z26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSet
- __Z26AVE_Job_GOPDecision_UninitP22_S_AVE_Job_GOPDecision
- __Z27AVE_CalcBufNumOfCodedHeader17_E_AVE_ClientTypeiiiiiiibb16_E_AVE_MCTF_Modei13_E_AVE_RCModei
- __Z27AVE_CalcBufNumOfSliceHeader16_E_AVE_CodecTypeiiiiiiibb16_E_AVE_MCTF_Modei13_E_AVE_RCModei
- __Z27AVE_CalcBufSetNumOfFwClienti
- __Z27AVE_ClientList_CalcDLBStatsP13_S_AVE_DLNodeyP18_S_AVE_DLB_EUStatsi
- __Z27AVE_Client_AcquireOutputBufP13_S_AVE_ClientP10_S_AVE_Cmdiy
- __Z27AVE_Client_CalcDPMThresholdP13_S_AVE_ClientP20_S_AVE_DPM_Threshold
- __Z27AVE_Client_CalcPerfNumOfCHMP13_S_AVE_ClientiPi
- __Z27AVE_Client_ReleaseOutputBufP13_S_AVE_ClientP10_S_AVE_Cmdiy
- __Z27AVE_Job_IntraInterCost_InitP15AVE_GOPDecisionP13AVE_IntraPrediPiPyP25_S_AVE_Job_IntraInterCost
- __Z27AVE_Pipeline_PrintAllMDCmdsP15_S_AVE_PipelinejiPKci
- __Z27AVE_Work_Enc_CalcRefNum_ExtP13_S_AVE_Client
- __Z28AVE_Client_AddDLBStatsPerCHMP13_S_AVE_ClientP13_S_AVE_SVEMapP18_S_AVE_DLB_EUStats
- __Z28AVE_Client_CalcInputQueueNumP13_S_AVE_Client
- __Z28AVE_Client_ConfigSurfacePoolP13_S_AVE_ClientP21_S_AVE_SurfaceInfoSetP17_S_AVE_SurfaceSet
- __Z28AVE_Client_SubDLBStatsPerCHMP13_S_AVE_ClientP13_S_AVE_SVEMapP18_S_AVE_DLB_EUStats
- __Z28AVE_CreateExternalInSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceIDInSetjP17_S_AVE_SurfaceSet
- __Z28AVE_Work_Enc_CalcSurfaceInfoP13_S_AVE_ClientP21_S_AVE_SurfaceInfoSet
- __Z29AVE_CalcBufNumOfProtectedDatabiiiiiiibb16_E_AVE_MCTF_Modei13_E_AVE_RCModei
- __Z29AVE_CalcBufTypeNumOfLowResRefbb
- __Z29AVE_Client_Enc_CalcRefNum_ExtP13_S_AVE_Client
- __Z29AVE_CreateExternalOutSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSet
- __Z29AVE_Job_IntraInterCost_UninitP25_S_AVE_Job_IntraInterCost
- __Z29AVE_Pipeline_GetCmdCntInMDAllP15_S_AVE_Pipelinej
- __Z29AVE_Work_LRME_CalcSurfaceInfoP13_S_AVE_ClientP21_S_AVE_SurfaceInfoSet
- __Z29AVE_Work_MCTF_CalcSurfaceInfoP13_S_AVE_ClientP21_S_AVE_SurfaceInfoSet
- __Z30AVE_Client_Enc_CalcSurfaceInfoP13_S_AVE_ClientP21_S_AVE_SurfaceInfoSet
- __Z31AVE_Client_CheckExternalSurfaceP13_S_AVE_ClientP17_S_AVE_SurfaceSet
- __Z31AVE_Client_CheckOutputBuf_QuotaP13_S_AVE_HwCMapi
- __Z31AVE_Client_LRME_CalcSurfaceInfoP13_S_AVE_ClientP21_S_AVE_SurfaceInfoSet
- __Z31AVE_Client_MCTF_CalcSurfaceInfoP13_S_AVE_ClientP21_S_AVE_SurfaceInfoSet
- __Z31AVE_Job_IntraInterCost_SetInputP25_S_AVE_Job_IntraInterCostP15AVE_GOPDecisionP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoji
- __Z31AVE_Pipeline_GetCmdCntInMDInputP15_S_AVE_Pipelinej
- __Z31AVE_Pipeline_GetCmdCntInMDStageP15_S_AVE_Pipeline15_E_AVE_MD_Stagej
- __Z32AVE_CalcBufSizeOfSrcNeighborData16_E_AVE_CodecTypei
- __Z32AVE_CalcBufTypeNumOfLowResResultbb
- __Z32AVE_Pipeline_GetCmdCntInMDOutputP15_S_AVE_Pipelinej
- __Z32AVE_Pipeline_GetCmdCntInMDStagesP15_S_AVE_Pipelinejj
- __Z33AVE_Client_UpdateOutputBuf_StatusP13_S_AVE_Clienti
- __Z34AVE_CalcBufTypeNumOfLowResRCResultbb
- __Z35AVE_Analytics_CollectThroughputModeP16_S_AVE_Analytics25HEVC_THROUGHPUT_RATE_MODE
- __Z35AVE_Client_CheckOutputBuf_AvailableP13_S_AVE_Clienti
- __Z35AVE_Client_UpdateFrameInfoFromStatsP13_S_AVE_ClientP16_S_AVE_FrameInfoP20S_AVE_DRC_FrameStats
- __Z40AVE_Client_UpdateFrameInfoFromOutputDataP13_S_AVE_ClientP16_S_AVE_FrameInfoP14CODED_DATA_HDR
- __ZL13gsc_saAVE_Job
- __ZL24AVE_WorkPool_ActionSleepP12AVE_WorkPool
- __ZL25AVE_WorkPool_ActionNewCmdP12AVE_WorkPool
- __ZL25gsc_saAVE_WorkPool_Action
- __ZL26AVE_WorkPool_ActionJobDoneP12AVE_WorkPool
- __ZN10AVE_MD_SVE15DecideSchedModeEv
- __ZN10AVE_MD_SVE15UpdateFrameInfoEP16_S_AVE_FrameInfo
- __ZN10AVE_MD_SVE24UpdateFrameInfoFromStatsEP16_S_AVE_FrameInfoP20S_AVE_DRC_FrameStats
- __ZN10AVE_MD_SVE29UpdateFrameInfoFromOutputDataEP16_S_AVE_FrameInfoP14CODED_DATA_HDR
- __ZN10AVE_MD_SVE9CalcEUMaxEi
- __ZN10AVE_MD_SVE9CalcEUNumEi
- __ZN10AVE_MD_SVE9ConfigDLBEP13_S_AVE_SVEMap
- __ZN10AVE_SVEDPB4InitEjiiiiPA2_A17_P11AVE_SurfacePS1_PA2_A10_S1_S8_
- __ZN12AVE_MD_LAGOP9ConfigDLBEP13_S_AVE_SVEMap
- __ZN12AVE_WorkPool10RequestJobEP14_S_AVE_WPParamiP11_S_AVE_Task
- __ZN12AVE_WorkPool11ActionSleepEv
- __ZN12AVE_WorkPool11ClearAllJobEv
- __ZN12AVE_WorkPool11MarkSkipCmdEP10_S_AVE_Job
- __ZN12AVE_WorkPool12ActionNewCmdEv
- __ZN12AVE_WorkPool13ActionJobDoneEv
- __ZN12AVE_WorkPool14ClearJobInTaskEP11_S_AVE_Task
- __ZN12AVE_WorkPool14WaitThreadIdleEji
- __ZN12AVE_WorkPool15CheckJobCounterEv
- __ZN12AVE_WorkPool15ProcessInputJobEv
- __ZN12AVE_WorkPool16ProcessAllNewCmdEv
- __ZN12AVE_WorkPool18ClearJobInPriorityEP13_S_AVE_DLNode
- __ZN12AVE_WorkPool19CheckTaskJobCounterEPK11_S_AVE_Task
- __ZN12AVE_WorkPool19ProcessAllOutputJobEv
- __ZN12AVE_WorkPool21ProcessInputJobInTaskEP11_S_AVE_Task
- __ZN12AVE_WorkPool22ProcessOutputJobInTaskEP11_S_AVE_Task
- __ZN12AVE_WorkPool23ProcessInputJobWhenIdleEv
- __ZN12AVE_WorkPool25ProcessInputJobInPriorityEP13_S_AVE_DLNode
- __ZN12AVE_WorkPool26ProcessOutputJobInPriorityEP13_S_AVE_DLNode
- __ZN12AVE_WorkPool7MoveJobEP10_S_AVE_Job15_E_AVE_WP_StageS2_
- __ZN12AVE_WorkPool7SkipJobEP10_S_AVE_Job
- __ZN12AVE_WorkPool8OpenTaskEy15_E_AVE_WorkTypeiPP11_S_AVE_Task
- __ZN12AVE_WorkPool8WorkPoolEv
- __ZN12AVE_WorkPool9NotifyJobEP10_S_AVE_Jobi
- __ZN14AVE_WorkThread10ProcessJobEv
- __ZN14AVE_WorkThread10WorkThreadEv
- __ZN14AVE_WorkThread8SetStateE23_E_AVE_WorkThread_State
- __ZN14AVE_WorkThread9NotifyJobEP10_S_AVE_Job
- __ZN15AVE_GOPDecision15MiniGOPDecisionEPA2_KiPS0_S2_S2_PK19_S_AVE_KeyFrameHintiiiii
- __ZN15AVE_GOPDecision17ScenecutDetectionEPA2_KiS2_PS0_i
- __ZN15AVE_GOPDecision27CalcBestIntraInterFrameCostEiiiiPA4_i
- __ZN16AVE_MD_IntraPred10PrepareJobEP14_S_AVE_CmdInfoP16_S_AVE_FrameInfo
- __ZN16AVE_MD_IntraPred9ConfigDLBEP13_S_AVE_SVEMap
- __ZN6AVE_MD10PrintStateEjiPKci
- __ZN6AVE_MD12PrintAllCmdsEjjji
- __ZN6AVE_MD9AssignEUCEv
- __ZN6AVE_MD9ConfigDLBEP13_S_AVE_SVEMap
- __ZN7AVE_DPM4InitEPK10_S_AVE_CfgjP8AVE_PMGR
- __ZN8Analyzer15miniGopDecisionEPA2_KiPS0_S2_S2_PK19_S_AVE_KeyFrameHintiiiiibi
- __ZN8Analyzer15storeLRMEFSCostEPA2_KiiPA4_i
- __ZN8Analyzer17scenecutDetectionEjPKiPA2_S0_S3_S1_j
- __ZN8Analyzer32calculateBestIntraInterFrameCostEiiiiPA4_i
- __ZZ13AVE_DLB_AllocP10_S_AVE_DLBP15_S_AVE_DLB_Info17_E_AVE_ClientTypeid16_E_AVE_CodecTypeE11_os_log_fmt
- __ZZ13AVE_DLB_AllocP10_S_AVE_DLBP15_S_AVE_DLB_Info17_E_AVE_ClientTypeid16_E_AVE_CodecTypeE11_os_log_fmt_0
- __ZZ13AVE_DLB_AllocP10_S_AVE_DLBP15_S_AVE_DLB_Info17_E_AVE_ClientTypeid16_E_AVE_CodecTypeE11_os_log_fmt_1
- __ZZ13AVE_DLB_ApplyP10_S_AVE_DLBP13_S_AVE_DLNodeE11_os_log_fmt
- __ZZ13AVE_DLB_ApplyP10_S_AVE_DLBP13_S_AVE_DLNodeE11_os_log_fmt_0
- __ZZ13AVE_DLB_ApplyP10_S_AVE_DLBP13_S_AVE_DLNodeE11_os_log_fmt_1
- __ZZ13AVE_DLB_ApplyP10_S_AVE_DLBP13_S_AVE_DLNodeE11_os_log_fmt_2
- __ZZ13AVE_DLB_ApplyP10_S_AVE_DLBP13_S_AVE_DLNodeE11_os_log_fmt_3
- __ZZ13AVE_DLB_ApplyP10_S_AVE_DLBP13_S_AVE_DLNodeE11_os_log_fmt_4
- __ZZ14AVE_DLB_AssignP10_S_AVE_DLBP15_S_AVE_DLB_Infoii17_E_AVE_ClientTypeid16_E_AVE_CodecTypeE11_os_log_fmt
- __ZZ14AVE_DLB_AssignP10_S_AVE_DLBP15_S_AVE_DLB_Infoii17_E_AVE_ClientTypeid16_E_AVE_CodecTypeE11_os_log_fmt_0
- __ZZ14AVE_DLB_AssignP10_S_AVE_DLBP15_S_AVE_DLB_Infoii17_E_AVE_ClientTypeid16_E_AVE_CodecTypeE11_os_log_fmt_1
- __ZZ14AVE_DLB_SelectP10_S_AVE_DLBP15_S_AVE_DLB_InfoP13_S_AVE_SVEMapE11_os_log_fmt
- __ZZ14AVE_DLB_SelectP10_S_AVE_DLBP15_S_AVE_DLB_InfoP13_S_AVE_SVEMapE11_os_log_fmt_0
- __ZZ14AVE_DLB_SelectP10_S_AVE_DLBP15_S_AVE_DLB_InfoP13_S_AVE_SVEMapE11_os_log_fmt_1
- __ZZ14AVE_DLB_SelectP10_S_AVE_DLBP15_S_AVE_DLB_InfoP13_S_AVE_SVEMapE11_os_log_fmt_2
- __ZZ14AVE_Job_CreatePviS_jE11_os_log_fmt
- __ZZ14AVE_Job_CreatePviS_jE11_os_log_fmt_0
- __ZZ14AVE_Job_CreatePviS_jE11_os_log_fmt_1
- __ZZ14AVE_Job_CreatePviS_jE11_os_log_fmt_2
- __ZZ14AVE_Job_CreatePviS_jE11_os_log_fmt_3
- __ZZ14AVE_Job_CreatePviS_jE19kalloc_type_view_65
- __ZZ15AVE_Job_DestroyP10_S_AVE_JobE20kalloc_type_view_100
- __ZZ16AVE_Client_StartP13_S_AVE_ClientP14_S_AVE_TimeOutiP21_S_AVE_SurfaceIDInSetP35AVE_SessionSettings_UserKernel_DataPKcE11_os_log_fmt__24_
- __ZZ16AVE_Client_StartP13_S_AVE_ClientP14_S_AVE_TimeOutiP21_S_AVE_SurfaceIDInSetP35AVE_SessionSettings_UserKernel_DataPKcE11_os_log_fmt__25_
- __ZZ16AVE_Client_StartP13_S_AVE_ClientP14_S_AVE_TimeOutiP21_S_AVE_SurfaceIDInSetP35AVE_SessionSettings_UserKernel_DataPKcE11_os_log_fmt__26_
- __ZZ16AVE_Client_StartP13_S_AVE_ClientP14_S_AVE_TimeOutiP21_S_AVE_SurfaceIDInSetP35AVE_SessionSettings_UserKernel_DataPKcE11_os_log_fmt__27_
- __ZZ16AVE_Client_StartP13_S_AVE_ClientP14_S_AVE_TimeOutiP21_S_AVE_SurfaceIDInSetP35AVE_SessionSettings_UserKernel_DataPKcE11_os_log_fmt__28_
- __ZZ16AVE_Client_StartP13_S_AVE_ClientP14_S_AVE_TimeOutiP21_S_AVE_SurfaceIDInSetP35AVE_SessionSettings_UserKernel_DataPKcE11_os_log_fmt__29_
- __ZZ17AVE_Client_ConfigP13_S_AVE_ClientE11_os_log_fmt
- __ZZ17AVE_Client_ConfigP13_S_AVE_ClientE11_os_log_fmt_1
- __ZZ17AVE_Client_InitPSP13_S_AVE_ClientE11_os_log_fmt
- __ZZ17AVE_Client_InitPSP13_S_AVE_ClientE11_os_log_fmt_0
- __ZZ17AVE_Client_InitPSP13_S_AVE_ClientE11_os_log_fmt_1
- __ZZ17AVE_Client_InitPSP13_S_AVE_ClientE11_os_log_fmt_2
- __ZZ17AVE_Client_InitPSP13_S_AVE_ClientE11_os_log_fmt_3
- __ZZ17AVE_Client_InitPSP13_S_AVE_ClientE11_os_log_fmt_4
- __ZZ17AVE_Client_InitPSP13_S_AVE_ClientE11_os_log_fmt_5
- __ZZ17AVE_Client_InitPSP13_S_AVE_ClientE11_os_log_fmt_6
- __ZZ17AVE_Client_InitPSP13_S_AVE_ClientE11_os_log_fmt_7
- __ZZ17AVE_Client_InitPSP13_S_AVE_ClientE11_os_log_fmt_8
- __ZZ17AVE_Client_InitPSP13_S_AVE_ClientE11_os_log_fmt_9
- __ZZ17AVE_Client_InitPSP13_S_AVE_ClientE11_os_log_fmt__10_
- __ZZ17AVE_Client_InitPSP13_S_AVE_ClientE11_os_log_fmt__11_
- __ZZ17AVE_Client_InitPSP13_S_AVE_ClientE11_os_log_fmt__12_
- __ZZ17AVE_Client_UpdateP13_S_AVE_ClientP18_S_AVE_ClientStatsP16_S_AVE_FrameInfoE11_os_log_fmt
- __ZZ17AVE_DLB_PrintInfoP15_S_AVE_DLB_InfojiPKciE11_os_log_fmt
- __ZZ17AVE_DLB_PrintInfoP15_S_AVE_DLB_InfojiPKciE11_os_log_fmt_0
- __ZZ17AVE_Pipeline_InitP15_S_AVE_PipelineyE11_os_log_fmt
- __ZZ17AVE_Pipeline_InitP15_S_AVE_PipelineyE11_os_log_fmt_0
- __ZZ17AVE_Pipeline_InitP15_S_AVE_PipelineyE11_os_log_fmt_1
- __ZZ17AVE_Pipeline_InitP15_S_AVE_PipelineyE11_os_log_fmt_2
- __ZZ18AVE_Client_PrepareP13_S_AVE_ClientP14_S_AVE_TimeOutiP21_S_AVE_SurfaceIDInSetP35AVE_SessionSettings_UserKernel_DataPKcE11_os_log_fmt__13_
- __ZZ18AVE_Client_PrepareP13_S_AVE_ClientP14_S_AVE_TimeOutiP21_S_AVE_SurfaceIDInSetP35AVE_SessionSettings_UserKernel_DataPKcE11_os_log_fmt__14_
- __ZZ18AVE_Client_PrepareP13_S_AVE_ClientP14_S_AVE_TimeOutiP21_S_AVE_SurfaceIDInSetP35AVE_SessionSettings_UserKernel_DataPKcE11_os_log_fmt__15_
- __ZZ18AVE_Client_PrepareP13_S_AVE_ClientP14_S_AVE_TimeOutiP21_S_AVE_SurfaceIDInSetP35AVE_SessionSettings_UserKernel_DataPKcE11_os_log_fmt__16_
- __ZZ18AVE_Client_PrepareP13_S_AVE_ClientP14_S_AVE_TimeOutiP21_S_AVE_SurfaceIDInSetP35AVE_SessionSettings_UserKernel_DataPKcE11_os_log_fmt__17_
- __ZZ19AVE_Client_PrintAllP13_S_AVE_ClientjiPKciE11_os_log_fmt__25_
- __ZZ19AVE_Client_PrintAllP13_S_AVE_ClientjiPKciE11_os_log_fmt__26_
- __ZZ19AVE_DLB_AllocSVENumP10_S_AVE_DLBP13_S_AVE_DLNodeE11_os_log_fmt
- __ZZ19AVE_DLB_AllocSVENumP10_S_AVE_DLBP13_S_AVE_DLNodeE11_os_log_fmt_0
- __ZZ19AVE_Job_GOPDecisionPvE11_os_log_fmt
- __ZZ19AVE_Job_GOPDecisionPvE11_os_log_fmt_0
- __ZZ19AVE_Job_GOPDecisionPvE11_os_log_fmt_1
- __ZZ19AVE_Pipeline_ConfigP15_S_AVE_Pipeline15_E_AVE_Pipeline17_E_AVE_ClientTypeE11_os_log_fmt
- __ZZ19AVE_Pipeline_ConfigP15_S_AVE_Pipeline15_E_AVE_Pipeline17_E_AVE_ClientTypeE11_os_log_fmt_0
- __ZZ19AVE_Pipeline_ConfigP15_S_AVE_Pipeline15_E_AVE_Pipeline17_E_AVE_ClientTypeE11_os_log_fmt_1
- __ZZ19AVE_Pipeline_ConfigP15_S_AVE_Pipeline15_E_AVE_Pipeline17_E_AVE_ClientTypeE11_os_log_fmt_2
- __ZZ19AVE_Pipeline_ConfigP15_S_AVE_Pipeline15_E_AVE_Pipeline17_E_AVE_ClientTypeE11_os_log_fmt_3
- __ZZ19AVE_Pipeline_ConfigP15_S_AVE_Pipeline15_E_AVE_Pipeline17_E_AVE_ClientTypeE11_os_log_fmt_4
- __ZZ19AVE_Pipeline_ConfigP15_S_AVE_Pipeline15_E_AVE_Pipeline17_E_AVE_ClientTypeE11_os_log_fmt_5
- __ZZ19AVE_SVESched_ConfigP15_S_AVE_SVESchedP13_S_AVE_SVEMapiE11_os_log_fmt
- __ZZ19AVE_SVESched_ConfigP15_S_AVE_SVESchedP13_S_AVE_SVEMapiE11_os_log_fmt_0
- __ZZ19AVE_SVESched_ConfigP15_S_AVE_SVESchedP13_S_AVE_SVEMapiE11_os_log_fmt_1
- __ZZ19AVE_SVESched_ConfigP15_S_AVE_SVESchedP13_S_AVE_SVEMapiE11_os_log_fmt_2
- __ZZ19AVE_SVESched_ConfigP15_S_AVE_SVESchedP13_S_AVE_SVEMapiE11_os_log_fmt_3
- __ZZ19AVE_SVESched_ConfigP15_S_AVE_SVESchedP13_S_AVE_SVEMapiE11_os_log_fmt_4
- __ZZ20AVE_Client_AssignHwCP13_S_AVE_ClientP13_S_AVE_SVEMapE11_os_log_fmt
- __ZZ20AVE_Client_ConfigDLBP13_S_AVE_ClientiE11_os_log_fmt
- __ZZ22AVE_Job_IntraInterCostPvE11_os_log_fmt
- __ZZ22AVE_Job_IntraInterCostPvE11_os_log_fmt_0
- __ZZ22AVE_Job_IntraInterCostPvE11_os_log_fmt_1
- __ZZ22AVE_Job_IntraInterCostPvE11_os_log_fmt_2
- __ZZ22AVE_Job_IntraInterCostPvE11_os_log_fmt_3
- __ZZ22AVE_Job_IntraInterCostPvE11_os_log_fmt_4
- __ZZ22AVE_Job_IntraInterCostPvE11_os_log_fmt_5
- __ZZ22AVE_Job_IntraInterCostPvE20kalloc_type_view_156
- __ZZ22AVE_Job_IntraInterCostPvE20kalloc_type_view_162
- __ZZ22AVE_Job_IntraInterCostPvE20kalloc_type_view_168
- __ZZ22AVE_Job_IntraInterCostPvE20kalloc_type_view_217
- __ZZ22AVE_Job_IntraInterCostPvE20kalloc_type_view_222
- __ZZ22AVE_Job_IntraInterCostPvE20kalloc_type_view_227
- __ZZ23AVE_GOPDecision_PrepareP10_S_AVE_CHMP15AVE_GOPDecisionP10FrameStatsP12AVE_KeyFramejiiP22_S_AVE_Job_GOPDecisionPA4_P10_S_AVE_CmdPP16_S_AVE_FrameInfoPiPA2_iSI_SI_E11_os_log_fmt
- __ZZ23AVE_GOPDecision_PrepareP10_S_AVE_CHMP15AVE_GOPDecisionP10FrameStatsP12AVE_KeyFramejiiP22_S_AVE_Job_GOPDecisionPA4_P10_S_AVE_CmdPP16_S_AVE_FrameInfoPiPA2_iSI_SI_E11_os_log_fmt_0
- __ZZ23AVE_GOPDecision_PrepareP10_S_AVE_CHMP15AVE_GOPDecisionP10FrameStatsP12AVE_KeyFramejiiP22_S_AVE_Job_GOPDecisionPA4_P10_S_AVE_CmdPP16_S_AVE_FrameInfoPiPA2_iSI_SI_E11_os_log_fmt_1
- __ZZ23AVE_GOPDecision_PrepareP10_S_AVE_CHMP15AVE_GOPDecisionP10FrameStatsP12AVE_KeyFramejiiP22_S_AVE_Job_GOPDecisionPA4_P10_S_AVE_CmdPP16_S_AVE_FrameInfoPiPA2_iSI_SI_E11_os_log_fmt_2
- __ZZ23AVE_GOPDecision_PrepareP10_S_AVE_CHMP15AVE_GOPDecisionP10FrameStatsP12AVE_KeyFramejiiP22_S_AVE_Job_GOPDecisionPA4_P10_S_AVE_CmdPP16_S_AVE_FrameInfoPiPA2_iSI_SI_E11_os_log_fmt_4
- __ZZ23AVE_GOPDecision_PrepareP10_S_AVE_CHMP15AVE_GOPDecisionP10FrameStatsP12AVE_KeyFramejiiP22_S_AVE_Job_GOPDecisionPA4_P10_S_AVE_CmdPP16_S_AVE_FrameInfoPiPA2_iSI_SI_E11_os_log_fmt_5
- __ZZ23AVE_GOPDecision_PrepareP10_S_AVE_CHMP15AVE_GOPDecisionP10FrameStatsP12AVE_KeyFramejiiP22_S_AVE_Job_GOPDecisionPA4_P10_S_AVE_CmdPP16_S_AVE_FrameInfoPiPA2_iSI_SI_E11_os_log_fmt_6
- __ZZ24AVE_Job_GOPDecision_InitP15AVE_GOPDecisionjiiiPiPyP22_S_AVE_Job_GOPDecisionE11_os_log_fmt
- __ZZ24AVE_Job_GOPDecision_InitP15AVE_GOPDecisionjiiiPiPyP22_S_AVE_Job_GOPDecisionE11_os_log_fmt_0
- __ZZ25AVE_CHM_SetDataInfo_FwBufP10_S_AVE_CHMP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoP14_S_AVE_DPB_SetP18AVE_PICMGMT_PARAMSE11_os_log_fmt__31_
- __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt
- __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt_0
- __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt_1
- __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt_2
- __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt_3
- __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt_4
- __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt_5
- __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt_6
- __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt_7
- __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt_8
- __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt_9
- __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt__10_
- __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt__11_
- __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt__12_
- __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt__13_
- __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt__14_
- __ZZ26AVE_CreateInternalSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt__15_
- __ZZ26AVE_Job_GOPDecision_UninitP22_S_AVE_Job_GOPDecisionE11_os_log_fmt
- __ZZ27AVE_ClientList_CalcDLBStatsP13_S_AVE_DLNodeyP18_S_AVE_DLB_EUStatsiE11_os_log_fmt
- __ZZ27AVE_ClientList_CalcDLBStatsP13_S_AVE_DLNodeyP18_S_AVE_DLB_EUStatsiE11_os_log_fmt_0
- __ZZ27AVE_Client_AcquireOutputBufP13_S_AVE_ClientP10_S_AVE_CmdiyE11_os_log_fmt
- __ZZ27AVE_Client_AcquireOutputBufP13_S_AVE_ClientP10_S_AVE_CmdiyE11_os_log_fmt_0
- __ZZ27AVE_Client_AcquireOutputBufP13_S_AVE_ClientP10_S_AVE_CmdiyE11_os_log_fmt_1
- __ZZ27AVE_Client_AcquireOutputBufP13_S_AVE_ClientP10_S_AVE_CmdiyE11_os_log_fmt_2
- __ZZ27AVE_Client_CalcDPMThresholdP13_S_AVE_ClientP20_S_AVE_DPM_ThresholdE11_os_log_fmt
- __ZZ27AVE_Client_ReleaseOutputBufP13_S_AVE_ClientP10_S_AVE_CmdiyE11_os_log_fmt
- __ZZ27AVE_Client_ReleaseOutputBufP13_S_AVE_ClientP10_S_AVE_CmdiyE11_os_log_fmt_0
- __ZZ27AVE_Client_ReleaseOutputBufP13_S_AVE_ClientP10_S_AVE_CmdiyE11_os_log_fmt_1
- __ZZ27AVE_Client_ReleaseOutputBufP13_S_AVE_ClientP10_S_AVE_CmdiyE11_os_log_fmt_2
- __ZZ27AVE_Job_IntraInterCost_InitP15AVE_GOPDecisionP13AVE_IntraPrediPiPyP25_S_AVE_Job_IntraInterCostE11_os_log_fmt
- __ZZ28AVE_Client_ConfigSurfacePoolP13_S_AVE_ClientP21_S_AVE_SurfaceInfoSetP17_S_AVE_SurfaceSetE11_os_log_fmt
- __ZZ28AVE_Client_ConfigSurfacePoolP13_S_AVE_ClientP21_S_AVE_SurfaceInfoSetP17_S_AVE_SurfaceSetE11_os_log_fmt_0
- __ZZ28AVE_Client_ConfigSurfacePoolP13_S_AVE_ClientP21_S_AVE_SurfaceInfoSetP17_S_AVE_SurfaceSetE11_os_log_fmt_1
- __ZZ28AVE_Client_ConfigSurfacePoolP13_S_AVE_ClientP21_S_AVE_SurfaceInfoSetP17_S_AVE_SurfaceSetE11_os_log_fmt_2
- __ZZ28AVE_Client_ConfigSurfacePoolP13_S_AVE_ClientP21_S_AVE_SurfaceInfoSetP17_S_AVE_SurfaceSetE11_os_log_fmt_3
- __ZZ28AVE_Client_ConfigSurfacePoolP13_S_AVE_ClientP21_S_AVE_SurfaceInfoSetP17_S_AVE_SurfaceSetE11_os_log_fmt_4
- __ZZ28AVE_Client_ConfigSurfacePoolP13_S_AVE_ClientP21_S_AVE_SurfaceInfoSetP17_S_AVE_SurfaceSetE11_os_log_fmt_5
- __ZZ28AVE_Client_ConfigSurfacePoolP13_S_AVE_ClientP21_S_AVE_SurfaceInfoSetP17_S_AVE_SurfaceSetE11_os_log_fmt_6
- __ZZ28AVE_CreateExternalInSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceIDInSetjP17_S_AVE_SurfaceSetE11_os_log_fmt
- __ZZ28AVE_CreateExternalInSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceIDInSetjP17_S_AVE_SurfaceSetE11_os_log_fmt_0
- __ZZ29AVE_CreateExternalOutSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt
- __ZZ29AVE_CreateExternalOutSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt_0
- __ZZ29AVE_CreateExternalOutSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt_1
- __ZZ29AVE_CreateExternalOutSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt_2
- __ZZ29AVE_CreateExternalOutSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt_3
- __ZZ29AVE_CreateExternalOutSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt_4
- __ZZ29AVE_CreateExternalOutSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt_5
- __ZZ29AVE_CreateExternalOutSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt_6
- __ZZ29AVE_CreateExternalOutSurfacesP14AVE_SurfaceMgrP4taskP21_S_AVE_SurfaceInfoSetyjP17_S_AVE_SurfaceSetE11_os_log_fmt_7
- __ZZ29AVE_Job_IntraInterCost_UninitP25_S_AVE_Job_IntraInterCostE11_os_log_fmt
- __ZZ31AVE_Client_CheckExternalSurfaceP13_S_AVE_ClientP17_S_AVE_SurfaceSetE11_os_log_fmt
- __ZZ31AVE_Client_CheckExternalSurfaceP13_S_AVE_ClientP17_S_AVE_SurfaceSetE11_os_log_fmt_0
- __ZZ31AVE_Client_CheckExternalSurfaceP13_S_AVE_ClientP17_S_AVE_SurfaceSetE11_os_log_fmt_1
- __ZZ31AVE_Client_CheckExternalSurfaceP13_S_AVE_ClientP17_S_AVE_SurfaceSetE11_os_log_fmt_2
- __ZZ31AVE_Client_CheckOutputBuf_QuotaP13_S_AVE_HwCMapiE11_os_log_fmt
- __ZZ31AVE_Job_IntraInterCost_SetInputP25_S_AVE_Job_IntraInterCostP15AVE_GOPDecisionP14_S_AVE_CmdInfoP16_S_AVE_FrameInfojiE11_os_log_fmt
- __ZZ33AVE_Client_UpdateOutputBuf_StatusP13_S_AVE_ClientiE11_os_log_fmt
- __ZZ33AVE_Client_UpdateOutputBuf_StatusP13_S_AVE_ClientiE11_os_log_fmt_0
- __ZZ33AVE_Client_UpdateOutputBuf_StatusP13_S_AVE_ClientiE11_os_log_fmt_1
- __ZZ35AVE_Analytics_CollectThroughputModeP16_S_AVE_Analytics25HEVC_THROUGHPUT_RATE_MODEE11_os_log_fmt
- __ZZ40AVE_Client_UpdateFrameInfoFromOutputDataP13_S_AVE_ClientP16_S_AVE_FrameInfoP14CODED_DATA_HDRE11_os_log_fmt
- __ZZ40AVE_Client_UpdateFrameInfoFromOutputDataP13_S_AVE_ClientP16_S_AVE_FrameInfoP14CODED_DATA_HDRE11_os_log_fmt_0
- __ZZL27AVE_SVESched_GenerateSVEMapP15_S_AVE_SVESchedPK13_S_AVE_SVEMapE11_os_log_fmt
- __ZZL27AVE_SVESched_GenerateSVEMapP15_S_AVE_SVESchedPK13_S_AVE_SVEMapE11_os_log_fmt_1
- __ZZL27AVE_SVESched_GenerateSVEMapP15_S_AVE_SVESchedPK13_S_AVE_SVEMapE11_os_log_fmt_2
- __ZZL27AVE_SVESched_GenerateSVEMapP15_S_AVE_SVESchedPK13_S_AVE_SVEMapE11_os_log_fmt_3
- __ZZN10AVE_MD_SVE29UpdateFrameInfoFromOutputDataEP16_S_AVE_FrameInfoP14CODED_DATA_HDRE11_os_log_fmt
- __ZZN10AVE_MD_SVE29UpdateFrameInfoFromOutputDataEP16_S_AVE_FrameInfoP14CODED_DATA_HDRE11_os_log_fmt_0
- __ZZN10AVE_MD_SVE9ConfigDLBEP13_S_AVE_SVEMapE11_os_log_fmt
- __ZZN10AVE_MD_SVE9ConfigDLBEP13_S_AVE_SVEMapE11_os_log_fmt_0
- __ZZN10AVE_MD_SVE9ConfigDLBEP13_S_AVE_SVEMapE11_os_log_fmt_1
- __ZZN10AVE_MD_SVE9ConfigDLBEP13_S_AVE_SVEMapE11_os_log_fmt_2
- __ZZN10AVE_SVEDPB4InitEjiiiiPA2_A17_P11AVE_SurfacePS1_PA2_A10_S1_S8_E11_os_log_fmt
- __ZZN10AVE_SVEDPB4InitEjiiiiPA2_A17_P11AVE_SurfacePS1_PA2_A10_S1_S8_E11_os_log_fmt_0
- __ZZN10AVE_SVEDPB4InitEjiiiiPA2_A17_P11AVE_SurfacePS1_PA2_A10_S1_S8_E11_os_log_fmt_1
- __ZZN10AVE_SVEDPB4InitEjiiiiPA2_A17_P11AVE_SurfacePS1_PA2_A10_S1_S8_E11_os_log_fmt_2
- __ZZN10AVE_SVEDPB4InitEjiiiiPA2_A17_P11AVE_SurfacePS1_PA2_A10_S1_S8_E11_os_log_fmt_3
- __ZZN10AVE_SVEDPB4InitEjiiiiPA2_A17_P11AVE_SurfacePS1_PA2_A10_S1_S8_E11_os_log_fmt_4
- __ZZN10AVE_SVEDPB4InitEjiiiiPA2_A17_P11AVE_SurfacePS1_PA2_A10_S1_S8_E11_os_log_fmt_5
- __ZZN10AVE_SVEDPB4InitEjiiiiPA2_A17_P11AVE_SurfacePS1_PA2_A10_S1_S8_E11_os_log_fmt_7
- __ZZN10AVE_SVEDPBdlEPvmE19kalloc_type_view_83
- __ZZN10AVE_SVEDPBnwEmE19kalloc_type_view_83
- __ZZN12AVE_MD_LAGOP9ConfigDLBEP13_S_AVE_SVEMapE11_os_log_fmt
- __ZZN12AVE_MD_LAGOP9ConfigDLBEP13_S_AVE_SVEMapE11_os_log_fmt_0
- __ZZN12AVE_MD_LAGOP9ConfigDLBEP13_S_AVE_SVEMapE11_os_log_fmt_1
- __ZZN12AVE_MD_LAGOP9ConfigDLBEP13_S_AVE_SVEMapE11_os_log_fmt_2
- __ZZN12AVE_MD_LAGOPdlEPvmE19kalloc_type_view_21
- __ZZN12AVE_MD_LAGOPnwEmE19kalloc_type_view_21
- __ZZN12AVE_WorkPool10RequestJobEP14_S_AVE_WPParamiP11_S_AVE_TaskE11_os_log_fmt
- __ZZN12AVE_WorkPool10RequestJobEP14_S_AVE_WPParamiP11_S_AVE_TaskE11_os_log_fmt_0
- __ZZN12AVE_WorkPool10RequestJobEP14_S_AVE_WPParamiP11_S_AVE_TaskE11_os_log_fmt_1
- __ZZN12AVE_WorkPool10RequestJobEP14_S_AVE_WPParamiP11_S_AVE_TaskE11_os_log_fmt_2
- __ZZN12AVE_WorkPool10RequestJobEP14_S_AVE_WPParamiP11_S_AVE_TaskE11_os_log_fmt_3
- __ZZN12AVE_WorkPool10RequestJobEP14_S_AVE_WPParamiP11_S_AVE_TaskE11_os_log_fmt_4
- __ZZN12AVE_WorkPool11ActionSleepEvE11_os_log_fmt
- __ZZN12AVE_WorkPool11ActionSleepEvE11_os_log_fmt_0
- __ZZN12AVE_WorkPool11ClearAllJobEvE11_os_log_fmt
- __ZZN12AVE_WorkPool11ClearAllJobEvE11_os_log_fmt_0
- __ZZN12AVE_WorkPool11ClearAllJobEvE11_os_log_fmt_1
- __ZZN12AVE_WorkPool11ClearAllJobEvE11_os_log_fmt_2
- __ZZN12AVE_WorkPool11MarkSkipCmdEP10_S_AVE_JobE11_os_log_fmt
- __ZZN12AVE_WorkPool12ActionNewCmdEvE11_os_log_fmt
- __ZZN12AVE_WorkPool12ActionNewCmdEvE11_os_log_fmt_0
- __ZZN12AVE_WorkPool13ActionJobDoneEvE11_os_log_fmt
- __ZZN12AVE_WorkPool13ActionJobDoneEvE11_os_log_fmt_0
- __ZZN12AVE_WorkPool14CheckSleepDoneEvE11_os_log_fmt_2
- __ZZN12AVE_WorkPool14ClearJobInTaskEP11_S_AVE_TaskE11_os_log_fmt
- __ZZN12AVE_WorkPool14ClearJobInTaskEP11_S_AVE_TaskE11_os_log_fmt_0
- __ZZN12AVE_WorkPool14ClearJobInTaskEP11_S_AVE_TaskE11_os_log_fmt_1
- __ZZN12AVE_WorkPool14ClearJobInTaskEP11_S_AVE_TaskE11_os_log_fmt_2
- __ZZN12AVE_WorkPool14ClearJobInTaskEP11_S_AVE_TaskE11_os_log_fmt_3
- __ZZN12AVE_WorkPool14WaitThreadIdleEjiE11_os_log_fmt
- __ZZN12AVE_WorkPool14WaitThreadIdleEjiE11_os_log_fmt_0
- __ZZN12AVE_WorkPool14WaitThreadIdleEjiE11_os_log_fmt_1
- __ZZN12AVE_WorkPool14WaitThreadIdleEjiE11_os_log_fmt_2
- __ZZN12AVE_WorkPool14WaitThreadIdleEjiE11_os_log_fmt_3
- __ZZN12AVE_WorkPool15GetIdleThreadIDEvE11_os_log_fmt_1
- __ZZN12AVE_WorkPool15GetIdleThreadIDEvE11_os_log_fmt_2
- __ZZN12AVE_WorkPool15GetIdleThreadIDEvE11_os_log_fmt_3
- __ZZN12AVE_WorkPool15ProcessInputJobEvE11_os_log_fmt
- __ZZN12AVE_WorkPool15ProcessInputJobEvE11_os_log_fmt_0
- __ZZN12AVE_WorkPool15ProcessInputJobEvE11_os_log_fmt_1
- __ZZN12AVE_WorkPool16ProcessAllNewCmdEvE11_os_log_fmt
- __ZZN12AVE_WorkPool16ProcessAllNewCmdEvE11_os_log_fmt_0
- __ZZN12AVE_WorkPool17WaitCloseTaskDoneEP11_S_AVE_TaskE11_os_log_fmt_2
- __ZZN12AVE_WorkPool17WaitCloseTaskDoneEP11_S_AVE_TaskE21kalloc_type_view_2028
- __ZZN12AVE_WorkPool18ClearJobInPriorityEP13_S_AVE_DLNodeE11_os_log_fmt
- __ZZN12AVE_WorkPool18ClearJobInPriorityEP13_S_AVE_DLNodeE11_os_log_fmt_0
- __ZZN12AVE_WorkPool18ProcessNewCmd_OpenEP14_S_AVE_WPParamiE11_os_log_fmt_1
- __ZZN12AVE_WorkPool19ClearTaskInPriorityEP13_S_AVE_DLNodeE21kalloc_type_view_1481
- __ZZN12AVE_WorkPool19ProcessAllOutputJobEvE11_os_log_fmt
- __ZZN12AVE_WorkPool19ProcessAllOutputJobEvE11_os_log_fmt_0
- __ZZN12AVE_WorkPool19ProcessAllOutputJobEvE11_os_log_fmt_1
- __ZZN12AVE_WorkPool21ProcessInputJobInTaskEP11_S_AVE_TaskE11_os_log_fmt
- __ZZN12AVE_WorkPool21ProcessInputJobInTaskEP11_S_AVE_TaskE11_os_log_fmt_0
- __ZZN12AVE_WorkPool21ProcessInputJobInTaskEP11_S_AVE_TaskE11_os_log_fmt_1
- __ZZN12AVE_WorkPool21ProcessInputJobInTaskEP11_S_AVE_TaskE11_os_log_fmt_2
- __ZZN12AVE_WorkPool22ProcessOutputJobInTaskEP11_S_AVE_TaskE11_os_log_fmt
- __ZZN12AVE_WorkPool22ProcessOutputJobInTaskEP11_S_AVE_TaskE11_os_log_fmt_0
- __ZZN12AVE_WorkPool22ProcessOutputJobInTaskEP11_S_AVE_TaskE11_os_log_fmt_1
- __ZZN12AVE_WorkPool23ProcessInputJobWhenIdleEvE11_os_log_fmt
- __ZZN12AVE_WorkPool23ProcessInputJobWhenIdleEvE11_os_log_fmt_0
- __ZZN12AVE_WorkPool25ProcessInputJobInPriorityEP13_S_AVE_DLNodeE11_os_log_fmt
- __ZZN12AVE_WorkPool26ProcessOutputJobInPriorityEP13_S_AVE_DLNodeE11_os_log_fmt
- __ZZN12AVE_WorkPool26ProcessOutputJobInPriorityEP13_S_AVE_DLNodeE11_os_log_fmt_0
- __ZZN12AVE_WorkPool7MoveJobEP10_S_AVE_Job15_E_AVE_WP_StageS2_E11_os_log_fmt
- __ZZN12AVE_WorkPool7MoveJobEP10_S_AVE_Job15_E_AVE_WP_StageS2_E11_os_log_fmt_0
- __ZZN12AVE_WorkPool7MoveJobEP10_S_AVE_Job15_E_AVE_WP_StageS2_E11_os_log_fmt_1
- __ZZN12AVE_WorkPool7MoveJobEP10_S_AVE_Job15_E_AVE_WP_StageS2_E11_os_log_fmt_2
- __ZZN12AVE_WorkPool7MoveJobEP10_S_AVE_Job15_E_AVE_WP_StageS2_E11_os_log_fmt_3
- __ZZN12AVE_WorkPool7SkipJobEP10_S_AVE_JobE11_os_log_fmt
- __ZZN12AVE_WorkPool7SkipJobEP10_S_AVE_JobE11_os_log_fmt_0
- __ZZN12AVE_WorkPool8OpenTaskEy15_E_AVE_WorkTypeiPP11_S_AVE_TaskE11_os_log_fmt
- __ZZN12AVE_WorkPool8OpenTaskEy15_E_AVE_WorkTypeiPP11_S_AVE_TaskE11_os_log_fmt_0
- __ZZN12AVE_WorkPool8OpenTaskEy15_E_AVE_WorkTypeiPP11_S_AVE_TaskE11_os_log_fmt_1
- __ZZN12AVE_WorkPool8OpenTaskEy15_E_AVE_WorkTypeiPP11_S_AVE_TaskE11_os_log_fmt_2
- __ZZN12AVE_WorkPool8OpenTaskEy15_E_AVE_WorkTypeiPP11_S_AVE_TaskE20kalloc_type_view_307
- __ZZN12AVE_WorkPool8OpenTaskEy15_E_AVE_WorkTypeiPP11_S_AVE_TaskE20kalloc_type_view_329
- __ZZN12AVE_WorkPool8WorkPoolEvE11_os_log_fmt
- __ZZN12AVE_WorkPool8WorkPoolEvE11_os_log_fmt_0
- __ZZN12AVE_WorkPool8WorkPoolEvE11_os_log_fmt_1
- __ZZN12AVE_WorkPool8WorkPoolEvE11_os_log_fmt_2
- __ZZN12AVE_WorkPool8WorkPoolEvE11_os_log_fmt_3
- __ZZN12AVE_WorkPool8WorkPoolEvE11_os_log_fmt_4
- __ZZN12AVE_WorkPool9CloseTaskEyiE20kalloc_type_view_393
- __ZZN12AVE_WorkPool9CloseTaskEyiE20kalloc_type_view_400
- __ZZN12AVE_WorkPool9NotifyJobEP10_S_AVE_JobiE11_os_log_fmt
- __ZZN12AVE_WorkPool9NotifyJobEP10_S_AVE_JobiE11_os_log_fmt_0
- __ZZN12AVE_WorkPool9NotifyJobEP10_S_AVE_JobiE11_os_log_fmt_1
- __ZZN14AVE_WorkThread10ProcessJobEvE11_os_log_fmt
- __ZZN14AVE_WorkThread10ProcessJobEvE11_os_log_fmt_0
- __ZZN14AVE_WorkThread10ProcessJobEvE11_os_log_fmt_1
- __ZZN14AVE_WorkThread10WorkThreadEvE11_os_log_fmt
- __ZZN14AVE_WorkThread10WorkThreadEvE11_os_log_fmt_0
- __ZZN14AVE_WorkThread10WorkThreadEvE11_os_log_fmt_1
- __ZZN14AVE_WorkThread10WorkThreadEvE11_os_log_fmt_2
- __ZZN14AVE_WorkThread10WorkThreadEvE11_os_log_fmt_3
- __ZZN14AVE_WorkThread10WorkThreadEvE11_os_log_fmt_4
- __ZZN14AVE_WorkThread9NotifyJobEP10_S_AVE_JobE11_os_log_fmt
- __ZZN14AVE_WorkThread9NotifyJobEP10_S_AVE_JobE11_os_log_fmt_0
- __ZZN14AVE_WorkThread9NotifyJobEP10_S_AVE_JobE11_os_log_fmt_1
- __ZZN16AVE_MD_IntraPred10PrepareJobEP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoE11_os_log_fmt
- __ZZN16AVE_MD_IntraPred10PrepareJobEP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoE11_os_log_fmt_0
- __ZZN16AVE_MD_IntraPred10PrepareJobEP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoE11_os_log_fmt_1
- __ZZN16AVE_MD_IntraPred10PrepareJobEP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoE11_os_log_fmt_2
- __ZZN16AVE_MD_IntraPred9ConfigDLBEP13_S_AVE_SVEMapE11_os_log_fmt
- __ZZN16AVE_MD_IntraPred9ConfigDLBEP13_S_AVE_SVEMapE11_os_log_fmt_0
- __ZZN16AVE_MD_IntraPred9ConfigDLBEP13_S_AVE_SVEMapE11_os_log_fmt_1
- __ZZN16AVE_MD_IntraPred9ConfigDLBEP13_S_AVE_SVEMapE11_os_log_fmt_2
- __ZZN19AppleAVE2UserClient4OpenEP20S_AVE_UCInParam_OpenP21S_AVE_UCOutParam_OpenE11_os_log_fmt_3
- __ZZN19AppleAVE2UserClient4OpenEP20S_AVE_UCInParam_OpenP21S_AVE_UCOutParam_OpenE11_os_log_fmt_6
- __ZZN19AppleAVE2UserClient4OpenEP20S_AVE_UCInParam_OpenP21S_AVE_UCOutParam_OpenE11_os_log_fmt_8
- __ZZN19AppleAVE2UserClient4StopEP20S_AVE_UCInParam_StopP21S_AVE_UCOutParam_StopE11_os_log_fmt_3
- __ZZN19AppleAVE2UserClient5CloseEP21S_AVE_UCInParam_CloseP22S_AVE_UCOutParam_CloseE11_os_log_fmt_3
- __ZZN19AppleAVE2UserClient5FlushEP21S_AVE_UCInParam_FlushP22S_AVE_UCOutParam_FlushE11_os_log_fmt_3
- __ZZN19AppleAVE2UserClient5ResetEP21S_AVE_UCInParam_ResetP22S_AVE_UCOutParam_ResetE11_os_log_fmt_3
- __ZZN19AppleAVE2UserClient5StartEP21S_AVE_UCInParam_StartP22S_AVE_UCOutParam_StartE11_os_log_fmt_3
- __ZZN19AppleAVE2UserClient7PrepareEP23S_AVE_UCInParam_PrepareP24S_AVE_UCOutParam_PrepareE11_os_log_fmt_3
- __ZZN19AppleAVE2UserClient7ProcessEP23S_AVE_UCInParam_ProcessP24S_AVE_UCOutParam_ProcessE11_os_log_fmt_3
- __ZZN19AppleAVE2UserClient8CompleteEP24S_AVE_UCInParam_CompleteP25S_AVE_UCOutParam_CompleteE11_os_log_fmt_3
- __ZZN25_S_AVE_SVESched_TimingMgrdlEPvmE19kalloc_type_view_51
- __ZZN25_S_AVE_SVESched_TimingMgrnwEmE19kalloc_type_view_51
- __ZZN6AVE_MD10PrintStateEjiPKciE11_os_log_fmt
- __ZZN6AVE_MD10PrintStateEjiPKciE11_os_log_fmt_0
- __ZZN6AVE_MD12ProcessInputEvE11_os_log_fmt
- __ZZN6AVE_MD12ProcessInputEvE11_os_log_fmt_0
- __ZZN6AVE_MD15ProcessInputCmdEP10_S_AVE_CmdE11_os_log_fmt
- __ZZN6AVE_MD15ProcessInputCmdEP10_S_AVE_CmdE11_os_log_fmt_0
- __ZZN6AVE_MD9AssignEUCEvE11_os_log_fmt
- __ZZN6AVE_MD9AssignEUCEvE11_os_log_fmt_1
- __ZZN6AVE_MD9AssignEUCEvE11_os_log_fmt_2
- __ZZN6AVE_MD9ConfigDLBEP13_S_AVE_SVEMapE11_os_log_fmt
- __ZZN6AVE_MD9ConfigDLBEP13_S_AVE_SVEMapE11_os_log_fmt_0
- __ZZN6AVE_MDdlEPvmE19kalloc_type_view_26
- __ZZN7AVE_DPM4InitEPK10_S_AVE_CfgjP8AVE_PMGRE11_os_log_fmt
- __ZZN7AVE_DPM4InitEPK10_S_AVE_CfgjP8AVE_PMGRE11_os_log_fmt_0
- __ZZN7AVE_DPM4InitEPK10_S_AVE_CfgjP8AVE_PMGRE11_os_log_fmt_1
- __ZZN7AVE_Drv20ProcessInputCmd_SyncEP13_S_AVE_ClientP10_S_AVE_CmdE11_os_log_fmt_1
- __ZZN7AVE_Drv22ProcessInputCmd_AssignEP13_S_AVE_ClientP10_S_AVE_CmdE11_os_log_fmt_3
- __ZZN7AVE_Drv22ProcessInputCmd_AssignEP13_S_AVE_ClientP10_S_AVE_CmdE11_os_log_fmt_4
- __ZZN7AVE_Drv22ProcessInputCmd_AssignEP13_S_AVE_ClientP10_S_AVE_CmdE11_os_log_fmt_5
- __ZZN7AVE_Drv22ProcessInputCmd_AssignEP13_S_AVE_ClientP10_S_AVE_CmdE11_os_log_fmt_6
- __ZZN7AVE_HwC4InitEP9IOServiceP10IOWorkLoopP28IOFilterInterruptEventSourcePK10_S_AVE_CfgP11AVE_DevInfoP14AVE_SurfaceMgrP10AVE_CryptojP11AVE_SurfaceP14_S_AVE_HistoryE11_os_log_fmt__32_
- __ZZN8Analyzer15miniGopDecisionEPA2_KiPS0_S2_S2_PK19_S_AVE_KeyFrameHintiiiiibiE11_os_log_fmt
- __ZZN8Analyzer15storeLRMEFSCostEPA2_KiiPA4_iE11_os_log_fmt
- __ZZN8Analyzer17scenecutDetectionEjPKiPA2_S0_S3_S1_jE11_os_log_fmt
- __ZZN8Analyzer17scenecutDetectionEjPKiPA2_S0_S3_S1_jE11_os_log_fmt_0
CStrings:
+ "\"iRevision < sizeof(gsc_saAVE_AXI2AF_Cfg_Erebus_8150[0]) / sizeof(gsc_saAVE_AXI2AF_Cfg_Erebus_8150[0][0])\" @%s:%d"
+ "\"iSVEID < sizeof(gsc_saAVE_AXI2AF_Cfg_Erebus_8150) / sizeof(gsc_saAVE_AXI2AF_Cfg_Erebus_8150[0])\" @%s:%d"
+ "%d %s"
+ "%dx%d - USAGE %s - codecType %s - eRCMode %d - B %d GOPFeature 0x%x slices %d - BITRATE %d\n"
+ "%dx%d - USAGE %s - codecType %s - eRCMode %d - REF %d B %d GOPFeature 0x%x slices %d - BITRATE %d\n"
+ "%dx%d - USAGE %s - codecType %s isHEIF %d - eRCMode %d - B %d GOPFeature 0x%x slices %d - BITRATE %d\n"
+ "%d|(%d %d)"
+ "%lld %d AVE %s: %dx%d - USAGE %s - codecType %s - eRCMode %d - B %d GOPFeature 0x%x slices %d - BITRATE %d\n"
+ "%lld %d AVE %s: %dx%d - USAGE %s - codecType %s - eRCMode %d - REF %d B %d GOPFeature 0x%x slices %d - BITRATE %d\n"
+ "%lld %d AVE %s: %dx%d - USAGE %s - codecType %s isHEIF %d - eRCMode %d - B %d GOPFeature 0x%x slices %d - BITRATE %d\n"
+ "%lld %d AVE %s: %s %s | %p %lld %s\n"
+ "%lld %d AVE %s: %s - debl %d - Quality (%f) - QP (I %d P %d B %d) - iMaxKeyFrameInterval %d\n"
+ "%lld %d AVE %s: %s Enter %p \n"
+ "%lld %d AVE %s: %s Enter %p %d %p %d\n"
+ "%lld %d AVE %s: %s Enter %p %llu %p\n"
+ "%lld %d AVE %s: %s Enter %p %p %p %p | %d %d %d | %p %p %p %p %p %p %p %p\n"
+ "%lld %d AVE %s: %s Exit %p %d %p %d %d\n"
+ "%lld %d AVE %s: %s Exit %p %d %p %d %p %d\n"
+ "%lld %d AVE %s: %s Exit %p %llu %p %d\n"
+ "%lld %d AVE %s: %s Exit %p %p %p %d %d\n"
+ "%lld %d AVE %s: %s Exit %p %p %p %p | %d %d %d | %p %p %p %p %p %p %p %p %d\n"
+ "%lld %d AVE %s: %s Exit %p%p %d\n"
+ "%lld %d AVE %s: %s:%d %lld %d %d %d %d DS %p | RC %d %p | inter %d %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %p %d %p | %p %d | %d %d %p\n"
+ "%lld %d AVE %s: %s:%d %p %d Frame[%d] dis %d | intra %d inter(FS) %d %d %d | SADSumZero %d %d | ZeroMvBinCnt %d %d | RC Cost %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %p %lld %p %d %lld input Q %d - %d | %d\n"
+ "%lld %d AVE %s: %s:%d %p %lld input Q number may not satified %d %d %d | %d\n"
+ "%lld %d AVE %s: %s:%d %p CmdPerSec: %4d, Cnt: %5d, Tile: %4dx%4d, MB: %6d, Time: %5d micro-s\n"
+ "%lld %d AVE %s: %s:%d %s | could not get output set %p %d %p %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to create mutex %p %llu %p %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to initialize RC %p %llu %p %lld %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to post-update UCInfo %p %llu %p %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to pre-update UCInfo %p %llu %p %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to allocate block pool %p %p %lld\n"
+ "%lld %d AVE %s: %s:%d %s | failed to calculate surface info %p %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to calculate surface info %p %llu %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to config MD %p %lld | %p %lld %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to configurate pipeline %p %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to configure DLB %p %d %p %d %p %p %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to create MiniDevice %p %llu\n"
+ "%lld %d AVE %s: %s:%d %s | failed to create MiniDevice %p %llu | %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to create block pool %p %p %lld %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to create external surfaces %p %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to create external surfaces %p %llu %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to create internal surfaces %p %llu %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to create surface %s %lld %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to create surface header %s %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to dart map external surfaces %p %llu %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to dart map internal surfaces %p %llu %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to dart map surfaces %p %d %p %d %p %p %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to find GOP decision MD %p %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to find intra prediction MD %p %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to get block from block pool %p %d %p %d %lld %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to initial MiniDevice %p %lld %p %d\n"
+ "%lld %d AVE %s: %s:%d %s | failed to initialize pipeline %p\n"
+ "%lld %d AVE %s: %s:%d %s | failed to uninitialize work pool %p %d\n"
+ "%lld %d AVE %s: %s:%d %s | firmware buffer luma header is invalid %d %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | firmware header buffer is invalid %d\n"
+ "%lld %d AVE %s: %s:%d %s | firmware header buffer is invalid %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | invalid L0a low res ref Chroma firmware buffer %p %d %p %d %p\n"
+ "%lld %d AVE %s: %s:%d %s | invalid L0a low res ref Chroma header firmware buffer %p %d %p %d %p\n"
+ "%lld %d AVE %s: %s:%d %s | invalid L0a low res ref luma header firmware buffer %p %d %p %d %p\n"
+ "%lld %d AVE %s: %s:%d %s | invalid L0b low res ref Chroma firmware buffer %p %d %p %d %p\n"
+ "%lld %d AVE %s: %s:%d %s | invalid L0b low res ref luma header firmware buffer %p %d %p %d %p\n"
+ "%lld %d AVE %s: %s:%d %s | invalid L1 low res ref Chroma firmware buffer %p %d %p %d %p\n"
+ "%lld %d AVE %s: %s:%d %s | invalid L1 low res ref Chroma header firmware buffer %p %d %p %d %p\n"
+ "%lld %d AVE %s: %s:%d %s | invalid L1 low res ref luma header firmware buffer %p %d %p %d %p\n"
+ "%lld %d AVE %s: %s:%d %s | invalid entropy coding header firmware buffer %p %d %p %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | library and driver mismatch %d %d %p %lld %s <- %s\n"
+ "%lld %d AVE %s: %s:%d %s | no enough memory for task command %p %d %p %d %d %ld\n"
+ "%lld %d AVE %s: %s:%d %s | no enough memory in the block buffer %p %lld %p %p %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | pipeline mismatch %p %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | surface is not correct %lld %d %d %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | surface is not enough %lld %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | surface is not enough %lld %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | wrong DLB configuration %d %d %p %lld\n"
+ "%lld %d AVE %s: %s:%d %s | wrong DLB configuration %p %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | wrong DPM configuration %d %d %p %lld\n"
+ "%lld %d AVE %s: %s:%d %s | wrong UC Info index %d %d %p %lld %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | wrong UC info surface %d %d %p %lld %d\n"
+ "%lld %d AVE %s: %s:%d %s | wrong callback %d %d %p %lld 0x%llx 0x%llx\n"
+ "%lld %d AVE %s: %s:%d %s | wrong common parameters %d %d %p %lld %d\n"
+ "%lld %d AVE %s: %s:%d %s | wrong common parameters %p %lld %d\n"
+ "%lld %d AVE %s: %s:%d %s | wrong data count %d %d %p %lld %lld\n"
+ "%lld %d AVE %s: %s:%d %s | wrong encode type %d %d %p %lld %d\n"
+ "%lld %d AVE %s: %s:%d %s | wrong enode mode %d %d %p %lld %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | wrong log configuration %d %d %p %lld\n"
+ "%lld %d AVE %s: %s:%d %s | wrong mode %d %d %p %lld\n"
+ "%lld %d AVE %s: %s:%d %s | wrong parameter %d %d %p\n"
+ "%lld %d AVE %s: %s:%d %s | wrong parameters %p %llu %p\n"
+ "%lld %d AVE %s: %s:%d %s | wrong parameters %p %p %lld %p\n"
+ "%lld %d AVE %s: %s:%d %s | wrong parameters %p %p %p %lld %p\n"
+ "%lld %d AVE %s: %s:%d DLBEntry %p %d transition is done\n"
+ "%lld %d AVE %s: %s:%d DLBUnit %p %d | %d - 0x%x %d %d %d | [ %s ]\n"
+ "%lld %d AVE %s: %s:%d DLBUnit %p %d | %d - 0x%x %d %d %d | { %s }\n"
+ "%lld %d AVE %s: %s:%d EUMap %p %d | < %s >\n"
+ "%lld %d AVE %s: %s:%d EUMap %p %d | [ %s ]\n"
+ "%lld %d AVE %s: %s:%d EUStats %d | %s\n"
+ "%lld %d AVE %s: %s:%d Skip the higher layer %p %lld %d\n"
+ "%lld %d AVE %s: %s:%d frame drop\n"
+ "%lld %d AVE %s: %s:%d invalid EUMap %p %d | [ %s ]\n"
+ "%lld %d AVE %s: %s:%d | %p %d %p %d | %p %lld %d %d\n"
+ "%lld %d AVE %s: %s:%d | %p %d %p %d | %p %lld %d %d | %d\n"
+ "%lld %d AVE %s: %s:%d | %p %d %p %d | %p %lld %d %d | %d %d\n"
+ "%lld %d AVE %s: %s:%d | %p %d %p %d | %p %lld %d %p %d %d\n"
+ "%lld %d AVE %s: %s::%s Enter %p %d %d %d %d %d %p %p %p %p %p %p %p\n"
+ "%lld %d AVE %s: %s::%s Enter %p %d %p %p %d %d\n"
+ "%lld %d AVE %s: %s::%s Enter %p %lld 0x%llx\n"
+ "%lld %d AVE %s: %s::%s Exit %p %d %d %d %d %d %p %p %p %p %p %p %p %d\n"
+ "%lld %d AVE %s: %s::%s Exit %p %d %p %p %d %d %d\n"
+ "%lld %d AVE %s: %s::%s Exit %p %lld 0x%llx %d\n"
+ "%lld %d AVE %s: %s::%s:%d %p %d %lld %d %p | %d %d | %d %d %d | %d %d %d | %d %d | %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %p %d %p %d %d task command %d task %p %lld\n"
+ "%lld %d AVE %s: %s::%s:%d %p %d Cur %d ToFrm %d | pool %d %d | flush %d | enc %d dis %d | %d %ld\n"
+ "%lld %d AVE %s: %s::%s:%d %p %d | <WPParam> %p | <Info> %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %p %lld %d %d %d \n"
+ "%lld %d AVE %s: %s::%s:%d %p %lld %d | %s\n"
+ "%lld %d AVE %s: %s::%s:%d %p %lld %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %p %lld | %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %p %lld | %d %d | %p %d | %lld %d %d %d | %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %p %lld | %p %d | %lld %d %d | %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %p %p %d %p %d QUEUESIZE %d %d %d | %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %p work thread gets task command %d %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | external surfaces are wrong %p %lld %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | fail to create command %p %lld %p %d %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | fail to generate id2idx %p %lld %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | fail to init bit allocation ratio array %p %d | %d %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | fail to initial SVE DPB %p %lld %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | fail to initial SVE GOP %p %lld %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | fail to initial SVE RC %p %lld %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to DART map external surfaces %p %llu %p %d %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to DART map internal surfaces %p %llu %p %d %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to DART unmap external surfaces %p %llu %p %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to calculate DPM threshold %p %lld %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to config SVE Scheduler %p %lld %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to create CR %p %lld %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to create DPB %p %lld %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to create SVE GOP %p %lld %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to create SVE RC %p %lld %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to create external in surfaces %p %lld %p %d %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to create external out surfaces %p %lld %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to create internal surfaces %p %lld %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to create new task command %p %d %p %lld %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to create task %p %d %p %p\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to destroy external surfaces %p %lld %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to destroy internal surfaces %p %lld %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to find CHM %p %lld %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to handle commands %p %lld %p %d 0x%x 0x%x %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to init GOP decision task command %p %lld %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to init base %p %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to init base %p %p %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to init intra inter cost task command %p %lld %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to initialize DPB %p %d %p %lld\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to initialize GOP decision %p %lld %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to initialize intra prediction %p %lld %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to manage DPB %p %lld %p %d %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to manage RC %p %lld %p %d %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to prepare intrainter cost task command %p %d %p %d %p %d %lld %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to set input of intra inter cost %p %lld %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to uninitialize GOP decision %p %lld %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to uninitialize GOP decision task command %p %lld %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to uninitialize intra inter cost task command %p %lld %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to uninitialize intra prediction %p %lld %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to update output buffer status %p %lld | %p %d %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | invalid coded header buffer %p %lld | %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | invalid command counter %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | invalid command counter %p %d %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | invalid priority %p %d %p %d %p\n"
+ "%lld %d AVE %s: %s::%s:%d %s | invalid state %p %d %p %d %p\n"
+ "%lld %d AVE %s: %s::%s:%d %s | invalid task command %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | invalid task command %p %d %p\n"
+ "%lld %d AVE %s: %s::%s:%d %s | invalid task command %p %d %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | previous task command not done %p %d %p\n"
+ "%lld %d AVE %s: %s::%s:%d %s | process command error %p %d | %p %d | %lld %d | %p %p %p %p %d %d | %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | request task command during work pool sleep %p %d %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | unsupportted SVE Sched Mode %p %lld %p %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | usage mode is not supported %p %lld %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong command %p %d 0x%lx %d 0x%x %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong input parameters %p %d %p %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong parameters %p %d %p %d %ld\n"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong parameters %p %lld %p\n"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong parameters %p %lld %p %d %p %p %p\n"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong result %p %d %p %d %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong result %p %d %p %d %p %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong stage %p %d %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong state %p %d %p %p %p\n"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong thread %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d -- %p %lld %p %d | %d %d %p\n"
+ "%lld %d AVE %s: %s::%s:%d Client info %p %d %s | %d %d %d | %d | %lld\n"
+ "%lld %d AVE %s: %s::%s:%d DPB Entry %p %d | %p 0x%x %lld %d %d | %p %p %p %p %p| %d %p %p %p %p %p| %d %p %p %p %p %p\n"
+ "%lld %d AVE %s: %s::%s:%d Enter %p %d %p\n"
+ "%lld %d AVE %s: %s::%s:%d Exit %p %d %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d L0 ref entry %p %d | %d %lld %d %d %d | %p %p %p %p %p\n"
+ "%lld %d AVE %s: %s::%s:%d L1 ref entry %p %d | %d %lld %d %d %d | %p %p %p %p %p\n"
+ "%lld %d AVE %s: %s::%s:%d Surface Info %p %lld\n"
+ "%lld %d AVE %s: %s::%s:%d TimeOut %d %lld | %lld %d\n"
+ "%lld %d AVE %s: %s::%s:%d command not in proc %p %d %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d failed to clear command in priority %p %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d failed to clear command in task %p %d %p %lld %d\n"
+ "%lld %d AVE %s: %s::%s:%d failed to notify command %p %d %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d failed to process output command in priority %p %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d failed to process output command in task %p %d %p %lld %d\n"
+ "%lld %d AVE %s: %s::%s:%d keep busying %p %d %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d list is not empty %p %d %p %lld %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d process command %p %d %p %d %lld %d %p %p\n"
+ "%lld %d AVE %s: %s::%s:%d receive command done %p %d %p %d %lld\n"
+ "%lld %d AVE %s: %s::%s:%d selected EU %p %lld | %d %p %d %d %d %d %lld\n"
+ "%lld %d AVE %s: %s::%s:%d thread terminated %p %d %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d unsupported work type %p %llu %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d wait %p %d %p %d %p\n"
+ "%lld %d AVE %s: %s::%s:%d wait %p %d %p %d %p %d %llu\n"
+ "%lld %d AVE %s: %s::%s:%d wait with timeout %p %d %d %p %d %p %d %llu\n"
+ "%lld %d AVE %s: %s::%s:%d wrong command counter %p %d %d %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d wrong command counter %p %d %d %d %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d wrong command counter in task %p %d %p %d %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d wrong command counter in task %p %d %p %d %d %d %d %d\n"
+ "%lld %d AVE %s: Analytics: %s(%d) %s(%d) %s(%d%%) %s(%d%%) %s(%d%%) %s(%d%%) %s(%d%%) %s(%d%%)\n"
+ "%lld %d AVE %s: BFramesMVaveThreshold XY %d %d BFramesIntraMBThreshold PB %d %d Extra PB %d %d\n"
+ "%lld %d AVE %s: Client Surface info: \n"
+ "%lld %d AVE %s: Client%s: %p ID: %d EUMap: %s\n"
+ "%lld %d AVE %s: DLB: %d - %d %d %d %s\n"
+ "%lld %d AVE %s: DLBUnit %s | %p %d | %d - 0x%x %d %d %d || %s\n"
+ "%lld %d AVE %s: DPM: 0x%x\n"
+ "%lld %d AVE %s: Mini-Device%s: %p ID: %lld %d %d\n"
+ "%lld %d AVE %s: SVESched %s | %p %d | %d | %d %d %d %lld %d\n"
+ "%lld %d AVE %s: bMinimizeMemoryUsage %d iOutputBufSizeFactor %d bPrioritizeEncodingSpeedOverQuality %d\n"
+ "%lld %d AVE %s: debl %d - Quality (%f) - QP (I %d P %d B %d) - iMaxKeyFrameInterval %d\n"
+ "%lld %d AVE %s: eThroughputMode %d bChangeBitrateAtNextIDR %d\n"
+ "%s %s | %p %lld %s\n"
+ "%s - debl %d - Quality (%f) - QP (I %d P %d B %d) - iMaxKeyFrameInterval %d\n"
+ "%s-%lld"
+ "%s-%lld-%d"
+ "%s::%s:%d "
+ "(eCurrStage >= AVE_WP_Stage_Input) && (eNewStage <= AVE_WP_Stage_Output) && (eCurrStage < eNewStage)"
+ "(pBuf != nullptr) && (psTask->iBufSize >= sizeof(*psTCmd))"
+ "(psCmd != nullptr) && (iSize >= sizeof(S_AVE_WPOutParam_Open))"
+ "(psCmd != nullptr) && (iSize >= sizeof(S_AVE_WPOutParam_Start))"
+ "(psInCmdOpen->iPriority >= -100) && (psInCmdOpen->iPriority <= 200)"
+ "(waitResult == 0) || (waitResult == 1)"
+ "*piBufOffset <= iBufSize"
+ "- %d %d "
+ "- %d (%d %d %d %d) "
+ "1121222222222222222222222222"
+ "112221222222111111"
+ "12111111111112222112222211111111111111111111111121222221122222222222222222222222222222222222111111112222222222222222222222222222222211111111"
+ "12111112122212121111111111111221111111111111"
+ "12221"
+ "12221211"
+ "12221222222211121111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
+ "211222222222222222222222222222222222222222222222"
+ "222111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111112222122222222222222222222222222222222221111111111111111111111222222222222222222222211222212222222222222222222222222222222222111111111111111111111122222222222222222222221122221222222222222222222222222222222222211111111111111111111112222222222222222222222112222122222222222222222222222222222222221111111111111111111111222222222222222222222211222212222222222222222222222222222222222111111111111111111111122222222222222222222221122221222222222222222222222222222222222211111111111111111111112222222222222222222222112222122222222222222222222222222222222221111111111111111111111222222222222222222222211222212222222222222222222222222222222222111111111111111111111122222222222222222222221122221222222222222222222222222222222222211111111111111111111112222222222222222222222112222122222222222222222222222222222222221111111111111111111111222222222222222222222211222212222222222222222222222222222222222111111111111111111111122222222222222222222221122221222222222222222222222222222222222211111111111111111111112222222222222222222222112222122222222222222222222222222222222221111111111111111111111222222222222222222222211222212222222222222222222222222222222222111111111111111111111122222222222222222222221122221222222222222222222222222222222222211111111111111111111112222222222222222222222112222122222222222222222222222222222222221111111111111111111111222222222222222222222211222212222222222222222222222222222222222111111111111111111111122222222222222222222221122221222222222222222222222222222222222211111111111111111111112222222222222222222222112222122222222222222222222222222222222221111111111111111111111222222222222222222222211222212222222222222222222222222222222222111111111111111111111122222222222222222222221122221222222222222222222222222222222222211111111111111111111112222222222222222222222112222122222222222222222222222222222222221111111111111111111111222222222222222222222211222212222222222222222222222222222222222111111111111111111111122222222222222222222221122221222222222222222222222222222222222211111111111111111111112222222222222222222222112222122222222222222222222222222222222221111111111111111111111222222222222222222222211"
+ "22:04:44"
+ "802.61.1"
+ "AVE_CheckExternalInSurfaces"
+ "AVE_Client_AssignEU"
+ "AVE_Client_PreUpdate"
+ "AVE_Client_UpdateOutputBuf"
+ "AVE_DLB_AllocEUNum"
+ "AVE_DLB_AllocUnit"
+ "AVE_DLB_ApplyDynamic"
+ "AVE_DLB_ApplyStatic"
+ "AVE_DLB_AssignUnit"
+ "AVE_DLB_CleanUnit"
+ "AVE_DLB_SelectUnit"
+ "AVE_EncMode_None < pIn->eEncMode && pIn->eEncMode < AVE_EncMode_Max"
+ "AVE_IOP_CheckIdle_Erebus"
+ "AVE_IOP_Config_Erebus"
+ "AVE_IOP_GetCurrTime_Erebus"
+ "AVE_IOP_Start_Erebus"
+ "AVE_Pipeline_AssignEUC"
+ "AVE_Pipeline_CalcInputQueueNum"
+ "AVE_Pipeline_CalcSurfaceInfo"
+ "AVE_Pipeline_Construct"
+ "AVE_Pipeline_CreateExternalSurfaces"
+ "AVE_Pipeline_CreateInternalSurfaces"
+ "AVE_Pipeline_CreateSurfaces"
+ "AVE_Pipeline_DARTMapExternalSurfaces"
+ "AVE_Pipeline_DARTMapInternalSurfaces"
+ "AVE_Pipeline_DARTMapSurfaces"
+ "AVE_Pipeline_DARTUnmapSurfaces"
+ "AVE_Pipeline_DestroyExternalSurfaces"
+ "AVE_Pipeline_DestroyInternalSurfaces"
+ "AVE_Pipeline_DestroySurfaces"
+ "AVE_Pipeline_Destruct"
+ "AVE_Pipeline_PostUpdate"
+ "AVE_Pipeline_PreUpdate"
+ "AVE_PrintClientSurfaces"
+ "AVE_SwC_CalcTaskBufSize"
+ "AVE_TaskCmd_Create"
+ "AVE_TaskCmd_GOPDecision"
+ "AVE_TaskCmd_GOPDecision_Init"
+ "AVE_TaskCmd_GOPDecision_Uninit"
+ "AVE_TaskCmd_IntraInterCost"
+ "AVE_TaskCmd_IntraInterCost_Init"
+ "AVE_TaskCmd_IntraInterCost_SetInput"
+ "AVE_TaskCmd_IntraInterCost_Uninit"
+ "AVE_Thread"
+ "AVE_UCCmd_CheckParam"
+ "AVE_UCCmd_CheckParam_Close"
+ "AVE_UCCmd_CheckParam_Complete"
+ "AVE_UCCmd_CheckParam_Config"
+ "AVE_UCCmd_CheckParam_Flush"
+ "AVE_UCCmd_CheckParam_Open"
+ "AVE_UCCmd_CheckParam_Prepare"
+ "AVE_UCCmd_CheckParam_Process"
+ "AVE_UCCmd_CheckParam_Reset"
+ "AVE_UCCmd_CheckParam_Start"
+ "AVE_UCCmd_CheckParam_Stop"
+ "AVE_Work_Enc_UpdateFrameInfoFromOutputData"
+ "AVE_Work_LRME_PostUpdate"
+ "AVE_Work_MCTF_PostUpdate"
+ "AcquireOutputBuf"
+ "Analytics: %s(%d) %s(%d) %s(%d%%) %s(%d%%) %s(%d%%) %s(%d%%) %s(%d%%) %s(%d%%)\n"
+ "AttachEUC"
+ "BFramesMVaveThreshold XY %d %d BFramesIntraMBThreshold PB %d %d Extra PB %d %d\n"
+ "CalcInputQueueNum"
+ "CalcSurfaceInfo"
+ "CheckCmdCnt"
+ "CheckOutputBuf_Quota"
+ "CheckTaskCmdCnt"
+ "ClearCmd"
+ "ClearCmdInPriority"
+ "ClearCmdInTask"
+ "Client Surface info: \n"
+ "Client%s: %p ID: %d EUMap: %s\n"
+ "CondSignal"
+ "CondTimedWait"
+ "CondWait"
+ "CreateExternalSurfaces"
+ "CreateInternalSurfaces"
+ "CreateThread"
+ "DARTMapExternalSurfaces"
+ "DARTMapInternalSurfaces"
+ "DARTUnmapExternalSurfaces"
+ "DARTUnmapInternalSurfaces"
+ "DLB: %d - %d %d %d %s\n"
+ "DLBUnit %s | %p %d | %d - 0x%x %d %d %d || %s\n"
+ "DPM: 0x%x\n"
+ "DestroyExternalSurfaces"
+ "DestroyInternalSurfaces"
+ "DetachEUC"
+ "EntropyCodingHeader"
+ "GGM"
+ "ID: %d %s | EU: "
+ "Jul  1 2024"
+ "LowResRefChroma"
+ "LowResRefChromaHeader"
+ "LowResRefLumaHeader"
+ "Mini-Device%s: %p ID: %lld %d %d\n"
+ "NotifyCmd"
+ "NotifyCmdDone"
+ "PostUpdate"
+ "PreUpdate"
+ "PrepareTaskCmd"
+ "ProcessInputCmdInPriority"
+ "ProcessInputCmdInTask"
+ "ProcessOutputCmd"
+ "ProcessOutputCmdInPriority"
+ "ProcessOutputCmdInTask"
+ "ProcessSleep"
+ "ProcessTermination"
+ "ReleaseOutputBuf"
+ "RequestTaskCmd"
+ "SVESched %s | %p %d | %d | %d %d %d %lld %d\n"
+ "SkipCmd"
+ "Thread"
+ "ThroughputModeRatioSlow"
+ "ThroughputModeRatioUltra1"
+ "UpdateOutputBuf_Status"
+ "WaitEvent"
+ "bMinimizeMemoryUsage %d iOutputBufSizeFactor %d bPrioritizeEncodingSpeedOverQuality %d\n"
+ "debl %d - Quality (%f) - QP (I %d P %d B %d) - iMaxKeyFrameInterval %d\n"
+ "eGOPMode > AVE_GOPMode_None && eGOPMode < AVE_GOPMode_Max"
+ "eMode < AVE_ThroughputMode_Max"
+ "iSVENum > 0 && iSVENum <= 4"
+ "m_iaCurrCmdCnt[AVE_WP_Stage_Input] == 0"
+ "m_iaCurrCmdCnt[AVE_WP_Stage_Output] == 0"
+ "m_pcIODrv != nullptr && m_psNotificationPort != nullptr && m_psClient != nullptr"
+ "m_pcaWorkThread[iThreadID] != nullptr"
+ "m_psDLB->iMode == 0"
+ "m_psTCmd == nullptr"
+ "m_psaTCmd[iThreadID] == nullptr"
+ "num == 0 || num >= psSInfoSet->iaRecon[AVE_SIIdx_Set]"
+ "pClient != nullptr && pDLBInfo != nullptr"
+ "pClient != nullptr && pUCInfo != nullptr && pCodedHeader != nullptr"
+ "pClient->pcaSurfacePool[AVE_SurPoolIdx_LRRCRes] != nullptr"
+ "pClient->pcaSurfacePool[AVE_SurPoolIdx_LRRef] != nullptr"
+ "pClient->pcaSurfacePool[AVE_SurPoolIdx_LRRes] != nullptr"
+ "pDevInfo != nullptr && pCfg != nullptr && id < 8 && pPMGR != nullptr"
+ "pIn != nullptr"
+ "pIn->iDataCnt >= 0"
+ "pIn->iUCInfoIdx >= 0"
+ "pIn->iUCInfoSID > 0"
+ "pIn->sTimeOut.iTimeOut >= 0 && pIn->sTimeOut.iStartTime >= 0"
+ "pInfo->sExtraBuff.saCavlcHeader[i].iAddr != 0"
+ "pInfo->sRef.saLow_Res_UV_L0[AVE_REFERENCE_A].iAddr != 0"
+ "pInfo->sRef.saLow_Res_UV_L0[AVE_REFERENCE_B].iAddr != 0"
+ "pInfo->sRef.saLow_Res_UV_L0_Header[AVE_REFERENCE_A].iAddr != 0"
+ "pInfo->sRef.saLow_Res_UV_L0_Header[AVE_REFERENCE_B].iAddr != 0"
+ "pInfo->sRef.saLow_Res_UV_L1[AVE_REFERENCE_A].iAddr != 0"
+ "pInfo->sRef.saLow_Res_UV_L1_Header[AVE_REFERENCE_A].iAddr != 0"
+ "pInfo->sRef.saLow_Res_Y_L0_Header[AVE_REFERENCE_A].iAddr != 0"
+ "pInfo->sRef.saLow_Res_Y_L0_Header[AVE_REFERENCE_B].iAddr != 0"
+ "pInfo->sRef.saLow_Res_Y_L1_Header[AVE_REFERENCE_A].iAddr != 0"
+ "pSVESched != nullptr && psEUMap != nullptr"
+ "pSVESched->iActiveSVENum == pEUMap->iNum"
+ "pSet->pcaRecon[i][j][k]->GetSize() >= psSInfoSet->iaRecon[AVE_SIIdx_Size]"
+ "pUCInfo->frameNumber == pCodedHeader->FrameNumberFromDriverReturned"
+ "pVP->saEntropyCodingHeader[0].iAddr != 0"
+ "pVP->saEntropyCodingHeader[i].iAddr != 0"
+ "pVP->saLowResChromaHeader[j][k].iAddr != 0"
+ "pVP->saLowResChroma[j][k].iAddr != 0"
+ "pVP->saLowResHeader[j][k].iAddr != 0"
+ "piaSID2Idx != nullptr && iIdxSize <= sizeof(m_iaSVEID2IDX)/sizeof(*m_iaSVEID2IDX)"
+ "psPL != nullptr && pClient != nullptr"
+ "psPL != nullptr && pDLBInfo != nullptr"
+ "psPL->eMode == eMode"
+ "psTCmd != nullptr"
+ "psTCmd->pMutex != nullptr"
+ "psTask->iaCurrCmdCnt[AVE_WP_Stage_Input] == 0"
+ "psTask->iaCurrCmdCnt[AVE_WP_Stage_Output] == 0"
+ "psTask->pcBlkPool != nullptr"
+ "site.AVE_Thread"
+ "storeLRMECost"
+ "tmpLayer == 0 || tmpLayer >= psSInfoSet->iaRecon[AVE_SIIdx_Layer]"
+ "tmpNum == 0 || tmpNum >= psSInfoSet->iaRecon[AVE_SIIdx_Num]"
+ "waitResult == 0"
- " -> "
- "\"AVE_DLList_Empty(&psTask->saJob[stage])\" @%s:%d"
- "\"eCurrStage < eNewStage\" @%s:%d"
- "\"eCurrStage >= AVE_WP_Stage_Input\" @%s:%d"
- "\"eNewStage <= AVE_WP_Stage_Output\" @%s:%d"
- "\"iSize >= sizeof(S_AVE_WPOutParam_Open)\" @%s:%d"
- "\"iSize >= sizeof(S_AVE_WPOutParam_Start)\" @%s:%d"
- "\"m_eState == AVE_WorkThread_State_Busy\" @%s:%d"
- "\"m_eState == AVE_WorkThread_State_Idle\" @%s:%d"
- "\"m_iaCurrJobCounter[AVE_WP_Stage_Input] == 0\" @%s:%d"
- "\"m_iaCurrJobCounter[AVE_WP_Stage_Output] == 0\" @%s:%d"
- "\"m_iaTotalJobCounter[AVE_WP_Stage_Input] == m_iaCurrJobCounter[AVE_WP_Stage_Input] + m_iaCurrJobCounter[AVE_WP_Stage_Run] + m_iaTotalJobCounter[AVE_WP_Stage_Output]\" @%s:%d"
- "\"m_iaTotalJobCounter[AVE_WP_Stage_Input] == m_iaCurrJobCounter[AVE_WP_Stage_Input] + m_iaTotalJobCounter[AVE_WP_Stage_Run] + m_iControlJobCounter + m_iSkippedJobCounter\" @%s:%d"
- "\"m_iaTotalJobCounter[AVE_WP_Stage_Output] == m_iaTotalJobCounter[AVE_WP_Stage_Run] - m_iaCurrJobCounter[AVE_WP_Stage_Run] + m_iControlJobCounter + m_iSkippedJobCounter\" @%s:%d"
- "\"m_pcaWorkThread[iThreadID] != NULL\" @%s:%d"
- "\"m_psJob == NULL\" @%s:%d"
- "\"psCmd != NULL\" @%s:%d"
- "\"psTask->iaCurrJobCounter[AVE_WP_Stage_Input] == 0\" @%s:%d"
- "\"psTask->iaCurrJobCounter[AVE_WP_Stage_Output] == 0\" @%s:%d"
- "\"psTask->iaTotalJobCounter[AVE_WP_Stage_Input] == psTask->iaCurrJobCounter[AVE_WP_Stage_Input] + psTask->iaCurrJobCounter[AVE_WP_Stage_Run] + psTask->iaTotalJobCounter[AVE_WP_Stage_Output]\" @%s:%d"
- "\"psTask->iaTotalJobCounter[AVE_WP_Stage_Input] == psTask->iaCurrJobCounter[AVE_WP_Stage_Input] + psTask->iaTotalJobCounter[AVE_WP_Stage_Run] + psTask->iControlJobCounter + psTask->iSkippedJobCounter\" @%s:%d"
- "\"psTask->iaTotalJobCounter[AVE_WP_Stage_Output] == psTask->iaTotalJobCounter[AVE_WP_Stage_Run] - psTask->iaCurrJobCounter[AVE_WP_Stage_Run] + psTask->iControlJobCounter + psTask->iSkippedJobCounter\" @%s:%d"
- "\"wait_result == THREAD_TIMED_OUT\" @%s:%d"
- "%dx%d - USAGE %s - codecType %s - eRCMode %d - B %d GOPFeature 0x%x CODED_BUFFERS %d - slices %d - BITRATE %d\n"
- "%dx%d - USAGE %s - codecType %s - eRCMode %d - REF %d B %d GOPFeature 0x%x CODED_BUFFERS %d - slices %d - BITRATE %d\n"
- "%dx%d - USAGE %s - codecType %s isHEIF %d - eRCMode %d - B %d GOPFeature 0x%x CODED_BUFFERS %d - slices %d - BITRATE %d\n"
- "%d|(%d 0x%x)"
- "%lld %d AVE %s: %dx%d - USAGE %s - codecType %s - eRCMode %d - B %d GOPFeature 0x%x CODED_BUFFERS %d - slices %d - BITRATE %d\n"
- "%lld %d AVE %s: %dx%d - USAGE %s - codecType %s - eRCMode %d - REF %d B %d GOPFeature 0x%x CODED_BUFFERS %d - slices %d - BITRATE %d\n"
- "%lld %d AVE %s: %dx%d - USAGE %s - codecType %s isHEIF %d - eRCMode %d - B %d GOPFeature 0x%x CODED_BUFFERS %d - slices %d - BITRATE %d\n"
- "%lld %d AVE %s: %s - debl %d - Quality (%d) - QP (I %d P %d B %d) - iMaxKeyFrameInterval %d\n"
- "%lld %d AVE %s: %s Enter %p %llu\n"
- "%lld %d AVE %s: %s Enter %p %p %p %p | %d %d %d | %p %p %p %p %p %p %p\n"
- "%lld %d AVE %s: %s Exit %p %llu %d\n"
- "%lld %d AVE %s: %s Exit %p %p %p %p | %d %d %d | %p %p %p %p %p %p %p %d\n"
- "%lld %d AVE %s: %s:%d %d %d %d \n"
- "%lld %d AVE %s: %s:%d %d %d %d %d %d DS %p | RC %d %p | inter %d %d %d %d\n"
- "%lld %d AVE %s: %s:%d %d %d | %d %d %d %d | %d %d %d %d | %d %d %d %d\n"
- "%lld %d AVE %s: %s:%d %p %d %d\n"
- "%lld %d AVE %s: %s:%d %p %d %d cnt %d %d %d %d\n"
- "%lld %d AVE %s: %s:%d %p %d %p %d %d %d\n"
- "%lld %d AVE %s: %s:%d %p %d Frame[%d] dis %d | intra %d inter %d %d | SADSumZero %d %d | ZeroMvBinCnt %d %d\n"
- "%lld %d AVE %s: %s:%d %p %d | %d %d %d\n"
- "%lld %d AVE %s: %s:%d %p %d | %p %d | %lld %d %d %d | %d %d %d\n"
- "%lld %d AVE %s: %s:%d %p %d | %p %d | %lld %d %d | %d %d %d\n"
- "%lld %d AVE %s: %s:%d %p %p %d %p %d QUEUESIZE %d %d %d | %d %d %d\n"
- "%lld %d AVE %s: %s:%d %p FPS: %4d, Frame: %5d, Tile: %4dx%4d, MB: %6d, Time: %5d microsec\n"
- "%lld %d AVE %s: %s:%d %p FPS: %4d, Job: %5d, Tile: %4dx%4d, MB: %6d, Time: %5d microsec\n"
- "%lld %d AVE %s: %s:%d %s | external surfaces are wrong %p %d %p %d %p %p %d\n"
- "%lld %d AVE %s: %s:%d %s | fail to create command %p %lld %p %d %p %d\n"
- "%lld %d AVE %s: %s:%d %s | fail to create mutex %p %llu %d\n"
- "%lld %d AVE %s: %s:%d %s | fail to generate id2idx %p %lld %p %d\n"
- "%lld %d AVE %s: %s:%d %s | fail to initial RC %p %llu %p %lld %d %d\n"
- "%lld %d AVE %s: %s:%d %s | fail to initial SVE DPB %p %lld %p %d\n"
- "%lld %d AVE %s: %s:%d %s | fail to initial SVE GOP %p %lld %p %d\n"
- "%lld %d AVE %s: %s:%d %s | fail to initial SVE RC %p %lld %p %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to DART map external surfaces %d %p %d %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to DART map internal surfaces %d %p %d %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to DART unmap external surfaces %d %p %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to DART unmap internal surfaces %d %p %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to calculate surface info %p %d %p %d %p %p %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to configure MD %p %d %p %d %p %p %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create CR %p %lld %p %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create DPB %p %lld %p %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create Mini Device %p %llu\n"
- "%lld %d AVE %s: %s:%d %s | failed to create Mini Device %p %llu | %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create SVE GOP %p %lld %p %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create SVE RC %p %lld %p %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create external surfaces %p %d %p %d %p %p %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create internal surfaces %p %d %p %d %p %p %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create intra block cost %p %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create job %p %d %p %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create the best intra inter block cost %p %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create top line buffer %p %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to handle commands %p %lld %p %d 0x%x 0x%x %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to init GOP decision job %p %lld %p %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to init intra inter cost job %p %lld %p %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to init pipeline %p\n"
- "%lld %d AVE %s: %s:%d %s | failed to initial MD %p %d %p %lld %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to initialize DPB %p %d %p %lld\n"
- "%lld %d AVE %s: %s:%d %s | failed to initialize GOP decision %p %lld %p %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to initialize intra prediction %p %lld %p %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to internal surfaces %p %d %p %d %p %p %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to manage DPB %p %lld %p %d %p %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to manage RC %p %lld %p %d %p %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to set input of intra inter cost %p %lld %p %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to uninitialize GOP decision %p %lld %p %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to uninitialize GOP decision job %p %lld %p %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to uninitialize intra inter cost job %p %lld %p %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to uninitialize intra prediction %p %lld %p %d %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to uninitialize work pool %d %p %d\n"
- "%lld %d AVE %s: %s:%d %s | failed to update output buffer status %p %d | %p %d %p %d\n"
- "%lld %d AVE %s: %s:%d %s | invalid coded header buffer %p %d | %d %d\n"
- "%lld %d AVE %s: %s:%d %s | invalid job parameters size %p %d %p %d %p %d\n"
- "%lld %d AVE %s: %s:%d %s | invalid work type %p %d %d %p %d\n"
- "%lld %d AVE %s: %s:%d %s | mismatch frame number %p %lld %d %d\n"
- "%lld %d AVE %s: %s:%d %s | surface is not correct %p %d %d %d %d %d %d\n"
- "%lld %d AVE %s: %s:%d %s | surface is not enough %p %d %d %d\n"
- "%lld %d AVE %s: %s:%d %s | surface is not enough %p %d %d %d %d\n"
- "%lld %d AVE %s: %s:%d %s | usage mode is not supported %p %lld %p %d %d\n"
- "%lld %d AVE %s: %s:%d %s | wrong parameters %p %lld %p\n"
- "%lld %d AVE %s: %s:%d %s | wrong parameters %p %lld %p %d %p %p\n"
- "%lld %d AVE %s: %s:%d %s | wrong parameters %p %lld %p %d %p %p %p\n"
- "%lld %d AVE %s: %s:%d %s | wrong parameters %p %lld %p %p\n"
- "%lld %d AVE %s: %s:%d %s | wrong parameters %p %llu\n"
- "%lld %d AVE %s: %s:%d %s | wrong parameters %p %p %d %p\n"
- "%lld %d AVE %s: %s:%d %s | wrong parameters %p %p %p %d %p\n"
- "%lld %d AVE %s: %s:%d DLB %d %d %lld | %d %d %lld | %d %d %lld | %d %d %lld\n"
- "%lld %d AVE %s: %s:%d DLB %p %d transition is done\n"
- "%lld %d AVE %s: %s:%d DLB %p %d | %d %d %d | %d %d %d | %d 0x%x %d\n"
- "%lld %d AVE %s: %s:%d DLB %p %d | %d 0x%x %d %d | [ %s ]\n"
- "%lld %d AVE %s: %s:%d DLB Configuration %p %d | %d %d %d %d\n"
- "%lld %d AVE %s: %s:%d Enter\n"
- "%lld %d AVE %s: %s:%d Enter %p \n"
- "%lld %d AVE %s: %s:%d Enter %p %p %p\n"
- "%lld %d AVE %s: %s:%d Exit %d\n"
- "%lld %d AVE %s: %s:%d Exit %p %d\n"
- "%lld %d AVE %s: %s:%d Exit %p %p %p %d\n"
- "%lld %d AVE %s: %s:%d SVEMap %p %d | [ %s ]\n"
- "%lld %d AVE %s: %s:%d SVEMap %p %d | { %s }\n"
- "%lld %d AVE %s: %s:%d SVEStats | %s\n"
- "%lld %d AVE %s: %s:%d Skip the higher layer %p %d %d\n"
- "%lld %d AVE %s: %s:%d TimeOut %d %lld | %lld %d\n"
- "%lld %d AVE %s: %s:%d frame drop in Parallel mode\n"
- "%lld %d AVE %s: %s:%d invalid SVEMap %p %d | [ %s ]\n"
- "%lld %d AVE %s: %s:%d | %p %d %p %d | %p %d %d\n"
- "%lld %d AVE %s: %s:%d | %p %d %p %d | %p %d %d | %d\n"
- "%lld %d AVE %s: %s:%d | %p %d %p %d | %p %d %d | %d %d\n"
- "%lld %d AVE %s: %s:%d | %p %d %p %d | %p %d %p %d %d\n"
- "%lld %d AVE %s: %s:%d | %p %d | %p %d %d\n"
- "%lld %d AVE %s: %s::%s Enter %p %d %d %d %d %d %p %p %p %p\n"
- "%lld %d AVE %s: %s::%s Enter %p %lld | %d\n"
- "%lld %d AVE %s: %s::%s Exit %p %d %d %d %d %d %p %p %p %p %d\n"
- "%lld %d AVE %s: %s::%s Exit %p %d %lld %d %p %p %d\n"
- "%lld %d AVE %s: %s::%s should not happen with single work thread %p %d %p %p %d\n"
- "%lld %d AVE %s: %s::%s:%d %p %d %lld %d %p | %d %d | %d %d %d | %d %d %d | %d %d\n"
- "%lld %d AVE %s: %s::%s:%d %p %d %p %d %d job %d task %p %lld\n"
- "%lld %d AVE %s: %s::%s:%d %p %d Cur %d ToFrm %d | pool %d %d | flush %d | enc %d dis %d | %d %d\n"
- "%lld %d AVE %s: %s::%s:%d %p %d | %p %d %lld %d | %d | %d %s\n"
- "%lld %d AVE %s: %s::%s:%d %p %d<WPCmdResult> %p %p %d %d <Job> %p [%p] intra %d <FrameInfo> %p %d\n"
- "%lld %d AVE %s: %s::%s:%d %p work thread gets job %d %d\n"
- "%lld %d AVE %s: %s::%s:%d %p work thread gets other event! %d\n"
- "%lld %d AVE %s: %s::%s:%d %p work thread terminates %d\n"
- "%lld %d AVE %s: %s::%s:%d %s | failed to DART map PMGR registers %p %d %p %d\n"
- "%lld %d AVE %s: %s::%s:%d %s | failed to create mutex %p %p %d\n"
- "%lld %d AVE %s: %s::%s:%d %s | failed to create new job %p %d %p %lld %p %d %d\n"
- "%lld %d AVE %s: %s::%s:%d %s | failed to create task %p %d %lld %d %p\n"
- "%lld %d AVE %s: %s::%s:%d %s | failed to prepare intrainter cost Job  %p %d %p %d %p %d %lld %d\n"
- "%lld %d AVE %s: %s::%s:%d %s | invalid job %p %d %p\n"
- "%lld %d AVE %s: %s::%s:%d %s | invalid job %p %d %p %d %d\n"
- "%lld %d AVE %s: %s::%s:%d %s | invalid priority %p %d %lld %d %p\n"
- "%lld %d AVE %s: %s::%s:%d %s | job error %p %d %p %d %lld %p %p %d %d\n"
- "%lld %d AVE %s: %s::%s:%d %s | library and driver mismatch %p %d %s <- %s\n"
- "%lld %d AVE %s: %s::%s:%d %s | request job during work pool sleep %p %d %p %d %d\n"
- "%lld %d AVE %s: %s::%s:%d %s | wrong command %p %d 0x%lx %d 0x%x 0x%x\n"
- "%lld %d AVE %s: %s::%s:%d %s | wrong parameters %p %d 0x%llx 0x%llx\n"
- "%lld %d AVE %s: %s::%s:%d %s | wrong parameters %p %lld %p %d %p\n"
- "%lld %d AVE %s: %s::%s:%d %s | wrong paramters %p %d %p\n"
- "%lld %d AVE %s: %s::%s:%d %s | wrong paramters %p %d %p %d\n"
- "%lld %d AVE %s: %s::%s:%d %s | wrong paramters %p %d %p %p\n"
- "%lld %d AVE %s: %s::%s:%d Client info %p %d %s | %d %d %d | %d %d 0x%x | %lld\n"
- "%lld %d AVE %s: %s::%s:%d DLB %p %lld %d | %s\n"
- "%lld %d AVE %s: %s::%s:%d DPB Entry %p %d | %p 0x%x %lld %d %d | %p %p | %d %p %p | %d %p %p\n"
- "%lld %d AVE %s: %s::%s:%d L0 ref entry %p %d | %d %lld %d %d %d | %p %p\n"
- "%lld %d AVE %s: %s::%s:%d L1 ref entry %p %d | %d %lld %d %d %d | %p %p\n"
- "%lld %d AVE %s: %s::%s:%d failed to DART map external surfaces %d %p %d %d %d\n"
- "%lld %d AVE %s: %s::%s:%d failed to DART map internal surfaces %d %p %d %d %d\n"
- "%lld %d AVE %s: %s::%s:%d failed to clear job in priority %p %d %d %d\n"
- "%lld %d AVE %s: %s::%s:%d failed to clear job in task %p %d %p %lld %d\n"
- "%lld %d AVE %s: %s::%s:%d failed to notify job %p %d %p %d %d\n"
- "%lld %d AVE %s: %s::%s:%d failed to process output job in priority %p %d %d %d\n"
- "%lld %d AVE %s: %s::%s:%d failed to process output job in task %p %d %p %lld %d\n"
- "%lld %d AVE %s: %s::%s:%d job not in proc %p %d %p %d %lld %p %p %d\n"
- "%lld %d AVE %s: %s::%s:%d process job %p %d %p %d %lld %p %p %d\n"
- "%lld %d AVE %s: %s::%s:%d receive command done %p %d 0x%x 0x%llx\n"
- "%lld %d AVE %s: %s::%s:%d selected SVE %p %lld | %d %d %d %d %lld\n"
- "%lld %d AVE %s: %s::%s:%d timeout %p %d %d %d %d\n"
- "%lld %d AVE %s: %s::%s:%d wait %p %d\n"
- "%lld %d AVE %s: %s::%s:%d wait %p %d %d %p %d %d\n"
- "%lld %d AVE %s: %s::%s:%d wait %p %d %p %d\n"
- "%lld %d AVE %s: %s::%s:%d wait %p %d %p %d %d\n"
- "%lld %d AVE %s: %s::%s:%d wait %p %d %p %d %d %d %llu\n"
- "%lld %d AVE %s: %s::%s:%d wait with timeout %p %d %d %p %d %d %d %llu\n"
- "%lld %d AVE %s: %s::%s:%d wait_timeout %p %d %p %d\n"
- "%lld %d AVE %s: %s::%s:%d wait_timeout done %p %d %p %d\n"
- "%lld %d AVE %s: Analytics: %s(%d) %s(%d%%) %s(%d%%) %s(%d%%) %s(%d%%) %s(%d%%)\n"
- "%lld %d AVE %s: DLB Info %s | %p | %d - %d 0x%x %d %d || %s\n"
- "%lld %d AVE %s: Dynamic Load Balancing: %d %d %s\n"
- "%lld %d AVE %s: Dynamic Power Management: 0x%x\n"
- "%lld %d AVE %s: Mini-Device%s: %p ID: %lld %d %d | SVEMap: %s\n"
- "%lld %d AVE %s: SVESched %s | %p %d | %d | %d %d %d %lld %d %d\n"
- "%lld %d AVE %s: Surface info: \n"
- "%lld %d AVE %s: bMinimizeMemoryUsage %d iOutputBufSizeFactor %d bThroughputRateModeSet %d bPrioritizeEncodingSpeedOverQuality %d\n"
- "%lld %d AVE %s: bVariableBFrames %d BFramesMVaveThreshold XY %d %d BFramesIntraMBThreshold PB %d %d Extra PB %d %d\n"
- "%lld %d AVE %s: debl %d - Quality (%d) - QP (I %d P %d B %d) - iMaxKeyFrameInterval %d\n"
- "%lld %d AVE %s: throughputRateMode %d bChangeBitrateAtNextIDR %d\n"
- "%s - debl %d - Quality (%d) - QP (I %d P %d B %d) - iMaxKeyFrameInterval %d\n"
- "%s-%d-%d"
- "(iPriority >= -100) && (iPriority <= 200)"
- "(paramsSize >= 0) && (paramsSize <= sizeof(psJob->iaParams))"
- "(workType > AVE_WorkType_Sw) && (workType < AVE_WorkType_Max)"
- "- %d %d %d "
- "11212112222222222222222"
- "1122222222111111"
- "12111111111112222112222211111111111111111111111121222221122222222222222222222222222222222222211111111"
- "1211111212221212111111111111121111111111111"
- "121222222222222222222222222"
- "122222111"
- "122222222221111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
- "20:41:07"
- "211222222222222222222222222222222222222222"
- "222111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111112222122222222222222222222222222222222221111111111222222222222222222222211222212222222222222222222222222222222222111111111122222222222222222222221122221222222222222222222222222222222222211111111112222222222222222222222112222122222222222222222222222222222222221111111111222222222222222222222211222212222222222222222222222222222222222111111111122222222222222222222221122221222222222222222222222222222222222211111111112222222222222222222222112222122222222222222222222222222222222221111111111222222222222222222222211222212222222222222222222222222222222222111111111122222222222222222222221122221222222222222222222222222222222222211111111112222222222222222222222112222122222222222222222222222222222222221111111111222222222222222222222211222212222222222222222222222222222222222111111111122222222222222222222221122221222222222222222222222222222222222211111111112222222222222222222222112222122222222222222222222222222222222221111111111222222222222222222222211222212222222222222222222222222222222222111111111122222222222222222222221122221222222222222222222222222222222222211111111112222222222222222222222112222122222222222222222222222222222222221111111111222222222222222222222211222212222222222222222222222222222222222111111111122222222222222222222221122221222222222222222222222222222222222211111111112222222222222222222222112222122222222222222222222222222222222221111111111222222222222222222222211222212222222222222222222222222222222222111111111122222222222222222222221122221222222222222222222222222222222222211111111112222222222222222222222112222122222222222222222222222222222222221111111111222222222222222222222211222212222222222222222222222222222222222111111111122222222222222222222221122221222222222222222222222222222222222211111111112222222222222222222222112222122222222222222222222222222222222221111111111222222222222222222222211"
- "802.37.1"
- "AVE_ClientList_CalcDLBStats"
- "AVE_Client_AcquireOutputBuf"
- "AVE_Client_AssignHwC"
- "AVE_Client_CalcDPMThreshold"
- "AVE_Client_CheckExternalSurface"
- "AVE_Client_CheckOutputBuf_Quota"
- "AVE_Client_ReleaseOutputBuf"
- "AVE_Client_Update"
- "AVE_Client_UpdateFrameInfoFromOutputData"
- "AVE_Client_UpdateOutputBuf_Status"
- "AVE_DLB_Alloc"
- "AVE_DLB_AllocSVENum"
- "AVE_DLB_Apply"
- "AVE_DLB_Assign"
- "AVE_DLB_Select"
- "AVE_Job_Create"
- "AVE_Job_GOPDecision"
- "AVE_Job_GOPDecision_Init"
- "AVE_Job_GOPDecision_Uninit"
- "AVE_Job_IntraInterCost"
- "AVE_Job_IntraInterCost_Init"
- "AVE_Job_IntraInterCost_SetInput"
- "AVE_Job_IntraInterCost_Uninit"
- "AVE_WorkPool.cpp"
- "AVE_WorkThread.cpp"
- "ActionJobDone"
- "ActionNewCmd"
- "ActionSleep"
- "Analytics: %s(%d) %s(%d%%) %s(%d%%) %s(%d%%) %s(%d%%) %s(%d%%)\n"
- "ClearAllJob"
- "ClearJobInPriority"
- "ClearJobInTask"
- "DLB Info %s | %p | %d - %d 0x%x %d %d || %s\n"
- "Dynamic Load Balancing: %d %d %s\n"
- "Dynamic Power Management: 0x%x\n"
- "ID: %d %s | SVE: "
- "Jun 20 2024"
- "Mini-Device%s: %p ID: %lld %d %d | SVEMap: %s\n"
- "MoveJob"
- "NotifyJob"
- "PrepareJob"
- "ProcessAllNewCmd"
- "ProcessAllOutputJob"
- "ProcessInput"
- "ProcessInputJob"
- "ProcessInputJobInPriority"
- "ProcessInputJobInTask"
- "ProcessInputJobWhenIdle"
- "ProcessJob"
- "ProcessOutputJobInPriority"
- "ProcessOutputJobInTask"
- "RequestJob"
- "SVESched %s | %p %d | %d | %d %d %d %lld %d %d\n"
- "SkipJob"
- "Surface info: \n"
- "UpdateFrameInfoFromOutputData"
- "WorkPool"
- "WorkThread"
- "bMinimizeMemoryUsage %d iOutputBufSizeFactor %d bThroughputRateModeSet %d bPrioritizeEncodingSpeedOverQuality %d\n"
- "bVariableBFrames %d BFramesMVaveThreshold XY %d %d BFramesIntraMBThreshold PB %d %d Extra PB %d %d\n"
- "bestIntraInterBlkCost != nullptr"
- "debl %d - Quality (%d) - QP (I %d P %d B %d) - iMaxKeyFrameInterval %d\n"
- "eMode < HEVC_THROUGHPUT_RATE_MODE_NUM"
- "iSVENum > 0 && iSVENum <= 4 && eGOPMode > AVE_GOPMode_None && eGOPMode < AVE_GOPMode_Max && piaSVEID2IDX != nullptr && iArrSize <= sizeof(m_iaSVEID2IDX)/sizeof(*m_iaSVEID2IDX)"
- "intraBlkCost != nullptr"
- "linebufT != nullptr"
- "m_sSVEMap.iMode == 0"
- "m_saNonRefBuf[i].psBuf != nullptr && m_saNonRefBuf[i].psLowResBuf != nullptr"
- "num == 0 || num >= pClient->sSurfaceInfoSet.iaRecon[AVE_SIIdx_Set]"
- "pCfg != nullptr && id < 8 && pPMGR != nullptr"
- "pClient != nullptr && pMap != nullptr"
- "pFrameInfo != nullptr && pCodedHeader != nullptr"
- "pSVESched != nullptr && psSVEMap != nullptr"
- "pSVESched->iActiveSVENum == psSVEMap->iNum"
- "pSet->pcaRecon[i][j][k]->GetSize() >= pClient->sSurfaceInfoSet.iaRecon[AVE_SIIdx_Size]"
- "psJob != nullptr"
- "psJob->pMutex != nullptr"
- "site.S_AVE_Job"
- "storeLRMEFSCost"
- "tmpLayer == 0 || tmpLayer >= pClient->sSurfaceInfoSet.iaRecon[AVE_SIIdx_Layer]"
- "tmpNum == 0 || tmpNum >= pClient->sSurfaceInfoSet.iaRecon[AVE_SIIdx_Num]"

```

>  `com.apple.driver.AppleBCMWLANCore`

```diff

-1253.56.0.0.0
+1253.58.0.0.0
   __TEXT.__const: 0x224c
-  __TEXT.__cstring: 0x6a142
+  __TEXT.__cstring: 0x6a3ca
   __TEXT.__os_log: 0x761e
-  __TEXT_EXEC.__text: 0x229250
+  __TEXT_EXEC.__text: 0x229e0c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x492
   __DATA.__common: 0x470

   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__mod_init_func: 0x1f8
   __DATA_CONST.__mod_term_func: 0x1e8
-  __DATA_CONST.__const: 0x1e320
+  __DATA_CONST.__const: 0x1e368
   __DATA_CONST.__kalloc_type: 0x42c0
   __DATA_CONST.__kalloc_var: 0x230
-  Functions: 4575
-  Symbols:   8445
-  CStrings:  10963
+  Functions: 4579
+  Symbols:   8452
+  CStrings:  10977
 
Symbols:
+ .str.1160
+ .str.1562
+ .str.1655
+ .str.1656
+ .str.1989
+ .str.2130
+ .str.2131
+ .str.2741
+ .str.2742
+ .str.2743
+ .str.2812
+ .str.3128
+ .str.3141
+ .str.3142
+ .str.3143
+ .str.3213
+ .str.3224
+ .str.3246
+ .str.3309
+ .str.3324
+ .str.3368
+ .str.3393
+ .str.3394
+ .str.3428
+ .str.3429
+ .str.3430
+ .str.3431
+ .str.3432
+ .str.3433
+ .str.3434
+ .str.3435
+ .str.3436
+ .str.3474
+ .str.668
+ .str.790
+ .str.791
+ .str.803
+ .str.804
+ _MergedGlobals.688
+ __FUNCTION__._ZN16AppleBCMWLANCore21disableHtSisoOnlySafeEv
+ __ZN16AppleBCMWLANCore19setMANUFACTURE_DATEEP27apple80211_manufacture_date
+ __ZN16AppleBCMWLANCore21disableHtSisoOnlySafeEv
+ __ZN16AppleBCMWLANCore26setFIRST_BOOT_COUNTRY_CODEEP28apple80211_country_code_data
+ __ZN25AppleBCMWLANInfraProtocol19setMANUFACTURE_DATEEP27apple80211_manufacture_date
+ __ZN25AppleBCMWLANInfraProtocol26setFIRST_BOOT_COUNTRY_CODEEP28apple80211_country_code_data
+ __ZNK16IO80211BSSBeacon12getTimestampEv
+ __ZZN16AppleBCMWLANCore10setHeStatsEP6OSData19AppleBCMWLANSliceIdE22kalloc_type_view_16492
+ __ZZN16AppleBCMWLANCore11setOmiStatsEP6OSData19AppleBCMWLANSliceIdE22kalloc_type_view_16655
+ __ZZN16AppleBCMWLANCore13freeResourcesEvE21kalloc_type_view_3973
+ __ZZN16AppleBCMWLANCore15setCurEtheraddrERK10ether_addrE22kalloc_type_view_25382
+ __ZZN16AppleBCMWLANCore15setCurEtheraddrERK10ether_addrE22kalloc_type_view_25398
+ __ZZN16AppleBCMWLANCore17configureLPASModeEjE22kalloc_type_view_50846
+ __ZZN16AppleBCMWLANCore17configureLPASModeEjE22kalloc_type_view_50857
+ __ZZN16AppleBCMWLANCore17handleDynSAREventEP14wl_event_msg_tE22kalloc_type_view_23525
+ __ZZN16AppleBCMWLANCore17handleDynSAREventEP14wl_event_msg_tE22kalloc_type_view_23577
+ __ZZN16AppleBCMWLANCore18configPerPeerStatsEbhhP10ether_addrE22kalloc_type_view_29793
+ __ZZN16AppleBCMWLANCore18configPerPeerStatsEbhhP10ether_addrE22kalloc_type_view_29803
+ __ZZN16AppleBCMWLANCore20parseEventLogRecordsEP6OSDataPjE22kalloc_type_view_21556
+ __ZZN16AppleBCMWLANCore20parseEventLogRecordsEP6OSDataPjE22kalloc_type_view_21635
+ __ZZN16AppleBCMWLANCore20parseEventLogRecordsEP6OSDataPjE22kalloc_type_view_21660
+ __ZZN16AppleBCMWLANCore26handleSetLpasAsyncCallBackER9CommandIDiR16CommandRxPayloadPvE22kalloc_type_view_12541
+ __ZZN16AppleBCMWLANCore26setMacAddressAsyncCallbackER9CommandIDiR16CommandRxPayloadPvE21kalloc_type_view_9312
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV2EP6OSDataE22kalloc_type_view_16733
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV2EP6OSDataE22kalloc_type_view_16819
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV3EP6OSDataE22kalloc_type_view_16847
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV3EP6OSDataE22kalloc_type_view_16933
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV4EP6OSDataE22kalloc_type_view_16958
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV4EP6OSDataE22kalloc_type_view_17011
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV6EP6OSDataE22kalloc_type_view_17040
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV6EP6OSDataE22kalloc_type_view_17141
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV7EP6OSDataE22kalloc_type_view_17170
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV7EP6OSDataE22kalloc_type_view_17281
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV9EP6OSDataE22kalloc_type_view_17984
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV9EP6OSDataE22kalloc_type_view_18106
+ __ZZN16AppleBCMWLANCore33parseEventLogRecordBTCoexStatsV11EP6OSDataE22kalloc_type_view_17311
+ __ZZN16AppleBCMWLANCore33parseEventLogRecordBTCoexStatsV11EP6OSDataE22kalloc_type_view_17471
+ __ZZN16AppleBCMWLANCore33parseEventLogRecordBTCoexStatsV12EP6OSDataE22kalloc_type_view_17505
+ __ZZN16AppleBCMWLANCore33parseEventLogRecordBTCoexStatsV12EP6OSDataE22kalloc_type_view_17742
+ __ZZN16AppleBCMWLANCore34handlePeerStatsConfigAsyncCallbackER9CommandIDiR16CommandRxPayloadPvE22kalloc_type_view_29650
+ __ZZN16AppleBCMWLANCore36convertwlMgmtCntToAppleFrameCountersEP16wl_ctl_mgt_cnt_tP25apple80211_frame_countersE22kalloc_type_view_28832
+ __ZZN16AppleBCMWLANCore36convertwlMgmtCntToAppleFrameCountersEP16wl_ctl_mgt_cnt_tP25apple80211_frame_countersE22kalloc_type_view_28886
+ __ZZN16AppleBCMWLANCore47parseEventLogRecordControlManagementFrameCountsEP6OSDataE22kalloc_type_view_21051
+ __ZZN16AppleBCMWLANCore47parseEventLogRecordControlManagementFrameCountsEP6OSDataE22kalloc_type_view_21086
+ __ZZN16AppleBCMWLANCore4freeEvE21kalloc_type_view_1746
+ __ZZN16AppleBCMWLANCore4initEP12OSDictionaryE21kalloc_type_view_1349
+ __ZZN16AppleBCMWLANCore5startEP9IOServiceE21kalloc_type_view_2450
+ __ZZN21AppleBCMWLANCommander14initWithConfigEP16AppleBCMWLANCoreP24AppleBCMWLANBusInterfacejE20kalloc_type_view_605
+ __ZZN21AppleBCMWLANCommander4freeEvE21kalloc_type_view_1369
+ __ZZN25AppleBCMWLANConfigManager4freeEvE20kalloc_type_view_583
+ __ZZN25AppleBCMWLANConfigManager4initEP16AppleBCMWLANCoreE20kalloc_type_view_370
+ __ZZN30AppleBCMWLANCoreFirmwareLoader16initWithProviderEP9IOServiceE22kalloc_type_view_60676
+ __ZZN30AppleBCMWLANCoreFirmwareLoader4freeEvE22kalloc_type_view_60764
+ __ZZN33AppleBCMWLANIO80211APSTAInterface24configureSoftAPPeerStatsEbE21kalloc_type_view_5472
+ __ZZN33AppleBCMWLANIO80211APSTAInterface24configureSoftAPPeerStatsEbE21kalloc_type_view_5482
+ __ZZN33AppleBCMWLANIO80211APSTAInterface36handleSoftAPStatsConfigAsyncCallbackER9CommandIDiR16CommandRxPayloadPvE21kalloc_type_view_5518
+ __ZZN33AppleBCMWLANIO80211APSTAInterface4freeEvE20kalloc_type_view_716
+ __ZZN33AppleBCMWLANIO80211APSTAInterface4initEP16AppleBCMWLANCoreP10ether_addrjPcE20kalloc_type_view_224
+ __ZZN33AppleBCMWLANIO80211APSTAInterface4initEvE20kalloc_type_view_206
+ __block_descriptor_tmp.1761
+ __block_descriptor_tmp.2012
+ __block_descriptor_tmp.2372
+ __block_descriptor_tmp.2406
+ __block_descriptor_tmp.2777
+ __block_descriptor_tmp.3319
+ __block_descriptor_tmp.743
+ __block_descriptor_tmp.891
+ __block_literal_global.2374
+ __block_literal_global.2408
- .str.1153
- .str.1555
- .str.1648
- .str.1649
- .str.1982
- .str.2123
- .str.2124
- .str.2732
- .str.2733
- .str.2734
- .str.2803
- .str.3119
- .str.3132
- .str.3133
- .str.3134
- .str.3204
- .str.3215
- .str.3237
- .str.3300
- .str.3315
- .str.3359
- .str.3375
- .str.3385
- .str.3417
- .str.3418
- .str.3419
- .str.3420
- .str.3421
- .str.3422
- .str.3423
- .str.3424
- .str.3425
- .str.665
- .str.783
- .str.784
- .str.796
- .str.797
- _MergedGlobals.690
- __ZN25AppleBCMWLANConfigManager11isNewDeviceEv
- __ZZN16AppleBCMWLANCore10setHeStatsEP6OSData19AppleBCMWLANSliceIdE22kalloc_type_view_16454
- __ZZN16AppleBCMWLANCore11setOmiStatsEP6OSData19AppleBCMWLANSliceIdE22kalloc_type_view_16617
- __ZZN16AppleBCMWLANCore13freeResourcesEvE21kalloc_type_view_3953
- __ZZN16AppleBCMWLANCore15setCurEtheraddrERK10ether_addrE22kalloc_type_view_25344
- __ZZN16AppleBCMWLANCore15setCurEtheraddrERK10ether_addrE22kalloc_type_view_25360
- __ZZN16AppleBCMWLANCore17configureLPASModeEjE22kalloc_type_view_50759
- __ZZN16AppleBCMWLANCore17configureLPASModeEjE22kalloc_type_view_50770
- __ZZN16AppleBCMWLANCore17handleDynSAREventEP14wl_event_msg_tE22kalloc_type_view_23487
- __ZZN16AppleBCMWLANCore17handleDynSAREventEP14wl_event_msg_tE22kalloc_type_view_23539
- __ZZN16AppleBCMWLANCore18configPerPeerStatsEbhhP10ether_addrE22kalloc_type_view_29753
- __ZZN16AppleBCMWLANCore18configPerPeerStatsEbhhP10ether_addrE22kalloc_type_view_29763
- __ZZN16AppleBCMWLANCore20parseEventLogRecordsEP6OSDataPjE22kalloc_type_view_21518
- __ZZN16AppleBCMWLANCore20parseEventLogRecordsEP6OSDataPjE22kalloc_type_view_21584
- __ZZN16AppleBCMWLANCore20parseEventLogRecordsEP6OSDataPjE22kalloc_type_view_21597
- __ZZN16AppleBCMWLANCore26handleSetLpasAsyncCallBackER9CommandIDiR16CommandRxPayloadPvE22kalloc_type_view_12503
- __ZZN16AppleBCMWLANCore26setMacAddressAsyncCallbackER9CommandIDiR16CommandRxPayloadPvE21kalloc_type_view_9274
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV2EP6OSDataE22kalloc_type_view_16695
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV2EP6OSDataE22kalloc_type_view_16781
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV3EP6OSDataE22kalloc_type_view_16809
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV3EP6OSDataE22kalloc_type_view_16895
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV4EP6OSDataE22kalloc_type_view_16920
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV4EP6OSDataE22kalloc_type_view_16973
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV6EP6OSDataE22kalloc_type_view_17002
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV6EP6OSDataE22kalloc_type_view_17103
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV7EP6OSDataE22kalloc_type_view_17132
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV7EP6OSDataE22kalloc_type_view_17243
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV9EP6OSDataE22kalloc_type_view_17946
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV9EP6OSDataE22kalloc_type_view_18068
- __ZZN16AppleBCMWLANCore33parseEventLogRecordBTCoexStatsV11EP6OSDataE22kalloc_type_view_17273
- __ZZN16AppleBCMWLANCore33parseEventLogRecordBTCoexStatsV11EP6OSDataE22kalloc_type_view_17433
- __ZZN16AppleBCMWLANCore33parseEventLogRecordBTCoexStatsV12EP6OSDataE22kalloc_type_view_17467
- __ZZN16AppleBCMWLANCore33parseEventLogRecordBTCoexStatsV12EP6OSDataE22kalloc_type_view_17704
- __ZZN16AppleBCMWLANCore34handlePeerStatsConfigAsyncCallbackER9CommandIDiR16CommandRxPayloadPvE22kalloc_type_view_29610
- __ZZN16AppleBCMWLANCore36convertwlMgmtCntToAppleFrameCountersEP16wl_ctl_mgt_cnt_tP25apple80211_frame_countersE22kalloc_type_view_28792
- __ZZN16AppleBCMWLANCore36convertwlMgmtCntToAppleFrameCountersEP16wl_ctl_mgt_cnt_tP25apple80211_frame_countersE22kalloc_type_view_28846
- __ZZN16AppleBCMWLANCore47parseEventLogRecordControlManagementFrameCountsEP6OSDataE22kalloc_type_view_21013
- __ZZN16AppleBCMWLANCore47parseEventLogRecordControlManagementFrameCountsEP6OSDataE22kalloc_type_view_21048
- __ZZN16AppleBCMWLANCore4freeEvE21kalloc_type_view_1726
- __ZZN16AppleBCMWLANCore4initEP12OSDictionaryE21kalloc_type_view_1345
- __ZZN16AppleBCMWLANCore5startEP9IOServiceE21kalloc_type_view_2430
- __ZZN21AppleBCMWLANCommander14initWithConfigEP16AppleBCMWLANCoreP24AppleBCMWLANBusInterfacejE20kalloc_type_view_603
- __ZZN21AppleBCMWLANCommander4freeEvE21kalloc_type_view_1367
- __ZZN25AppleBCMWLANConfigManager4freeEvE20kalloc_type_view_585
- __ZZN25AppleBCMWLANConfigManager4initEP16AppleBCMWLANCoreE20kalloc_type_view_372
- __ZZN30AppleBCMWLANCoreFirmwareLoader16initWithProviderEP9IOServiceE22kalloc_type_view_60582
- __ZZN30AppleBCMWLANCoreFirmwareLoader4freeEvE22kalloc_type_view_60670
- __ZZN33AppleBCMWLANIO80211APSTAInterface24configureSoftAPPeerStatsEbE21kalloc_type_view_5471
- __ZZN33AppleBCMWLANIO80211APSTAInterface24configureSoftAPPeerStatsEbE21kalloc_type_view_5481
- __ZZN33AppleBCMWLANIO80211APSTAInterface36handleSoftAPStatsConfigAsyncCallbackER9CommandIDiR16CommandRxPayloadPvE21kalloc_type_view_5515
- __ZZN33AppleBCMWLANIO80211APSTAInterface4freeEvE20kalloc_type_view_715
- __ZZN33AppleBCMWLANIO80211APSTAInterface4initEP16AppleBCMWLANCoreP10ether_addrjPcE20kalloc_type_view_223
- __ZZN33AppleBCMWLANIO80211APSTAInterface4initEvE20kalloc_type_view_205
- __block_descriptor_tmp.1754
- __block_descriptor_tmp.2005
- __block_descriptor_tmp.2365
- __block_descriptor_tmp.2399
- __block_descriptor_tmp.2768
- __block_descriptor_tmp.3310
- __block_descriptor_tmp.736
- __block_descriptor_tmp.884
- __block_literal_global.2367
- __block_literal_global.2401
CStrings:
+ "\"AppleBCMWLANV3_Drivers-1253.58\""
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.0.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/IOKit/apple80211/IO80211Util.h"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANBSSBeacon.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANBssManager.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCommandMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCommander.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCore.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCoreDbg.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANIOReportingPerSlice.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANJoinAdapter.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANNANInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANPowerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANProximityInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANScanAdapter.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANTimeSyncEngine.cpp"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANTxPowerManager.cpp"
+ "11112222222222222222222212222222212222222212"
+ "222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221212222222222222222222222121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212122222222211122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111111111111111111112222222222222222222222222222222222222222222222222222222222222222222222222222111111111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211121111111111111111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222222222212222222222222222222222222222222222222222222222222222222221112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111122122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222121122222222222222222222222222222222222222222221211122221222222222222222222222222222222222222222222222222111222222222222"
+ "AppleBCMWLANV3_Drivers-1253.58"
+ "Jul  3 2024 20:03:25"
+ "[ik] %s@%d: WiFiCC : fw query for chanspecs SUCCEEDED during init : %s\n"
+ "[ik] %s@%d:Not a german device but Siso enable, lets disable it cc<%c %c> siso=<%d> isAssociated=<%d>\n"
+ "[ik] %s@%d:Old device=<%d>  date<%d/%d/%d> limit<%d/%d/%d> siso=<%d> isAssociated=<%d>\n"
+ "[ik] %s@%d:WiFiCC : Current host country code [%s] setup to FW is complete.\n"
+ "[ik] %s@%d:WiFiCC : Initializing FW with country code [%s]. Probably a chip reset recovery\n"
+ "[ik] %s@%d:WiFiCC : host country code not present. Defaulting fHostCountryEnabled to false\n"
+ "[ik] %s@%d:WiFiCC : setup default countrycode to FW complete. rv : [%s] \n"
+ "[ik] %s@%d:disable HT Siso \n"
+ "[ik] %s@%d:isAllowHtSiso false \n"
+ "bluetooth-pcie"
+ "disableHtSisoOnlySafe"
+ "setFIRST_BOOT_COUNTRY_CODE"
+ "setMANUFACTURE_DATE"
+ "wlan.isAllowHtSiso"
+ "wlan.mf.day"
+ "wlan.mf.month"
+ "wlan.mf.year"
- "\"AppleBCMWLANV3_Drivers-1253.56\""
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.0.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/IOKit/apple80211/IO80211Util.h"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANBSSBeacon.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANBssManager.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCommandMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCommander.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCore.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCoreDbg.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANIOReportingPerSlice.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANJoinAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANNANInterface.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANPowerManager.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANProximityInterface.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANScanAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANTimeSyncEngine.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANTxPowerManager.cpp"
- "111122222222222222222222122222222122222222122"
- "22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222121222222222222222222222212122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221212222222221112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111111111111111111111111222222222222222222222222222222222222222222222222222222222222222222222222222211111111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221112111111111111111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222122222222221222222222222222222222222222222222222222222222222222222222111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211112212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212112222222222222222222222222222222222222222222121112222122222222222222222222222222222222222222222222222211122222222222"
- "AppleBCMWLANV3_Drivers-1253.56"
- "Jun 20 2024 20:31:01"
- "[ik] %s@%d: fw query for chanspecs SUCCEEDED during init : %s\n"
- "[ik] %s@%d: fw query for chanspecs failed after watchdog complete\n "
- "wlan.debug.isNewDevice"

```

>  `com.apple.driver.AppleBiometricSensor`

```diff

-259.0.0.0.0
-  __TEXT.__cstring: 0x283a
-  __TEXT.__os_log: 0x80ff
+259.0.1.0.0
+  __TEXT.__cstring: 0x28bf
+  __TEXT.__os_log: 0x8307
   __TEXT.__const: 0x360
-  __TEXT_EXEC.__text: 0x1ff00
+  __TEXT_EXEC.__text: 0x20150
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x1c8

   __DATA_CONST.__const: 0x5f90
   __DATA_CONST.__kalloc_type: 0x3c0
   Functions: 422
-  Symbols:   1860
-  CStrings:  411
+  Symbols:   1868
+  CStrings:  413
 
Symbols:
+ __ZN15AppleSandDollar17enableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEb
+ __ZN15AppleSandDollar18disableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEb
+ __ZN9AppleMesa12enableSensorEN20AppleBiometricSensor23eSensorPowerControlTypeEb
+ __ZN9AppleMesa13disableSensorEN20AppleBiometricSensor23eSensorPowerControlTypeEb
+ __ZN9AppleMesa17enableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEb
+ __ZN9AppleMesa17enableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEb_vfpthunk_
+ __ZN9AppleMesa18disableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEb
+ __ZN9AppleMesa18disableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEb_vfpthunk_
+ __ZZN15AppleSandDollar17enableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEbE11_os_log_fmt
+ __ZZN15AppleSandDollar17enableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEbE11_os_log_fmt_0
+ __ZZN15AppleSandDollar18disableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEbE11_os_log_fmt
+ __ZZN15AppleSandDollar18disableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEbE11_os_log_fmt_0
+ __ZZN15AppleSandDollar18disableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEbE11_os_log_fmt_1
+ __ZZN15AppleSandDollar18disableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEbE11_os_log_fmt_2
+ __ZZN9AppleMesa13SetPowerGatedEjE11_os_log_fmt__15_
+ __ZZN9AppleMesa13handleCMDSyncEjmmmE11_os_log_fmt__10_
+ __ZZN9AppleMesa15setCurrentStateEjE11_os_log_fmt_1
+ __ZZN9AppleMesa17ESDRecoveryActionEP13IOEventSourceE11_os_log_fmt__13_
+ __ZZN9AppleMesa17enableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEbE11_os_log_fmt
+ __ZZN9AppleMesa17enableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEbE11_os_log_fmt_0
+ __ZZN9AppleMesa17enableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEbE11_os_log_fmt_1
+ __ZZN9AppleMesa17enableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEbE11_os_log_fmt_2
+ __ZZN9AppleMesa17enableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEbE11_os_log_fmt_3
+ __ZZN9AppleMesa17enableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEbE11_os_log_fmt_4
+ __ZZN9AppleMesa18disableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEbE11_os_log_fmt
+ __ZZN9AppleMesa18disableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEbE11_os_log_fmt_0
+ __ZZN9AppleMesa18disableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEbE11_os_log_fmt_1
+ __ZZN9AppleMesa18disableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEbE11_os_log_fmt_2
+ __ZZN9AppleMesa18disableSensorGatedEN20AppleBiometricSensor23eSensorPowerControlTypeEbE11_os_log_fmt_3
+ __ZZN9AppleMesa20dispatchCaptureReadyEP18IOMemoryDescriptoryyE21kalloc_type_view_6827
+ __ZZN9AppleMesa20dispatchCaptureReadyEP18IOMemoryDescriptoryyE21kalloc_type_view_6843
- __ZN15AppleSandDollar18disableSensorGatedEv
- __ZN15AppleSandDollar18setPropertiesGatedEP8OSObject
- __ZN9AppleMesa12enableSensorEv
- __ZN9AppleMesa13disableSensorEv
- __ZN9AppleMesa17enableSensorGatedEv
- __ZN9AppleMesa17enableSensorGatedEv_vfpthunk_
- __ZN9AppleMesa18disableSensorGatedEv
- __ZN9AppleMesa18disableSensorGatedEv_vfpthunk_
- __ZZN15AppleSandDollar18disableSensorGatedEvE11_os_log_fmt
- __ZZN15AppleSandDollar18disableSensorGatedEvE11_os_log_fmt_0
- __ZZN15AppleSandDollar18disableSensorGatedEvE11_os_log_fmt_1
- __ZZN15AppleSandDollar18setPropertiesGatedEP8OSObjectE11_os_log_fmt
- __ZZN9AppleMesa17enableSensorGatedEvE11_os_log_fmt
- __ZZN9AppleMesa17enableSensorGatedEvE11_os_log_fmt_0
- __ZZN9AppleMesa17enableSensorGatedEvE11_os_log_fmt_1
- __ZZN9AppleMesa17enableSensorGatedEvE11_os_log_fmt_2
- __ZZN9AppleMesa17enableSensorGatedEvE11_os_log_fmt_3
- __ZZN9AppleMesa18disableSensorGatedEvE11_os_log_fmt
- __ZZN9AppleMesa18disableSensorGatedEvE11_os_log_fmt_0
- __ZZN9AppleMesa18disableSensorGatedEvE11_os_log_fmt_1
- __ZZN9AppleMesa18disableSensorGatedEvE11_os_log_fmt_2
- __ZZN9AppleMesa20dispatchCaptureReadyEP18IOMemoryDescriptoryyE21kalloc_type_view_6786
- __ZZN9AppleMesa20dispatchCaptureReadyEP18IOMemoryDescriptoryyE21kalloc_type_view_6802
CStrings:
+ "!powerState || _currentState != kDeviceDisabled"
+ "(_currentState != kDeviceDisabled)"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBiometricSensor/ABSLogging.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBiometricSensor/AppleMesa.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBiometricSensor/AppleMesaResources.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBiometricSensor/AppleSPIBiometricSensor.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleBiometricSensor/AppleSandDollar.cpp"
+ "_currentState != kDeviceDisabled || _setSensorPowerUserOverride"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBiometricSensor/ABSLogging.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBiometricSensor/AppleMesa.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBiometricSensor/AppleMesaResources.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBiometricSensor/AppleSPIBiometricSensor.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleBiometricSensor/AppleSandDollar.cpp"
- "wakeOnMenuPin"

```

>  `com.apple.driver.AppleM2ScalerCSCDriver`

```diff

-148.0.45.0.0
-  __TEXT.__cstring: 0x17d57
-  __TEXT.__const: 0x4f518
-  __TEXT_EXEC.__text: 0xe0b5c
+148.0.46.0.0
+  __TEXT.__cstring: 0x17d09
+  __TEXT.__const: 0x4ec98
+  __TEXT_EXEC.__text: 0xe084c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1fe40
   __DATA.__common: 0x20a8

   __DATA_CONST.__auth_ptr: 0x88
   __DATA_CONST.__mod_init_func: 0x570
   __DATA_CONST.__mod_term_func: 0x548
-  __DATA_CONST.__const: 0x31080
+  __DATA_CONST.__const: 0x31038
   __DATA_CONST.__kalloc_type: 0x3c40
   __DATA_CONST.__kalloc_var: 0x500
-  Functions: 6009
+  Functions: 6008
   Symbols:   9228
-  CStrings:  2386
+  CStrings:  2384
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AXI2AFControl/IosaAxi2AfControl.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriver.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriverFilters.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHal.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR10j.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR11.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR15.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR16.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR2.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR21.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR22.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR4.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR6.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR7.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR9.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR16.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR17.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR21.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR22.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DisplayScalerFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DriverCommonFunctions.h"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23Dv.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23Rtk.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR25RTK.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FrameDescriptorRing.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FrameDescriptorRingMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IOAsynchronousScheduler.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IOSurfaceAcceleratorClient.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IOSurfaceAcceleratorPreparator.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR15.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR18.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR4.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaFilmGrainControlMSR16.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaFilmGrainControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPowerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControl.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR18.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaTiledCompressedMemMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaWdmaControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/K2KTests.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControl.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR4.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControl.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR20.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControl.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR6.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControl.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR10.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR22.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR4.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR8.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MSR23ChromaDownsampleFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MSR23DefaultFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MailBox.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MailBoxMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/ModularDefaultFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStream.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStreamMSR15.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStreamMSR19.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrBlockDescriptorRegisterStream.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrBlockDescriptorRegisterStreamMSR23.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrRegisterStream.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/Request.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/RingBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/Shared/Utility/IOFBSAGammaLUT.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/SpillBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/StatusDescriptorRing.cpp"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/StatusDescriptorRingMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AXI2AFControl/IosaAxi2AfControl.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriver.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCDriverFilters.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHal.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR10j.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR11.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR15.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR16.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR2.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR21.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR22.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR4.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR6.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR7.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/AppleM2ScalerCSCHalMSR9.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR16.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR17.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR21.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR22.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DisplayScalerFilter.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/DriverCommonFunctions.h"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23Dv.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR23Rtk.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR25RTK.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FrameDescriptorRing.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/FrameDescriptorRingMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IOAsynchronousScheduler.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IOSurfaceAcceleratorClient.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IOSurfaceAcceleratorPreparator.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR15.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR18.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR4.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaColorManagerMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaFilmGrainControlMSR16.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaFilmGrainControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPowerManager.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaPowerManagerMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControl.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR18.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaRdmaControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaTiledCompressedMemMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/IosaWdmaControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/K2KTests.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControl.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR4.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerCSCColorConversionControlMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControl.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR20.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingASEControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControl.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR6.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerScalingControlMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControl.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR10.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR22.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR4.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/M2ScalerSrcDestCfgControlMSR8.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MSR23ChromaDownsampleFilter.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MSR23DefaultFilter.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MailBox.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MailBoxMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/ModularDefaultFilter.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStream.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStreamMSR15.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrApiodmaRegisterStreamMSR19.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrBlockDescriptorRegisterStream.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrBlockDescriptorRegisterStreamMSR23.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/MsrRegisterStream.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/Request.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/RingBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/Shared/Utility/IOFBSAGammaLUT.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/SpillBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/StatusDescriptorRing.cpp"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator/StatusDescriptorRingMSR23.cpp"
- "[IOSA][Boot ] Allocating BlockDescriptorRegStreamMSR23\n"
- "[IOSA][Boot ] obj=%p\n"

```

>  `com.apple.driver.AppleMobileFileIntegrity`

```diff

-938.0.16.0.0
+938.0.19.0.0
   __TEXT.__const: 0x1610
-  __TEXT.__cstring: 0x18cfd
+  __TEXT.__cstring: 0x18c81
   __TEXT.__os_log: 0x380
-  __TEXT_EXEC.__text: 0x31c1c
+  __TEXT_EXEC.__text: 0x31b44
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x81a
   __DATA.__common: 0xb0
   __DATA.__bss: 0x129
-  __DATA_CONST.__auth_got: 0x908
+  __DATA_CONST.__auth_got: 0x900
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__mod_init_func: 0x20

   __DATA_CONST.__const: 0xb130
   __DATA_CONST.__kalloc_type: 0x1200
   __DATA_CONST.__kalloc_var: 0x11d0
-  Functions: 899
+  Functions: 900
   Symbols:   1964
-  CStrings:  3068
+  CStrings:  3065
 
Symbols:
+ _AMFIUsingResearchVariant
+ __ZN20StaticPlatformPolicyILb1ELb1ELb1ELb1ELb1ELb1ELb1ELb0ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELj1ELb1ELb0EE29loadEntitlementsFromSignatureEPP14OSEntitlementsP7cs_blobP8LazyPathPPKc
+ __ZZL27_process_matches_constraintP4procyE21kalloc_type_view_5024
+ __ZZL27_process_matches_constraintP4procyE21kalloc_type_view_5047
+ __ZZN20StaticPlatformPolicyILb1ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELb1ELb0ELb1ELb0ELb0ELb1ELb0ELj2ELb1ELb0EE15check_signatureEP8LazyPathiP7cs_blobPjS5_ibbbjPPcPmE21kalloc_type_view_2857
+ __ZZN20StaticPlatformPolicyILb1ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELb1ELb0ELb1ELb0ELb0ELb1ELb0ELj2ELb1ELb0EE15check_signatureEP8LazyPathiP7cs_blobPjS5_ibbbjPPcPmE21kalloc_type_view_3067
+ __ZZN20StaticPlatformPolicyILb1ELb1ELb1ELb1ELb1ELb1ELb1ELb0ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELj1ELb1ELb0EE15check_signatureEP8LazyPathiP7cs_blobPjS5_ibbbjPPcPmE21kalloc_type_view_2857
+ __ZZN20StaticPlatformPolicyILb1ELb1ELb1ELb1ELb1ELb1ELb1ELb0ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELj1ELb1ELb0EE15check_signatureEP8LazyPathiP7cs_blobPjS5_ibbbjPPcPmE21kalloc_type_view_3067
- __ZN20StaticPlatformPolicyILb1ELb1ELb1ELb1ELb1ELb1ELb1ELb0ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELj1ELb0ELb1ELb0EE29loadEntitlementsFromSignatureEPP14OSEntitlementsP7cs_blobP8LazyPathPPKc
- __ZZL27_process_matches_constraintP4procyE21kalloc_type_view_5041
- __ZZL27_process_matches_constraintP4procyE21kalloc_type_view_5064
- __ZZN20StaticPlatformPolicyILb1ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELb1ELb0ELb1ELb0ELb0ELb1ELb0ELj2ELb0ELb1ELb0EE15check_signatureEP8LazyPathiP7cs_blobPjS5_ibbbjPPcPmE21kalloc_type_view_2857
- __ZZN20StaticPlatformPolicyILb1ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELb1ELb0ELb1ELb0ELb0ELb1ELb0ELj2ELb0ELb1ELb0EE15check_signatureEP8LazyPathiP7cs_blobPjS5_ibbbjPPcPmE21kalloc_type_view_3067
- __ZZN20StaticPlatformPolicyILb1ELb1ELb1ELb1ELb1ELb1ELb1ELb0ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELj1ELb0ELb1ELb0EE15check_signatureEP8LazyPathiP7cs_blobPjS5_ibbbjPPcPmE21kalloc_type_view_2857
- __ZZN20StaticPlatformPolicyILb1ELb1ELb1ELb1ELb1ELb1ELb1ELb0ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELj1ELb0ELb1ELb0EE15check_signatureEP8LazyPathiP7cs_blobPjS5_ibbbjPPcPmE21kalloc_type_view_3067
- _img4_chip_instantiate
CStrings:
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/CommonMem.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
+ "21:43:16"
+ "Jul  1 2024"
+ "cmd = (acm_command_t *)({ size_t sizeVal = (cmdSize); void *ptr = acm_mem_alloc_data(sizeVal); acm_mem_alloc_info(\"<data>\", ptr, sizeVal, \"/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c\", 22, __func__); ptr; })"
- "\"AMFI: No chip from IMG4? errno: %d\" @%s:%d"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/CommonMem.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
- "20:29:49"
- "AMFI: Allowing research due to amfi_allow_research boot arg"
- "Jun 20 2024"
- "amfi_allow_research"
- "cmd = (acm_command_t *)({ size_t sizeVal = (cmdSize); void *ptr = acm_mem_alloc_data(sizeVal); acm_mem_alloc_info(\"<data>\", ptr, sizeVal, \"/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c\", 22, __func__); ptr; })"

```

>  `com.apple.filesystems.hfs.kext`

```diff

-670.0.0.0.0
+672.0.0.0.0
   __TEXT.__const: 0x1a08
   __TEXT.__cstring: 0xa724
-  __TEXT_EXEC.__text: 0x4e01c
+  __TEXT_EXEC.__text: 0x4e0a0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4d0
   __DATA.__common: 0x10
CStrings:
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/hfs/core/VolumeAllocation.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_attrlist.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_btreeio.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_cnode.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_hotfiles.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_journal.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_readwrite.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_search.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_vfsops.c"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_vfsutils.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/hfs/core/VolumeAllocation.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_attrlist.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_btreeio.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_cnode.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_hotfiles.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_journal.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_readwrite.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_search.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_vfsops.c"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_vfsutils.c"

```

>  `com.apple.security.sandbox`

```diff

-2401.0.37.0.2
-  __TEXT.__const: 0x1df5b
-  __TEXT.__cstring: 0x70c0
+2401.0.48.0.0
+  __TEXT.__const: 0x1e02b
+  __TEXT.__cstring: 0x70ff
   __TEXT.__os_log: 0x1b6e
-  __TEXT_EXEC.__text: 0x424a4
+  __TEXT_EXEC.__text: 0x42550
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2b8
-  __DATA.__bss: 0x164f0
-  __DATA_CONST.__auth_got: 0x9b8
+  __DATA.__bss: 0x7e1b8
+  __DATA_CONST.__auth_got: 0x9c0
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x3a68
   __DATA_CONST.__kalloc_var: 0x550
   __DATA_CONST.__kalloc_type: 0x1200
   Functions: 846
-  Symbols:   1819
-  CStrings:  1240
+  Symbols:   1820
+  CStrings:  1242
 
Symbols:
+ _AMFIUsingResearchVariant
+ __block_descriptor_tmp.1.2976
+ __block_descriptor_tmp.1.3622
+ __block_descriptor_tmp.12.2529
+ __block_descriptor_tmp.12.3160
+ __block_descriptor_tmp.13.3174
+ __block_descriptor_tmp.13.811
+ __block_descriptor_tmp.14.2605
+ __block_descriptor_tmp.14.2762
+ __block_descriptor_tmp.14.3561
+ __block_descriptor_tmp.16.974
+ __block_descriptor_tmp.20.3175
+ __block_descriptor_tmp.23.2390
+ __block_descriptor_tmp.2383
+ __block_descriptor_tmp.2437
+ __block_descriptor_tmp.2498
+ __block_descriptor_tmp.25.2504
+ __block_descriptor_tmp.2604
+ __block_descriptor_tmp.2744
+ __block_descriptor_tmp.2984
+ __block_descriptor_tmp.3056
+ __block_descriptor_tmp.3157
+ __block_descriptor_tmp.317
+ __block_descriptor_tmp.3187
+ __block_descriptor_tmp.320
+ __block_descriptor_tmp.3240
+ __block_descriptor_tmp.3556
+ __block_descriptor_tmp.3618
+ __block_descriptor_tmp.4.3567
+ __block_descriptor_tmp.4.3625
+ __block_descriptor_tmp.5.3201
+ __block_descriptor_tmp.7.3630
+ __block_descriptor_tmp.805
+ __block_descriptor_tmp.849
+ __block_descriptor_tmp.9.2745
+ __block_descriptor_tmp.9.3076
+ __block_descriptor_tmp.973
+ __block_literal_global.2381
+ __block_literal_global.2975
+ __block_literal_global.3158
+ __block_literal_global.3198
+ __block_literal_global.3216
+ __block_literal_global.3615
+ _proc_matches_signing_id
+ check_data_volume_mounted.done_data_volume_mount
+ macl_lock_group.2445
+ operation_names.3310
+ pending_approval_entry_create.kalloc_type_view_1386
+ pending_approval_entry_create.kalloc_type_view_1394
+ pending_approval_entry_release.kalloc_type_view_1365
+ sandbox_lock_grp.2503
+ syscall_set_userland_profile._os_log_fmt.304
- __block_descriptor_tmp.1.2975
- __block_descriptor_tmp.1.3621
- __block_descriptor_tmp.12.2528
- __block_descriptor_tmp.12.3159
- __block_descriptor_tmp.13.3173
- __block_descriptor_tmp.13.812
- __block_descriptor_tmp.14.2604
- __block_descriptor_tmp.14.2761
- __block_descriptor_tmp.14.3560
- __block_descriptor_tmp.16.975
- __block_descriptor_tmp.20.3174
- __block_descriptor_tmp.23.2389
- __block_descriptor_tmp.2382
- __block_descriptor_tmp.2436
- __block_descriptor_tmp.2497
- __block_descriptor_tmp.25.2503
- __block_descriptor_tmp.2603
- __block_descriptor_tmp.2743
- __block_descriptor_tmp.2983
- __block_descriptor_tmp.3055
- __block_descriptor_tmp.315
- __block_descriptor_tmp.3156
- __block_descriptor_tmp.318
- __block_descriptor_tmp.3186
- __block_descriptor_tmp.3239
- __block_descriptor_tmp.3555
- __block_descriptor_tmp.3617
- __block_descriptor_tmp.4.3566
- __block_descriptor_tmp.4.3624
- __block_descriptor_tmp.5.3200
- __block_descriptor_tmp.7.3629
- __block_descriptor_tmp.806
- __block_descriptor_tmp.850
- __block_descriptor_tmp.9.2744
- __block_descriptor_tmp.9.3075
- __block_descriptor_tmp.974
- __block_literal_global.2380
- __block_literal_global.2974
- __block_literal_global.3157
- __block_literal_global.3197
- __block_literal_global.3215
- __block_literal_global.3614
- _check_data_volume_mounted
- _done_data_volume_mount
- macl_lock_group.2444
- operation_names.3309
- pending_approval_entry_create.kalloc_type_view_1388
- pending_approval_entry_create.kalloc_type_view_1396
- pending_approval_entry_release.kalloc_type_view_1367
- sandbox_lock_grp.2502
- syscall_set_userland_profile._os_log_fmt.306
CStrings:
+ "59GAB85EFG.com.apple.dt.Xcode"
+ "com.apple.application-identifier"

```

>  `com.apple.driver.AppleThunderboltNHI`

```diff

-798.0.1.0.0
+798.0.2.0.0
   __TEXT.__const: 0x28a08
-  __TEXT.__cstring: 0xa6c0
+  __TEXT.__cstring: 0xa6db
   __TEXT.__os_log: 0x6cea
-  __TEXT_EXEC.__text: 0x394fc
+  __TEXT_EXEC.__text: 0x3962c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x280
   __DATA.__common: 0x450
-  __DATA_CONST.__auth_got: 0x398
+  __DATA_CONST.__auth_got: 0x3a0
   __DATA_CONST.__got: 0x128
   __DATA_CONST.__mod_init_func: 0xd8
   __DATA_CONST.__mod_term_func: 0xd8

   __DATA_CONST.__kalloc_type: 0x6c0
   __DATA_CONST.__kalloc_var: 0x460
   Functions: 897
-  Symbols:   1987
-  CStrings:  586
+  Symbols:   1988
+  CStrings:  587
 
Symbols:
+ __ZN20IOPortTransportState12copyMetadataEPKc
CStrings:
+ "20:01:17"
+ "AsymmetricModeSupportedBit"
+ "Jul  3 2024"
- "20:30:07"
- "Jun 20 2024"

```

>  `com.apple.driver.AppleDCP`

```diff

-811.0.17.0.0
+811.0.20.0.0
   __TEXT.__cstring: 0x1664
   __TEXT.__const: 0x18
   __TEXT_EXEC.__text: 0x61f0

   __DATA_CONST.__got: 0x80
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x20b8
+  __DATA_CONST.__const: 0x20b0
   __DATA_CONST.__kalloc_type: 0x100
   Functions: 175
-  Symbols:   577
+  Symbols:   576
   CStrings:  115
 
Symbols:
- __ZNK11AFKEPKextV222useRTBuddyPowerActionsEv

```

>  `com.apple.driver.AppleH11ANEInterface`

```diff

-8.13.2.0.0
-  __TEXT.__os_log: 0x310c7
-  __TEXT.__cstring: 0xab3d
-  __TEXT.__const: 0x5b0
-  __TEXT_EXEC.__text: 0xa3d3c
+8.15.1.0.0
+  __TEXT.__os_log: 0x312ff
+  __TEXT.__cstring: 0xac33
+  __TEXT.__const: 0x5c0
+  __TEXT_EXEC.__text: 0xa4784
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2be0
   __DATA.__common: 0x3c8
   __DATA.__bss: 0x270
   __DATA_CONST.__auth_got: 0x878
   __DATA_CONST.__got: 0x118
-  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x98
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0xa038
-  __DATA_CONST.__kalloc_type: 0x2c80
-  __DATA_CONST.__kalloc_var: 0x2850
-  Functions: 1826
-  Symbols:   5988
-  CStrings:  992
+  __DATA_CONST.__const: 0xa058
+  __DATA_CONST.__kalloc_type: 0x2d00
+  __DATA_CONST.__kalloc_var: 0x2990
+  Functions: 1829
+  Symbols:   6002
+  CStrings:  1002
 
Symbols:
+ __Block_byref_object_copy_.521
+ __Block_byref_object_dispose_.522
+ __ZN13ANEDataBuffer9asyncWireEjj
+ __ZN17H11ANEBufferCache14isBufferCachedEjj13ANEBufferType
+ __ZN17H11ANEBufferCache26freeAutoPrewiredBufferInfoEb
+ __ZN8H11ANEIn22findClientByOwningTaskEP4taskP5OSSet
+ __ZN8H11ANEIn23findClientByCodesigningEPhS0_P5OSSetb
+ __ZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbb
+ __ZN8H11ANEIn38ANE_unwireAllAutoPrewiredBuffers_gatedEv
+ __ZN8H11ANEIn39ANE_ProgramCheckandPrewireBuffers_gatedEP17H11ANEBufferCacheP30H11ANEProgramRequestArgsStructP46H11ANEProgramSendRequestAdditionalParamsStruct
+ __ZN8H11ANEIn42setClientHintInitialChecksAndLookups_gatedEP19ANEClientHintStruct
+ __ZZL10ffw_callocmmE22kalloc_type_view_24412
+ __ZZL8ffw_freePvmE22kalloc_type_view_24435
+ __ZZN13ANEDataBuffer9asyncWireEjjE11_os_log_fmt
+ __ZZN13ANEDataBuffer9asyncWireEjjE11_os_log_fmt_0
+ __ZZN17H11ANEBufferCache14freeBufferInfoEP22H11ANEBufferInfoStructbE21kalloc_type_view_1123
+ __ZZN17H11ANEBufferCache14freeBufferInfoEP22H11ANEBufferInfoStructbE21kalloc_type_view_1125
+ __ZZN17H11ANEBufferCache14freeBufferInfoEP22H11ANEBufferInfoStructbE21kalloc_type_view_1132
+ __ZZN17H11ANEBufferCache14isBufferCachedEjj13ANEBufferTypeE11_os_log_fmt
+ __ZZN17H11ANEBufferCache26freeAutoPrewiredBufferInfoEbE11_os_log_fmt
+ __ZZN17H11ANEBufferCache26freeAutoPrewiredBufferInfoEbE11_os_log_fmt_0
+ __ZZN17H11ANEBufferCachedlEPvmE20kalloc_type_view_631
+ __ZZN17H11ANEBufferCachenwEmE20kalloc_type_view_631
+ __ZZN18AneIspIPCEndPointsdlEPvmE21kalloc_type_view_1141
+ __ZZN18AneIspIPCEndPointsnwEmE21kalloc_type_view_1141
+ __ZZN18McacheDriverClient24McacheDriverStreamObjectdaEPvE21kalloc_type_view_1169
+ __ZZN18McacheDriverClient24McacheDriverStreamObjectnaEmE21kalloc_type_view_1169
+ __ZZN18McacheDriverClientdlEPvmE21kalloc_type_view_1230
+ __ZZN18McacheDriverClientnwEmE21kalloc_type_view_1230
+ __ZZN8H11ANEIn12ProcessAbortEP25H11ANEProcessParamsStructPvbE22kalloc_type_view_11012
+ __ZZN8H11ANEIn12ProcessAbortEP25H11ANEProcessParamsStructPvbE22kalloc_type_view_11016
+ __ZZN8H11ANEIn12ProcessAbortEP25H11ANEProcessParamsStructPvbE22kalloc_type_view_11020
+ __ZZN8H11ANEIn12ProcessAbortEP25H11ANEProcessParamsStructPvbE22kalloc_type_view_11049
+ __ZZN8H11ANEIn13setClientHintEP19ANEClientHintStructE11_os_log_fmt
+ __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45442
+ __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45473
+ __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45482
+ __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45490
+ __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45494
+ __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45514
+ __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45524
+ __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45532
+ __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45538
+ __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45557
+ __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45568
+ __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45576
+ __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45580
+ __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45600
+ __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45610
+ __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45618
+ __ZZN8H11ANEIn17clearfActionQueueEvE22kalloc_type_view_12557
+ __ZZN8H11ANEIn17workerThreadEntryEPS_E22kalloc_type_view_12500
+ __ZZN8H11ANEIn18enqueueActionBlockEU13block_pointerFvvEE22kalloc_type_view_12451
+ __ZZN8H11ANEIn22ANE_ProgramSendRequestEP30H11ANEProgramRequestArgsStructPyPvbP27H11ANEReqCallbackDataStructP4taskP24H11ANESharedEventsStructE22kalloc_type_view_36476
+ __ZZN8H11ANEIn22ANE_ProgramSendRequestEP30H11ANEProgramRequestArgsStructPyPvbP27H11ANEReqCallbackDataStructP4taskP24H11ANESharedEventsStructE22kalloc_type_view_36486
+ __ZZN8H11ANEIn22ANE_ProgramSendRequestEP30H11ANEProgramRequestArgsStructPyPvbP27H11ANEReqCallbackDataStructP4taskP24H11ANESharedEventsStructE22kalloc_type_view_36589
+ __ZZN8H11ANEIn22ANE_ProgramSendRequestEP30H11ANEProgramRequestArgsStructPyPvbP27H11ANEReqCallbackDataStructP4taskP24H11ANESharedEventsStructE22kalloc_type_view_36603
+ __ZZN8H11ANEIn22findClientByOwningTaskEP4taskP5OSSetE11_os_log_fmt
+ __ZZN8H11ANEIn22findClientByOwningTaskEP4taskP5OSSetE11_os_log_fmt_0
+ __ZZN8H11ANEIn22findClientByOwningTaskEP4taskP5OSSetE11_os_log_fmt_1
+ __ZZN8H11ANEIn22findClientByOwningTaskEP4taskP5OSSetE11_os_log_fmt_2
+ __ZZN8H11ANEIn22initializeANESoCConfigEvE21kalloc_type_view_5218
+ __ZZN8H11ANEIn22initializeANESoCConfigEvE21kalloc_type_view_5298
+ __ZZN8H11ANEIn22initializeANESoCConfigEvE21kalloc_type_view_5804
+ __ZZN8H11ANEIn22initializeANESoCConfigEvE21kalloc_type_view_6038
+ __ZZN8H11ANEIn23ANE_ProgramCreate_gatedEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructE11_os_log_fmt__132_
+ __ZZN8H11ANEIn23ANE_ProgramCreate_gatedEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructE11_os_log_fmt__152_
+ __ZZN8H11ANEIn23ANE_ProgramCreate_gatedEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructE22kalloc_type_view_29160
+ __ZZN8H11ANEIn23ANE_ProgramCreate_gatedEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructE22kalloc_type_view_29302
+ __ZZN8H11ANEIn23ANE_ProgramCreate_gatedEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructE22kalloc_type_view_29538
+ __ZZN8H11ANEIn23ANE_ProgramCreate_gatedEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructE22kalloc_type_view_29626
+ __ZZN8H11ANEIn23ANE_ProgramCreate_gatedEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructE22kalloc_type_view_30907
+ __ZZN8H11ANEIn23ANE_ProgramCreate_gatedEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructE22kalloc_type_view_31337
+ __ZZN8H11ANEIn23ANE_ProgramCreate_gatedEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructE22kalloc_type_view_31387
+ __ZZN8H11ANEIn23ANE_ProgramCreate_gatedEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructE22kalloc_type_view_31403
+ __ZZN8H11ANEIn23findClientByCodesigningEPhS0_P5OSSetbE11_os_log_fmt
+ __ZZN8H11ANEIn23findClientByCodesigningEPhS0_P5OSSetbE11_os_log_fmt_0
+ __ZZN8H11ANEIn23handleRequestCompletionEP25H11ANERequestParamsStructiE21kalloc_type_view_9142
+ __ZZN8H11ANEIn23handleRequestCompletionEP25H11ANERequestParamsStructiE21kalloc_type_view_9146
+ __ZZN8H11ANEIn23handleRequestCompletionEP25H11ANERequestParamsStructiE21kalloc_type_view_9150
+ __ZZN8H11ANEIn23handleRequestCompletionEP25H11ANERequestParamsStructiE21kalloc_type_view_9188
+ __ZZN8H11ANEIn23initializeANEPropertiesEvE21kalloc_type_view_4558
+ __ZZN8H11ANEIn24ANE_UserClientOpen_gatedEPvPKcP4taskjE11_os_log_fmt_2
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt_0
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt_1
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt_2
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt_3
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt_4
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt_5
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt_6
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt_7
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt_8
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt_9
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__10_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__11_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__12_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__13_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__14_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__15_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__16_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__17_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__18_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__19_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__20_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__21_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__22_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__23_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__24_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__25_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__26_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__27_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__28_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__29_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__30_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__31_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__32_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__33_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__34_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__35_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__36_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__37_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE11_os_log_fmt__38_
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE22kalloc_type_view_42532
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE22kalloc_type_view_42641
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE22kalloc_type_view_42644
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE22kalloc_type_view_42850
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE22kalloc_type_view_42853
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE22kalloc_type_view_43047
+ __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbbE22kalloc_type_view_43089
+ __ZZN8H11ANEIn26AllocateIntermediateBufferEyPP43H11ANEIntermediateBufferSurfaceParamsStructP31H11ANEProgramBufferParamsStructP25H11ANEProcessParamsStructybE21kalloc_type_view_2061
+ __ZZN8H11ANEIn26AllocateIntermediateBufferEyPP43H11ANEIntermediateBufferSurfaceParamsStructP31H11ANEProgramBufferParamsStructP25H11ANEProcessParamsStructybE21kalloc_type_view_2078
+ __ZZN8H11ANEIn26ReleaseProgramMemoryBufferEP31H11ANEProgramBufferParamsStructbE21kalloc_type_view_3498
+ __ZZN8H11ANEIn26ReleaseProgramMemoryBufferEP31H11ANEProgramBufferParamsStructbE21kalloc_type_view_3560
+ __ZZN8H11ANEIn26ReleaseProgramMemoryBufferEP31H11ANEProgramBufferParamsStructbE21kalloc_type_view_3564
+ __ZZN8H11ANEIn26cleanupAllChainingMappingsEP34H11ANEChainingCacheReqParamsStructE22kalloc_type_view_32124
+ __ZZN8H11ANEIn26cleanupAllChainingMappingsEP34H11ANEChainingCacheReqParamsStructE22kalloc_type_view_32129
+ __ZZN8H11ANEIn26cleanupAllChainingMappingsEP34H11ANEChainingCacheReqParamsStructE22kalloc_type_view_32189
+ __ZZN8H11ANEIn26cleanupAllChainingMappingsEP34H11ANEChainingCacheReqParamsStructE22kalloc_type_view_32204
+ __ZZN8H11ANEIn27SendRequestToFirmware_gatedEP25H11ANERequestParamsStructP9IOSurfaceibbE22kalloc_type_view_35133
+ __ZZN8H11ANEIn27SendRequestToFirmware_gatedEP25H11ANERequestParamsStructP9IOSurfaceibbE22kalloc_type_view_35137
+ __ZZN8H11ANEIn27SendRequestToFirmware_gatedEP25H11ANERequestParamsStructP9IOSurfaceibbE22kalloc_type_view_35141
+ __ZZN8H11ANEIn27SendRequestToFirmware_gatedEP25H11ANERequestParamsStructP9IOSurfaceibbE22kalloc_type_view_35179
+ __ZZN8H11ANEIn28ANE_ProgramInputsReady_gatedEP29H11ANEInputBuffersReadyStructE22kalloc_type_view_33464
+ __ZZN8H11ANEIn28processTargetToHostIOCommandEyyyE22kalloc_type_view_13360
+ __ZZN8H11ANEIn28processTargetToHostIOCommandEyyyE22kalloc_type_view_13507
+ __ZZN8H11ANEIn28processTargetToHostIOCommandEyyyE22kalloc_type_view_14325
+ __ZZN8H11ANEIn28processTargetToHostIOCommandEyyyE22kalloc_type_view_14912
+ __ZZN8H11ANEIn28processTargetToHostIOCommandEyyyE22kalloc_type_view_14916
+ __ZZN8H11ANEIn28processTargetToHostIOCommandEyyyE22kalloc_type_view_14920
+ __ZZN8H11ANEIn28processTargetToHostIOCommandEyyyE22kalloc_type_view_14939
+ __ZZN8H11ANEIn29ANE_AddClientForProgram_gatedEPvP22H11ANEDeviceInfoStructP4taskE22kalloc_type_view_20086
+ __ZZN8H11ANEIn29ANE_AddClientForProgram_gatedEPvP22H11ANEDeviceInfoStructP4taskE22kalloc_type_view_20111
+ __ZZN8H11ANEIn29ANE_AddClientForProgram_gatedEPvP22H11ANEDeviceInfoStructP4taskE22kalloc_type_view_20120
+ __ZZN8H11ANEIn29ANE_AddClientForProgram_gatedEPvP22H11ANEDeviceInfoStructP4taskE22kalloc_type_view_20133
+ __ZZN8H11ANEIn29ANE_AddClientForProgram_gatedEPvP22H11ANEDeviceInfoStructP4taskE22kalloc_type_view_20143
+ __ZZN8H11ANEIn29patchMutableInstanceProcedureEP25H11ANEProcessParamsStructjjP36H11ANEProgramInstanceProcedureStructiE22kalloc_type_view_33981
+ __ZZN8H11ANEIn29patchMutableInstanceProcedureEP25H11ANEProcessParamsStructjjP36H11ANEProgramInstanceProcedureStructiE22kalloc_type_view_34116
+ __ZZN8H11ANEIn30ANE_ProgramCreatePreprocessingEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructPP23ZinComputeProgramStructPP31H11ANEProgramBufferParamsStructP35H11ANEProgramCreateArgsStructOutputE22kalloc_type_view_27825
+ __ZZN8H11ANEIn30ANE_ProgramCreatePreprocessingEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructPP23ZinComputeProgramStructPP31H11ANEProgramBufferParamsStructP35H11ANEProgramCreateArgsStructOutputE22kalloc_type_view_27883
+ __ZZN8H11ANEIn30ANE_ProgramCreatePreprocessingEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructPP23ZinComputeProgramStructPP31H11ANEProgramBufferParamsStructP35H11ANEProgramCreateArgsStructOutputE22kalloc_type_view_28074
+ __ZZN8H11ANEIn31ANE_MemoryMapStatsBuffers_gatedEP27H11ANEMemoryMapParamsStructE22kalloc_type_view_43424
+ __ZZN8H11ANEIn32ANE_ProgramChainingPrepare_gatedEP33_H11ANEProgramChainingPrepareArgsP40H11ANEProgramChainingPrepareOutputStructE22kalloc_type_view_32701
+ __ZZN8H11ANEIn32ANE_ProgramChainingPrepare_gatedEP33_H11ANEProgramChainingPrepareArgsP40H11ANEProgramChainingPrepareOutputStructE22kalloc_type_view_32837
+ __ZZN8H11ANEIn32ANE_ProgramChainingPrepare_gatedEP33_H11ANEProgramChainingPrepareArgsP40H11ANEProgramChainingPrepareOutputStructE22kalloc_type_view_32838
+ __ZZN8H11ANEIn33buildFirmwareChainingCacheRequestEP34H11ANEChainingCacheReqParamsStructP35H11ANEProgramCreateArgsStructOutputE22kalloc_type_view_32321
+ __ZZN8H11ANEIn33deleteProgramChainingCacheRequestEPP34H11ANEChainingCacheReqParamsStructE22kalloc_type_view_32086
+ __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40803
+ __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40943
+ __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40973
+ __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_41552
+ __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_41644
+ __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_41649
+ __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_41696
+ __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_41700
+ __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_41704
+ __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_42244
+ __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_42248
+ __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_42252
+ __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_42286
+ __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_42293
+ __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_42298
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_37347
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_37364
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_37373
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_37382
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_37391
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_37402
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_37424
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_37457
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_37458
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_37468
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_37478
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_39822
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_39844
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_39850
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_39891
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_39895
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_39899
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40587
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40591
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40595
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40656
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40663
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40669
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40675
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40681
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40688
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40691
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40694
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40697
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40700
+ __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40702
+ __ZZN8H11ANEIn36patchClusterMutableInstanceProcedureEP25H11ANEProcessParamsStructjjP36H11ANEProgramInstanceProcedureStructPP13ANEDataBufferiE22kalloc_type_view_33813
+ __ZZN8H11ANEIn36patchClusterMutableInstanceProcedureEP25H11ANEProcessParamsStructjjP36H11ANEProgramInstanceProcedureStructPP13ANEDataBufferiE22kalloc_type_view_33942
+ __ZZN8H11ANEIn38ANE_unwireAllAutoPrewiredBuffers_gatedEvE11_os_log_fmt
+ __ZZN8H11ANEIn39ANE_ProgramCheckandPrewireBuffers_gatedEP17H11ANEBufferCacheP30H11ANEProgramRequestArgsStructP46H11ANEProgramSendRequestAdditionalParamsStructE11_os_log_fmt
+ __ZZN8H11ANEIn39ANE_ProgramCheckandPrewireBuffers_gatedEP17H11ANEBufferCacheP30H11ANEProgramRequestArgsStructP46H11ANEProgramSendRequestAdditionalParamsStructE11_os_log_fmt_0
+ __ZZN8H11ANEIn39ANE_ProgramCheckandPrewireBuffers_gatedEP17H11ANEBufferCacheP30H11ANEProgramRequestArgsStructP46H11ANEProgramSendRequestAdditionalParamsStructE11_os_log_fmt_1
+ __ZZN8H11ANEIn39ANE_ProgramCheckandPrewireBuffers_gatedEP17H11ANEBufferCacheP30H11ANEProgramRequestArgsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40726
+ __ZZN8H11ANEIn39ANE_ProgramCheckandPrewireBuffers_gatedEP17H11ANEBufferCacheP30H11ANEProgramRequestArgsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40743
+ __ZZN8H11ANEIn39ANE_ProgramCheckandPrewireBuffers_gatedEP17H11ANEBufferCacheP30H11ANEProgramRequestArgsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40760
+ __ZZN8H11ANEIn39ANE_ProgramCheckandPrewireBuffers_gatedEP17H11ANEBufferCacheP30H11ANEProgramRequestArgsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40788
+ __ZZN8H11ANEIn42setClientHintInitialChecksAndLookups_gatedEP19ANEClientHintStructE11_os_log_fmt_0
+ __ZZN8H11ANEIn42setClientHintInitialChecksAndLookups_gatedEP19ANEClientHintStructE11_os_log_fmt_1
+ __ZZN8H11ANEIn42setClientHintInitialChecksAndLookups_gatedEP19ANEClientHintStructE11_os_log_fmt_2
+ __ZZN8H11ANEIn42setClientHintInitialChecksAndLookups_gatedEP19ANEClientHintStructE11_os_log_fmt_3
+ __ZZN8H11ANEIn42setClientHintInitialChecksAndLookups_gatedEP19ANEClientHintStructE11_os_log_fmt_4
+ __ZZN8H11ANEIn42setClientHintInitialChecksAndLookups_gatedEP19ANEClientHintStructE11_os_log_fmt_5
+ __ZZN8H11ANEIn42setClientHintInitialChecksAndLookups_gatedEP19ANEClientHintStructE11_os_log_fmt_6
+ __ZZN8H11ANEIn42setClientHintInitialChecksAndLookups_gatedEP19ANEClientHintStructE11_os_log_fmt_7
+ __ZZN8H11ANEIn42setClientHintInitialChecksAndLookups_gatedEP19ANEClientHintStructE11_os_log_fmt_8
+ __ZZN8H11ANEIn42setClientHintInitialChecksAndLookups_gatedEP19ANEClientHintStructE11_os_log_fmt_9
+ __ZZN8H11ANEIn45ANE_PatchClusterProcessInstanceWeightsBuffersEP25H11ANEProcessParamsStructP33H11ANEProgramInstanceParamsStructP4taskE22kalloc_type_view_44073
+ __ZZN8H11ANEIn45ANE_PatchClusterProcessInstanceWeightsBuffersEP25H11ANEProcessParamsStructP33H11ANEProgramInstanceParamsStructP4taskE22kalloc_type_view_44348
+ __ZZN8H11ANEIn4stopEP9IOServiceE22kalloc_type_view_12268
+ __ZZN8H11ANEIn4stopEP9IOServiceE22kalloc_type_view_12323
+ __ZZN8H11ANEIn4stopEP9IOServiceE22kalloc_type_view_12326
+ __ZZN8H11ANEIn51ANE_ProgramSendRequestInitialChecksAndLookups_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE11_os_log_fmt__25_
+ __ZZN8H11ANEIn51ANE_ProgramSendRequestInitialChecksAndLookups_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE11_os_log_fmt__43_
+ __ZZZN13ANEDataBuffer9asyncWireEjjEUb_E11_os_log_fmt
+ __ZZZN13ANEDataBuffer9asyncWireEjjEUb_E11_os_log_fmt_0
+ __ZZZN13ANEDataBuffer9asyncWireEjjEUb_E11_os_log_fmt_1
+ __ZZZN8H11ANEIn13setClientHintEP19ANEClientHintStructEUb2_E11_os_log_fmt
+ __ZZZN8H11ANEIn26lookupProgramWithAssetPathEP12OSCollectionPKcPP31H11ANEProgramBufferParamsStructPP25H11ANEProcessParamsStructP5OSSetEUb3_E11_os_log_fmt
+ __ZZZN8H11ANEIn26lookupProgramWithAssetPathEP12OSCollectionPKcPP31H11ANEProgramBufferParamsStructPP25H11ANEProcessParamsStructP5OSSetEUb3_E11_os_log_fmt_0
+ __ZZZZN8H11ANEIn26lookupProgramWithAssetPathEP12OSCollectionPKcPP31H11ANEProgramBufferParamsStructPP25H11ANEProcessParamsStructP5OSSetEUb3_EUb4_E11_os_log_fmt
+ __ZZZZN8H11ANEIn26lookupProgramWithAssetPathEP12OSCollectionPKcPP31H11ANEProgramBufferParamsStructPP25H11ANEProcessParamsStructP5OSSetEUb3_EUb4_E11_os_log_fmt_0
+ __ZZZZN8H11ANEIn26lookupProgramWithAssetPathEP12OSCollectionPKcPP31H11ANEProgramBufferParamsStructPP25H11ANEProcessParamsStructP5OSSetEUb3_EUb4_E11_os_log_fmt_1
+ __ZZZZN8H11ANEIn26lookupProgramWithAssetPathEP12OSCollectionPKcPP31H11ANEProgramBufferParamsStructPP25H11ANEProcessParamsStructP5OSSetEUb3_EUb4_E11_os_log_fmt_2
+ __ZZZZN8H11ANEIn26lookupProgramWithAssetPathEP12OSCollectionPKcPP31H11ANEProgramBufferParamsStructPP25H11ANEProcessParamsStructP5OSSetEUb3_EUb4_E11_os_log_fmt_3
+ __ZZZZN8H11ANEIn26lookupProgramWithAssetPathEP12OSCollectionPKcPP31H11ANEProgramBufferParamsStructPP25H11ANEProcessParamsStructP5OSSetEUb3_EUb4_E11_os_log_fmt_4
+ __ZZZZN8H11ANEIn26lookupProgramWithAssetPathEP12OSCollectionPKcPP31H11ANEProgramBufferParamsStructPP25H11ANEProcessParamsStructP5OSSetEUb3_EUb4_E11_os_log_fmt_5
+ __ZZZZN8H11ANEIn27HandleFirmwareTimeout_gatedEvEUb5_EUb6_E11_os_log_fmt
+ ___ZN8H11ANEIn19setClientHint_gatedEP19ANEClientHintStruct_block_invoke.314
+ ___ZN8H11ANEIn19setClientHint_gatedEP19ANEClientHintStruct_block_invoke.318
+ ____ZN13ANEDataBuffer9asyncWireEjj_block_invoke
+ ____ZN13ANEDataBuffer9asyncWireEjj_block_invoke_2
+ ____ZN8H11ANEIn13setClientHintEP19ANEClientHintStruct_block_invoke_2
+ __block_descriptor_tmp.305
+ __block_descriptor_tmp.313
+ __block_descriptor_tmp.317
+ __block_descriptor_tmp.321
+ __block_descriptor_tmp.324
+ __block_descriptor_tmp.327
+ __block_descriptor_tmp.339
+ __block_descriptor_tmp.460
+ __block_descriptor_tmp.491
+ __block_descriptor_tmp.503
+ __block_descriptor_tmp.504
+ __block_descriptor_tmp.513
+ __block_descriptor_tmp.514
+ __block_descriptor_tmp.518
+ __block_descriptor_tmp.527
+ __block_descriptor_tmp.542
+ __block_descriptor_tmp.543
+ __block_descriptor_tmp.544
+ __block_descriptor_tmp.545
+ __cxx_global_var_init.2427
+ __cxx_global_var_init.2428
+ __cxx_global_var_init.2429
+ __cxx_global_var_init.2430
+ __cxx_global_var_init.2431
- __Block_byref_object_copy_.518
- __Block_byref_object_dispose_.519
- __ZN13ANEDataBuffer9asyncWireEj
- __ZN17H11ANEBufferCache14isBufferCachedEj
- __ZN8H11ANEIn22findClientByOwningTaskEP4taskPP25H11ANEClientContextStructPKc
- __ZN8H11ANEIn23findClientByCodesigningEPhS0_PKcPP25H11ANEClientContextStructb
- __ZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructb
- __ZZL10ffw_callocmmE22kalloc_type_view_24292
- __ZZL8ffw_freePvmE22kalloc_type_view_24315
- __ZZN13ANEDataBuffer9asyncWireEjE11_os_log_fmt
- __ZZN13ANEDataBuffer9asyncWireEjE11_os_log_fmt_0
- __ZZN17H11ANEBufferCache14freeBufferInfoEP22H11ANEBufferInfoStructbE21kalloc_type_view_1112
- __ZZN17H11ANEBufferCache14freeBufferInfoEP22H11ANEBufferInfoStructbE21kalloc_type_view_1114
- __ZZN17H11ANEBufferCache14freeBufferInfoEP22H11ANEBufferInfoStructbE21kalloc_type_view_1121
- __ZZN17H11ANEBufferCache14isBufferCachedEjE11_os_log_fmt
- __ZZN17H11ANEBufferCachedlEPvmE20kalloc_type_view_618
- __ZZN17H11ANEBufferCachenwEmE20kalloc_type_view_618
- __ZZN18AneIspIPCEndPointsdlEPvmE21kalloc_type_view_1113
- __ZZN18AneIspIPCEndPointsnwEmE21kalloc_type_view_1113
- __ZZN18McacheDriverClient24McacheDriverStreamObjectdaEPvE21kalloc_type_view_1141
- __ZZN18McacheDriverClient24McacheDriverStreamObjectnaEmE21kalloc_type_view_1141
- __ZZN18McacheDriverClientdlEPvmE21kalloc_type_view_1202
- __ZZN18McacheDriverClientnwEmE21kalloc_type_view_1202
- __ZZN24ANEClientHintsUserClient13setPropertiesEP8OSObjectE11_os_log_fmt_7
- __ZZN8H11ANEIn12ProcessAbortEP25H11ANEProcessParamsStructPvbE22kalloc_type_view_10943
- __ZZN8H11ANEIn12ProcessAbortEP25H11ANEProcessParamsStructPvbE22kalloc_type_view_10947
- __ZZN8H11ANEIn12ProcessAbortEP25H11ANEProcessParamsStructPvbE22kalloc_type_view_10951
- __ZZN8H11ANEIn12ProcessAbortEP25H11ANEProcessParamsStructPvbE22kalloc_type_view_10980
- __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45117
- __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45148
- __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45157
- __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45165
- __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45169
- __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45189
- __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45199
- __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45207
- __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45213
- __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45232
- __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45243
- __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45251
- __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45255
- __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45275
- __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45285
- __ZZN8H11ANEIn15createReportersEvE22kalloc_type_view_45293
- __ZZN8H11ANEIn17clearfActionQueueEvE22kalloc_type_view_12488
- __ZZN8H11ANEIn17workerThreadEntryEPS_E22kalloc_type_view_12431
- __ZZN8H11ANEIn18enqueueActionBlockEU13block_pointerFvvEE22kalloc_type_view_12382
- __ZZN8H11ANEIn19setClientHint_gatedEP19ANEClientHintStructE11_os_log_fmt__31_
- __ZZN8H11ANEIn19setClientHint_gatedEP19ANEClientHintStructE11_os_log_fmt__35_
- __ZZN8H11ANEIn19setClientHint_gatedEP19ANEClientHintStructE11_os_log_fmt__36_
- __ZZN8H11ANEIn19setClientHint_gatedEP19ANEClientHintStructE11_os_log_fmt__37_
- __ZZN8H11ANEIn19setClientHint_gatedEP19ANEClientHintStructE11_os_log_fmt__38_
- __ZZN8H11ANEIn19setClientHint_gatedEP19ANEClientHintStructE11_os_log_fmt__39_
- __ZZN8H11ANEIn19setClientHint_gatedEP19ANEClientHintStructE11_os_log_fmt__40_
- __ZZN8H11ANEIn19setClientHint_gatedEP19ANEClientHintStructE11_os_log_fmt__41_
- __ZZN8H11ANEIn19setClientHint_gatedEP19ANEClientHintStructE11_os_log_fmt__43_
- __ZZN8H11ANEIn19setClientHint_gatedEP19ANEClientHintStructE11_os_log_fmt__44_
- __ZZN8H11ANEIn19setClientHint_gatedEP19ANEClientHintStructE11_os_log_fmt__45_
- __ZZN8H11ANEIn22ANE_ProgramSendRequestEP30H11ANEProgramRequestArgsStructPyPvbP27H11ANEReqCallbackDataStructP4taskP24H11ANESharedEventsStructE22kalloc_type_view_36343
- __ZZN8H11ANEIn22ANE_ProgramSendRequestEP30H11ANEProgramRequestArgsStructPyPvbP27H11ANEReqCallbackDataStructP4taskP24H11ANESharedEventsStructE22kalloc_type_view_36353
- __ZZN8H11ANEIn22ANE_ProgramSendRequestEP30H11ANEProgramRequestArgsStructPyPvbP27H11ANEReqCallbackDataStructP4taskP24H11ANESharedEventsStructE22kalloc_type_view_36456
- __ZZN8H11ANEIn22ANE_ProgramSendRequestEP30H11ANEProgramRequestArgsStructPyPvbP27H11ANEReqCallbackDataStructP4taskP24H11ANESharedEventsStructE22kalloc_type_view_36470
- __ZZN8H11ANEIn22findClientByOwningTaskEP4taskPP25H11ANEClientContextStructPKcE11_os_log_fmt
- __ZZN8H11ANEIn22findClientByOwningTaskEP4taskPP25H11ANEClientContextStructPKcE11_os_log_fmt_0
- __ZZN8H11ANEIn22findClientByOwningTaskEP4taskPP25H11ANEClientContextStructPKcE11_os_log_fmt_1
- __ZZN8H11ANEIn22findClientByOwningTaskEP4taskPP25H11ANEClientContextStructPKcE11_os_log_fmt_2
- __ZZN8H11ANEIn22findClientByOwningTaskEP4taskPP25H11ANEClientContextStructPKcE11_os_log_fmt_3
- __ZZN8H11ANEIn22findClientByOwningTaskEP4taskPP25H11ANEClientContextStructPKcE11_os_log_fmt_4
- __ZZN8H11ANEIn22initializeANESoCConfigEvE21kalloc_type_view_5163
- __ZZN8H11ANEIn22initializeANESoCConfigEvE21kalloc_type_view_5243
- __ZZN8H11ANEIn22initializeANESoCConfigEvE21kalloc_type_view_5746
- __ZZN8H11ANEIn22initializeANESoCConfigEvE21kalloc_type_view_5979
- __ZZN8H11ANEIn23ANE_ProgramCreate_gatedEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructE11_os_log_fmt__134_
- __ZZN8H11ANEIn23ANE_ProgramCreate_gatedEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructE22kalloc_type_view_29033
- __ZZN8H11ANEIn23ANE_ProgramCreate_gatedEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructE22kalloc_type_view_29169
- __ZZN8H11ANEIn23ANE_ProgramCreate_gatedEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructE22kalloc_type_view_29405
- __ZZN8H11ANEIn23ANE_ProgramCreate_gatedEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructE22kalloc_type_view_29493
- __ZZN8H11ANEIn23ANE_ProgramCreate_gatedEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructE22kalloc_type_view_30774
- __ZZN8H11ANEIn23ANE_ProgramCreate_gatedEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructE22kalloc_type_view_31204
- __ZZN8H11ANEIn23ANE_ProgramCreate_gatedEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructE22kalloc_type_view_31254
- __ZZN8H11ANEIn23ANE_ProgramCreate_gatedEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructE22kalloc_type_view_31270
- __ZZN8H11ANEIn23findClientByCodesigningEPhS0_PKcPP25H11ANEClientContextStructbE11_os_log_fmt
- __ZZN8H11ANEIn23findClientByCodesigningEPhS0_PKcPP25H11ANEClientContextStructbE11_os_log_fmt_0
- __ZZN8H11ANEIn23findClientByCodesigningEPhS0_PKcPP25H11ANEClientContextStructbE11_os_log_fmt_1
- __ZZN8H11ANEIn23findClientByCodesigningEPhS0_PKcPP25H11ANEClientContextStructbE11_os_log_fmt_2
- __ZZN8H11ANEIn23handleRequestCompletionEP25H11ANERequestParamsStructiE21kalloc_type_view_9073
- __ZZN8H11ANEIn23handleRequestCompletionEP25H11ANERequestParamsStructiE21kalloc_type_view_9077
- __ZZN8H11ANEIn23handleRequestCompletionEP25H11ANERequestParamsStructiE21kalloc_type_view_9081
- __ZZN8H11ANEIn23handleRequestCompletionEP25H11ANERequestParamsStructiE21kalloc_type_view_9119
- __ZZN8H11ANEIn23initializeANEPropertiesEvE21kalloc_type_view_4503
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt_0
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt_1
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt_2
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt_3
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt_4
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt_5
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt_6
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt_7
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt_8
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt_9
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__10_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__11_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__12_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__13_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__14_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__15_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__16_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__17_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__18_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__19_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__20_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__21_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__22_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__23_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__24_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__25_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__26_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__27_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__28_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__29_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__30_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__31_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__32_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__33_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__34_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__35_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE11_os_log_fmt__36_
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE22kalloc_type_view_42396
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE22kalloc_type_view_42399
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE22kalloc_type_view_42587
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE22kalloc_type_view_42590
- __ZZN8H11ANEIn26ANE_MemoryMapRequest_gatedEP27H11ANEMemoryMapParamsStructbE22kalloc_type_view_42767
- __ZZN8H11ANEIn26AllocateIntermediateBufferEyPP43H11ANEIntermediateBufferSurfaceParamsStructP31H11ANEProgramBufferParamsStructP25H11ANEProcessParamsStructybE21kalloc_type_view_2011
- __ZZN8H11ANEIn26AllocateIntermediateBufferEyPP43H11ANEIntermediateBufferSurfaceParamsStructP31H11ANEProgramBufferParamsStructP25H11ANEProcessParamsStructybE21kalloc_type_view_2028
- __ZZN8H11ANEIn26ReleaseProgramMemoryBufferEP31H11ANEProgramBufferParamsStructbE21kalloc_type_view_3448
- __ZZN8H11ANEIn26ReleaseProgramMemoryBufferEP31H11ANEProgramBufferParamsStructbE21kalloc_type_view_3510
- __ZZN8H11ANEIn26ReleaseProgramMemoryBufferEP31H11ANEProgramBufferParamsStructbE21kalloc_type_view_3514
- __ZZN8H11ANEIn26cleanupAllChainingMappingsEP34H11ANEChainingCacheReqParamsStructE22kalloc_type_view_31991
- __ZZN8H11ANEIn26cleanupAllChainingMappingsEP34H11ANEChainingCacheReqParamsStructE22kalloc_type_view_31996
- __ZZN8H11ANEIn26cleanupAllChainingMappingsEP34H11ANEChainingCacheReqParamsStructE22kalloc_type_view_32056
- __ZZN8H11ANEIn26cleanupAllChainingMappingsEP34H11ANEChainingCacheReqParamsStructE22kalloc_type_view_32071
- __ZZN8H11ANEIn27ANE_UserClientCleanup_gatedEPvbE11_os_log_fmt_9
- __ZZN8H11ANEIn27SendRequestToFirmware_gatedEP25H11ANERequestParamsStructP9IOSurfaceibbE22kalloc_type_view_35000
- __ZZN8H11ANEIn27SendRequestToFirmware_gatedEP25H11ANERequestParamsStructP9IOSurfaceibbE22kalloc_type_view_35004
- __ZZN8H11ANEIn27SendRequestToFirmware_gatedEP25H11ANERequestParamsStructP9IOSurfaceibbE22kalloc_type_view_35008
- __ZZN8H11ANEIn27SendRequestToFirmware_gatedEP25H11ANERequestParamsStructP9IOSurfaceibbE22kalloc_type_view_35046
- __ZZN8H11ANEIn28ANE_ProgramInputsReady_gatedEP29H11ANEInputBuffersReadyStructE22kalloc_type_view_33331
- __ZZN8H11ANEIn28processTargetToHostIOCommandEyyyE22kalloc_type_view_13289
- __ZZN8H11ANEIn28processTargetToHostIOCommandEyyyE22kalloc_type_view_13436
- __ZZN8H11ANEIn28processTargetToHostIOCommandEyyyE22kalloc_type_view_14254
- __ZZN8H11ANEIn28processTargetToHostIOCommandEyyyE22kalloc_type_view_14841
- __ZZN8H11ANEIn28processTargetToHostIOCommandEyyyE22kalloc_type_view_14845
- __ZZN8H11ANEIn28processTargetToHostIOCommandEyyyE22kalloc_type_view_14849
- __ZZN8H11ANEIn28processTargetToHostIOCommandEyyyE22kalloc_type_view_14868
- __ZZN8H11ANEIn29ANE_AddClientForProgram_gatedEPvP22H11ANEDeviceInfoStructP4taskE22kalloc_type_view_20014
- __ZZN8H11ANEIn29ANE_AddClientForProgram_gatedEPvP22H11ANEDeviceInfoStructP4taskE22kalloc_type_view_20039
- __ZZN8H11ANEIn29ANE_AddClientForProgram_gatedEPvP22H11ANEDeviceInfoStructP4taskE22kalloc_type_view_20048
- __ZZN8H11ANEIn29ANE_AddClientForProgram_gatedEPvP22H11ANEDeviceInfoStructP4taskE22kalloc_type_view_20061
- __ZZN8H11ANEIn29ANE_AddClientForProgram_gatedEPvP22H11ANEDeviceInfoStructP4taskE22kalloc_type_view_20071
- __ZZN8H11ANEIn29patchMutableInstanceProcedureEP25H11ANEProcessParamsStructjjP36H11ANEProgramInstanceProcedureStructiE22kalloc_type_view_33848
- __ZZN8H11ANEIn29patchMutableInstanceProcedureEP25H11ANEProcessParamsStructjjP36H11ANEProgramInstanceProcedureStructiE22kalloc_type_view_33983
- __ZZN8H11ANEIn30ANE_ProgramCreatePreprocessingEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructPP23ZinComputeProgramStructPP31H11ANEProgramBufferParamsStructP35H11ANEProgramCreateArgsStructOutputE22kalloc_type_view_27705
- __ZZN8H11ANEIn30ANE_ProgramCreatePreprocessingEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructPP23ZinComputeProgramStructPP31H11ANEProgramBufferParamsStructP35H11ANEProgramCreateArgsStructOutputE22kalloc_type_view_27763
- __ZZN8H11ANEIn30ANE_ProgramCreatePreprocessingEP29H11ANEProgramCreateArgsStructP45H11ANEProgramCreateArgsAdditionalParamsStructPP23ZinComputeProgramStructPP31H11ANEProgramBufferParamsStructP35H11ANEProgramCreateArgsStructOutputE22kalloc_type_view_27954
- __ZZN8H11ANEIn31ANE_MemoryMapStatsBuffers_gatedEP27H11ANEMemoryMapParamsStructE22kalloc_type_view_43139
- __ZZN8H11ANEIn32ANE_ProgramChainingPrepare_gatedEP33_H11ANEProgramChainingPrepareArgsP40H11ANEProgramChainingPrepareOutputStructE22kalloc_type_view_32568
- __ZZN8H11ANEIn32ANE_ProgramChainingPrepare_gatedEP33_H11ANEProgramChainingPrepareArgsP40H11ANEProgramChainingPrepareOutputStructE22kalloc_type_view_32704
- __ZZN8H11ANEIn32ANE_ProgramChainingPrepare_gatedEP33_H11ANEProgramChainingPrepareArgsP40H11ANEProgramChainingPrepareOutputStructE22kalloc_type_view_32705
- __ZZN8H11ANEIn33buildFirmwareChainingCacheRequestEP34H11ANEChainingCacheReqParamsStructP35H11ANEProgramCreateArgsStructOutputE22kalloc_type_view_32188
- __ZZN8H11ANEIn33deleteProgramChainingCacheRequestEPP34H11ANEChainingCacheReqParamsStructE22kalloc_type_view_31953
- __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE11_os_log_fmt__83_
- __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE11_os_log_fmt__84_
- __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40570
- __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40708
- __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40746
- __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40760
- __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40794
- __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_41443
- __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_41448
- __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_41495
- __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_41499
- __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_41503
- __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_42043
- __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_42047
- __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_42051
- __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_42085
- __ZZN8H11ANEIn34ANE_ProgramSendCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_42092
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_37196
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_37213
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_37222
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_37231
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_37240
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_37251
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_37273
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_37306
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_37307
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_37317
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_37327
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_39675
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_39697
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_39703
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_39744
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_39748
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_39752
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40440
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40444
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40448
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40509
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40516
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40522
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40528
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40534
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40541
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40544
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40547
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40550
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40553
- __ZZN8H11ANEIn36ANE_ProgramSendUnCachedRequest_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE22kalloc_type_view_40555
- __ZZN8H11ANEIn36patchClusterMutableInstanceProcedureEP25H11ANEProcessParamsStructjjP36H11ANEProgramInstanceProcedureStructPP13ANEDataBufferiE22kalloc_type_view_33680
- __ZZN8H11ANEIn36patchClusterMutableInstanceProcedureEP25H11ANEProcessParamsStructjjP36H11ANEProgramInstanceProcedureStructPP13ANEDataBufferiE22kalloc_type_view_33809
- __ZZN8H11ANEIn45ANE_PatchClusterProcessInstanceWeightsBuffersEP25H11ANEProcessParamsStructP33H11ANEProgramInstanceParamsStructP4taskE22kalloc_type_view_43750
- __ZZN8H11ANEIn45ANE_PatchClusterProcessInstanceWeightsBuffersEP25H11ANEProcessParamsStructP33H11ANEProgramInstanceParamsStructP4taskE22kalloc_type_view_44025
- __ZZN8H11ANEIn4stopEP9IOServiceE22kalloc_type_view_12199
- __ZZN8H11ANEIn4stopEP9IOServiceE22kalloc_type_view_12254
- __ZZN8H11ANEIn4stopEP9IOServiceE22kalloc_type_view_12257
- __ZZN8H11ANEIn51ANE_ProgramSendRequestInitialChecksAndLookups_gatedEP30H11ANEProgramRequestArgsStructP24H11ANESharedEventsStructP46H11ANEProgramSendRequestAdditionalParamsStructE11_os_log_fmt__27_
- __ZZZN13ANEDataBuffer9asyncWireEjEUb_E11_os_log_fmt
- __ZZZN13ANEDataBuffer9asyncWireEjEUb_E11_os_log_fmt_0
- __ZZZN13ANEDataBuffer9asyncWireEjEUb_E11_os_log_fmt_1
- __ZZZN8H11ANEIn26lookupProgramWithAssetPathEP12OSCollectionPKcPP31H11ANEProgramBufferParamsStructPP25H11ANEProcessParamsStructP5OSSetEUb2_E11_os_log_fmt
- __ZZZN8H11ANEIn26lookupProgramWithAssetPathEP12OSCollectionPKcPP31H11ANEProgramBufferParamsStructPP25H11ANEProcessParamsStructP5OSSetEUb2_E11_os_log_fmt_0
- __ZZZZN8H11ANEIn26lookupProgramWithAssetPathEP12OSCollectionPKcPP31H11ANEProgramBufferParamsStructPP25H11ANEProcessParamsStructP5OSSetEUb2_EUb3_E11_os_log_fmt
- __ZZZZN8H11ANEIn26lookupProgramWithAssetPathEP12OSCollectionPKcPP31H11ANEProgramBufferParamsStructPP25H11ANEProcessParamsStructP5OSSetEUb2_EUb3_E11_os_log_fmt_0
- __ZZZZN8H11ANEIn26lookupProgramWithAssetPathEP12OSCollectionPKcPP31H11ANEProgramBufferParamsStructPP25H11ANEProcessParamsStructP5OSSetEUb2_EUb3_E11_os_log_fmt_1
- __ZZZZN8H11ANEIn26lookupProgramWithAssetPathEP12OSCollectionPKcPP31H11ANEProgramBufferParamsStructPP25H11ANEProcessParamsStructP5OSSetEUb2_EUb3_E11_os_log_fmt_2
- __ZZZZN8H11ANEIn26lookupProgramWithAssetPathEP12OSCollectionPKcPP31H11ANEProgramBufferParamsStructPP25H11ANEProcessParamsStructP5OSSetEUb2_EUb3_E11_os_log_fmt_3
- __ZZZZN8H11ANEIn26lookupProgramWithAssetPathEP12OSCollectionPKcPP31H11ANEProgramBufferParamsStructPP25H11ANEProcessParamsStructP5OSSetEUb2_EUb3_E11_os_log_fmt_4
- __ZZZZN8H11ANEIn26lookupProgramWithAssetPathEP12OSCollectionPKcPP31H11ANEProgramBufferParamsStructPP25H11ANEProcessParamsStructP5OSSetEUb2_EUb3_E11_os_log_fmt_5
- __ZZZZN8H11ANEIn27HandleFirmwareTimeout_gatedEvEUb4_EUb5_E11_os_log_fmt
- ___ZN8H11ANEIn19setClientHint_gatedEP19ANEClientHintStruct_block_invoke.313
- ___ZN8H11ANEIn19setClientHint_gatedEP19ANEClientHintStruct_block_invoke.317
- ____ZN13ANEDataBuffer9asyncWireEj_block_invoke
- ____ZN13ANEDataBuffer9asyncWireEj_block_invoke_2
- ___chkstk_darwin
- ___chkstk_darwin_probe
- __block_descriptor_tmp.312
- __block_descriptor_tmp.316
- __block_descriptor_tmp.320
- __block_descriptor_tmp.323
- __block_descriptor_tmp.326
- __block_descriptor_tmp.337
- __block_descriptor_tmp.457
- __block_descriptor_tmp.488
- __block_descriptor_tmp.500
- __block_descriptor_tmp.501
- __block_descriptor_tmp.509
- __block_descriptor_tmp.510
- __block_descriptor_tmp.511
- __block_descriptor_tmp.524
- __block_descriptor_tmp.536
- __block_descriptor_tmp.537
- __block_descriptor_tmp.538
- __block_descriptor_tmp.539
- __cxx_global_var_init.2414
- __cxx_global_var_init.2415
- __cxx_global_var_init.2416
- __cxx_global_var_init.2417
- __cxx_global_var_init.2418
CStrings:
+ "ANE_ProgramCheckandPrewireBuffers_gated"
+ "ANE_unwireAllAutoPrewiredBuffers_gated"
+ "__KERN_"
+ "__kern_"
+ "freeAutoPrewiredBufferInfo"
+ "setClientHint"
+ "setClientHintInitialChecksAndLookups_gated"
+ "setClientHint_block_invoke"
+ "site.H11ANEBufferInfo *"
+ "site.OSObject *"

```

>  `com.apple.driver.AppleProResHW`

```diff

-400.59.1.0.0
-  __TEXT.__const: 0x1ae8
-  __TEXT.__os_log: 0x71db
-  __TEXT.__cstring: 0xde4
-  __TEXT_EXEC.__text: 0x187a4
+400.73.0.0.0
+  __TEXT.__const: 0x1b40
+  __TEXT.__os_log: 0x7363
+  __TEXT.__cstring: 0xdf9
+  __TEXT_EXEC.__text: 0x18d20
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x358
   __DATA.__common: 0x70

   __DATA_CONST.__const: 0x62c8
   __DATA_CONST.__kalloc_type: 0x380
   __DATA_CONST.__kalloc_var: 0xa0
-  Functions: 418
-  Symbols:   2264
-  CStrings:  163
+  Functions: 425
+  Symbols:   2278
+  CStrings:  164
 
Symbols:
+ __ZL24ProResPerfStateInfoTable
+ __ZN13AppleProResHW10addElementEP13SlidingWindowd
+ __ZN13AppleProResHW10freeWindowEP13SlidingWindow
+ __ZN13AppleProResHW10getAverageEP13SlidingWindow
+ __ZN13AppleProResHW10initWindowEy
+ __ZN13AppleProResHW16releaseCoreGatedEv
+ __ZN13AppleProResHW17deletePrevElementEP13SlidingWindow
+ __ZN13AppleProResHW19getDynamicPerfStateEP16UserClientInfo_sddj
+ __ZN13AppleProResHW8getTotalEP13SlidingWindow
+ __ZZN13AppleProResHW11EncodeFrameEP9IOServicePvE11_os_log_fmt__13_
+ __ZZN13AppleProResHW12attachClientEP9IOServicePvP4taskE21kalloc_type_view_5462
+ __ZZN13AppleProResHW12attachClientEP9IOServicePvP4taskE21kalloc_type_view_5595
+ __ZZN13AppleProResHW12detachClientEP9IOServiceE21kalloc_type_view_5856
+ __ZZN13AppleProResHW12timerHandlerEP18IOTimerEventSourceE11_os_log_fmt__12_
+ __ZZN13AppleProResHW12timerHandlerEP18IOTimerEventSourceE11_os_log_fmt__13_
+ __ZZN13AppleProResHW16acquireCoreGatedEvE11_os_log_fmt_4
+ __ZZN13AppleProResHW16acquireCoreGatedEvE11_os_log_fmt_5
+ __ZZN13AppleProResHW16attachTestClientEP9IOServicePvP4taskE21kalloc_type_view_5399
+ __ZZN13AppleProResHW16attachTestClientEP9IOServicePvP4taskE21kalloc_type_view_5436
+ __ZZN13AppleProResHW16detachTestClientEP9IOServiceE21kalloc_type_view_5761
+ __ZZN13AppleProResHW16releaseCoreGatedEvE11_os_log_fmt
+ __ZZN13AppleProResHW19delayListClearGatedEjjE21kalloc_type_view_6101
+ __ZZN13AppleProResHW19delayListClearGatedEjjE21kalloc_type_view_6102
+ __ZZN13AppleProResHW19getDynamicPerfStateEP16UserClientInfo_sddjE11_os_log_fmt
+ __ZZN13AppleProResHW19getDynamicPerfStateEP16UserClientInfo_sddjE11_os_log_fmt_0
+ __ZZN13AppleProResHW19getDynamicPerfStateEP16UserClientInfo_sddjE11_os_log_fmt_1
+ __ZZN13AppleProResHW19getDynamicPerfStateEP16UserClientInfo_sddjE11_os_log_fmt_2
+ __ZZN13AppleProResHW19getDynamicPerfStateEP16UserClientInfo_sddjE11_os_log_fmt_3
+ __ZZN13AppleProResHW24unMapBufferWithDARTGatedEP15ProResBufInfo_sjjE21kalloc_type_view_5072
+ __ZZN13AppleProResHW24unMapBufferWithDARTGatedEP15ProResBufInfo_sjjE21kalloc_type_view_5075
- __ZN13AppleProResHW19getDynamicPerfStateEP16UserClientInfo_s15ProResPerfStateS2_ff
- __ZZN13AppleProResHW12attachClientEP9IOServicePvP4taskE21kalloc_type_view_5420
- __ZZN13AppleProResHW12attachClientEP9IOServicePvP4taskE21kalloc_type_view_5553
- __ZZN13AppleProResHW12detachClientEP9IOServiceE21kalloc_type_view_5804
- __ZZN13AppleProResHW16attachTestClientEP9IOServicePvP4taskE21kalloc_type_view_5357
- __ZZN13AppleProResHW16attachTestClientEP9IOServicePvP4taskE21kalloc_type_view_5394
- __ZZN13AppleProResHW16detachTestClientEP9IOServiceE21kalloc_type_view_5714
- __ZZN13AppleProResHW19delayListClearGatedEjjE21kalloc_type_view_6049
- __ZZN13AppleProResHW19delayListClearGatedEjjE21kalloc_type_view_6050
- __ZZN13AppleProResHW19getDynamicPerfStateEP16UserClientInfo_s15ProResPerfStateS2_ffE11_os_log_fmt
- __ZZN13AppleProResHW19getDynamicPerfStateEP16UserClientInfo_s15ProResPerfStateS2_ffE11_os_log_fmt_0
- __ZZN13AppleProResHW19getDynamicPerfStateEP16UserClientInfo_s15ProResPerfStateS2_ffE11_os_log_fmt_1
- __ZZN13AppleProResHW19getDynamicPerfStateEP16UserClientInfo_s15ProResPerfStateS2_ffE11_os_log_fmt_2
- __ZZN13AppleProResHW19getDynamicPerfStateEP16UserClientInfo_s15ProResPerfStateS2_ffE11_os_log_fmt_3
- __ZZN13AppleProResHW24unMapBufferWithDARTGatedEP15ProResBufInfo_sjjE21kalloc_type_view_5030
- __ZZN13AppleProResHW24unMapBufferWithDARTGatedEP15ProResBufInfo_sjjE21kalloc_type_view_5033
CStrings:
+ "1211111212221212112211112111111211111121111112112222111122222111121111112111111211111121111111111111111111111121121121121111111111111111111111111111111111111111122222222222222222111111122221111111111112122"
+ "211111121121112222222122"
+ "releaseCoreGated"
- "121111121222121211221111211111121111112111111211222211112222211112111111211111121111112111111111111111111111112112112112111111111111111111111111111111111111111112222222222222222111111122221111111111112122"
- "211111121121112222222"

```

>  `com.apple.iokit.IOSurface`

```diff

-368.0.2.0.0
-  __TEXT.__cstring: 0x4ea5
+368.0.4.0.0
+  __TEXT.__cstring: 0x4eb9
   __TEXT.__const: 0x48
-  __TEXT.__os_log: 0x46c
-  __TEXT_EXEC.__text: 0x2dfa4
+  __TEXT.__os_log: 0x43b
+  __TEXT_EXEC.__text: 0x2e0b4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x178
   __DATA.__common: 0x3e8
-  __DATA.__bss: 0x28
-  __DATA_CONST.__auth_got: 0x480
+  __DATA.__bss: 0x38
+  __DATA_CONST.__auth_got: 0x490
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__mod_init_func: 0x78
   __DATA_CONST.__mod_term_func: 0x78
   __DATA_CONST.__const: 0x6450
   __DATA_CONST.__kalloc_type: 0xb80
   __DATA_CONST.__kalloc_var: 0x8c0
-  Functions: 1197
-  Symbols:   2037
-  CStrings:  490
+  Functions: 1199
+  Symbols:   2044
+  CStrings:  492
 
Symbols:
+ __ZL30IOSurfaceViolateUseCountChangebPKcjjj
+ __ZN9IOSurface21clear_data_propertiesEv
+ __ZZL12alloc_sharedPP25_IOSurfaceSharedListEntryjmjPjPPvE21kalloc_type_view_1918
+ __ZZL12alloc_sharedPP25_IOSurfaceSharedListEntryjmjPjPPvE21kalloc_type_view_1932
+ __ZZL12alloc_sharedPP25_IOSurfaceSharedListEntryjmjPjPPvE21kalloc_type_view_1956
+ __ZZL12alloc_sharedPP25_IOSurfaceSharedListEntryjmjPjPPvE21kalloc_type_view_1965
+ __ZZL30IOSurfaceViolateUseCountChangebPKcjjjE11_os_log_fmt
+ __ZZN13IOSurfaceRoot11free_sharedEvE21kalloc_type_view_2078
+ __ZZN13IOSurfaceRoot11free_sharedEvE21kalloc_type_view_2090
+ __ZZN13IOSurfaceRoot11free_sharedEvE21kalloc_type_view_2102
+ __ZZN13IOSurfaceRoot12free_handlesEvE21kalloc_type_view_1615
+ __ZZN13IOSurfaceRoot13alloc_handlesEvE21kalloc_type_view_1577
+ __ZZN13IOSurfaceRoot13alloc_handlesEvE21kalloc_type_view_1596
+ __ZZN13IOSurfaceRoot14client_startedEP23IOSurfaceRootUserClientP4taskE21kalloc_type_view_2757
+ __ZZN13IOSurfaceRoot14client_startedEP23IOSurfaceRootUserClientP4taskE21kalloc_type_view_2767
+ __ZZN13IOSurfaceRoot16setSurfaceNotifyEPyP19IOSurfaceNotifyArgsP23IOSurfaceRootUserClientE21kalloc_type_view_1340
+ __ZZN13IOSurfaceRoot19removeSurfaceNotifyEP19IOSurfaceNotifyArgsP23IOSurfaceRootUserClientE21kalloc_type_view_1386
+ __ZZN13IOSurfaceRoot22addEventNotifierClientEPFvP8OSObjectES1_E21kalloc_type_view_2703
+ __ZZN13IOSurfaceRoot25free_shared_event_handlesEvE21kalloc_type_view_1783
+ __ZZN13IOSurfaceRoot25removeEventNotifierClientEP28IOSurfaceEventNotifierClientE21kalloc_type_view_2733
+ __ZZN13IOSurfaceRoot26alloc_shared_event_handlesEvE21kalloc_type_view_1745
+ __ZZN13IOSurfaceRoot26alloc_shared_event_handlesEvE21kalloc_type_view_1764
+ __ZZN13IOSurfaceRoot26removeSurfaceNotificationsEP23IOSurfaceRootUserClientE21kalloc_type_view_1434
+ __ZZN9IOSurface12setPurgeableEjPjE21kalloc_type_view_3207
+ __ZZN9IOSurface12setPurgeableEjPjE21kalloc_type_view_3385
+ __ZZN9IOSurface12setPurgeableEjPjE21kalloc_type_view_3427
+ __ZZN9IOSurface12setPurgeableEjPjE21kalloc_type_view_3476
+ __ZZN9IOSurface16parse_propertiesEP12OSDictionaryE21kalloc_type_view_1001
+ __ZZN9IOSurface16parse_propertiesEP12OSDictionaryE21kalloc_type_view_2399
+ __ZZN9IOSurface19trace_current_fenceEP7IOFenceE21kalloc_type_view_5439
+ __ZZN9IOSurface25synchronize_device_cachesEjjbE21kalloc_type_view_2907
+ __ZZN9IOSurface25synchronize_device_cachesEjjbE21kalloc_type_view_2929
+ __ZZN9IOSurface32decrement_use_count_for_categoryEjE11_creatorPID
+ __ZZN9IOSurface32decrement_use_count_for_categoryEjE11_currentPID
+ __ZZN9IOSurface32increment_use_count_for_categoryEjE11_creatorPID
+ __ZZN9IOSurface32increment_use_count_for_categoryEjE11_currentPID
+ __ZZN9IOSurface4freeEvE20kalloc_type_view_541
+ __ZZN9IOSurface4freeEvE20kalloc_type_view_561
+ __ZZN9IOSurface8finalizeEvE20kalloc_type_view_456
+ __block_descriptor_tmp.255
+ _proc_rele
+ _proc_self
- __ZZL12alloc_sharedPP25_IOSurfaceSharedListEntryjmjPjPPvE21kalloc_type_view_1924
- __ZZL12alloc_sharedPP25_IOSurfaceSharedListEntryjmjPjPPvE21kalloc_type_view_1938
- __ZZL12alloc_sharedPP25_IOSurfaceSharedListEntryjmjPjPPvE21kalloc_type_view_1962
- __ZZL12alloc_sharedPP25_IOSurfaceSharedListEntryjmjPjPPvE21kalloc_type_view_1971
- __ZZN13IOSurfaceRoot11free_sharedEvE21kalloc_type_view_2084
- __ZZN13IOSurfaceRoot11free_sharedEvE21kalloc_type_view_2096
- __ZZN13IOSurfaceRoot11free_sharedEvE21kalloc_type_view_2108
- __ZZN13IOSurfaceRoot12free_handlesEvE21kalloc_type_view_1621
- __ZZN13IOSurfaceRoot13alloc_handlesEvE21kalloc_type_view_1583
- __ZZN13IOSurfaceRoot13alloc_handlesEvE21kalloc_type_view_1602
- __ZZN13IOSurfaceRoot14client_startedEP23IOSurfaceRootUserClientP4taskE21kalloc_type_view_2763
- __ZZN13IOSurfaceRoot14client_startedEP23IOSurfaceRootUserClientP4taskE21kalloc_type_view_2773
- __ZZN13IOSurfaceRoot16setSurfaceNotifyEPyP19IOSurfaceNotifyArgsP23IOSurfaceRootUserClientE21kalloc_type_view_1346
- __ZZN13IOSurfaceRoot19removeSurfaceNotifyEP19IOSurfaceNotifyArgsP23IOSurfaceRootUserClientE21kalloc_type_view_1392
- __ZZN13IOSurfaceRoot22addEventNotifierClientEPFvP8OSObjectES1_E21kalloc_type_view_2709
- __ZZN13IOSurfaceRoot25free_shared_event_handlesEvE21kalloc_type_view_1789
- __ZZN13IOSurfaceRoot25removeEventNotifierClientEP28IOSurfaceEventNotifierClientE21kalloc_type_view_2739
- __ZZN13IOSurfaceRoot26alloc_shared_event_handlesEvE21kalloc_type_view_1751
- __ZZN13IOSurfaceRoot26alloc_shared_event_handlesEvE21kalloc_type_view_1770
- __ZZN13IOSurfaceRoot26removeSurfaceNotificationsEP23IOSurfaceRootUserClientE21kalloc_type_view_1440
- __ZZN9IOSurface12setPurgeableEjPjE21kalloc_type_view_3200
- __ZZN9IOSurface12setPurgeableEjPjE21kalloc_type_view_3378
- __ZZN9IOSurface12setPurgeableEjPjE21kalloc_type_view_3420
- __ZZN9IOSurface12setPurgeableEjPjE21kalloc_type_view_3469
- __ZZN9IOSurface16parse_propertiesEP12OSDictionaryE20kalloc_type_view_994
- __ZZN9IOSurface16parse_propertiesEP12OSDictionaryE21kalloc_type_view_2392
- __ZZN9IOSurface19trace_current_fenceEP7IOFenceE21kalloc_type_view_5400
- __ZZN9IOSurface25synchronize_device_cachesEjjbE21kalloc_type_view_2900
- __ZZN9IOSurface25synchronize_device_cachesEjjbE21kalloc_type_view_2922
- __ZZN9IOSurface32decrement_use_count_for_categoryEjE11_os_log_fmt
- __ZZN9IOSurface32increment_use_count_for_categoryEjE11_os_log_fmt
- __ZZN9IOSurface4freeEvE20kalloc_type_view_534
- __ZZN9IOSurface4freeEvE20kalloc_type_view_554
- __ZZN9IOSurface8finalizeEvE20kalloc_type_view_451
- __block_descriptor_tmp.251
CStrings:
+ "decrement"
+ "increment"

```

</details>

## MachO

### 🆕 NEW (32)

<details>
  <summary><i>View NEW</i></summary>

- `/System/Library/Extensions/AMDShared.bundle/Contents/MacOS/AMDShared`
- `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/UtilityExtension.appex/Contents/MacOS/UtilityExtension`
- `/System/Library/PrivateFrameworks/ApplePDPHelper.framework/Versions/A/ApplePDPHelper`
- `/System/Library/PrivateFrameworks/FeedbackService.framework/Versions/A/Support/FeedbackRemoteView.app/Contents/MacOS/FeedbackRemoteView`
- `/System/Library/PrivateFrameworks/HelloWorldMacHelper.framework/Versions/A/HelloWorldMacHelper`
- `/System/Library/PrivateFrameworks/ImagePlayground.framework/Versions/A/PlugIns/com.apple.ImagePlayground.DiagnosticExtension.appex/Contents/MacOS/com.apple.ImagePlayground.DiagnosticExtension`
- `/System/Library/PrivateFrameworks/PlugInKitDaemon.framework/Versions/A/PlugInKitDaemon`
- `/System/Library/PrivateFrameworks/SafariFoundation.framework/Versions/A/XPCServices/CredentialProviderExtensionHelper.xpc/Contents/MacOS/CredentialProviderExtensionHelper`
- `/System/Library/PrivateFrameworks/SafariFoundation.framework/Versions/A/XPCServices/SafariConfigurationSubscriber.xpc/Contents/MacOS/SafariConfigurationSubscriber`
- `/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper`
- `/System/Library/PrivateFrameworks/SafariShared.framework/Versions/A/XPCServices/com.apple.Safari.CredentialExtractionHelper.xpc/Contents/MacOS/com.apple.Safari.CredentialExtractionHelper`
- `/System/Library/PrivateFrameworks/SafariShared.framework/Versions/A/XPCServices/com.apple.Safari.SearchHelper.xpc/Contents/MacOS/com.apple.Safari.SearchHelper`
- `/System/Library/PrivateFrameworks/VisualIntelligenceStream.framework/Versions/A/VisualIntelligenceStream`
- `/System/Library/PrivateFrameworks/WebDriver.framework/Versions/A/XPCServices/com.apple.WebDriver.HTTPService.xpc/Contents/MacOS/com.apple.WebDriver.HTTPService`
- `/System/iOSSupport/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/UtilityExtension.appex/Contents/MacOS/UtilityExtension`
- `/tmp/090-49769-068.dmg.mount/System/Library/PrivateFrameworks/SafariFoundation.framework/Versions/A/XPCServices/CredentialProviderExtensionHelper.xpc/Contents/MacOS/CredentialProviderExtensionHelper`
- `/tmp/090-49769-068.dmg.mount/System/Library/PrivateFrameworks/SafariFoundation.framework/Versions/A/XPCServices/SafariConfigurationSubscriber.xpc/Contents/MacOS/SafariConfigurationSubscriber`
- `/tmp/090-49769-068.dmg.mount/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper`
- `/tmp/090-49769-068.dmg.mount/System/Library/PrivateFrameworks/SafariShared.framework/Versions/A/XPCServices/com.apple.Safari.CredentialExtractionHelper.xpc/Contents/MacOS/com.apple.Safari.CredentialExtractionHelper`
- `/tmp/090-49769-068.dmg.mount/System/Library/PrivateFrameworks/SafariShared.framework/Versions/A/XPCServices/com.apple.Safari.SearchHelper.xpc/Contents/MacOS/com.apple.Safari.SearchHelper`
- `/tmp/090-49769-068.dmg.mount/System/Library/PrivateFrameworks/WebDriver.framework/Versions/A/XPCServices/com.apple.WebDriver.HTTPService.xpc/Contents/MacOS/com.apple.WebDriver.HTTPService`
- `/tmp/090-49769-068.dmg.mount/System/iOSSupport/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc`
- `/tmp/090-49769-068.dmg.mount/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.GPU.xpc/Contents/MacOS/com.apple.WebKit.GPU`
- `/tmp/090-49769-068.dmg.mount/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.GPU.xpc/Contents/PlugIns/MediaFormatReader.bundle/Contents/MacOS/MediaFormatReader`
- `/tmp/090-49769-068.dmg.mount/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.Networking.xpc/Contents/MacOS/com.apple.WebKit.Networking`
- `/tmp/090-49769-068.dmg.mount/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.CaptivePortal.xpc/Contents/MacOS/com.apple.WebKit.WebContent.CaptivePortal`
- `/tmp/090-49769-068.dmg.mount/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.CaptivePortal.xpc/Contents/PlugIns/MediaFormatReader.bundle/Contents/MacOS/MediaFormatReader`
- `/tmp/090-49769-068.dmg.mount/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.Development.xpc/Contents/MacOS/com.apple.WebKit.WebContent.Development`
- `/tmp/090-49769-068.dmg.mount/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.Development.xpc/Contents/PlugIns/MediaFormatReader.bundle/Contents/MacOS/MediaFormatReader`
- `/tmp/090-49769-068.dmg.mount/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.xpc/Contents/MacOS/com.apple.WebKit.WebContent`
- `/tmp/090-49769-068.dmg.mount/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.xpc/Contents/PlugIns/MediaFormatReader.bundle/Contents/MacOS/MediaFormatReader`
- `/usr/sbin/shareddspd`

</details>

### ❌ Removed (26)

- `/System/Library/Extensions/AppleIntelKBLGraphicsMTLDriver.bundle/Contents/MacOS/AppleIntelKBLGraphicsMTLDriver`
- `/System/Library/Frameworks/AuthenticationServices.framework/Versions/A/XPCServices/com.apple.AuthenticationServices.Helper.xpc/Contents/MacOS/com.apple.AuthenticationServices.Helper`
- `/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc`
- `/System/Library/Frameworks/OpenCL.framework/Versions/A/Libraries/3425AMD/libcl2module.dylib`
- `/System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/3425AMD/libLLVMContainer.dylib`
- `/System/Library/Frameworks/SafariServices.framework/Versions/A/XPCServices/com.apple.SafariServices.ExtensionHelper.xpc/Contents/MacOS/com.apple.SafariServices.ExtensionHelper`
- `/System/Library/Frameworks/SafariServices.framework/Versions/A/XPCServices/com.apple.SafariServices.xpc/Contents/MacOS/com.apple.SafariServices`
- `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/UtilityExtension_macOS.appex/Contents/MacOS/UtilityExtension_macOS`
- `/System/Library/PrivateFrameworks/ImageGenerationUI.framework/Versions/A/PlugIns/com.apple.ImageGenerationUI.DiagnosticExtension.appex/Contents/MacOS/com.apple.ImageGenerationUI.DiagnosticExtension`
- `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/Versions/A/XPCServices/ModelCatalogCompilationService.xpc/Contents/MacOS/ModelCatalogCompilationService`
- `/System/iOSSupport/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/UtilityExtension_catalyst.appex/Contents/MacOS/UtilityExtension_catalyst`
- `/tmp/090-49769-058.dmg.mount/System/Library/Frameworks/AuthenticationServices.framework/Versions/A/XPCServices/com.apple.AuthenticationServices.Helper.xpc/Contents/MacOS/com.apple.AuthenticationServices.Helper`
- `/tmp/090-49769-058.dmg.mount/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc`
- `/tmp/090-49769-058.dmg.mount/System/Library/Frameworks/SafariServices.framework/Versions/A/XPCServices/com.apple.SafariServices.ExtensionHelper.xpc/Contents/MacOS/com.apple.SafariServices.ExtensionHelper`
- `/tmp/090-49769-058.dmg.mount/System/Library/Frameworks/SafariServices.framework/Versions/A/XPCServices/com.apple.SafariServices.xpc/Contents/MacOS/com.apple.SafariServices`
- `/tmp/090-49769-058.dmg.mount/System/iOSSupport/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc`
- `/tmp/090-49769-058.dmg.mount/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.GPU.xpc/Contents/MacOS/com.apple.WebKit.GPU`
- `/tmp/090-49769-058.dmg.mount/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.GPU.xpc/Contents/PlugIns/MediaFormatReader.bundle/Contents/MacOS/MediaFormatReader`
- `/tmp/090-49769-058.dmg.mount/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.Networking.xpc/Contents/MacOS/com.apple.WebKit.Networking`
- `/tmp/090-49769-058.dmg.mount/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.CaptivePortal.xpc/Contents/MacOS/com.apple.WebKit.WebContent.CaptivePortal`
- `/tmp/090-49769-058.dmg.mount/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.CaptivePortal.xpc/Contents/PlugIns/MediaFormatReader.bundle/Contents/MacOS/MediaFormatReader`
- `/tmp/090-49769-058.dmg.mount/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.Development.xpc/Contents/MacOS/com.apple.WebKit.WebContent.Development`
- `/tmp/090-49769-058.dmg.mount/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.Development.xpc/Contents/PlugIns/MediaFormatReader.bundle/Contents/MacOS/MediaFormatReader`
- `/tmp/090-49769-058.dmg.mount/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.xpc/Contents/MacOS/com.apple.WebKit.WebContent`
- `/tmp/090-49769-058.dmg.mount/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.xpc/Contents/PlugIns/MediaFormatReader.bundle/Contents/MacOS/MediaFormatReader`
- `/usr/libexec/silhouette`

### ⬆️ Updated (980)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Applications/App Store.app/Contents/MacOS/App Store](MACHOS/App_Store.md)
- [/System/Applications/Books.app/Contents/Frameworks/AEBookPlugins.framework/Versions/A/AEBookPlugins](MACHOS/AEBookPlugins.md)
- [/System/Applications/Books.app/Contents/Frameworks/BKLibrary.framework/Versions/A/BKLibrary](MACHOS/BKLibrary.md)
- [/System/Applications/Books.app/Contents/Frameworks/BlissReader.framework/Versions/A/BlissReader](MACHOS/BlissReader.md)
- [/System/Applications/Books.app/Contents/Frameworks/BookAnalytics.framework/Versions/A/BookAnalytics](MACHOS/BookAnalytics.md)
- [/System/Applications/Books.app/Contents/Frameworks/BookCore.framework/Versions/A/BookCore](MACHOS/BookCore.md)
- [/System/Applications/Books.app/Contents/Frameworks/BookEPUB.framework/Versions/A/BookEPUB](MACHOS/BookEPUB.md)
- [/System/Applications/Books.app/Contents/Frameworks/BookStoreUI.framework/Versions/A/BookStoreUI](MACHOS/BookStoreUI.md)
- [/System/Applications/Books.app/Contents/Frameworks/BooksPersonalization.framework/Versions/A/BooksPersonalization](MACHOS/BooksPersonalization.md)
- [/System/Applications/Books.app/Contents/Frameworks/BooksUI.framework/Versions/A/BooksUI](MACHOS/BooksUI.md)
- [/System/Applications/Books.app/Contents/Frameworks/JSApp.framework/Versions/A/JSApp](MACHOS/JSApp.md)
- [/System/Applications/Books.app/Contents/Frameworks/TemplateUI.framework/Versions/A/TemplateUI](MACHOS/TemplateUI.md)
- [/System/Applications/Books.app/Contents/MacOS/Books](MACHOS/Books.md)
- [/System/Applications/Books.app/Contents/PlugIns/BookEPUBWebProcessPlugin.bundle/Contents/MacOS/BookEPUBWebProcessPlugin](MACHOS/BookEPUBWebProcessPlugin.md)
- [/System/Applications/Calculator.app/Contents/MacOS/Calculator](MACHOS/Calculator.md)
- [/System/Applications/Calendar.app/Contents/MacOS/Calendar](MACHOS/Calendar.md)
- [/System/Applications/Clock.app/Contents/MacOS/Clock](MACHOS/Clock.md)
- [/System/Applications/Clock.app/Contents/PlugIns/WorldClockWidget.appex/Contents/MacOS/WorldClockWidget](MACHOS/WorldClockWidget.md)
- [/System/Applications/FaceTime.app/Contents/Frameworks/FaceTimeMac.framework/Versions/A/FaceTimeMac](MACHOS/FaceTimeMac.md)
- [/System/Applications/FaceTime.app/Contents/Frameworks/FaceTimeSettingsUI.framework/Versions/A/FaceTimeSettingsUI](MACHOS/FaceTimeSettingsUI.md)
- [/System/Applications/FaceTime.app/Contents/MacOS/FaceTime](MACHOS/FaceTime.md)
- [/System/Applications/FaceTime.app/Contents/PlugIns/FaceTimeMacHelper.bundle/Contents/MacOS/FaceTimeMacHelper](MACHOS/FaceTimeMacHelper.md)
- [/System/Applications/FindMy.app/Contents/Frameworks/FindMyAppCore.framework/Versions/A/FindMyAppCore](MACHOS/FindMyAppCore.md)
- [/System/Applications/FindMy.app/Contents/MacOS/FindMy](MACHOS/FindMy.md)
- [/System/Applications/FindMy.app/Contents/PlugIns/FindMyNotificationsService.appex/Contents/MacOS/FindMyNotificationsService](MACHOS/FindMyNotificationsService.md)
- [/System/Applications/FindMy.app/Contents/PlugIns/FindMyWidgetItems.appex/Contents/MacOS/FindMyWidgetItems](MACHOS/FindMyWidgetItems.md)
- [/System/Applications/Font Book.app/Contents/MacOS/Font Book](MACHOS/Font_Book.md)
- [/System/Applications/Freeform.app/Contents/Extensions/USDRendererExtension.appex/Contents/MacOS/USDRendererExtension](MACHOS/USDRendererExtension.md)
- [/System/Applications/Freeform.app/Contents/MacOS/Freeform](MACHOS/Freeform.md)
- [/System/Applications/Freeform.app/Contents/PlugIns/FreeformSharingExtension.appex/Contents/MacOS/FreeformSharingExtension](MACHOS/FreeformSharingExtension.md)
- [/System/Applications/Home.app/Contents/MacOS/Home](MACHOS/Home.md)
- [/System/Applications/Home.app/Contents/PlugIns/HomeEnergyWidgetsExtension.appex/Contents/MacOS/HomeEnergyWidgetsExtension](MACHOS/HomeEnergyWidgetsExtension.md)
- [/System/Applications/Home.app/Contents/PlugIns/HomeWidget.appex/Contents/MacOS/HomeWidget](MACHOS/HomeWidget.md)
- [/System/Applications/Image Playground.app/Contents/Extensions/GenerativePlaygroundAppIntents.appex/Contents/MacOS/GenerativePlaygroundAppIntents](MACHOS/GenerativePlaygroundAppIntents.md)
- [/System/Applications/Image Playground.app/Contents/MacOS/Image Playground](MACHOS/Image_Playground.md)
- [/System/Applications/Image Playground.app/Contents/PlugIns/GenerativePlaygroundMessagesAppExtension.appex/Contents/MacOS/GenerativePlaygroundMessagesAppExtension](MACHOS/GenerativePlaygroundMessagesAppExtension.md)
- [/System/Applications/Maps.app/Contents/MacOS/Maps](MACHOS/Maps.md)
- [/System/Applications/Maps.app/Contents/PlugIns/MapsAppKitBundle.bundle/Contents/MacOS/MapsAppKitBundle](MACHOS/MapsAppKitBundle.md)
- [/System/Applications/Messages.app/Contents/MacOS/Messages](MACHOS/Messages.md)
- [/System/Applications/Messages.app/Contents/PlugIns/Messages Reply Extension.appex/Contents/MacOS/Messages Reply Extension](MACHOS/Messages_Reply_Extension.md)
- [/System/Applications/Messages.app/Contents/PlugIns/Messages Share Extension.appex/Contents/MacOS/Messages Share Extension](MACHOS/Messages_Share_Extension.md)
- [/System/Applications/Messages.app/Contents/PlugIns/MessagesAppKitBridge.bundle/Contents/MacOS/MessagesAppKitBridge](MACHOS/MessagesAppKitBridge.md)
- [/System/Applications/Music.app/Contents/MacOS/Music](MACHOS/Music.md)
- [/System/Applications/Music.app/Contents/PlugIns/MusicCacheExtension.appex/Contents/MacOS/MusicCacheExtension](MACHOS/MusicCacheExtension.md)
- [/System/Applications/Music.app/Contents/PlugIns/MusicStorageExtension.appex/Contents/MacOS/MusicStorageExtension](MACHOS/MusicStorageExtension.md)
- [/System/Applications/Music.app/Contents/PlugIns/com.apple.Music.web.bundle/Contents/MacOS/com.apple.Music.web](MACHOS/com.apple.Music.web.md)
- [/System/Applications/News.app/Contents/MacOS/News](MACHOS/News.md)
- [/System/Applications/News.app/Contents/PlugIns/NewsToday2.appex/Contents/MacOS/NewsToday2](MACHOS/NewsToday2.md)
- [/System/Applications/News.app/Contents/PlugIns/NewsTodayIntents.appex/Contents/MacOS/NewsTodayIntents](MACHOS/NewsTodayIntents.md)
- [/System/Applications/Notes.app/Contents/MacOS/Notes](MACHOS/Notes.md)
- [/System/Applications/Notes.app/Contents/PlugIns/com.apple.Notes.IntentsExtension.appex/Contents/MacOS/com.apple.Notes.IntentsExtension](MACHOS/com.apple.Notes.IntentsExtension.md)
- [/System/Applications/Notes.app/Contents/PlugIns/com.apple.Notes.QuickLookExtension.appex/Contents/MacOS/com.apple.Notes.QuickLookExtension](MACHOS/com.apple.Notes.QuickLookExtension.md)
- [/System/Applications/Notes.app/Contents/PlugIns/com.apple.Notes.SharingExtension.appex/Contents/MacOS/com.apple.Notes.SharingExtension](MACHOS/com.apple.Notes.SharingExtension.md)
- [/System/Applications/Notes.app/Contents/PlugIns/com.apple.Notes.WidgetExtension.appex/Contents/MacOS/com.apple.Notes.WidgetExtension](MACHOS/com.apple.Notes.WidgetExtension.md)
- [/System/Applications/Passwords.app/Contents/Library/LoginItems/PasswordsMenuBarExtra.app/Contents/MacOS/PasswordsMenuBarExtra](MACHOS/PasswordsMenuBarExtra.md)
- [/System/Applications/Passwords.app/Contents/MacOS/Passwords](MACHOS/Passwords.md)
- [/System/Applications/Photos.app/Contents/MacOS/Photos](MACHOS/Photos.md)
- [/System/Applications/Photos.app/Contents/PlugIns/PhotosFileProvider.appex/Contents/MacOS/PhotosFileProvider](MACHOS/PhotosFileProvider.md)
- [/System/Applications/Photos.app/Contents/PlugIns/PhotosReliveWidget.appex/Contents/MacOS/PhotosReliveWidget](MACHOS/PhotosReliveWidget.md)
- [/System/Applications/Podcasts.app/Contents/Frameworks/IMDebug.framework/Versions/A/IMDebug](MACHOS/IMDebug.md)
- [/System/Applications/Podcasts.app/Contents/Frameworks/NowPlayingUI.framework/Versions/A/NowPlayingUI](MACHOS/NowPlayingUI.md)
- [/System/Applications/Podcasts.app/Contents/Frameworks/ShelfKit.framework/Versions/A/ShelfKit](MACHOS/ShelfKit.md)
- [/System/Applications/Podcasts.app/Contents/Frameworks/ShelfKitCollectionViews.framework/Versions/A/ShelfKitCollectionViews](MACHOS/ShelfKitCollectionViews.md)
- [/System/Applications/Podcasts.app/Contents/MacOS/Podcasts](MACHOS/Podcasts.md)
- [/System/Applications/Preview.app/Contents/MacOS/Preview](MACHOS/Preview.md)
- [/System/Applications/Reminders.app/Contents/MacOS/Reminders](MACHOS/Reminders.md)
- [/System/Applications/Reminders.app/Contents/PlugIns/RemindersSharingExtension.appex/Contents/MacOS/RemindersSharingExtension](MACHOS/RemindersSharingExtension.md)
- [/System/Applications/Reminders.app/Contents/PlugIns/RemindersWidgetExtension.appex/Contents/MacOS/RemindersWidgetExtension](MACHOS/RemindersWidgetExtension.md)
- [/System/Applications/Shortcuts.app/Contents/MacOS/Shortcuts](MACHOS/Shortcuts.md)
- [/System/Applications/Shortcuts.app/Contents/PlugIns/ShortcutsWidgetExtension.appex/Contents/MacOS/ShortcutsWidgetExtension](MACHOS/ShortcutsWidgetExtension.md)
- [/System/Applications/Stocks.app/Contents/PlugIns/StocksWidget.appex/Contents/MacOS/StocksWidget](MACHOS/StocksWidget.md)
- [/System/Applications/System Settings.app/Contents/MacOS/System Settings](MACHOS/System_Settings.md)
- [/System/Applications/System Settings.app/Contents/PlugIns/GeneralSettings.appex/Contents/MacOS/GeneralSettings](MACHOS/GeneralSettings.md)
- [/System/Applications/System Settings.app/Contents/PlugIns/csimporter.appex/Contents/MacOS/csimporter](MACHOS/csimporter.md)
- [/System/Applications/System Settings.app/Contents/Resources/systemsettingsagent](MACHOS/systemsettingsagent.md)
- [/System/Applications/TV.app/Contents/MacOS/TV](MACHOS/TV.md)
- [/System/Applications/TV.app/Contents/PlugIns/TVCacheExtension.appex/Contents/MacOS/TVCacheExtension](MACHOS/TVCacheExtension.md)
- [/System/Applications/TV.app/Contents/PlugIns/TVStorageExtension.appex/Contents/MacOS/TVStorageExtension](MACHOS/TVStorageExtension.md)
- [/System/Applications/TV.app/Contents/PlugIns/com.apple.TV.web.bundle/Contents/MacOS/com.apple.TV.web](MACHOS/com.apple.TV.web.md)
- [/System/Applications/Tips.app/Contents/MacOS/Tips](MACHOS/Tips.md)
- [/System/Applications/Tips.app/Contents/PlugIns/HelpViewer-Quicklook.appex/Contents/MacOS/HelpViewer-Quicklook](MACHOS/HelpViewer-Quicklook.md)
- [/System/Applications/Utilities/Boot Camp Assistant.app/Contents/MacOS/Boot Camp Assistant](MACHOS/Boot_Camp_Assistant.md)
- [/System/Applications/Utilities/Console.app/Contents/MacOS/Console](MACHOS/Console.md)
- [/System/Applications/Utilities/Print Center.app/Contents/MacOS/Print Center](MACHOS/Print_Center.md)
- [/System/Applications/Utilities/Screen Sharing.app/Contents/MacOS/Screen Sharing](MACHOS/Screen_Sharing.md)
- [/System/Applications/Utilities/VoiceOver Utility.app/Contents/MacOS/VoiceOver Utility](MACHOS/VoiceOver_Utility.md)
- [/System/Applications/Utilities/VoiceOver Utility.app/Contents/OtherBinaries/VoiceOverUtilityCacheBuilder.app/Contents/MacOS/VoiceOver Utility](MACHOS/VoiceOver_Utility.md)
- [/System/Applications/VoiceMemos.app/Contents/MacOS/VoiceMemos](MACHOS/VoiceMemos.md)
- [/System/Applications/VoiceMemos.app/Contents/PlugIns/VoiceMemosSettingsWidgetExtension.appex/Contents/MacOS/VoiceMemosSettingsWidgetExtension](MACHOS/VoiceMemosSettingsWidgetExtension.md)
- [/System/Applications/Weather.app/Contents/MacOS/Weather](MACHOS/Weather.md)
- [/System/Applications/Weather.app/Contents/PlugIns/AppKitPlugin.bundle/Contents/MacOS/AppKitPlugin](MACHOS/AppKitPlugin.md)
- [/System/Applications/Weather.app/Contents/PlugIns/WeatherWidget.appex/Contents/MacOS/WeatherWidget](MACHOS/WeatherWidget.md)
- [/System/Applications/iPhone Mirroring.app/Contents/Frameworks/ScreenContinuityUI.framework/Versions/A/ScreenContinuityUI](MACHOS/ScreenContinuityUI.md)
- [/System/Applications/iPhone Mirroring.app/Contents/MacOS/iPhone Mirroring](MACHOS/iPhone_Mirroring.md)
- [/System/Applications/iPhone Mirroring.app/Contents/PlugIns/OnenessDockTile.docktileplugin/Contents/MacOS/OnenessDockTile](MACHOS/OnenessDockTile.md)
- [/System/Library/Accessibility/BundlesBase/com.apple.MailUI.axbundle/Versions/A/com.apple.MailUI](MACHOS/com.apple.MailUI.md)
- [/System/Library/Accessibility/BundlesBase/com.apple.Preview.axbundle/Versions/A/com.apple.Preview](MACHOS/com.apple.Preview.md)
- [/System/Library/Accounts/Authentication/AMSAccountAuthenticationPlugin.bundle/Contents/MacOS/AMSAccountAuthenticationPlugin](MACHOS/AMSAccountAuthenticationPlugin.md)
- [/System/Library/Accounts/Authentication/GoogleAuthenticationPlugin.bundle/Contents/MacOS/GoogleAuthenticationPlugin](MACHOS/GoogleAuthenticationPlugin.md)
- [/System/Library/Accounts/DataclassOwners/FreeformDataclassOwner.bundle/Contents/MacOS/FreeformDataclassOwner](MACHOS/FreeformDataclassOwner.md)
- [/System/Library/Accounts/DataclassOwners/PassbookDataclassOwnerPlugin.bundle/Contents/MacOS/PassbookDataclassOwnerPlugin](MACHOS/PassbookDataclassOwnerPlugin.md)
- [/System/Library/Accounts/DataclassOwners/StocksDataclassOwner.bundle/Contents/MacOS/StocksDataclassOwner](MACHOS/StocksDataclassOwner.md)
- [/System/Library/Accounts/Notification/AMPAccountNotificationPlugin.bundle/Contents/MacOS/AMPAccountNotificationPlugin](MACHOS/AMPAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/NotesAccountNotificationPlugin.bundle/Contents/MacOS/NotesAccountNotificationPlugin](MACHOS/NotesAccountNotificationPlugin.md)
- [/System/Library/Accounts/ServiceOwners/AMSMediaServiceOwner.bundle/Contents/MacOS/AMSMediaServiceOwner](MACHOS/AMSMediaServiceOwner.md)
- [/System/Library/Accounts/SwiftUI/iCloudSwiftUIPlugin.bundle/Contents/MacOS/iCloudSwiftUIPlugin](MACHOS/iCloudSwiftUIPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/CoreDynamicUIPlugin.bundle/Contents/MacOS/CoreDynamicUIPlugin](MACHOS/CoreDynamicUIPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/Contents/MacOS/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/iCloudDynamicUIPlugin.bundle/Contents/MacOS/iCloudDynamicUIPlugin](MACHOS/iCloudDynamicUIPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AlarmFlowPlugin.bundle/Contents/MacOS/AlarmFlowPlugin](MACHOS/AlarmFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/MacOS/AudioFlowDelegatePlugin](MACHOS/AudioFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EdutainmentFlowPlugin.bundle/Contents/MacOS/EdutainmentFlowPlugin](MACHOS/EdutainmentFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/GeoFlowDelegatePlugin.bundle/Contents/MacOS/GeoFlowDelegatePlugin](MACHOS/GeoFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HealthFlowDelegatePlugin.bundle/Contents/MacOS/HealthFlowDelegatePlugin](MACHOS/HealthFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Contents/MacOS/InformationFlowPlugin](MACHOS/InformationFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Contents/MacOS/PhoneCallFlowDelegatePlugin](MACHOS/PhoneCallFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SettingsFlowDelegatePlugin.bundle/Contents/MacOS/SettingsFlowDelegatePlugin](MACHOS/SettingsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriLinkFlowPlugin.bundle/Contents/MacOS/SiriLinkFlowPlugin](MACHOS/SiriLinkFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Contents/MacOS/SocialConversationFlowDelegatePlugin](MACHOS/SocialConversationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/TimerFlowDelegatePlugin.bundle/Contents/MacOS/TimerFlowDelegatePlugin](MACHOS/TimerFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Contents/MacOS/WellnessFlowPlugin](MACHOS/WellnessFlowPlugin.md)
- [/System/Library/Assistant/Plugins/Maps.assistantBundle/Contents/MacOS/Maps](MACHOS/Maps.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningInferencePlugin.bundle/Contents/MacOS/SiriPrivateLearningInferencePlugin](MACHOS/SiriPrivateLearningInferencePlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningPatternExtractionPlugin.bundle/Contents/MacOS/SiriPrivateLearningPatternExtractionPlugin](MACHOS/SiriPrivateLearningPatternExtractionPlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningTTSMispronunciationPlugin.bundle/Contents/MacOS/SiriPrivateLearningTTSMispronunciationPlugin](MACHOS/SiriPrivateLearningTTSMispronunciationPlugin.md)
- [/System/Library/Assistant/Suggestions/InferenceBridge/SiriSuggestionsInferenceBridge.bundle/Contents/MacOS/SiriSuggestionsInferenceBridge](MACHOS/SiriSuggestionsInferenceBridge.md)
- [/System/Library/Assistant/UIPlugins/Maps.siriUIBundle/Contents/MacOS/Maps](MACHOS/Maps.md)
- [/System/Library/Assistant/UIPlugins/RemindersUI.siriUIBundle/Contents/MacOS/RemindersUI](MACHOS/RemindersUI.md)
- [/System/Library/Audio/Plug-Ins/HAL/AppleAVBAudio2.driver/Contents/MacOS/AppleAVBAudio2](MACHOS/AppleAVBAudio2.md)
- [/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/Contents/MacOS/BTAudioHALPlugin](MACHOS/BTAudioHALPlugin.md)
- [/System/Library/Audio/Plug-Ins/usbaudio.bundle/Contents/MacOS/usbaudiod](MACHOS/usbaudiod.md)
- [/System/Library/Components/AudioCodecs.component/Contents/MacOS/AudioCodecs](MACHOS/AudioCodecs.md)
- [/System/Library/Components/AudioDSP.component/Contents/MacOS/AudioDSP](MACHOS/AudioDSP.md)
- [/System/Library/CoreImage/CIInpainting.cifilter/Contents/MacOS/CIInpainting](MACHOS/CIInpainting.md)
- [/System/Library/CoreServices/APFSUserAgent](MACHOS/APFSUserAgent.md)
- [/System/Library/CoreServices/Applications/Feedback Assistant.app/Contents/Library/LaunchServices/fbahelperd](MACHOS/fbahelperd.md)
- [/System/Library/CoreServices/Applications/Keychain Access.app/Contents/MacOS/Keychain Access](MACHOS/Keychain_Access.md)
- [/System/Library/CoreServices/AskToMessagesHost.app/Contents/PlugIns/AskToMessagesExtension.appex/Contents/MacOS/AskToMessagesExtension](MACHOS/AskToMessagesExtension.md)
- [/System/Library/CoreServices/ControlCenter.app/Contents/MacOS/ControlCenter](MACHOS/ControlCenter.md)
- [/System/Library/CoreServices/ControlCenter.app/Contents/XPCServices/ControlCenterHelper.xpc/Contents/MacOS/ControlCenterHelper](MACHOS/ControlCenterHelper.md)
- [/System/Library/CoreServices/ControlStrip.app/Contents/MacOS/ControlStrip](MACHOS/ControlStrip.md)
- [/System/Library/CoreServices/ControlStrip.app/Contents/XPCServices/com.apple.DFRSystemExtra.NightShift.xpc/Contents/MacOS/com.apple.DFRSystemExtra.NightShift](MACHOS/com.apple.DFRSystemExtra.NightShift.md)
- [/System/Library/CoreServices/CoreServicesUIAgent.app/Contents/MacOS/CoreServicesUIAgent](MACHOS/CoreServicesUIAgent.md)
- [/System/Library/CoreServices/Diagnostics Reporter.app/Contents/MacOS/Diagnostics Reporter](MACHOS/Diagnostics_Reporter.md)
- [/System/Library/CoreServices/Dock.app/Contents/MacOS/Dock](MACHOS/Dock.md)
- [/System/Library/CoreServices/Dock.app/Contents/XPCServices/DockHelper.xpc/Contents/MacOS/DockHelper](MACHOS/DockHelper.md)
- [/System/Library/CoreServices/Dock.app/Contents/XPCServices/com.apple.dock.extra.xpc/Contents/MacOS/com.apple.dock.extra](MACHOS/com.apple.dock.extra.md)
- [/System/Library/CoreServices/Finder.app/Contents/MacOS/Finder](MACHOS/Finder.md)
- [/System/Library/CoreServices/Installer.app/Contents/MacOS/Installer](MACHOS/Installer.md)
- [/System/Library/CoreServices/KeyboardSetupAssistant.app/Contents/MacOS/KeyboardSetupAssistant](MACHOS/KeyboardSetupAssistant.md)
- [/System/Library/CoreServices/MTLReplayer.app/Contents/Frameworks/MTLReplayController.framework/Versions/A/MTLReplayController](MACHOS/MTLReplayController.md)
- [/System/Library/CoreServices/ManagedClient.app/Contents/MacOS/ManagedClient](MACHOS/ManagedClient.md)
- [/System/Library/CoreServices/ManagedClient.app/Contents/PlugIns/ManagedSettingsMacOSExtension.appex/Contents/MacOS/ManagedSettingsMacOSExtension](MACHOS/ManagedSettingsMacOSExtension.md)
- [/System/Library/CoreServices/ManagedClient.app/Contents/PlugIns/RestrictionsPlugin.profileDomainPlugin/Contents/MacOS/RestrictionsPlugin](MACHOS/RestrictionsPlugin.md)
- [/System/Library/CoreServices/Menu Extras/TimeMachine.menu/Contents/MacOS/TimeMachine](MACHOS/TimeMachine.md)
- [/System/Library/CoreServices/NotificationCenter.app/Contents/MacOS/NotificationCenter](MACHOS/NotificationCenter.md)
- [/System/Library/CoreServices/PIPAgent.app/Contents/MacOS/PIPAgent](MACHOS/PIPAgent.md)
- [/System/Library/CoreServices/PasswordManagerBrowserExtensionHelper.app/Contents/MacOS/PasswordManagerBrowserExtensionHelper](MACHOS/PasswordManagerBrowserExtensionHelper.md)
- [/System/Library/CoreServices/PeopleMessageService.app/Contents/PlugIns/PeopleMessagesScreenTime.appex/Contents/MacOS/PeopleMessagesScreenTime](MACHOS/PeopleMessagesScreenTime.md)
- [/System/Library/CoreServices/PeopleViewService.app/Contents/PlugIns/PeopleWidget_macOSExtension.appex/Contents/MacOS/PeopleWidget_macOSExtension](MACHOS/PeopleWidget_macOSExtension.md)
- [/System/Library/CoreServices/PreviewShell.app/Contents/MacOS/PreviewShell](MACHOS/PreviewShell.md)
- [/System/Library/CoreServices/RFBEventHelper.bundle/Contents/MacOS/RFBEventHelperd](MACHOS/RFBEventHelperd.md)
- [/System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/MacOS/ARDAgent](MACHOS/ARDAgent.md)
- [/System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/Support/Shared Screen Viewer.app/Contents/MacOS/Shared Screen Viewer](MACHOS/Shared_Screen_Viewer.md)
- [/System/Library/CoreServices/RemoteManagement/SSMenuAgent.app/Contents/MacOS/SSMenuAgent](MACHOS/SSMenuAgent.md)
- [/System/Library/CoreServices/ReportCrash](MACHOS/ReportCrash.md)
- [/System/Library/CoreServices/SafariSupport.bundle/Contents/MacOS/SafariBookmarksSyncAgent](MACHOS/SafariBookmarksSyncAgent.md)
- [/System/Library/CoreServices/Screen Time.app/Contents/MacOS/Screen Time](MACHOS/Screen_Time.md)
- [/System/Library/CoreServices/Screen Time.app/Contents/PlugIns/ScreenTimeWidgetExtension.appex/Contents/MacOS/ScreenTimeWidgetExtension](MACHOS/ScreenTimeWidgetExtension.md)
- [/System/Library/CoreServices/Screen Time.app/Contents/PlugIns/ScreenTimeWidgetIntentsExtension.appex/Contents/MacOS/ScreenTimeWidgetIntentsExtension](MACHOS/ScreenTimeWidgetIntentsExtension.md)
- [/System/Library/CoreServices/SecurityAgentPlugins/LocalAuthentication.bundle/Contents/MacOS/LocalAuthentication](MACHOS/LocalAuthentication.md)
- [/System/Library/CoreServices/SecurityAgentPlugins/loginwindow.bundle/Contents/MacOS/loginwindow](MACHOS/loginwindow.md)
- [/System/Library/CoreServices/Setup Assistant.app/Contents/MacOS/Setup Assistant](MACHOS/Setup_Assistant.md)
- [/System/Library/CoreServices/Siri.app/Contents/MacOS/Siri](MACHOS/Siri.md)
- [/System/Library/CoreServices/Siri.app/Contents/XPCServices/SiriNCService.xpc/Contents/MacOS/SiriNCService](MACHOS/SiriNCService.md)
- [/System/Library/CoreServices/SpacesTouchBarAgent.app/Contents/MacOS/SpacesTouchBarAgent](MACHOS/SpacesTouchBarAgent.md)
- [/System/Library/CoreServices/Spotlight.app/Contents/Extensions/SpotlightPreferenceExtension.appex/Contents/MacOS/SpotlightPreferenceExtension](MACHOS/SpotlightPreferenceExtension.md)
- [/System/Library/CoreServices/Spotlight.app/Contents/MacOS/Spotlight](MACHOS/Spotlight.md)
- [/System/Library/CoreServices/SystemUIServer.app/Contents/MacOS/SystemUIServer](MACHOS/SystemUIServer.md)
- [/System/Library/CoreServices/TextInputSwitcher.app/Contents/MacOS/TextInputSwitcher](MACHOS/TextInputSwitcher.md)
- [/System/Library/CoreServices/TimeMachine/backupd](MACHOS/backupd.md)
- [/System/Library/CoreServices/TimeMachine/backupd-helper](MACHOS/backupd-helper.md)
- [/System/Library/CoreServices/TouchBarEvent.bundle](MACHOS/TouchBarEvent.bundle.md)
- [/System/Library/CoreServices/UAUPlugins/ControlCenterUpdater.bundle/Contents/MacOS/ControlCenterUpdater](MACHOS/ControlCenterUpdater.md)
- [/System/Library/CoreServices/UAUPlugins/DockUpdater.bundle/Contents/MacOS/DockUpdater](MACHOS/DockUpdater.md)
- [/System/Library/CoreServices/UAUPlugins/SettingsUAUPlugin.bundle/Contents/Resources/IndexSettings](MACHOS/IndexSettings.md)
- [/System/Library/CoreServices/UAUPlugins/SpacesUpdater.bundle/Contents/MacOS/SpacesUpdater](MACHOS/SpacesUpdater.md)
- [/System/Library/CoreServices/UniversalControl.app/Contents/MacOS/UniversalControl](MACHOS/UniversalControl.md)
- [/System/Library/CoreServices/WallpaperAgent.app/Contents/MacOS/WallpaperAgent](MACHOS/WallpaperAgent.md)
- [/System/Library/CoreServices/WidgetKit Simulator.app/Contents/MacOS/WidgetKit Simulator](MACHOS/WidgetKit_Simulator.md)
- [/System/Library/CoreServices/WindowManager.app/Contents/MacOS/WindowManager](MACHOS/WindowManager.md)
- [/System/Library/CoreServices/WindowManagerShowDesktopEducation.app/Contents/MacOS/WindowManagerShowDesktopEducation](MACHOS/WindowManagerShowDesktopEducation.md)
- [/System/Library/CoreServices/appplaceholdersyncd](MACHOS/appplaceholdersyncd.md)
- [/System/Library/CoreServices/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/System/Library/CoreServices/lockoutagent](MACHOS/lockoutagent.md)
- [/System/Library/CoreServices/loginwindow.app/Contents/MacOS/loginwindow](MACHOS/loginwindow.md)
- [/System/Library/CoreServices/osanalyticshelper](MACHOS/osanalyticshelper.md)
- [/System/Library/CoreServices/powerd.bundle/powerd](MACHOS/powerd.md)
- [/System/Library/CoreServices/screencaptureui.app/Contents/MacOS/screencaptureui](MACHOS/screencaptureui.md)
- [/System/Library/CoreServices/sharedfilelistd](MACHOS/sharedfilelistd.md)
- [/System/Library/CryptoTokenKit/com.apple.ifdreader.slotd/Contents/MacOS/com.apple.ifdreader](MACHOS/com.apple.ifdreader.md)
- [/System/Library/CryptoTokenKit/usbsmartcardreaderd.slotd/Contents/MacOS/usbsmartcardreaderd](MACHOS/usbsmartcardreaderd.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN.md)
- [/System/Library/ExtensionKit/Extensions/ /BluetoothSettingsAppIntentsWidgetExtension.appex/Contents/MacOS/BluetoothSettingsAppIntentsWidgetExtension](MACHOS/BluetoothSettingsAppIntentsWidgetExtension.md)
- [/System/Library/ExtensionKit/Extensions/AccessibilitySettingsExtension.appex/Contents/MacOS/AccessibilitySettingsExtension](MACHOS/AccessibilitySettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/AccessibilitySettingsWidgetExtension.appex/Contents/MacOS/AccessibilitySettingsWidgetExtension](MACHOS/AccessibilitySettingsWidgetExtension.md)
- [/System/Library/ExtensionKit/Extensions/Appearance.appex/Contents/MacOS/Appearance](MACHOS/Appearance.md)
- [/System/Library/ExtensionKit/Extensions/AppearanceIntentsExtension.appex/Contents/MacOS/AppearanceIntentsExtension](MACHOS/AppearanceIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/AppleIDSettings.appex/Contents/MacOS/AppleIDSettings](MACHOS/AppleIDSettings.md)
- [/System/Library/ExtensionKit/Extensions/AudiovisualThumbnailExtension.appex/Contents/MacOS/AudiovisualThumbnailExtension](MACHOS/AudiovisualThumbnailExtension.md)
- [/System/Library/ExtensionKit/Extensions/BiomeLibraryEventUploader.appex/Contents/MacOS/BiomeLibraryEventUploader](MACHOS/BiomeLibraryEventUploader.md)
- [/System/Library/ExtensionKit/Extensions/BitacoraWorker.appex/Contents/MacOS/BitacoraWorker](MACHOS/BitacoraWorker.md)
- [/System/Library/ExtensionKit/Extensions/Bluetooth.appex/Contents/MacOS/Bluetooth](MACHOS/Bluetooth.md)
- [/System/Library/ExtensionKit/Extensions/CDs & DVDs Settings Extension.appex/Contents/MacOS/CDs & DVDs Settings Extension](MACHOS/CDs_&_DVDs_Settings_Extension.md)
- [/System/Library/ExtensionKit/Extensions/CalendarThumbnailExtension.appex/Contents/MacOS/CalendarThumbnailExtension](MACHOS/CalendarThumbnailExtension.md)
- [/System/Library/ExtensionKit/Extensions/ClassKitAppIntents.appex/Contents/MacOS/ClassKitAppIntents](MACHOS/ClassKitAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/ClassKitSettings.appex/Contents/MacOS/ClassKitSettings](MACHOS/ClassKitSettings.md)
- [/System/Library/ExtensionKit/Extensions/ClassroomDeviceExpert.appex/Contents/MacOS/ClassroomDeviceExpert](MACHOS/ClassroomDeviceExpert.md)
- [/System/Library/ExtensionKit/Extensions/ClassroomSettings.appex/Contents/MacOS/ClassroomSettings](MACHOS/ClassroomSettings.md)
- [/System/Library/ExtensionKit/Extensions/ControlCenterSettings.appex/Contents/MacOS/ControlCenterSettings](MACHOS/ControlCenterSettings.md)
- [/System/Library/ExtensionKit/Extensions/ControlCenterSettingsIntents.appex/Contents/MacOS/ControlCenterSettingsIntents](MACHOS/ControlCenterSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/DateAndTime Extension.appex/Contents/MacOS/DateAndTime Extension](MACHOS/DateAndTime_Extension.md)
- [/System/Library/ExtensionKit/Extensions/DateTimeIntentsExtension.appex/Contents/MacOS/DateTimeIntentsExtension](MACHOS/DateTimeIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/DefaultExtensionEnablement.appex/Contents/MacOS/DefaultExtensionEnablement](MACHOS/DefaultExtensionEnablement.md)
- [/System/Library/ExtensionKit/Extensions/DesktopSettings.appex/Contents/MacOS/DesktopSettings](MACHOS/DesktopSettings.md)
- [/System/Library/ExtensionKit/Extensions/DesktopSettings.appex/Contents/Resources/DesktopSettingsScripting.scripting/Contents/MacOS/DesktopSettingsScripting](MACHOS/DesktopSettingsScripting.md)
- [/System/Library/ExtensionKit/Extensions/DesktopSettingsIntents.appex/Contents/MacOS/DesktopSettingsIntents](MACHOS/DesktopSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/DevicePropertiesExtension.appex/Contents/MacOS/DevicePropertiesExtension](MACHOS/DevicePropertiesExtension.md)
- [/System/Library/ExtensionKit/Extensions/DisplaysExt.appex/Contents/MacOS/DisplaysExt](MACHOS/DisplaysExt.md)
- [/System/Library/ExtensionKit/Extensions/DoNotDisturbAppIntents.appex/Contents/MacOS/DoNotDisturbAppIntents](MACHOS/DoNotDisturbAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/EventKitUIRemoteUIExtension.appex/Contents/MacOS/EventKitUIRemoteUIExtension](MACHOS/EventKitUIRemoteUIExtension.md)
- [/System/Library/ExtensionKit/Extensions/ExperimentationExtension.appex/Contents/MacOS/ExperimentationExtension](MACHOS/ExperimentationExtension.md)
- [/System/Library/ExtensionKit/Extensions/FaceTimeNotificationExtension.appex/Contents/MacOS/FaceTimeNotificationExtension](MACHOS/FaceTimeNotificationExtension.md)
- [/System/Library/ExtensionKit/Extensions/FamilySettings.appex/Contents/MacOS/FamilySettings](MACHOS/FamilySettings.md)
- [/System/Library/ExtensionKit/Extensions/FocusSettingsExtension.appex/Contents/MacOS/FocusSettingsExtension](MACHOS/FocusSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/FontThumbnailExtension.appex/Contents/MacOS/FontThumbnailExtension](MACHOS/FontThumbnailExtension.md)
- [/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/Contents/MacOS/GPUIExtension](MACHOS/GPUIExtension.md)
- [/System/Library/ExtensionKit/Extensions/HeadphoneSettingsExtension.appex/Contents/MacOS/HeadphoneSettingsExtension](MACHOS/HeadphoneSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/IEMetricsWorker.appex/Contents/MacOS/IEMetricsWorker](MACHOS/IEMetricsWorker.md)
- [/System/Library/ExtensionKit/Extensions/IFTelemetrySELFIngestor.appex/Contents/MacOS/IFTelemetrySELFIngestor](MACHOS/IFTelemetrySELFIngestor.md)
- [/System/Library/ExtensionKit/Extensions/ImageThumbnailExtension.appex/Contents/MacOS/ImageThumbnailExtension](MACHOS/ImageThumbnailExtension.md)
- [/System/Library/ExtensionKit/Extensions/InternationalSettingsExtension.appex/Contents/MacOS/InternationalSettingsExtension](MACHOS/InternationalSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/KeyboardSettings.appex/Contents/MacOS/KeyboardSettings](MACHOS/KeyboardSettings.md)
- [/System/Library/ExtensionKit/Extensions/LegacyPluginEnablement.appex/Contents/MacOS/LegacyPluginEnablement](MACHOS/LegacyPluginEnablement.md)
- [/System/Library/ExtensionKit/Extensions/Localization.appex/Contents/MacOS/Localization](MACHOS/Localization.md)
- [/System/Library/ExtensionKit/Extensions/LockScreen.appex/Contents/MacOS/LockScreen](MACHOS/LockScreen.md)
- [/System/Library/ExtensionKit/Extensions/LockScreenIntentsExtension.appex/Contents/MacOS/LockScreenIntentsExtension](MACHOS/LockScreenIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/LoginItems.appex/Contents/MacOS/LoginItems](MACHOS/LoginItems.md)
- [/System/Library/ExtensionKit/Extensions/LoginItemsIntentsExtension.appex/Contents/MacOS/LoginItemsIntentsExtension](MACHOS/LoginItemsIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MKRemoteUI.appex/Contents/MacOS/MKRemoteUI](MACHOS/MKRemoteUI.md)
- [/System/Library/ExtensionKit/Extensions/MetricsExtension.appex/Contents/MacOS/MetricsExtension](MACHOS/MetricsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MouseExtension.appex/Contents/MacOS/MouseExtension](MACHOS/MouseExtension.md)
- [/System/Library/ExtensionKit/Extensions/Network.appex/Contents/MacOS/Network](MACHOS/Network.md)
- [/System/Library/ExtensionKit/Extensions/NotificationsSettings.appex/Contents/MacOS/NotificationsSettings](MACHOS/NotificationsSettings.md)
- [/System/Library/ExtensionKit/Extensions/NotificationsSettingsIntents.appex/Contents/MacOS/NotificationsSettingsIntents](MACHOS/NotificationsSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/OfficeThumbnailExtension.appex/Contents/MacOS/OfficeThumbnailExtension](MACHOS/OfficeThumbnailExtension.md)
- [/System/Library/ExtensionKit/Extensions/PnROnDeviceWorker.appex/Contents/MacOS/PnROnDeviceWorker](MACHOS/PnROnDeviceWorker.md)
- [/System/Library/ExtensionKit/Extensions/PowerPreferences.appex/Contents/MacOS/PowerPreferences](MACHOS/PowerPreferences.md)
- [/System/Library/ExtensionKit/Extensions/PrivateMLClientInferenceProviderService.appex/Contents/MacOS/PrivateMLClientInferenceProviderService](MACHOS/PrivateMLClientInferenceProviderService.md)
- [/System/Library/ExtensionKit/Extensions/ProfilesSettingsExt.appex/Contents/MacOS/ProfilesSettingsExt](MACHOS/ProfilesSettingsExt.md)
- [/System/Library/ExtensionKit/Extensions/RepackagingWorker.appex/Contents/MacOS/RepackagingWorker](MACHOS/RepackagingWorker.md)
- [/System/Library/ExtensionKit/Extensions/Screen Saver.appex/Contents/MacOS/Screen Saver](MACHOS/Screen_Saver.md)
- [/System/Library/ExtensionKit/Extensions/ScreenTimePreferencesExtension.appex/Contents/MacOS/ScreenTimePreferencesExtension](MACHOS/ScreenTimePreferencesExtension.md)
- [/System/Library/ExtensionKit/Extensions/SecurityPrivacyExtension.appex/Contents/MacOS/SecurityPrivacyExtension](MACHOS/SecurityPrivacyExtension.md)
- [/System/Library/ExtensionKit/Extensions/SettingsSystemExtensionController.appex/Contents/MacOS/SettingsSystemExtensionController](MACHOS/SettingsSystemExtensionController.md)
- [/System/Library/ExtensionKit/Extensions/Sharing.appex/Contents/MacOS/Sharing](MACHOS/Sharing.md)
- [/System/Library/ExtensionKit/Extensions/SiriPreferenceExtension.appex/Contents/MacOS/SiriPreferenceExtension](MACHOS/SiriPreferenceExtension.md)
- [/System/Library/ExtensionKit/Extensions/SoftwareUpdateSettingsExtension.appex/Contents/MacOS/SoftwareUpdateSettingsExtension](MACHOS/SoftwareUpdateSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/SoftwareUpdateSettingsWidgetExtension.appex/Contents/MacOS/SoftwareUpdateSettingsWidgetExtension](MACHOS/SoftwareUpdateSettingsWidgetExtension.md)
- [/System/Library/ExtensionKit/Extensions/SpotlightPreferenceExtension.appex/Contents/MacOS/SpotlightPreferenceExtension](MACHOS/SpotlightPreferenceExtension.md)
- [/System/Library/ExtensionKit/Extensions/Storage.appex/Contents/MacOS/Storage](MACHOS/Storage.md)
- [/System/Library/ExtensionKit/Extensions/TimeMachineSettings.appex/Contents/MacOS/TimeMachineSettings](MACHOS/TimeMachineSettings.md)
- [/System/Library/ExtensionKit/Extensions/Touch ID & Password.appex/Contents/MacOS/Touch ID & Password](MACHOS/Touch_ID_&_Password.md)
- [/System/Library/ExtensionKit/Extensions/TrackpadExtension.appex/Contents/MacOS/TrackpadExtension](MACHOS/TrackpadExtension.md)
- [/System/Library/ExtensionKit/Extensions/TrackpadIntentsExtension.appex/Contents/MacOS/TrackpadIntentsExtension](MACHOS/TrackpadIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/USDAppIntents.appex/Contents/MacOS/USDAppIntents](MACHOS/USDAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/UsersGroups.appex/Contents/MacOS/UsersGroups](MACHOS/UsersGroups.md)
- [/System/Library/ExtensionKit/Extensions/UsersGroupsIntentsExtension.appex/Contents/MacOS/UsersGroupsIntentsExtension](MACHOS/UsersGroupsIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/VPN.appex/Contents/MacOS/VPN](MACHOS/VPN.md)
- [/System/Library/ExtensionKit/Extensions/Wallpaper.appex/Contents/MacOS/Wallpaper](MACHOS/Wallpaper.md)
- [/System/Library/ExtensionKit/Extensions/WallpaperCAPackageExtension.appex/Contents/MacOS/WallpaperCAPackageExtension](MACHOS/WallpaperCAPackageExtension.md)
- [/System/Library/ExtensionKit/Extensions/WallpaperDynamicExtension.appex/Contents/MacOS/WallpaperDynamicExtension](MACHOS/WallpaperDynamicExtension.md)
- [/System/Library/ExtensionKit/Extensions/WallpaperGradientExtension.appex/Contents/MacOS/WallpaperGradientExtension](MACHOS/WallpaperGradientExtension.md)
- [/System/Library/ExtensionKit/Extensions/WallpaperHeliosExtension.appex/Contents/MacOS/WallpaperHeliosExtension](MACHOS/WallpaperHeliosExtension.md)
- [/System/Library/ExtensionKit/Extensions/WallpaperImageExtension.appex/Contents/MacOS/WallpaperImageExtension](MACHOS/WallpaperImageExtension.md)
- [/System/Library/ExtensionKit/Extensions/WallpaperMacintoshExtension.appex/Contents/MacOS/WallpaperMacintoshExtension](MACHOS/WallpaperMacintoshExtension.md)
- [/System/Library/ExtensionKit/Extensions/WallpaperMontereyExtension.appex/Contents/MacOS/WallpaperMontereyExtension](MACHOS/WallpaperMontereyExtension.md)
- [/System/Library/ExtensionKit/Extensions/WallpaperVenturaExtension.appex/Contents/MacOS/WallpaperVenturaExtension](MACHOS/WallpaperVenturaExtension.md)
- [/System/Library/ExtensionKit/Extensions/WallpaperVideoExtension.appex/Contents/MacOS/WallpaperVideoExtension](MACHOS/WallpaperVideoExtension.md)
- [/System/Library/ExtensionKit/Extensions/WebThumbnailExtension.appex/Contents/MacOS/WebThumbnailExtension](MACHOS/WebThumbnailExtension.md)
- [/System/Library/ExtensionKit/Extensions/Wi-Fi.appex/Contents/MacOS/Wi-Fi](MACHOS/Wi-Fi.md)
- [/System/Library/ExtensionKit/Extensions/ZeoliteExtension.appex/Contents/MacOS/ZeoliteExtension](MACHOS/ZeoliteExtension.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.msdos.appex/Contents/MacOS/com.apple.fskit.msdos](MACHOS/com.apple.fskit.msdos.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.SampleWorker.appex/Contents/MacOS/com.apple.mlhost.SampleWorker](MACHOS/com.apple.mlhost.SampleWorker.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.TelemetryWorker.appex/Contents/MacOS/com.apple.mlhost.TelemetryWorker](MACHOS/com.apple.mlhost.TelemetryWorker.md)
- [/System/Library/Extensions/AGXMetal13_3.bundle/Contents/MacOS/AGXMetal13_3](MACHOS/AGXMetal13_3.md)
- [/System/Library/Extensions/AGXMetalG13X.bundle/Contents/MacOS/AGXMetalG13X](MACHOS/AGXMetalG13X.md)
- [/System/Library/Extensions/AGXMetalG14G.bundle/Contents/MacOS/AGXMetalG14G](MACHOS/AGXMetalG14G.md)
- [/System/Library/Extensions/AGXMetalG14X.bundle/Contents/MacOS/AGXMetalG14X](MACHOS/AGXMetalG14X.md)
- [/System/Library/Extensions/AGXMetalG15G_B0.bundle/Contents/MacOS/AGXMetalG15G_B0](MACHOS/AGXMetalG15G_B0.md)
- [/System/Library/Extensions/AGXMetalG15G_C0.bundle/Contents/MacOS/AGXMetalG15G_C0](MACHOS/AGXMetalG15G_C0.md)
- [/System/Library/Extensions/AGXMetalG15X_M0.bundle/Contents/MacOS/AGXMetalG15X_M0](MACHOS/AGXMetalG15X_M0.md)
- [/System/Library/Extensions/AGXMetalG15X_M1.bundle/Contents/MacOS/AGXMetalG15X_M1](MACHOS/AGXMetalG15X_M1.md)
- [/System/Library/Extensions/AppleMetalOpenGLRenderer.bundle/Contents/MacOS/AppleMetalOpenGLRenderer](MACHOS/AppleMetalOpenGLRenderer.md)
- [/System/Library/Filesystems/acfs.fs/Contents/bin/fsmpm](MACHOS/fsmpm.md)
- [/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_condenser](MACHOS/apfs_condenser.md)
- [/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_invert](MACHOS/apfs_invert.md)
- [/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_prepare_cryptex](MACHOS/apfs_prepare_cryptex.md)
- [/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_vol_converter](MACHOS/apfs_vol_converter.md)
- [/System/Library/Filesystems/apfs.fs/Contents/Resources/fsck_apfs](MACHOS/fsck_apfs.md)
- [/System/Library/Filesystems/apfs.fs/Contents/Resources/hfs_convert](MACHOS/hfs_convert.md)
- [/System/Library/Filesystems/apfs.fs/Contents/Resources/newfs_apfs](MACHOS/newfs_apfs.md)
- [/System/Library/Filesystems/apfs.fs/Contents/Resources/slurpAPFSMeta](MACHOS/slurpAPFSMeta.md)
- [/System/Library/Frameworks/Accounts.framework/Versions/A/Support/accountsd](MACHOS/accountsd.md)
- [/System/Library/Frameworks/AddressBook.framework/Helpers/AddressBookSync.app/Contents/MacOS/AddressBookSync](MACHOS/AddressBookSync.md)
- [/System/Library/Frameworks/AppKit.framework/Versions/C/XPCServices/ThemeWidgetControlViewService.xpc/Contents/MacOS/ThemeWidgetControlViewService](MACHOS/ThemeWidgetControlViewService.md)
- [/System/Library/Frameworks/AppKit.framework/Versions/C/XPCServices/TrustedUIService.xpc/Contents/MacOS/TrustedUIService](MACHOS/TrustedUIService.md)
- [/System/Library/Frameworks/AppKit.framework/Versions/C/XPCServices/TypographyPanelService.xpc/Contents/MacOS/TypographyPanelService](MACHOS/TypographyPanelService.md)
- [/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/A/Support/fontd](MACHOS/fontd.md)
- [/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/PrintCore.framework/Versions/A/printtool](MACHOS/printtool.md)
- [/System/Library/Frameworks/Automator.framework/Versions/A/XPCServices/com.apple.automator.runner.xpc/Contents/MacOS/com.apple.automator.runner](MACHOS/com.apple.automator.runner.md)
- [/System/Library/Frameworks/CFNetwork.framework/Versions/A/Support/AuthBrokerAgent](MACHOS/AuthBrokerAgent.md)
- [/System/Library/Frameworks/CFNetwork.framework/Versions/A/Support/CFNetworkAgent](MACHOS/CFNetworkAgent.md)
- [/System/Library/Frameworks/ClassKit.framework/Versions/A/progressd](MACHOS/progressd.md)
- [/System/Library/Frameworks/ColorSync.framework/Support/colorsync.useragent](MACHOS/colorsync.useragent.md)
- [/System/Library/Frameworks/CoreMediaIO.framework/Versions/A/Resources/BaseUnits/CMIOBaseUnits.bundle/Contents/MacOS/CMIOBaseUnits](MACHOS/CMIOBaseUnits.md)
- [/System/Library/Frameworks/CoreMediaIO.framework/Versions/A/Resources/CinematicFramingOnboardingUI.app/Contents/MacOS/CinematicFramingOnboardingUI](MACHOS/CinematicFramingOnboardingUI.md)
- [/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/AE.framework/Versions/A/Support/AEServer](MACHOS/AEServer.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged](MACHOS/spotlightknowledged.md)
- [/System/Library/Frameworks/CreateML.framework/Versions/A/CreateML](MACHOS/CreateML.md)
- [/System/Library/Frameworks/CryptoTokenKit.framework/ctkcard](MACHOS/ctkcard.md)
- [/System/Library/Frameworks/FamilyControls.framework/Versions/A/FamilyControlsAgent](MACHOS/FamilyControlsAgent.md)
- [/System/Library/Frameworks/FileProvider.framework/OverrideBundles/FinderSyncCollaborationFileProviderOverride.bundle/Contents/MacOS/FinderSyncCollaborationFileProviderOverride](MACHOS/FinderSyncCollaborationFileProviderOverride.md)
- [/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd](MACHOS/fileproviderd.md)
- [/System/Library/Frameworks/ImageCaptureCore.framework/Versions/A/XPCServices/mscamerad-xpc.xpc/Contents/MacOS/mscamerad-xpc](MACHOS/mscamerad-xpc.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPasscode.bundle/Contents/MacOS/MechPasscode](MACHOS/MechPasscode.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechTouchId.bundle/Contents/MacOS/MechTouchId](MACHOS/MechTouchId.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechWatch.bundle/Contents/MacOS/MechWatch](MACHOS/MechWatch.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/ModulePlugins/ModuleACM.bundle/Contents/MacOS/ModuleACM](MACHOS/ModuleACM.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/coreautha.bundle/Contents/MacOS/coreautha](MACHOS/coreautha.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd](MACHOS/coreauthd.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributionagent](MACHOS/managedappdistributionagent.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond](MACHOS/managedappdistributiond.md)
- [/System/Library/Frameworks/ManagedSettings.framework/Versions/A/ManagedSettingsAgent](MACHOS/ManagedSettingsAgent.md)
- [/System/Library/Frameworks/ParavirtualizedGraphics.framework/Versions/A/XPCServices/com.apple.gpusw.ParavirtualizedGraphicsGPUTask.xpc/Contents/MacOS/com.apple.gpusw.ParavirtualizedGraphicsGPUTask](MACHOS/com.apple.gpusw.ParavirtualizedGraphicsGPUTask.md)
- [/System/Library/Frameworks/QuickLookUI.framework/Versions/A/PlugIns/Image.qldisplay/Contents/MacOS/Image](MACHOS/Image.md)
- [/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/MacOS/SecurityAgent](MACHOS/SecurityAgent.md)
- [/System/Library/Frameworks/Security.framework/Versions/A/MachServices/authorizationhost.bundle/Contents/MacOS/authorizationhost](MACHOS/authorizationhost.md)
- [/System/Library/Frameworks/Security.framework/Versions/A/Resources/CloudKeychainProxy.bundle/Contents/MacOS/CloudKeychainProxy](MACHOS/CloudKeychainProxy.md)
- [/System/Library/Frameworks/Security.framework/Versions/A/XPCServices/TrustedPeersHelper.xpc/Contents/MacOS/TrustedPeersHelper](MACHOS/TrustedPeersHelper.md)
- [/System/Library/Frameworks/Security.framework/Versions/A/XPCServices/XPCKeychainSandboxCheck.xpc/Contents/MacOS/XPCKeychainSandboxCheck](MACHOS/XPCKeychainSandboxCheck.md)
- [/System/Library/Frameworks/Security.framework/Versions/A/XPCServices/authd.xpc/Contents/MacOS/authd](MACHOS/authd.md)
- [/System/Library/Frameworks/ShazamKit.framework/shazamd](MACHOS/shazamd.md)
- [/System/Library/Frameworks/Speech.framework/Versions/A/XPCServices/localspeechrecognition.xpc/Contents/MacOS/localspeechrecognition](MACHOS/localspeechrecognition.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitagent](MACHOS/storekitagent.md)
- [/System/Library/Frameworks/SystemExtensions.framework/Versions/A/Helpers/sysextd](MACHOS/sysextd.md)
- [/System/Library/Frameworks/Translation.framework/translationd](MACHOS/translationd.md)
- [/System/Library/Frameworks/Virtualization.framework/Versions/A/XPCServices/com.apple.Virtualization.EventTap.xpc/Contents/MacOS/com.apple.Virtualization.EventTap](MACHOS/com.apple.Virtualization.EventTap.md)
- [/System/Library/Frameworks/Virtualization.framework/Versions/A/XPCServices/com.apple.Virtualization.Installation.xpc/Contents/MacOS/com.apple.Virtualization.Installation](MACHOS/com.apple.Virtualization.Installation.md)
- [/System/Library/Frameworks/Virtualization.framework/Versions/A/XPCServices/com.apple.Virtualization.LinuxRosetta.xpc/Contents/MacOS/com.apple.Virtualization.LinuxRosetta](MACHOS/com.apple.Virtualization.LinuxRosetta.md)
- [/System/Library/Frameworks/Virtualization.framework/Versions/A/XPCServices/com.apple.Virtualization.VirtualMachine.xpc/Contents/MacOS/com.apple.Virtualization.VirtualMachine](MACHOS/com.apple.Virtualization.VirtualMachine.md)
- [/System/Library/Frameworks/WeatherKit.framework/Versions/A/XPCServices/com.apple.weatherkit.authservice.xpc/Contents/MacOS/com.apple.weatherkit.authservice](MACHOS/com.apple.weatherkit.authservice.md)
- [/System/Library/HIDPlugins/ServiceFilters/UniversalControlServiceFilter.plugin/Contents/MacOS/UniversalControlServiceFilter](MACHOS/UniversalControlServiceFilter.md)
- [/System/Library/HIDPlugins/ServicePlugins/DualSenseHIDServicePlugin.plugin/Contents/MacOS/DualSenseHIDServicePlugin](MACHOS/DualSenseHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/DualShock4HIDServicePlugin.plugin/Contents/MacOS/DualShock4HIDServicePlugin](MACHOS/DualShock4HIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/GenericGamepadHIDServicePlugin.plugin/Contents/MacOS/GenericGamepadHIDServicePlugin](MACHOS/GenericGamepadHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/HSTouchHIDService.plugin/Contents/MacOS/HSTouchHIDService](MACHOS/HSTouchHIDService.md)
- [/System/Library/HIDPlugins/ServicePlugins/JoyConHIDServicePlugin.plugin/Contents/MacOS/JoyConHIDServicePlugin](MACHOS/JoyConHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/LunaHIDServicePlugin.plugin/Contents/MacOS/LunaHIDServicePlugin](MACHOS/LunaHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/XboxGamepadHIDServicePlugin.plugin/Contents/MacOS/XboxGamepadHIDServicePlugin](MACHOS/XboxGamepadHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/XboxOneHIDServicePlugin.plugin/Contents/MacOS/XboxOneHIDServicePlugin](MACHOS/XboxOneHIDServicePlugin.md)
- [/System/Library/HIDPlugins/SessionFilters/CoreRCPlugin.plugin/Contents/MacOS/CoreRCPlugin](MACHOS/CoreRCPlugin.md)
- [/System/Library/Image Capture/Support/icdd](MACHOS/icdd.md)
- [/System/Library/Input Methods/CharacterPalette.app/Contents/MacOS/CharacterPalette](MACHOS/CharacterPalette.md)
- [/System/Library/Input Methods/DictationIM.app/Contents/MacOS/DictationIM](MACHOS/DictationIM.md)
- [/System/Library/Kernels/kernel](MACHOS/kernel.md)
- [/System/Library/Kernels/kernel.release.t6000](MACHOS/kernel.release.t6000.md)
- [/System/Library/Kernels/kernel.release.t6020](MACHOS/kernel.release.t6020.md)
- [/System/Library/Kernels/kernel.release.t6030](MACHOS/kernel.release.t6030.md)
- [/System/Library/Kernels/kernel.release.t6031](MACHOS/kernel.release.t6031.md)
- [/System/Library/Kernels/kernel.release.t8103](MACHOS/kernel.release.t8103.md)
- [/System/Library/Kernels/kernel.release.t8112](MACHOS/kernel.release.t8112.md)
- [/System/Library/Kernels/kernel.release.t8122](MACHOS/kernel.release.t8122.md)
- [/System/Library/Kernels/kernel.release.vmapple](MACHOS/kernel.release.vmapple.md)
- [/System/Library/Messages/PlugIns/RCS.imservice/Contents/MacOS/RCS](MACHOS/RCS.md)
- [/System/Library/Messages/PlugIns/SMS.imservice/Contents/MacOS/SMS](MACHOS/SMS.md)
- [/System/Library/Messages/PlugIns/iMessage.imservice/Contents/MacOS/iMessage](MACHOS/iMessage.md)
- [/System/Library/Messages/iMessageBalloons/RichLinkProvider.bundle/Contents/MacOS/RichLinkProvider](MACHOS/RichLinkProvider.md)
- [/System/Library/PDF Services/Save to Web Receipts](MACHOS/Save_to_Web_Receipts.md)
- [/System/Library/PDF Services/Save to iCloud Drive](MACHOS/Save_to_iCloud_Drive.md)
- [/System/Library/Printers/Libraries/makequeuesagent](MACHOS/makequeuesagent.md)
- [/System/Library/PrivateFrameworks/AACCore.framework/Versions/A/XPCServices/AssessmentUIService.xpc/Contents/MacOS/AssessmentUIService](MACHOS/AssessmentUIService.md)
- [/System/Library/PrivateFrameworks/AMPDevices.framework/Versions/A/Support/AMPDeviceDiscoveryAgent](MACHOS/AMPDeviceDiscoveryAgent.md)
- [/System/Library/PrivateFrameworks/AMPDevices.framework/Versions/A/Support/AMPDevicesAgent](MACHOS/AMPDevicesAgent.md)
- [/System/Library/PrivateFrameworks/AMPLibrary.framework/Versions/A/Support/AMPArtworkAgent](MACHOS/AMPArtworkAgent.md)
- [/System/Library/PrivateFrameworks/AMPLibrary.framework/Versions/A/Support/AMPLibraryAgent](MACHOS/AMPLibraryAgent.md)
- [/System/Library/PrivateFrameworks/AMPSharing.framework/Versions/A/PlugIns/SharingPrefsExtension.appex/Contents/MacOS/SharingPrefsExtension](MACHOS/SharingPrefsExtension.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/Versions/A/XPCServices/ASOctaneSupportXPCService.xpc/Contents/MacOS/ASOctaneSupportXPCService](MACHOS/ASOctaneSupportXPCService.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/Versions/A/Support/MotionTrackingAgent](MACHOS/MotionTrackingAgent.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/Versions/A/XPCServices/HeuristicInterpreter.xpc/Contents/MacOS/HeuristicInterpreter](MACHOS/HeuristicInterpreter.md)
- [/System/Library/PrivateFrameworks/AppSSO.framework/Support/AppSSODaemon](MACHOS/AppSSODaemon.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd](MACHOS/appstorecomponentsd.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstoreagent](MACHOS/appstoreagent.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Versions/A/XPCServices/com.apple.AppStoreDaemon.StoreUIService.xpc/Contents/MacOS/com.apple.AppStoreDaemon.StoreUIService](MACHOS/com.apple.AppStoreDaemon.StoreUIService.md)
- [/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/Versions/A/XPCServices/AppleDeviceQueryService.xpc/Contents/MacOS/AppleDeviceQueryService](MACHOS/AppleDeviceQueryService.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/Versions/A/Resources/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/Versions/A/AppleMediaServicesUIDynamic](MACHOS/AppleMediaServicesUIDynamic.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/Versions/A/XPCServices/AppleMediaServicesUIDynamicService.xpc/Contents/MacOS/AppleMediaServicesUIDynamicService](MACHOS/AppleMediaServicesUIDynamicService.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIPaymentSheets.framework/Versions/A/XPCServices/AMSUIPaymentViewService_macOS.xpc/Contents/MacOS/AMSUIPaymentViewService_macOS](MACHOS/AMSUIPaymentViewService_macOS.md)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/apsd](MACHOS/apsd.md)
- [/System/Library/PrivateFrameworks/AskPermission.framework/Versions/A/Resources/AskPermissionUI.app/Contents/MacOS/AskPermissionUI](MACHOS/AskPermissionUI.md)
- [/System/Library/PrivateFrameworks/AskPermission.framework/Versions/A/Resources/askpermissiond](MACHOS/askpermissiond.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/PlugIns/RAQLPreviewExtension.appex/Contents/MacOS/RAQLPreviewExtension](MACHOS/RAQLPreviewExtension.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/PlugIns/RAQLThumbnailExtension.appex/Contents/MacOS/RAQLThumbnailExtension](MACHOS/RAQLThumbnailExtension.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/Versions/A/XPCServices/RAQL-Inline-Service.xpc/Contents/MacOS/RAQL-Inline-Service](MACHOS/RAQL-Inline-Service.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/Support/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/Support/akd](MACHOS/akd.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKAppSSOExtension_macOS.appex/Contents/MacOS/AKAppSSOExtension_macOS](MACHOS/AKAppSSOExtension_macOS.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/Versions/A/XPCServices/AKAuthorizationRemoteViewService.xpc/Contents/MacOS/AKAuthorizationRemoteViewService](MACHOS/AKAuthorizationRemoteViewService.md)
- [/System/Library/PrivateFrameworks/AvatarPersistence.framework/Support/avatarsd](MACHOS/avatarsd.md)
- [/System/Library/PrivateFrameworks/BackgroundTaskManagement.framework/Support/BackgroundTaskManagementAgent.app/Contents/MacOS/BackgroundTaskManagementAgent](MACHOS/BackgroundTaskManagementAgent.md)
- [/System/Library/PrivateFrameworks/BackgroundTaskManagement.framework/Versions/A/Resources/backgroundtaskmanagementd](MACHOS/backgroundtaskmanagementd.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/Support/BiomeAgent](MACHOS/BiomeAgent.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/Support/biomed](MACHOS/biomed.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored](MACHOS/bookdatastored.md)
- [/System/Library/PrivateFrameworks/BookKit.framework/Versions/A/XPCServices/com.apple.BKAgentService.xpc/Contents/MacOS/com.apple.BKAgentService](MACHOS/com.apple.BKAgentService.md)
- [/System/Library/PrivateFrameworks/BookLibraryCore.framework/Support/bookassetd](MACHOS/bookassetd.md)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/businessservicesd](MACHOS/businessservicesd.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted](MACHOS/deleted.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/Support/CallHistoryPluginHelper](MACHOS/CallHistoryPluginHelper.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/Support/CallHistorySyncHelper](MACHOS/CallHistorySyncHelper.md)
- [/System/Library/PrivateFrameworks/CascadeSets.framework/Versions/A/XPCServices/SetStoreUpdateService.xpc/Contents/MacOS/SetStoreUpdateService](MACHOS/SetStoreUpdateService.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod](MACHOS/chronod.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/cloudd](MACHOS/cloudd.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Versions/A/Support/cloudphotod](MACHOS/cloudphotod.md)
- [/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd](MACHOS/com.apple.sbd.md)
- [/System/Library/PrivateFrameworks/CloudSharing.framework/Versions/A/XPCServices/SPIHelper.xpc/Contents/MacOS/SPIHelper](MACHOS/SPIHelper.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/Versions/A/PlugIns/CloudSharingUISKExtension.appex/Contents/MacOS/CloudSharingUISKExtension](MACHOS/CloudSharingUISKExtension.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/Versions/A/XPCServices/ManageViewService.xpc/Contents/MacOS/ManageViewService](MACHOS/ManageViewService.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/Versions/A/XPCServices/com.apple.CloudSharingUI.AddParticipants.xpc/Contents/MacOS/com.apple.CloudSharingUI.AddParticipants](MACHOS/com.apple.CloudSharingUI.AddParticipants.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/Versions/A/XPCServices/CloudTelemetryService.xpc/Contents/MacOS/CloudTelemetryService](MACHOS/CloudTelemetryService.md)
- [/System/Library/PrivateFrameworks/CommerceKit.framework/Versions/A/Resources/storedownloadd](MACHOS/storedownloadd.md)
- [/System/Library/PrivateFrameworks/CommerceKit.framework/Versions/A/Resources/storeuid.app/Contents/MacOS/storeuid](MACHOS/storeuid.md)
- [/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CMFSyncAgent](MACHOS/CMFSyncAgent.md)
- [/System/Library/PrivateFrameworks/ConfigurationProfiles.framework/XPCServices/ExecutionPolicyService.xpc/Contents/MacOS/ExecutionPolicyService](MACHOS/ExecutionPolicyService.md)
- [/System/Library/PrivateFrameworks/ConfigurationProfiles.framework/XPCServices/SystemExtensionsMDM.xpc/Contents/MacOS/SystemExtensionsMDM](MACHOS/SystemExtensionsMDM.md)
- [/System/Library/PrivateFrameworks/ContactsDonation.framework/Versions/A/Support/contactsdonationagent](MACHOS/contactsdonationagent.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd](MACHOS/accessoryd.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd](MACHOS/analyticsd.md)
- [/System/Library/PrivateFrameworks/CoreFollowUp.framework/Versions/A/Support/followupd](MACHOS/followupd.md)
- [/System/Library/PrivateFrameworks/CoreLocationTiles.framework/Versions/A/XPCServices/TilesService.xpc/Contents/MacOS/TilesService](MACHOS/TilesService.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/PlugIns/SearchPoirotExtension.appex/Contents/MacOS/SearchPoirotExtension](MACHOS/SearchPoirotExtension.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf](MACHOS/parsec-fbf.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/CoreRC.framework/PlugIns/CoreRCHIDService.plugin/Contents/MacOS/CoreRCHIDService](MACHOS/CoreRCHIDService.md)
- [/System/Library/PrivateFrameworks/CoreRoutine.framework/Versions/A/XPCServices/CoreRoutineHelperService.xpc/Contents/MacOS/CoreRoutineHelperService](MACHOS/CoreRoutineHelperService.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd](MACHOS/corespeechd.md)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/Tools/suggest_tool](MACHOS/suggest_tool.md)
- [/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod](MACHOS/threadradiod.md)
- [/System/Library/PrivateFrameworks/DataDetectors.framework/Versions/A/XPCServices/DataDetectorsViewService.xpc/Contents/MacOS/DataDetectorsViewService](MACHOS/DataDetectorsViewService.md)
- [/System/Library/PrivateFrameworks/DendriteIngest.framework/Versions/A/XPCServices/IngestService.xpc/Contents/MacOS/IngestService](MACHOS/IngestService.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/A/Resources/DesktopServicesHelper](MACHOS/DesktopServicesHelper.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/A/XPCServices/ArchiveService.xpc/Contents/MacOS/ArchiveService](MACHOS/ArchiveService.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/A/XPCServices/QuarantineService.xpc/Contents/MacOS/QuarantineService](MACHOS/QuarantineService.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/Contents/MacOS/AirPlayDiagnosticExtension](MACHOS/AirPlayDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.sysdiagnose.appex/Contents/MacOS/com.apple.DiagnosticExtensions.sysdiagnose](MACHOS/com.apple.DiagnosticExtensions.sysdiagnose.md)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/XPCServices/DPSubmissionService.xpc/Contents/MacOS/DPSubmissionService](MACHOS/DPSubmissionService.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/Versions/A/XPCServices/diskimagescontroller.xpc/Contents/MacOS/diskimagescontroller](MACHOS/diskimagescontroller.md)
- [/System/Library/PrivateFrameworks/EFILogin.framework/Versions/A/Resources/efilogin-helper](MACHOS/efilogin-helper.md)
- [/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/Support/ecosystemanalyticsd](MACHOS/ecosystemanalyticsd.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/Versions/A/maild](MACHOS/maild.md)
- [/System/Library/PrivateFrameworks/EventMetaDataExtractor.framework/PlugIns/EventMetaDataExtractorPluginMac.appex/Contents/MacOS/EventMetaDataExtractorPluginMac](MACHOS/EventMetaDataExtractorPluginMac.md)
- [/System/Library/PrivateFrameworks/FaceTimeNotificationViewBridge.framework/Versions/A/XPCServices/FaceTimeNotificationViewBridgeService.xpc/Contents/MacOS/FaceTimeNotificationViewBridgeService](MACHOS/FaceTimeNotificationViewBridgeService.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/Versions/A/Resources/familycircled](MACHOS/familycircled.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/Versions/A/Resources/TypographyPanel.bundle/Contents/MacOS/TypographyPanel](MACHOS/TypographyPanel.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libGPUCompilerImplLazy.dylib](MACHOS/libGPUCompilerImplLazy.dylib.md)
- [/System/Library/PrivateFrameworks/GPUToolsCapture.framework/Versions/A/GPUToolsCapture](MACHOS/GPUToolsCapture.md)
- [/System/Library/PrivateFrameworks/GameCenterFoundation.framework/Versions/A/gamed](MACHOS/gamed.md)
- [/System/Library/PrivateFrameworks/GameCenterUICore.framework/XPCServices/com.apple.gamecenter.GameCenterUIService.xpc/Contents/MacOS/com.apple.gamecenter.GameCenterUIService](MACHOS/com.apple.gamecenter.GameCenterUIService.md)
- [/System/Library/PrivateFrameworks/GenerationalStorage.framework/Versions/A/Support/revisiond](MACHOS/revisiond.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/Versions/A/GenerativeModelsDiagnostics.appex/Contents/MacOS/GenerativeModelsDiagnostics](MACHOS/GenerativeModelsDiagnostics.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/Versions/A/generativeexperiencesd](MACHOS/generativeexperiencesd.md)
- [/System/Library/PrivateFrameworks/HelpData.framework/Versions/A/Resources/helpd](MACHOS/helpd.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed](MACHOS/homed.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/Versions/A/HomeKitDaemonLegacy](MACHOS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/Hydra.framework/Versions/C/XPCServices/HydraRenderingService.xpc/Contents/MacOS/HydraRenderingService](MACHOS/HydraRenderingService.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/Contents/MacOS/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/Contents/MacOS/imagent](MACHOS/imagent.md)
- [/System/Library/PrivateFrameworks/IMTransferServices.framework/IMTransferAgent.app/Contents/MacOS/IMTransferAgent](MACHOS/IMTransferAgent.md)
- [/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd](MACHOS/installcoordinationd.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/Versions/A/intelligencecontextd](MACHOS/intelligencecontextd.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/Versions/A/intelligenceflowd](MACHOS/intelligenceflowd.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/PlugIns/DiagnosticExtension.appex/Contents/MacOS/DiagnosticExtension](MACHOS/DiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/Versions/A/XPCServices/IntelligencePlatformComputeService.xpc/Contents/MacOS/IntelligencePlatformComputeService](MACHOS/IntelligencePlatformComputeService.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/Versions/A/intelligenceplatformd](MACHOS/intelligenceplatformd.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/Versions/A/knowledgeconstructiond](MACHOS/knowledgeconstructiond.md)
- [/System/Library/PrivateFrameworks/MailUI.framework/Versions/A/PlugIns/MailUIWebBundle.bundle/Contents/MacOS/MailUIWebBundle](MACHOS/MailUIWebBundle.md)
- [/System/Library/PrivateFrameworks/ManagedClient.framework/PlugIns/ManagedSettingsMacOSExtension.appex/Contents/MacOS/ManagedSettingsMacOSExtension](MACHOS/ManagedSettingsMacOSExtension.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/mapssyncd](MACHOS/mapssyncd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/Versions/A/mediaanalysisd](MACHOS/mediaanalysisd.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted](MACHOS/mediaremoted.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/Versions/A/XPCServices/MessagesAirlockService.xpc/Contents/MacOS/MessagesAirlockService](MACHOS/MessagesAirlockService.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/Versions/A/XPCServices/MessagesBlastDoorService.xpc/Contents/MacOS/MessagesBlastDoorService](MACHOS/MessagesBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MetricMeasurement.framework/Versions/A/XPCServices/MetricMeasurementHelper.xpc/Contents/MacOS/MetricMeasurementHelper](MACHOS/MetricMeasurementHelper.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd](MACHOS/accessoryupdaterd.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/fudHelperAgent](MACHOS/fudHelperAgent.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/Contents/MacOS/EAUpdaterService](MACHOS/EAUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceDFU.xpc/Contents/MacOS/UARPUpdaterServiceDFU](MACHOS/UARPUpdaterServiceDFU.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceHID.xpc/Contents/MacOS/UARPUpdaterServiceHID](MACHOS/UARPUpdaterServiceHID.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/Contents/MacOS/UARPUpdaterServiceLegacyAudio](MACHOS/UARPUpdaterServiceLegacyAudio.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceUSBPD.xpc/Contents/MacOS/UARPUpdaterServiceUSBPD](MACHOS/UARPUpdaterServiceUSBPD.md)
- [/System/Library/PrivateFrameworks/MobileInstallation.framework/Support/appinstalld](MACHOS/appinstalld.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/Versions/A/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/Contents/MacOS/com.apple.MobileSoftwareUpdate.CleanupPreparePathService](MACHOS/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.md)
- [/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/Versions/A/modelcatalogd](MACHOS/modelcatalogd.md)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd](MACHOS/newsd.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/Contents/LinkedNotesUIService.app/Contents/MacOS/LinkedNotesUIService](MACHOS/LinkedNotesUIService.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/People.framework/peopled](MACHOS/peopled.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/Versions/A/Support/photolibraryd](MACHOS/photolibraryd.md)
- [/System/Library/PrivateFrameworks/PodcastServices.framework/XPCServices/PodcastContentService.xpc/Contents/MacOS/PodcastContentService](MACHOS/PodcastContentService.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Support/previewsd](MACHOS/previewsd.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Versions/A/XPCServices/PreviewShellMac.xpc/Contents/MacOS/PreviewShellMac](MACHOS/PreviewShellMac.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/Contents/MacOS/privatecloudcomputed](MACHOS/privatecloudcomputed.md)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/Helpers/ProtectedCloudKeySyncing](MACHOS/ProtectedCloudKeySyncing.md)
- [/System/Library/PrivateFrameworks/ReminderKitUI.framework/Versions/A/XPCServices/com.apple.ReminderKitUI.ReminderCreationViewService.xpc/Contents/MacOS/com.apple.ReminderKitUI.ReminderCreationViewService](MACHOS/com.apple.ReminderKitUI.ReminderCreationViewService.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagementAgent](MACHOS/RemoteManagementAgent.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/DiskManagementSubscriber.xpc/Contents/MacOS/DiskManagementSubscriber](MACHOS/DiskManagementSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/InteractiveLegacyProfilesSubscriber.xpc/Contents/MacOS/InteractiveLegacyProfilesSubscriber](MACHOS/InteractiveLegacyProfilesSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/LegacyProfilesSubscriber.xpc/Contents/MacOS/LegacyProfilesSubscriber](MACHOS/LegacyProfilesSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagedConfigurationFilesSubscriber.xpc/Contents/MacOS/ManagedConfigurationFilesSubscriber](MACHOS/ManagedConfigurationFilesSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/PasscodeSettingsSubscriber.xpc/Contents/MacOS/PasscodeSettingsSubscriber](MACHOS/PasscodeSettingsSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/SecuritySubscriber.xpc/Contents/MacOS/SecuritySubscriber](MACHOS/SecuritySubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/remotemanagementd](MACHOS/remotemanagementd.md)
- [/System/Library/PrivateFrameworks/RemotePairingDevice.framework/Versions/A/RemotePairingDevice](MACHOS/RemotePairingDevice.md)
- [/System/Library/PrivateFrameworks/RenderBox.framework/Versions/A/Resources/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/PrivateFrameworks/ReplicatorCore.framework/Support/replicatord](MACHOS/replicatord.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/Versions/A/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/SensingPredictServices.framework/Versions/A/XPCServices/SensingPredictXPCService.xpc/Contents/MacOS/SensingPredictXPCService](MACHOS/SensingPredictXPCService.md)
- [/System/Library/PrivateFrameworks/SidecarCore.framework/Versions/A/XPCServices/DisplayMarkup.xpc/Contents/MacOS/DisplayMarkup](MACHOS/DisplayMarkup.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/Versions/A/XPCServices/SAExtensionOrchestrator.xpc/Contents/MacOS/SAExtensionOrchestrator](MACHOS/SAExtensionOrchestrator.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/Versions/A/siriinferenced](MACHOS/siriinferenced.md)
- [/System/Library/PrivateFrameworks/SiriSignals.framework/PlugIns/MusicAppSelectionPFLPlugin.appex/Contents/MacOS/MusicAppSelectionPFLPlugin](MACHOS/MusicAppSelectionPFLPlugin.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd](MACHOS/sirittsd.md)
- [/System/Library/PrivateFrameworks/SiriTTSTraining.framework/SiriTTSTrainingAgent](MACHOS/SiriTTSTrainingAgent.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdate.framework/Versions/A/Resources/SoftwareUpdateNotificationManager.app/Contents/MacOS/SoftwareUpdateNotificationManager](MACHOS/SoftwareUpdateNotificationManager.md)
- [/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond](MACHOS/spaceattributiond.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/Versions/A/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/Contents/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/Contents/MacOS/com.apple.SpeechRecognitionCore.speechrecognitiond](MACHOS/com.apple.SpeechRecognitionCore.speechrecognitiond.md)
- [/System/Library/PrivateFrameworks/StatusKit.framework/StatusKitAgent](MACHOS/StatusKitAgent.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Support/stickersd](MACHOS/stickersd.md)
- [/System/Library/PrivateFrameworks/StorageManagement.framework/Versions/A/Resources/diskspaced](MACHOS/diskspaced.md)
- [/System/Library/PrivateFrameworks/Synapse.framework/Support/contentlinkingd](MACHOS/contentlinkingd.md)
- [/System/Library/PrivateFrameworks/SyncedDefaults.framework/Support/syncdefaultsd](MACHOS/syncdefaultsd.md)
- [/System/Library/PrivateFrameworks/SystemMigration.framework/Versions/A/Resources/DirectorySurgeon](MACHOS/DirectorySurgeon.md)
- [/System/Library/PrivateFrameworks/SystemMigration.framework/Versions/A/Resources/compatchecker](MACHOS/compatchecker.md)
- [/System/Library/PrivateFrameworks/SystemMigration.framework/Versions/A/Resources/safecp](MACHOS/safecp.md)
- [/System/Library/PrivateFrameworks/SystemMigration.framework/Versions/A/Resources/systemmigrationd](MACHOS/systemmigrationd.md)
- [/System/Library/PrivateFrameworks/SystemMigrationUtils.framework/Versions/A/Resources/Tools/drop_sip](MACHOS/drop_sip.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/PlugIns/PhoneIntentHandler.appex/Contents/MacOS/PhoneIntentHandler](MACHOS/PhoneIntentHandler.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/PlugIns/SiriAUSP.appex/Contents/MacOS/SiriAUSP](MACHOS/SiriAUSP.md)
- [/System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/Versions/A/PlugIns/MauiAUSP.appex/Contents/MacOS/MauiAUSP](MACHOS/MauiAUSP.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/PlugIns/VoiceBankingDiagnostics.appex/Contents/MacOS/VoiceBankingDiagnostics](MACHOS/VoiceBankingDiagnostics.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/Support/voicebankingd](MACHOS/voicebankingd.md)
- [/System/Library/PrivateFrameworks/TimelineUI.framework/Versions/A/TimelineUI](MACHOS/TimelineUI.md)
- [/System/Library/PrivateFrameworks/TranslationUIServices.framework/PlugIns/TranslationUIService.appex/Contents/MacOS/TranslationUIService](MACHOS/TranslationUIService.md)
- [/System/Library/PrivateFrameworks/UVFSXPCService.framework/Versions/A/XPCServices/UVFSService.xpc/Contents/MacOS/UVFSService](MACHOS/UVFSService.md)
- [/System/Library/PrivateFrameworks/UniversalAccess.framework/Versions/A/Resources/AXVisualSupportAgent.app/Contents/MacOS/AXVisualSupportAgent](MACHOS/AXVisualSupportAgent.md)
- [/System/Library/PrivateFrameworks/UniversalAccess.framework/Versions/A/Resources/Accessibility Tutorial.app/Contents/MacOS/Accessibility Tutorial](MACHOS/Accessibility_Tutorial.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/Versions/A/UsageTrackingAgent](MACHOS/UsageTrackingAgent.md)
- [/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd](MACHOS/useractivityd.md)
- [/System/Library/PrivateFrameworks/VideoProcessing.framework/Versions/A/PlugIns/Codecs/VCPRealtimeEncoder.bundle/Contents/MacOS/VCPRealtimeEncoder](MACHOS/VCPRealtimeEncoder.md)
- [/System/Library/PrivateFrameworks/VisualUnderstanding.framework/Plugins.bundle/Contents/MacOS/Plugins](MACHOS/Plugins.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Versions/A/Support/siriactionsd](MACHOS/siriactionsd.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/weatherd](MACHOS/weatherd.md)
- [/System/Library/PrivateFrameworks/WebPrivacy.framework/Versions/A/webprivacyd](MACHOS/webprivacyd.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/Contents/MacOS/BackgroundShortcutRunner](MACHOS/BackgroundShortcutRunner.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/ShortcutsViewService.xpc/Contents/MacOS/ShortcutsViewService](MACHOS/ShortcutsViewService.md)
- [/System/Library/PrivateFrameworks/WorkflowUIServices.framework/XPCServices/FocusConfigurationXPCServiceMac.xpc/Contents/MacOS/FocusConfigurationXPCServiceMac](MACHOS/FocusConfigurationXPCServiceMac.md)
- [/System/Library/PrivateFrameworks/WritingToolsUI.framework/Versions/A/XPCServices/WritingToolsViewService.xpc/Contents/MacOS/WritingToolsViewService](MACHOS/WritingToolsViewService.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/Versions/A/XPCServices/ZhuGeService.xpc/Contents/MacOS/ZhuGeService](MACHOS/ZhuGeService.md)
- [/System/Library/PrivateFrameworks/iCloudNotification.framework/iCloudNotificationAgent](MACHOS/iCloudNotificationAgent.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd](MACHOS/itunescloudd.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/HomeAutomationSiriSuggestions.bundle/Contents/MacOS/HomeAutomationSiriSuggestions](MACHOS/HomeAutomationSiriSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriLinkSuggestionsPlugin.bundle/Contents/MacOS/SiriLinkSuggestionsPlugin](MACHOS/SiriLinkSuggestionsPlugin.md)
- [/System/Library/Snippets/UIPlugins/AudioUIPlugin.bundle/Contents/MacOS/AudioUIPlugin](MACHOS/AudioUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/ContactsFlowUIPlugin.bundle/Contents/MacOS/ContactsFlowUIPlugin](MACHOS/ContactsFlowUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/FindMyUIPlugin.bundle/Contents/MacOS/FindMyUIPlugin](MACHOS/FindMyUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/ResponseGenerationUIPlugin.bundle/Contents/MacOS/ResponseGenerationUIPlugin](MACHOS/ResponseGenerationUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriInferenceFlowsUIPlugin.bundle/Contents/MacOS/SiriInferenceFlowsUIPlugin](MACHOS/SiriInferenceFlowsUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriPaymentsUIPlugin.bundle/Contents/MacOS/SiriPaymentsUIPlugin](MACHOS/SiriPaymentsUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SystemPlugin.bundle/Contents/MacOS/SystemPlugin](MACHOS/SystemPlugin.md)
- [/System/Library/Spotlight/CoreMedia.mdimporter/Contents/MacOS/CoreMedia](MACHOS/CoreMedia.md)
- [/System/Library/SystemConfiguration/EAPOLController.bundle/Contents/Resources/eapolclient](MACHOS/eapolclient.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorAdload](MACHOS/XProtectRemediatorAdload.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorBadGacha](MACHOS/XProtectRemediatorBadGacha.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorBlueTop](MACHOS/XProtectRemediatorBlueTop.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorCardboardCutout](MACHOS/XProtectRemediatorCardboardCutout.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorColdSnap](MACHOS/XProtectRemediatorColdSnap.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorCrapyrator](MACHOS/XProtectRemediatorCrapyrator.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorDubRobber](MACHOS/XProtectRemediatorDubRobber.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorEicar](MACHOS/XProtectRemediatorEicar.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorFloppyFlipper](MACHOS/XProtectRemediatorFloppyFlipper.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorGenieo](MACHOS/XProtectRemediatorGenieo.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorGreenAcre](MACHOS/XProtectRemediatorGreenAcre.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorKeySteal](MACHOS/XProtectRemediatorKeySteal.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorMRTv3](MACHOS/XProtectRemediatorMRTv3.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorPirrit](MACHOS/XProtectRemediatorPirrit.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorRankStank](MACHOS/XProtectRemediatorRankStank.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorRedPine](MACHOS/XProtectRemediatorRedPine.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorRoachFlight](MACHOS/XProtectRemediatorRoachFlight.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorSheepSwap](MACHOS/XProtectRemediatorSheepSwap.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorSnowBeagle](MACHOS/XProtectRemediatorSnowBeagle.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorSnowDrift](MACHOS/XProtectRemediatorSnowDrift.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorToyDrop](MACHOS/XProtectRemediatorToyDrop.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorTrovi](MACHOS/XProtectRemediatorTrovi.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorWaterNet](MACHOS/XProtectRemediatorWaterNet.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/Resources/libXProtectPayloads.dylib](MACHOS/libXProtectPayloads.dylib.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/Mercury.framework/Versions/A/Mercury](MACHOS/Mercury.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/MobileDevice.framework/Versions/A/MobileDevice](MACHOS/MobileDevice.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/RemotePairing.framework/Versions/A/RemotePairing](MACHOS/RemotePairing.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/RemotePairing.framework/Versions/A/Resources/bin/RemotePairingDataVaultHelper](MACHOS/RemotePairingDataVaultHelper.md)
- [/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/RemotePairing.framework/Versions/A/XPCServices/remotepairingd.xpc/Contents/MacOS/remotepairingd](MACHOS/remotepairingd.md)
- [/System/Library/Templates/Data/Library/Application Support/iLifeMediaBrowser/Plug-Ins/iLMBPhotosPlugin.ilmbplugin/Contents/MacOS/iLMBPhotosPlugin](MACHOS/iLMBPhotosPlugin.md)
- [/System/Library/TextInput/TextInput_ko.bundle/Versions/A/TextInput_ko](MACHOS/TextInput_ko.md)
- [/System/Library/TextInput/TextInput_pa.bundle/Versions/A/TextInput_pa](MACHOS/TextInput_pa.md)
- [/System/Library/TextInput/TextInput_th.bundle/Versions/A/TextInput_th](MACHOS/TextInput_th.md)
- [/System/Library/Trace/Providers/Required.bundle/Contents/MacOS/Required](MACHOS/Required.md)
- [/System/Library/UserEventPlugins/com.apple.nsurlsessiond.plugin/Contents/MacOS/com.apple.nsurlsessiond](MACHOS/com.apple.nsurlsessiond.md)
- [/System/Library/UserNotifications/Bundles/com.apple.ScreenTimeEnabledNotifications.bundle/Contents/MacOS/com.apple.ScreenTimeEnabledNotifications](MACHOS/com.apple.ScreenTimeEnabledNotifications.md)
- [/System/Library/Video/Plug-Ins/AppleMCTF.bundle/Contents/MacOS/AppleMCTF](MACHOS/AppleMCTF.md)
- [/System/Library/Video/Plug-Ins/AppleProResHWDecoder.bundle/Contents/MacOS/AppleProResHWDecoder](MACHOS/AppleProResHWDecoder.md)
- [/System/Library/Video/Plug-Ins/AppleProResHWEncoder.bundle/Contents/MacOS/AppleProResHWEncoder](MACHOS/AppleProResHWEncoder.md)
- [/System/Library/Video/Plug-Ins/AppleVideoDecoder.bundle/Contents/MacOS/AppleVideoDecoder](MACHOS/AppleVideoDecoder.md)
- [/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/Contents/MacOS/AppleVideoEncoder](MACHOS/AppleVideoEncoder.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/InvertColorsManager.bundle/Contents/MacOS/InvertColorsManager](MACHOS/InvertColorsManager.md)
- [/System/iOSSupport/System/Library/AppleMediaServices/DynamicUI/PlugIns/CoreDynamicUIPlugin.bundle/Contents/MacOS/CoreDynamicUIPlugin](MACHOS/CoreDynamicUIPlugin.md)
- [/System/iOSSupport/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/Contents/MacOS/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/iOSSupport/System/Library/Frameworks/BusinessChat.framework/PlugIns/Business.appex/Contents/MacOS/Business](MACHOS/Business.md)
- [/System/iOSSupport/System/Library/Frameworks/GameController.framework/Versions/A/Resources/GameControllerSettings-macOS.bundle/Contents/MacOS/GameControllerSettings-macOS](MACHOS/GameControllerSettings-macOS.md)
- [/System/iOSSupport/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc](MACHOS/jsc.md)
- [/System/iOSSupport/System/Library/Messages/iMessageApps/FindMyMessagesApp.bundle/Contents/MacOS/FindMyMessagesApp](MACHOS/FindMyMessagesApp.md)
- [/System/iOSSupport/System/Library/Messages/iMessageApps/SafetyMonitorMessages.bundle/Contents/MacOS/SafetyMonitorMessages](MACHOS/SafetyMonitorMessages.md)
- [/System/iOSSupport/System/Library/Messages/iMessageBalloons/RichLinkProvider.bundle/Contents/MacOS/RichLinkProvider](MACHOS/RichLinkProvider.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/AuthKitUIMacHelper.framework/Versions/A/XPCServices/AKAuthorizationRemoteViewService.xpc/Contents/MacOS/AKAuthorizationRemoteViewService](MACHOS/AKAuthorizationRemoteViewService.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/AvatarUI.framework/PlugIns/StickersUltraExtension.appex/Contents/MacOS/StickersUltraExtension](MACHOS/StickersUltraExtension.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterMessageExtension.appex/Contents/MacOS/GameCenterMessageExtension](MACHOS/GameCenterMessageExtension.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/WidgetConfigurationExtension.appex/Contents/MacOS/WidgetConfigurationExtension](MACHOS/WidgetConfigurationExtension.md)
- [/bin/dash](MACHOS/dash.md)
- [/bin/launchctl](MACHOS/launchctl.md)
- [/sbin/launchd](MACHOS/launchd.md)
- [/sbin/mount](MACHOS/mount.md)
- [/sbin/nfsd](MACHOS/nfsd.md)
- [/sbin/ping6](MACHOS/ping6.md)
- [/usr/bin/DeRez](MACHOS/DeRez.md)
- [/usr/bin/GetFileInfo](MACHOS/GetFileInfo.md)
- [/usr/bin/ResMerger](MACHOS/ResMerger.md)
- [/usr/bin/Rez](MACHOS/Rez.md)
- [/usr/bin/SetFile](MACHOS/SetFile.md)
- [/usr/bin/SplitForks](MACHOS/SplitForks.md)
- [/usr/bin/actool](MACHOS/actool.md)
- [/usr/bin/agvtool](MACHOS/agvtool.md)
- [/usr/bin/ar](MACHOS/ar.md)
- [/usr/bin/as](MACHOS/as.md)
- [/usr/bin/asa](MACHOS/asa.md)
- [/usr/bin/assetutil](MACHOS/assetutil.md)
- [/usr/bin/atos](MACHOS/atos.md)
- [/usr/bin/automationmodetool](MACHOS/automationmodetool.md)
- [/usr/bin/automator](MACHOS/automator.md)
- [/usr/bin/avbanalyse](MACHOS/avbanalyse.md)
- [/usr/bin/bison](MACHOS/bison.md)
- [/usr/bin/bm4](MACHOS/bm4.md)
- [/usr/bin/brctl](MACHOS/brctl.md)
- [/usr/bin/c++](MACHOS/c++.md)
- [/usr/bin/c++filt](MACHOS/c++filt.md)
- [/usr/bin/c89](MACHOS/c89.md)
- [/usr/bin/c99](MACHOS/c99.md)
- [/usr/bin/cc](MACHOS/cc.md)
- [/usr/bin/clang](MACHOS/clang.md)
- [/usr/bin/clang++](MACHOS/clang++.md)
- [/usr/bin/clangd](MACHOS/clangd.md)
- [/usr/bin/cmpdylib](MACHOS/cmpdylib.md)
- [/usr/bin/codesign_allocate](MACHOS/codesign_allocate.md)
- [/usr/bin/cpp](MACHOS/cpp.md)
- [/usr/bin/ctags](MACHOS/ctags.md)
- [/usr/bin/ctf_insert](MACHOS/ctf_insert.md)
- [/usr/bin/dddiagnose](MACHOS/dddiagnose.md)
- [/usr/bin/desdp](MACHOS/desdp.md)
- [/usr/bin/dist_package_tool](MACHOS/dist_package_tool.md)
- [/usr/bin/dsymutil](MACHOS/dsymutil.md)
- [/usr/bin/dwarfdump](MACHOS/dwarfdump.md)
- [/usr/bin/dyld_info](MACHOS/dyld_info.md)
- [/usr/bin/eslogger](MACHOS/eslogger.md)
- [/usr/bin/fileproviderctl](MACHOS/fileproviderctl.md)
- [/usr/bin/filtercalltree](MACHOS/filtercalltree.md)
- [/usr/bin/flex](MACHOS/flex.md)
- [/usr/bin/flex++](MACHOS/flex++.md)
- [/usr/bin/footprint](MACHOS/footprint.md)
- [/usr/bin/g++](MACHOS/g++.md)
- [/usr/bin/gatherheaderdoc](MACHOS/gatherheaderdoc.md)
- [/usr/bin/gcc](MACHOS/gcc.md)
- [/usr/bin/gcov](MACHOS/gcov.md)
- [/usr/bin/genstrings](MACHOS/genstrings.md)
- [/usr/bin/git](MACHOS/git.md)
- [/usr/bin/git-receive-pack](MACHOS/git-receive-pack.md)
- [/usr/bin/git-shell](MACHOS/git-shell.md)
- [/usr/bin/git-upload-archive](MACHOS/git-upload-archive.md)
- [/usr/bin/git-upload-pack](MACHOS/git-upload-pack.md)
- [/usr/bin/gm4](MACHOS/gm4.md)
- [/usr/bin/gnumake](MACHOS/gnumake.md)
- [/usr/bin/gperf](MACHOS/gperf.md)
- [/usr/bin/hdxml2manxml](MACHOS/hdxml2manxml.md)
- [/usr/bin/headerdoc2html](MACHOS/headerdoc2html.md)
- [/usr/bin/heap](MACHOS/heap.md)
- [/usr/bin/ibtool](MACHOS/ibtool.md)
- [/usr/bin/ictool](MACHOS/ictool.md)
- [/usr/bin/indent](MACHOS/indent.md)
- [/usr/bin/install_name_tool](MACHOS/install_name_tool.md)
- [/usr/bin/kmutil](MACHOS/kmutil.md)
- [/usr/bin/layerutil](MACHOS/layerutil.md)
- [/usr/bin/ld](MACHOS/ld.md)
- [/usr/bin/leaks](MACHOS/leaks.md)
- [/usr/bin/lex](MACHOS/lex.md)
- [/usr/bin/libtool](MACHOS/libtool.md)
- [/usr/bin/lipo](MACHOS/lipo.md)
- [/usr/bin/lldb](MACHOS/lldb.md)
- [/usr/bin/llvm-g++](MACHOS/llvm-g++.md)
- [/usr/bin/llvm-gcc](MACHOS/llvm-gcc.md)
- [/usr/bin/lorder](MACHOS/lorder.md)
- [/usr/bin/m4](MACHOS/m4.md)
- [/usr/bin/make](MACHOS/make.md)
- [/usr/bin/malloc_history](MACHOS/malloc_history.md)
- [/usr/bin/mig](MACHOS/mig.md)
- [/usr/bin/modelmanagerdump](MACHOS/modelmanagerdump.md)
- [/usr/bin/networkQuality](MACHOS/networkQuality.md)
- [/usr/bin/nm](MACHOS/nm.md)
- [/usr/bin/nmedit](MACHOS/nmedit.md)
- [/usr/bin/nscurl](MACHOS/nscurl.md)
- [/usr/bin/objdump](MACHOS/objdump.md)
- [/usr/bin/opendiff](MACHOS/opendiff.md)
- [/usr/bin/osacompile](MACHOS/osacompile.md)
- [/usr/bin/osascript](MACHOS/osascript.md)
- [/usr/bin/otool](MACHOS/otool.md)
- [/usr/bin/pagestuff](MACHOS/pagestuff.md)
- [/usr/bin/pip3](MACHOS/pip3.md)
- [/usr/bin/python3](MACHOS/python3.md)
- [/usr/bin/ranlib](MACHOS/ranlib.md)
- [/usr/bin/resolveLinks](MACHOS/resolveLinks.md)
- [/usr/bin/rpcgen](MACHOS/rpcgen.md)
- [/usr/bin/sample](MACHOS/sample.md)
- [/usr/bin/scp](MACHOS/scp.md)
- [/usr/bin/sdef](MACHOS/sdef.md)
- [/usr/bin/sdp](MACHOS/sdp.md)
- [/usr/bin/security](MACHOS/security.md)
- [/usr/bin/segedit](MACHOS/segedit.md)
- [/usr/bin/sftp](MACHOS/sftp.md)
- [/usr/bin/shazam](MACHOS/shazam.md)
- [/usr/bin/shortcuts](MACHOS/shortcuts.md)
- [/usr/bin/size](MACHOS/size.md)
- [/usr/bin/sourcekit-lsp](MACHOS/sourcekit-lsp.md)
- [/usr/bin/sqlite3](MACHOS/sqlite3.md)
- [/usr/bin/ssh](MACHOS/ssh.md)
- [/usr/bin/ssh-add](MACHOS/ssh-add.md)
- [/usr/bin/ssh-agent](MACHOS/ssh-agent.md)
- [/usr/bin/ssh-keygen](MACHOS/ssh-keygen.md)
- [/usr/bin/ssh-keyscan](MACHOS/ssh-keyscan.md)
- [/usr/bin/stapler](MACHOS/stapler.md)
- [/usr/bin/stringdups](MACHOS/stringdups.md)
- [/usr/bin/strings](MACHOS/strings.md)
- [/usr/bin/strip](MACHOS/strip.md)
- [/usr/bin/sudo](MACHOS/sudo.md)
- [/usr/bin/swift](MACHOS/swift.md)
- [/usr/bin/swift-inspect](MACHOS/swift-inspect.md)
- [/usr/bin/swiftc](MACHOS/swiftc.md)
- [/usr/bin/symbols](MACHOS/symbols.md)
- [/usr/bin/syscapturediags](MACHOS/syscapturediags.md)
- [/usr/bin/sysdiagnose](MACHOS/sysdiagnose.md)
- [/usr/bin/syspolicy_check](MACHOS/syspolicy_check.md)
- [/usr/bin/tailspin](MACHOS/tailspin.md)
- [/usr/bin/timesyncanalyse](MACHOS/timesyncanalyse.md)
- [/usr/bin/tmutil](MACHOS/tmutil.md)
- [/usr/bin/unifdef](MACHOS/unifdef.md)
- [/usr/bin/unifdefall](MACHOS/unifdefall.md)
- [/usr/bin/usdchecker](MACHOS/usdchecker.md)
- [/usr/bin/usdcrush](MACHOS/usdcrush.md)
- [/usr/bin/usdrecord](MACHOS/usdrecord.md)
- [/usr/bin/usdzip](MACHOS/usdzip.md)
- [/usr/bin/vmmap](MACHOS/vmmap.md)
- [/usr/bin/vtool](MACHOS/vtool.md)
- [/usr/bin/xcdebug](MACHOS/xcdebug.md)
- [/usr/bin/xcodebuild](MACHOS/xcodebuild.md)
- [/usr/bin/xcscontrol](MACHOS/xcscontrol.md)
- [/usr/bin/xcsdiagnose](MACHOS/xcsdiagnose.md)
- [/usr/bin/xctrace](MACHOS/xctrace.md)
- [/usr/bin/xed](MACHOS/xed.md)
- [/usr/bin/xml2man](MACHOS/xml2man.md)
- [/usr/bin/yacc](MACHOS/yacc.md)
- [/usr/lib/dyld](MACHOS/dyld.md)
- [/usr/lib/swift/libswiftRemoteMirror.dylib](MACHOS/libswiftRemoteMirror.dylib.md)
- [/usr/lib/zsh/5.9/zsh/complete.so](MACHOS/complete.so.md)
- [/usr/lib/zsh/5.9/zsh/computil.so](MACHOS/computil.so.md)
- [/usr/libexec/ASPCarryLog](MACHOS/ASPCarryLog.md)
- [/usr/libexec/AppleQEMUGuestAgent](MACHOS/AppleQEMUGuestAgent.md)
- [/usr/libexec/ApplicationFirewall/socketfilterfw](MACHOS/socketfilterfw.md)
- [/usr/libexec/AssetCache/AssetCache](MACHOS/AssetCache.md)
- [/usr/libexec/AssetCacheAgent/AssetCacheAgent](MACHOS/AssetCacheAgent.md)
- [/usr/libexec/CSCSupportd](MACHOS/CSCSupportd.md)
- [/usr/libexec/ContainerMigrationService](MACHOS/ContainerMigrationService.md)
- [/usr/libexec/DataDetectorsLocalSources](MACHOS/DataDetectorsLocalSources.md)
- [/usr/libexec/DataDetectorsSourceAccess](MACHOS/DataDetectorsSourceAccess.md)
- [/usr/libexec/DumpPanic](MACHOS/DumpPanic.md)
- [/usr/libexec/MTLAssetUpgraderD](MACHOS/MTLAssetUpgraderD.md)
- [/usr/libexec/NANDTaskScheduler](MACHOS/NANDTaskScheduler.md)
- [/usr/libexec/PowerUIAgent](MACHOS/PowerUIAgent.md)
- [/usr/libexec/SidecarDisplayAgent](MACHOS/SidecarDisplayAgent.md)
- [/usr/libexec/SidecarRelay](MACHOS/SidecarRelay.md)
- [/usr/libexec/TouchBarServer](MACHOS/TouchBarServer.md)
- [/usr/libexec/adprivacyd](MACHOS/adprivacyd.md)
- [/usr/libexec/airportd](MACHOS/airportd.md)
- [/usr/libexec/amfid](MACHOS/amfid.md)
- [/usr/libexec/aonsensed](MACHOS/aonsensed.md)
- [/usr/libexec/apfsd](MACHOS/apfsd.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/appleh13camerad](MACHOS/appleh13camerad.md)
- [/usr/libexec/appleh16camerad](MACHOS/appleh16camerad.md)
- [/usr/libexec/asktod](MACHOS/asktod.md)
- [/usr/libexec/assessmentagent](MACHOS/assessmentagent.md)
- [/usr/libexec/attach_automation_image](MACHOS/attach_automation_image.md)
- [/usr/libexec/audioanalyticsd](MACHOS/audioanalyticsd.md)
- [/usr/libexec/audioclocksyncd](MACHOS/audioclocksyncd.md)
- [/usr/libexec/automation_trampoline](MACHOS/automation_trampoline.md)
- [/usr/libexec/betaenrollmentd](MACHOS/betaenrollmentd.md)
- [/usr/libexec/biomesyncd](MACHOS/biomesyncd.md)
- [/usr/libexec/bluetoothuserd](MACHOS/bluetoothuserd.md)
- [/usr/libexec/bootinstalld](MACHOS/bootinstalld.md)
- [/usr/libexec/ciphermld](MACHOS/ciphermld.md)
- [/usr/libexec/companiond](MACHOS/companiond.md)
- [/usr/libexec/containermanagerd](MACHOS/containermanagerd.md)
- [/usr/libexec/containermanagerd_system](MACHOS/containermanagerd_system.md)
- [/usr/libexec/coordinated](MACHOS/coordinated.md)
- [/usr/libexec/corercd](MACHOS/corercd.md)
- [/usr/libexec/countryd](MACHOS/countryd.md)
- [/usr/libexec/create_automation_image_overlay](MACHOS/create_automation_image_overlay.md)
- [/usr/libexec/cryptexd](MACHOS/cryptexd.md)
- [/usr/libexec/dasd](MACHOS/dasd.md)
- [/usr/libexec/diagnosticextensionsd](MACHOS/diagnosticextensionsd.md)
- [/usr/libexec/diagnosticspushd](MACHOS/diagnosticspushd.md)
- [/usr/libexec/diskarbitrationd](MACHOS/diskarbitrationd.md)
- [/usr/libexec/diskimagesiod](MACHOS/diskimagesiod.md)
- [/usr/libexec/dmd](MACHOS/dmd.md)
- [/usr/libexec/duetexpertd](MACHOS/duetexpertd.md)
- [/usr/libexec/efiupdater](MACHOS/efiupdater.md)
- [/usr/libexec/eligibilityd](MACHOS/eligibilityd.md)
- [/usr/libexec/fairplaydeviceidentityd](MACHOS/fairplaydeviceidentityd.md)
- [/usr/libexec/feedbackd](MACHOS/feedbackd.md)
- [/usr/libexec/findmybeaconingd](MACHOS/findmybeaconingd.md)
- [/usr/libexec/findmydevice-user-agent](MACHOS/findmydevice-user-agent.md)
- [/usr/libexec/findmydeviced](MACHOS/findmydeviced.md)
- [/usr/libexec/findmylocateagent](MACHOS/findmylocateagent.md)
- [/usr/libexec/firmwaresyncd](MACHOS/firmwaresyncd.md)
- [/usr/libexec/fmfd](MACHOS/fmfd.md)
- [/usr/libexec/fskitd](MACHOS/fskitd.md)
- [/usr/libexec/gamecontrolleragentd](MACHOS/gamecontrolleragentd.md)
- [/usr/libexec/gamecontrollerd](MACHOS/gamecontrollerd.md)
- [/usr/libexec/gamepolicyd](MACHOS/gamepolicyd.md)
- [/usr/libexec/griddatad](MACHOS/griddatad.md)
- [/usr/libexec/handwritingd](MACHOS/handwritingd.md)
- [/usr/libexec/icloudmailagent](MACHOS/icloudmailagent.md)
- [/usr/libexec/kernelmanager_helper](MACHOS/kernelmanager_helper.md)
- [/usr/libexec/kernelmanagerd](MACHOS/kernelmanagerd.md)
- [/usr/libexec/keychainsharingmessagingd](MACHOS/keychainsharingmessagingd.md)
- [/usr/libexec/lightsoutmanagementd](MACHOS/lightsoutmanagementd.md)
- [/usr/libexec/linkd](MACHOS/linkd.md)
- [/usr/libexec/locationd](MACHOS/locationd.md)
- [/usr/libexec/logd_reporter](MACHOS/logd_reporter.md)
- [/usr/libexec/loginitemregisterd](MACHOS/loginitemregisterd.md)
- [/usr/libexec/managedeventsd](MACHOS/managedeventsd.md)
- [/usr/libexec/mc_notifier](MACHOS/mc_notifier.md)
- [/usr/libexec/mdmclient](MACHOS/mdmclient.md)
- [/usr/libexec/metrickitd](MACHOS/metrickitd.md)
- [/usr/libexec/microstackshot](MACHOS/microstackshot.md)
- [/usr/libexec/mlhostd](MACHOS/mlhostd.md)
- [/usr/libexec/mlruntimed](MACHOS/mlruntimed.md)
- [/usr/libexec/mmaintenanced](MACHOS/mmaintenanced.md)
- [/usr/libexec/modelmanagerd](MACHOS/modelmanagerd.md)
- [/usr/libexec/neagent](MACHOS/neagent.md)
- [/usr/libexec/nearbyd](MACHOS/nearbyd.md)
- [/usr/libexec/nehelper](MACHOS/nehelper.md)
- [/usr/libexec/nesessionmanager](MACHOS/nesessionmanager.md)
- [/usr/libexec/networkserviceproxy](MACHOS/networkserviceproxy.md)
- [/usr/libexec/nexusd](MACHOS/nexusd.md)
- [/usr/libexec/nfcd](MACHOS/nfcd.md)
- [/usr/libexec/nsurlsessiond](MACHOS/nsurlsessiond.md)
- [/usr/libexec/online-auth-agent](MACHOS/online-auth-agent.md)
- [/usr/libexec/ospredictiond](MACHOS/ospredictiond.md)
- [/usr/libexec/otherbsd](MACHOS/otherbsd.md)
- [/usr/libexec/pkd](MACHOS/pkd.md)
- [/usr/libexec/powerdatad](MACHOS/powerdatad.md)
- [/usr/libexec/powerexperienced](MACHOS/powerexperienced.md)
- [/usr/libexec/proactiveeventtrackerd](MACHOS/proactiveeventtrackerd.md)
- [/usr/libexec/promotedcontentd](MACHOS/promotedcontentd.md)
- [/usr/libexec/ptpcamerad](MACHOS/ptpcamerad.md)
- [/usr/libexec/rapportd](MACHOS/rapportd.md)
- [/usr/libexec/relatived](MACHOS/relatived.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/remoted](MACHOS/remoted.md)
- [/usr/libexec/replayd](MACHOS/replayd.md)
- [/usr/libexec/rosetta/oahd](MACHOS/oahd.md)
- [/usr/libexec/rosetta/oahd-helper](MACHOS/oahd-helper.md)
- [/usr/libexec/rsync/rsync.openrsync](MACHOS/rsync.openrsync.md)
- [/usr/libexec/rtcreportingd](MACHOS/rtcreportingd.md)
- [/usr/libexec/sandboxd](MACHOS/sandboxd.md)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd.md)
- [/usr/libexec/searchpartyuseragent](MACHOS/searchpartyuseragent.md)
- [/usr/libexec/secd](MACHOS/secd.md)
- [/usr/libexec/secinitd](MACHOS/secinitd.md)
- [/usr/libexec/securityd_system](MACHOS/securityd_system.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/seld](MACHOS/seld.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/sftp-server](MACHOS/sftp-server.md)
- [/usr/libexec/sharingd](MACHOS/sharingd.md)
- [/usr/libexec/slapconfig-keygen](MACHOS/slapconfig-keygen.md)
- [/usr/libexec/smd](MACHOS/smd.md)
- [/usr/libexec/sportsd](MACHOS/sportsd.md)
- [/usr/libexec/srp-mdns-proxy](MACHOS/srp-mdns-proxy.md)
- [/usr/libexec/ssh-apple-pkcs11](MACHOS/ssh-apple-pkcs11.md)
- [/usr/libexec/ssh-keysign](MACHOS/ssh-keysign.md)
- [/usr/libexec/ssh-pkcs11-helper](MACHOS/ssh-pkcs11-helper.md)
- [/usr/libexec/ssh-sk-helper](MACHOS/ssh-sk-helper.md)
- [/usr/libexec/sshd-keygen-wrapper](MACHOS/sshd-keygen-wrapper.md)
- [/usr/libexec/swcd](MACHOS/swcd.md)
- [/usr/libexec/swtransparencyd](MACHOS/swtransparencyd.md)
- [/usr/libexec/symptomsd](MACHOS/symptomsd.md)
- [/usr/libexec/symptomsd-diag](MACHOS/symptomsd-diag.md)
- [/usr/libexec/sysdiagnose_helper](MACHOS/sysdiagnose_helper.md)
- [/usr/libexec/sysdiagnosed](MACHOS/sysdiagnosed.md)
- [/usr/libexec/syspolicyd](MACHOS/syspolicyd.md)
- [/usr/libexec/tailspind](MACHOS/tailspind.md)
- [/usr/libexec/taskgated-helper](MACHOS/taskgated-helper.md)
- [/usr/libexec/teslad](MACHOS/teslad.md)
- [/usr/libexec/testmanagerd](MACHOS/testmanagerd.md)
- [/usr/libexec/textcontextd](MACHOS/textcontextd.md)
- [/usr/libexec/timed](MACHOS/timed.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/trustd](MACHOS/trustd.md)
- [/usr/libexec/tznotify](MACHOS/tznotify.md)
- [/usr/libexec/uarppersonalizationd](MACHOS/uarppersonalizationd.md)
- [/usr/libexec/wallpaperexportd](MACHOS/wallpaperexportd.md)
- [/usr/libexec/wifiFirmwareLoader](MACHOS/wifiFirmwareLoader.md)
- [/usr/libexec/wifip2pd](MACHOS/wifip2pd.md)
- [/usr/libexec/wifivelocityd](MACHOS/wifivelocityd.md)
- [/usr/libexec/x11-select](MACHOS/x11-select.md)
- [/usr/libexec/xpcproxy](MACHOS/xpcproxy.md)
- [/usr/libexec/xpcroleaccountd](MACHOS/xpcroleaccountd.md)
- [/usr/sbin/BTLEServer](MACHOS/BTLEServer.md)
- [/usr/sbin/BTLEServerAgent](MACHOS/BTLEServerAgent.md)
- [/usr/sbin/DevToolsSecurity](MACHOS/DevToolsSecurity.md)
- [/usr/sbin/WirelessRadioManagerd](MACHOS/WirelessRadioManagerd.md)
- [/usr/sbin/appleh13camerad](MACHOS/appleh13camerad.md)
- [/usr/sbin/appleh16camerad](MACHOS/appleh16camerad.md)
- [/usr/sbin/avbdeviced](MACHOS/avbdeviced.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/diskutil](MACHOS/diskutil.md)
- [/usr/sbin/mDNSResponder](MACHOS/mDNSResponder.md)
- [/usr/sbin/otctl](MACHOS/otctl.md)
- [/usr/sbin/rpc.statd](MACHOS/rpc.statd.md)
- [/usr/sbin/rpcbind](MACHOS/rpcbind.md)
- [/usr/sbin/screencapture](MACHOS/screencapture.md)
- [/usr/sbin/skywalkctl](MACHOS/skywalkctl.md)
- [/usr/sbin/smbd](MACHOS/smbd.md)
- [/usr/sbin/softwareupdate](MACHOS/softwareupdate.md)
- [/usr/sbin/spctl](MACHOS/spctl.md)
- [/usr/sbin/spindump](MACHOS/spindump.md)
- [/usr/sbin/sshd](MACHOS/sshd.md)
- [/usr/sbin/systemsoundserverd](MACHOS/systemsoundserverd.md)
- [/usr/sbin/tcpdump](MACHOS/tcpdump.md)
- [/usr/sbin/uasysdiagnose](MACHOS/uasysdiagnose.md)
- [/usr/sbin/usernoted](MACHOS/usernoted.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (95)

<details>
  <summary><i>View Updated</i></summary>

- [AppleAVE2FW_H13C.im4p](FIRMWARE/AppleAVE2FW_H13C.im4p.md)
- [AppleAVE2FW_H13D.im4p](FIRMWARE/AppleAVE2FW_H13D.im4p.md)
- [AppleAVE2FW_H13G.im4p](FIRMWARE/AppleAVE2FW_H13G.im4p.md)
- [AppleAVE2FW_H13S.im4p](FIRMWARE/AppleAVE2FW_H13S.im4p.md)
- [AppleAVE2FW_H14C.im4p](FIRMWARE/AppleAVE2FW_H14C.im4p.md)
- [AppleAVE2FW_H14D.im4p](FIRMWARE/AppleAVE2FW_H14D.im4p.md)
- [AppleAVE2FW_H14G.im4p](FIRMWARE/AppleAVE2FW_H14G.im4p.md)
- [AppleAVE2FW_H14S.im4p](FIRMWARE/AppleAVE2FW_H14S.im4p.md)
- [AppleAVE2FW_H15C.im4p](FIRMWARE/AppleAVE2FW_H15C.im4p.md)
- [AppleAVE2FW_H15G.im4p](FIRMWARE/AppleAVE2FW_H15G.im4p.md)
- [AppleAVE2FW_H15M.im4p](FIRMWARE/AppleAVE2FW_H15M.im4p.md)
- [AppleAVE2FW_H15S.im4p](FIRMWARE/AppleAVE2FW_H15S.im4p.md)
- [SmartIOFirmware_ASCv4.im4p](FIRMWARE/SmartIOFirmware_ASCv4.im4p.md)
- [SmartIOFirmware_ASCv5.im4p](FIRMWARE/SmartIOFirmware_ASCv5.im4p.md)
- [SmartIOFirmware_ASCv6.im4p](FIRMWARE/SmartIOFirmware_ASCv6.im4p.md)
- [adc-aion-ls5x.im4p](FIRMWARE/adc-aion-ls5x.im4p.md)
- [adc-aion-pc5x.im4p](FIRMWARE/adc-aion-pc5x.im4p.md)
- [adc-astraeus-jc3x.im4p](FIRMWARE/adc-astraeus-jc3x.im4p.md)
- [adc-helios-rc4x.im4p](FIRMWARE/adc-helios-rc4x.im4p.md)
- [adc-hestia-j129.im4p](FIRMWARE/adc-hestia-j129.im4p.md)
- [adc-pallas-j129.im4p](FIRMWARE/adc-pallas-j129.im4p.md)
- [adc-triton-j129.im4p](FIRMWARE/adc-triton-j129.im4p.md)
- [agx_a000.bin](FIRMWARE/agx_a000.bin.md)
- [agx_b000.bin](FIRMWARE/agx_b000.bin.md)
- [agx_b100.bin](FIRMWARE/agx_b100.bin.md)
- [agx_c000.bin](FIRMWARE/agx_c000.bin.md)
- [ansf.t6000.release.im4p](FIRMWARE/ansf.t6000.release.im4p.md)
- [ansf.t6020.release.im4p](FIRMWARE/ansf.t6020.release.im4p.md)
- [ansf.t6030.release.im4p](FIRMWARE/ansf.t6030.release.im4p.md)
- [ansf.t603x.release.im4p](FIRMWARE/ansf.t603x.release.im4p.md)
- [ansf.t8103.release.im4p](FIRMWARE/ansf.t8103.release.im4p.md)
- [ansf.t8112.release.im4p](FIRMWARE/ansf.t8112.release.im4p.md)
- [ansf.t8122.release.im4p](FIRMWARE/ansf.t8122.release.im4p.md)
- [aopfw-mac13gaop.RELEASE.im4p](FIRMWARE/aopfw-mac13gaop.RELEASE.im4p.md)
- [aopfw-mac13jaop.RELEASE.im4p](FIRMWARE/aopfw-mac13jaop.RELEASE.im4p.md)
- [aopfw-mac14gaop.RELEASE.im4p](FIRMWARE/aopfw-mac14gaop.RELEASE.im4p.md)
- [aopfw-mac14jaop.RELEASE.im4p](FIRMWARE/aopfw-mac14jaop.RELEASE.im4p.md)
- [aopfw-mac15gaop.RELEASE.im4p](FIRMWARE/aopfw-mac15gaop.RELEASE.im4p.md)
- [aopfw-mac15jaop.RELEASE.im4p](FIRMWARE/aopfw-mac15jaop.RELEASE.im4p.md)
- [aopfw-mac15saop.RELEASE.im4p](FIRMWARE/aopfw-mac15saop.RELEASE.im4p.md)
- [h13_ane_fw_styx_j5x.im4p](FIRMWARE/h13_ane_fw_styx_j5x.im4p.md)
- [h14_ane_fw_bia_j4xx.im4p](FIRMWARE/h14_ane_fw_bia_j4xx.im4p.md)
- [h15_ane_fw_themis_j51y.im4p](FIRMWARE/h15_ane_fw_themis_j51y.im4p.md)
- [ipad13dcp.im4p](FIRMWARE/ipad13dcp.im4p.md)
- [ipad13dcp_restore.im4p](FIRMWARE/ipad13dcp_restore.im4p.md)
- [ipad14dcp.im4p](FIRMWARE/ipad14dcp.im4p.md)
- [ipad14dcp_restore.im4p](FIRMWARE/ipad14dcp_restore.im4p.md)
- [rans.t6000.release.im4p](FIRMWARE/rans.t6000.release.im4p.md)
- [rans.t6020.release.im4p](FIRMWARE/rans.t6020.release.im4p.md)
- [rans.t6030.release.im4p](FIRMWARE/rans.t6030.release.im4p.md)
- [rans.t603x.release.im4p](FIRMWARE/rans.t603x.release.im4p.md)
- [rans.t8103.release.im4p](FIRMWARE/rans.t8103.release.im4p.md)
- [rans.t8112.release.im4p](FIRMWARE/rans.t8112.release.im4p.md)
- [rans.t8122.release.im4p](FIRMWARE/rans.t8122.release.im4p.md)
- [sptm.t8112.release.im4p](FIRMWARE/sptm.t8112.release.im4p.md)
- [t6000ciofw.im4p](FIRMWARE/t6000ciofw.im4p.md)
- [t6000pmp.im4p](FIRMWARE/t6000pmp.im4p.md)
- [t6001ciofw.im4p](FIRMWARE/t6001ciofw.im4p.md)
- [t6002ciofw.im4p](FIRMWARE/t6002ciofw.im4p.md)
- [t600x_ane0_fw_eos_jc3x.im4p](FIRMWARE/t600x_ane0_fw_eos_jc3x.im4p.md)
- [t600x_ane1_fw_eos_jc3x.im4p](FIRMWARE/t600x_ane1_fw_eos_jc3x.im4p.md)
- [t600x_ane2_fw_eos_jc3x.im4p](FIRMWARE/t600x_ane2_fw_eos_jc3x.im4p.md)
- [t600x_ane3_fw_eos_jc3x.im4p](FIRMWARE/t600x_ane3_fw_eos_jc3x.im4p.md)
- [t600xdcp.im4p](FIRMWARE/t600xdcp.im4p.md)
- [t600xdcp_restore.im4p](FIRMWARE/t600xdcp_restore.im4p.md)
- [t6020ciofw.im4p](FIRMWARE/t6020ciofw.im4p.md)
- [t6020pmp.im4p](FIRMWARE/t6020pmp.im4p.md)
- [t6021ciofw.im4p](FIRMWARE/t6021ciofw.im4p.md)
- [t6022ciofw.im4p](FIRMWARE/t6022ciofw.im4p.md)
- [t602x_ane0_fw_selene_rc4x.im4p](FIRMWARE/t602x_ane0_fw_selene_rc4x.im4p.md)
- [t602x_ane1_fw_selene_rc4x.im4p](FIRMWARE/t602x_ane1_fw_selene_rc4x.im4p.md)
- [t602xdcp.im4p](FIRMWARE/t602xdcp.im4p.md)
- [t602xdcp_restore.im4p](FIRMWARE/t602xdcp_restore.im4p.md)
- [t602xscodec.im4p](FIRMWARE/t602xscodec.im4p.md)
- [t6030ciofw.im4p](FIRMWARE/t6030ciofw.im4p.md)
- [t6030dcp.im4p](FIRMWARE/t6030dcp.im4p.md)
- [t6030dcp_restore.im4p](FIRMWARE/t6030dcp_restore.im4p.md)
- [t6030pmp.im4p](FIRMWARE/t6030pmp.im4p.md)
- [t6031ciofw.im4p](FIRMWARE/t6031ciofw.im4p.md)
- [t6031pmp.im4p](FIRMWARE/t6031pmp.im4p.md)
- [t6034ciofw.im4p](FIRMWARE/t6034ciofw.im4p.md)
- [t603x_ane0_fw_erebus_ls5x.im4p](FIRMWARE/t603x_ane0_fw_erebus_ls5x.im4p.md)
- [t603x_ane0_fw_erebus_pc5x.im4p](FIRMWARE/t603x_ane0_fw_erebus_pc5x.im4p.md)
- [t603xdcp.im4p](FIRMWARE/t603xdcp.im4p.md)
- [t603xdcp_restore.im4p](FIRMWARE/t603xdcp_restore.im4p.md)
- [t8103ciofw.im4p](FIRMWARE/t8103ciofw.im4p.md)
- [t8103pmp.im4p](FIRMWARE/t8103pmp.im4p.md)
- [t8112ciofw.im4p](FIRMWARE/t8112ciofw.im4p.md)
- [t8112pmp.im4p](FIRMWARE/t8112pmp.im4p.md)
- [t8112scodec.im4p](FIRMWARE/t8112scodec.im4p.md)
- [t8122ciofw.im4p](FIRMWARE/t8122ciofw.im4p.md)
- [t8122dcp.im4p](FIRMWARE/t8122dcp.im4p.md)
- [t8122dcp_restore.im4p](FIRMWARE/t8122dcp_restore.im4p.md)
- [t8122pmp.im4p](FIRMWARE/t8122pmp.im4p.md)
- [txm.macosx.release.im4p](FIRMWARE/txm.macosx.release.im4p.md)

</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 15.0 *(24A5279h)* | 619.1.18.11.1 |
| 15.0 *(24A5289g)* | 619.1.20.11.1 |

### Dylibs

#### 🆕 NEW (9)

- `/System/Library/Frameworks/_SwiftUICore.framework/Versions/A/_SwiftUICore`
- `/System/Library/PrivateFrameworks/AppStoreDaemonUI.framework/Versions/A/AppStoreDaemonUI`
- `/System/Library/PrivateFrameworks/CallHistoryToolKit.framework/Versions/A/CallHistoryToolKit`
- `/System/Library/PrivateFrameworks/CoreSpeechUtils.framework/Versions/A/CoreSpeechUtils`
- `/System/Library/PrivateFrameworks/ImagePlayground.framework/Versions/A/ImagePlayground`
- `/System/Library/PrivateFrameworks/TestHook.framework/Versions/A/TestHook`
- `/System/Library/PrivateFrameworks/TestHookService.framework/Versions/A/TestHookService`
- `/System/Library/PrivateFrameworks/TestHookShared.framework/Versions/A/TestHookShared`
- `/System/iOSSupport/System/Library/PrivateFrameworks/ImagePlayground.framework/Versions/A/ImagePlayground`

#### ❌ Removed (3)

- `/System/Library/PrivateFrameworks/ImageGenerationUI.framework/Versions/A/ImageGenerationUI`
- `/System/iOSSupport/System/Library/PrivateFrameworks/CoreChartSwift.framework/Versions/A/CoreChartSwift`
- `/System/iOSSupport/System/Library/PrivateFrameworks/ImageGenerationUI.framework/Versions/A/ImageGenerationUI`

#### ⬆️ Updated (1319)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/Accounts/Notification/AMSAccountNotificationPlugin.bundle/Contents/MacOS/AMSAccountNotificationPlugin](DYLIBS/AMSAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/DonationAccountWatcher.bundle/Contents/MacOS/DonationAccountWatcher](DYLIBS/DonationAccountWatcher.md)
- [/System/Library/Accounts/Notification/PassbookAccountNotificationPlugin.bundle/Contents/MacOS/PassbookAccountNotificationPlugin](DYLIBS/PassbookAccountNotificationPlugin.md)
- [/System/Library/Assistant/UIPlugins/SiriFindMyUIPlugin.siriUIBundle/Contents/Frameworks/SiriFindMyUI.framework/Versions/A/SiriFindMyUI](DYLIBS/SiriFindMyUI.md)
- [/System/Library/CoreServices/RawCamera.bundle/Contents/MacOS/RawCamera](DYLIBS/RawCamera.md)
- [/System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio](DYLIBS/AVFAudio.md)
- [/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libBLAS.dylib](DYLIBS/libBLAS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libBNNS.dylib](DYLIBS/libBNNS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libLAPACK.dylib](DYLIBS/libLAPACK.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libSparseBLAS.dylib](DYLIBS/libSparseBLAS.dylib.md)
- [/System/Library/Frameworks/Accounts.framework/Versions/A/Accounts](DYLIBS/Accounts.md)
- [/System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/AppKit.framework/Versions/C/AppKit](DYLIBS/AppKit.md)
- [/System/Library/Frameworks/AppTrackingTransparency.framework/Versions/A/AppTrackingTransparency](DYLIBS/AppTrackingTransparency.md)
- [/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/A/Resources/libFontRegistry.dylib](DYLIBS/libFontRegistry.dylib.md)
- [/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/HIServices.framework/Versions/A/HIServices](DYLIBS/HIServices.md)
- [/System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AudioVideoBridging.framework/Versions/A/AudioVideoBridging](DYLIBS/AudioVideoBridging.md)
- [/System/Library/Frameworks/AuthenticationServices.framework/Versions/A/AuthenticationServices](DYLIBS/AuthenticationServices.md)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Versions/A/Frameworks/AACClient.framework/Versions/A/AACClient](DYLIBS/AACClient.md)
- [/System/Library/Frameworks/BackgroundAssets.framework/Versions/A/BackgroundAssets](DYLIBS/BackgroundAssets.md)
- [/System/Library/Frameworks/BrowserEngineKit.framework/Versions/A/BrowserEngineKit](DYLIBS/BrowserEngineKit.md)
- [/System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork](DYLIBS/CFNetwork.md)
- [/System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/HIToolbox.framework/Versions/A/HIToolbox](DYLIBS/HIToolbox.md)
- [/System/Library/Frameworks/Charts.framework/Versions/A/Charts](DYLIBS/Charts.md)
- [/System/Library/Frameworks/Cinematic.framework/Versions/A/Cinematic](DYLIBS/Cinematic.md)
- [/System/Library/Frameworks/ClassKit.framework/Versions/A/ClassKit](DYLIBS/ClassKit.md)
- [/System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit](DYLIBS/CloudKit.md)
- [/System/Library/Frameworks/ColorSync.framework/Versions/A/ColorSync](DYLIBS/ColorSync.md)
- [/System/Library/Frameworks/Combine.framework/Versions/A/Combine](DYLIBS/Combine.md)
- [/System/Library/Frameworks/ContactProvider.framework/Versions/A/ContactProvider](DYLIBS/ContactProvider.md)
- [/System/Library/Frameworks/Contacts.framework/Versions/A/Contacts](DYLIBS/Contacts.md)
- [/System/Library/Frameworks/ContactsUI.framework/Versions/A/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio](DYLIBS/CoreAudio.md)
- [/System/Library/Frameworks/CoreAudioKit.framework/Versions/A/CoreAudioKit](DYLIBS/CoreAudioKit.md)
- [/System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth](DYLIBS/CoreBluetooth.md)
- [/System/Library/Frameworks/CoreData.framework/Versions/A/CoreData](DYLIBS/CoreData.md)
- [/System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation](DYLIBS/CoreFoundation.md)
- [/System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics](DYLIBS/CoreGraphics.md)
- [/System/Library/Frameworks/CoreImage.framework/Versions/A/CoreImage](DYLIBS/CoreImage.md)
- [/System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation](DYLIBS/CoreLocation.md)
- [/System/Library/Frameworks/CoreML.framework/Versions/A/CoreML](DYLIBS/CoreML.md)
- [/System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreMediaIO.framework/Versions/A/CoreMediaIO](DYLIBS/CoreMediaIO.md)
- [/System/Library/Frameworks/CoreMotion.framework/Versions/A/CoreMotion](DYLIBS/CoreMotion.md)
- [/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/AE.framework/Versions/A/AE](DYLIBS/AE.md)
- [/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/DictionaryServices.framework/Versions/A/DictionaryServices](DYLIBS/DictionaryServices.md)
- [/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/FSEvents.framework/Versions/A/FSEvents](DYLIBS/FSEvents.md)
- [/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/LaunchServices](DYLIBS/LaunchServices.md)
- [/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Metadata](DYLIBS/Metadata.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/Versions/A/CoreSpotlight](DYLIBS/CoreSpotlight.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib](DYLIBS/libCommCenterBase.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Versions/A/CoreTelephony](DYLIBS/CoreTelephony.md)
- [/System/Library/Frameworks/CoreText.framework/Versions/A/CoreText](DYLIBS/CoreText.md)
- [/System/Library/Frameworks/CoreTransferable.framework/Versions/A/CoreTransferable](DYLIBS/CoreTransferable.md)
- [/System/Library/Frameworks/CoreVideo.framework/Versions/A/CoreVideo](DYLIBS/CoreVideo.md)
- [/System/Library/Frameworks/CreateMLComponents.framework/Versions/A/CreateMLComponents](DYLIBS/CreateMLComponents.md)
- [/System/Library/Frameworks/CryptoKit.framework/Versions/A/CryptoKit](DYLIBS/CryptoKit.md)
- [/System/Library/Frameworks/CryptoTokenKit.framework/Versions/A/CryptoTokenKit](DYLIBS/CryptoTokenKit.md)
- [/System/Library/Frameworks/DVDPlayback.framework/Versions/A/DVDPlayback](DYLIBS/DVDPlayback.md)
- [/System/Library/Frameworks/DeveloperToolsSupport.framework/Versions/A/DeveloperToolsSupport](DYLIBS/DeveloperToolsSupport.md)
- [/System/Library/Frameworks/EventKit.framework/Versions/A/EventKit](DYLIBS/EventKit.md)
- [/System/Library/Frameworks/ExecutionPolicy.framework/Versions/A/ExecutionPolicy](DYLIBS/ExecutionPolicy.md)
- [/System/Library/Frameworks/ExtensionFoundation.framework/Versions/A/ExtensionFoundation](DYLIBS/ExtensionFoundation.md)
- [/System/Library/Frameworks/ExtensionKit.framework/Versions/A/ExtensionKit](DYLIBS/ExtensionKit.md)
- [/System/Library/Frameworks/FSKit.framework/Versions/A/FSKit](DYLIBS/FSKit.md)
- [/System/Library/Frameworks/FileProvider.framework/Versions/A/FileProvider](DYLIBS/FileProvider.md)
- [/System/Library/Frameworks/FinanceKit.framework/Versions/A/FinanceKit](DYLIBS/FinanceKit.md)
- [/System/Library/Frameworks/FinanceKitUI.framework/Versions/A/FinanceKitUI](DYLIBS/FinanceKitUI.md)
- [/System/Library/Frameworks/Foundation.framework/Versions/C/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/GameController.framework/Versions/A/GameController](DYLIBS/GameController.md)
- [/System/Library/Frameworks/GameKit.framework/Versions/A/GameKit](DYLIBS/GameKit.md)
- [/System/Library/Frameworks/GroupActivities.framework/Versions/A/GroupActivities](DYLIBS/GroupActivities.md)
- [/System/Library/Frameworks/HealthKit.framework/Versions/A/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/Hypervisor.framework/Versions/A/Hypervisor](DYLIBS/Hypervisor.md)
- [/System/Library/Frameworks/IdentityLookup.framework/Versions/A/IdentityLookup](DYLIBS/IdentityLookup.md)
- [/System/Library/Frameworks/ImageCaptureCore.framework/Versions/A/ImageCaptureCore](DYLIBS/ImageCaptureCore.md)
- [/System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO](DYLIBS/ImageIO.md)
- [/System/Library/Frameworks/Intents.framework/Versions/A/Intents](DYLIBS/Intents.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/LightweightCodeRequirements.framework/Versions/A/LightweightCodeRequirements](DYLIBS/LightweightCodeRequirements.md)
- [/System/Library/Frameworks/LinkPresentation.framework/Versions/A/LinkPresentation](DYLIBS/LinkPresentation.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/Versions/A/DaemonUtils](DYLIBS/DaemonUtils.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/Versions/A/MechanismBase](DYLIBS/MechanismBase.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/ModuleBase.framework/Versions/A/ModuleBase](DYLIBS/ModuleBase.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/Versions/A/SharedUtils](DYLIBS/SharedUtils.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Versions/A/LocalAuthentication](DYLIBS/LocalAuthentication.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Versions/A/ManagedAppDistribution](DYLIBS/ManagedAppDistribution.md)
- [/System/Library/Frameworks/ManagedSettings.framework/Versions/A/ManagedSettings](DYLIBS/ManagedSettings.md)
- [/System/Library/Frameworks/MapKit.framework/Versions/A/MapKit](DYLIBS/MapKit.md)
- [/System/Library/Frameworks/Matter.framework/Versions/A/Matter](DYLIBS/Matter.md)
- [/System/Library/Frameworks/MatterSupport.framework/Versions/A/MatterSupport](DYLIBS/MatterSupport.md)
- [/System/Library/Frameworks/MediaAccessibility.framework/Versions/A/MediaAccessibility](DYLIBS/MediaAccessibility.md)
- [/System/Library/Frameworks/MediaPlayer.framework/Versions/A/MediaPlayer](DYLIBS/MediaPlayer.md)
- [/System/Library/Frameworks/MediaToolbox.framework/Versions/A/MediaToolbox](DYLIBS/MediaToolbox.md)
- [/System/Library/Frameworks/Metal.framework/Versions/A/Metal](DYLIBS/Metal.md)
- [/System/Library/Frameworks/MetalFX.framework/Versions/A/MetalFX](DYLIBS/MetalFX.md)
- [/System/Library/Frameworks/MetalKit.framework/Versions/A/MetalKit](DYLIBS/MetalKit.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Versions/A/Frameworks/MPSImage.framework/Versions/A/MPSImage](DYLIBS/MPSImage.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Versions/A/Frameworks/MPSNDArray.framework/Versions/A/MPSNDArray](DYLIBS/MPSNDArray.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Versions/A/Frameworks/MPSRayIntersector.framework/Versions/A/MPSRayIntersector](DYLIBS/MPSRayIntersector.md)
- [/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/Versions/A/MetalPerformanceShadersGraph](DYLIBS/MetalPerformanceShadersGraph.md)
- [/System/Library/Frameworks/MusicKit.framework/Versions/A/MusicKit](DYLIBS/MusicKit.md)
- [/System/Library/Frameworks/NaturalLanguage.framework/Versions/A/NaturalLanguage](DYLIBS/NaturalLanguage.md)
- [/System/Library/Frameworks/Network.framework/Versions/A/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/NetworkExtension.framework/Versions/A/NetworkExtension](DYLIBS/NetworkExtension.md)
- [/System/Library/Frameworks/PHASE.framework/Versions/A/PHASE](DYLIBS/PHASE.md)
- [/System/Library/Frameworks/ParavirtualizedGraphics.framework/Versions/A/ParavirtualizedGraphics](DYLIBS/ParavirtualizedGraphics.md)
- [/System/Library/Frameworks/PencilKit.framework/Versions/A/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/Frameworks/Photos.framework/Versions/A/Photos](DYLIBS/Photos.md)
- [/System/Library/Frameworks/Quartz.framework/Versions/A/Frameworks/ImageKit.framework/Versions/A/ImageKit](DYLIBS/ImageKit.md)
- [/System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/QuickLook.framework/Versions/A/QuickLook](DYLIBS/QuickLook.md)
- [/System/Library/Frameworks/QuickLookThumbnailing.framework/Versions/A/QuickLookThumbnailing](DYLIBS/QuickLookThumbnailing.md)
- [/System/Library/Frameworks/RealityFoundation.framework/Versions/A/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/Library/Frameworks/RealityKit.framework/Versions/A/RealityKit](DYLIBS/RealityKit.md)
- [/System/Library/Frameworks/ScreenCaptureKit.framework/Versions/A/ScreenCaptureKit](DYLIBS/ScreenCaptureKit.md)
- [/System/Library/Frameworks/ScriptingBridge.framework/Versions/A/ScriptingBridge](DYLIBS/ScriptingBridge.md)
- [/System/Library/Frameworks/Security.framework/Versions/A/Security](DYLIBS/Security.md)
- [/System/Library/Frameworks/SensorKit.framework/Versions/A/SensorKit](DYLIBS/SensorKit.md)
- [/System/Library/Frameworks/ShazamKit.framework/Versions/A/ShazamKit](DYLIBS/ShazamKit.md)
- [/System/Library/Frameworks/Social.framework/Versions/A/Social](DYLIBS/Social.md)
- [/System/Library/Frameworks/SoundAnalysis.framework/Versions/A/SoundAnalysis](DYLIBS/SoundAnalysis.md)
- [/System/Library/Frameworks/Speech.framework/Versions/A/Speech](DYLIBS/Speech.md)
- [/System/Library/Frameworks/StickerKit.framework/Versions/A/StickerKit](DYLIBS/StickerKit.md)
- [/System/Library/Frameworks/StoreKit.framework/Versions/A/StoreKit](DYLIBS/StoreKit.md)
- [/System/Library/Frameworks/SwiftData.framework/Versions/A/SwiftData](DYLIBS/SwiftData.md)
- [/System/Library/Frameworks/SwiftUI.framework/Versions/A/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/Frameworks/SwiftUICore.framework/Versions/A/SwiftUICore](DYLIBS/SwiftUICore.md)
- [/System/Library/Frameworks/Symbols.framework/Versions/A/Symbols](DYLIBS/Symbols.md)
- [/System/Library/Frameworks/SystemExtensions.framework/Versions/A/SystemExtensions](DYLIBS/SystemExtensions.md)
- [/System/Library/Frameworks/TabularData.framework/Versions/A/TabularData](DYLIBS/TabularData.md)
- [/System/Library/Frameworks/TipKit.framework/Versions/A/TipKit](DYLIBS/TipKit.md)
- [/System/Library/Frameworks/Translation.framework/Versions/A/Translation](DYLIBS/Translation.md)
- [/System/Library/Frameworks/VideoSubscriberAccount.framework/Versions/A/VideoSubscriberAccount](DYLIBS/VideoSubscriberAccount.md)
- [/System/Library/Frameworks/VideoToolbox.framework/Versions/A/VideoToolbox](DYLIBS/VideoToolbox.md)
- [/System/Library/Frameworks/Virtualization.framework/Versions/A/Virtualization](DYLIBS/Virtualization.md)
- [/System/Library/Frameworks/Vision.framework/Versions/A/Vision](DYLIBS/Vision.md)
- [/System/Library/Frameworks/Vision.framework/libfaceCore.dylib](DYLIBS/libfaceCore.dylib.md)
- [/System/Library/Frameworks/WeatherKit.framework/Versions/A/WeatherKit](DYLIBS/WeatherKit.md)
- [/System/Library/Frameworks/WebKit.framework/Versions/A/Frameworks/WebCore.framework/Versions/A/Frameworks/libANGLE-shared.dylib](DYLIBS/libANGLE-shared.dylib.md)
- [/System/Library/Frameworks/WebKit.framework/Versions/A/Frameworks/WebCore.framework/Versions/A/Frameworks/libwebrtc.dylib](DYLIBS/libwebrtc.dylib.md)
- [/System/Library/Frameworks/WebKit.framework/Versions/A/Frameworks/WebCore.framework/Versions/A/WebCore](DYLIBS/WebCore.md)
- [/System/Library/Frameworks/WebKit.framework/Versions/A/Frameworks/WebKitLegacy.framework/Versions/A/WebKitLegacy](DYLIBS/WebKitLegacy.md)
- [/System/Library/Frameworks/WebKit.framework/Versions/A/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Frameworks/WidgetKit.framework/Versions/A/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/Library/Frameworks/WorkoutKit.framework/Versions/A/WorkoutKit](DYLIBS/WorkoutKit.md)
- [/System/Library/Frameworks/_AVKit_SwiftUI.framework/Versions/A/_AVKit_SwiftUI](DYLIBS/_AVKit_SwiftUI.md)
- [/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/Versions/A/_DeviceActivity_SwiftUI](DYLIBS/_DeviceActivity_SwiftUI.md)
- [/System/Library/Frameworks/_LocalAuthentication_SwiftUI.framework/Versions/A/_LocalAuthentication_SwiftUI](DYLIBS/_LocalAuthentication_SwiftUI.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/Versions/A/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/Frameworks/_PhotosUI_SwiftUI.framework/Versions/A/_PhotosUI_SwiftUI](DYLIBS/_PhotosUI_SwiftUI.md)
- [/System/Library/Frameworks/_QuickLook_SwiftUI.framework/Versions/A/_QuickLook_SwiftUI](DYLIBS/_QuickLook_SwiftUI.md)
- [/System/Library/Frameworks/_RealityKit_SwiftUI.framework/Versions/A/_RealityKit_SwiftUI](DYLIBS/_RealityKit_SwiftUI.md)
- [/System/Library/Frameworks/_StoreKit_SwiftUI.framework/Versions/A/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI.md)
- [/System/Library/Frameworks/_SwiftData_SwiftUI.framework/Versions/A/_SwiftData_SwiftUI](DYLIBS/_SwiftData_SwiftUI.md)
- [/System/Library/Frameworks/iTunesLibrary.framework/Versions/A/iTunesLibrary](DYLIBS/iTunesLibrary.md)
- [/System/Library/MediaCapture/H13ISP.mediacapture](DYLIBS/H13ISP.mediacapture.md)
- [/System/Library/MediaCapture/H16ISP.mediacapture](DYLIBS/H16ISP.mediacapture.md)
- [/System/Library/PrivateFrameworks/AAAFoundationSwift.framework/Versions/A/AAAFoundationSwift](DYLIBS/AAAFoundationSwift.md)
- [/System/Library/PrivateFrameworks/ACSEFoundation.framework/Versions/A/ACSEFoundation](DYLIBS/ACSEFoundation.md)
- [/System/Library/PrivateFrameworks/AGXCompilerCore.framework/Versions/A/AGXCompilerCore](DYLIBS/AGXCompilerCore.md)
- [/System/Library/PrivateFrameworks/AIMLExperimentationAnalytics.framework/Versions/A/AIMLExperimentationAnalytics](DYLIBS/AIMLExperimentationAnalytics.md)
- [/System/Library/PrivateFrameworks/AIMLInstrumentationStreams.framework/Versions/A/AIMLInstrumentationStreams](DYLIBS/AIMLInstrumentationStreams.md)
- [/System/Library/PrivateFrameworks/ALDataTypes.framework/Versions/A/ALDataTypes.dylib](DYLIBS/ALDataTypes.dylib.md)
- [/System/Library/PrivateFrameworks/AMPDesktopUI.framework/Versions/A/AMPDesktopUI](DYLIBS/AMPDesktopUI.md)
- [/System/Library/PrivateFrameworks/AMPLibrary.framework/Versions/A/AMPLibrary](DYLIBS/AMPLibrary.md)
- [/System/Library/PrivateFrameworks/ANECompiler.framework/Versions/A/ANECompiler](DYLIBS/ANECompiler.md)
- [/System/Library/PrivateFrameworks/ANEServices.framework/Versions/A/ANEServices](DYLIBS/ANEServices.md)
- [/System/Library/PrivateFrameworks/AONSense.framework/Versions/A/AONSense.dylib](DYLIBS/AONSense.dylib.md)
- [/System/Library/PrivateFrameworks/AOSUI.framework/Versions/A/AOSUI](DYLIBS/AOSUI.md)
- [/System/Library/PrivateFrameworks/APConfigurationSystem.framework/Versions/A/APConfigurationSystem](DYLIBS/APConfigurationSystem.md)
- [/System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS](DYLIBS/APFS.md)
- [/System/Library/PrivateFrameworks/APFoundation.framework/Versions/A/APFoundation](DYLIBS/APFoundation.md)
- [/System/Library/PrivateFrameworks/APTransport.framework/Versions/A/APTransport](DYLIBS/APTransport.md)
- [/System/Library/PrivateFrameworks/ASRBridge.framework/Versions/A/ASRBridge](DYLIBS/ASRBridge.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/Versions/A/ViceroyTrace](DYLIBS/ViceroyTrace.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Versions/A/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVFCapture.framework/Versions/A/AVFCapture](DYLIBS/AVFCapture.md)
- [/System/Library/PrivateFrameworks/AVFCore.framework/Versions/A/AVFCore](DYLIBS/AVFCore.md)
- [/System/Library/PrivateFrameworks/AVFoundationCF.framework/Versions/A/AVFoundationCF](DYLIBS/AVFoundationCF.md)
- [/System/Library/PrivateFrameworks/AVKitCore.framework/Versions/A/AVKitCore](DYLIBS/AVKitCore.md)
- [/System/Library/PrivateFrameworks/AXCoreUtilities.framework/Versions/A/AXCoreUtilities](DYLIBS/AXCoreUtilities.md)
- [/System/Library/PrivateFrameworks/AXMediaUtilities.framework/Versions/A/AXMediaUtilities](DYLIBS/AXMediaUtilities.md)
- [/System/Library/PrivateFrameworks/AXRuntime.framework/Versions/A/AXRuntime](DYLIBS/AXRuntime.md)
- [/System/Library/PrivateFrameworks/AccessibilitySettingsUI.framework/Versions/A/AccessibilitySettingsUI](DYLIBS/AccessibilitySettingsUI.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/Versions/A/AccessibilitySharedUISupport](DYLIBS/AccessibilitySharedUISupport.md)
- [/System/Library/PrivateFrameworks/AccessibilitySupport.framework/Versions/A/Frameworks/AccessibilityKit.framework/Versions/A/AccessibilityKit](DYLIBS/AccessibilityKit.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/Versions/A/AccessibilityUtilities](DYLIBS/AccessibilityUtilities.md)
- [/System/Library/PrivateFrameworks/AccountsDaemon.framework/Versions/A/AccountsDaemon](DYLIBS/AccountsDaemon.md)
- [/System/Library/PrivateFrameworks/AccountsUISettings.framework/Versions/A/AccountsUISettings](DYLIBS/AccountsUISettings.md)
- [/System/Library/PrivateFrameworks/ActionKit.framework/Versions/A/ActionKit](DYLIBS/ActionKit.md)
- [/System/Library/PrivateFrameworks/ActionKitUI.framework/Versions/A/ActionKitUI](DYLIBS/ActionKitUI.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/Versions/A/ActionPredictionHeuristics](DYLIBS/ActionPredictionHeuristics.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristicsInternal.framework/Versions/A/ActionPredictionHeuristicsInternal](DYLIBS/ActionPredictionHeuristicsInternal.md)
- [/System/Library/PrivateFrameworks/AdID.framework/Versions/A/AdID](DYLIBS/AdID.md)
- [/System/Library/PrivateFrameworks/AdaptiveVoiceShortcuts.framework/Versions/A/AdaptiveVoiceShortcuts](DYLIBS/AdaptiveVoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiver.framework/Versions/A/AirPlayReceiver](DYLIBS/AirPlayReceiver.md)
- [/System/Library/PrivateFrameworks/AirPlaySender.framework/Versions/A/AirPlaySender](DYLIBS/AirPlaySender.md)
- [/System/Library/PrivateFrameworks/AirPlaySupport.framework/Versions/A/AirPlaySupport](DYLIBS/AirPlaySupport.md)
- [/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/Versions/A/AltruisticBodyPoseKit](DYLIBS/AltruisticBodyPoseKit.md)
- [/System/Library/PrivateFrameworks/AppAnalytics.framework/Versions/A/AppAnalytics](DYLIBS/AppAnalytics.md)
- [/System/Library/PrivateFrameworks/AppIntentsServices.framework/Versions/A/AppIntentsServices](DYLIBS/AppIntentsServices.md)
- [/System/Library/PrivateFrameworks/AppNotificationsLoggingClient.framework/Versions/A/AppNotificationsLoggingClient](DYLIBS/AppNotificationsLoggingClient.md)
- [/System/Library/PrivateFrameworks/AppPlaceholderSync.framework/Versions/A/AppPlaceholderSync](DYLIBS/AppPlaceholderSync.md)
- [/System/Library/PrivateFrameworks/AppPredictionClient.framework/Versions/A/AppPredictionClient](DYLIBS/AppPredictionClient.md)
- [/System/Library/PrivateFrameworks/AppPredictionFoundation.framework/Versions/A/AppPredictionFoundation](DYLIBS/AppPredictionFoundation.md)
- [/System/Library/PrivateFrameworks/AppPredictionInternal.framework/Versions/A/AppPredictionInternal](DYLIBS/AppPredictionInternal.md)
- [/System/Library/PrivateFrameworks/AppSandbox.framework/Versions/A/AppSandbox](DYLIBS/AppSandbox.md)
- [/System/Library/PrivateFrameworks/AppServerSupport.framework/Versions/A/AppServerSupport](DYLIBS/AppServerSupport.md)
- [/System/Library/PrivateFrameworks/AppState.framework/Versions/A/AppState](DYLIBS/AppState.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/Versions/A/AppStoreComponents](DYLIBS/AppStoreComponents.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Versions/A/AppStoreDaemon](DYLIBS/AppStoreDaemon.md)
- [/System/Library/PrivateFrameworks/AppStoreFoundation.framework/Versions/A/AppStoreFoundation](DYLIBS/AppStoreFoundation.md)
- [/System/Library/PrivateFrameworks/AppStoreKitInternal.framework/Versions/A/AppStoreKitInternal](DYLIBS/AppStoreKitInternal.md)
- [/System/Library/PrivateFrameworks/AppStoreUI.framework/Versions/A/AppStoreUI](DYLIBS/AppStoreUI.md)
- [/System/Library/PrivateFrameworks/AppSupport.framework/Versions/A/AppSupport](DYLIBS/AppSupport.md)
- [/System/Library/PrivateFrameworks/AppleAccount.framework/Versions/A/AppleAccount](DYLIBS/AppleAccount.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/Versions/A/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/PrivateFrameworks/AppleCVA.framework/Versions/A/AppleCVA](DYLIBS/AppleCVA.md)
- [/System/Library/PrivateFrameworks/AppleDepth.framework/Versions/A/AppleDepth](DYLIBS/AppleDepth.md)
- [/System/Library/PrivateFrameworks/AppleDepthCore.framework/Versions/A/AppleDepthCore](DYLIBS/AppleDepthCore.md)
- [/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/Versions/A/AppleDeviceQuerySupport](DYLIBS/AppleDeviceQuerySupport.md)
- [/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/Versions/A/libAppleDeviceQueryArmory.dylib](DYLIBS/libAppleDeviceQueryArmory.dylib.md)
- [/System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/Versions/A/AppleIDSSOAuthentication](DYLIBS/AppleIDSSOAuthentication.md)
- [/System/Library/PrivateFrameworks/AppleIDSetup.framework/Versions/A/AppleIDSetup](DYLIBS/AppleIDSetup.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupDaemon.framework/Versions/A/AppleIDSetupDaemon](DYLIBS/AppleIDSetupDaemon.md)
- [/System/Library/PrivateFrameworks/AppleJPEG.framework/Versions/A/AppleJPEG](DYLIBS/AppleJPEG.md)
- [/System/Library/PrivateFrameworks/AppleKeyStore.framework/Versions/A/AppleKeyStore](DYLIBS/AppleKeyStore.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/Versions/A/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Versions/A/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIPaymentSheets.framework/Versions/A/AppleMediaServicesUIPaymentSheets](DYLIBS/AppleMediaServicesUIPaymentSheets.md)
- [/System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/Versions/A/AppleMobileFileIntegrity](DYLIBS/AppleMobileFileIntegrity.md)
- [/System/Library/PrivateFrameworks/ApplePhotonDetectorServices.framework/Versions/A/ApplePhotonDetectorServices](DYLIBS/ApplePhotonDetectorServices.md)
- [/System/Library/PrivateFrameworks/ArchetypeEngine.framework/Versions/A/ArchetypeEngine](DYLIBS/ArchetypeEngine.md)
- [/System/Library/PrivateFrameworks/ArgumentParserInternal.framework/Versions/A/ArgumentParserInternal](DYLIBS/ArgumentParserInternal.md)
- [/System/Library/PrivateFrameworks/AskTo.framework/Versions/A/AskTo](DYLIBS/AskTo.md)
- [/System/Library/PrivateFrameworks/AskToCore.framework/Versions/A/AskToCore](DYLIBS/AskToCore.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/PrivateFrameworks/AtomicsInternal.framework/Versions/A/AtomicsInternal](DYLIBS/AtomicsInternal.md)
- [/System/Library/PrivateFrameworks/AttributeGraph.framework/Versions/A/AttributeGraph](DYLIBS/AttributeGraph.md)
- [/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/Versions/A/AudioAccessoryServices](DYLIBS/AudioAccessoryServices.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/Versions/A/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsExternal.framework/Versions/A/AudioAnalyticsExternal](DYLIBS/AudioAnalyticsExternal.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOA2.framework/Versions/A/AudioServerDriverTransports_IOA2](DYLIBS/AudioServerDriverTransports_IOA2.md)
- [/System/Library/PrivateFrameworks/AudioToolboxCore.framework/Versions/A/AudioToolboxCore](DYLIBS/AudioToolboxCore.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/Versions/A/AuthenticationServicesCore](DYLIBS/AuthenticationServicesCore.md)
- [/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/Versions/A/AutoBugCaptureCore](DYLIBS/AutoBugCaptureCore.md)
- [/System/Library/PrivateFrameworks/AutoFillCore.framework/Versions/A/AutoFillCore](DYLIBS/AutoFillCore.md)
- [/System/Library/PrivateFrameworks/BackBoardServices.framework/Versions/A/BackBoardServices](DYLIBS/BackBoardServices.md)
- [/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/Versions/A/BackgroundSystemTasks](DYLIBS/BackgroundSystemTasks.md)
- [/System/Library/PrivateFrameworks/BackgroundTaskManagement.framework/Versions/A/BackgroundTaskManagement](DYLIBS/BackgroundTaskManagement.md)
- [/System/Library/PrivateFrameworks/Backup.framework/Versions/A/Backup](DYLIBS/Backup.md)
- [/System/Library/PrivateFrameworks/BaseBoard.framework/Versions/A/BaseBoard](DYLIBS/BaseBoard.md)
- [/System/Library/PrivateFrameworks/BatteryCenterUI.framework/Versions/A/BatteryCenterUI](DYLIBS/BatteryCenterUI.md)
- [/System/Library/PrivateFrameworks/BiomeDSL.framework/Versions/A/BiomeDSL](DYLIBS/BiomeDSL.md)
- [/System/Library/PrivateFrameworks/BiomeFoundation.framework/Versions/A/BiomeFoundation](DYLIBS/BiomeFoundation.md)
- [/System/Library/PrivateFrameworks/BiomeLibrary.framework/Versions/A/BiomeLibrary](DYLIBS/BiomeLibrary.md)
- [/System/Library/PrivateFrameworks/BiomePubSub.framework/Versions/A/BiomePubSub](DYLIBS/BiomePubSub.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams](DYLIBS/BiomeStreams.md)
- [/System/Library/PrivateFrameworks/BiomeSync.framework/Versions/A/BiomeSync](DYLIBS/BiomeSync.md)
- [/System/Library/PrivateFrameworks/BlastDoor.framework/Versions/A/BlastDoor](DYLIBS/BlastDoor.md)
- [/System/Library/PrivateFrameworks/BlockMonitoring.framework/Versions/A/BlockMonitoring](DYLIBS/BlockMonitoring.md)
- [/System/Library/PrivateFrameworks/BluetoothServices.framework/Versions/A/BluetoothServices](DYLIBS/BluetoothServices.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/Versions/A/BookDataStore](DYLIBS/BookDataStore.md)
- [/System/Library/PrivateFrameworks/BookFoundation.framework/Versions/A/BookFoundation](DYLIBS/BookFoundation.md)
- [/System/Library/PrivateFrameworks/Bootability.framework/Versions/A/Frameworks/BootabilityBrain.framework/Versions/A/BootabilityBrain](DYLIBS/BootabilityBrain.md)
- [/System/Library/PrivateFrameworks/BusinessServices.framework/Versions/A/BusinessServices](DYLIBS/BusinessServices.md)
- [/System/Library/PrivateFrameworks/C2.framework/Versions/A/C2](DYLIBS/C2.md)
- [/System/Library/PrivateFrameworks/CBORLibrary.framework/Versions/A/CBORLibrary](DYLIBS/CBORLibrary.md)
- [/System/Library/PrivateFrameworks/CDMFoundation.framework/Versions/A/CDMFoundation](DYLIBS/CDMFoundation.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/Versions/A/CMCapture](DYLIBS/CMCapture.md)
- [/System/Library/PrivateFrameworks/CMCaptureCore.framework/Versions/A/CMCaptureCore](DYLIBS/CMCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/Versions/A/CMContinuityCaptureCore](DYLIBS/CMContinuityCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMImaging.framework/Versions/A/CMImaging](DYLIBS/CMImaging.md)
- [/System/Library/PrivateFrameworks/CMPhoto.framework/Versions/A/CMPhoto](DYLIBS/CMPhoto.md)
- [/System/Library/PrivateFrameworks/CPAnalytics.framework/Versions/A/CPAnalytics](DYLIBS/CPAnalytics.md)
- [/System/Library/PrivateFrameworks/CTBlastDoorSupport.framework/Versions/A/CTBlastDoorSupport](DYLIBS/CTBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/CTLazuliSupport.framework/Versions/A/CTLazuliSupport](DYLIBS/CTLazuliSupport.md)
- [/System/Library/PrivateFrameworks/CVNLP.framework/Versions/A/CVNLP](DYLIBS/CVNLP.md)
- [/System/Library/PrivateFrameworks/Calculate.framework/Versions/A/Calculate](DYLIBS/Calculate.md)
- [/System/Library/PrivateFrameworks/CalculateUI.framework/Versions/A/CalculateUI](DYLIBS/CalculateUI.md)
- [/System/Library/PrivateFrameworks/CalendarDaemon.framework/Versions/A/CalendarDaemon](DYLIBS/CalendarDaemon.md)
- [/System/Library/PrivateFrameworks/CalendarDatabase.framework/Versions/A/CalendarDatabase](DYLIBS/CalendarDatabase.md)
- [/System/Library/PrivateFrameworks/CalendarFoundation.framework/Versions/A/CalendarFoundation](DYLIBS/CalendarFoundation.md)
- [/System/Library/PrivateFrameworks/CalendarIntegrationSupport.framework/Versions/A/CalendarIntegrationSupport](DYLIBS/CalendarIntegrationSupport.md)
- [/System/Library/PrivateFrameworks/CalendarLink.framework/Versions/A/CalendarLink](DYLIBS/CalendarLink.md)
- [/System/Library/PrivateFrameworks/CalendarUI.framework/Versions/A/CalendarUI](DYLIBS/CalendarUI.md)
- [/System/Library/PrivateFrameworks/CalendarUIKit.framework/Versions/A/CalendarUIKit](DYLIBS/CalendarUIKit.md)
- [/System/Library/PrivateFrameworks/CalendarUIKitInternal.framework/Versions/A/CalendarUIKitInternal](DYLIBS/CalendarUIKitInternal.md)
- [/System/Library/PrivateFrameworks/CalendarWidget.framework/Versions/A/CalendarWidget](DYLIBS/CalendarWidget.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/Versions/A/CallHistory](DYLIBS/CallHistory.md)
- [/System/Library/PrivateFrameworks/CallstackAnalysis.framework/Versions/A/CallstackAnalysis](DYLIBS/CallstackAnalysis.md)
- [/System/Library/PrivateFrameworks/CascadeEngine.framework/Versions/A/CascadeEngine](DYLIBS/CascadeEngine.md)
- [/System/Library/PrivateFrameworks/CascadeSets.framework/Versions/A/CascadeSets](DYLIBS/CascadeSets.md)
- [/System/Library/PrivateFrameworks/Catalyst.framework/Versions/A/Catalyst](DYLIBS/Catalyst.md)
- [/System/Library/PrivateFrameworks/CharacterPicker.framework/Versions/A/CharacterPicker](DYLIBS/CharacterPicker.md)
- [/System/Library/PrivateFrameworks/Chirp.framework/Versions/A/Chirp](DYLIBS/Chirp.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/Versions/A/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/PrivateFrameworks/ChronoKit.framework/Versions/A/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/Library/PrivateFrameworks/ChronoServices.framework/Versions/A/ChronoServices](DYLIBS/ChronoServices.md)
- [/System/Library/PrivateFrameworks/ChronoUIServices.framework/Versions/A/ChronoUIServices](DYLIBS/ChronoUIServices.md)
- [/System/Library/PrivateFrameworks/CipherML.framework/Versions/A/CipherML](DYLIBS/CipherML.md)
- [/System/Library/PrivateFrameworks/CloudAsset.framework/Versions/A/CloudAsset](DYLIBS/CloudAsset.md)
- [/System/Library/PrivateFrameworks/CloudAssetDaemon.framework/Versions/A/CloudAssetDaemon](DYLIBS/CloudAssetDaemon.md)
- [/System/Library/PrivateFrameworks/CloudAssets.framework/Versions/A/CloudAssets](DYLIBS/CloudAssets.md)
- [/System/Library/PrivateFrameworks/CloudAttestation.framework/Versions/A/CloudAttestation](DYLIBS/CloudAttestation.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/Versions/A/CloudDocs](DYLIBS/CloudDocs.md)
- [/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/Versions/A/CloudDocsDaemon](DYLIBS/CloudDocsDaemon.md)
- [/System/Library/PrivateFrameworks/CloudKitCode.framework/Versions/A/CloudKitCode](DYLIBS/CloudKitCode.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Versions/A/CloudKitDaemon](DYLIBS/CloudKitDaemon.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Versions/A/CloudPhotoLibrary](DYLIBS/CloudPhotoLibrary.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/Versions/A/CloudSubscriptionFeatures](DYLIBS/CloudSubscriptionFeatures.md)
- [/System/Library/PrivateFrameworks/CloudTelemetryTools.framework/Versions/A/CloudTelemetryTools](DYLIBS/CloudTelemetryTools.md)
- [/System/Library/PrivateFrameworks/Coherence.framework/Versions/A/Coherence](DYLIBS/Coherence.md)
- [/System/Library/PrivateFrameworks/CollectionsInternal.framework/Versions/A/CollectionsInternal](DYLIBS/CollectionsInternal.md)
- [/System/Library/PrivateFrameworks/CompanionServices.framework/Versions/A/CompanionServices](DYLIBS/CompanionServices.md)
- [/System/Library/PrivateFrameworks/ComputeSafeguards.framework/Versions/A/ComputeSafeguards](DYLIBS/ComputeSafeguards.md)
- [/System/Library/PrivateFrameworks/ContactsAccounts.framework/Versions/A/ContactsAccounts](DYLIBS/ContactsAccounts.md)
- [/System/Library/PrivateFrameworks/ContactsAutocomplete.framework/Versions/A/ContactsAutocomplete](DYLIBS/ContactsAutocomplete.md)
- [/System/Library/PrivateFrameworks/ContactsFoundation.framework/Versions/A/ContactsFoundation](DYLIBS/ContactsFoundation.md)
- [/System/Library/PrivateFrameworks/ContactsUICore.framework/Versions/A/ContactsUICore](DYLIBS/ContactsUICore.md)
- [/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/Versions/A/ContainerManagerCommon](DYLIBS/ContainerManagerCommon.md)
- [/System/Library/PrivateFrameworks/ContainerManagerSystem.framework/Versions/A/ContainerManagerSystem](DYLIBS/ContainerManagerSystem.md)
- [/System/Library/PrivateFrameworks/ContainerManagerUser.framework/Versions/A/ContainerManagerUser](DYLIBS/ContainerManagerUser.md)
- [/System/Library/PrivateFrameworks/ContentKit.framework/Versions/A/ContentKit](DYLIBS/ContentKit.md)
- [/System/Library/PrivateFrameworks/ContextSync.framework/Versions/A/ContextSync](DYLIBS/ContextSync.md)
- [/System/Library/PrivateFrameworks/ContextualUnderstanding.framework/Versions/A/ContextualUnderstanding](DYLIBS/ContextualUnderstanding.md)
- [/System/Library/PrivateFrameworks/ControlCenter.framework/Versions/A/ControlCenter](DYLIBS/ControlCenter.md)
- [/System/Library/PrivateFrameworks/ConversationKit.framework/Versions/A/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/PrivateFrameworks/Coordination.framework/Versions/A/Coordination](DYLIBS/Coordination.md)
- [/System/Library/PrivateFrameworks/CopresenceCore.framework/Versions/A/CopresenceCore](DYLIBS/CopresenceCore.md)
- [/System/Library/PrivateFrameworks/CoreAccessibility.framework/Additions/libCoreAccessibilityEyeCandyAdditions.dylib](DYLIBS/libCoreAccessibilityEyeCandyAdditions.dylib.md)
- [/System/Library/PrivateFrameworks/CoreAccessibility.framework/Versions/A/CoreAccessibility](DYLIBS/CoreAccessibility.md)
- [/System/Library/PrivateFrameworks/CoreBrightness.framework/Versions/A/CoreBrightness](DYLIBS/CoreBrightness.md)
- [/System/Library/PrivateFrameworks/CoreCDP.framework/Versions/A/CoreCDP](DYLIBS/CoreCDP.md)
- [/System/Library/PrivateFrameworks/CoreCDPInternal.framework/Versions/A/CoreCDPInternal](DYLIBS/CoreCDPInternal.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/Versions/A/CoreCDPUI](DYLIBS/CoreCDPUI.md)
- [/System/Library/PrivateFrameworks/CoreDiagnostics.framework/Versions/A/CoreDiagnostics](DYLIBS/CoreDiagnostics.md)
- [/System/Library/PrivateFrameworks/CoreDuet.framework/Versions/A/CoreDuet](DYLIBS/CoreDuet.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/Versions/A/CoreEmbeddedSpeechRecognition](DYLIBS/CoreEmbeddedSpeechRecognition.md)
- [/System/Library/PrivateFrameworks/CoreFollowUp.framework/Versions/A/CoreFollowUp](DYLIBS/CoreFollowUp.md)
- [/System/Library/PrivateFrameworks/CoreHAP.framework/Versions/A/CoreHAP](DYLIBS/CoreHAP.md)
- [/System/Library/PrivateFrameworks/CoreHandwriting.framework/Versions/A/CoreHandwriting](DYLIBS/CoreHandwriting.md)
- [/System/Library/PrivateFrameworks/CoreHapticsTools.framework/Versions/A/CoreHapticsTools](DYLIBS/CoreHapticsTools.md)
- [/System/Library/PrivateFrameworks/CoreIK.framework/Versions/A/CoreIK](DYLIBS/CoreIK.md)
- [/System/Library/PrivateFrameworks/CoreKnowledge.framework/Versions/A/CoreKnowledge](DYLIBS/CoreKnowledge.md)
- [/System/Library/PrivateFrameworks/CoreLocationTiles.framework/Versions/A/CoreLocationTiles](DYLIBS/CoreLocationTiles.md)
- [/System/Library/PrivateFrameworks/CoreNLP.framework/Versions/A/CoreNLP](DYLIBS/CoreNLP.md)
- [/System/Library/PrivateFrameworks/CoreOCModules.framework/Versions/A/CoreOCModules](DYLIBS/CoreOCModules.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/Versions/A/CoreParsec](DYLIBS/CoreParsec.md)
- [/System/Library/PrivateFrameworks/CorePhotogrammetry.framework/Versions/A/CorePhotogrammetry](DYLIBS/CorePhotogrammetry.md)
- [/System/Library/PrivateFrameworks/CoreRE.framework/Versions/A/CoreRE](DYLIBS/CoreRE.md)
- [/System/Library/PrivateFrameworks/CoreRealityIO.framework/Versions/A/CoreRealityIO](DYLIBS/CoreRealityIO.md)
- [/System/Library/PrivateFrameworks/CoreRoutine.framework/Versions/A/CoreRoutine](DYLIBS/CoreRoutine.md)
- [/System/Library/PrivateFrameworks/CoreSVG.framework/Versions/A/CoreSVG](DYLIBS/CoreSVG.md)
- [/System/Library/PrivateFrameworks/CoreSceneUnderstanding.framework/Versions/A/CoreSceneUnderstanding](DYLIBS/CoreSceneUnderstanding.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/Versions/A/CoreSpeech](DYLIBS/CoreSpeech.md)
- [/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/Versions/A/CoreSpeechFoundation](DYLIBS/CoreSpeechFoundation.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsUI.framework/Versions/A/CoreSuggestionsUI](DYLIBS/CoreSuggestionsUI.md)
- [/System/Library/PrivateFrameworks/CoreSymbolication.framework/Versions/A/CoreSymbolication](DYLIBS/CoreSymbolication.md)
- [/System/Library/PrivateFrameworks/CoreUARP.framework/Versions/A/CoreUARP](DYLIBS/CoreUARP.md)
- [/System/Library/PrivateFrameworks/CoreUI.framework/Versions/A/CoreUI](DYLIBS/CoreUI.md)
- [/System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils](DYLIBS/CoreUtils.md)
- [/System/Library/PrivateFrameworks/CoreUtilsSwift.framework/Versions/A/CoreUtilsSwift](DYLIBS/CoreUtilsSwift.md)
- [/System/Library/PrivateFrameworks/CoreUtilsUI.framework/Versions/A/CoreUtilsUI](DYLIBS/CoreUtilsUI.md)
- [/System/Library/PrivateFrameworks/CoreWiFi.framework/Versions/A/CoreWiFi](DYLIBS/CoreWiFi.md)
- [/System/Library/PrivateFrameworks/Cosmo.framework/Versions/A/Cosmo](DYLIBS/Cosmo.md)
- [/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/Versions/A/CryptoKitPrivate](DYLIBS/CryptoKitPrivate.md)
- [/System/Library/PrivateFrameworks/DMCUtilities.framework/Versions/A/DMCUtilities](DYLIBS/DMCUtilities.md)
- [/System/Library/PrivateFrameworks/DarwinDirectory.framework/Versions/A/DarwinDirectory](DYLIBS/DarwinDirectory.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACalDAV.framework/Versions/A/DACalDAV](DYLIBS/DACalDAV.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DADaemonSupport.framework/Versions/A/DADaemonSupport](DYLIBS/DADaemonSupport.md)
- [/System/Library/PrivateFrameworks/DataDeliveryServices.framework/Versions/A/DataDeliveryServices](DYLIBS/DataDeliveryServices.md)
- [/System/Library/PrivateFrameworks/DataDetectorsCore.framework/Versions/A/DataDetectorsCore](DYLIBS/DataDetectorsCore.md)
- [/System/Library/PrivateFrameworks/DeepThoughtBiomeFoundation.framework/Versions/A/DeepThoughtBiomeFoundation](DYLIBS/DeepThoughtBiomeFoundation.md)
- [/System/Library/PrivateFrameworks/Dendrite.framework/Versions/A/Dendrite](DYLIBS/Dendrite.md)
- [/System/Library/PrivateFrameworks/DendriteIngest.framework/Versions/A/DendriteIngest](DYLIBS/DendriteIngest.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/A/DesktopServicesPriv](DYLIBS/DesktopServicesPriv.md)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUI.framework/Versions/A/DeviceDiscoveryUI](DYLIBS/DeviceDiscoveryUI.md)
- [/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Versions/A/DeviceExpertIntents](DYLIBS/DeviceExpertIntents.md)
- [/System/Library/PrivateFrameworks/DeviceExpertUI.framework/Versions/A/DeviceExpertUI](DYLIBS/DeviceExpertUI.md)
- [/System/Library/PrivateFrameworks/DeviceManagement.framework/Versions/A/DeviceManagement](DYLIBS/DeviceManagement.md)
- [/System/Library/PrivateFrameworks/DeviceSpecSupport.framework/Versions/A/DeviceSpecSupport](DYLIBS/DeviceSpecSupport.md)
- [/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/Versions/A/DiagnosticRequestService](DYLIBS/DiagnosticRequestService.md)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/Versions/A/DialogEngine](DYLIBS/DialogEngine.md)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/Versions/A/DifferentialPrivacy](DYLIBS/DifferentialPrivacy.md)
- [/System/Library/PrivateFrameworks/DirectResource.framework/Versions/A/DirectResource](DYLIBS/DirectResource.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/Versions/A/DiskImages2](DYLIBS/DiskImages2.md)
- [/System/Library/PrivateFrameworks/DistributedEvaluation.framework/Versions/A/DistributedEvaluation](DYLIBS/DistributedEvaluation.md)
- [/System/Library/PrivateFrameworks/DistributedTimers.framework/Versions/A/DistributedTimers](DYLIBS/DistributedTimers.md)
- [/System/Library/PrivateFrameworks/DistributedTimersDaemon.framework/Versions/A/DistributedTimersDaemon](DYLIBS/DistributedTimersDaemon.md)
- [/System/Library/PrivateFrameworks/DoNotDisturb.framework/Versions/A/DoNotDisturb](DYLIBS/DoNotDisturb.md)
- [/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/Versions/A/DoNotDisturbServer](DYLIBS/DoNotDisturbServer.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/Versions/A/DocumentUnderstanding](DYLIBS/DocumentUnderstanding.md)
- [/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/Versions/A/DuetActivityScheduler](DYLIBS/DuetActivityScheduler.md)
- [/System/Library/PrivateFrameworks/DynamicDesktop.framework/Versions/A/DynamicDesktop](DYLIBS/DynamicDesktop.md)
- [/System/Library/PrivateFrameworks/EDPSecurity.framework/Versions/A/EDPSecurity](DYLIBS/EDPSecurity.md)
- [/System/Library/PrivateFrameworks/Email.framework/Versions/A/Email](DYLIBS/Email.md)
- [/System/Library/PrivateFrameworks/EmailCore.framework/Versions/A/EmailCore](DYLIBS/EmailCore.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/Versions/A/EmailDaemon](DYLIBS/EmailDaemon.md)
- [/System/Library/PrivateFrameworks/EmailFoundation.framework/Versions/A/EmailFoundation](DYLIBS/EmailFoundation.md)
- [/System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/Versions/A/EmbeddedAcousticRecognition](DYLIBS/EmbeddedAcousticRecognition.md)
- [/System/Library/PrivateFrameworks/EmojiFoundation.framework/Versions/A/EmojiFoundation](DYLIBS/EmojiFoundation.md)
- [/System/Library/PrivateFrameworks/EnhancedLoggingState.framework/Versions/A/EnhancedLoggingState](DYLIBS/EnhancedLoggingState.md)
- [/System/Library/PrivateFrameworks/Espresso.framework/Versions/A/Espresso](DYLIBS/Espresso.md)
- [/System/Library/PrivateFrameworks/ExchangeSync.framework/Versions/A/ExchangeSync](DYLIBS/ExchangeSync.md)
- [/System/Library/PrivateFrameworks/ExtensionKitSettings.framework/Versions/A/ExtensionKitSettings](DYLIBS/ExtensionKitSettings.md)
- [/System/Library/PrivateFrameworks/FMFCore.framework/Versions/A/FMFCore](DYLIBS/FMFCore.md)
- [/System/Library/PrivateFrameworks/FMIPCore.framework/Versions/A/FMIPCore](DYLIBS/FMIPCore.md)
- [/System/Library/PrivateFrameworks/FPFS.framework/Versions/A/FPFS](DYLIBS/FPFS.md)
- [/System/Library/PrivateFrameworks/FRC.framework/Versions/A/FRC](DYLIBS/FRC.md)
- [/System/Library/PrivateFrameworks/FTServices.framework/Versions/A/FTServices](DYLIBS/FTServices.md)
- [/System/Library/PrivateFrameworks/FaceTimeFeatureControl.framework/Versions/A/FaceTimeFeatureControl](DYLIBS/FaceTimeFeatureControl.md)
- [/System/Library/PrivateFrameworks/FaceTimeMacHelperCore.framework/Versions/A/FaceTimeMacHelperCore](DYLIBS/FaceTimeMacHelperCore.md)
- [/System/Library/PrivateFrameworks/FaceTimeNotificationCore.framework/Versions/A/FaceTimeNotificationCore](DYLIBS/FaceTimeNotificationCore.md)
- [/System/Library/PrivateFrameworks/FaceTimeNotificationServiceCore.framework/Versions/A/FaceTimeNotificationServiceCore](DYLIBS/FaceTimeNotificationServiceCore.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/Versions/A/FamilyCircle](DYLIBS/FamilyCircle.md)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/Versions/A/FamilyCircleUI](DYLIBS/FamilyCircleUI.md)
- [/System/Library/PrivateFrameworks/FeatureStore.framework/Versions/A/FeatureStore](DYLIBS/FeatureStore.md)
- [/System/Library/PrivateFrameworks/FedStats.framework/Versions/A/FedStats](DYLIBS/FedStats.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/Versions/A/Feedback](DYLIBS/Feedback.md)
- [/System/Library/PrivateFrameworks/FeedbackLogger.framework/Versions/A/FeedbackLogger](DYLIBS/FeedbackLogger.md)
- [/System/Library/PrivateFrameworks/FeedbackService.framework/Versions/A/FeedbackService](DYLIBS/FeedbackService.md)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/Versions/A/FileProviderDaemon](DYLIBS/FileProviderDaemon.md)
- [/System/Library/PrivateFrameworks/FinanceDaemon.framework/Versions/A/FinanceDaemon](DYLIBS/FinanceDaemon.md)
- [/System/Library/PrivateFrameworks/FindMyBase.framework/Versions/A/FindMyBase](DYLIBS/FindMyBase.md)
- [/System/Library/PrivateFrameworks/FindMyBluetooth.framework/Versions/A/FindMyBluetooth](DYLIBS/FindMyBluetooth.md)
- [/System/Library/PrivateFrameworks/FindMyCloudKit.framework/Versions/A/FindMyCloudKit](DYLIBS/FindMyCloudKit.md)
- [/System/Library/PrivateFrameworks/FindMyCommon.framework/Versions/A/FindMyCommon](DYLIBS/FindMyCommon.md)
- [/System/Library/PrivateFrameworks/FindMyDaemonSupport.framework/Versions/A/FindMyDaemonSupport](DYLIBS/FindMyDaemonSupport.md)
- [/System/Library/PrivateFrameworks/FindMyLocate.framework/Versions/A/FindMyLocate](DYLIBS/FindMyLocate.md)
- [/System/Library/PrivateFrameworks/FindMyLocateObjCWrapper.framework/Versions/A/FindMyLocateObjCWrapper](DYLIBS/FindMyLocateObjCWrapper.md)
- [/System/Library/PrivateFrameworks/FindMyMessaging.framework/Versions/A/FindMyMessaging](DYLIBS/FindMyMessaging.md)
- [/System/Library/PrivateFrameworks/FindMyUnsafeAsyncBridging.framework/Versions/A/FindMyUnsafeAsyncBridging](DYLIBS/FindMyUnsafeAsyncBridging.md)
- [/System/Library/PrivateFrameworks/FinderKit.framework/Versions/A/FinderKit](DYLIBS/FinderKit.md)
- [/System/Library/PrivateFrameworks/FocusSettingsUI.framework/Versions/A/FocusSettingsUI](DYLIBS/FocusSettingsUI.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib](DYLIBS/libFontParser.dylib.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libXTFontStaticRegistryData.dylib](DYLIBS/libXTFontStaticRegistryData.dylib.md)
- [/System/Library/PrivateFrameworks/FrontBoard.framework/Versions/A/FrontBoard](DYLIBS/FrontBoard.md)
- [/System/Library/PrivateFrameworks/FrontBoardServices.framework/Versions/A/FrontBoardServices](DYLIBS/FrontBoardServices.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libComposeFilters.dylib](DYLIBS/libComposeFilters.dylib.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libGPUCompiler.dylib](DYLIBS/libGPUCompiler.dylib.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libGPUCompilerImpl.dylib](DYLIBS/libGPUCompilerImpl.dylib.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libLLVM.dylib](DYLIBS/libLLVM.dylib.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libllvm-flatbuffers.dylib](DYLIBS/libllvm-flatbuffers.dylib.md)
- [/System/Library/PrivateFrameworks/GPUToolsTransport.framework/Versions/A/GPUToolsTransport](DYLIBS/GPUToolsTransport.md)
- [/System/Library/PrivateFrameworks/GRDBInternal.framework/Versions/A/GRDBInternal](DYLIBS/GRDBInternal.md)
- [/System/Library/PrivateFrameworks/GameCenterFoundation.framework/Versions/A/GameCenterFoundation](DYLIBS/GameCenterFoundation.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/Versions/A/GameCenterUI](DYLIBS/GameCenterUI.md)
- [/System/Library/PrivateFrameworks/GameCenterUICore.framework/Versions/A/GameCenterUICore](DYLIBS/GameCenterUICore.md)
- [/System/Library/PrivateFrameworks/GameServicesProtocols.framework/Versions/A/GameServicesProtocols](DYLIBS/GameServicesProtocols.md)
- [/System/Library/PrivateFrameworks/GenerationalStorage.framework/Versions/A/GenerationalStorage](DYLIBS/GenerationalStorage.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiences.framework/Versions/A/GenerativeExperiences](DYLIBS/GenerativeExperiences.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/Versions/A/GenerativeExperiencesRuntime](DYLIBS/GenerativeExperiencesRuntime.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctions.framework/Versions/A/GenerativeFunctions](DYLIBS/GenerativeFunctions.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/Versions/A/GenerativeFunctionsFoundation](DYLIBS/GenerativeFunctionsFoundation.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/Versions/A/GenerativeFunctionsInstrumentation](DYLIBS/GenerativeFunctionsInstrumentation.md)
- [/System/Library/PrivateFrameworks/GenerativeModels.framework/Versions/A/GenerativeModels](DYLIBS/GenerativeModels.md)
- [/System/Library/PrivateFrameworks/GenerativeModelsFoundation.framework/Versions/A/GenerativeModelsFoundation](DYLIBS/GenerativeModelsFoundation.md)
- [/System/Library/PrivateFrameworks/GenerativePlaygroundUI.framework/Versions/A/GenerativePlaygroundUI](DYLIBS/GenerativePlaygroundUI.md)
- [/System/Library/PrivateFrameworks/GeoAnalytics.framework/Versions/A/GeoAnalytics](DYLIBS/GeoAnalytics.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/Versions/A/GeoServices](DYLIBS/GeoServices.md)
- [/System/Library/PrivateFrameworks/GeoUIFramework.framework/Versions/A/GeoUIFramework](DYLIBS/GeoUIFramework.md)
- [/System/Library/PrivateFrameworks/GroupKitCrypto.framework/Versions/A/GroupKitCrypto](DYLIBS/GroupKitCrypto.md)
- [/System/Library/PrivateFrameworks/H16ISPServices.framework/Versions/A/H16ISPServices](DYLIBS/H16ISPServices.md)
- [/System/Library/PrivateFrameworks/HMFoundation.framework/Versions/A/HMFoundation](DYLIBS/HMFoundation.md)
- [/System/Library/PrivateFrameworks/HeadGestures.framework/Versions/A/HeadGestures](DYLIBS/HeadGestures.md)
- [/System/Library/PrivateFrameworks/HeadphoneManager.framework/Versions/A/HeadphoneManager](DYLIBS/HeadphoneManager.md)
- [/System/Library/PrivateFrameworks/HeadphoneProxFeatureService.framework/Versions/A/HeadphoneProxFeatureService](DYLIBS/HeadphoneProxFeatureService.md)
- [/System/Library/PrivateFrameworks/HealthDaemon.framework/Versions/A/HealthDaemon](DYLIBS/HealthDaemon.md)
- [/System/Library/PrivateFrameworks/HealthKitAdditions.framework/Versions/A/HealthKitAdditions](DYLIBS/HealthKitAdditions.md)
- [/System/Library/PrivateFrameworks/HearingModeService.framework/Versions/A/HearingModeService](DYLIBS/HearingModeService.md)
- [/System/Library/PrivateFrameworks/HearingModeService_Private.framework/Versions/A/HearingModeService_Private](DYLIBS/HearingModeService_Private.md)
- [/System/Library/PrivateFrameworks/HearingUtilities.framework/Versions/A/HearingUtilities](DYLIBS/HearingUtilities.md)
- [/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Versions/A/HomeAutomationInternal](DYLIBS/HomeAutomationInternal.md)
- [/System/Library/PrivateFrameworks/HomeAutomationUIFramework.framework/Versions/A/HomeAutomationUIFramework](DYLIBS/HomeAutomationUIFramework.md)
- [/System/Library/PrivateFrameworks/HomeDataModel.framework/Versions/A/HomeDataModel](DYLIBS/HomeDataModel.md)
- [/System/Library/PrivateFrameworks/HomeKit.framework/Versions/A/HomeKit](DYLIBS/HomeKit.md)
- [/System/Library/PrivateFrameworks/HomeKitCore.framework/Versions/A/HomeKitCore](DYLIBS/HomeKitCore.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Versions/A/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/Versions/A/HomeKitEvents](DYLIBS/HomeKitEvents.md)
- [/System/Library/PrivateFrameworks/HomeKitMatter.framework/Versions/A/HomeKitMatter](DYLIBS/HomeKitMatter.md)
- [/System/Library/PrivateFrameworks/HomeKitMetrics.framework/Versions/A/HomeKitMetrics](DYLIBS/HomeKitMetrics.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/Versions/A/HomePlatformSettingsUI](DYLIBS/HomePlatformSettingsUI.md)
- [/System/Library/PrivateFrameworks/HumanUnderstandingEvidence.framework/Versions/A/HumanUnderstandingEvidence](DYLIBS/HumanUnderstandingEvidence.md)
- [/System/Library/PrivateFrameworks/HumanUnderstandingFoundation.framework/Versions/A/HumanUnderstandingFoundation](DYLIBS/HumanUnderstandingFoundation.md)
- [/System/Library/PrivateFrameworks/IDS.framework/Versions/A/IDS](DYLIBS/IDS.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/Versions/A/IDSFoundation](DYLIBS/IDSFoundation.md)
- [/System/Library/PrivateFrameworks/IMAP.framework/Versions/A/IMAP](DYLIBS/IMAP.md)
- [/System/Library/PrivateFrameworks/IMAssistantCore.framework/Versions/A/IMAssistantCore](DYLIBS/IMAssistantCore.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/Versions/A/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/Versions/A/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/Versions/A/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMFoundation.framework/Versions/A/IMFoundation](DYLIBS/IMFoundation.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/Versions/A/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/IMTranscoderAgent.framework/Versions/A/IMTranscoderAgent](DYLIBS/IMTranscoderAgent.md)
- [/System/Library/PrivateFrameworks/IMTransferAgent.framework/Versions/A/IMTransferAgent](DYLIBS/IMTransferAgent.md)
- [/System/Library/PrivateFrameworks/IMTransferServices.framework/Versions/A/IMTransferServices](DYLIBS/IMTransferServices.md)
- [/System/Library/PrivateFrameworks/IO80211.framework/Versions/A/IO80211](DYLIBS/IO80211.md)
- [/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib](DYLIBS/libIPTelephony.dylib.md)
- [/System/Library/PrivateFrameworks/IconFoundation.framework/Versions/A/IconFoundation](DYLIBS/IconFoundation.md)
- [/System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices](DYLIBS/IconServices.md)
- [/System/Library/PrivateFrameworks/ImageHarmonizationKit.framework/Versions/A/ImageHarmonizationKit](DYLIBS/ImageHarmonizationKit.md)
- [/System/Library/PrivateFrameworks/InfoQueryPersonalizationFeatures.framework/Versions/A/InfoQueryPersonalizationFeatures](DYLIBS/InfoQueryPersonalizationFeatures.md)
- [/System/Library/PrivateFrameworks/InputAnalytics.framework/Versions/A/InputAnalytics](DYLIBS/InputAnalytics.md)
- [/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/Versions/A/InputAnalyticsServer](DYLIBS/InputAnalyticsServer.md)
- [/System/Library/PrivateFrameworks/InputTranscoder.framework/Versions/A/InputTranscoder](DYLIBS/InputTranscoder.md)
- [/System/Library/PrivateFrameworks/InstallCoordination.framework/Versions/A/InstallCoordination](DYLIBS/InstallCoordination.md)
- [/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/Versions/A/InstalledContentLibrary](DYLIBS/InstalledContentLibrary.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlow.framework/Versions/A/IntelligenceFlow](DYLIBS/IntelligenceFlow.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowAppIntentsPreviewToolSupport.framework/Versions/A/IntelligenceFlowAppIntentsPreviewToolSupport](DYLIBS/IntelligenceFlowAppIntentsPreviewToolSupport.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContext.framework/Versions/A/IntelligenceFlowContext](DYLIBS/IntelligenceFlowContext.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/Versions/A/IntelligenceFlowContextRuntime](DYLIBS/IntelligenceFlowContextRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Versions/A/IntelligenceFlowPlannerRuntime](DYLIBS/IntelligenceFlowPlannerRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/Versions/A/IntelligenceFlowPlannerSupport](DYLIBS/IntelligenceFlowPlannerSupport.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/Versions/A/IntelligenceFlowRuntime](DYLIBS/IntelligenceFlowRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowShared.framework/Versions/A/IntelligenceFlowShared](DYLIBS/IntelligenceFlowShared.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/Versions/A/IntelligencePlatform](DYLIBS/IntelligencePlatform.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/Versions/A/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/Versions/A/IntelligencePlatformLibrary](DYLIBS/IntelligencePlatformLibrary.md)
- [/System/Library/PrivateFrameworks/IntelligentRoutingDaemon.framework/Versions/A/IntelligentRoutingDaemon](DYLIBS/IntelligentRoutingDaemon.md)
- [/System/Library/PrivateFrameworks/IntentsCore.framework/Versions/A/IntentsCore](DYLIBS/IntentsCore.md)
- [/System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/Versions/A/InternalSwiftProtobuf](DYLIBS/InternalSwiftProtobuf.md)
- [/System/Library/PrivateFrameworks/InternationalSupport.framework/Versions/A/InternationalSupport](DYLIBS/InternationalSupport.md)
- [/System/Library/PrivateFrameworks/IntlPreferences.framework/Versions/A/IntlPreferences](DYLIBS/IntlPreferences.md)
- [/System/Library/PrivateFrameworks/JetEngine.framework/Versions/A/JetEngine](DYLIBS/JetEngine.md)
- [/System/Library/PrivateFrameworks/JetUI.framework/Versions/A/JetUI](DYLIBS/JetUI.md)
- [/System/Library/PrivateFrameworks/KeychainCircle.framework/Versions/A/KeychainCircle](DYLIBS/KeychainCircle.md)
- [/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/Versions/A/KnowledgeGraphKit](DYLIBS/KnowledgeGraphKit.md)
- [/System/Library/PrivateFrameworks/Koa.framework/Versions/A/Koa](DYLIBS/Koa.md)
- [/System/Library/PrivateFrameworks/LLMCache.framework/Versions/A/LLMCache](DYLIBS/LLMCache.md)
- [/System/Library/PrivateFrameworks/LanguageModeling.framework/Versions/A/LanguageModeling](DYLIBS/LanguageModeling.md)
- [/System/Library/PrivateFrameworks/Leonardo.framework/Versions/A/Leonardo](DYLIBS/Leonardo.md)
- [/System/Library/PrivateFrameworks/Lexicon.framework/Versions/A/Lexicon](DYLIBS/Lexicon.md)
- [/System/Library/PrivateFrameworks/LiftUI.framework/Versions/A/LiftUI](DYLIBS/LiftUI.md)
- [/System/Library/PrivateFrameworks/LighthouseBackground.framework/Versions/A/LighthouseBackground](DYLIBS/LighthouseBackground.md)
- [/System/Library/PrivateFrameworks/LighthouseDataProcessor.framework/Versions/A/LighthouseDataProcessor](DYLIBS/LighthouseDataProcessor.md)
- [/System/Library/PrivateFrameworks/LinkMetadata.framework/Versions/A/LinkMetadata](DYLIBS/LinkMetadata.md)
- [/System/Library/PrivateFrameworks/LinkPresentationStyleSheetParsing.framework/Versions/A/LinkPresentationStyleSheetParsing](DYLIBS/LinkPresentationStyleSheetParsing.md)
- [/System/Library/PrivateFrameworks/LinkServices.framework/Versions/A/LinkServices](DYLIBS/LinkServices.md)
- [/System/Library/PrivateFrameworks/LiveExecutionResultsProbe.framework/Versions/A/LiveExecutionResultsProbe](DYLIBS/LiveExecutionResultsProbe.md)
- [/System/Library/PrivateFrameworks/LiveSpeechServices.framework/Versions/A/LiveSpeechServices](DYLIBS/LiveSpeechServices.md)
- [/System/Library/PrivateFrameworks/LiveTranscription.framework/Versions/A/LiveTranscription](DYLIBS/LiveTranscription.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/Versions/A/LocalAuthenticationCore](DYLIBS/LocalAuthenticationCore.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/Versions/A/LocalAuthenticationCoreUI](DYLIBS/LocalAuthenticationCoreUI.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationUI.framework/Versions/A/LocalAuthenticationUI](DYLIBS/LocalAuthenticationUI.md)
- [/System/Library/PrivateFrameworks/LocalStatusKit.framework/Versions/A/LocalStatusKit](DYLIBS/LocalStatusKit.md)
- [/System/Library/PrivateFrameworks/LoginUIKit.framework/Versions/A/LoginUIKit](DYLIBS/LoginUIKit.md)
- [/System/Library/PrivateFrameworks/MCCKitCategorization_macOS.framework/Versions/A/MCCKitCategorization_macOS](DYLIBS/MCCKitCategorization_macOS.md)
- [/System/Library/PrivateFrameworks/MIL.framework/Versions/A/MIL](DYLIBS/MIL.md)
- [/System/Library/PrivateFrameworks/MLModelSpecification.framework/Versions/A/MLModelSpecification](DYLIBS/MLModelSpecification.md)
- [/System/Library/PrivateFrameworks/MMCS.framework/Versions/A/MMCS](DYLIBS/MMCS.md)
- [/System/Library/PrivateFrameworks/MTLCompiler.framework/Versions/32023/MTLCompiler](DYLIBS/MTLCompiler.md)
- [/System/Library/PrivateFrameworks/MTLCompiler.framework/Versions/32024/MTLCompiler](DYLIBS/MTLCompiler.md)
- [/System/Library/PrivateFrameworks/Mail.framework/Versions/A/Mail](DYLIBS/Mail.md)
- [/System/Library/PrivateFrameworks/MailCore.framework/Versions/A/MailCore](DYLIBS/MailCore.md)
- [/System/Library/PrivateFrameworks/MailSupport.framework/Versions/A/MailSupport](DYLIBS/MailSupport.md)
- [/System/Library/PrivateFrameworks/MailUI.framework/Versions/A/MailUI](DYLIBS/MailUI.md)
- [/System/Library/PrivateFrameworks/MailWebProcessSupport.framework/Versions/A/MailWebProcessSupport](DYLIBS/MailWebProcessSupport.md)
- [/System/Library/PrivateFrameworks/MallocStackLogging.framework/Versions/A/MallocStackLogging](DYLIBS/MallocStackLogging.md)
- [/System/Library/PrivateFrameworks/ManagedConfigurationFiles.framework/Versions/A/ManagedConfigurationFiles](DYLIBS/ManagedConfigurationFiles.md)
- [/System/Library/PrivateFrameworks/MapsSuggestions.framework/Versions/A/MapsSuggestions](DYLIBS/MapsSuggestions.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/Versions/A/MapsSupport](DYLIBS/MapsSupport.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/Versions/A/MapsSync](DYLIBS/MapsSync.md)
- [/System/Library/PrivateFrameworks/MapsUI.framework/Versions/A/MapsUI](DYLIBS/MapsUI.md)
- [/System/Library/PrivateFrameworks/Marrs.framework/Versions/A/Marrs](DYLIBS/Marrs.md)
- [/System/Library/PrivateFrameworks/MathTypesetting.framework/Versions/A/MathTypesetting](DYLIBS/MathTypesetting.md)
- [/System/Library/PrivateFrameworks/MatrixKit.framework/Versions/A/MatrixKit](DYLIBS/MatrixKit.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/Versions/A/MediaAnalysis](DYLIBS/MediaAnalysis.md)
- [/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/Versions/A/MediaAnalysisServices](DYLIBS/MediaAnalysisServices.md)
- [/System/Library/PrivateFrameworks/MediaControl.framework/Versions/A/MediaControl](DYLIBS/MediaControl.md)
- [/System/Library/PrivateFrameworks/MediaCoreUI.framework/Versions/A/MediaCoreUI](DYLIBS/MediaCoreUI.md)
- [/System/Library/PrivateFrameworks/MediaExperience.framework/Versions/A/MediaExperience](DYLIBS/MediaExperience.md)
- [/System/Library/PrivateFrameworks/MediaFoundation.framework/Versions/A/MediaFoundation](DYLIBS/MediaFoundation.md)
- [/System/Library/PrivateFrameworks/MediaML.framework/Versions/A/MediaML](DYLIBS/MediaML.md)
- [/System/Library/PrivateFrameworks/MediaMiningKit.framework/Versions/A/MediaMiningKit](DYLIBS/MediaMiningKit.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/Versions/A/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Versions/A/MediaRemote](DYLIBS/MediaRemote.md)
- [/System/Library/PrivateFrameworks/MediaServices.framework/Versions/A/MediaServices](DYLIBS/MediaServices.md)
- [/System/Library/PrivateFrameworks/MessageProtection.framework/Versions/A/MessageProtection](DYLIBS/MessageProtection.md)
- [/System/Library/PrivateFrameworks/MessageSecurity.framework/Versions/A/MessageSecurity](DYLIBS/MessageSecurity.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/Versions/A/MessagesBlastDoorSupport](DYLIBS/MessagesBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/MessagesCloudSync.framework/Versions/A/MessagesCloudSync](DYLIBS/MessagesCloudSync.md)
- [/System/Library/PrivateFrameworks/MetadataUtilities.framework/Versions/A/MetadataUtilities](DYLIBS/MetadataUtilities.md)
- [/System/Library/PrivateFrameworks/MetalTools.framework/Versions/A/MetalTools](DYLIBS/MetalTools.md)
- [/System/Library/PrivateFrameworks/MetricMeasurement.framework/Versions/A/MetricMeasurement](DYLIBS/MetricMeasurement.md)
- [/System/Library/PrivateFrameworks/MetricsFramework.framework/Versions/A/MetricsFramework](DYLIBS/MetricsFramework.md)
- [/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/Versions/A/MicroLocationDaemon](DYLIBS/MicroLocationDaemon.md)
- [/System/Library/PrivateFrameworks/MobileBluetooth.framework/Versions/A/MobileBluetooth](DYLIBS/MobileBluetooth.md)
- [/System/Library/PrivateFrameworks/MobileContainerManager.framework/Versions/A/MobileContainerManager](DYLIBS/MobileContainerManager.md)
- [/System/Library/PrivateFrameworks/MobileInstallation.framework/Versions/A/MobileInstallation](DYLIBS/MobileInstallation.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoCore.framework/Versions/A/MobileStoreDemoCore](DYLIBS/MobileStoreDemoCore.md)
- [/System/Library/PrivateFrameworks/MobileTimerSupport.framework/Versions/A/MobileTimerSupport](DYLIBS/MobileTimerSupport.md)
- [/System/Library/PrivateFrameworks/ModalityXObjects.framework/Versions/A/ModalityXObjects](DYLIBS/ModalityXObjects.md)
- [/System/Library/PrivateFrameworks/ModelCatalog.framework/Versions/A/ModelCatalog](DYLIBS/ModelCatalog.md)
- [/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/Versions/A/ModelCatalogRuntime](DYLIBS/ModelCatalogRuntime.md)
- [/System/Library/PrivateFrameworks/ModelManagerServices.framework/Versions/A/ModelManagerServices](DYLIBS/ModelManagerServices.md)
- [/System/Library/PrivateFrameworks/MorphunSwift.framework/Versions/A/MorphunSwift](DYLIBS/MorphunSwift.md)
- [/System/Library/PrivateFrameworks/MusicKitInternal.framework/Versions/A/MusicKitInternal](DYLIBS/MusicKitInternal.md)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/Versions/A/MusicLibrary](DYLIBS/MusicLibrary.md)
- [/System/Library/PrivateFrameworks/MusicUI.framework/Versions/A/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/PrivateFrameworks/Navigation.framework/Versions/A/Navigation](DYLIBS/Navigation.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/Versions/A/NeighborhoodActivityConduit](DYLIBS/NeighborhoodActivityConduit.md)
- [/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/Versions/A/NetworkServiceProxy](DYLIBS/NetworkServiceProxy.md)
- [/System/Library/PrivateFrameworks/NeuralNetworks.framework/Versions/A/NeuralNetworks](DYLIBS/NeuralNetworks.md)
- [/System/Library/PrivateFrameworks/NeutrinoCore.framework/Versions/A/NeutrinoCore](DYLIBS/NeutrinoCore.md)
- [/System/Library/PrivateFrameworks/NeutrinoKit.framework/Versions/A/NeutrinoKit](DYLIBS/NeutrinoKit.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/Versions/A/NewDeviceOutreach](DYLIBS/NewDeviceOutreach.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreachMacUI.framework/Versions/A/NewDeviceOutreachMacUI](DYLIBS/NewDeviceOutreachMacUI.md)
- [/System/Library/PrivateFrameworks/NewsAnalyticsUpload.framework/Versions/A/NewsAnalyticsUpload](DYLIBS/NewsAnalyticsUpload.md)
- [/System/Library/PrivateFrameworks/NewsCore.framework/Versions/A/NewsCore](DYLIBS/NewsCore.md)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/Versions/A/NewsDaemon](DYLIBS/NewsDaemon.md)
- [/System/Library/PrivateFrameworks/NewsFoundation.framework/Versions/A/NewsFoundation](DYLIBS/NewsFoundation.md)
- [/System/Library/PrivateFrameworks/NewsToday.framework/Versions/A/NewsToday](DYLIBS/NewsToday.md)
- [/System/Library/PrivateFrameworks/NewsURLResolution.framework/Versions/A/NewsURLResolution](DYLIBS/NewsURLResolution.md)
- [/System/Library/PrivateFrameworks/Nexus.framework/Versions/A/Nexus](DYLIBS/Nexus.md)
- [/System/Library/PrivateFrameworks/NexusDaemon.framework/Versions/A/NexusDaemon](DYLIBS/NexusDaemon.md)
- [/System/Library/PrivateFrameworks/NotesEditor.framework/Versions/A/NotesEditor](DYLIBS/NotesEditor.md)
- [/System/Library/PrivateFrameworks/NotesShared.framework/Versions/A/NotesShared](DYLIBS/NotesShared.md)
- [/System/Library/PrivateFrameworks/NotesSiriUI.framework/Versions/A/NotesSiriUI](DYLIBS/NotesSiriUI.md)
- [/System/Library/PrivateFrameworks/NotesSupport.framework/Versions/A/NotesSupport](DYLIBS/NotesSupport.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/Versions/A/NotesUI](DYLIBS/NotesUI.md)
- [/System/Library/PrivateFrameworks/NotificationCenterUI.framework/Versions/A/NotificationCenterUI](DYLIBS/NotificationCenterUI.md)
- [/System/Library/PrivateFrameworks/OSIntelligence.framework/Versions/A/OSIntelligence](DYLIBS/OSIntelligence.md)
- [/System/Library/PrivateFrameworks/OSUpdate.framework/Versions/A/OSUpdate](DYLIBS/OSUpdate.md)
- [/System/Library/PrivateFrameworks/OfficeImport.framework/Versions/A/OfficeImport](DYLIBS/OfficeImport.md)
- [/System/Library/PrivateFrameworks/OmniSearch.framework/Versions/A/OmniSearch](DYLIBS/OmniSearch.md)
- [/System/Library/PrivateFrameworks/OmniSearchTypes.framework/Versions/A/OmniSearchTypes](DYLIBS/OmniSearchTypes.md)
- [/System/Library/PrivateFrameworks/OnBoardingKit.framework/Versions/A/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/PrivateFrameworks/PAImaging.framework/Versions/A/PAImaging](DYLIBS/PAImaging.md)
- [/System/Library/PrivateFrameworks/PackageKit.framework/Versions/A/PackageKit](DYLIBS/PackageKit.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/Versions/A/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/Versions/A/PassKitCore](DYLIBS/PassKitCore.md)
- [/System/Library/PrivateFrameworks/PassKitMacHelper.framework/Versions/A/PassKitMacHelper](DYLIBS/PassKitMacHelper.md)
- [/System/Library/PrivateFrameworks/PassKitUI.framework/Versions/A/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/Versions/A/PasswordManagerUI](DYLIBS/PasswordManagerUI.md)
- [/System/Library/PrivateFrameworks/PaymentUIBase.framework/Versions/A/PaymentUIBase](DYLIBS/PaymentUIBase.md)
- [/System/Library/PrivateFrameworks/PegasusAPI.framework/Versions/A/PegasusAPI](DYLIBS/PegasusAPI.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/Versions/A/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PegasusKit.framework/Versions/A/PegasusKit](DYLIBS/PegasusKit.md)
- [/System/Library/PrivateFrameworks/PegasusPersistence.framework/Versions/A/PegasusPersistence](DYLIBS/PegasusPersistence.md)
- [/System/Library/PrivateFrameworks/People.framework/Versions/A/People](DYLIBS/People.md)
- [/System/Library/PrivateFrameworks/PeopleSuggester.framework/Versions/A/PeopleSuggester](DYLIBS/PeopleSuggester.md)
- [/System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/Versions/A/PerfPowerMetricMonitor](DYLIBS/PerfPowerMetricMonitor.md)
- [/System/Library/PrivateFrameworks/PersonalAudio.framework/Versions/A/PersonalAudio](DYLIBS/PersonalAudio.md)
- [/System/Library/PrivateFrameworks/PersonalizationPortraitInternals.framework/Versions/A/PersonalizationPortraitInternals](DYLIBS/PersonalizationPortraitInternals.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/Versions/A/PersonalizedSensing](DYLIBS/PersonalizedSensing.md)
- [/System/Library/PrivateFrameworks/PhoneSnippetUI.framework/Versions/A/PhoneSnippetUI](DYLIBS/PhoneSnippetUI.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Versions/A/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotoImaging.framework/Versions/A/PhotoImaging](DYLIBS/PhotoImaging.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/Versions/A/PhotoLibraryServices](DYLIBS/PhotoLibraryServices.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/Versions/A/PhotoLibraryServicesCore](DYLIBS/PhotoLibraryServicesCore.md)
- [/System/Library/PrivateFrameworks/PhotosFormats.framework/Versions/A/PhotosFormats](DYLIBS/PhotosFormats.md)
- [/System/Library/PrivateFrameworks/PhotosGraph.framework/Versions/A/PhotosGraph](DYLIBS/PhotosGraph.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/Versions/A/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligenceCore.framework/Versions/A/PhotosIntelligenceCore](DYLIBS/PhotosIntelligenceCore.md)
- [/System/Library/PrivateFrameworks/PhotosKnowledgeGraph.framework/Versions/A/PhotosKnowledgeGraph](DYLIBS/PhotosKnowledgeGraph.md)
- [/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/Versions/A/PhotosSwiftUICore](DYLIBS/PhotosSwiftUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/Versions/A/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIEdit.framework/Versions/A/PhotosUIEdit](DYLIBS/PhotosUIEdit.md)
- [/System/Library/PrivateFrameworks/PhotosUIFoundation.framework/Versions/A/PhotosUIFoundation](DYLIBS/PhotosUIFoundation.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/Versions/A/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PhotosensitivityProcessing.framework/Versions/A/PhotosensitivityProcessing](DYLIBS/PhotosensitivityProcessing.md)
- [/System/Library/PrivateFrameworks/Planks.framework/Versions/A/Planks](DYLIBS/Planks.md)
- [/System/Library/PrivateFrameworks/PlatformSSO.framework/Versions/A/PlatformSSO](DYLIBS/PlatformSSO.md)
- [/System/Library/PrivateFrameworks/PlatformSSOCore.framework/Versions/A/PlatformSSOCore](DYLIBS/PlatformSSOCore.md)
- [/System/Library/PrivateFrameworks/PnROnDeviceFramework.framework/Versions/A/PnROnDeviceFramework](DYLIBS/PnROnDeviceFramework.md)
- [/System/Library/PrivateFrameworks/PodcastsFoundation.framework/Versions/A/PodcastsFoundation](DYLIBS/PodcastsFoundation.md)
- [/System/Library/PrivateFrameworks/PoirotBlocks.framework/Versions/A/PoirotBlocks](DYLIBS/PoirotBlocks.md)
- [/System/Library/PrivateFrameworks/PoirotSQLite.framework/Versions/A/PoirotSQLite](DYLIBS/PoirotSQLite.md)
- [/System/Library/PrivateFrameworks/PoirotSchematizer.framework/Versions/A/PoirotSchematizer](DYLIBS/PoirotSchematizer.md)
- [/System/Library/PrivateFrameworks/PoirotUDFs.framework/Versions/A/PoirotUDFs](DYLIBS/PoirotUDFs.md)
- [/System/Library/PrivateFrameworks/Portrait.framework/Versions/A/Portrait](DYLIBS/Portrait.md)
- [/System/Library/PrivateFrameworks/PostSiriEngagement.framework/Versions/A/PostSiriEngagement](DYLIBS/PostSiriEngagement.md)
- [/System/Library/PrivateFrameworks/PowerExperience.framework/Versions/A/PowerExperience](DYLIBS/PowerExperience.md)
- [/System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog](DYLIBS/PowerLog.md)
- [/System/Library/PrivateFrameworks/PowerUI.framework/Versions/A/PowerUI](DYLIBS/PowerUI.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/Versions/A/PowerlogCore](DYLIBS/PowerlogCore.md)
- [/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/Versions/A/PowerlogHelperdOperators](DYLIBS/PowerlogHelperdOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/Versions/A/PowerlogLiteOperators](DYLIBS/PowerlogLiteOperators.md)
- [/System/Library/PrivateFrameworks/PreviewShellKit.framework/Versions/A/PreviewShellKit](DYLIBS/PreviewShellKit.md)
- [/System/Library/PrivateFrameworks/PreviewsFoundationOS.framework/Versions/A/PreviewsFoundationOS](DYLIBS/PreviewsFoundationOS.md)
- [/System/Library/PrivateFrameworks/PreviewsInjection.framework/Versions/A/PreviewsInjection](DYLIBS/PreviewsInjection.md)
- [/System/Library/PrivateFrameworks/PreviewsMessagingOS.framework/Versions/A/PreviewsMessagingOS](DYLIBS/PreviewsMessagingOS.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Versions/A/PreviewsOSSupport](DYLIBS/PreviewsOSSupport.md)
- [/System/Library/PrivateFrameworks/PreviewsServices.framework/Versions/A/PreviewsServices](DYLIBS/PreviewsServices.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/Versions/A/PrivateCloudCompute](DYLIBS/PrivateCloudCompute.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/Versions/A/PrivateFederatedLearning](DYLIBS/PrivateFederatedLearning.md)
- [/System/Library/PrivateFrameworks/PrivateMLClient.framework/Versions/A/PrivateMLClient](DYLIBS/PrivateMLClient.md)
- [/System/Library/PrivateFrameworks/PrivateMLClientInferenceProvider.framework/Versions/A/PrivateMLClientInferenceProvider](DYLIBS/PrivateMLClientInferenceProvider.md)
- [/System/Library/PrivateFrameworks/ProDisplayLibrary.framework/Versions/A/ProDisplayLibrary](DYLIBS/ProDisplayLibrary.md)
- [/System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/Versions/A/ProactiveDaemonSupport](DYLIBS/ProactiveDaemonSupport.md)
- [/System/Library/PrivateFrameworks/ProactiveSuggestionClientModel.framework/Versions/A/ProactiveSuggestionClientModel](DYLIBS/ProactiveSuggestionClientModel.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarization.framework/Versions/A/ProactiveSummarization](DYLIBS/ProactiveSummarization.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarizationClient.framework/Versions/A/ProactiveSummarizationClient](DYLIBS/ProactiveSummarizationClient.md)
- [/System/Library/PrivateFrameworks/ProductKit.framework/Versions/A/ProductKit](DYLIBS/ProductKit.md)
- [/System/Library/PrivateFrameworks/PromotedContentPrediction.framework/Versions/A/PromotedContentPrediction](DYLIBS/PromotedContentPrediction.md)
- [/System/Library/PrivateFrameworks/PromptKit.framework/Versions/A/PromptKit](DYLIBS/PromptKit.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetup.framework/Versions/A/ProximityAppleIDSetup](DYLIBS/ProximityAppleIDSetup.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetupUI.framework/Versions/A/ProximityAppleIDSetupUI](DYLIBS/ProximityAppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/QOSToolkit.framework/Versions/A/QOSToolkit](DYLIBS/QOSToolkit.md)
- [/System/Library/PrivateFrameworks/QueryParser.framework/Versions/A/QueryParser](DYLIBS/QueryParser.md)
- [/System/Library/PrivateFrameworks/QueryUnderstanding.framework/Versions/A/QueryUnderstanding](DYLIBS/QueryUnderstanding.md)
- [/System/Library/PrivateFrameworks/QuickLookIosmac.framework/Versions/A/QuickLookIosmac](DYLIBS/QuickLookIosmac.md)
- [/System/Library/PrivateFrameworks/QuickLookSupport.framework/Versions/A/QuickLookSupport](DYLIBS/QuickLookSupport.md)
- [/System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/Versions/A/QuickLookThumbnailingDaemon](DYLIBS/QuickLookThumbnailingDaemon.md)
- [/System/Library/PrivateFrameworks/Rapport.framework/Versions/A/Rapport](DYLIBS/Rapport.md)
- [/System/Library/PrivateFrameworks/RealityFusion.framework/Versions/A/RealityFusion](DYLIBS/RealityFusion.md)
- [/System/Library/PrivateFrameworks/RealityIO.framework/Versions/A/RealityIO](DYLIBS/RealityIO.md)
- [/System/Library/PrivateFrameworks/Recount.framework/Versions/A/Recount](DYLIBS/Recount.md)
- [/System/Library/PrivateFrameworks/ReminderKit.framework/Versions/A/ReminderKit](DYLIBS/ReminderKit.md)
- [/System/Library/PrivateFrameworks/ReminderKitInternal.framework/Versions/A/ReminderKitInternal](DYLIBS/ReminderKitInternal.md)
- [/System/Library/PrivateFrameworks/ReminderKitUI.framework/Versions/A/ReminderKitUI](DYLIBS/ReminderKitUI.md)
- [/System/Library/PrivateFrameworks/RemindersAppIntents.framework/Versions/A/RemindersAppIntents](DYLIBS/RemindersAppIntents.md)
- [/System/Library/PrivateFrameworks/RemindersUICore.framework/Versions/A/RemindersUICore](DYLIBS/RemindersUICore.md)
- [/System/Library/PrivateFrameworks/RemoteConfiguration.framework/Versions/A/RemoteConfiguration](DYLIBS/RemoteConfiguration.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/Versions/A/RemoteManagement](DYLIBS/RemoteManagement.md)
- [/System/Library/PrivateFrameworks/RemoteManagementStore.framework/Versions/A/RemoteManagementStore](DYLIBS/RemoteManagementStore.md)
- [/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/Versions/A/RemoteServiceDiscovery](DYLIBS/RemoteServiceDiscovery.md)
- [/System/Library/PrivateFrameworks/RemoteTextInput.framework/Versions/A/RemoteTextInput](DYLIBS/RemoteTextInput.md)
- [/System/Library/PrivateFrameworks/RemoteUI.framework/Versions/A/RemoteUI](DYLIBS/RemoteUI.md)
- [/System/Library/PrivateFrameworks/RemoteXPC.framework/Versions/A/RemoteXPC](DYLIBS/RemoteXPC.md)
- [/System/Library/PrivateFrameworks/RenderBox.framework/Versions/A/RenderBox](DYLIBS/RenderBox.md)
- [/System/Library/PrivateFrameworks/ReplicatorCore.framework/Versions/A/ReplicatorCore](DYLIBS/ReplicatorCore.md)
- [/System/Library/PrivateFrameworks/ReplicatorEngine.framework/Versions/A/ReplicatorEngine](DYLIBS/ReplicatorEngine.md)
- [/System/Library/PrivateFrameworks/ReplicatorServices.framework/Versions/A/ReplicatorServices](DYLIBS/ReplicatorServices.md)
- [/System/Library/PrivateFrameworks/RequestDispatcherBridges.framework/Versions/A/RequestDispatcherBridges](DYLIBS/RequestDispatcherBridges.md)
- [/System/Library/PrivateFrameworks/RoomScanCore.framework/Versions/A/RoomScanCore](DYLIBS/RoomScanCore.md)
- [/System/Library/PrivateFrameworks/RunningBoard.framework/Versions/A/RunningBoard](DYLIBS/RunningBoard.md)
- [/System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices](DYLIBS/RunningBoardServices.md)
- [/System/Library/PrivateFrameworks/RuntimeInternal.framework/Versions/A/RuntimeInternal](DYLIBS/RuntimeInternal.md)
- [/System/Library/PrivateFrameworks/SAML.framework/Versions/A/SAML](DYLIBS/SAML.md)
- [/System/Library/PrivateFrameworks/SAObjects.framework/Versions/A/SAObjects](DYLIBS/SAObjects.md)
- [/System/Library/PrivateFrameworks/SDAPI.framework/Versions/A/SDAPI](DYLIBS/SDAPI.md)
- [/System/Library/PrivateFrameworks/SEService.framework/Versions/A/SEService](DYLIBS/SEService.md)
- [/System/Library/PrivateFrameworks/SFSymbols.framework/Versions/A/SFSymbols](DYLIBS/SFSymbols.md)
- [/System/Library/PrivateFrameworks/SMBClient.framework/Versions/A/SMBClient](DYLIBS/SMBClient.md)
- [/System/Library/PrivateFrameworks/SPShared.framework/Versions/A/SPShared](DYLIBS/SPShared.md)
- [/System/Library/PrivateFrameworks/Safari.framework/Versions/A/Safari](DYLIBS/Safari.md)
- [/System/Library/PrivateFrameworks/SafariCore.framework/Versions/A/SafariCore](DYLIBS/SafariCore.md)
- [/System/Library/PrivateFrameworks/SafariShared.framework/Versions/A/SafariShared](DYLIBS/SafariShared.md)
- [/System/Library/PrivateFrameworks/SafariSharedUI.framework/Versions/A/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/Library/PrivateFrameworks/SafariSwift.framework/Versions/A/SafariSwift](DYLIBS/SafariSwift.md)
- [/System/Library/PrivateFrameworks/SafetyMonitor.framework/Versions/A/SafetyMonitor](DYLIBS/SafetyMonitor.md)
- [/System/Library/PrivateFrameworks/Sage.framework/Versions/A/Sage](DYLIBS/Sage.md)
- [/System/Library/PrivateFrameworks/SampleAnalysis.framework/Frameworks/SAHelper.framework/Versions/A/SAHelper](DYLIBS/SAHelper.md)
- [/System/Library/PrivateFrameworks/SampleAnalysis.framework/Versions/A/SampleAnalysis](DYLIBS/SampleAnalysis.md)
- [/System/Library/PrivateFrameworks/ScreenContinuityServices.framework/Versions/A/ScreenContinuityServices](DYLIBS/ScreenContinuityServices.md)
- [/System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/ScreenReader](DYLIBS/ScreenReader.md)
- [/System/Library/PrivateFrameworks/ScreenSharing.framework/Versions/A/ScreenSharing](DYLIBS/ScreenSharing.md)
- [/System/Library/PrivateFrameworks/ScreenSharingKit.framework/Versions/A/ScreenSharingKit](DYLIBS/ScreenSharingKit.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/Versions/A/ScreenTimeCore](DYLIBS/ScreenTimeCore.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/Versions/A/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSwift.framework/Versions/A/ScreenTimeSwift](DYLIBS/ScreenTimeSwift.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUI.framework/Versions/A/ScreenTimeUI](DYLIBS/ScreenTimeUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/Versions/A/ScreenTimeUICore](DYLIBS/ScreenTimeUICore.md)
- [/System/Library/PrivateFrameworks/SearchAds.framework/Versions/A/SearchAds](DYLIBS/SearchAds.md)
- [/System/Library/PrivateFrameworks/SearchAssets.framework/Versions/A/SearchAssets](DYLIBS/SearchAssets.md)
- [/System/Library/PrivateFrameworks/SearchFoundation.framework/Versions/A/SearchFoundation](DYLIBS/SearchFoundation.md)
- [/System/Library/PrivateFrameworks/SearchUI.framework/Versions/A/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/PrivateFrameworks/SearchUICardKitProviderSupport.framework/Versions/A/SearchUICardKitProviderSupport](DYLIBS/SearchUICardKitProviderSupport.md)
- [/System/Library/PrivateFrameworks/SecureTransactionService.framework/Versions/A/SecureTransactionService](DYLIBS/SecureTransactionService.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/Versions/A/SensitiveContentAnalysisML](DYLIBS/SensitiveContentAnalysisML.md)
- [/System/Library/PrivateFrameworks/SentencePieceInternal.framework/Versions/A/SentencePieceInternal](DYLIBS/SentencePieceInternal.md)
- [/System/Library/PrivateFrameworks/ServiceExtensions.framework/Versions/A/ServiceExtensions](DYLIBS/ServiceExtensions.md)
- [/System/Library/PrivateFrameworks/Settings.framework/Versions/A/Settings](DYLIBS/Settings.md)
- [/System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/Versions/A/SetupAssistantSupportUI](DYLIBS/SetupAssistantSupportUI.md)
- [/System/Library/PrivateFrameworks/SetupKit.framework/Versions/A/SetupKit](DYLIBS/SetupKit.md)
- [/System/Library/PrivateFrameworks/SetupKitUI.framework/Versions/A/SetupKitUI](DYLIBS/SetupKitUI.md)
- [/System/Library/PrivateFrameworks/ShaderGraph.framework/Versions/A/ShaderGraph](DYLIBS/ShaderGraph.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/Versions/A/Sharing](DYLIBS/Sharing.md)
- [/System/Library/PrivateFrameworks/SharingUI.framework/Versions/A/SharingUI](DYLIBS/SharingUI.md)
- [/System/Library/PrivateFrameworks/ShazamCore.framework/Versions/A/ShazamCore](DYLIBS/ShazamCore.md)
- [/System/Library/PrivateFrameworks/ShazamEvents.framework/Versions/A/ShazamEvents](DYLIBS/ShazamEvents.md)
- [/System/Library/PrivateFrameworks/ShazamKitUI.framework/Versions/A/ShazamKitUI](DYLIBS/ShazamKitUI.md)
- [/System/Library/PrivateFrameworks/ShimGameServices.framework/Versions/A/ShimGameServices](DYLIBS/ShimGameServices.md)
- [/System/Library/PrivateFrameworks/SignpostSupport.framework/Versions/A/SignpostSupport](DYLIBS/SignpostSupport.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/Versions/A/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/Versions/A/SiriAppLaunchIntents](DYLIBS/SiriAppLaunchIntents.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchUIFramework.framework/Versions/A/SiriAppLaunchUIFramework](DYLIBS/SiriAppLaunchUIFramework.md)
- [/System/Library/PrivateFrameworks/SiriAppResolution.framework/Versions/A/SiriAppResolution](DYLIBS/SiriAppResolution.md)
- [/System/Library/PrivateFrameworks/SiriAudioIntentUtils.framework/Versions/A/SiriAudioIntentUtils](DYLIBS/SiriAudioIntentUtils.md)
- [/System/Library/PrivateFrameworks/SiriAudioSupport.framework/Versions/A/SiriAudioSupport](DYLIBS/SiriAudioSupport.md)
- [/System/Library/PrivateFrameworks/SiriAutoComplete.framework/Versions/A/SiriAutoComplete](DYLIBS/SiriAutoComplete.md)
- [/System/Library/PrivateFrameworks/SiriAutoCompleteAPI.framework/Versions/A/SiriAutoCompleteAPI](DYLIBS/SiriAutoCompleteAPI.md)
- [/System/Library/PrivateFrameworks/SiriCalendarIntents.framework/Versions/A/SiriCalendarIntents](DYLIBS/SiriCalendarIntents.md)
- [/System/Library/PrivateFrameworks/SiriCalendarUI.framework/Versions/A/SiriCalendarUI](DYLIBS/SiriCalendarUI.md)
- [/System/Library/PrivateFrameworks/SiriCam.framework/Versions/A/SiriCam](DYLIBS/SiriCam.md)
- [/System/Library/PrivateFrameworks/SiriContactsCommon.framework/Versions/A/SiriContactsCommon](DYLIBS/SiriContactsCommon.md)
- [/System/Library/PrivateFrameworks/SiriContactsIntents.framework/Versions/A/SiriContactsIntents](DYLIBS/SiriContactsIntents.md)
- [/System/Library/PrivateFrameworks/SiriContactsUI.framework/Versions/A/SiriContactsUI](DYLIBS/SiriContactsUI.md)
- [/System/Library/PrivateFrameworks/SiriCoreMetrics.framework/Versions/A/SiriCoreMetrics](DYLIBS/SiriCoreMetrics.md)
- [/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/Versions/A/SiriCrossDeviceArbitration](DYLIBS/SiriCrossDeviceArbitration.md)
- [/System/Library/PrivateFrameworks/SiriCrossDeviceArbitrationFeedback.framework/Versions/A/SiriCrossDeviceArbitrationFeedback](DYLIBS/SiriCrossDeviceArbitrationFeedback.md)
- [/System/Library/PrivateFrameworks/SiriDailyBriefingInternal.framework/Versions/A/SiriDailyBriefingInternal](DYLIBS/SiriDailyBriefingInternal.md)
- [/System/Library/PrivateFrameworks/SiriEntityMatcher.framework/Versions/A/SiriEntityMatcher](DYLIBS/SiriEntityMatcher.md)
- [/System/Library/PrivateFrameworks/SiriFindMy.framework/Versions/A/SiriFindMy](DYLIBS/SiriFindMy.md)
- [/System/Library/PrivateFrameworks/SiriGeo.framework/Versions/A/SiriGeo](DYLIBS/SiriGeo.md)
- [/System/Library/PrivateFrameworks/SiriGestureBridge.framework/Versions/A/SiriGestureBridge](DYLIBS/SiriGestureBridge.md)
- [/System/Library/PrivateFrameworks/SiriInCall.framework/Versions/A/SiriInCall](DYLIBS/SiriInCall.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/Versions/A/SiriInference](DYLIBS/SiriInference.md)
- [/System/Library/PrivateFrameworks/SiriInformationSearch.framework/Versions/A/SiriInformationSearch](DYLIBS/SiriInformationSearch.md)
- [/System/Library/PrivateFrameworks/SiriInformationTypes.framework/Versions/A/SiriInformationTypes](DYLIBS/SiriInformationTypes.md)
- [/System/Library/PrivateFrameworks/SiriInstrumentation.framework/Versions/A/SiriInstrumentation](DYLIBS/SiriInstrumentation.md)
- [/System/Library/PrivateFrameworks/SiriInteractive.framework/Versions/A/SiriInteractive](DYLIBS/SiriInteractive.md)
- [/System/Library/PrivateFrameworks/SiriKitFlow.framework/Versions/A/SiriKitFlow](DYLIBS/SiriKitFlow.md)
- [/System/Library/PrivateFrameworks/SiriKitRuntime.framework/Versions/A/SiriKitRuntime](DYLIBS/SiriKitRuntime.md)
- [/System/Library/PrivateFrameworks/SiriLiminal.framework/Versions/A/SiriLiminal](DYLIBS/SiriLiminal.md)
- [/System/Library/PrivateFrameworks/SiriMailInternal.framework/Versions/A/SiriMailInternal](DYLIBS/SiriMailInternal.md)
- [/System/Library/PrivateFrameworks/SiriMailUI.framework/Versions/A/SiriMailUI](DYLIBS/SiriMailUI.md)
- [/System/Library/PrivateFrameworks/SiriMailUIModel.framework/Versions/A/SiriMailUIModel](DYLIBS/SiriMailUIModel.md)
- [/System/Library/PrivateFrameworks/SiriMessageTypes.framework/Versions/A/SiriMessageTypes](DYLIBS/SiriMessageTypes.md)
- [/System/Library/PrivateFrameworks/SiriMessagesCommon.framework/Versions/A/SiriMessagesCommon](DYLIBS/SiriMessagesCommon.md)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/Versions/A/SiriMessagesFlow](DYLIBS/SiriMessagesFlow.md)
- [/System/Library/PrivateFrameworks/SiriMessagesUI.framework/Versions/A/SiriMessagesUI](DYLIBS/SiriMessagesUI.md)
- [/System/Library/PrivateFrameworks/SiriNLUOverrides.framework/Versions/A/SiriNLUOverrides](DYLIBS/SiriNLUOverrides.md)
- [/System/Library/PrivateFrameworks/SiriNLUTypes.framework/Versions/A/SiriNLUTypes](DYLIBS/SiriNLUTypes.md)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageGeneration.framework/Versions/A/SiriNaturalLanguageGeneration](DYLIBS/SiriNaturalLanguageGeneration.md)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageParsing.framework/Versions/A/SiriNaturalLanguageParsing](DYLIBS/SiriNaturalLanguageParsing.md)
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
- [/System/Library/PrivateFrameworks/SiriReferenceResolution.framework/Versions/A/SiriReferenceResolution](DYLIBS/SiriReferenceResolution.md)
- [/System/Library/PrivateFrameworks/SiriReferenceResolver.framework/Versions/A/SiriReferenceResolver](DYLIBS/SiriReferenceResolver.md)
- [/System/Library/PrivateFrameworks/SiriRemembers.framework/Versions/A/SiriRemembers](DYLIBS/SiriRemembers.md)
- [/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/Versions/A/SiriSettingsIntents](DYLIBS/SiriSettingsIntents.md)
- [/System/Library/PrivateFrameworks/SiriSetup.framework/Versions/A/SiriSetup](DYLIBS/SiriSetup.md)
- [/System/Library/PrivateFrameworks/SiriSharedUI.framework/Versions/A/SiriSharedUI](DYLIBS/SiriSharedUI.md)
- [/System/Library/PrivateFrameworks/SiriSignals.framework/Versions/A/SiriSignals](DYLIBS/SiriSignals.md)
- [/System/Library/PrivateFrameworks/SiriSuggestions.framework/Versions/A/SiriSuggestions](DYLIBS/SiriSuggestions.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/Versions/A/SiriSuggestionsAPI](DYLIBS/SiriSuggestionsAPI.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Versions/A/SiriSuggestionsBaseModel](DYLIBS/SiriSuggestionsBaseModel.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsIntelligence.framework/Versions/A/SiriSuggestionsIntelligence](DYLIBS/SiriSuggestionsIntelligence.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/Versions/A/SiriSuggestionsKit](DYLIBS/SiriSuggestionsKit.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/Versions/A/SiriSuggestionsSupport](DYLIBS/SiriSuggestionsSupport.md)
- [/System/Library/PrivateFrameworks/SiriTTS.framework/Versions/A/SiriTTS](DYLIBS/SiriTTS.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/Versions/A/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SiriTimeTimerInternal.framework/Versions/A/SiriTimeTimerInternal](DYLIBS/SiriTimeTimerInternal.md)
- [/System/Library/PrivateFrameworks/SiriTranslationIntents.framework/Versions/A/SiriTranslationIntents](DYLIBS/SiriTranslationIntents.md)
- [/System/Library/PrivateFrameworks/SiriTurnTakingManager.framework/Versions/A/SiriTurnTakingManager](DYLIBS/SiriTurnTakingManager.md)
- [/System/Library/PrivateFrameworks/SiriUI.framework/Versions/A/SiriUI](DYLIBS/SiriUI.md)
- [/System/Library/PrivateFrameworks/SiriUICore.framework/Versions/A/SiriUICore](DYLIBS/SiriUICore.md)
- [/System/Library/PrivateFrameworks/SiriUIFoundation.framework/Versions/A/SiriUIFoundation](DYLIBS/SiriUIFoundation.md)
- [/System/Library/PrivateFrameworks/SiriUserSegments.framework/Versions/A/SiriUserSegments](DYLIBS/SiriUserSegments.md)
- [/System/Library/PrivateFrameworks/SiriUtilities.framework/Versions/A/SiriUtilities](DYLIBS/SiriUtilities.md)
- [/System/Library/PrivateFrameworks/SiriVOX.framework/Versions/A/SiriVOX](DYLIBS/SiriVOX.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/Versions/A/SiriVideoIntents](DYLIBS/SiriVideoIntents.md)
- [/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/SkyLight](DYLIBS/SkyLight.md)
- [/System/Library/PrivateFrameworks/Sleep.framework/Versions/A/Sleep](DYLIBS/Sleep.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/Versions/A/SleepHealthUI](DYLIBS/SleepHealthUI.md)
- [/System/Library/PrivateFrameworks/SnippetKit.framework/Versions/A/SnippetKit](DYLIBS/SnippetKit.md)
- [/System/Library/PrivateFrameworks/SnippetUI.framework/Versions/A/SnippetUI](DYLIBS/SnippetUI.md)
- [/System/Library/PrivateFrameworks/SocialAppsCore.framework/Versions/A/SocialAppsCore](DYLIBS/SocialAppsCore.md)
- [/System/Library/PrivateFrameworks/SocialServices.framework/Versions/A/SocialServices](DYLIBS/SocialServices.md)
- [/System/Library/PrivateFrameworks/SocialUI.framework/Versions/A/SocialUI](DYLIBS/SocialUI.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateMacController.framework/Versions/A/SoftwareUpdateMacController](DYLIBS/SoftwareUpdateMacController.md)
- [/System/Library/PrivateFrameworks/SonicFoundation.framework/Versions/A/SonicFoundation](DYLIBS/SonicFoundation.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/Versions/A/SonicKit](DYLIBS/SonicKit.md)
- [/System/Library/PrivateFrameworks/SpaceAttribution.framework/Versions/A/SpaceAttribution](DYLIBS/SpaceAttribution.md)
- [/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/SpeakerRecognition](DYLIBS/SpeakerRecognition.md)
- [/System/Library/PrivateFrameworks/SpeechObjects.framework/Versions/A/SpeechObjects](DYLIBS/SpeechObjects.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionSharedSupport.framework/Versions/A/SpeechRecognitionSharedSupport](DYLIBS/SpeechRecognitionSharedSupport.md)
- [/System/Library/PrivateFrameworks/SportsKit.framework/Versions/A/SportsKit](DYLIBS/SportsKit.md)
- [/System/Library/PrivateFrameworks/Spotlight.framework/Versions/A/Spotlight](DYLIBS/Spotlight.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/Versions/A/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
- [/System/Library/PrivateFrameworks/SpotlightIndex.framework/Versions/A/SpotlightIndex](DYLIBS/SpotlightIndex.md)
- [/System/Library/PrivateFrameworks/SpotlightKnowledge.framework/Versions/A/SpotlightKnowledge](DYLIBS/SpotlightKnowledge.md)
- [/System/Library/PrivateFrameworks/SpotlightLinguistics.framework/Versions/A/SpotlightLinguistics](DYLIBS/SpotlightLinguistics.md)
- [/System/Library/PrivateFrameworks/SpotlightResources.framework/Versions/A/SpotlightResources](DYLIBS/SpotlightResources.md)
- [/System/Library/PrivateFrameworks/SpotlightServices.framework/Versions/A/SpotlightServices](DYLIBS/SpotlightServices.md)
- [/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/Versions/A/StatusKitAgentCore](DYLIBS/StatusKitAgentCore.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Versions/A/Stickers](DYLIBS/Stickers.md)
- [/System/Library/PrivateFrameworks/StocksCore.framework/Versions/A/StocksCore](DYLIBS/StocksCore.md)
- [/System/Library/PrivateFrameworks/StocksKit.framework/Versions/A/StocksKit](DYLIBS/StocksKit.md)
- [/System/Library/PrivateFrameworks/StoreFoundation.framework/Versions/A/StoreFoundation](DYLIBS/StoreFoundation.md)
- [/System/Library/PrivateFrameworks/SummarizationKit.framework/Versions/A/SummarizationKit](DYLIBS/SummarizationKit.md)
- [/System/Library/PrivateFrameworks/SwiftASN1.framework/Versions/A/SwiftASN1](DYLIBS/SwiftASN1.md)
- [/System/Library/PrivateFrameworks/SwiftNN.framework/Versions/A/SwiftNN](DYLIBS/SwiftNN.md)
- [/System/Library/PrivateFrameworks/SwiftSQLite.framework/Versions/A/SwiftSQLite](DYLIBS/SwiftSQLite.md)
- [/System/Library/PrivateFrameworks/Symbolication.framework/Versions/A/Symbolication](DYLIBS/Symbolication.md)
- [/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/Versions/A/SymptomDiagnosticReporter](DYLIBS/SymptomDiagnosticReporter.md)
- [/System/Library/PrivateFrameworks/SyncedDefaults.framework/Versions/A/SyncedDefaults](DYLIBS/SyncedDefaults.md)
- [/System/Library/PrivateFrameworks/SyncedModels.framework/Versions/A/SyncedModels](DYLIBS/SyncedModels.md)
- [/System/Library/PrivateFrameworks/SystemAdministrationInterface.framework/Versions/A/SystemAdministrationInterface](DYLIBS/SystemAdministrationInterface.md)
- [/System/Library/PrivateFrameworks/SystemMigration.framework/Versions/A/SystemMigration](DYLIBS/SystemMigration.md)
- [/System/Library/PrivateFrameworks/SystemPolicy.framework/Versions/A/SystemPolicy](DYLIBS/SystemPolicy.md)
- [/System/Library/PrivateFrameworks/SystemStatus.framework/Versions/A/SystemStatus](DYLIBS/SystemStatus.md)
- [/System/Library/PrivateFrameworks/TVAppServices.framework/Versions/A/TVAppServices](DYLIBS/TVAppServices.md)
- [/System/Library/PrivateFrameworks/TVIdleServices.framework/Versions/A/TVIdleServices](DYLIBS/TVIdleServices.md)
- [/System/Library/PrivateFrameworks/TVPlayback.framework/Versions/A/TVPlayback](DYLIBS/TVPlayback.md)
- [/System/Library/PrivateFrameworks/TVRemoteCore.framework/Versions/A/TVRemoteCore](DYLIBS/TVRemoteCore.md)
- [/System/Library/PrivateFrameworks/Tabi.framework/Versions/A/Tabi](DYLIBS/Tabi.md)
- [/System/Library/PrivateFrameworks/TeaDB.framework/Versions/A/TeaDB](DYLIBS/TeaDB.md)
- [/System/Library/PrivateFrameworks/TeaFoundation.framework/Versions/A/TeaFoundation](DYLIBS/TeaFoundation.md)
- [/System/Library/PrivateFrameworks/TeaSettings.framework/Versions/A/TeaSettings](DYLIBS/TeaSettings.md)
- [/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/Versions/A/TelephonyBlastDoorSupport](DYLIBS/TelephonyBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/Versions/A/TelephonyUtilities](DYLIBS/TelephonyUtilities.md)
- [/System/Library/PrivateFrameworks/TextComposer.framework/Versions/A/TextComposer](DYLIBS/TextComposer.md)
- [/System/Library/PrivateFrameworks/TextGenerationInference.framework/Versions/A/TextGenerationInference](DYLIBS/TextGenerationInference.md)
- [/System/Library/PrivateFrameworks/TextInput.framework/Versions/A/TextInput](DYLIBS/TextInput.md)
- [/System/Library/PrivateFrameworks/TextInputCore.framework/Versions/A/TextInputCore](DYLIBS/TextInputCore.md)
- [/System/Library/PrivateFrameworks/TextInputTestingKit.framework/Versions/A/TextInputTestingKit](DYLIBS/TextInputTestingKit.md)
- [/System/Library/PrivateFrameworks/TextRecognition.framework/Versions/A/TextRecognition](DYLIBS/TextRecognition.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/Versions/A/TextToSpeech](DYLIBS/TextToSpeech.md)
- [/System/Library/PrivateFrameworks/TextToSpeechBundleSupport.framework/Versions/A/TextToSpeechBundleSupport](DYLIBS/TextToSpeechBundleSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/Versions/A/TextToSpeechMauiSupport](DYLIBS/TextToSpeechMauiSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/Versions/A/TextToSpeechVoiceBankingSupport](DYLIBS/TextToSpeechVoiceBankingSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingUI.framework/Versions/A/TextToSpeechVoiceBankingUI](DYLIBS/TextToSpeechVoiceBankingUI.md)
- [/System/Library/PrivateFrameworks/TextUnderstandingShared.framework/Versions/A/TextUnderstandingShared](DYLIBS/TextUnderstandingShared.md)
- [/System/Library/PrivateFrameworks/TimeMachine.framework/Versions/A/TimeMachine](DYLIBS/TimeMachine.md)
- [/System/Library/PrivateFrameworks/TimeMachinePrivate.framework/Versions/A/TimeMachinePrivate](DYLIBS/TimeMachinePrivate.md)
- [/System/Library/PrivateFrameworks/TipKitCore.framework/Versions/A/TipKitCore](DYLIBS/TipKitCore.md)
- [/System/Library/PrivateFrameworks/TipKitServices.framework/Versions/A/TipKitServices](DYLIBS/TipKitServices.md)
- [/System/Library/PrivateFrameworks/TipsCore.framework/Versions/A/TipsCore](DYLIBS/TipsCore.md)
- [/System/Library/PrivateFrameworks/TipsDaemon.framework/Versions/A/TipsDaemon](DYLIBS/TipsDaemon.md)
- [/System/Library/PrivateFrameworks/TipsUI.framework/Versions/A/TipsUI](DYLIBS/TipsUI.md)
- [/System/Library/PrivateFrameworks/TokenGeneration.framework/Versions/A/TokenGeneration](DYLIBS/TokenGeneration.md)
- [/System/Library/PrivateFrameworks/TokenGenerationCore.framework/Versions/A/TokenGenerationCore](DYLIBS/TokenGenerationCore.md)
- [/System/Library/PrivateFrameworks/TokenGenerationInference.framework/Versions/A/TokenGenerationInference](DYLIBS/TokenGenerationInference.md)
- [/System/Library/PrivateFrameworks/ToolKit.framework/Versions/A/ToolKit](DYLIBS/ToolKit.md)
- [/System/Library/PrivateFrameworks/TranslationDaemon.framework/Versions/A/TranslationDaemon](DYLIBS/TranslationDaemon.md)
- [/System/Library/PrivateFrameworks/TranslationUI.framework/Versions/A/TranslationUI](DYLIBS/TranslationUI.md)
- [/System/Library/PrivateFrameworks/Transparency.framework/Versions/A/Transparency](DYLIBS/Transparency.md)
- [/System/Library/PrivateFrameworks/Trial.framework/Versions/A/Trial](DYLIBS/Trial.md)
- [/System/Library/PrivateFrameworks/TrialProto.framework/Versions/A/TrialProto](DYLIBS/TrialProto.md)
- [/System/Library/PrivateFrameworks/TrialServer.framework/Versions/A/TrialServer](DYLIBS/TrialServer.md)
- [/System/Library/PrivateFrameworks/Tungsten.framework/Versions/A/Tungsten](DYLIBS/Tungsten.md)
- [/System/Library/PrivateFrameworks/TuriCore.framework/Versions/A/TuriCore](DYLIBS/TuriCore.md)
- [/System/Library/PrivateFrameworks/TypistFramework.framework/Versions/A/TypistFramework](DYLIBS/TypistFramework.md)
- [/System/Library/PrivateFrameworks/UARPiCloud.framework/Versions/A/UARPiCloud](DYLIBS/UARPiCloud.md)
- [/System/Library/PrivateFrameworks/UIAccessibility.framework/Versions/A/UIAccessibility](DYLIBS/UIAccessibility.md)
- [/System/Library/PrivateFrameworks/UIFoundation.framework/Versions/A/UIFoundation](DYLIBS/UIFoundation.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceIntents.framework/Versions/A/UIIntelligenceIntents](DYLIBS/UIIntelligenceIntents.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupport.framework/Versions/A/UIIntelligenceSupport](DYLIBS/UIIntelligenceSupport.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupportAgent.framework/Versions/A/UIIntelligenceSupportAgent](DYLIBS/UIIntelligenceSupportAgent.md)
- [/System/Library/PrivateFrameworks/UIKitMacHelper.framework/Versions/A/UIKitMacHelper](DYLIBS/UIKitMacHelper.md)
- [/System/Library/PrivateFrameworks/UIKitServices.framework/Versions/A/UIKitServices](DYLIBS/UIKitServices.md)
- [/System/Library/PrivateFrameworks/UIUnderstanding.framework/Versions/A/UIUnderstanding](DYLIBS/UIUnderstanding.md)
- [/System/Library/PrivateFrameworks/UXKit.framework/Versions/A/UXKit](DYLIBS/UXKit.md)
- [/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/Versions/A/UnifiedAssetFramework](DYLIBS/UnifiedAssetFramework.md)
- [/System/Library/PrivateFrameworks/UniversalAccess.framework/Versions/A/Frameworks/UniversalAccessCore.framework/Versions/A/UniversalAccessCore](DYLIBS/UniversalAccessCore.md)
- [/System/Library/PrivateFrameworks/UniversalControl.framework/Versions/A/UniversalControl](DYLIBS/UniversalControl.md)
- [/System/Library/PrivateFrameworks/UniversalDrag.framework/Versions/A/UniversalDrag](DYLIBS/UniversalDrag.md)
- [/System/Library/PrivateFrameworks/UniversalHID.framework/Versions/A/UniversalHID](DYLIBS/UniversalHID.md)
- [/System/Library/PrivateFrameworks/UniversalHIDKit.framework/Versions/A/UniversalHIDKit](DYLIBS/UniversalHIDKit.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/Versions/A/UsageTracking](DYLIBS/UsageTracking.md)
- [/System/Library/PrivateFrameworks/UserActivity.framework/Versions/A/UserActivity](DYLIBS/UserActivity.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Versions/A/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsKit.framework/Versions/A/UserNotificationsKit](DYLIBS/UserNotificationsKit.md)
- [/System/Library/PrivateFrameworks/UserNotificationsServices.framework/Versions/A/UserNotificationsServices](DYLIBS/UserNotificationsServices.md)
- [/System/Library/PrivateFrameworks/VDAF.framework/Versions/A/VDAF](DYLIBS/VDAF.md)
- [/System/Library/PrivateFrameworks/VFX.framework/Versions/A/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/Versions/A/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/PrivateFrameworks/VectorSearch.framework/Versions/A/VectorSearch](DYLIBS/VectorSearch.md)
- [/System/Library/PrivateFrameworks/VideoProcessing.framework/Versions/A/VideoProcessing](DYLIBS/VideoProcessing.md)
- [/System/Library/PrivateFrameworks/VideoSubscriberAccountUI.framework/Versions/A/VideoSubscriberAccountUI](DYLIBS/VideoSubscriberAccountUI.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/Versions/A/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VideosUICore.framework/Versions/A/VideosUICore](DYLIBS/VideosUICore.md)
- [/System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge](DYLIBS/ViewBridge.md)
- [/System/Library/PrivateFrameworks/VirtualGarage.framework/Versions/A/VirtualGarage](DYLIBS/VirtualGarage.md)
- [/System/Library/PrivateFrameworks/VisionCore.framework/Versions/A/VisionCore](DYLIBS/VisionCore.md)
- [/System/Library/PrivateFrameworks/VisionKitCore.framework/Versions/A/VisionKitCore](DYLIBS/VisionKitCore.md)
- [/System/Library/PrivateFrameworks/VisualGeneration.framework/Versions/A/VisualGeneration](DYLIBS/VisualGeneration.md)
- [/System/Library/PrivateFrameworks/VisualIntelligence.framework/Versions/A/VisualIntelligence](DYLIBS/VisualIntelligence.md)
- [/System/Library/PrivateFrameworks/VisualUnderstanding.framework/Versions/A/VisualUnderstanding](DYLIBS/VisualUnderstanding.md)
- [/System/Library/PrivateFrameworks/VoiceActions.framework/Versions/A/VoiceActions](DYLIBS/VoiceActions.md)
- [/System/Library/PrivateFrameworks/VoiceControlUI.framework/Versions/A/VoiceControlUI](DYLIBS/VoiceControlUI.md)
- [/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/Versions/A/VoiceShortcutClient](DYLIBS/VoiceShortcutClient.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Versions/A/VoiceShortcuts](DYLIBS/VoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/Versions/A/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/Wallpaper.framework/Versions/A/Wallpaper](DYLIBS/Wallpaper.md)
- [/System/Library/PrivateFrameworks/WallpaperExtensionKit.framework/Versions/A/WallpaperExtensionKit](DYLIBS/WallpaperExtensionKit.md)
- [/System/Library/PrivateFrameworks/WallpaperFoundation.framework/Versions/A/WallpaperFoundation](DYLIBS/WallpaperFoundation.md)
- [/System/Library/PrivateFrameworks/WatchListKit.framework/Versions/A/WatchListKit](DYLIBS/WatchListKit.md)
- [/System/Library/PrivateFrameworks/WeatherAnalytics.framework/Versions/A/WeatherAnalytics](DYLIBS/WeatherAnalytics.md)
- [/System/Library/PrivateFrameworks/WeatherCore.framework/Versions/A/WeatherCore](DYLIBS/WeatherCore.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/Versions/A/WeatherDaemon](DYLIBS/WeatherDaemon.md)
- [/System/Library/PrivateFrameworks/WebBookmarks.framework/Versions/A/WebBookmarks](DYLIBS/WebBookmarks.md)
- [/System/Library/PrivateFrameworks/WebBookmarksSwift.framework/Versions/A/WebBookmarksSwift](DYLIBS/WebBookmarksSwift.md)
- [/System/Library/PrivateFrameworks/WebDriver.framework/Versions/A/WebDriver](DYLIBS/WebDriver.md)
- [/System/Library/PrivateFrameworks/WebGPU.framework/Versions/A/WebGPU](DYLIBS/WebGPU.md)
- [/System/Library/PrivateFrameworks/WebInspector.framework/Versions/A/WebInspector](DYLIBS/WebInspector.md)
- [/System/Library/PrivateFrameworks/WellnessUI.framework/Versions/A/WellnessUI](DYLIBS/WellnessUI.md)
- [/System/Library/PrivateFrameworks/WiFiAnalytics.framework/Versions/A/WiFiAnalytics](DYLIBS/WiFiAnalytics.md)
- [/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/Versions/A/WiFiPeerToPeer](DYLIBS/WiFiPeerToPeer.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/Versions/A/WiFiPolicy](DYLIBS/WiFiPolicy.md)
- [/System/Library/PrivateFrameworks/WiFiSettingsKit.framework/Versions/A/WiFiSettingsKit](DYLIBS/WiFiSettingsKit.md)
- [/System/Library/PrivateFrameworks/WiFiVelocity.framework/Versions/A/WiFiVelocity](DYLIBS/WiFiVelocity.md)
- [/System/Library/PrivateFrameworks/WidgetObservation.framework/Versions/A/WidgetObservation](DYLIBS/WidgetObservation.md)
- [/System/Library/PrivateFrameworks/WidgetRenderer.framework/Versions/A/WidgetRenderer](DYLIBS/WidgetRenderer.md)
- [/System/Library/PrivateFrameworks/WindowManager.framework/Versions/A/WindowManager](DYLIBS/WindowManager.md)
- [/System/Library/PrivateFrameworks/WorkflowEditor.framework/Versions/A/WorkflowEditor](DYLIBS/WorkflowEditor.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/Versions/A/WorkflowKit](DYLIBS/WorkflowKit.md)
- [/System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/Versions/A/WorkflowResponsiveness](DYLIBS/WorkflowResponsiveness.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/Versions/A/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/PrivateFrameworks/WorkflowUICore.framework/Versions/A/WorkflowUICore](DYLIBS/WorkflowUICore.md)
- [/System/Library/PrivateFrameworks/WorkflowUIServices.framework/Versions/A/WorkflowUIServices](DYLIBS/WorkflowUIServices.md)
- [/System/Library/PrivateFrameworks/WritingToolsUI.framework/Versions/A/WritingToolsUI](DYLIBS/WritingToolsUI.md)
- [/System/Library/PrivateFrameworks/XCTAutomationSupport.framework/Versions/A/XCTAutomationSupport](DYLIBS/XCTAutomationSupport.md)
- [/System/Library/PrivateFrameworks/XOJIT.framework/Versions/A/XOJIT](DYLIBS/XOJIT.md)
- [/System/Library/PrivateFrameworks/ZeoliteFramework.framework/Versions/A/ZeoliteFramework](DYLIBS/ZeoliteFramework.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/Versions/A/ZhuGeSupport](DYLIBS/ZhuGeSupport.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/Versions/A/libZhuGeArmory.dylib](DYLIBS/libZhuGeArmory.dylib.md)
- [/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/Versions/A/_JetEngine_SwiftUI](DYLIBS/_JetEngine_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_JetUI_SwiftUI.framework/Versions/A/_JetUI_SwiftUI](DYLIBS/_JetUI_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/Versions/A/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_SonicKit_MusicKit.framework/Versions/A/_SonicKit_MusicKit](DYLIBS/_SonicKit_MusicKit.md)
- [/System/Library/PrivateFrameworks/caulk.framework/Versions/A/caulk](DYLIBS/caulk.md)
- [/System/Library/PrivateFrameworks/iCloudDriveCore.framework/Versions/A/iCloudDriveCore](DYLIBS/iCloudDriveCore.md)
- [/System/Library/PrivateFrameworks/iCloudQuota.framework/Versions/A/iCloudQuota](DYLIBS/iCloudQuota.md)
- [/System/Library/PrivateFrameworks/iCloudSettings.framework/Versions/A/iCloudSettings](DYLIBS/iCloudSettings.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/Versions/A/iTunesCloud](DYLIBS/iTunesCloud.md)
- [/System/Library/PrivateFrameworks/icloudMCCKit.framework/Versions/A/icloudMCCKit](DYLIBS/icloudMCCKit.md)
- [/System/Library/PrivateFrameworks/ktrace.framework/Versions/A/ktrace](DYLIBS/ktrace.md)
- [/System/Library/PrivateFrameworks/lighthouse_runtime.framework/Versions/A/lighthouse_runtime](DYLIBS/lighthouse_runtime.md)
- [/System/Library/QuickLook/iWork.qlgenerator/Contents/Frameworks/TSUtility.framework/Versions/A/TSUtility](DYLIBS/TSUtility.md)
- [/System/Library/Spotlight/iWork.mdimporter/Contents/Frameworks/TSUtility.framework/Versions/A/TSUtility](DYLIBS/TSUtility.md)
- [/System/Library/TextInput/TextInput_zh.bundle/Versions/A/TextInput_zh](DYLIBS/TextInput_zh.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/AccessibilitySettingsLoader.bundle/Versions/A/AccessibilitySettingsLoader](DYLIBS/AccessibilitySettingsLoader.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/AvatarUI.axbundle/Contents/MacOS/AvatarUI](DYLIBS/AvatarUI.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/ChatKitFramework.axbundle/Contents/MacOS/ChatKitFramework](DYLIBS/ChatKitFramework.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/Clock.axbundle/Contents/MacOS/Clock](DYLIBS/Clock.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/ContactsUI.axbundle/Contents/MacOS/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/ControlCenterUI.axbundle/Contents/MacOS/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/ControlCenterUIKit.axbundle/Contents/MacOS/ControlCenterUIKit](DYLIBS/ControlCenterUIKit.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/ConversationKit.axbundle/Contents/MacOS/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/EventKitUIFramework.axbundle/Contents/MacOS/EventKitUIFramework](DYLIBS/EventKitUIFramework.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/HomeUI.axbundle/Contents/MacOS/HomeUI](DYLIBS/HomeUI.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/HomeUIService.axbundle/Contents/MacOS/HomeUIService](DYLIBS/HomeUIService.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/MapKitFramework.axbundle/Contents/MacOS/MapKitFramework](DYLIBS/MapKitFramework.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/Maps.axbundle/Contents/MacOS/Maps](DYLIBS/Maps.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/MessageUIFramework.axbundle/Versions/A/MessageUIFramework](DYLIBS/MessageUIFramework.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/MobileSafariUI.axbundle/Contents/MacOS/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/PencilKit.axbundle/Contents/MacOS/PencilKit](DYLIBS/PencilKit.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/PhotosUIFramework.axbundle/Versions/A/PhotosUIFramework](DYLIBS/PhotosUIFramework.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/Podcasts.axbundle/Contents/MacOS/Podcasts](DYLIBS/Podcasts.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/TelephonyUIFramework.axbundle/Contents/MacOS/TelephonyUIFramework](DYLIBS/TelephonyUIFramework.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/UIKit.axbundle/Contents/MacOS/UIKit](DYLIBS/UIKit.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/VectorKit.axbundle/Contents/MacOS/VectorKit](DYLIBS/VectorKit.md)
- [/System/iOSSupport/System/Library/AccessibilityBundles/WebCore.axbundle/Versions/A/WebCore](DYLIBS/WebCore.md)
- [/System/iOSSupport/System/Library/Frameworks/AVKit.framework/Versions/A/AVKit](DYLIBS/AVKit.md)
- [/System/iOSSupport/System/Library/Frameworks/AdAttributionKit.framework/Versions/A/AdAttributionKit](DYLIBS/AdAttributionKit.md)
- [/System/iOSSupport/System/Library/Frameworks/Assignables.framework/Versions/A/Assignables](DYLIBS/Assignables.md)
- [/System/iOSSupport/System/Library/Frameworks/AuthenticationServices.framework/Versions/A/AuthenticationServices](DYLIBS/AuthenticationServices.md)
- [/System/iOSSupport/System/Library/Frameworks/Charts.framework/Versions/A/Charts](DYLIBS/Charts.md)
- [/System/iOSSupport/System/Library/Frameworks/ClockKit.framework/Versions/A/ClockKit](DYLIBS/ClockKit.md)
- [/System/iOSSupport/System/Library/Frameworks/ContactsUI.framework/Versions/A/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/iOSSupport/System/Library/Frameworks/CoreAudioKit.framework/Versions/A/CoreAudioKit](DYLIBS/CoreAudioKit.md)
- [/System/iOSSupport/System/Library/Frameworks/CoreLocationUI.framework/Versions/A/CoreLocationUI](DYLIBS/CoreLocationUI.md)
- [/System/iOSSupport/System/Library/Frameworks/EventKitUI.framework/Versions/A/EventKitUI](DYLIBS/EventKitUI.md)
- [/System/iOSSupport/System/Library/Frameworks/ExtensionKit.framework/Versions/A/ExtensionKit](DYLIBS/ExtensionKit.md)
- [/System/iOSSupport/System/Library/Frameworks/GameController.framework/Versions/A/GameController](DYLIBS/GameController.md)
- [/System/iOSSupport/System/Library/Frameworks/GameKit.framework/Versions/A/GameKit](DYLIBS/GameKit.md)
- [/System/iOSSupport/System/Library/Frameworks/HomeKit.framework/Versions/A/HomeKit](DYLIBS/HomeKit.md)
- [/System/iOSSupport/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/iOSSupport/System/Library/Frameworks/LinkPresentation.framework/Versions/A/LinkPresentation](DYLIBS/LinkPresentation.md)
- [/System/iOSSupport/System/Library/Frameworks/MapKit.framework/Versions/A/MapKit](DYLIBS/MapKit.md)
- [/System/iOSSupport/System/Library/Frameworks/MediaPlayer.framework/Versions/A/MediaPlayer](DYLIBS/MediaPlayer.md)
- [/System/iOSSupport/System/Library/Frameworks/MessageUI.framework/Versions/A/MessageUI](DYLIBS/MessageUI.md)
- [/System/iOSSupport/System/Library/Frameworks/MetalKit.framework/Versions/A/MetalKit](DYLIBS/MetalKit.md)
- [/System/iOSSupport/System/Library/Frameworks/PDFKit.framework/Versions/A/PDFKit](DYLIBS/PDFKit.md)
- [/System/iOSSupport/System/Library/Frameworks/PencilKit.framework/Versions/A/PencilKit](DYLIBS/PencilKit.md)
- [/System/iOSSupport/System/Library/Frameworks/ProximityReader.framework/Versions/A/ProximityReader](DYLIBS/ProximityReader.md)
- [/System/iOSSupport/System/Library/Frameworks/QuickLook.framework/Versions/A/QuickLook](DYLIBS/QuickLook.md)
- [/System/iOSSupport/System/Library/Frameworks/RealityFoundation.framework/Versions/A/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/iOSSupport/System/Library/Frameworks/RealityKit.framework/Versions/A/RealityKit](DYLIBS/RealityKit.md)
- [/System/iOSSupport/System/Library/Frameworks/RoomPlan.framework/Versions/A/RoomPlan](DYLIBS/RoomPlan.md)
- [/System/iOSSupport/System/Library/Frameworks/SafariServices.framework/Versions/A/SafariServices](DYLIBS/SafariServices.md)
- [/System/iOSSupport/System/Library/Frameworks/Social.framework/Versions/A/Social](DYLIBS/Social.md)
- [/System/iOSSupport/System/Library/Frameworks/StoreKit.framework/Versions/A/StoreKit](DYLIBS/StoreKit.md)
- [/System/iOSSupport/System/Library/Frameworks/SwiftUI.framework/Versions/A/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/iOSSupport/System/Library/Frameworks/TipKit.framework/Versions/A/TipKit](DYLIBS/TipKit.md)
- [/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/WebKit](DYLIBS/WebKit.md)
- [/System/iOSSupport/System/Library/Frameworks/WidgetKit.framework/Versions/A/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/iOSSupport/System/Library/Frameworks/_AVKit_SwiftUI.framework/Versions/A/_AVKit_SwiftUI](DYLIBS/_AVKit_SwiftUI.md)
- [/System/iOSSupport/System/Library/Frameworks/_AdAttributionKit_StoreKit.framework/Versions/A/_AdAttributionKit_StoreKit](DYLIBS/_AdAttributionKit_StoreKit.md)
- [/System/iOSSupport/System/Library/Frameworks/_AuthenticationServices_SwiftUI.framework/Versions/A/_AuthenticationServices_SwiftUI](DYLIBS/_AuthenticationServices_SwiftUI.md)
- [/System/iOSSupport/System/Library/Frameworks/_CoreNFC_UIKit.framework/Versions/A/_CoreNFC_UIKit](DYLIBS/_CoreNFC_UIKit.md)
- [/System/iOSSupport/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/Versions/A/_DeviceActivity_SwiftUI](DYLIBS/_DeviceActivity_SwiftUI.md)
- [/System/iOSSupport/System/Library/Frameworks/_GroupActivities_UIKit.framework/Versions/A/_GroupActivities_UIKit](DYLIBS/_GroupActivities_UIKit.md)
- [/System/iOSSupport/System/Library/Frameworks/_MapKit_SwiftUI.framework/Versions/A/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/iOSSupport/System/Library/Frameworks/_PassKit_SwiftUI.framework/Versions/A/_PassKit_SwiftUI](DYLIBS/_PassKit_SwiftUI.md)
- [/System/iOSSupport/System/Library/Frameworks/_PhotosUI_SwiftUI.framework/Versions/A/_PhotosUI_SwiftUI](DYLIBS/_PhotosUI_SwiftUI.md)
- [/System/iOSSupport/System/Library/Frameworks/_QuickLook_SwiftUI.framework/Versions/A/_QuickLook_SwiftUI](DYLIBS/_QuickLook_SwiftUI.md)
- [/System/iOSSupport/System/Library/Frameworks/_RealityKit_SwiftUI.framework/Versions/A/_RealityKit_SwiftUI](DYLIBS/_RealityKit_SwiftUI.md)
- [/System/iOSSupport/System/Library/Frameworks/_SpriteKit_SwiftUI.framework/Versions/A/_SpriteKit_SwiftUI](DYLIBS/_SpriteKit_SwiftUI.md)
- [/System/iOSSupport/System/Library/Frameworks/_StoreKit_SwiftUI.framework/Versions/A/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI.md)
- [/System/iOSSupport/System/Library/Frameworks/_SwiftData_SwiftUI.framework/Versions/A/_SwiftData_SwiftUI](DYLIBS/_SwiftData_SwiftUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/AccessibilityUIService.framework/Versions/A/AccessibilityUIService](DYLIBS/AccessibilityUIService.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/Versions/A/AccessibilityUIUtilities](DYLIBS/AccessibilityUIUtilities.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ActionKit.framework/Versions/A/ActionKit](DYLIBS/ActionKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ActionKitUI.framework/Versions/A/ActionKitUI](DYLIBS/ActionKitUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ActivityRingsUI.framework/Versions/A/ActivityRingsUI](DYLIBS/ActivityRingsUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/AnnotationKit.framework/Versions/A/AnnotationKit](DYLIBS/AnnotationKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/AppStoreComponents.framework/Versions/A/AppStoreComponents](DYLIBS/AppStoreComponents.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Versions/A/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/Versions/A/AppleMediaServicesUIDynamic](DYLIBS/AppleMediaServicesUIDynamic.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/BaseBoardUI.framework/Versions/A/BaseBoardUI](DYLIBS/BaseBoardUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/BatteryCenterUI.framework/Versions/A/BatteryCenterUI](DYLIBS/BatteryCenterUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/BusinessServicesUI.framework/Versions/A/BusinessServicesUI](DYLIBS/BusinessServicesUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/CalculateUI.framework/Versions/A/CalculateUI](DYLIBS/CalculateUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/CalendarUIKit.framework/Versions/A/CalendarUIKit](DYLIBS/CalendarUIKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ChatKit.framework/Versions/A/ChatKit](DYLIBS/ChatKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ChronoKit.framework/Versions/A/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ChronoUIServices.framework/Versions/A/ChronoUIServices](DYLIBS/ChronoUIServices.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/CommunicationsUI.framework/Versions/A/CommunicationsUI](DYLIBS/CommunicationsUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ContactsAutocompleteUI.framework/Versions/A/ContactsAutocompleteUI](DYLIBS/ContactsAutocompleteUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ConversationKit.framework/Versions/A/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/CoreHapticsTools.framework/Versions/A/CoreHapticsTools](DYLIBS/CoreHapticsTools.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/DocumentManager.framework/Versions/A/DocumentManager](DYLIBS/DocumentManager.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/DocumentManagerCore.framework/Versions/A/DocumentManagerCore](DYLIBS/DocumentManagerCore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/EnergyKit.framework/Versions/A/EnergyKit](DYLIBS/EnergyKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/EnergyKitFoundation.framework/Versions/A/EnergyKitFoundation](DYLIBS/EnergyKitFoundation.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/Versions/A/FaceTimeMessageStore](DYLIBS/FaceTimeMessageStore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/FaceTimeNotificationUI.framework/Versions/A/FaceTimeNotificationUI](DYLIBS/FaceTimeNotificationUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/FindMyUICore.framework/Versions/A/FindMyUICore](DYLIBS/FindMyUICore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/GameCenterUI.framework/Versions/A/GameCenterUI](DYLIBS/GameCenterUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/GenerativePlaygroundUI.framework/Versions/A/GenerativePlaygroundUI](DYLIBS/GenerativePlaygroundUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/Home.framework/Versions/A/Home](DYLIBS/Home.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/Versions/A/HomeAccessoryControlUI](DYLIBS/HomeAccessoryControlUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/HomeDataModel.framework/Versions/A/HomeDataModel](DYLIBS/HomeDataModel.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/Versions/A/HomeEnergyDaemon](DYLIBS/HomeEnergyDaemon.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/HomeEnergyUI.framework/Versions/A/HomeEnergyUI](DYLIBS/HomeEnergyUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/HomeServices.framework/Versions/A/HomeServices](DYLIBS/HomeServices.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/HomeUI.framework/Versions/A/HomeUI](DYLIBS/HomeUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/HomeUI2.framework/Versions/A/HomeUI2](DYLIBS/HomeUI2.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/HomeUICommon.framework/Versions/A/HomeUICommon](DYLIBS/HomeUICommon.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/HomeUtilityServices.framework/Versions/A/HomeUtilityServices](DYLIBS/HomeUtilityServices.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/IMAssistantCore.framework/Versions/A/IMAssistantCore](DYLIBS/IMAssistantCore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/IMCore.framework/Versions/A/IMCore](DYLIBS/IMCore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/IMDPersistence.framework/Versions/A/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/IMSharedUtilities.framework/Versions/A/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/IMTranscoderAgent.framework/Versions/A/IMTranscoderAgent](DYLIBS/IMTranscoderAgent.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/IntlPreferences.framework/Versions/A/IntlPreferences](DYLIBS/IntlPreferences.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/JITAppKit.framework/Versions/A/JITAppKit](DYLIBS/JITAppKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/JetEngine.framework/Versions/A/JetEngine](DYLIBS/JetEngine.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/JetUI.framework/Versions/A/JetUI](DYLIBS/JetUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/Versions/A/LocalAuthenticationCoreUI](DYLIBS/LocalAuthenticationCoreUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ManagedConfiguration.framework/Versions/A/ManagedConfiguration](DYLIBS/ManagedConfiguration.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/MapsUI.framework/Versions/A/MapsUI](DYLIBS/MapsUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/MediaCoreUI.framework/Versions/A/MediaCoreUI](DYLIBS/MediaCoreUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/Versions/A/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/NewsAds.framework/Versions/A/NewsAds](DYLIBS/NewsAds.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/NewsAnalytics.framework/Versions/A/NewsAnalytics](DYLIBS/NewsAnalytics.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/NewsArticles.framework/Versions/A/NewsArticles](DYLIBS/NewsArticles.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/NewsEngagement.framework/Versions/A/NewsEngagement](DYLIBS/NewsEngagement.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/NewsFeed.framework/Versions/A/NewsFeed](DYLIBS/NewsFeed.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/NewsLiveActivitiesCore.framework/Versions/A/NewsLiveActivitiesCore](DYLIBS/NewsLiveActivitiesCore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/NewsPersonalization.framework/Versions/A/NewsPersonalization](DYLIBS/NewsPersonalization.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/NewsServicesInternal.framework/Versions/A/NewsServicesInternal](DYLIBS/NewsServicesInternal.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/NewsSubscription.framework/Versions/A/NewsSubscription](DYLIBS/NewsSubscription.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/NewsUI.framework/Versions/A/NewsUI](DYLIBS/NewsUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/NewsUI2.framework/Versions/A/NewsUI2](DYLIBS/NewsUI2.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PaperKit.framework/Versions/A/PaperKit](DYLIBS/PaperKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PassKitUI.framework/Versions/A/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/Versions/A/PhotosSwiftUICore](DYLIBS/PhotosSwiftUICore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PhotosUICore.framework/Versions/A/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PhotosUIFoundation.framework/Versions/A/PhotosUIFoundation](DYLIBS/PhotosUIFoundation.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/Versions/A/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PodcastsUI.framework/Versions/A/PodcastsUI](DYLIBS/PodcastsUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PreviewShellKit.framework/Versions/A/PreviewShellKit](DYLIBS/PreviewShellKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PreviewsInjection.framework/Versions/A/PreviewsInjection](DYLIBS/PreviewsInjection.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PreviewsServicesUI.framework/Versions/A/PreviewsServicesUI](DYLIBS/PreviewsServicesUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PromotedContent.framework/Versions/A/PromotedContent](DYLIBS/PromotedContent.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/PromotedContentUI.framework/Versions/A/PromotedContentUI](DYLIBS/PromotedContentUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/RTTUI.framework/Versions/A/RTTUI](DYLIBS/RTTUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/SafariShared.framework/Versions/A/SafariShared](DYLIBS/SafariShared.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/SafariSharedUI.framework/Versions/A/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/Versions/A/SafetyMonitorUI](DYLIBS/SafetyMonitorUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ScreenTimeUI.framework/Versions/A/ScreenTimeUI](DYLIBS/ScreenTimeUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ShareSheet.framework/Versions/A/ShareSheet](DYLIBS/ShareSheet.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ShazamKitUI.framework/Versions/A/ShazamKitUI](DYLIBS/ShazamKitUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/Silex.framework/Versions/A/Silex](DYLIBS/Silex.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/SilexVideo.framework/Versions/A/SilexVideo](DYLIBS/SilexVideo.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/SocialLayer.framework/Versions/A/SocialLayer](DYLIBS/SocialLayer.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/StickersUI.framework/Versions/A/StickersUI](DYLIBS/StickersUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/StocksUI.framework/Versions/A/StocksUI](DYLIBS/StocksUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/TSReading.framework/Versions/A/TSReading](DYLIBS/TSReading.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/TeaCharts.framework/Versions/A/TeaCharts](DYLIBS/TeaCharts.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/TeaSnappy.framework/Versions/A/TeaSnappy](DYLIBS/TeaSnappy.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/TeaTemplate.framework/Versions/A/TeaTemplate](DYLIBS/TeaTemplate.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/TeaUI.framework/Versions/A/TeaUI](DYLIBS/TeaUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/TelephonyUI.framework/Versions/A/TelephonyUI](DYLIBS/TelephonyUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/TextInputUI.framework/Versions/A/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/TipsUI.framework/Versions/A/TipsUI](DYLIBS/TipsUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/TouchML.framework/Versions/A/TouchML](DYLIBS/TouchML.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/Tungsten.framework/Versions/A/Tungsten](DYLIBS/Tungsten.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/UIAccessibility.framework/Versions/A/UIAccessibility](DYLIBS/UIAccessibility.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/UIKitCore.framework/Versions/A/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/VFX.framework/Versions/A/VFX](DYLIBS/VFX.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/VisionKitCore.framework/Versions/A/VisionKitCore](DYLIBS/VisionKitCore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/VisionKitInternal.framework/Versions/A/VisionKitInternal](DYLIBS/VisionKitInternal.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/VoiceMemos.framework/Versions/A/VoiceMemos](DYLIBS/VoiceMemos.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/VoiceOverServices.framework/Versions/A/VoiceOverServices](DYLIBS/VoiceOverServices.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Versions/A/VoiceShortcuts](DYLIBS/VoiceShortcuts.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/WeatherAppSupport.framework/Versions/A/WeatherAppSupport](DYLIBS/WeatherAppSupport.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/WeatherMaps.framework/Versions/A/WeatherMaps](DYLIBS/WeatherMaps.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/WeatherUI.framework/Versions/A/WeatherUI](DYLIBS/WeatherUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/WebCore.framework/Versions/A/Frameworks/libANGLE-shared.dylib](DYLIBS/libANGLE-shared.dylib.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/WebCore.framework/Versions/A/WebCore](DYLIBS/WebCore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/WebGPU.framework/Versions/A/WebGPU](DYLIBS/WebGPU.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/WebKitLegacy.framework/Versions/A/WebKitLegacy](DYLIBS/WebKitLegacy.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/WorkflowEditor.framework/Versions/A/WorkflowEditor](DYLIBS/WorkflowEditor.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/WorkflowKit.framework/Versions/A/WorkflowKit](DYLIBS/WorkflowKit.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/WorkflowUI.framework/Versions/A/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/WorkflowUICore.framework/Versions/A/WorkflowUICore](DYLIBS/WorkflowUICore.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/WorkflowUIServices.framework/Versions/A/WorkflowUIServices](DYLIBS/WorkflowUIServices.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/ZoomServices.framework/Versions/A/ZoomServices](DYLIBS/ZoomServices.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/Versions/A/_JetEngine_SwiftUI](DYLIBS/_JetEngine_SwiftUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/_JetUI_SwiftUI.framework/Versions/A/_JetUI_SwiftUI](DYLIBS/_JetUI_SwiftUI.md)
- [/System/iOSSupport/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/Versions/A/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI.md)
- [/System/iOSSupport/usr/lib/swift/libswiftCarPlay.dylib](DYLIBS/libswiftCarPlay.dylib.md)
- [/System/iOSSupport/usr/lib/swift/libswiftGameplayKit.dylib](DYLIBS/libswiftGameplayKit.dylib.md)
- [/System/iOSSupport/usr/lib/swift/libswiftMapKit.dylib](DYLIBS/libswiftMapKit.dylib.md)
- [/System/iOSSupport/usr/lib/swift/libswiftMetalKit.dylib](DYLIBS/libswiftMetalKit.dylib.md)
- [/System/iOSSupport/usr/lib/swift/libswiftSafariServices.dylib](DYLIBS/libswiftSafariServices.dylib.md)
- [/System/iOSSupport/usr/lib/swift/libswiftSceneKit.dylib](DYLIBS/libswiftSceneKit.dylib.md)
- [/System/iOSSupport/usr/lib/swift/libswiftSpriteKit.dylib](DYLIBS/libswiftSpriteKit.dylib.md)
- [/System/iOSSupport/usr/lib/swift/libswiftWatchKit.dylib](DYLIBS/libswiftWatchKit.dylib.md)
- [/System/iOSSupport/usr/lib/swift/libswiftWebKit.dylib](DYLIBS/libswiftWebKit.dylib.md)
- [/System/iOSSupport/usr/lib/swift/~libswiftPencilKit.dylib](DYLIBS/~libswiftPencilKit.dylib.md)
- [/usr/lib/dyld](DYLIBS/dyld.md)
- [/usr/lib/libAccessibility.dylib](DYLIBS/libAccessibility.dylib.md)
- [/usr/lib/libAmber.dylib](DYLIBS/libAmber.dylib.md)
- [/usr/lib/libAppleEXR.dylib](DYLIBS/libAppleEXR.dylib.md)
- [/usr/lib/libAppletTranslationLibrary.dylib](DYLIBS/libAppletTranslationLibrary.dylib.md)
- [/usr/lib/libAudioDSPCore.dylib](DYLIBS/libAudioDSPCore.dylib.md)
- [/usr/lib/libEndpointSecuritySystem.dylib](DYLIBS/libEndpointSecuritySystem.dylib.md)
- [/usr/lib/libFosl_dynamic.dylib](DYLIBS/libFosl_dynamic.dylib.md)
- [/usr/lib/libMobileGestalt.dylib](DYLIBS/libMobileGestalt.dylib.md)
- [/usr/lib/libNFC_Comet.dylib](DYLIBS/libNFC_Comet.dylib.md)
- [/usr/lib/libNFC_HAL.dylib](DYLIBS/libNFC_HAL.dylib.md)
- [/usr/lib/libPN548_API.dylib](DYLIBS/libPN548_API.dylib.md)
- [/usr/lib/libParallelCompression.dylib](DYLIBS/libParallelCompression.dylib.md)
- [/usr/lib/libRosetta.dylib](DYLIBS/libRosetta.dylib.md)
- [/usr/lib/libTelephonyCapabilities.dylib](DYLIBS/libTelephonyCapabilities.dylib.md)
- [/usr/lib/libUSBCfwflasher.dylib](DYLIBS/libUSBCfwflasher.dylib.md)
- [/usr/lib/libarchive.2.dylib](DYLIBS/libarchive.2.dylib.md)
- [/usr/lib/libauthinstall.dylib](DYLIBS/libauthinstall.dylib.md)
- [/usr/lib/libboringssl.dylib](DYLIBS/libboringssl.dylib.md)
- [/usr/lib/libcoreroutine.dylib](DYLIBS/libcoreroutine.dylib.md)
- [/usr/lib/libcryptex.dylib](DYLIBS/libcryptex.dylib.md)
- [/usr/lib/libcryptex_core.dylib](DYLIBS/libcryptex_core.dylib.md)
- [/usr/lib/libcryptex_interface.dylib](DYLIBS/libcryptex_interface.dylib.md)
- [/usr/lib/libcryptex_trampoline.dylib](DYLIBS/libcryptex_trampoline.dylib.md)
- [/usr/lib/libicucore.A.dylib](DYLIBS/libicucore.A.dylib.md)
- [/usr/lib/libimage4.dylib](DYLIBS/libimage4.dylib.md)
- [/usr/lib/libmecabra.dylib](DYLIBS/libmecabra.dylib.md)
- [/usr/lib/libmis.dylib](DYLIBS/libmis.dylib.md)
- [/usr/lib/libmorphun.dylib](DYLIBS/libmorphun.dylib.md)
- [/usr/lib/libnetquality.dylib](DYLIBS/libnetquality.dylib.md)
- [/usr/lib/libnetwork.dylib](DYLIBS/libnetwork.dylib.md)
- [/usr/lib/libnfshared.dylib](DYLIBS/libnfshared.dylib.md)
- [/usr/lib/libnwswifttls.dylib](DYLIBS/libnwswifttls.dylib.md)
- [/usr/lib/liboah.dylib](DYLIBS/liboah.dylib.md)
- [/usr/lib/libobjc.A.dylib](DYLIBS/libobjc.A.dylib.md)
- [/usr/lib/libquic.dylib](DYLIBS/libquic.dylib.md)
- [/usr/lib/libsandbox.1.dylib](DYLIBS/libsandbox.1.dylib.md)
- [/usr/lib/libskit.dylib](DYLIBS/libskit.dylib.md)
- [/usr/lib/libsqlite3.dylib](DYLIBS/libsqlite3.dylib.md)
- [/usr/lib/libtailspin.dylib](DYLIBS/libtailspin.dylib.md)
- [/usr/lib/libtidy.A.dylib](DYLIBS/libtidy.A.dylib.md)
- [/usr/lib/libusrtcp.dylib](DYLIBS/libusrtcp.dylib.md)
- [/usr/lib/log/liblog_location.dylib](DYLIBS/liblog_location.dylib.md)
- [/usr/lib/log/liblog_network.dylib](DYLIBS/liblog_network.dylib.md)
- [/usr/lib/swift/libswiftAVFoundation.dylib](DYLIBS/libswiftAVFoundation.dylib.md)
- [/usr/lib/swift/libswiftAccelerate.dylib](DYLIBS/libswiftAccelerate.dylib.md)
- [/usr/lib/swift/libswiftAppleArchive.dylib](DYLIBS/libswiftAppleArchive.dylib.md)
- [/usr/lib/swift/libswiftCompression.dylib](DYLIBS/libswiftCompression.dylib.md)
- [/usr/lib/swift/libswiftCore.dylib](DYLIBS/libswiftCore.dylib.md)
- [/usr/lib/swift/libswiftCoreImage.dylib](DYLIBS/libswiftCoreImage.dylib.md)
- [/usr/lib/swift/libswiftCoreML.dylib](DYLIBS/libswiftCoreML.dylib.md)
- [/usr/lib/swift/libswiftCoreMedia.dylib](DYLIBS/libswiftCoreMedia.dylib.md)
- [/usr/lib/swift/libswiftCoreMediaIO.dylib](DYLIBS/libswiftCoreMediaIO.dylib.md)
- [/usr/lib/swift/libswiftDarwin.dylib](DYLIBS/libswiftDarwin.dylib.md)
- [/usr/lib/swift/libswiftDemangle.dylib](DYLIBS/libswiftDemangle.dylib.md)
- [/usr/lib/swift/libswiftDispatch.dylib](DYLIBS/libswiftDispatch.dylib.md)
- [/usr/lib/swift/libswiftDistributed.dylib](DYLIBS/libswiftDistributed.dylib.md)
- [/usr/lib/swift/libswiftNetwork.dylib](DYLIBS/libswiftNetwork.dylib.md)
- [/usr/lib/swift/libswiftObservation.dylib](DYLIBS/libswiftObservation.dylib.md)
- [/usr/lib/swift/libswiftQuartzCore.dylib](DYLIBS/libswiftQuartzCore.dylib.md)
- [/usr/lib/swift/libswiftRegexBuilder.dylib](DYLIBS/libswiftRegexBuilder.dylib.md)
- [/usr/lib/swift/libswiftSwiftOnoneSupport.dylib](DYLIBS/libswiftSwiftOnoneSupport.dylib.md)
- [/usr/lib/swift/libswiftSynchronization.dylib](DYLIBS/libswiftSynchronization.dylib.md)
- [/usr/lib/swift/libswiftVideoToolbox.dylib](DYLIBS/libswiftVideoToolbox.dylib.md)
- [/usr/lib/swift/libswiftVision.dylib](DYLIBS/libswiftVision.dylib.md)
- [/usr/lib/swift/libswiftWebKit.dylib](DYLIBS/libswiftWebKit.dylib.md)
- [/usr/lib/swift/libswiftXPC.dylib](DYLIBS/libswiftXPC.dylib.md)
- [/usr/lib/swift/libswift_Backtracing.dylib](DYLIBS/libswift_Backtracing.dylib.md)
- [/usr/lib/swift/libswift_Builtin_float.dylib](DYLIBS/libswift_Builtin_float.dylib.md)
- [/usr/lib/swift/libswift_Concurrency.dylib](DYLIBS/libswift_Concurrency.dylib.md)
- [/usr/lib/swift/libswift_Differentiation.dylib](DYLIBS/libswift_Differentiation.dylib.md)
- [/usr/lib/swift/libswift_RegexParser.dylib](DYLIBS/libswift_RegexParser.dylib.md)
- [/usr/lib/swift/libswift_StringProcessing.dylib](DYLIBS/libswift_StringProcessing.dylib.md)
- [/usr/lib/system/libcorecrypto.dylib](DYLIBS/libcorecrypto.dylib.md)
- [/usr/lib/system/libcorecrypto_noasm.dylib](DYLIBS/libcorecrypto_noasm.dylib.md)
- [/usr/lib/system/libcorecrypto_trace.dylib](DYLIBS/libcorecrypto_trace.dylib.md)
- [/usr/lib/system/libdyld.dylib](DYLIBS/libdyld.dylib.md)
- [/usr/lib/system/liblaunch.dylib](DYLIBS/liblaunch.dylib.md)
- [/usr/lib/system/libquarantine.dylib](DYLIBS/libquarantine.dylib.md)
- [/usr/lib/system/libsystem_containermanager.dylib](DYLIBS/libsystem_containermanager.dylib.md)
- [/usr/lib/system/libsystem_eligibility.dylib](DYLIBS/libsystem_eligibility.dylib.md)
- [/usr/lib/system/libsystem_m.dylib](DYLIBS/libsystem_m.dylib.md)
- [/usr/lib/system/libsystem_notify.dylib](DYLIBS/libsystem_notify.dylib.md)
- [/usr/lib/updaters/libAce3Updater.dylib](DYLIBS/libAce3Updater.dylib.md)
- [/usr/lib/updaters/libAppleTypeCRetimerUpdater.dylib](DYLIBS/libAppleTypeCRetimerUpdater.dylib.md)
- [/usr/lib/updaters/libPFXUpdater.dylib](DYLIBS/libPFXUpdater.dylib.md)
- [/usr/lib/updaters/libSEUpdater.dylib](DYLIBS/libSEUpdater.dylib.md)
- [/usr/lib/usd/libusd_ms.dylib](DYLIBS/libusd_ms.dylib.md)

</details>

### Feature Flags

#### ❌ Removed (4)

- `Domain/BlockMonitoring.plist`
- `Domain/CoreChartSwift.plist`
- `Domain/CoreChartSwift_iosmac.plist`
- `Domain/ModelCatalog.plist`

#### ⬆️ Updated (21)

<details>
  <summary><i>View Updated</i></summary>

- [Domain/Freeform.plist](FEATURES/Freeform.plist.md)
- [Domain/Home.plist](FEATURES/Home.plist.md)
- [Domain/IDS.plist](FEATURES/IDS.plist.md)
- [Domain/IconServices.plist](FEATURES/IconServices.plist.md)
- [Domain/MediaAnalysis.plist](FEATURES/MediaAnalysis.plist.md)
- [Domain/MediaRemote.plist](FEATURES/MediaRemote.plist.md)
- [Domain/NanoTimeKit.plist](FEATURES/NanoTimeKit.plist.md)
- [Domain/NetworkServiceProxy.plist](FEATURES/NetworkServiceProxy.plist.md)
- [Domain/ProactiveHarvesting.plist](FEATURES/ProactiveHarvesting.plist.md)
- [Domain/RealityKit.plist](FEATURES/RealityKit.plist.md)
- [Domain/SiriAnalytics.plist](FEATURES/SiriAnalytics.plist.md)
- [Domain/SiriHomeAutomation.plist](FEATURES/SiriHomeAutomation.plist.md)
- [Domain/SoundAnalysis.plist](FEATURES/SoundAnalysis.plist.md)
- [Domain/Spotlight.plist](FEATURES/Spotlight.plist.md)
- [Domain/TV.plist](FEATURES/TV.plist.md)
- [Domain/TVApp.plist](FEATURES/TVApp.plist.md)
- [Domain/TVRemoteCore.plist](FEATURES/TVRemoteCore.plist.md)
- [Domain/TrialXP.plist](FEATURES/TrialXP.plist.md)
- [Domain/UIKit.plist](FEATURES/UIKit.plist.md)
- [Domain/UserNotifications.plist](FEATURES/UserNotifications.plist.md)
- [Domain/WritingTools.plist](FEATURES/WritingTools.plist.md)

</details>

## EOF
