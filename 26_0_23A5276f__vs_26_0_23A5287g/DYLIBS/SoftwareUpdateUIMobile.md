## SoftwareUpdateUIMobile

> `/System/Library/PrivateFrameworks/SoftwareUpdateUIMobile.framework/SoftwareUpdateUIMobile`

```diff

-492.0.0.0.5
-  __TEXT.__text: 0x6699c
+508.0.1.502.1
+  __TEXT.__text: 0x66d9c
   __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_methlist: 0x239c
-  __TEXT.__cstring: 0x384e
+  __TEXT.__objc_methlist: 0x23b4
+  __TEXT.__cstring: 0x386e
   __TEXT.__gcc_except_tab: 0x3b20
-  __TEXT.__oslogstring: 0x5d78
+  __TEXT.__oslogstring: 0x5de8
   __TEXT.__const: 0x3a0
   __TEXT.__constg_swiftt: 0xfc
   __TEXT.__swift5_typeref: 0x124

   __TEXT.__unwind_info: 0xad0
   __TEXT.__eh_frame: 0x110
   __TEXT.__objc_classname: 0x5a5
-  __TEXT.__objc_methname: 0x68fd
+  __TEXT.__objc_methname: 0x6910
   __TEXT.__objc_methtype: 0x18b8
-  __TEXT.__objc_stubs: 0x3b40
+  __TEXT.__objc_stubs: 0x3b60
   __DATA_CONST.__got: 0x808
-  __DATA_CONST.__const: 0x6d78
+  __DATA_CONST.__const: 0x6e88
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1590
+  __DATA_CONST.__objc_selrefs: 0x1598
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xe8
   __AUTH_CONST.__auth_got: 0x420
   __AUTH_CONST.__const: 0x48
-  __AUTH_CONST.__cfstring: 0x1aa0
+  __AUTH_CONST.__cfstring: 0x1ac0
   __AUTH_CONST.__objc_const: 0x7118
   __AUTH.__objc_data: 0xb28
   __AUTH.__data: 0x58

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 38400D71-524F-36B0-AA15-203A0C78D349
-  Functions: 797
-  Symbols:   6298
-  CStrings:  1893
+  UUID: 81681B19-23FF-3A91-A5AE-BA17BCFC45AB
+  Functions: 800
+  Symbols:   6339
+  CStrings:  1897
 
Symbols:
+ -[SUUIMobileStatefulUIManager clearPastDownload:]
+ -[SUUIMobileStatefulUIManager clearPastScanResults]
+ GCC_except_table25
+ GCC_except_table32
+ GCC_except_table75
+ _MA_ASSET_PROPERTY_ALLOW_USER_INTERACTION
+ ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.307
+ ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.308
+ ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.309
+ ___57-[SUUIMobileScanOperation action_QueryUpdatesInfo:error:]_block_invoke.326
+ ___58-[SUUIMobileScanOperation action_ReportScanOutcome:error:]_block_invoke.336
+ ___58-[SUUIMobileUpdateOperation fsmAction_AquireKeybag:error:]_block_invoke.312
+ ___58-[SUUIMobileUpdateOperation fsmAction_AquireKeybag:error:]_block_invoke.313
+ ___60-[SUUIMobileUpdateOperation fsmAction_ScheduleUpdate:error:]_block_invoke.334
+ ___61-[SUUIMobileScanOperation action_QueryCurrentDownload:error:]_block_invoke.321
+ ___64-[SUUIMobileScanOperation queryRollbackStatus:withReplyHandler:]_block_invoke.409
+ ___64-[SUUIMobileStatefulUIManager autoInstallOperationWasCancelled:]_block_invoke.470
+ ___64-[SUUIMobileStatefulUIManager client:downloadDidFail:withError:]_block_invoke.412
+ ___64-[SUUIMobileStatefulUIManager client:downloadProgressDidChange:]_block_invoke.409
+ ___65-[SUUIMobileStatefulUIManager handleScanFinishedRollbackApplied:]_block_invoke.472
+ ___65-[SUUIMobileStatefulUIManager handleScanFinishedRollbackApplied:]_block_invoke.473
+ ___68-[SUUIMobileScanOperation checkForMDMRestrictions:withReplyHandler:]_block_invoke.393
+ ___68-[SUUIMobileUpdateOperation fsmAction_InitiateUpdateDownload:error:]_block_invoke.330
+ ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.318
+ ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.319
+ ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.320
+ ___71-[SUUIMobileScanOperation checkIfAutoUpdateScheduled:withReplyHandler:]_block_invoke.413
+ ___71-[SUUIMobileScanOperation checkIsEligibleForRollback:withReplyHandler:]_block_invoke.411
+ ___71-[SUUIMobileStatefulUIManager autoInstallOperationDidExpire:withError:]_block_invoke.471
+ ___72-[SUUIMobileUpdateOperation fsmAction_PresentDownloadConstraints:error:]_block_invoke.327
+ ___72-[SUUIMobileUpdateOperation fsmAction_PresentDownloadConstraints:error:]_block_invoke.328
+ ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.391
+ ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.392
+ ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.336
+ ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.338
+ ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.340
+ ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.342
+ ___77-[SUUIMobileStatefulUIManager client:clearingSpaceForDownload:clearingSpace:]_block_invoke.415
+ ___78-[SUUIMobileScanOperation scanForDeviceEligibleBetaPrograms:withReplyHandler:]_block_invoke.403
+ ___os_log_helper_16_2_4_8_32_8_0_8_66_8_66
+ _objc_msgSend$clearPastDownload:
- GCC_except_table27
- GCC_except_table30
- GCC_except_table38
- GCC_except_table59
- GCC_except_table60
- GCC_except_table72
- ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.303
- ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.304
- ___56-[SUUIMobileUpdateOperation fsmAction_PurgeSpace:error:]_block_invoke.305
- ___57-[SUUIMobileScanOperation action_QueryUpdatesInfo:error:]_block_invoke.323
- ___58-[SUUIMobileScanOperation action_ReportScanOutcome:error:]_block_invoke.333
- ___58-[SUUIMobileUpdateOperation fsmAction_AquireKeybag:error:]_block_invoke.309
- ___58-[SUUIMobileUpdateOperation fsmAction_AquireKeybag:error:]_block_invoke.310
- ___60-[SUUIMobileUpdateOperation fsmAction_ScheduleUpdate:error:]_block_invoke.331
- ___61-[SUUIMobileScanOperation action_QueryCurrentDownload:error:]_block_invoke.318
- ___64-[SUUIMobileScanOperation queryRollbackStatus:withReplyHandler:]_block_invoke.406
- ___64-[SUUIMobileStatefulUIManager autoInstallOperationWasCancelled:]_block_invoke.463
- ___64-[SUUIMobileStatefulUIManager client:downloadDidFail:withError:]_block_invoke.405
- ___64-[SUUIMobileStatefulUIManager client:downloadProgressDidChange:]_block_invoke.402
- ___65-[SUUIMobileStatefulUIManager handleScanFinishedRollbackApplied:]_block_invoke.465
- ___65-[SUUIMobileStatefulUIManager handleScanFinishedRollbackApplied:]_block_invoke.466
- ___68-[SUUIMobileScanOperation checkForMDMRestrictions:withReplyHandler:]_block_invoke.390
- ___68-[SUUIMobileUpdateOperation fsmAction_InitiateUpdateDownload:error:]_block_invoke.327
- ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.315
- ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.316
- ___68-[SUUIMobileUpdateOperation fsmAction_PresentTermsConditions:error:]_block_invoke.317
- ___71-[SUUIMobileScanOperation checkIfAutoUpdateScheduled:withReplyHandler:]_block_invoke.410
- ___71-[SUUIMobileScanOperation checkIsEligibleForRollback:withReplyHandler:]_block_invoke.408
- ___71-[SUUIMobileStatefulUIManager autoInstallOperationDidExpire:withError:]_block_invoke.464
- ___72-[SUUIMobileUpdateOperation fsmAction_PresentDownloadConstraints:error:]_block_invoke.324
- ___72-[SUUIMobileUpdateOperation fsmAction_PresentDownloadConstraints:error:]_block_invoke.325
- ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.386
- ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.388
- ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.333
- ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.335
- ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.337
- ___74-[SUUIMobileUpdateOperation fsmAction_ReportUpdateOperationOutcome:error:]_block_invoke.339
- ___77-[SUUIMobileStatefulUIManager client:clearingSpaceForDownload:clearingSpace:]_block_invoke.408
- ___78-[SUUIMobileScanOperation scanForDeviceEligibleBetaPrograms:withReplyHandler:]_block_invoke.400
CStrings:
+ "%s [%p]: Cleaning up the manager state after a download failure.\n\t- fullScan: %{public}@\n\t- bgScan: %{public}@"
+ "%s [%{public}@|%{public}@]: Assigning rollback descriptor %@ (%p) instead of %@ (%p)"
+ "%s [%{public}@|%{public}@]: Ignoring request to call dispatch_group_leave for the action %{public}@, as the running actions set has no entry for this action anymore."
+ "_AllowUserInteraction"
+ "clearPastDownload:"
- "%s [%{public}@|%{public}@]: Assigning roolback descriptor %@ (%p) instead of %@ (%p)"
- "%s [%{public}@|%{public}@]: Ignoring request to call dispatch_group_leave for the action %{public}@, as the runnig actions set has no entry for this action anymore."

```
