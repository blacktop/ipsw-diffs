## MobileInBoxUpdate

> `/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate`

```diff

-153.80.3.0.0
-  __TEXT.__text: 0x2bcf4
-  __TEXT.__auth_stubs: 0x9d0
-  __TEXT.__objc_methlist: 0x14a8
+153.80.6.0.0
+  __TEXT.__text: 0x2cdf0
+  __TEXT.__auth_stubs: 0xac0
+  __TEXT.__objc_methlist: 0x1500
   __TEXT.__const: 0x5eb8
-  __TEXT.__cstring: 0x132a
-  __TEXT.__oslogstring: 0x1de2
+  __TEXT.__cstring: 0x14ca
+  __TEXT.__oslogstring: 0x2062
   __TEXT.__gcc_except_tab: 0x1c8
   __TEXT.__swift5_typeref: 0x98
   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x888
+  __TEXT.__unwind_info: 0x8d0
   __TEXT.__eh_frame: 0x80
-  __TEXT.__objc_classname: 0x20e
-  __TEXT.__objc_methname: 0x2a88
-  __TEXT.__objc_methtype: 0x5a1
-  __TEXT.__objc_stubs: 0x2880
-  __DATA_CONST.__got: 0x280
+  __TEXT.__objc_classname: 0x21c
+  __TEXT.__objc_methname: 0x2aea
+  __TEXT.__objc_methtype: 0x5a9
+  __TEXT.__objc_stubs: 0x28e0
+  __DATA_CONST.__got: 0x290
   __DATA_CONST.__const: 0x3cc8
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
-  __AUTH_CONST.__auth_got: 0x4f8
-  __AUTH_CONST.__const: 0x22e0
-  __AUTH_CONST.__cfstring: 0x1740
-  __AUTH_CONST.__objc_const: 0x2440
-  __AUTH_CONST.__objc_intobj: 0x1128
+  __DATA_CONST.__objc_arraydata: 0x258
+  __AUTH_CONST.__auth_got: 0x570
+  __AUTH_CONST.__const: 0x2440
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
   __DATA.__data: 0xef8

   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 16850A7E-50B8-3D5F-8E1C-2E7C64567F1D
-  Functions: 1120
-  Symbols:   4343
-  CStrings:  1267
+  UUID: CFB817C4-4655-3446-87B6-CFDD85959586
+  Functions: 1154
+  Symbols:   4473
+  CStrings:  1319
 
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
+ GCC_except_table41
+ GCC_except_table47
+ GCC_except_table62
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
+ __OBJC_$_CLASS_METHODS_MIBUPMUHelper
+ __OBJC_CLASS_RO_$_MIBUPMUHelper
+ __OBJC_METACLASS_RO_$_MIBUPMUHelper
+ ___23-[MIBUClient shutdown:]_block_invoke.118
+ ___23-[MIBUClient shutdown:]_block_invoke.118.cold.1
+ ___23-[MIBUClient shutdown:]_block_invoke.118.cold.2
+ ___23-[MIBUClient shutdown:]_block_invoke.121
+ ___23-[MIBUClient shutdown:]_block_invoke.121.cold.1
+ ___23-[MIBUClient shutdown:]_block_invoke_2.122
+ ___23-[MIBUClient shutdown:]_block_invoke_2.122.cold.1
+ ___28-[MIBUClient connectToWiFi:]_block_invoke.89
+ ___28-[MIBUClient connectToWiFi:]_block_invoke.89.cold.1
+ ___28-[MIBUClient connectToWiFi:]_block_invoke.89.cold.2
+ ___28-[MIBUClient connectToWiFi:]_block_invoke.92
+ ___28-[MIBUClient connectToWiFi:]_block_invoke.92.cold.1
+ ___28-[MIBUClient connectToWiFi:]_block_invoke_2.93
+ ___28-[MIBUClient connectToWiFi:]_block_invoke_2.93.cold.1
+ ___30+[MIBUPMUHelper enableLPMFlag]_block_invoke
+ ___30+[MIBUPMUHelper enableLPMFlag]_block_invoke.38
+ ___30+[MIBUPMUHelper enableLPMFlag]_block_invoke.38.cold.1
+ ___30+[MIBUPMUHelper enableLPMFlag]_block_invoke.cold.1
+ ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.101
+ ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.101.cold.1
+ ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.98
+ ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.98.cold.1
+ ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.98.cold.2
+ ___30-[MIBUClient stopWiFiMonitor:]_block_invoke_2.102
+ ___30-[MIBUClient stopWiFiMonitor:]_block_invoke_2.102.cold.1
+ ___32+[MIBUPMUHelper readBTFWOKFlag:]_block_invoke
+ ___32+[MIBUPMUHelper readBTFWOKFlag:]_block_invoke.cold.1
+ ___33+[MIBUPMUHelper wakedUpFromLPMSU]_block_invoke
+ ___33+[MIBUPMUHelper wakedUpFromLPMSU]_block_invoke.6
+ ___33+[MIBUPMUHelper wakedUpFromLPMSU]_block_invoke.6.cold.1
+ ___33+[MIBUPMUHelper wakedUpFromLPMSU]_block_invoke.9
+ ___33+[MIBUPMUHelper wakedUpFromLPMSU]_block_invoke.9.cold.1
+ ___33+[MIBUPMUHelper wakedUpFromLPMSU]_block_invoke.cold.1
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.56
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.56.cold.1
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.59
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.59.cold.1
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.59.cold.2
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.62
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.62.cold.1
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke_2.63
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke_2.63.cold.1
+ ___39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke
+ ___39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.73
+ ___39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.73.cold.1
+ ___39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.76
+ ___39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.76.cold.1
+ ___39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.79
+ ___39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.79.cold.1
+ ___39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.cold.1
+ ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.71
+ ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.71.cold.1
+ ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.71.cold.2
+ ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.74
+ ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke_2.75
+ ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke_2.75.cold.1
+ ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.83
+ ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.83.cold.1
+ ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.83.cold.2
+ ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.86
+ ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.107
+ ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.107.cold.1
+ ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.107.cold.2
+ ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.110
+ ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.110.cold.1
+ ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke_2.111
+ ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke_2.111.cold.1
+ ___block_literal_global.104
+ ___block_literal_global.193
+ ___block_literal_global.72
+ ___block_literal_global.75
+ ___block_literal_global.88
+ ___block_literal_global.95
+ ___block_literal_global.97
+ _kIOMainPortDefault
+ _objc_msgSend$_findServicePmuPrimary
+ _objc_msgSend$wakedFromLPMSU
+ _objc_msgSend$wakedUpFromLPMSU
- GCC_except_table29
- GCC_except_table40
- GCC_except_table46
- GCC_except_table61
- ___23-[MIBUClient shutdown:]_block_invoke.114
- ___23-[MIBUClient shutdown:]_block_invoke.114.cold.1
- ___23-[MIBUClient shutdown:]_block_invoke.114.cold.2
- ___23-[MIBUClient shutdown:]_block_invoke.117
- ___23-[MIBUClient shutdown:]_block_invoke.117.cold.1
- ___23-[MIBUClient shutdown:]_block_invoke_2.118
- ___23-[MIBUClient shutdown:]_block_invoke_2.118.cold.1
- ___28-[MIBUClient connectToWiFi:]_block_invoke.85
- ___28-[MIBUClient connectToWiFi:]_block_invoke.85.cold.1
- ___28-[MIBUClient connectToWiFi:]_block_invoke.85.cold.2
- ___28-[MIBUClient connectToWiFi:]_block_invoke.88
- ___28-[MIBUClient connectToWiFi:]_block_invoke.88.cold.1
- ___28-[MIBUClient connectToWiFi:]_block_invoke_2.89
- ___28-[MIBUClient connectToWiFi:]_block_invoke_2.89.cold.1
- ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.94
- ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.94.cold.1
- ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.94.cold.2
- ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.97
- ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.97.cold.1
- ___30-[MIBUClient stopWiFiMonitor:]_block_invoke_2.98
- ___30-[MIBUClient stopWiFiMonitor:]_block_invoke_2.98.cold.1
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.55
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.55.cold.1
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.55.cold.2
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.58
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.58.cold.1
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke_2.59
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke_2.59.cold.1
- ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.67
- ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.67.cold.1
- ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.67.cold.2
- ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.70
- ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke_2.71
- ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke_2.71.cold.1
- ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.79
- ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.79.cold.1
- ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.79.cold.2
- ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.82
- ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.103
- ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.103.cold.1
- ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.103.cold.2
- ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.106
- ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.106.cold.1
- ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke_2.107
- ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke_2.107.cold.1
- ___block_literal_global.102
- ___block_literal_global.105
- ___block_literal_global.111
- ___block_literal_global.116
- ___block_literal_global.123
- ___block_literal_global.189
- ___block_literal_global.69
- ___block_literal_global.84
- ___block_literal_global.87
- ___block_literal_global.93
- ___block_literal_global.96
CStrings:
+ "%{public}@: cannot find io registry entry for IOPMUPrimary"
+ "%{public}@: cannot set properties for IOPMUBootLPMCtrl"
+ "AppleDialogSPMIPMU"
+ "Cannot find IO registry entry for IOPMUPrimary"
+ "Cannot find IO registry entry property for IOPMUBootLPMCtrl"
+ "Cannot find IO registry entry property for IOPMUBootLPMFWOK"
+ "Cannot get value for IOPMUBootLPMFWOK"
+ "Device is NOT booted from LPMSU and not in InPalletUpdate mode"
+ "Device is already activated and not in InPalletUpdate mode"
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
