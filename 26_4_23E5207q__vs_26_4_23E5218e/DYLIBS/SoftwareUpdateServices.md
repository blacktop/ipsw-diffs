## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-950.100.130.0.1
-  __TEXT.__text: 0xc29f8
+950.100.134.0.0
+  __TEXT.__text: 0xc35b4
   __TEXT.__auth_stubs: 0xe40
-  __TEXT.__objc_methlist: 0xb474
-  __TEXT.__const: 0x328
-  __TEXT.__cstring: 0x23677
-  __TEXT.__gcc_except_tab: 0x125c
+  __TEXT.__objc_methlist: 0xb4bc
+  __TEXT.__const: 0x330
+  __TEXT.__cstring: 0x239bc
+  __TEXT.__gcc_except_tab: 0x12b8
   __TEXT.__oslogstring: 0x85d
-  __TEXT.__unwind_info: 0x3680
+  __TEXT.__unwind_info: 0x36a8
   __TEXT.__objc_classname: 0xf77
-  __TEXT.__objc_methname: 0x1a294
+  __TEXT.__objc_methname: 0x1a3d9
   __TEXT.__objc_methtype: 0x3502
-  __TEXT.__objc_stubs: 0x15300
-  __DATA_CONST.__got: 0xe00
-  __DATA_CONST.__const: 0x2a60
+  __TEXT.__objc_stubs: 0x15480
+  __DATA_CONST.__got: 0xe08
+  __DATA_CONST.__const: 0x2ab0
   __DATA_CONST.__objc_classlist: 0x3f8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x60f0
+  __DATA_CONST.__objc_selrefs: 0x6150
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x340
   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0x730
   __AUTH_CONST.__const: 0x7e0
-  __AUTH_CONST.__cfstring: 0x14ae0
-  __AUTH_CONST.__objc_const: 0x16308
+  __AUTH_CONST.__cfstring: 0x14d40
+  __AUTH_CONST.__objc_const: 0x16348
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x1018
-  __DATA.__objc_ivar: 0x9d8
+  __DATA.__objc_ivar: 0x9dc
   __DATA.__data: 0xef8
   __DATA.__bss: 0x108
   __DATA_DIRTY.__objc_data: 0x1798

   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
+  - /System/Library/PrivateFrameworks/Seeding.framework/Seeding
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore
   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0256C3DC-92CA-377E-BEA0-E277B38F7ACD
-  Functions: 4681
-  Symbols:   15511
-  CStrings:  10823
+  UUID: C145BC85-EBDB-3733-A6F1-183AE43D1B0D
+  Functions: 4693
+  Symbols:   15553
+  CStrings:  10879
 
Symbols:
+ -[SUPreferences timeBombOverride]
+ -[SUSHistoryInstalls queryLatestEntry]
+ -[SUSHistoryTracker fetchLatestEntry]
+ -[SUScanner _resetToCustomerAudienceAndRescan]
+ -[SUScanner _shouldResetToCustomerAudienceAfterLongPeriod]
+ -[SUState setTimeBombedDate:]
+ -[SUState timeBombedDate]
+ GCC_except_table86
+ OBJC_IVAR_$_SUState._timeBombedDate
+ ___25-[SUState timeBombedDate]_block_invoke
+ ___29-[SUState setTimeBombedDate:]_block_invoke
+ ___32-[SUInstaller installCompleted:]_block_invoke.435
+ ___32-[SUInstaller installCompleted:]_block_invoke_2.436
+ ___32-[SUInstaller installCompleted:]_block_invoke_3.445
+ ___32-[SUInstaller installCompleted:]_block_invoke_4.446
+ ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.580
+ ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.584
+ ___46-[SUScanner _resetToCustomerAudienceAndRescan]_block_invoke
+ ___46-[SUScanner _resetToCustomerAudienceAndRescan]_block_invoke_2
+ ___58-[SUScanner _shouldResetToCustomerAudienceAfterLongPeriod]_block_invoke
+ ___86-[SUManagerCore updatesDownloadableWithOptions:alternateDownloadOptions:replyHandler:]_block_invoke.550
+ ___block_descriptor_40_e8_32s_e8_v12?0B8ls32l8
+ ___block_descriptor_48_e8_32s40r_e8_v12?0B8lr40l8s32l8
+ ___block_literal_global.341
+ ___block_literal_global.352
+ ___block_literal_global.357
+ ___block_literal_global.362
+ ___block_literal_global.367
+ ___block_literal_global.372
+ ___block_literal_global.377
+ ___block_literal_global.382
+ ___block_literal_global.387
+ ___block_literal_global.392
+ ___block_literal_global.397
+ ___block_literal_global.405
+ ___block_literal_global.410
+ ___block_literal_global.418
+ ___block_literal_global.445
+ ___block_literal_global.447
+ ___block_literal_global.453
+ ___block_literal_global.459
+ ___block_literal_global.481
+ ___block_literal_global.521
+ ___block_literal_global.568
+ ___block_literal_global.590
+ ___block_literal_global.595
+ ___block_literal_global.641
+ ___block_literal_global.646
+ ___block_literal_global.657
+ ___block_literal_global.688
+ ___block_literal_global.692
+ _kSUCoreControllerCleanupLevelKey
+ _objc_msgSend$_resetToCustomerAudienceAndRescan
+ _objc_msgSend$_shouldResetToCustomerAudienceAfterLongPeriod
+ _objc_msgSend$currentDevice
+ _objc_msgSend$fetchLatestEntry
+ _objc_msgSend$isDeviceEnrolledInBetaProgram:completion:
+ _objc_msgSend$lastObject
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$queryLatestEntry
+ _objc_msgSend$setTimeBombedDate:
+ _objc_msgSend$timeBombOverride
+ _objc_msgSend$timeBombedDate
+ _objc_msgSend$unenrollDevice:completion:
- ___32-[SUInstaller installCompleted:]_block_invoke.396
- ___32-[SUInstaller installCompleted:]_block_invoke_2.397
- ___32-[SUInstaller installCompleted:]_block_invoke_3.406
- ___32-[SUInstaller installCompleted:]_block_invoke_4.407
- ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.541
- ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.545
- ___86-[SUManagerCore updatesDownloadableWithOptions:alternateDownloadOptions:replyHandler:]_block_invoke.511
- ___block_literal_global.299
- ___block_literal_global.302
- ___block_literal_global.313
- ___block_literal_global.318
- ___block_literal_global.323
- ___block_literal_global.328
- ___block_literal_global.333
- ___block_literal_global.343
- ___block_literal_global.348
- ___block_literal_global.353
- ___block_literal_global.358
- ___block_literal_global.366
- ___block_literal_global.371
- ___block_literal_global.379
- ___block_literal_global.406
- ___block_literal_global.408
- ___block_literal_global.414
- ___block_literal_global.420
- ___block_literal_global.442
- ___block_literal_global.482
- ___block_literal_global.529
- ___block_literal_global.551
- ___block_literal_global.556
- ___block_literal_global.602
- ___block_literal_global.607
- ___block_literal_global.618
- ___block_literal_global.649
- ___block_literal_global.653
CStrings:
+ "%s: Beta enrolled"
+ "%s: Checking beta enrollment"
+ "%s: Fetching latest install history entry"
+ "%s: Less than one week since last time bomb (%@ seconds ago)"
+ "%s: No available date from history: %@"
+ "%s: No history"
+ "%s: Not beta enrolled"
+ "%s: Seeding framework not available"
+ "-[SUSHistoryTracker fetchLatestEntry]"
+ "-[SUScanner _resetToCustomerAudienceAndRescan]"
+ "-[SUScanner _shouldResetToCustomerAudienceAfterLongPeriod]"
+ "Failed to unenroll device from seed audience"
+ "More than 4 months since last update applied. Resetting to customer audience and rescanning"
+ "Qualifies a beta enrolled device to have customer audience reset immediately instead of after 4 months"
+ "SDBetaManager"
+ "SDDevice"
+ "SUTimeBombOverride"
+ "T@\"NSDate\",&,N,V_timeBombedDate"
+ "TIME OUT waiting for beta enrollment check in %s"
+ "TimeBombedDate"
+ "Timebombing audience"
+ "_resetToCustomerAudienceAndRescan"
+ "_shouldResetToCustomerAudienceAfterLongPeriod"
+ "_timeBombedDate"
+ "com.apple.sus.ddm_manager"
+ "currentDevice"
+ "fetchLatestEntry"
+ "isDeviceEnrolledInBetaProgram:completion:"
+ "lastObject"
+ "numberWithDouble:"
+ "queryLatestEntry"
+ "scan-after-global-settings"
+ "setTimeBombedDate:"
+ "timeBombOverride"
+ "timeBombedDate"
+ "unenrollDevice:completion:"
+ "v12@?0B8"

```
