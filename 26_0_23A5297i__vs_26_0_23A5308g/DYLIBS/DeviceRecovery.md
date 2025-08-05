## DeviceRecovery

> `/System/Library/PrivateFrameworks/DeviceRecovery.framework/DeviceRecovery`

```diff

-88.0.0.0.4
-  __TEXT.__text: 0x1eb94
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0x588
+95.0.0.0.1
+  __TEXT.__text: 0x1ed80
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__objc_methlist: 0x5c0
   __TEXT.__const: 0x188
   __TEXT.__gcc_except_tab: 0x2d4
-  __TEXT.__cstring: 0x39f6
+  __TEXT.__cstring: 0x3a70
   __TEXT.__oslogstring: 0xc6a
-  __TEXT.__unwind_info: 0x580
+  __TEXT.__unwind_info: 0x590
   __TEXT.__objc_classname: 0xa2
-  __TEXT.__objc_methname: 0xefe
+  __TEXT.__objc_methname: 0xfe7
   __TEXT.__objc_methtype: 0x28a
-  __TEXT.__objc_stubs: 0x940
+  __TEXT.__objc_stubs: 0x9e0
   __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x4a8
+  __DATA_CONST.__const: 0x4b8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x438
+  __DATA_CONST.__objc_selrefs: 0x470
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x328
-  __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0xe40
-  __AUTH_CONST.__objc_const: 0x718
+  __AUTH_CONST.__auth_got: 0x330
+  __AUTH_CONST.__const: 0x180
+  __AUTH_CONST.__cfstring: 0xea0
+  __AUTH_CONST.__objc_const: 0x778
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x54
+  __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0xca
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x8

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 606AA69B-8302-3886-AB31-2C8A306CE7FA
-  Functions: 720
-  Symbols:   1599
-  CStrings:  805
+  UUID: 34691EBB-2924-3A7E-BA04-5D02A90F162E
+  Functions: 727
+  Symbols:   1625
+  CStrings:  823
 
Symbols:
+ +[DeviceRecoveryController sharedController].cold.1
+ -[DeviceRecoveryController isPasscodeSet]
+ -[DeviceRecoveryController mainOSLanguageCode]
+ -[DeviceRecoveryController setIsPasscodeSet:]
+ -[DeviceRecoveryController setMainOSLanguageCode:]
+ -[DeviceRecoveryEnvironmentWorker getObjectFromInternalCookie:]
+ -[DeviceRecoveryEnvironmentWorker getObjectFromInternalCookie:].cold.1
+ GCC_except_table103
+ GCC_except_table104
+ GCC_except_table105
+ GCC_except_table15
+ GCC_except_table79
+ _DRServiceAttributeIsPasscodeSet
+ _DRServiceAttributeMainOSLanguageCode
+ _OBJC_IVAR_$_DeviceRecoveryController._isPasscodeSet
+ _OBJC_IVAR_$_DeviceRecoveryController._mainOSLanguageCode
+ ___32-[DeviceRecoveryController init]_block_invoke.28
+ ___32-[DeviceRecoveryController init]_block_invoke.29
+ ___32-[DeviceRecoveryController init]_block_invoke.29.cold.1
+ ___32-[DeviceRecoveryController init]_block_invoke.34
+ ___32-[DeviceRecoveryController init]_block_invoke.34.cold.1
+ ___32-[DeviceRecoveryController init]_block_invoke.34.cold.2
+ ___32-[DeviceRecoveryController init]_block_invoke.34.cold.3
+ ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.52
+ ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.52.cold.1
+ ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.52.cold.2
+ ___44+[DeviceRecoveryController sharedController]_block_invoke
+ ___52-[DeviceRecoveryController disableRecoveryAutoBoot:]_block_invoke.83
+ ___52-[DeviceRecoveryController disableRecoveryAutoBoot:]_block_invoke.83.cold.1
+ ___54-[DeviceRecoveryController recoverDeviceFromBootedOS:]_block_invoke.82
+ ___54-[DeviceRecoveryController recoverDeviceFromBootedOS:]_block_invoke.82.cold.1
+ ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.80
+ ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.80.cold.1
+ ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.80.cold.2
+ ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.79
+ ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.79.cold.1
+ ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.79.cold.2
+ ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.51
+ ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.51.cold.1
+ ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.51.cold.2
+ ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.75
+ ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.75.cold.1
+ ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.76
+ ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.76.cold.1
+ ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.76.cold.2
+ ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.78
+ ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.78.cold.1
+ ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.78.cold.2
+ ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.77
+ ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.77.cold.1
+ ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.77.cold.2
+ ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke.81
+ ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke.81.cold.1
+ ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke.81.cold.2
+ ___block_literal_global.32
+ _objc_msgSend$getObjectFromInternalCookie:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$setIsPasscodeSet:
+ _objc_msgSend$setMainOSLanguageCode:
+ _objc_msgSend$unsignedIntValue
+ _objc_release_x9
+ _sharedController.onceToken
- -[DeviceRecoveryEnvironmentWorker populateDREDescription:].cold.3
- GCC_except_table14
- GCC_except_table2
- GCC_except_table73
- GCC_except_table97
- GCC_except_table98
- GCC_except_table99
- ___32-[DeviceRecoveryController init]_block_invoke.26
- ___32-[DeviceRecoveryController init]_block_invoke.27
- ___32-[DeviceRecoveryController init]_block_invoke.27.cold.1
- ___32-[DeviceRecoveryController init]_block_invoke.32
- ___32-[DeviceRecoveryController init]_block_invoke.32.cold.1
- ___32-[DeviceRecoveryController init]_block_invoke.32.cold.2
- ___32-[DeviceRecoveryController init]_block_invoke.32.cold.3
- ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.50
- ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.50.cold.1
- ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.50.cold.2
- ___52-[DeviceRecoveryController disableRecoveryAutoBoot:]_block_invoke.81
- ___52-[DeviceRecoveryController disableRecoveryAutoBoot:]_block_invoke.81.cold.1
- ___54-[DeviceRecoveryController recoverDeviceFromBootedOS:]_block_invoke.80
- ___54-[DeviceRecoveryController recoverDeviceFromBootedOS:]_block_invoke.80.cold.1
- ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.78
- ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.78.cold.1
- ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.78.cold.2
- ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.77
- ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.77.cold.1
- ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.77.cold.2
- ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.49
- ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.49.cold.1
- ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.49.cold.2
- ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.73
- ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.73.cold.1
- ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.74
- ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.74.cold.1
- ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.74.cold.2
- ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.76
- ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.76.cold.1
- ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.76.cold.2
- ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.75
- ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.75.cold.1
- ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.75.cold.2
- ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke.79
- ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke.79.cold.1
- ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke.79.cold.2
- ___block_literal_global.30
CStrings:
+ "+[DeviceRecoveryController sharedController]_block_invoke"
+ "-[DeviceRecoveryEnvironmentWorker getObjectFromInternalCookie:]"
+ "3"
+ "IsPasscodeSet"
+ "MainOSLanguageCode"
+ "T@\"NSString\",&,V_mainOSLanguageCode"
+ "TB,V_isPasscodeSet"
+ "_isPasscodeSet"
+ "_mainOSLanguageCode"
+ "getObjectFromInternalCookie:"
+ "isPasscodeSet"
+ "mainOSLanguageCode"
+ "numberWithUnsignedInt:"
+ "setIsPasscodeSet:"
+ "setMainOSLanguageCode:"
+ "unsignedIntValue"
- "+[DeviceRecoveryController sharedController]"
- "2"

```
