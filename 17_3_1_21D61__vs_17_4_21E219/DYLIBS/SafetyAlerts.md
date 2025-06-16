## SafetyAlerts

> `/System/Library/PrivateFrameworks/SafetyAlerts.framework/SafetyAlerts`

```diff

-45.0.2.0.0
-  __TEXT.__text: 0x4a40
-  __TEXT.__auth_stubs: 0x2c0
-  __TEXT.__objc_methlist: 0x320
+45.0.8.0.0
+  __TEXT.__text: 0x5518
+  __TEXT.__auth_stubs: 0x420
+  __TEXT.__objc_methlist: 0x334
   __TEXT.__const: 0x4c
-  __TEXT.__cstring: 0x81d
-  __TEXT.__oslogstring: 0x1754
-  __TEXT.__gcc_except_tab: 0xc
-  __TEXT.__unwind_info: 0x160
-  __TEXT.__objc_classname: 0x22
-  __TEXT.__objc_methname: 0xafb
-  __TEXT.__objc_methtype: 0x106
-  __TEXT.__objc_stubs: 0x960
+  __TEXT.__gcc_except_tab: 0x38c
+  __TEXT.__cstring: 0x83b
+  __TEXT.__oslogstring: 0x17ec
+  __TEXT.__unwind_info: 0x264
+  __TEXT.__eh_frame: 0x38
+  __TEXT.__objc_classname: 0x24
+  __TEXT.__objc_methname: 0xb9f
+  __TEXT.__objc_methtype: 0x114
+  __TEXT.__objc_stubs: 0xa20
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x1a0
+  __DATA_CONST.__const: 0x1e8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1b8
-  __DATA_CONST.__objc_selrefs: 0x320
+  __DATA_CONST.__objc_selrefs: 0x360
+  __DATA_CONST.__objc_classrefs: 0x70
+  __DATA_CONST.__objc_superrefs: 0x10
+  __AUTH_CONST.__cfstring: 0x700
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x6e0
   __AUTH_CONST.__objc_const: 0x120
-  __AUTH_CONST.__auth_got: 0x170
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_classrefs: 0x68
-  __DATA.__objc_superrefs: 0x10
+  __AUTH_CONST.__auth_got: 0x220
   __DATA.__objc_ivar: 0x24
-  __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__common: 0x10
+  __DATA_DIRTY.__objc_data: 0xa0
+  __DATA_DIRTY.__common: 0x28
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EF1C2EA1-E6F9-31FA-85A6-9D3A7A8A647D
-  Functions: 85
-  Symbols:   358
-  CStrings:  336
+  UUID: 68433434-3840-3FFC-9998-84DEF06F127B
+  Functions: 89
+  Symbols:   420
+  CStrings:  349
 
Symbols:
+ -[SAEDFollowUpManager .cxx_destruct]
+ -[SafetyAlerts onAPSDConnectionChangeIsOverWiFi:isOverCell:]
+ GCC_except_table11
+ GCC_except_table13
+ GCC_except_table2
+ GCC_except_table20
+ GCC_except_table21
+ GCC_except_table22
+ GCC_except_table23
+ GCC_except_table24
+ GCC_except_table25
+ GCC_except_table27
+ GCC_except_table30
+ GCC_except_table32
+ GCC_except_table33
+ GCC_except_table34
+ GCC_except_table36
+ GCC_except_table39
+ GCC_except_table40
+ GCC_except_table43
+ GCC_except_table5
+ GCC_except_table53
+ GCC_except_table55
+ GCC_except_table57
+ GCC_except_table58
+ GCC_except_table6
+ _BiomeLibrary
+ _OBJC_CLASS_$_BMDeviceAPSDInterfaceStatus
+ __ZN14SAPlatformInfo20isAOPSupportedDeviceEv
+ __ZSt9terminatev
+ ___39-[SAEDFollowUpManager _retractFollowUp]_block_invoke.92
+ ___52-[SAEDFollowUpManager _evaluateFollowUpState_LOCKED]_block_invoke.47
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_ea8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_descriptor_40_ea8_32s_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_40_ea8_32s_e5_v8?0ls32l8
+ ___block_descriptor_41_ea8_32s_e5_v8?0ls32l8
+ ___block_descriptor_49_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32o40o48b_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s48l8s40l8
+ ___block_descriptor_56_ea8_32s40s48s_e20_v24?0Q8"NSError"16ls32l8s40l8s48l8
+ ___clang_call_terminate
+ ___cxa_begin_catch
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$APSDInterfaceStatus
+ _objc_msgSend$Device
+ _objc_msgSend$Wireless
+ _objc_msgSend$initWithStarting:isAPSDOverWiFi:isAPSDOverCell:
+ _objc_msgSend$sendEvent:
+ _objc_msgSend$source
+ _objc_release
+ _objc_release_x1
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x8
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_storeStrong
- ___39-[SAEDFollowUpManager _retractFollowUp]_block_invoke.91
- ___52-[SAEDFollowUpManager _evaluateFollowUpState_LOCKED]_block_invoke.29
- ___block_descriptor_40_e8_32o_e19_"NSDictionary"8?0ls32l8
- ___block_descriptor_40_e8_32o_e20_v20?0B8"NSError"12ls32l8
- ___block_descriptor_41_e8_32o_e5_v8?0ls32l8
- ___block_descriptor_48_e8_32o40b_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8
- ___block_descriptor_49_e8_32o40o_e5_v8?0ls32l8s40l8
- ___block_descriptor_56_e8_32o40o48o_e20_v24?0Q8"NSError"16ls32l8s40l8s48l8
CStrings:
+ "\x01"
+ ".cxx_destruct"
+ "APSDInterfaceStatus"
+ "Device"
+ "Wireless"
+ "initWithStarting:isAPSDOverWiFi:isAPSDOverCell:"
+ "onAPSDConnectionChangeIsOverWiFi:isOverCell:"
+ "saEmergencyAlertSwitchEnabled"
+ "sendEvent:"
+ "source"
+ "v24@0:8B16B20"
+ "{\"msg%{public}.0s\":\"#saClient,getIgneousEnablementStateReply\", \"inCountry\":%{public}hhd, \"inCoverage\":%{public}hhd, \"inMagnetMode\":%{public}hhd, \"optedIn\":%{public}hhd, \"enabled\":%{public}hhd, \"emergencyEnabled\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saClient,onAPSDConnectionChange\", \"isAPSDOverWiFi\":%{private}hhd, \"isAPSDOverCell\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#saClient,getIgneousEnablementStateReply\", \"inCountry\":%{public}hhd, \"inCoverage\":%{public}hhd, \"inMagnetMode\":%{public}hhd, \"optedIn\":%{public}hhd, \"enabled\":%{public}hhd}"

```
