## SoftwareUpdateUIMobile

> `/System/Library/PrivateFrameworks/SoftwareUpdateUIMobile.framework/SoftwareUpdateUIMobile`

```diff

-508.40.50.0.0
-  __TEXT.__text: 0x6ceb0
-  __TEXT.__auth_stubs: 0xa70
+508.40.54.0.0
+  __TEXT.__text: 0x6dcf8
+  __TEXT.__auth_stubs: 0xa50
   __TEXT.__objc_methlist: 0x2474
-  __TEXT.__cstring: 0x398b
-  __TEXT.__gcc_except_tab: 0x3ff0
-  __TEXT.__oslogstring: 0x6f55
+  __TEXT.__cstring: 0x393b
+  __TEXT.__gcc_except_tab: 0x4118
+  __TEXT.__oslogstring: 0x7425
   __TEXT.__const: 0x3a0
   __TEXT.__constg_swiftt: 0xfc
   __TEXT.__swift5_typeref: 0x1d0

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_capture: 0x70
-  __TEXT.__unwind_info: 0xba8
-  __TEXT.__eh_frame: 0x1e8
+  __TEXT.__unwind_info: 0xba0
+  __TEXT.__eh_frame: 0x2c8
   __TEXT.__objc_classname: 0x5f8
-  __TEXT.__objc_methname: 0x6a42
+  __TEXT.__objc_methname: 0x6a64
   __TEXT.__objc_methtype: 0x1974
-  __TEXT.__objc_stubs: 0x3c20
-  __DATA_CONST.__got: 0x860
-  __DATA_CONST.__const: 0x75a0
+  __TEXT.__objc_stubs: 0x3c40
+  __DATA_CONST.__got: 0x858
+  __DATA_CONST.__const: 0x7528
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1600
+  __DATA_CONST.__objc_selrefs: 0x1610
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xe8
-  __AUTH_CONST.__auth_got: 0x548
+  __AUTH_CONST.__auth_got: 0x538
   __AUTH_CONST.__const: 0x1d0
-  __AUTH_CONST.__cfstring: 0x1ae0
+  __AUTH_CONST.__cfstring: 0x1a40
   __AUTH_CONST.__objc_const: 0x7550
   __AUTH.__objc_data: 0xb80
   __AUTH.__data: 0x50

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 38F20A31-D25F-31BC-892B-632D28405EDB
-  Functions: 866
-  Symbols:   6648
-  CStrings:  1963
+  UUID: 9535C33E-20D7-333E-AD61-99E380896E52
+  Functions: 862
+  Symbols:   6636
+  CStrings:  1960
 
Symbols:
+ -[SUUIMobileScanOperation concurrentActionsFailed]
+ -[SUUIMobileScanOperation setConcurrentActionsFailed:]
+ GCC_except_table38
+ GCC_except_table39
+ GCC_except_table43
+ GCC_except_table46
+ GCC_except_table48
+ GCC_except_table51
+ GCC_except_table59
+ GCC_except_table60
+ GCC_except_table66
+ GCC_except_table72
+ _OBJC_IVAR_$_SUUIMobileScanOperation._concurrentActionsFailed
+ ___58-[SUUIMobileScanOperation action_ReportScanOutcome:error:]_block_invoke.354
+ ___64-[SUUIMobileScanOperation queryRollbackStatus:withReplyHandler:]_block_invoke.421
+ ___65-[SUUIMobileScanOperation action_ObserveConcurrentQueries:error:]_block_invoke.342
+ ___68-[SUUIMobileScanOperation checkForMDMRestrictions:withReplyHandler:]_block_invoke.405
+ ___71-[SUUIMobileScanOperation checkIfAutoUpdateScheduled:withReplyHandler:]_block_invoke.425
+ ___71-[SUUIMobileScanOperation checkIsEligibleForRollback:withReplyHandler:]_block_invoke.423
+ ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.403
+ ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.404
+ ___78-[SUUIMobileScanOperation scanForDeviceEligibleBetaPrograms:withReplyHandler:]_block_invoke.415
+ ___block_descriptor_72_e8_32s40r48r56w_e5_v8?0lw56l8r40l8s32l8r48l8
+ ___block_descriptor_73_e8_32s40s48s56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ ___os_log_helper_16_2_25_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0
+ ___os_log_helper_16_2_26_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66
+ ___os_log_helper_16_2_27_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_4_0_4_0
+ ___os_log_helper_16_2_27_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_0_8_0
+ ___os_log_helper_16_2_27_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66_8_0
+ ___os_log_helper_16_2_27_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66_8_66
+ ___os_log_helper_16_2_28_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66_8_0_8_66
+ ___os_log_helper_16_2_31_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_64_4_0_8_66_4_0_8_66_4_0
+ ___os_log_helper_16_2_5_8_32_8_66_8_66_8_0_8_66
+ __os_log_debug_impl
+ _dispatch_after
+ _objc_msgSend$allObjects
+ _objc_msgSend$checkForAvailableUpdates:forceScan:
+ _objc_msgSend$checkForUpdatesInBackground:forceScan:
+ _objc_msgSend$currentUpdateOperationType
- -[SUUIMobileScanOperation scheduledConcurrentActionCount]
- -[SUUIMobileScanOperation setScheduledConcurrentActionCount:]
- GCC_except_table37
- GCC_except_table41
- GCC_except_table47
- GCC_except_table52
- GCC_except_table55
- GCC_except_table58
- GCC_except_table65
- GCC_except_table67
- GCC_except_table73
- _OBJC_IVAR_$_SUUIMobileScanOperation._scheduledConcurrentActionCount
- ___58-[SUUIMobileScanOperation action_ReportScanOutcome:error:]_block_invoke.346
- ___64-[SUUIMobileScanOperation queryRollbackStatus:withReplyHandler:]_block_invoke.418
- ___68-[SUUIMobileScanOperation checkForMDMRestrictions:withReplyHandler:]_block_invoke.402
- ___71-[SUUIMobileScanOperation checkIfAutoUpdateScheduled:withReplyHandler:]_block_invoke.422
- ___71-[SUUIMobileScanOperation checkIsEligibleForRollback:withReplyHandler:]_block_invoke.420
- ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.398
- ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.400
- ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke.401
- ___78-[SUUIMobileScanOperation scanForDeviceEligibleBetaPrograms:withReplyHandler:]_block_invoke.412
- ___Block_byref_object_copy_
- ___Block_byref_object_dispose_
- ___block_descriptor_64_e8_32s40r48w_e5_v8?0lw48l8s32l8r40l8
- ___block_descriptor_64_e8_32s40s48r56w_e5_v8?0lw56l8r48l8s32l8s40l8
- ___block_descriptor_72_e8_32s40s48r56w_e20_v20?0B8"NSError"12lw56l8r48l8s32l8s40l8
- ___block_descriptor_80_e8_32s40s48r56w_e5_v8?0lw56l8r48l8s32l8s40l8
- ___block_descriptor_81_e8_32s40s48s56r64w_e5_v8?0lw64l8r56l8s32l8s40l8s48l8
- ___os_log_helper_16_2_24_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0
- ___os_log_helper_16_2_25_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66
- ___os_log_helper_16_2_26_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_4_0_4_0
- ___os_log_helper_16_2_26_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_0_8_0
- ___os_log_helper_16_2_26_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66_8_0
- ___os_log_helper_16_2_26_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66_8_66
- ___os_log_helper_16_2_27_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66_8_0_8_66
- ___os_log_helper_16_2_30_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_64_4_0_8_66_4_0_8_66_4_0
- ___os_log_helper_16_2_6_8_32_8_66_8_66_8_0_8_0_8_66
- ___os_log_helper_16_2_9_8_32_8_66_8_66_8_66_8_0_8_0_8_66_8_66_8_66
- __dispatch_source_type_timer
- _dispatch_resume
- _dispatch_source_cancel
- _dispatch_source_create
- _dispatch_source_set_event_handler
- _dispatch_source_set_timer
- _objc_msgSend$checkForAvailableUpdates
- _objc_msgSend$checkForAvailableUpdates:
- _objc_msgSend$scheduledConcurrentActionCount
CStrings:
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\n"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nBattery level changed: %f -> %f"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nBattery state changed: %d -> %d"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nCan not unschedule an update when the auto-install operation is nil."
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nChanged network type: %@ (%d) -> %{public}@ (%d) (current network type: %{public}@ (%d))"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nClearing space for update %{public}@ (%p): %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nCould not resolve the targeted update from the current download. Skipping on the downloadDidStart event and performing a new scan instead."
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nCould not resolve the targeted update from the current download. Skipping on the downloadProgressDidChange event and performing a new scan instead."
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nDownload of update %{public}@ (%p) failed: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nDownload was invalidated for new updates available: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nFailed to install an update. Error: %{public}@; Descriptor: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nFinished to download an update targeting \"%{public}@\": (%p)"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nRollback already applied, show the user an alert to reboot, and show no available updates."
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nRollback applied. Attempts to ask to reboot the device."
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nScan has finished, but we've been given a nil options. Skipping."
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nScan has finished, triggered by the initiator: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nScan has started on behalf of: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nStarting to download an update targeting \"%{public}@\" (%p)"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nStarting to install an update targeting \"%{public}@\" (%p)"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nUser responded to the rollback reboot request: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\ninstallTonightScheduled called, start to refresh state"
+ "%s [%{public}@|%{public}@]: Concurrent operation \"%{public}@\" has been finished. Success: %{public}@; error: %{public}@. Previous error: %{public}@"
+ "%s [%{public}@|%{public}@]: Concurrent operations completed, but timeout already handled."
+ "%s [%{public}@|%{public}@]: Concurrent operations timed out. Bailing out."
+ "%s [%{public}@|%{public}@]: Concurrent queue is nil, cannot dispatch action %{public}@"
+ "%s [%{public}@|%{public}@]: No concurrent operations are running, proceeding immediately."
+ "%s [%{public}@|%{public}@]: Starting to execute concurrent action: \"%{public}@\""
+ "%s [%{public}@|%{public}@]: Stop resolving %{public}@ because a previous action has already been failed"
+ "%s [%{public}@|%{public}@]: There's a previous operation error (%{public}@). Skipping on the execution of: %{public}@"
+ "%s [%{public}@|%{public}@]: Timeout fired, but concurrent operations already completed."
+ "%s [%{public}@|%{public}@]: Waiting for %lu concurrent operations to complete: %{public}@"
+ "Concurrent operations timed out."
+ "TB,V_concurrentActionsFailed"
+ "_concurrentActionsFailed"
+ "allObjects"
+ "checkForAvailableUpdates:forceScan:"
+ "checkForUpdatesInBackground:forceScan:"
+ "concurrentActionsFailed"
+ "currentUpdateOperationType"
+ "setConcurrentActionsFailed:"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\n"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nBattery level changed: %f -> %f"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nBattery state changed: %d -> %d"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nCan not unschedule an update when the auto-install operation is nil."
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nChanged network type: %@ (%d) -> %{public}@ (%d) (current network type: %{public}@ (%d))"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nClearing space for update %{public}@ (%p): %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nCould not resolve the targeted update from the current download. Skipping on the downloadDidStart event and performing a new scan instead."
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nCould not resolve the targeted update from the current download. Skipping on the downloadProgressDidChange event and performing a new scan instead."
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nDownload of update %{public}@ (%p) failed: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nDownload was invalidated for new updates available: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nFailed to install an update. Error: %{public}@; Descriptor: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nFinished to download an update targeting \"%{public}@\": (%p)"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nRollback already applied, show the user an alert to reboot, and show no available updates."
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nRollback applied. Attempts to ask to reboot the device."
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nScan has finished, but we've been given a nil options. Skipping."
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nScan has finished, triggered by the initiator: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nScan has started on behalf of: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nStarting to download an update targeting \"%{public}@\" (%p)"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nStarting to install an update targeting \"%{public}@\" (%p)"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nUser responded to the rollback reboot request: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\ninstallTonightScheduled called, start to refresh state"
- "%s [%{public}@|%{public}@]: Concurrent operation \"%{public}@\" has been finished [i: %lu|pool: %lu]. Success: %{public}@; error: %{public}@. Previous error: %{public}@"
- "%s [%{public}@|%{public}@]: Starting to execute concurrent action [i: %lu|pool: %lu]: \"%{public}@\""
- "%s [%{public}@|%{public}@]: Stop resolving %{public}@ because a previous action has already failed or timed out"
- "%s [%{public}@|%{public}@]: TIMEOUT: Concurrent action %{public}@ did not complete within %lu seconds - forcing completion"
- "%s [%{public}@|%{public}@]: Waiting for %lu concurrent operations to complete"
- "Action %@ timed out after %lu seconds"
- "DownloadAndInstall"
- "DownloadAndSchedule"
- "DownloadOnly"
- "InstallNow"
- "ScheduleOnly"
- "TQ,V_scheduledConcurrentActionCount"
- "_scheduledConcurrentActionCount"
- "checkForAvailableUpdates"
- "checkForAvailableUpdates:"
- "scheduledConcurrentActionCount"
- "setScheduledConcurrentActionCount:"

```
