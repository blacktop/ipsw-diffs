## SoftwareUpdateUIMobile

> `/System/Library/PrivateFrameworks/SoftwareUpdateUIMobile.framework/SoftwareUpdateUIMobile`

```diff

-  __TEXT.__text: 0x7d79c
-  __TEXT.__objc_methlist: 0x26c4
-  __TEXT.__cstring: 0x46c7
-  __TEXT.__oslogstring: 0x8500
-  __TEXT.__gcc_except_tab: 0x1978
+  __TEXT.__text: 0x75d1c
+  __TEXT.__objc_methlist: 0x27d4
+  __TEXT.__cstring: 0x4727
+  __TEXT.__oslogstring: 0x77f0
+  __TEXT.__gcc_except_tab: 0x11b4
   __TEXT.__const: 0x3f0
   __TEXT.__constg_swiftt: 0xf0
   __TEXT.__swift5_typeref: 0x22d

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8ef8
-  __DATA_CONST.__objc_classlist: 0x100
+  __DATA_CONST.__const: 0x9330
+  __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1848
+  __DATA_CONST.__objc_selrefs: 0x1878
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xd8
-  __DATA_CONST.__got: 0x8f8
+  __DATA_CONST.__got: 0x8e0
   __AUTH_CONST.__const: 0x988
-  __AUTH_CONST.__cfstring: 0x1f60
-  __AUTH_CONST.__objc_const: 0x7b78
-  __AUTH_CONST.__auth_got: 0x708
-  __AUTH.__objc_data: 0xb50
+  __AUTH_CONST.__cfstring: 0x1fe0
+  __AUTH_CONST.__objc_const: 0x7f30
+  __AUTH_CONST.__auth_got: 0x6d0
+  __AUTH.__objc_data: 0xc90
   __AUTH.__data: 0x58
-  __DATA.__objc_ivar: 0x1fc
-  __DATA.__data: 0xd90
+  __DATA.__objc_ivar: 0x214
+  __DATA.__data: 0xda0
   __DATA.__bss: 0x310
   __DATA.__common: 0x40
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1129
-  Symbols:   7793
-  CStrings:  937
+  Functions: 1148
+  Symbols:   8002
+  CStrings:  919
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH.__data : content changed
Symbols:
+ +[SUUIMobileScanAutoUpdateResult resultWithScheduled:autoInstallOperation:]
+ +[SUUIMobileScanBetaResult resultWithSeedingDevice:betaPrograms:enrolledBetaProgram:]
+ +[SUUIMobileScanMDMResult resultWithPathRestriction:isDelayingUpdate:]
+ +[SUUIMobileScanRollbackStatusResult resultWithRollingBack:rollbackDescriptor:]
+ -[SUUIMobileScanAutoUpdateResult .cxx_destruct]
+ -[SUUIMobileScanAutoUpdateResult autoInstallOperation]
+ -[SUUIMobileScanAutoUpdateResult isAutoUpdateScheduled]
+ -[SUUIMobileScanBetaResult .cxx_destruct]
+ -[SUUIMobileScanBetaResult betaPrograms]
+ -[SUUIMobileScanBetaResult enrolledBetaProgram]
+ -[SUUIMobileScanBetaResult seedingDevice]
+ -[SUUIMobileScanMDMResult isDelayingUpdate]
+ -[SUUIMobileScanMDMResult pathRestriction]
+ -[SUUIMobileScanOperation checkForMDMRestrictionsWithReplyHandler:]
+ -[SUUIMobileScanOperation checkIfAutoUpdateScheduledWithReplyHandler:]
+ -[SUUIMobileScanOperation checkIsEligibleForRollbackWithReplyHandler:]
+ -[SUUIMobileScanOperation metadataGroup]
+ -[SUUIMobileScanOperation queryDDMDeclarationWithReplyHandler:]
+ -[SUUIMobileScanOperation queryRollbackStatusWithReplyHandler:]
+ -[SUUIMobileScanOperation scheduleAutoUpdateScheduledTask]
+ -[SUUIMobileScanOperation selfRetain]
+ -[SUUIMobileScanOperation setMetadataGroup:]
+ -[SUUIMobileScanOperation setSelfRetain:]
+ -[SUUIMobileScanOperationParam applyConcurrentResults:]
+ -[SUUIMobileScanRollbackStatusResult .cxx_destruct]
+ -[SUUIMobileScanRollbackStatusResult rollbackDescriptor]
+ -[SUUIMobileScanRollbackStatusResult rollingBack]
+ -[SUUIMobileStatefulError rebootRequired]
+ GCC_except_table24
+ GCC_except_table36
+ GCC_except_table61
+ GCC_except_table73
+ _OBJC_CLASS_$_SUUIMobileScanAutoUpdateResult
+ _OBJC_CLASS_$_SUUIMobileScanBetaResult
+ _OBJC_CLASS_$_SUUIMobileScanMDMResult
+ _OBJC_CLASS_$_SUUIMobileScanRollbackStatusResult
+ _OBJC_CLASS_$_SUUITaskGroup
+ _OBJC_IVAR_$_SUUIMobileScanAutoUpdateResult._autoInstallOperation
+ _OBJC_IVAR_$_SUUIMobileScanAutoUpdateResult._isAutoUpdateScheduled
+ _OBJC_IVAR_$_SUUIMobileScanBetaResult._betaPrograms
+ _OBJC_IVAR_$_SUUIMobileScanBetaResult._enrolledBetaProgram
+ _OBJC_IVAR_$_SUUIMobileScanBetaResult._seedingDevice
+ _OBJC_IVAR_$_SUUIMobileScanMDMResult._isDelayingUpdate
+ _OBJC_IVAR_$_SUUIMobileScanMDMResult._pathRestriction
+ _OBJC_IVAR_$_SUUIMobileScanOperation._metadataGroup
+ _OBJC_IVAR_$_SUUIMobileScanOperation._selfRetain
+ _OBJC_IVAR_$_SUUIMobileScanRollbackStatusResult._rollbackDescriptor
+ _OBJC_IVAR_$_SUUIMobileScanRollbackStatusResult._rollingBack
+ _OBJC_METACLASS_$_SUUIMobileScanAutoUpdateResult
+ _OBJC_METACLASS_$_SUUIMobileScanBetaResult
+ _OBJC_METACLASS_$_SUUIMobileScanMDMResult
+ _OBJC_METACLASS_$_SUUIMobileScanRollbackStatusResult
+ __OBJC_$_CLASS_METHODS_SUUIMobileScanAutoUpdateResult
+ __OBJC_$_CLASS_METHODS_SUUIMobileScanBetaResult
+ __OBJC_$_CLASS_METHODS_SUUIMobileScanMDMResult
+ __OBJC_$_CLASS_METHODS_SUUIMobileScanRollbackStatusResult
+ __OBJC_$_INSTANCE_METHODS_SUUIMobileScanAutoUpdateResult
+ __OBJC_$_INSTANCE_METHODS_SUUIMobileScanBetaResult
+ __OBJC_$_INSTANCE_METHODS_SUUIMobileScanMDMResult
+ __OBJC_$_INSTANCE_METHODS_SUUIMobileScanRollbackStatusResult
+ __OBJC_$_INSTANCE_VARIABLES_SUUIMobileScanAutoUpdateResult
+ __OBJC_$_INSTANCE_VARIABLES_SUUIMobileScanBetaResult
+ __OBJC_$_INSTANCE_VARIABLES_SUUIMobileScanMDMResult
+ __OBJC_$_INSTANCE_VARIABLES_SUUIMobileScanRollbackStatusResult
+ __OBJC_$_PROP_LIST_SUUIMobileScanAutoUpdateResult
+ __OBJC_$_PROP_LIST_SUUIMobileScanBetaResult
+ __OBJC_$_PROP_LIST_SUUIMobileScanMDMResult
+ __OBJC_$_PROP_LIST_SUUIMobileScanRollbackStatusResult
+ __OBJC_CLASS_RO_$_SUUIMobileScanAutoUpdateResult
+ __OBJC_CLASS_RO_$_SUUIMobileScanBetaResult
+ __OBJC_CLASS_RO_$_SUUIMobileScanMDMResult
+ __OBJC_CLASS_RO_$_SUUIMobileScanRollbackStatusResult
+ __OBJC_METACLASS_RO_$_SUUIMobileScanAutoUpdateResult
+ __OBJC_METACLASS_RO_$_SUUIMobileScanBetaResult
+ __OBJC_METACLASS_RO_$_SUUIMobileScanMDMResult
+ __OBJC_METACLASS_RO_$_SUUIMobileScanRollbackStatusResult
+ ___44-[SUUIMobileScanOperation invalidateMachine]_block_invoke
+ ___58-[SUUIMobileScanOperation scheduleAutoUpdateScheduledTask]_block_invoke
+ ___62-[SUUIMobileScanOperation action_QueryFullScanMetadata:error:]_block_invoke
+ ___62-[SUUIMobileScanOperation action_QueryFullScanMetadata:error:]_block_invoke_2
+ ___63-[SUUIMobileScanOperation queryDDMDeclarationWithReplyHandler:]_block_invoke
+ ___63-[SUUIMobileScanOperation queryRollbackStatusWithReplyHandler:]_block_invoke
+ ___67-[SUUIMobileScanOperation checkForMDMRestrictionsWithReplyHandler:]_block_invoke
+ ___70-[SUUIMobileScanOperation checkIfAutoUpdateScheduledWithReplyHandler:]_block_invoke
+ ___70-[SUUIMobileScanOperation checkIsEligibleForRollbackWithReplyHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e42_v24?0"SUCoreDDMDeclaration"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e18_v16?0"SDDevice"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e20_v24?0Q8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e42_v24?0"SURollbackDescriptor"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e45_v28?0B8"SURollbackDescriptor"12"NSError"20ls32l8s40l8
+ ___block_descriptor_48_e8_32w_e28_v24?08?<v?"NSError">16lw32l8
+ ___block_descriptor_49_e8_32s40bs_e44_v24?0"SUAutoInstallOperation"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e20_v24?0"NSArray"8q16ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40w_e28_v24?08?<v?"NSError">16lw40l8s32l8
+ ___block_descriptor_64_e8_32s40r48w_e29_v16?0"SUUITaskGroupResult"8lw48l8s32l8r40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e23_v16?0"SDBetaProgram"8ls32l8s56l8s40l8s48l8
+ ___os_log_helper_16_2_6_8_32_8_66_8_66_8_0_8_66_8_66
+ _kSUUIMobileScanTaskAutoUpdateScheduled
+ _kSUUIMobileScanTaskBetaPrograms
+ _kSUUIMobileScanTaskDDMDeclaration
+ _kSUUIMobileScanTaskMDMRestrictions
+ _kSUUIMobileScanTaskRollbackEligibility
+ _kSUUIMobileScanTaskRollbackStatus
+ _objc_msgSend$addTaskNamed:task:
+ _objc_msgSend$applyConcurrentResults:
+ _objc_msgSend$checkForAvailableUpdatesWithRetriesCount:forceScan:
+ _objc_msgSend$checkForBetaPrograms:withReplyHandler:
+ _objc_msgSend$checkForMDMRestrictionsWithReplyHandler:
+ _objc_msgSend$checkIfAutoUpdateScheduledWithReplyHandler:
+ _objc_msgSend$checkIsEligibleForRollbackWithReplyHandler:
+ _objc_msgSend$finishedTaskNames
+ _objc_msgSend$firstError
+ _objc_msgSend$initWithIdentifier:timeout:policy:
+ _objc_msgSend$metadataGroup
+ _objc_msgSend$outcome
+ _objc_msgSend$pathRestriction
+ _objc_msgSend$queryDDMDeclarationWithReplyHandler:
+ _objc_msgSend$queryRollbackStatusWithReplyHandler:
+ _objc_msgSend$resultForTaskNamed:
+ _objc_msgSend$resultWithPathRestriction:isDelayingUpdate:
+ _objc_msgSend$resultWithRollingBack:rollbackDescriptor:
+ _objc_msgSend$resultWithScheduled:autoInstallOperation:
+ _objc_msgSend$resultWithSeedingDevice:betaPrograms:enrolledBetaProgram:
+ _objc_msgSend$rollingBack
+ _objc_msgSend$scheduleAutoUpdateScheduledTask
+ _objc_msgSend$seedingDevice
+ _objc_msgSend$selfRetain
+ _objc_msgSend$setMetadataGroup:
+ _objc_msgSend$setSelfRetain:
+ _objc_msgSend$start
+ _objc_msgSend$unfinishedTaskNames
+ _objc_msgSend$waitForResult:
- -[SUUIMobileScanOperation checkForMDMRestrictions:withReplyHandler:]
- -[SUUIMobileScanOperation checkIfAutoUpdateScheduled:withReplyHandler:]
- -[SUUIMobileScanOperation checkIsEligibleForRollback:withReplyHandler:]
- -[SUUIMobileScanOperation concurrentActionsFailed]
- -[SUUIMobileScanOperation concurrentQueue]
- -[SUUIMobileScanOperation concurrentRunningActionsNames]
- -[SUUIMobileScanOperation queryDDMDeclaration:withReplyHandler:]
- -[SUUIMobileScanOperation queryRollbackStatus:withReplyHandler:]
- -[SUUIMobileScanOperation scanGroup]
- -[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]
- -[SUUIMobileScanOperation setConcurrentActionsFailed:]
- -[SUUIMobileScanOperation setConcurrentQueue:]
- -[SUUIMobileScanOperation setConcurrentRunningActionsNames:]
- -[SUUIMobileScanOperation setScanGroup:]
- GCC_except_table14
- GCC_except_table23
- GCC_except_table29
- GCC_except_table30
- GCC_except_table35
- GCC_except_table55
- GCC_except_table65
- GCC_except_table66
- GCC_except_table67
- _OBJC_CLASS_$_NSInvocation
- _OBJC_CLASS_$_NSMutableSet
- _OBJC_IVAR_$_SUUIMobileScanOperation._concurrentActionsFailed
- _OBJC_IVAR_$_SUUIMobileScanOperation._concurrentLock
- _OBJC_IVAR_$_SUUIMobileScanOperation._concurrentQueue
- _OBJC_IVAR_$_SUUIMobileScanOperation._concurrentRunningActionsNames
- _OBJC_IVAR_$_SUUIMobileScanOperation._scanGroup
- ___64-[SUUIMobileScanOperation queryDDMDeclaration:withReplyHandler:]_block_invoke
- ___64-[SUUIMobileScanOperation queryRollbackStatus:withReplyHandler:]_block_invoke
- ___68-[SUUIMobileScanOperation checkForMDMRestrictions:withReplyHandler:]_block_invoke
- ___71-[SUUIMobileScanOperation checkIfAutoUpdateScheduled:withReplyHandler:]_block_invoke
- ___71-[SUUIMobileScanOperation checkIsEligibleForRollback:withReplyHandler:]_block_invoke
- ___74-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke
- ___block_descriptor_48_e8_32s40bs_e42_v24?0"SUCoreDDMDeclaration"8"NSError"16ls40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e18_v16?0"SDDevice"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48bs_e20_v20?0B8"NSError"12ls32l8s48l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e20_v24?0"NSArray"8q16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48bs_e20_v24?0Q8"NSError"16ls32l8s48l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e23_v16?0"SDBetaProgram"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48bs_e42_v24?0"SURollbackDescriptor"8"NSError"16ls32l8s48l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e45_v28?0B8"SURollbackDescriptor"12"NSError"20ls32l8s48l8s40l8
- ___block_descriptor_57_e8_32s40s48bs_e44_v24?0"SUAutoInstallOperation"8"NSError"16ls32l8s48l8s40l8
- ___block_descriptor_64_e8_32s40s48bs_e20_v20?0B8"NSError"12ls32l8s48l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40r48r56w_e5_v8?0lw56l8r40l8s32l8r48l8
- ___block_descriptor_73_e8_32s40s48s56w_e5_v8?0lw56l8s32l8s40l8s48l8
- ___os_log_helper_16_2_5_8_32_8_66_8_66_8_0_8_66
- ___os_log_helper_16_2_7_8_32_8_66_8_66_8_64_8_0_8_64_8_0
- __dispatch_queue_attr_concurrent
- _dispatch_after
- _dispatch_barrier_async
- _dispatch_group_create
- _dispatch_group_enter
- _dispatch_group_leave
- _dispatch_group_notify
- _dispatch_time
- _kSU_E_FullScanNoUpdateAvailable
- _objc_msgSend$allObjects
- _objc_msgSend$checkForAvailableUpdatesWithRetriesCount:
- _objc_msgSend$concurrentQueue
- _objc_msgSend$invocationWithMethodSignature:
- _objc_msgSend$invoke
- _objc_msgSend$methodSignatureForSelector:
- _objc_msgSend$removeObject:
- _objc_msgSend$scanGroup
- _objc_msgSend$scheduleConcurrentActionWithSelector:eventInfo:
- _objc_msgSend$setArgument:atIndex:
- _objc_msgSend$setSelector:
- _objc_msgSend$setTarget:
CStrings:
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nRollback already applied. Prompting user to restart; if declined, shows a restart-required error in the scan-failed view."
+ "%s [%{public}@|%{public}@]: Concurrent metadata tasks settled: outcome=%ld; firstError=%{public}@; unfinished=%{public}@"
+ "-[SUUIMobileScanOperation action_QueryFullScanMetadata:error:]_block_invoke"
+ "-[SUUIMobileScanOperation action_QueryFullScanMetadata:error:]_block_invoke_2"
+ "-[SUUIMobileScanOperation checkForMDMRestrictionsWithReplyHandler:]_block_invoke"
+ "-[SUUIMobileScanOperation checkIfAutoUpdateScheduledWithReplyHandler:]_block_invoke"
+ "-[SUUIMobileScanOperation checkIsEligibleForRollbackWithReplyHandler:]_block_invoke"
+ "-[SUUIMobileScanOperation queryRollbackStatusWithReplyHandler:]_block_invoke"
+ "-[SUUIMobileScanOperation scheduleAutoUpdateScheduledTask]_block_invoke"
+ "AutoUpdateScheduled"
+ "BetaPrograms"
+ "DDMDeclaration"
+ "MDMRestrictions"
+ "RollbackEligibility"
+ "RollbackStatus"
+ "v16@?0@\"SUUITaskGroupResult\"8"
+ "v24@?0@8@?<v@?@@\"NSError\">16"
- "%@.concurrent-queue"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nRollback already applied, show the user an alert to reboot, and show no available updates."
- "%s [%{public}@|%{public}@]: All of the concurrent operations has been finished. Current operation error: %{public}@"
- "%s [%{public}@|%{public}@]: Assigning rollback descriptor %@ (%p) instead of %@ (%p)"
- "%s [%{public}@|%{public}@]: Calling dispatch_group_leave for action %{public}@, and removing the entry from the set of running actions"
- "%s [%{public}@|%{public}@]: Concurrent operation \"%{public}@\" has been finished. Success: %{public}@; error: %{public}@. Previous error: %{public}@"
- "%s [%{public}@|%{public}@]: Concurrent operations completed, but timeout already handled."
- "%s [%{public}@|%{public}@]: Concurrent operations timed out. Bailing out."
- "%s [%{public}@|%{public}@]: Concurrent queue is nil, cannot dispatch action %{public}@"
- "%s [%{public}@|%{public}@]: Ignoring request to call dispatch_group_leave for the action %{public}@, as the running actions set has no entry for this action anymore."
- "%s [%{public}@|%{public}@]: No concurrent operations are running, proceeding immediately."
- "%s [%{public}@|%{public}@]: Not scheduling action %{public}@ because a previous action has already failed or timed out"
- "%s [%{public}@|%{public}@]: One or more of the concurrent operations have been failed/timed out."
- "%s [%{public}@|%{public}@]: Starting to execute concurrent action: \"%{public}@\""
- "%s [%{public}@|%{public}@]: Stop resolving %{public}@ because a previous action has already been failed"
- "%s [%{public}@|%{public}@]: The task has already been canceled. Stopping execution for %{public}@."
- "%s [%{public}@|%{public}@]: There's a previous operation error (%{public}@). Skipping on the execution of: %{public}@"
- "%s [%{public}@|%{public}@]: Timeout fired, but concurrent operations already completed."
- "%s [%{public}@|%{public}@]: Waiting for %lu concurrent operations to complete: %{public}@"
- "-[SUUIMobileScanOperation action_ObserveConcurrentQueries:error:]"
- "-[SUUIMobileScanOperation checkForMDMRestrictions:withReplyHandler:]_block_invoke"
- "-[SUUIMobileScanOperation checkIfAutoUpdateScheduled:withReplyHandler:]_block_invoke"
- "-[SUUIMobileScanOperation checkIsEligibleForRollback:withReplyHandler:]_block_invoke"
- "-[SUUIMobileScanOperation queryRollbackStatus:withReplyHandler:]_block_invoke"
- "-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]"
- "-[SUUIMobileScanOperation scheduleConcurrentActionWithSelector:eventInfo:]_block_invoke"
- "Concurrent operations timed out."
- "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.QueryCurrentDownload: checkIfAutoUpdateScheduled:withReplyHandler:"
- "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions: checkForBetaPrograms:withReplyHandler:"
- "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions: checkForMDMRestrictions:withReplyHandler:"
- "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions: checkIsEligibleForRollback:withReplyHandler:"
- "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions: queryDDMDeclaration:withReplyHandler:"
- "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions: queryRollbackStatus:withReplyHandler:"
- "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.QueryCurrentDownload: checkIfAutoUpdateScheduled:withReplyHandler:"
- "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions: checkForBetaPrograms:withReplyHandler:"
- "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions: checkForMDMRestrictions:withReplyHandler:"
- "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions: checkIsEligibleForRollback:withReplyHandler:"
- "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions: queryDDMDeclaration:withReplyHandler:"
- "com.apple.SoftwareUpdateUI.StatefulUI.ScanOperation.State.ScheduleConcurrentActions: queryRollbackStatus:withReplyHandler:"

```
