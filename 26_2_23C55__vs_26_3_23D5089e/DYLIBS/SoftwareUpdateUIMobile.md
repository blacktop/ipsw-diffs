## SoftwareUpdateUIMobile

> `/System/Library/PrivateFrameworks/SoftwareUpdateUIMobile.framework/SoftwareUpdateUIMobile`

```diff

-508.62.1.0.0
+508.80.78.0.0
   __TEXT.__text: 0x6debc
   __TEXT.__auth_stubs: 0xa50
   __TEXT.__objc_methlist: 0x2474
-  __TEXT.__cstring: 0x39ab
+  __TEXT.__cstring: 0x393b
   __TEXT.__gcc_except_tab: 0x4118
   __TEXT.__oslogstring: 0x7425
   __TEXT.__const: 0x3c0

   __TEXT.__objc_methtype: 0x1974
   __TEXT.__objc_stubs: 0x3c40
   __DATA_CONST.__got: 0x858
-  __DATA_CONST.__const: 0x7888
+  __DATA_CONST.__const: 0x7528
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xd8

   __DATA_CONST.__objc_superrefs: 0xe8
   __AUTH_CONST.__auth_got: 0x538
   __AUTH_CONST.__const: 0x1d0
-  __AUTH_CONST.__cfstring: 0x1aa0
+  __AUTH_CONST.__cfstring: 0x1a40
   __AUTH_CONST.__objc_const: 0x7550
   __AUTH.__objc_data: 0xb80
   __AUTH.__data: 0x50

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0D4C536C-9AB4-3056-B97C-67F5764CF9B8
+  UUID: E71B918C-298E-3E99-B015-90004A44CAE6
   Functions: 862
-  Symbols:   6744
-  CStrings:  1966
+  Symbols:   6636
+  CStrings:  1960
 
Symbols:
+ ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.306
+ ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.307
+ ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.308
+ ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.309
+ ___57-[SUUIMobileScanOperation action_QueryUpdatesInfo:error:]_block_invoke.337
+ ___58-[SUUIMobileScanOperation action_ReportScanOutcome:error:]_block_invoke.354
+ ___58-[SUUIMobileUpdateOperation fsmAction_AquireKeybag:error:]_block_invoke.312
+ ___58-[SUUIMobileUpdateOperation fsmAction_AquireKeybag:error:]_block_invoke.313
+ ___60-[SUUIMobileUpdateOperation fsmAction_ScheduleUpdate:error:]_block_invoke.334
+ ___61-[SUUIMobileScanOperation action_QueryCurrentDownload:error:]_block_invoke.332
+ ___64-[SUUIMobileScanOperation action_CheckForAvailableUpdate:error:]_block_invoke.325
+ ___64-[SUUIMobileScanOperation queryRollbackStatus:withReplyHandler:]_block_invoke.421
+ ___64-[SUUIMobileStatefulUIManager autoInstallOperationWasCancelled:]_block_invoke.470
+ ___64-[SUUIMobileStatefulUIManager client:downloadDidFail:withError:]_block_invoke.412
+ ___64-[SUUIMobileStatefulUIManager client:downloadProgressDidChange:]_block_invoke.409
+ ___65-[SUUIMobileScanOperation action_ObserveConcurrentQueries:error:]_block_invoke.342
+ ___65-[SUUIMobileStatefulUIManager handleScanFinishedRollbackApplied:]_block_invoke.472
+ ___65-[SUUIMobileStatefulUIManager handleScanFinishedRollbackApplied:]_block_invoke.473
+ ___68-[SUUIMobileScanOperation checkForMDMRestrictions:withReplyHandler:]_block_invoke.405
+ ___68-[SUUIMobileUpdateOperation fsmAction_InitiateUpdateDownload:error:]_block_invoke.330
+ ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.318
+ ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.319
+ ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.320
+ ___71-[SUUIMobileScanOperation checkIfAutoUpdateScheduled:withReplyHandler:]_block_invoke.425
+ ___71-[SUUIMobileScanOperation checkIsEligibleForRollback:withReplyHandler:]_block_invoke.423
+ ___71-[SUUIMobileStatefulUIManager autoInstallOperationDidExpire:withError:]_block_invoke.471
+ ___72-[SUUIMobileUpdateOperation fsmAction_PresentDownloadConstraints:error:]_block_invoke.327
+ ___72-[SUUIMobileUpdateOperation fsmAction_PresentDownloadConstraints:error:]_block_invoke.328
+ ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.403
+ ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.404
+ ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.336
+ ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.338
+ ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.340
+ ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.342
+ ___77-[SUUIMobileStatefulUIManager client:clearingSpaceForDownload:clearingSpace:]_block_invoke.415
+ ___78-[SUUIMobileScanOperation scanForDeviceEligibleBetaPrograms:withReplyHandler:]_block_invoke.415
- _INTERNAL_PALLAS_SERVER_URL_V2_AUTH
- _MA_PALLAS_AUDIENCE_CUSTOMER_SEASHIP
- _MA_PALLAS_AUDIENCE_INTERNAL_SEASHIP
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
- ___64-[SUUIMobileScanOperation queryRollbackStatus:withReplyHandler:]_block_invoke.430
- ___64-[SUUIMobileStatefulUIManager autoInstallOperationWasCancelled:]_block_invoke.479
- ___64-[SUUIMobileStatefulUIManager client:downloadDidFail:withError:]_block_invoke.421
- ___64-[SUUIMobileStatefulUIManager client:downloadProgressDidChange:]_block_invoke.418
- ___65-[SUUIMobileScanOperation action_ObserveConcurrentQueries:error:]_block_invoke.351
- ___65-[SUUIMobileStatefulUIManager handleScanFinishedRollbackApplied:]_block_invoke.481
- ___65-[SUUIMobileStatefulUIManager handleScanFinishedRollbackApplied:]_block_invoke.482
- ___68-[SUUIMobileScanOperation checkForMDMRestrictions:withReplyHandler:]_block_invoke.414
- ___68-[SUUIMobileUpdateOperation fsmAction_InitiateUpdateDownload:error:]_block_invoke.339
- ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.327
- ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.328
- ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.329
- ___71-[SUUIMobileScanOperation checkIfAutoUpdateScheduled:withReplyHandler:]_block_invoke.434
- ___71-[SUUIMobileScanOperation checkIsEligibleForRollback:withReplyHandler:]_block_invoke.432
- ___71-[SUUIMobileStatefulUIManager autoInstallOperationDidExpire:withError:]_block_invoke.480
- ___72-[SUUIMobileUpdateOperation fsmAction_PresentDownloadConstraints:error:]_block_invoke.336
- ___72-[SUUIMobileUpdateOperation fsmAction_PresentDownloadConstraints:error:]_block_invoke.337
- ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.412
- ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.413
- ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.345
- ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.347
- ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.349
- ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.351
- ___77-[SUUIMobileStatefulUIManager client:clearingSpaceForDownload:clearingSpace:]_block_invoke.424
- ___78-[SUUIMobileScanOperation scanForDeviceEligibleBetaPrograms:withReplyHandler:]_block_invoke.424
CStrings:
- "cd060049-2465-43e3-bbb5-d769a66da2d7"
- "ffc25f86-b83c-4139-b8ad-91131d0e5429"
- "https://gdmf-auth-stg.apple.com/v2/assets"

```
