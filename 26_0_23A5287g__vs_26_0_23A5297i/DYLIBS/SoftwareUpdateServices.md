## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-950.0.19.0.1
-  __TEXT.__text: 0xaecd8
+950.0.24.0.0
+  __TEXT.__text: 0xaf8ac
   __TEXT.__auth_stubs: 0xea0
-  __TEXT.__objc_methlist: 0xab6c
+  __TEXT.__objc_methlist: 0xac0c
   __TEXT.__const: 0x318
-  __TEXT.__cstring: 0x208e6
+  __TEXT.__cstring: 0x20c51
   __TEXT.__gcc_except_tab: 0x1014
   __TEXT.__oslogstring: 0xd81
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x3138
-  __TEXT.__objc_classname: 0xeec
-  __TEXT.__objc_methname: 0x18aac
+  __TEXT.__unwind_info: 0x3160
+  __TEXT.__objc_classname: 0xf05
+  __TEXT.__objc_methname: 0x18b72
   __TEXT.__objc_methtype: 0x344d
-  __TEXT.__objc_stubs: 0x140a0
-  __DATA_CONST.__got: 0xd90
-  __DATA_CONST.__const: 0x28d8
-  __DATA_CONST.__objc_classlist: 0x3d0
+  __TEXT.__objc_stubs: 0x141a0
+  __DATA_CONST.__got: 0xd98
+  __DATA_CONST.__const: 0x2900
+  __DATA_CONST.__objc_classlist: 0x3d8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5ba0
+  __DATA_CONST.__objc_selrefs: 0x5be0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x318
+  __DATA_CONST.__objc_superrefs: 0x320
   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0x760
   __AUTH_CONST.__const: 0x780
-  __AUTH_CONST.__cfstring: 0x12980
-  __AUTH_CONST.__objc_const: 0x156e8
+  __AUTH_CONST.__cfstring: 0x12b80
+  __AUTH_CONST.__objc_const: 0x157b0
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH.__objc_data: 0xfc8
-  __DATA.__objc_ivar: 0x948
+  __AUTH.__objc_data: 0x1018
+  __DATA.__objc_ivar: 0x94c
   __DATA.__data: 0xe98
   __DATA.__bss: 0xe8
   __DATA_DIRTY.__objc_data: 0x1658

   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler
+  - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/LockdownMode.framework/LockdownMode
   - /System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: FFF10FD4-134D-33A3-96D8-BEAF99BC602D
-  Functions: 4453
-  Symbols:   14778
-  CStrings:  10033
+  UUID: A4D3AA0A-A082-36BA-A51A-E9872D8F8AB7
+  Functions: 4471
+  Symbols:   14830
+  CStrings:  10076
 
Symbols:
+ +[SUSpace _runGetOffTestingIfNecessary:handler:]
+ -[SUAppPurgingAlertItem modelSpecificLocalizedStringKeyForKey:]
+ -[SUGetOffTestingAlertItem .cxx_destruct]
+ -[SUGetOffTestingAlertItem _noButton]
+ -[SUGetOffTestingAlertItem _yesButton]
+ -[SUGetOffTestingAlertItem alertWasDismissed:]
+ -[SUGetOffTestingAlertItem buttons]
+ -[SUGetOffTestingAlertItem initWithHandler:]
+ -[SUGetOffTestingAlertItem message]
+ -[SUGetOffTestingAlertItem title]
+ -[SUPreferences setTestGetOffSampleRate:]
+ -[SUPreferences testGetOffSampleRate]
+ GCC_except_table52
+ _OBJC_CLASS_$_GMAvailabilityWrapper
+ _OBJC_CLASS_$_SUGetOffTestingAlertItem
+ _OBJC_IVAR_$_SUGetOffTestingAlertItem._handler
+ _OBJC_METACLASS_$_SUGetOffTestingAlertItem
+ __OBJC_$_INSTANCE_METHODS_SUGetOffTestingAlertItem
+ __OBJC_$_INSTANCE_VARIABLES_SUGetOffTestingAlertItem
+ __OBJC_CLASS_RO_$_SUGetOffTestingAlertItem
+ __OBJC_METACLASS_RO_$_SUGetOffTestingAlertItem
+ ___32-[SUInstaller installCompleted:]_block_invoke.381
+ ___32-[SUInstaller installCompleted:]_block_invoke_2.382
+ ___32-[SUInstaller installCompleted:]_block_invoke_3.388
+ ___37-[SUGetOffTestingAlertItem _noButton]_block_invoke
+ ___38-[SUGetOffTestingAlertItem _yesButton]_block_invoke
+ ___40+[SUSpace makeRoomForUpdate:completion:]_block_invoke_8
+ ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.529
+ ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.533
+ ___48+[SUSpace _runGetOffTestingIfNecessary:handler:]_block_invoke
+ ___48+[SUSpace _runGetOffTestingIfNecessary:handler:]_block_invoke_2
+ ___48+[SUSpace _runGetOffTestingIfNecessary:handler:]_block_invoke_3
+ ___86-[SUManagerCore updatesDownloadableWithOptions:alternateDownloadOptions:replyHandler:]_block_invoke.491
+ ___block_descriptor_48_e8_32bs_e8_v12?0i8ls32l8
+ ___block_descriptor_56_e8_32s40bs_e41_v24?0"SUSpaceCheckResults"8"NSError"16ls32l8s40l8
+ ___block_literal_global.287
+ ___block_literal_global.301
+ ___block_literal_global.306
+ ___block_literal_global.311
+ ___block_literal_global.316
+ ___block_literal_global.321
+ ___block_literal_global.326
+ ___block_literal_global.331
+ ___block_literal_global.336
+ ___block_literal_global.344
+ ___block_literal_global.349
+ ___block_literal_global.357
+ ___block_literal_global.393
+ ___block_literal_global.401
+ ___block_literal_global.407
+ ___block_literal_global.429
+ ___block_literal_global.460
+ ___block_literal_global.507
+ ___block_literal_global.532
+ ___block_literal_global.537
+ ___block_literal_global.564
+ ___block_literal_global.580
+ ___block_literal_global.590
+ ___block_literal_global.612
+ ___block_literal_global.622
+ _objc_msgSend$_runGetOffTestingIfNecessary:handler:
+ _objc_msgSend$initWithHandler:
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$setTestGetOffSampleRate:
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$testGetOffSampleRate
+ _objc_msgSend$uppercaseString
+ _objc_msgSend$wasEverAvailable
- _OBJC_CLASS_$_UIDevice
- ___32-[SUInstaller installCompleted:]_block_invoke.384
- ___32-[SUInstaller installCompleted:]_block_invoke_2.385
- ___32-[SUInstaller installCompleted:]_block_invoke_3.391
- ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.532
- ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.536
- ___86-[SUManagerCore updatesDownloadableWithOptions:alternateDownloadOptions:replyHandler:]_block_invoke.494
- ___block_descriptor_56_e8_32s40bs_e41_v24?0"SUSpaceCheckResults"8"NSError"16ls40l8s32l8
- ___block_literal_global.293
- ___block_literal_global.304
- ___block_literal_global.309
- ___block_literal_global.314
- ___block_literal_global.319
- ___block_literal_global.324
- ___block_literal_global.329
- ___block_literal_global.334
- ___block_literal_global.339
- ___block_literal_global.347
- ___block_literal_global.352
- ___block_literal_global.360
- ___block_literal_global.396
- ___block_literal_global.398
- ___block_literal_global.404
- ___block_literal_global.410
- ___block_literal_global.432
- ___block_literal_global.463
- ___block_literal_global.510
- ___block_literal_global.535
- ___block_literal_global.540
- ___block_literal_global.567
- ___block_literal_global.583
- ___block_literal_global.593
- ___block_literal_global.615
- ___block_literal_global.625
CStrings:
+ " "
+ "%@_%@"
+ "+[SUSpace _runGetOffTestingIfNecessary:handler:]_block_invoke_2"
+ "+[SUSpace _runGetOffTestingIfNecessary:handler:]_block_invoke_3"
+ "+[SUSpace makeRoomForUpdate:completion:]_block_invoke_5"
+ "Continue"
+ "Continue Without Offloading"
+ "Failed to submit event %@\n"
+ "GSDeviceName"
+ "SUGetOffTestingAlertItem"
+ "SUTestGetOffSampleRate"
+ "Temporarily Disable Apple Intelligence Features to Install Update"
+ "The sample rate (probability) of enabling the Get-Off testing flow"
+ "[%@] User chose Continue"
+ "[%@] User chose Install-Without-Offload"
+ "[Intenral Only]\nTo help verify our ability to offload Apple Intelligence for users on low-disk space devices. We are asking you to consent to offloading Apple Intelligence. Offloading should immediately disable some Apple Intelligence features while on the current OS. If this fails, you will be prompted to file a radar."
+ "_"
+ "_SIMULATOR"
+ "_runGetOffTestingIfNecessary:handler:"
+ "initWithHandler:"
+ "mobileAssetSuspend failed with %@; disabling get-off testing"
+ "rangeOfString:"
+ "setTestGetOffSampleRate:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "testGetOffSampleRate"
+ "the user declined; disabling get-off testing"
+ "uppercaseString"
+ "wasEverAvailable"
- "+[SUSpace makeRoomForUpdate:completion:]_block_invoke_4"

```
