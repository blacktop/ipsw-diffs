## SoftwareUpdateUIMobile

> `/System/Library/PrivateFrameworks/SoftwareUpdateUIMobile.framework/SoftwareUpdateUIMobile`

```diff

-508.100.172.0.0
-  __TEXT.__text: 0x7887c
+508.100.173.0.0
+  __TEXT.__text: 0x786e4
   __TEXT.__auth_stubs: 0xcd0
   __TEXT.__objc_methlist: 0x259c
-  __TEXT.__cstring: 0x3ee7
+  __TEXT.__cstring: 0x4027
   __TEXT.__oslogstring: 0x7a8c
   __TEXT.__gcc_except_tab: 0x4054
   __TEXT.__const: 0x3c0

   __TEXT.__unwind_info: 0xd08
   __TEXT.__eh_frame: 0x310
   __TEXT.__objc_classname: 0x681
-  __TEXT.__objc_methname: 0x706e
+  __TEXT.__objc_methname: 0x6fdb
   __TEXT.__objc_methtype: 0x19d5
-  __TEXT.__objc_stubs: 0x4300
+  __TEXT.__objc_stubs: 0x4220
   __DATA_CONST.__got: 0x898
-  __DATA_CONST.__const: 0x7598
+  __DATA_CONST.__const: 0x8090
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17a0
+  __DATA_CONST.__objc_selrefs: 0x1768
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xd8
   __AUTH_CONST.__auth_got: 0x678
   __AUTH_CONST.__const: 0x5c8
-  __AUTH_CONST.__cfstring: 0x1c20
+  __AUTH_CONST.__cfstring: 0x1dc0
   __AUTH_CONST.__objc_const: 0x78e8
   __AUTH.__objc_data: 0xb40
   __AUTH.__data: 0x58

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 57634768-9CDE-3A45-A8B4-6D36F8B328E4
+  UUID: 3AD7D5F9-A3AC-391B-9BD4-C8164FD03528
   Functions: 997
-  Symbols:   6776
-  CStrings:  2073
+  Symbols:   7121
+  CStrings:  2092
 
Symbols:
+ _MABrainLoadErrorDomain
+ _MA_FORCE_MOBILEASSETBRAIN_UPDATE_KEY
+ _MA_PALLAS_AUDIENCE_INTERNAL_UNTESTED
+ _MA_PALLAS_AUDIENCE_NAME_CUSTOMER
+ _MA_PALLAS_AUDIENCE_NAME_EXTERNAL_PRE_RELEASE
+ _MA_PALLAS_AUDIENCE_NAME_LIVABLE
+ _MA_PALLAS_AUDIENCE_NAME_SEED_STAGING
+ _MA_PALLAS_AUDIENCE_NAME_UNTESTED
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_CUSTOMER
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_EXT_PRERELEASE
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_LIVABLE
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_SEED_STAGING
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_UNTESTED
+ ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.354
+ ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.355
+ ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.356
+ ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.357
+ ___57-[SUUIMobileScanOperation action_QueryUpdatesInfo:error:]_block_invoke.385
+ ___58-[SUUIMobileScanOperation action_ReportScanOutcome:error:]_block_invoke.402
+ ___58-[SUUIMobileUpdateOperation fsmAction_AquireKeybag:error:]_block_invoke.360
+ ___58-[SUUIMobileUpdateOperation fsmAction_AquireKeybag:error:]_block_invoke.361
+ ___60-[SUUIMobileUpdateOperation fsmAction_ScheduleUpdate:error:]_block_invoke.382
+ ___61-[SUUIMobileScanOperation action_QueryCurrentDownload:error:]_block_invoke.380
+ ___64-[SUUIMobileScanOperation action_CheckForAvailableUpdate:error:]_block_invoke.373
+ ___64-[SUUIMobileScanOperation queryRollbackStatus:withReplyHandler:]_block_invoke.464
+ ___64-[SUUIMobileStatefulUIManager autoInstallOperationWasCancelled:]_block_invoke.521
+ ___64-[SUUIMobileStatefulUIManager client:downloadDidFail:withError:]_block_invoke.460
+ ___64-[SUUIMobileStatefulUIManager client:downloadProgressDidChange:]_block_invoke.457
+ ___65-[SUUIMobileScanOperation action_ObserveConcurrentQueries:error:]_block_invoke.390
+ ___65-[SUUIMobileStatefulUIManager handleScanFinishedRollbackApplied:]_block_invoke.523
+ ___65-[SUUIMobileStatefulUIManager handleScanFinishedRollbackApplied:]_block_invoke.524
+ ___68-[SUUIMobileScanOperation checkForMDMRestrictions:withReplyHandler:]_block_invoke.450
+ ___68-[SUUIMobileUpdateOperation fsmAction_InitiateUpdateDownload:error:]_block_invoke.378
+ ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.366
+ ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.367
+ ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.368
+ ___71-[SUUIMobileScanOperation checkIfAutoUpdateScheduled:withReplyHandler:]_block_invoke.468
+ ___71-[SUUIMobileScanOperation checkIsEligibleForRollback:withReplyHandler:]_block_invoke.466
+ ___71-[SUUIMobileStatefulUIManager autoInstallOperationDidExpire:withError:]_block_invoke.522
+ ___72-[SUUIMobileUpdateOperation fsmAction_PresentDownloadConstraints:error:]_block_invoke.375
+ ___72-[SUUIMobileUpdateOperation fsmAction_PresentDownloadConstraints:error:]_block_invoke.376
+ ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.448
+ ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.449
+ ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.384
+ ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.386
+ ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.388
+ ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.390
+ ___77-[SUUIMobileStatefulUIManager client:clearingSpaceForDownload:clearingSpace:]_block_invoke.463
+ ___78-[SUUIMobileScanOperation scanForDeviceEligibleBetaPrograms:withReplyHandler:]_block_invoke.458
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftSpatial_$_SoftwareUpdateUIMobile
+ _objc_msgSend$userDefaults
- _MA_PALLAS_AUDIENCE_CUSTOMER_XROS
- _MA_PALLAS_AUDIENCE_CUSTOMER_XROS_ALT
- _MA_PALLAS_AUDIENCE_CUSTOMER_XROS_GENERIC
- ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.315
- ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.316
- ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.317
- ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.318
- ___57-[SUUIMobileScanOperation action_QueryUpdatesInfo:error:]_block_invoke.346
- ___58-[SUUIMobileScanOperation action_ReportScanOutcome:error:]_block_invoke.363
- ___58-[SUUIMobileUpdateOperation fsmAction_AquireKeybag:error:]_block_invoke.321
- ___58-[SUUIMobileUpdateOperation fsmAction_AquireKeybag:error:]_block_invoke.322
- ___60-[SUUIMobileUpdateOperation fsmAction_ScheduleUpdate:error:]_block_invoke.343
- ___61-[SUUIMobileScanOperation action_QueryCurrentDownload:error:]_block_invoke.341
- ___64-[SUUIMobileScanOperation action_CheckForAvailableUpdate:error:]_block_invoke.334
- ___64-[SUUIMobileScanOperation queryRollbackStatus:withReplyHandler:]_block_invoke.425
- ___64-[SUUIMobileStatefulUIManager autoInstallOperationWasCancelled:]_block_invoke.482
- ___64-[SUUIMobileStatefulUIManager client:downloadDidFail:withError:]_block_invoke.421
- ___64-[SUUIMobileStatefulUIManager client:downloadProgressDidChange:]_block_invoke.418
- ___65-[SUUIMobileScanOperation action_ObserveConcurrentQueries:error:]_block_invoke.351
- ___65-[SUUIMobileStatefulUIManager handleScanFinishedRollbackApplied:]_block_invoke.484
- ___65-[SUUIMobileStatefulUIManager handleScanFinishedRollbackApplied:]_block_invoke.485
- ___68-[SUUIMobileScanOperation checkForMDMRestrictions:withReplyHandler:]_block_invoke.411
- ___68-[SUUIMobileUpdateOperation fsmAction_InitiateUpdateDownload:error:]_block_invoke.339
- ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.327
- ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.328
- ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.329
- ___71-[SUUIMobileScanOperation checkIfAutoUpdateScheduled:withReplyHandler:]_block_invoke.429
- ___71-[SUUIMobileScanOperation checkIsEligibleForRollback:withReplyHandler:]_block_invoke.427
- ___71-[SUUIMobileStatefulUIManager autoInstallOperationDidExpire:withError:]_block_invoke.483
- ___72-[SUUIMobileUpdateOperation fsmAction_PresentDownloadConstraints:error:]_block_invoke.336
- ___72-[SUUIMobileUpdateOperation fsmAction_PresentDownloadConstraints:error:]_block_invoke.337
- ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.409
- ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.410
- ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.345
- ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.347
- ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.349
- ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.351
- ___77-[SUUIMobileStatefulUIManager client:clearingSpaceForDownload:clearingSpace:]_block_invoke.424
- ___78-[SUUIMobileScanOperation scanForDeviceEligibleBetaPrograms:withReplyHandler:]_block_invoke.419
- _objc_msgSend$dataForEntry:
- _objc_msgSend$dateForEntry:
- _objc_msgSend$numberForEntry:
- _objc_msgSend$setData:forEntry:
- _objc_msgSend$setDate:forEntry:
- _objc_msgSend$setNumber:forEntry:
- _objc_msgSend$setString:forEntry:
- _objc_msgSend$stringForEntry:
Functions:
~ -[SUUIUserDefaults(Mobile) cachedScanResults] : 488 -> 440
~ -[SUUIUserDefaults(Mobile) cachedScanResults:] : 464 -> 404
~ -[SUUIUserDefaults(Mobile) cachedScanResultsTTL] : 476 -> 428
~ -[SUUIUserDefaults(Mobile) cachedScanResultsTTL:] : 452 -> 392
~ -[SUUIUserDefaults(Mobile) cachedFingerprint] : 476 -> 428
~ -[SUUIUserDefaults(Mobile) cachedFingerprint:] : 452 -> 392
~ -[SUUIUserDefaults(Mobile) scanResultsCachingDuration] : 476 -> 428
~ -[SUUIUserDefaults(Mobile) scanResultsCachingDuration:] : 452 -> 392
~ sub_276c4221c -> sub_27781c0b4 : 92 -> 108
~ sub_276c425e4 -> sub_27781c48c : 256 -> 264
CStrings:
+ "245326d2-3ddb-4c46-a08e-aab8b6060a1b"
+ "85ff7a90-361b-42d1-a420-97dee860f018"
+ "97d68e5c-95bb-4136-9aa0-f08964fcc0e1"
+ "ForceMABrainUpdate"
+ "MABrainLoadError"
+ "b1f792b1-0797-48f1-8603-107cefcf1d45"
+ "customer"
+ "ed5a1c1d-2a39-4993-8bcc-f260c4b42868"
+ "external-pre-release"
+ "fb333b76-b463-401f-8899-96d82fc4c598"
+ "livable"
+ "seed-staging"
+ "untested"
+ "userDefaults"
- "dataForEntry:"
- "dateForEntry:"
- "numberForEntry:"
- "setData:forEntry:"
- "setDate:forEntry:"
- "setNumber:forEntry:"
- "setString:forEntry:"
- "stringForEntry:"

```
