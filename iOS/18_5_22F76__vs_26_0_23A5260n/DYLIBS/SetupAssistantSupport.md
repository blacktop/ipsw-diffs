## SetupAssistantSupport

> `/System/Library/PrivateFrameworks/SetupAssistantSupport.framework/SetupAssistantSupport`

```diff

-534.0.0.0.0
-  __TEXT.__text: 0x137dc
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x177c
-  __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0xf75
-  __TEXT.__oslogstring: 0x9c2
-  __TEXT.__gcc_except_tab: 0x2a4
-  __TEXT.__dlopen_cstrs: 0x5ed
-  __TEXT.__unwind_info: 0x440
-  __TEXT.__objc_classname: 0x318
-  __TEXT.__objc_methname: 0x4115
-  __TEXT.__objc_methtype: 0x761
-  __TEXT.__objc_stubs: 0x33e0
-  __DATA_CONST.__got: 0x2d8
-  __DATA_CONST.__const: 0x830
+540.1.103.0.0
+  __TEXT.__text: 0x14a3c
+  __TEXT.__auth_stubs: 0x760
+  __TEXT.__objc_methlist: 0x17e4
+  __TEXT.__const: 0xb0
+  __TEXT.__cstring: 0xfeb
+  __TEXT.__oslogstring: 0xa2a
+  __TEXT.__gcc_except_tab: 0x2c0
+  __TEXT.__dlopen_cstrs: 0x692
+  __TEXT.__unwind_info: 0x470
+  __TEXT.__objc_classname: 0x319
+  __TEXT.__objc_methname: 0x42b3
+  __TEXT.__objc_methtype: 0x779
+  __TEXT.__objc_stubs: 0x35c0
+  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__const: 0x860
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1078
+  __DATA_CONST.__objc_selrefs: 0x1118
   __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x3b8
+  __AUTH_CONST.__auth_got: 0x3c0
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x1420
-  __AUTH_CONST.__objc_const: 0x2d78
-  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__cfstring: 0x1500
+  __AUTH_CONST.__objc_const: 0x2db8
+  __AUTH_CONST.__objc_intobj: 0x90
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x1c0
+  __DATA.__objc_ivar: 0x1c4
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x140
+  __DATA.__bss: 0x160
   __DATA_DIRTY.__objc_data: 0x730
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5D641932-15C0-3397-AC18-6DD18CF387B2
-  Functions: 559
-  Symbols:   2252
-  CStrings:  1324
+  UUID: 7A931121-565F-3F65-A473-B4BFD68E0C4B
+  Functions: 575
+  Symbols:   2295
+  CStrings:  1364
 
Symbols:
+ +[SASExpressCloudSettings _iPadMultitaskingMode]
+ +[SASLogging defaultCategory]
+ +[SASLogging defaultSubsystem]
+ +[SASSystemInformation storageAvailable].cold.1
+ -[SASExpressSettings StringAsIPadMultitaskingMode:]
+ -[SASExpressSettings hasIPadMultitaskingMode]
+ -[SASExpressSettings iPadMultitaskingModeAsString:]
+ -[SASExpressSettings iPadMultitaskingMode]
+ -[SASExpressSettings setHasIPadMultitaskingMode:]
+ -[SASExpressSettings setIPadMultitaskingMode:]
+ GCC_except_table36
+ OBJC_IVAR_$_SASExpressSettings._iPadMultitaskingMode
+ _SpringBoardServicesLibraryCore.frameworkLibrary
+ _UIKitLibraryCore.frameworkLibrary
+ ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.346
+ ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.346.cold.1
+ ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.347
+ ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.347.cold.1
+ ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.351
+ ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.351.cold.1
+ ___67-[SASExpressCloudSettings _fetchAppropriateSettingsWithCompletion:]_block_invoke.375
+ ___67-[SASExpressCloudSettings _fetchAppropriateSettingsWithCompletion:]_block_invoke.376
+ ___67-[SASExpressCloudSettings _fetchAppropriateSettingsWithCompletion:]_block_invoke.376.cold.1
+ ___SpringBoardServicesLibraryCore_block_invoke
+ ___UIKitLibraryCore_block_invoke
+ ___getSBSBuddyMultitaskingFlowClass_block_invoke
+ ___getSBSBuddyMultitaskingFlowClass_block_invoke.cold.1
+ ___getUIDeviceClass_block_invoke
+ ___getUIDeviceClass_block_invoke.cold.1
+ _audit_stringSpringBoardServices
+ _audit_stringUIKit
+ _getSBSBuddyMultitaskingFlowClass.softClass
+ _getUIDeviceClass.softClass
+ _objc_msgSend$_iPadMultitaskingMode
+ _objc_msgSend$_setError
+ _objc_msgSend$cStringUsingEncoding:
+ _objc_msgSend$currentMultitaskingOption
+ _objc_msgSend$defaultCategory
+ _objc_msgSend$defaultSubsystem
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$length
+ _objc_msgSend$position
+ _objc_msgSend$setIPadMultitaskingMode:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$userInterfaceIdiom
+ _statfs
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.340
- ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.340.cold.1
- ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.341
- ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.341.cold.1
- ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.345
- ___57-[SASExpressCloudSettings updateSettings:withCompletion:]_block_invoke.345.cold.1
- ___67-[SASExpressCloudSettings _fetchAppropriateSettingsWithCompletion:]_block_invoke.369
- ___67-[SASExpressCloudSettings _fetchAppropriateSettingsWithCompletion:]_block_invoke.370
- ___67-[SASExpressCloudSettings _fetchAppropriateSettingsWithCompletion:]_block_invoke.370.cold.1
- _kMGQDiskUsageTotalDataAvailable
CStrings:
+ "/private/var"
+ "AppsAndFullScreen"
+ "Fullscreen"
+ "SBSBuddyMultitaskingFlow"
+ "StringAsIPadMultitaskingMode:"
+ "Ti,N,V_iPadMultitaskingMode"
+ "UIDevice"
+ "_iPadMultitaskingMode"
+ "_setError"
+ "cStringUsingEncoding:"
+ "currentMultitaskingOption"
+ "defaultCategory"
+ "defaultSubsystem"
+ "fileSystemRepresentation"
+ "getBytes:range:"
+ "hasError"
+ "hasIPadMultitaskingMode"
+ "iPadMultitaskingMode"
+ "iPadMultitaskingModeAsString:"
+ "ipadmultitaskingmode"
+ "length"
+ "position"
+ "setHasIPadMultitaskingMode:"
+ "setIPadMultitaskingMode:"
+ "setPosition:"
+ "softlink:r:path:/System/Library/Frameworks/UIKit.framework/UIKit"
+ "softlink:r:path:/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices"
+ "storageAvailable returning %@"
+ "storageAvailable statfs failed with error %d"
+ "storageCapacity returning %@"
+ "unsignedIntValue"
+ "userInterfaceIdiom"
+ "{?=\"appearanceMode\"b1\"displayZoomOption\"b1\"iPadMultitaskingMode\"b1\"appAnalyticsOptIn\"b1\"deviceAnalyticsOptIn\"b1\"fileVaultEnabled\"b1\"findMyOptIn\"b1\"locationServicesOptIn\"b1\"screenTimeEnabled\"b1\"siriDataSharingOptIn\"b1\"siriOptIn\"b1\"siriVoiceTriggerEnabled\"b1\"softwareUpdateAutoDownloadEnabled\"b1\"softwareUpdateAutoUpdateEnabled\"b1\"stolenDeviceProtectionEnabled\"b1\"stolenDeviceProtectionStrictModeEnabled\"b1\"unlockWithWatchEnabled\"b1}"
- "{?=\"appearanceMode\"b1\"displayZoomOption\"b1\"appAnalyticsOptIn\"b1\"deviceAnalyticsOptIn\"b1\"fileVaultEnabled\"b1\"findMyOptIn\"b1\"locationServicesOptIn\"b1\"screenTimeEnabled\"b1\"siriDataSharingOptIn\"b1\"siriOptIn\"b1\"siriVoiceTriggerEnabled\"b1\"softwareUpdateAutoDownloadEnabled\"b1\"softwareUpdateAutoUpdateEnabled\"b1\"stolenDeviceProtectionEnabled\"b1\"stolenDeviceProtectionStrictModeEnabled\"b1\"unlockWithWatchEnabled\"b1}"

```
