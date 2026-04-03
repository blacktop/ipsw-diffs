# 26.5 (23F5043g) .vs 26.5 (23F5043k)

## Inputs

- `iPhone18,1_26.5_23F5043g_Restore.ipsw`
- `iPhone18,1_26.5_23F5043k_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 26.5 *(23F5043g)* | 25.5.0 | 12377.120.72.0.4~14 | Fri, 20Mar2026 18:55:25 PDT |
| 26.5 *(23F5043k)* | 25.5.0 | 12377.120.72.0.4~14 | Fri, 20Mar2026 18:55:25 PDT |

### Kexts

### ⬆️ Updated (2)

<details>
  <summary><i>View Updated</i></summary>

#### com.apple.driver.ApplePearlSEPDriver

>  `com.apple.driver.ApplePearlSEPDriver`

```diff

-877.120.2.0.0
+877.100.21.0.0
   __TEXT.__const: 0x318
-  __TEXT.__cstring: 0xadd0
-  __TEXT.__os_log: 0x4abd
-  __TEXT_EXEC.__text: 0x3df94
+  __TEXT.__cstring: 0xa992
+  __TEXT.__os_log: 0x498f
+  __TEXT_EXEC.__text: 0x3d2bc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcd
   __DATA.__common: 0x1d8

   __DATA_CONST.__got: 0x150
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x2058
+  __DATA_CONST.__const: 0x2050
   __DATA_CONST.__kalloc_type: 0x580
   __DATA_CONST.__kalloc_var: 0x1e0
-  UUID: 29B24457-7BA7-3882-80D6-DEFC108BCE59
-  Functions: 664
+  UUID: 8AD09EE4-AAD6-3F92-9E35-0094C6F0A878
+  Functions: 655
   Symbols:   0
-  CStrings:  1696
+  CStrings:  1677
 
CStrings:
+ "121111121222121211212111111111111111111111211211222222221222112222222212111211111212222111212111222222222222211222222222212211121112112221112222222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222212212222222212122222222221222122222222222222221212112222222212212221221111222222221121222231112221221221111111111121122211122"
- "%s <- _analyticsCurrentEvent: %d _proxState:%d\n"
- "%s <- _analyticsCurrentEvent: %d _proxState:%d newState:%d \n"
- "%s <- _proxState:%d\n"
- "%s <- newState:%d\n"
- "%s: Waiting for prox state to clear...\n"
- "12111112122212121121211111111111111111111121121122222222122211222222221211121111121222211121211122222222222221122222222221221112111211222111222222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222122222222122122222222121222222222212221222222222222222212121122222222122122212211112222222211212222311122212212211111111111211222111221"
- "ProxStateChanged"
- "__os_warn_unused(__builtin_sub_overflow((mach_continuous_time()), (_analyticsFaceDetectEvent.analyticsFaceDetectStartTime), (&_analyticsFaceDetectEvent.analyticsFaceDetectProxStateInfo.proxClearedEndTime))) == 0 "
- "__os_warn_unused(__builtin_sub_overflow((mach_continuous_time()), (_analyticsFaceDetectEvent.analyticsFaceDetectStartTime), (&_analyticsFaceDetectEvent.analyticsFaceDetectProxStateInfo.proxFirstSampleEndTime))) == 0 "
- "__os_warn_unused(__builtin_sub_overflow((mach_continuous_time()), (_analyticsMatchEvent.analyticsMatchStartTime), (&_analyticsMatchEvent.analyticsMatchProxStateInfo.proxClearedEndTime))) == 0 "
- "__os_warn_unused(__builtin_sub_overflow((mach_continuous_time()), (_analyticsMatchEvent.analyticsMatchStartTime), (&_analyticsMatchEvent.analyticsMatchProxStateInfo.proxFirstSampleEndTime))) == 0 "
- "_proxStateUpdateTimerEventSource"
- "analyticsProxStateChanged"
- "analyticsProxStateHandleClear"
- "checkProxStateAtOperationStart"
- "clearOperationProxState"
- "handleClearProxState"
- "proxStateChanged"
- "proxStateUpdateTimerHandler"
- "selectSecureFaceDetectFlowForFdet"

```

#### com.apple.driver.AppleProxDriver

>  `com.apple.driver.AppleProxDriver`

```diff

-49.5.5.0.0
+49.5.1.0.0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x8ca
-  __TEXT.__os_log: 0x787
-  __TEXT_EXEC.__text: 0xa5d4
+  __TEXT.__cstring: 0x884
+  __TEXT.__os_log: 0x710
+  __TEXT_EXEC.__text: 0xa014
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xe0
   __DATA.__common: 0xd8
-  __DATA_CONST.__auth_got: 0x188
-  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0x78
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
-  __DATA_CONST.__const: 0x2138
+  __DATA_CONST.__const: 0x2118
   __DATA_CONST.__kalloc_type: 0x140
-  UUID: 73DF2B45-B210-3687-8D37-A748494910BE
-  Functions: 196
+  UUID: 32D8BE36-C048-3C64-B427-9D554663B17F
+  Functions: 190
   Symbols:   0
-  CStrings:  165
+  CStrings:  157
 
CStrings:
+ "12111112122212121111111211111122111112121"
- "121111121222121211111112111111221111121212222"
- "DetectionMask"
- "DispatchProxEvent"
- "Prox is alive again!"
- "Prox not alive for %llu ms"
- "ProxAlive"
- "ProxClearSeen"
- "ProxState"
- "Set ProxClearSeen"

```


</details>

## MachO

### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### AppleProxServiceFilter

>  `/System/Library/HIDPlugins/ServiceFilters/AppleProxServiceFilter.plugin/AppleProxServiceFilter`

```diff

-49.5.5.0.0
-  __TEXT.__text: 0x9f1c
+49.5.1.0.0
+  __TEXT.__text: 0x9864
   __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_stubs: 0xdc0
+  __TEXT.__objc_stubs: 0xd00
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x9fc
-  __TEXT.__gcc_except_tab: 0xb5c
+  __TEXT.__objc_methlist: 0x92c
+  __TEXT.__gcc_except_tab: 0xad4
   __TEXT.__const: 0x1e8
-  __TEXT.__cstring: 0xd17
-  __TEXT.__oslogstring: 0xaa5
-  __TEXT.__objc_methname: 0x18bf
+  __TEXT.__cstring: 0xcc7
+  __TEXT.__oslogstring: 0xa45
+  __TEXT.__objc_methname: 0x16bc
   __TEXT.__objc_classname: 0x1ae
   __TEXT.__objc_methtype: 0x6e9
   __TEXT.__swift5_typeref: 0xa8

   __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x458
+  __TEXT.__unwind_info: 0x408
   __TEXT.__eh_frame: 0x80
   __DATA_CONST.__auth_got: 0x4b0
   __DATA_CONST.__got: 0x128
   __DATA_CONST.__auth_ptr: 0x68
   __DATA_CONST.__const: 0x1a8
-  __DATA_CONST.__cfstring: 0x1440
+  __DATA_CONST.__cfstring: 0x13a0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0xf70
-  __DATA.__objc_selrefs: 0x700
-  __DATA.__objc_ivar: 0xb0
+  __DATA.__objc_const: 0xe50
+  __DATA.__objc_selrefs: 0x670
+  __DATA.__objc_ivar: 0x98
   __DATA.__objc_data: 0x200
   __DATA.__data: 0x308
   __DATA.__bss: 0xd0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B5BA6DFC-7F06-350E-A6FE-FBF0C5EB496C
-  Functions: 278
+  UUID: 9AB27267-533C-3B78-A8D5-98FC68DAE9D4
+  Functions: 260
   Symbols:   171
-  CStrings:  843
+  CStrings:  798
 
CStrings:
+ "6\""
- "\""
- "H\""
- "HostStateNotification"
- "Prox alive after first clear event"
- "Prox is alive again!"
- "Prox not alive for %fs"
- "ProxAlive"
- "ProxClearSeen"
- "ProxClearSeen=%d"
- "ProxDetectionMode"
- "ProxState"
- "T@\"NSDate\",&,N,V_lastTurnOff"
- "T@\"NSDate\",&,N,V_lastTurnOn"
- "TB,N,V_clearSeen"
- "TB,N,V_eventReceivedAfterOn"
- "TB,N,V_isAlive"
- "TC,N,V_detectionMode"
- "_clearSeen"
- "_detectionMode"
- "_eventReceivedAfterOn"
- "_isAlive"
- "_lastTurnOff"
- "_lastTurnOn"
- "aliveCheck"
- "aliveEventReceived"
- "aliveTransitionHandling:"
- "clearSeen"
- "detectionMode"
- "eventReceivedAfterOn"
- "isAlive"
- "lastTurnOff"
- "lastTurnOn"
- "readClearSeen"
- "setClearSeen:"
- "setDetectionMode:"
- "setEventReceivedAfterOn:"
- "setIsAlive:"
- "setLastTurnOff:"
- "setLastTurnOn:"
- "unsignedCharValue"
- "writeClearSeen"

```


</details>

### iBoot

| iOS | Version |
| :-- | :------ |
| 26.5 *(23F5043g)* | mBoot-18000.120.27 |
| 26.5 *(23F5043k)* | mBoot-18000.120.27 |

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 26.5 *(23F5043g)* | 624.2.1.10.1 |
| 26.5 *(23F5043k)* | 624.2.1.10.1 |

### Dylibs

#### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### libBKDM2.dylib

>  `/usr/lib/libBKDM2.dylib`

```diff

-877.120.2.0.0
-  __TEXT.__text: 0x7a294
-  __TEXT.__auth_stubs: 0xe30
-  __TEXT.__objc_methlist: 0x5c94
+877.100.21.0.0
+  __TEXT.__text: 0x7976c
+  __TEXT.__auth_stubs: 0xdb0
+  __TEXT.__objc_methlist: 0x5bfc
   __TEXT.__const: 0x8dff
-  __TEXT.__cstring: 0x6caf
-  __TEXT.__oslogstring: 0x4372
-  __TEXT.__gcc_except_tab: 0x16e0
+  __TEXT.__cstring: 0x6c01
+  __TEXT.__oslogstring: 0x42ae
+  __TEXT.__gcc_except_tab: 0x1688
   __TEXT.__ustring: 0x11c
-  __TEXT.__unwind_info: 0xde0
+  __TEXT.__unwind_info: 0xdc8
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x37d
-  __TEXT.__objc_methname: 0x14a9b
-  __TEXT.__objc_methtype: 0x29a7
-  __TEXT.__objc_stubs: 0x7ea0
+  __TEXT.__objc_classname: 0x37a
+  __TEXT.__objc_methname: 0x1495d
+  __TEXT.__objc_methtype: 0x297f
+  __TEXT.__objc_stubs: 0x7e20
   __DATA_CONST.__got: 0x468
   __DATA_CONST.__const: 0x1528
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3cb0
+  __DATA_CONST.__objc_selrefs: 0x3c78
   __DATA_CONST.__objc_superrefs: 0xb8
-  __DATA_CONST.__objc_arraydata: 0x360
-  __AUTH_CONST.__auth_got: 0x728
+  __DATA_CONST.__objc_arraydata: 0x328
+  __AUTH_CONST.__auth_got: 0x6e8
   __AUTH_CONST.__const: 0x968
-  __AUTH_CONST.__cfstring: 0x60c0
-  __AUTH_CONST.__objc_const: 0x9448
-  __AUTH_CONST.__objc_intobj: 0x3a8
-  __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH_CONST.__objc_arrayobj: 0xf0
+  __AUTH_CONST.__cfstring: 0x5fa0
+  __AUTH_CONST.__objc_const: 0x92c8
+  __AUTH_CONST.__objc_intobj: 0x378
+  __AUTH_CONST.__objc_dictobj: 0xa0
+  __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0xa48
+  __DATA.__objc_ivar: 0xa24
   __DATA.__data: 0x890
   __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0x410

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: F534D562-59A1-380C-89DB-1D018E07C1C7
-  Functions: 2831
-  Symbols:   8579
-  CStrings:  5492
+  UUID: B132BCA9-D195-3855-B208-BABD905D1B45
+  Functions: 2812
+  Symbols:   8520
+  CStrings:  5448
 
Symbols:
+ GCC_except_table105
+ GCC_except_table109
+ GCC_except_table110
+ GCC_except_table116
+ GCC_except_table117
+ GCC_except_table124
+ GCC_except_table212
+ GCC_except_table228
+ GCC_except_table232
+ GCC_except_table244
+ GCC_except_table245
+ GCC_except_table251
+ GCC_except_table253
+ GCC_except_table65
+ GCC_except_table81
+ ___34-[BiometricKitXPCServerPearl init]_block_invoke.225
+ ___34-[BiometricKitXPCServerPearl init]_block_invoke.228
+ ___34-[BiometricKitXPCServerPearl init]_block_invoke_2.251
+ ___43-[BiometricKitXPCServerPearl serviceMatch:]_block_invoke.269
+ ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.876
+ ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.877
+ ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.878
+ ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.881
+ ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.882
+ ___75-[BiometricKitXPCServerPearl serviceStatus:version:ordinal:data:timestamp:]_block_invoke.274
+ ___block_literal_global.253
+ ___block_literal_global.518
+ ___block_literal_global.880
+ ___block_literal_global.884
+ ___block_literal_global.928
- -[BiometricKitXPCServerPearl init].cold.15
- -[BiometricKitXPCServerPearl init].cold.16
- -[BiometricKitXPCServerPearl updateProxState:]
- -[BiometricKitXPCServerPearl updateProxState:].cold.1
- -[BiometricKitXPCServerPearl updateProxState:].cold.2
- -[PearlCoreAnalyticsFaceDetectEvent proxClearedEndTime]
- -[PearlCoreAnalyticsFaceDetectEvent proxFirstSampleEndTime]
- -[PearlCoreAnalyticsFaceDetectEvent proxState]
- -[PearlCoreAnalyticsFaceDetectEvent setProxClearedEndTime:]
- -[PearlCoreAnalyticsFaceDetectEvent setProxFirstSampleEndTime:]
- -[PearlCoreAnalyticsFaceDetectEvent setProxState:]
- -[PearlCoreAnalyticsMatchEvent proxClearedEndTime]
- -[PearlCoreAnalyticsMatchEvent proxFirstSampleEndTime]
- -[PearlCoreAnalyticsMatchEvent proxState]
- -[PearlCoreAnalyticsMatchEvent setProxClearedEndTime:]
- -[PearlCoreAnalyticsMatchEvent setProxFirstSampleEndTime:]
- -[PearlCoreAnalyticsMatchEvent setProxState:]
- GCC_except_table113
- GCC_except_table114
- GCC_except_table119
- GCC_except_table120
- GCC_except_table127
- GCC_except_table215
- GCC_except_table231
- GCC_except_table241
- GCC_except_table247
- GCC_except_table248
- GCC_except_table256
- GCC_except_table257
- GCC_except_table66
- GCC_except_table84
- _IOHIDEventGetType
- _IOHIDEventSystemClientCopyServices
- _IOHIDEventSystemClientCreateWithType
- _IOHIDEventSystemClientRegisterEventCallback
- _IOHIDEventSystemClientScheduleWithDispatchQueue
- _IOHIDEventSystemClientSetMatching
- _IOHIDServiceClientCopyProperty
- _MGGetStringAnswer
- _OBJC_IVAR_$_BiometricKitXPCServerPearl._hidClient
- _OBJC_IVAR_$_BiometricKitXPCServerPearl._hidClientQueue
- _OBJC_IVAR_$_BiometricKitXPCServerPearl._proxState
- _OBJC_IVAR_$_PearlCoreAnalyticsFaceDetectEvent._proxClearedEndTime
- _OBJC_IVAR_$_PearlCoreAnalyticsFaceDetectEvent._proxFirstSampleEndTime
- _OBJC_IVAR_$_PearlCoreAnalyticsFaceDetectEvent._proxState
- _OBJC_IVAR_$_PearlCoreAnalyticsMatchEvent._proxClearedEndTime
- _OBJC_IVAR_$_PearlCoreAnalyticsMatchEvent._proxFirstSampleEndTime
- _OBJC_IVAR_$_PearlCoreAnalyticsMatchEvent._proxState
- ___34-[BiometricKitXPCServerPearl init]_block_invoke.259
- ___34-[BiometricKitXPCServerPearl init]_block_invoke.262
- ___34-[BiometricKitXPCServerPearl init]_block_invoke_2.285
- ___43-[BiometricKitXPCServerPearl serviceMatch:]_block_invoke.303
- ___43-[BiometricKitXPCServerPearl serviceMatch:]_block_invoke_2
- ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.922
- ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.923
- ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.924
- ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.927
- ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.928
- ___75-[BiometricKitXPCServerPearl serviceStatus:version:ordinal:data:timestamp:]_block_invoke.308
- ___HIDEventCallback
- ___block_literal_global.287
- ___block_literal_global.562
- ___block_literal_global.926
- ___block_literal_global.974
- ___block_literal_global.976
- _objc_msgSend$setProxClearedEndTime:
- _objc_msgSend$setProxFirstSampleEndTime:
- _objc_msgSend$setProxState:
- _objc_msgSend$updateProxState:
CStrings:
+ "v24@0:8^{?=icQBBCQQQBQCB{?=III}{?=BBiSSSSSCCIII}BQsB{?=III}{?=BBiSSSSSCCIII}Qs{?=III}{?=BBiSSSSSCCIII}CCB{?=BCCQQI(?={?={?=CCCCCCCCCCCCCCCCCCCC}{?=CCCCCCCCCCCCCCCCCCCC}CCCiiC}{?=[3[3i]]CC})}IIIIIBBCBB{?=BBBBBBBBBBBB}B[17c]B{?=IiiiB}CQCB{?=CCCCCC}{?=BBBBBBBBBBBB}{?=IIIBBB}C}16"
- "DeviceUsage"
- "DeviceUsagePage"
- "DeviceUsagePairs"
- "ProductType"
- "ProxAlive"
- "ProxState"
- "T@\"NSNumber\",&,V_proxClearedEndTime"
- "T@\"NSNumber\",&,V_proxFirstSampleEndTime"
- "T@\"NSNumber\",&,V_proxState"
- "^{__IOHIDEventSystemClient=}"
- "__HIDEventCallback(target:%p, event:%p)\n"
- "_hidClient"
- "_hidClientQueue"
- "_proxClearedEndTime"
- "_proxFirstSampleEndTime"
- "_proxState"
- "c"
- "com.apple.pearld.hid"
- "hidServices.count > 0"
- "iPhone15,2"
- "iPhone15,3"
- "ipad"
- "isIPad:%u productType:%@\n"
- "proxClearedEndTime"
- "proxFirstSampleEndTime"
- "proxState"
- "setProxClearedEndTime:"
- "setProxFirstSampleEndTime:"
- "setProxState:"
- "updateProxState:"
- "updateProxState: _proxState:%d -> newProxState:%d\n"
- "updateProxState: proxAliveProperty:%@\n"
- "updateProxState: proxStateProperty:%@\n"
- "v24@0:8^{?=icQBBCQQQBQCB{?=III}{?=BBiSSSSSCCIII}BQsB{?=III}{?=BBiSSSSSCCIII}Qs{?=III}{?=BBiSSSSSCCIII}CCB{?=BCCQQI(?={?={?=CCCCCCCCCCCCCCCCCCCC}{?=CCCCCCCCCCCCCCCCCCCC}CCCiiC}{?=[3[3i]]CC})}IIIIIBBCBB{?=BBBBBBBBBBBB}B[17c]B{?=IiiiB}CQCB{?=CCCCCC}{?=BBBBBBBBBBBB}{?=IIIBBB}C{?=QBQBc}}16"

```


</details>

## EOF
