## MobileInBoxUpdate

> `/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/Versions/A/MobileInBoxUpdate`

```diff

-153.80.3.0.0
-  __TEXT.__text: 0x2d83c
-  __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_methlist: 0x14a8
+153.80.6.0.0
+  __TEXT.__text: 0x2e970
+  __TEXT.__auth_stubs: 0x910
+  __TEXT.__objc_methlist: 0x1500
   __TEXT.__const: 0x5eb8
-  __TEXT.__cstring: 0x12fa
-  __TEXT.__oslogstring: 0x1d9a
+  __TEXT.__cstring: 0x149a
+  __TEXT.__oslogstring: 0x1fdf
   __TEXT.__gcc_except_tab: 0x1bc
   __TEXT.__swift5_typeref: 0x98
   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x870
+  __TEXT.__unwind_info: 0x8c0
   __TEXT.__eh_frame: 0x80
-  __TEXT.__objc_classname: 0x20e
-  __TEXT.__objc_methname: 0x2a88
-  __TEXT.__objc_methtype: 0x5a1
-  __TEXT.__objc_stubs: 0x2860
-  __DATA_CONST.__got: 0x278
+  __TEXT.__objc_classname: 0x21c
+  __TEXT.__objc_methname: 0x2aea
+  __TEXT.__objc_methtype: 0x5a9
+  __TEXT.__objc_stubs: 0x28c0
+  __DATA_CONST.__got: 0x288
   __DATA_CONST.__const: 0x3b90
-  __DATA_CONST.__objc_classlist: 0xb8
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd68
+  __DATA_CONST.__objc_selrefs: 0xd98
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x80
-  __DATA_CONST.__objc_arraydata: 0x1f8
-  __AUTH_CONST.__auth_got: 0x420
-  __AUTH_CONST.__const: 0x2400
-  __AUTH_CONST.__cfstring: 0x1740
-  __AUTH_CONST.__objc_const: 0x2440
-  __AUTH_CONST.__objc_intobj: 0x1128
+  __DATA_CONST.__objc_arraydata: 0x258
+  __AUTH_CONST.__auth_got: 0x498
+  __AUTH_CONST.__const: 0x2560
+  __AUTH_CONST.__cfstring: 0x1920
+  __AUTH_CONST.__objc_const: 0x24d0
+  __AUTH_CONST.__objc_intobj: 0x1158
   __AUTH_CONST.__objc_arrayobj: 0x318
+  __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x6f0
+  __AUTH.__objc_data: 0x740
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x178
   __DATA.__data: 0x1500

   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/Versions/A/CoreWiFi

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: E8FEED9F-3F27-323A-8E3F-51F29F1FB09E
-  Functions: 1125
-  Symbols:   3005
-  CStrings:  1265
+  UUID: C51FD6ED-7921-3177-A119-F53ACFA993FB
+  Functions: 1159
+  Symbols:   3088
+  CStrings:  1316
 
Symbols:
+ +[MIBUPMUHelper _findServicePmuPrimary]
+ +[MIBUPMUHelper _findServicePmuPrimary].cold.1
+ +[MIBUPMUHelper _findServicePmuPrimary].cold.2
+ +[MIBUPMUHelper _findServicePmuPrimary].cold.3
+ +[MIBUPMUHelper _findServicePmuPrimary].cold.4
+ +[MIBUPMUHelper _findServicePmuPrimary].cold.5
+ +[MIBUPMUHelper _findServicePmuPrimary].cold.6
+ +[MIBUPMUHelper enableLPMFlag]
+ +[MIBUPMUHelper enableLPMFlag].cold.1
+ +[MIBUPMUHelper enableLPMFlag].cold.2
+ +[MIBUPMUHelper enableLPMFlag].cold.3
+ +[MIBUPMUHelper enableLPMFlag].cold.4
+ +[MIBUPMUHelper readBTFWOKFlag:]
+ +[MIBUPMUHelper readBTFWOKFlag:].cold.1
+ +[MIBUPMUHelper readBTFWOKFlag:].cold.2
+ +[MIBUPMUHelper readLPMFlag:]
+ +[MIBUPMUHelper wakedUpFromLPMSU]
+ +[MIBUPMUHelper wakedUpFromLPMSU].cold.1
+ +[MIBUPMUHelper wakedUpFromLPMSU].cold.2
+ +[MIBUPMUHelper wakedUpFromLPMSU].cold.3
+ +[MIBUPMUHelper wakedUpFromLPMSU].cold.4
+ +[MIBUPMUHelper wakedUpFromLPMSU].cold.5
+ -[MIBUClient isInPalletUpdateMode:].cold.2
+ -[MIBUTestPreferences wakedFromLPMSU]
+ GCC_except_table30
+ GCC_except_table45
+ GCC_except_table51
+ GCC_except_table66
+ _CFDictionaryGetTypeID
+ _CFGetTypeID
+ _CFNumberGetTypeID
+ _CFNumberGetValue
+ _CFRelease
+ _CFStringCreateWithCString
+ _IOIteratorNext
+ _IOObjectRelease
+ _IORegistryEntryCopyPath
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryGetProperty
+ _IORegistryEntrySearchCFProperty
+ _IORegistryEntrySetCFProperties
+ _IOServiceGetMatchingServices
+ _IOServiceNameMatching
+ _OBJC_CLASS_$_MIBUPMUHelper
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_METACLASS_$_MIBUPMUHelper
+ __23-[MIBUClient shutdown:]_block_invoke.111
+ __23-[MIBUClient shutdown:]_block_invoke.111.cold.1
+ __23-[MIBUClient shutdown:]_block_invoke.111.cold.2
+ __23-[MIBUClient shutdown:]_block_invoke.114
+ __23-[MIBUClient shutdown:]_block_invoke.114.cold.1
+ __23-[MIBUClient shutdown:]_block_invoke_2.115
+ __23-[MIBUClient shutdown:]_block_invoke_2.115.cold.1
+ __28-[MIBUClient connectToWiFi:]_block_invoke.82
+ __28-[MIBUClient connectToWiFi:]_block_invoke.82.cold.1
+ __28-[MIBUClient connectToWiFi:]_block_invoke.82.cold.2
+ __28-[MIBUClient connectToWiFi:]_block_invoke.85
+ __28-[MIBUClient connectToWiFi:]_block_invoke.85.cold.1
+ __28-[MIBUClient connectToWiFi:]_block_invoke_2.86
+ __28-[MIBUClient connectToWiFi:]_block_invoke_2.86.cold.1
+ __30+[MIBUPMUHelper enableLPMFlag]_block_invoke.38
+ __30+[MIBUPMUHelper enableLPMFlag]_block_invoke.38.cold.1
+ __30+[MIBUPMUHelper enableLPMFlag]_block_invoke.cold.1
+ __30-[MIBUClient stopWiFiMonitor:]_block_invoke.91
+ __30-[MIBUClient stopWiFiMonitor:]_block_invoke.91.cold.1
+ __30-[MIBUClient stopWiFiMonitor:]_block_invoke.91.cold.2
+ __30-[MIBUClient stopWiFiMonitor:]_block_invoke.94
+ __30-[MIBUClient stopWiFiMonitor:]_block_invoke.94.cold.1
+ __30-[MIBUClient stopWiFiMonitor:]_block_invoke_2.95
+ __30-[MIBUClient stopWiFiMonitor:]_block_invoke_2.95.cold.1
+ __32+[MIBUPMUHelper readBTFWOKFlag:]_block_invoke.cold.1
+ __33+[MIBUPMUHelper wakedUpFromLPMSU]_block_invoke.6
+ __33+[MIBUPMUHelper wakedUpFromLPMSU]_block_invoke.6.cold.1
+ __33+[MIBUPMUHelper wakedUpFromLPMSU]_block_invoke.9
+ __33+[MIBUPMUHelper wakedUpFromLPMSU]_block_invoke.9.cold.1
+ __33+[MIBUPMUHelper wakedUpFromLPMSU]_block_invoke.cold.1
+ __35-[MIBUClient isInPalletUpdateMode:]_block_invoke.56
+ __35-[MIBUClient isInPalletUpdateMode:]_block_invoke.56.cold.1
+ __39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.73
+ __39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.73.cold.1
+ __39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.76
+ __39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.76.cold.1
+ __39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.79
+ __39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.79.cold.1
+ __39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.cold.1
+ __45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.64
+ __45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.64.cold.1
+ __45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.64.cold.2
+ __45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.67
+ __45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke_2.68
+ __45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke_2.68.cold.1
+ __49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.76
+ __49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.76.cold.1
+ __49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.76.cold.2
+ __49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.79
+ __52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.100
+ __52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.100.cold.1
+ __52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.100.cold.2
+ __52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.103
+ __52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.103.cold.1
+ __52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke_2.104
+ __52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke_2.104.cold.1
+ __OBJC_$_CLASS_METHODS_MIBUPMUHelper
+ __OBJC_CLASS_RO_$_MIBUPMUHelper
+ __OBJC_METACLASS_RO_$_MIBUPMUHelper
+ ___30+[MIBUPMUHelper enableLPMFlag]_block_invoke
+ ___32+[MIBUPMUHelper readBTFWOKFlag:]_block_invoke
+ ___33+[MIBUPMUHelper wakedUpFromLPMSU]_block_invoke
+ ___39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke
+ __block_literal_global.108
+ __block_literal_global.110
+ __block_literal_global.60
+ __block_literal_global.72
+ __block_literal_global.75
+ __block_literal_global.78
+ __block_literal_global.81
+ __block_literal_global.88
+ __block_literal_global.90
+ __block_literal_global.97
+ __block_literal_global.99
+ _kIOMainPortDefault
+ _objc_msgSend$_findServicePmuPrimary
+ _objc_msgSend$wakedFromLPMSU
+ _objc_msgSend$wakedUpFromLPMSU
- GCC_except_table29
- GCC_except_table44
- GCC_except_table50
- GCC_except_table65
- __23-[MIBUClient shutdown:]_block_invoke.107
- __23-[MIBUClient shutdown:]_block_invoke.107.cold.1
- __23-[MIBUClient shutdown:]_block_invoke.107.cold.2
- __23-[MIBUClient shutdown:]_block_invoke.110
- __23-[MIBUClient shutdown:]_block_invoke.110.cold.1
- __23-[MIBUClient shutdown:]_block_invoke_2.111
- __23-[MIBUClient shutdown:]_block_invoke_2.111.cold.1
- __28-[MIBUClient connectToWiFi:]_block_invoke.78
- __28-[MIBUClient connectToWiFi:]_block_invoke.78.cold.1
- __28-[MIBUClient connectToWiFi:]_block_invoke.78.cold.2
- __28-[MIBUClient connectToWiFi:]_block_invoke.81
- __28-[MIBUClient connectToWiFi:]_block_invoke.81.cold.1
- __28-[MIBUClient connectToWiFi:]_block_invoke_2.82
- __28-[MIBUClient connectToWiFi:]_block_invoke_2.82.cold.1
- __30-[MIBUClient stopWiFiMonitor:]_block_invoke.87
- __30-[MIBUClient stopWiFiMonitor:]_block_invoke.87.cold.1
- __30-[MIBUClient stopWiFiMonitor:]_block_invoke.87.cold.2
- __30-[MIBUClient stopWiFiMonitor:]_block_invoke.90
- __30-[MIBUClient stopWiFiMonitor:]_block_invoke.90.cold.1
- __30-[MIBUClient stopWiFiMonitor:]_block_invoke_2.91
- __30-[MIBUClient stopWiFiMonitor:]_block_invoke_2.91.cold.1
- __45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.60
- __45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.60.cold.1
- __45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.60.cold.2
- __45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.63
- __45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke_2.64
- __45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke_2.64.cold.1
- __49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.72
- __49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.72.cold.1
- __49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.72.cold.2
- __49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.75
- __52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.96
- __52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.96.cold.1
- __52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.96.cold.2
- __52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.99
- __52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.99.cold.1
- __52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke_2.100
- __52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke_2.100.cold.1
- __block_literal_global.104
- __block_literal_global.119
- __block_literal_global.56
- __block_literal_global.74
- __block_literal_global.86
- __block_literal_global.89
- __block_literal_global.95
- __block_literal_global.98
CStrings:
+ "%{public}@: cannot find io registry entry for IOPMUPrimary"
+ "%{public}@: cannot set properties for IOPMUBootLPMCtrl"
+ "AppleDialogSPMIPMU"
+ "Cannot find IO registry entry for IOPMUPrimary"
+ "Cannot find IO registry entry property for IOPMUBootLPMCtrl"
+ "Cannot find IO registry entry property for IOPMUBootLPMFWOK"
+ "Cannot get value for IOPMUBootLPMFWOK"
+ "Device is NOT booted from LPMSU and not in InPalletUpdate mode"
+ "Forcing wakedUpFromLPMSU to YES!"
+ "Found primary PMU service: %{public}@"
+ "I16@0:8"
+ "IOPMUBootLPMCtrl"
+ "IOPMUBootLPMFWOK"
+ "IOPMUBootReasonLPMSU"
+ "IOPMUPrimary"
+ "IOService"
+ "MIBUPMUHelper"
+ "No IOPMUPrimary property found in PMU service: %{public}@"
+ "Not able to find AppleDialogSPMIPMU. IOServiceGetMatchingServices returned 0x%x"
+ "Not able to find primary PMU service."
+ "Not able to get property value of IOPMUBootReasonLPMSU. IORegistryEntryGetProperty returned 0x%x"
+ "Unexpected data type found for IOPMUBootLPMCtrl"
+ "Unexpected data type found for IOPMUBootLPMFWOK"
+ "Unexpected data type found for lpm3 key"
+ "WakedFromLPMSU"
+ "_findServicePmuPrimary"
+ "enableLPMFlag"
+ "imgIdx"
+ "lpm0"
+ "lpm1"
+ "lpm2"
+ "lpm3"
+ "readBTFWOKFlag:"
+ "readLPMFlag:"
+ "wakedFromLPMSU"
+ "wakedUpFromLPMSU"

```
