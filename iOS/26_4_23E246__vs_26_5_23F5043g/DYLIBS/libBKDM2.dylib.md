## libBKDM2.dylib

> `/usr/lib/libBKDM2.dylib`

```diff

-877.100.21.0.0
-  __TEXT.__text: 0x7976c
-  __TEXT.__auth_stubs: 0xdb0
-  __TEXT.__objc_methlist: 0x5bfc
+877.120.2.0.0
+  __TEXT.__text: 0x7a294
+  __TEXT.__auth_stubs: 0xe30
+  __TEXT.__objc_methlist: 0x5c94
   __TEXT.__const: 0x8dff
-  __TEXT.__cstring: 0x6c01
-  __TEXT.__oslogstring: 0x42ae
-  __TEXT.__gcc_except_tab: 0x1688
+  __TEXT.__cstring: 0x6caf
+  __TEXT.__oslogstring: 0x4372
+  __TEXT.__gcc_except_tab: 0x16e0
   __TEXT.__ustring: 0x11c
-  __TEXT.__unwind_info: 0xdc8
+  __TEXT.__unwind_info: 0xde0
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x37a
-  __TEXT.__objc_methname: 0x1495d
-  __TEXT.__objc_methtype: 0x297f
-  __TEXT.__objc_stubs: 0x7e20
+  __TEXT.__objc_classname: 0x37d
+  __TEXT.__objc_methname: 0x14a9b
+  __TEXT.__objc_methtype: 0x29a7
+  __TEXT.__objc_stubs: 0x7ea0
   __DATA_CONST.__got: 0x468
   __DATA_CONST.__const: 0x1528
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3c78
+  __DATA_CONST.__objc_selrefs: 0x3cb0
   __DATA_CONST.__objc_superrefs: 0xb8
-  __DATA_CONST.__objc_arraydata: 0x328
-  __AUTH_CONST.__auth_got: 0x6e8
+  __DATA_CONST.__objc_arraydata: 0x360
+  __AUTH_CONST.__auth_got: 0x728
   __AUTH_CONST.__const: 0x968
-  __AUTH_CONST.__cfstring: 0x5fa0
-  __AUTH_CONST.__objc_const: 0x92c8
-  __AUTH_CONST.__objc_intobj: 0x378
-  __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH_CONST.__objc_arrayobj: 0xd8
+  __AUTH_CONST.__cfstring: 0x60c0
+  __AUTH_CONST.__objc_const: 0x9448
+  __AUTH_CONST.__objc_intobj: 0x3a8
+  __AUTH_CONST.__objc_dictobj: 0xf0
+  __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0xa24
+  __DATA.__objc_ivar: 0xa48
   __DATA.__data: 0x890
   __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0x410

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: DB5F0EEC-85C3-3902-941C-B02C932EF0A0
-  Functions: 2812
-  Symbols:   8520
-  CStrings:  5448
+  UUID: F534D562-59A1-380C-89DB-1D018E07C1C7
+  Functions: 2831
+  Symbols:   8579
+  CStrings:  5492
 
Symbols:
+ -[BiometricKitXPCServerPearl init].cold.15
+ -[BiometricKitXPCServerPearl init].cold.16
+ -[BiometricKitXPCServerPearl updateProxState:]
+ -[BiometricKitXPCServerPearl updateProxState:].cold.1
+ -[BiometricKitXPCServerPearl updateProxState:].cold.2
+ -[PearlCoreAnalyticsFaceDetectEvent proxClearedEndTime]
+ -[PearlCoreAnalyticsFaceDetectEvent proxFirstSampleEndTime]
+ -[PearlCoreAnalyticsFaceDetectEvent proxState]
+ -[PearlCoreAnalyticsFaceDetectEvent setProxClearedEndTime:]
+ -[PearlCoreAnalyticsFaceDetectEvent setProxFirstSampleEndTime:]
+ -[PearlCoreAnalyticsFaceDetectEvent setProxState:]
+ -[PearlCoreAnalyticsMatchEvent proxClearedEndTime]
+ -[PearlCoreAnalyticsMatchEvent proxFirstSampleEndTime]
+ -[PearlCoreAnalyticsMatchEvent proxState]
+ -[PearlCoreAnalyticsMatchEvent setProxClearedEndTime:]
+ -[PearlCoreAnalyticsMatchEvent setProxFirstSampleEndTime:]
+ -[PearlCoreAnalyticsMatchEvent setProxState:]
+ GCC_except_table113
+ GCC_except_table114
+ GCC_except_table119
+ GCC_except_table120
+ GCC_except_table127
+ GCC_except_table215
+ GCC_except_table231
+ GCC_except_table241
+ GCC_except_table247
+ GCC_except_table248
+ GCC_except_table256
+ GCC_except_table257
+ GCC_except_table66
+ GCC_except_table84
+ _IOHIDEventGetType
+ _IOHIDEventSystemClientCopyServices
+ _IOHIDEventSystemClientCreateWithType
+ _IOHIDEventSystemClientRegisterEventCallback
+ _IOHIDEventSystemClientScheduleWithDispatchQueue
+ _IOHIDEventSystemClientSetMatching
+ _IOHIDServiceClientCopyProperty
+ _MGGetStringAnswer
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._hidClient
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._hidClientQueue
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._proxState
+ _OBJC_IVAR_$_PearlCoreAnalyticsFaceDetectEvent._proxClearedEndTime
+ _OBJC_IVAR_$_PearlCoreAnalyticsFaceDetectEvent._proxFirstSampleEndTime
+ _OBJC_IVAR_$_PearlCoreAnalyticsFaceDetectEvent._proxState
+ _OBJC_IVAR_$_PearlCoreAnalyticsMatchEvent._proxClearedEndTime
+ _OBJC_IVAR_$_PearlCoreAnalyticsMatchEvent._proxFirstSampleEndTime
+ _OBJC_IVAR_$_PearlCoreAnalyticsMatchEvent._proxState
+ ___34-[BiometricKitXPCServerPearl init]_block_invoke.259
+ ___34-[BiometricKitXPCServerPearl init]_block_invoke.262
+ ___34-[BiometricKitXPCServerPearl init]_block_invoke_2.285
+ ___43-[BiometricKitXPCServerPearl serviceMatch:]_block_invoke.303
+ ___43-[BiometricKitXPCServerPearl serviceMatch:]_block_invoke_2
+ ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.922
+ ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.923
+ ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.924
+ ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.927
+ ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.928
+ ___75-[BiometricKitXPCServerPearl serviceStatus:version:ordinal:data:timestamp:]_block_invoke.308
+ ___HIDEventCallback
+ ___block_literal_global.287
+ ___block_literal_global.562
+ ___block_literal_global.926
+ ___block_literal_global.974
+ ___block_literal_global.976
+ _objc_msgSend$setProxClearedEndTime:
+ _objc_msgSend$setProxFirstSampleEndTime:
+ _objc_msgSend$setProxState:
+ _objc_msgSend$updateProxState:
- GCC_except_table105
- GCC_except_table109
- GCC_except_table110
- GCC_except_table116
- GCC_except_table117
- GCC_except_table124
- GCC_except_table212
- GCC_except_table228
- GCC_except_table232
- GCC_except_table244
- GCC_except_table245
- GCC_except_table251
- GCC_except_table253
- GCC_except_table65
- GCC_except_table81
- ___34-[BiometricKitXPCServerPearl init]_block_invoke.225
- ___34-[BiometricKitXPCServerPearl init]_block_invoke.228
- ___34-[BiometricKitXPCServerPearl init]_block_invoke_2.251
- ___43-[BiometricKitXPCServerPearl serviceMatch:]_block_invoke.269
- ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.876
- ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.877
- ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.878
- ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.881
- ___50-[BiometricKitXPCServerPearl initSecureFaceDetect]_block_invoke.882
- ___75-[BiometricKitXPCServerPearl serviceStatus:version:ordinal:data:timestamp:]_block_invoke.274
- ___block_literal_global.253
- ___block_literal_global.518
- ___block_literal_global.880
- ___block_literal_global.884
- ___block_literal_global.928
CStrings:
+ "DeviceUsage"
+ "DeviceUsagePage"
+ "DeviceUsagePairs"
+ "ProductType"
+ "ProxAlive"
+ "ProxState"
+ "T@\"NSNumber\",&,V_proxClearedEndTime"
+ "T@\"NSNumber\",&,V_proxFirstSampleEndTime"
+ "T@\"NSNumber\",&,V_proxState"
+ "^{__IOHIDEventSystemClient=}"
+ "__HIDEventCallback(target:%p, event:%p)\n"
+ "_hidClient"
+ "_hidClientQueue"
+ "_proxClearedEndTime"
+ "_proxFirstSampleEndTime"
+ "_proxState"
+ "c"
+ "com.apple.pearld.hid"
+ "hidServices.count > 0"
+ "iPhone15,2"
+ "iPhone15,3"
+ "ipad"
+ "isIPad:%u productType:%@\n"
+ "proxClearedEndTime"
+ "proxFirstSampleEndTime"
+ "proxState"
+ "setProxClearedEndTime:"
+ "setProxFirstSampleEndTime:"
+ "setProxState:"
+ "updateProxState:"
+ "updateProxState: _proxState:%d -> newProxState:%d\n"
+ "updateProxState: proxAliveProperty:%@\n"
+ "updateProxState: proxStateProperty:%@\n"
+ "v24@0:8^{?=icQBBCQQQBQCB{?=III}{?=BBiSSSSSCCIII}BQsB{?=III}{?=BBiSSSSSCCIII}Qs{?=III}{?=BBiSSSSSCCIII}CCB{?=BCCQQI(?={?={?=CCCCCCCCCCCCCCCCCCCC}{?=CCCCCCCCCCCCCCCCCCCC}CCCiiC}{?=[3[3i]]CC})}IIIIIBBCBB{?=BBBBBBBBBBBB}B[17c]B{?=IiiiB}CQCB{?=CCCCCC}{?=BBBBBBBBBBBB}{?=IIIBBB}C{?=QBQBc}}16"
- "v24@0:8^{?=icQBBCQQQBQCB{?=III}{?=BBiSSSSSCCIII}BQsB{?=III}{?=BBiSSSSSCCIII}Qs{?=III}{?=BBiSSSSSCCIII}CCB{?=BCCQQI(?={?={?=CCCCCCCCCCCCCCCCCCCC}{?=CCCCCCCCCCCCCCCCCCCC}CCCiiC}{?=[3[3i]]CC})}IIIIIBBCBB{?=BBBBBBBBBBBB}B[17c]B{?=IiiiB}CQCB{?=CCCCCC}{?=BBBBBBBBBBBB}{?=IIIBBB}C}16"

```
