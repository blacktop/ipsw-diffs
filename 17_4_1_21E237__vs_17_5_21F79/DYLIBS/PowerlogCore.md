## PowerlogCore

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`

```diff

-1851.102.4.0.0
-  __TEXT.__text: 0xd4344
-  __TEXT.__auth_stubs: 0x1960
-  __TEXT.__objc_methlist: 0x7db0
-  __TEXT.__const: 0x14b8
-  __TEXT.__cstring: 0x33d21
+1851.120.59.0.0
+  __TEXT.__text: 0xd5910
+  __TEXT.__auth_stubs: 0x1990
+  __TEXT.__objc_methlist: 0x7de8
+  __TEXT.__const: 0x15a8
+  __TEXT.__cstring: 0x34159
   __TEXT.__gcc_except_tab: 0x21b0
-  __TEXT.__oslogstring: 0x6108
-  __TEXT.__unwind_info: 0x2acc
+  __TEXT.__oslogstring: 0x60de
+  __TEXT.__unwind_info: 0x2af0
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x827
-  __TEXT.__objc_methname: 0x11f0a
+  __TEXT.__objc_methname: 0x11f90
   __TEXT.__objc_methtype: 0x173a
-  __TEXT.__objc_stubs: 0xeb00
+  __TEXT.__objc_stubs: 0xeb80
   __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0x23c8
+  __DATA_CONST.__const: 0x23f8
   __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_nlclslist: 0x80
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x6528
-  __DATA_CONST.__objc_selrefs: 0x4b48
+  __DATA_CONST.__objc_selrefs: 0x4b70
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_classrefs: 0x3f0
   __DATA_CONST.__objc_superrefs: 0x290
-  __DATA_CONST.__objc_arraydata: 0x31330
-  __AUTH_CONST.__const: 0x1c00
-  __AUTH_CONST.__cfstring: 0x4fa80
+  __DATA_CONST.__objc_arraydata: 0x31b00
+  __AUTH_CONST.__const: 0x1be0
+  __AUTH_CONST.__cfstring: 0x50220
   __AUTH_CONST.__objc_const: 0x29c0
-  __AUTH_CONST.__objc_intobj: 0x4320
-  __AUTH_CONST.__objc_doubleobj: 0xcb0
-  __AUTH_CONST.__objc_arrayobj: 0xf18
-  __AUTH_CONST.__objc_dictobj: 0xc8f0
-  __AUTH_CONST.__auth_got: 0xcc8
+  __AUTH_CONST.__objc_intobj: 0x4380
+  __AUTH_CONST.__objc_doubleobj: 0xd10
+  __AUTH_CONST.__objc_arrayobj: 0xf30
+  __AUTH_CONST.__objc_dictobj: 0xca80
+  __AUTH_CONST.__auth_got: 0xce0
   __AUTH.__objc_data: 0x410
   __DATA.__objc_ivar: 0x604
-  __DATA.__data: 0x438
-  __DATA.__bss: 0x1bd9
+  __DATA.__data: 0x458
+  __DATA.__bss: 0x1bb1
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x1a40
   __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__bss: 0xa88
+  __DATA_DIRTY.__bss: 0xab0
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 5E28F1F3-7AD4-39BA-B50A-E22D90B3B5E4
-  Functions: 4563
-  Symbols:   14776
-  CStrings:  25020
+  UUID: 82B2F678-1CF9-36A6-8514-52E5E5101F06
+  Functions: 4572
+  Symbols:   14809
+  CStrings:  25148
 
Symbols:
+ +[PLUtilities cleanLaunchdApplicationMacOS:]
+ +[PLUtilities cleanLaunchdName:]
+ +[PLUtilities cleanLaunchdName:].cold.1
+ -[PLSubmissionFileXC copyDatabaseToPath:]
+ -[PLSubmissionFileXC userActionCountForConnection:]
+ -[PLSubmissionFileXC xcodeVersionFromUserActions]
+ -[PLSubmissionFileXC xcodeVersionFromUserActions].cold.1
+ -[PLSubmissionFileXC xcodeVersionFromUserActions].cold.2
+ -[PLTimeReferenceKernel currentTime].cold.3
+ _AnalyticsSendEvent
+ ___21-[PLTimeManager init]_block_invoke.23
+ ___21-[PLTimeManager init]_block_invoke.23.cold.1
+ ___27-[PLArchiveManager migrate]_block_invoke.412
+ ___35-[PLArchiveManager migrateArchive:]_block_invoke.396
+ ___36-[PLTimeReferenceKernel currentTime]_block_invoke.13
+ ___36-[PLTimeReferenceKernel currentTime]_block_invoke.22
+ ___38-[PLArchiveManager trimCleanEnergyLog]_block_invoke.373
+ ___46-[PLArchiveManager trimExtendedPersistenceLog]_block_invoke.374
+ ___77-[PLTimeManager bucketTimeStampForDate:withTimeReference:withBucketInterval:]_block_invoke.54
+ ___77-[PLTimeManager bucketTimeStampForDate:withTimeReference:withBucketInterval:]_block_invoke.60
+ ___77-[PLTimeManager bucketTimeStampForDate:withTimeReference:withBucketInterval:]_block_invoke.66
+ ___block_literal_global.152
+ ___block_literal_global.188
+ ___block_literal_global.205
+ ___block_literal_global.210
+ ___block_literal_global.27
+ ___block_literal_global.334
+ ___block_literal_global.359
+ ___block_literal_global.371
+ ___block_literal_global.389
+ ___block_literal_global.391
+ ___block_literal_global.396
+ ___block_literal_global.403
+ ___block_literal_global.405
+ ___block_literal_global.412
+ ___block_literal_global.415
+ ___block_literal_global.418
+ ___block_literal_global.426
+ ___block_literal_global.431
+ ___block_literal_global.448
+ ___block_literal_global.457
+ ___block_literal_global.472
+ ___block_literal_global.482
+ ___block_literal_global.484
+ ___block_literal_global.486
+ ___block_literal_global.496
+ ___block_literal_global.499
+ ___block_literal_global.501
+ ___block_literal_global.503
+ ___block_literal_global.505
+ ___block_literal_global.507
+ ___block_literal_global.509
+ ___block_literal_global.511
+ ___block_literal_global.513
+ ___block_literal_global.521
+ ___block_literal_global.523
+ ___block_literal_global.525
+ ___block_literal_global.527
+ ___block_literal_global.529
+ ___block_literal_global.606
+ ___block_literal_global.665
+ ___block_literal_global.667
+ ___block_literal_global.678
+ ___block_literal_global.683
+ ___block_literal_global.696
+ ___block_literal_global.883
+ ___stringIsUUID_block_invoke
+ __unnamed_array_storage.347
+ _bucketTimeStampForDate:withTimeReference:withBucketInterval:.classDebugEnabled.53
+ _bucketTimeStampForDate:withTimeReference:withBucketInterval:.classDebugEnabled.59
+ _bucketTimeStampForDate:withTimeReference:withBucketInterval:.classDebugEnabled.65
+ _bucketTimeStampForDate:withTimeReference:withBucketInterval:.defaultOnce.52
+ _bucketTimeStampForDate:withTimeReference:withBucketInterval:.defaultOnce.58
+ _bucketTimeStampForDate:withTimeReference:withBucketInterval:.defaultOnce.64
+ _currentTime.classDebugEnabled.21
+ _currentTime.defaultOnce.20
+ _guiPrefix
+ _macAppPrefix
+ _migrateArchive:.classDebugEnabled.395
+ _migrateArchive:.defaultOnce.394
+ _objc_msgSend$characterSetWithCharactersInString:
+ _objc_msgSend$cleanLaunchdApplicationMacOS:
+ _objc_msgSend$isSupersetOfSet:
+ _objc_msgSend$userActionCountForConnection:
+ _objc_msgSend$xcodeVersionFromUserActions
+ _pidPrefix
+ _sqlite3_column_blob
+ _sqlite3_column_bytes
+ _stringIsUUID.hexChars
+ _stringIsUUID.onceToken
+ _systemPrefix
+ _uikitAppPrefix
+ _userPrefix
- -[PLTimeReferenceKernel initializeOffsetWithEntries:].cold.1
- -[PLTimeReferenceKernel quarantineWithExitReason:]
- _PLLogTimeManager
- _PLLogTimeManager._logHandle
- _PLLogTimeManager.onceToken
- ___21-[PLTimeManager init]_block_invoke.25
- ___21-[PLTimeManager init]_block_invoke.25.cold.1
- ___27-[PLArchiveManager migrate]_block_invoke.406
- ___35-[PLArchiveManager migrateArchive:]_block_invoke.390
- ___37+[PLUtilities exitWithReason:action:]_block_invoke_9
- ___38-[PLArchiveManager trimCleanEnergyLog]_block_invoke.367
- ___46-[PLArchiveManager trimExtendedPersistenceLog]_block_invoke.368
- ___77-[PLTimeManager bucketTimeStampForDate:withTimeReference:withBucketInterval:]_block_invoke.56
- ___77-[PLTimeManager bucketTimeStampForDate:withTimeReference:withBucketInterval:]_block_invoke.62
- ___77-[PLTimeManager bucketTimeStampForDate:withTimeReference:withBucketInterval:]_block_invoke.68
- ___PLLogTimeManager_block_invoke
- ___block_literal_global.14
- ___block_literal_global.148
- ___block_literal_global.184
- ___block_literal_global.191
- ___block_literal_global.201
- ___block_literal_global.206
- ___block_literal_global.321
- ___block_literal_global.328
- ___block_literal_global.365
- ___block_literal_global.377
- ___block_literal_global.407
- ___block_literal_global.414
- ___block_literal_global.419
- ___block_literal_global.423
- ___block_literal_global.427
- ___block_literal_global.430
- ___block_literal_global.433
- ___block_literal_global.435
- ___block_literal_global.436
- ___block_literal_global.439
- ___block_literal_global.444
- ___block_literal_global.445
- ___block_literal_global.449
- ___block_literal_global.450
- ___block_literal_global.452
- ___block_literal_global.454
- ___block_literal_global.458
- ___block_literal_global.459
- ___block_literal_global.464
- ___block_literal_global.466
- ___block_literal_global.469
- ___block_literal_global.471
- ___block_literal_global.473
- ___block_literal_global.475
- ___block_literal_global.479
- ___block_literal_global.481
- ___block_literal_global.489
- ___block_literal_global.493
- ___block_literal_global.495
- ___block_literal_global.515
- ___block_literal_global.603
- ___block_literal_global.662
- ___block_literal_global.664
- ___block_literal_global.675
- ___block_literal_global.680
- ___block_literal_global.684
- __unnamed_array_storage.326
- __unnamed_array_storage.327
- __unnamed_array_storage.341
- __unnamed_array_storage.350
- __unnamed_array_storage.373
- _bucketTimeStampForDate:withTimeReference:withBucketInterval:.classDebugEnabled.55
- _bucketTimeStampForDate:withTimeReference:withBucketInterval:.classDebugEnabled.61
- _bucketTimeStampForDate:withTimeReference:withBucketInterval:.classDebugEnabled.67
- _bucketTimeStampForDate:withTimeReference:withBucketInterval:.defaultOnce.54
- _bucketTimeStampForDate:withTimeReference:withBucketInterval:.defaultOnce.60
- _bucketTimeStampForDate:withTimeReference:withBucketInterval:.defaultOnce.66
- _migrateArchive:.classDebugEnabled.389
- _migrateArchive:.defaultOnce.388
- _objc_msgSend$quarantineWithExitReason:
CStrings:
+ "-[PLTimeReferenceKernel currentTime]"
+ "/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLTimeReferenceClasses/PLTimeReferenceKernel.m"
+ "0123456789ABCDEFabcdef"
+ "1002055"
+ "1002056"
+ "1006025"
+ "1006028"
+ "1006029"
+ "BroadcastRXDuration"
+ "DeviceCoverGlassCoating"
+ "IBSSRXDuration"
+ "J507"
+ "J508"
+ "J537"
+ "J538"
+ "J717"
+ "J718"
+ "J720"
+ "J721"
+ "MBSSRXDuration"
+ "MulticastRXDuration"
+ "No Xcode Version found in User Action table"
+ "OBSSRXDuration"
+ "PDEP"
+ "PDLP"
+ "PLSMCAgent_EventBackward_DisplayPowerKeys"
+ "PerformanceMetrics"
+ "PerformanceMetrics_WorkflowResponsiveness_1_2"
+ "PerformanceMetrics_WorkflowResponsiveness_1_2_Dynamic"
+ "ResetDataCorruption"
+ "ResetDataHardFault"
+ "ResetDataSwWatchDog"
+ "SBAP"
+ "SELECT DISTINCT %@ FROM %@ ORDER BY timestamp DESC limit 1"
+ "TAOC"
+ "TAOI"
+ "TIOP"
+ "TTDb"
+ "TVB1"
+ "TVB2"
+ "TVB3"
+ "TVB4"
+ "TVBL"
+ "UIKitApplication:"
+ "UserActionCount_System"
+ "UserActionCount_Upload"
+ "WorkflowResponsiveness"
+ "Xcode Version = %f"
+ "application."
+ "characterSetWithCharactersInString:"
+ "cleanLaunchdApplicationMacOS:"
+ "cleanLaunchdName:"
+ "cleanLaunchdName: Unknown launchd service name: %@"
+ "com.apple.perfpowerservices.submission.xcode_sizes"
+ "endTimeMachContNs"
+ "ftD0"
+ "gui/"
+ "has_user_actions"
+ "isSupersetOfSet:"
+ "overallEndTime"
+ "overallStartTime"
+ "pid/"
+ "preparation_stage"
+ "shm_size"
+ "signpostName"
+ "startTimeMachContNs"
+ "system/"
+ "user/"
+ "userActionCountForConnection:"
+ "user_action_row_count"
+ "wal_size"
+ "workflowName"
+ "xcodeVersionFromUserActions"
+ "xcsql_size"
- "%@KernelTimePowerlog_%f%@"
- "com.apple.power.error.kernelTimeDB"
- "kPLExitReasonDescKernelTime"
- "kernelTimeDB"
- "monotonicTimeWentBackwards=%d"
- "quarantineWithExitReason:"

```
