## UnblockService

> `/System/Library/PrivateFrameworks/UnblockService.framework/UnblockService`

```diff

-13.0.0.0.0
-  __TEXT.__text: 0xbfb0
-  __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__objc_methlist: 0x3c8
+14.0.0.0.0
+  __TEXT.__text: 0xe2b4
+  __TEXT.__auth_stubs: 0x610
+  __TEXT.__objc_methlist: 0x404
   __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0x1ec
-  __TEXT.__cstring: 0x4b1
-  __TEXT.__oslogstring: 0x1973
-  __TEXT.__unwind_info: 0x1f0
-  __TEXT.__objc_classname: 0xbd
-  __TEXT.__objc_methname: 0x159b
-  __TEXT.__objc_methtype: 0x2aa
-  __TEXT.__objc_stubs: 0x1740
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x1a8
+  __TEXT.__gcc_except_tab: 0x190
+  __TEXT.__cstring: 0x4b2
+  __TEXT.__oslogstring: 0x1e7a
+  __TEXT.__unwind_info: 0x208
+  __TEXT.__objc_classname: 0xc7
+  __TEXT.__objc_methname: 0x16b3
+  __TEXT.__objc_methtype: 0x30a
+  __TEXT.__objc_stubs: 0x1800
+  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__const: 0x180
   __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x628
+  __DATA_CONST.__objc_selrefs: 0x660
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x370
+  __DATA_CONST.__objc_arraydata: 0x60
+  __AUTH_CONST.__auth_got: 0x318
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x380
-  __AUTH_CONST.__objc_const: 0x908
+  __AUTH_CONST.__objc_const: 0x940
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_ivar: 0x80
+  __DATA.__data: 0x60
   __DATA.__common: 0x4
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x1e0

   - /System/Library/PrivateFrameworks/UnblockClient.framework/UnblockClient
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0C0E2093-351B-3518-AE7D-36054F7A2C88
-  Functions: 160
-  Symbols:   772
-  CStrings:  462
+  UUID: AFC278FF-3DAD-3339-86F2-3741195B3EEB
+  Functions: 180
+  Symbols:   816
+  CStrings:  489
 
Symbols:
+ -[UBDeadlockInfo copyWithZone:]
+ -[UBThreadExhaustionInfo copyWithZone:]
+ -[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:suspendedTaskSelected:threadExhaustions:processLevelDependencies:options:]
+ -[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:suspendedTaskSelected:threadExhaustions:processLevelDependencies:options:].cold.1
+ -[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:suspendedTaskSelected:threadExhaustions:processLevelDependencies:options:].cold.2
+ -[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:suspendedTaskSelected:threadExhaustions:processLevelDependencies:options:].cold.3
+ -[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:suspendedTaskSelected:threadExhaustions:processLevelDependencies:options:].cold.4
+ -[UBUnblockReactiveRecovery reasonToAvoidKillingTask:options:]
+ -[UBUnblockReactiveRecovery reasonToAvoidKillingTask:options:].cold.1
+ -[UBUnblockReactiveRecovery reasonToAvoidKillingTask:options:].cold.2
+ -[UBUnblockReactiveRecovery selectTaskInThreadDependencyChainWithServiceContext:]
+ -[UBUnblockReactiveRecovery selectTaskInThreadDependencyChainWithServiceContext:].cold.1
+ -[UBUnblockReactiveRecovery selectTaskInThreadDependencyChainWithServiceContext:].cold.2
+ -[UBUnblockReactiveRecovery selectTaskInvolvedInAnyIssueWithServiceContext:ignoreMinTimeBlocked:]
+ -[UBUnblockReactiveRecovery selectTaskInvolvedInAnyIssueWithServiceContext:ignoreMinTimeBlocked:].cold.1
+ -[UBUnblockReactiveRecovery selectTaskInvolvedInAnyIssueWithServiceContext:ignoreMinTimeBlocked:].cold.2
+ -[UBUnblockReactiveRecovery(Deadlock) selectNodeInDeadlocksBlockingTask:preferredMinimumDuration:serviceContext:processLevelDependencies:]
+ -[UBUnblockReactiveRecovery(Deadlock) selectNodeInDeadlocksBlockingTask:preferredMinimumDuration:serviceContext:processLevelDependencies:].cold.1
+ -[UBUnblockReactiveRecovery(ThreadExhaustion) selectThreadExhaustionBlockingTask:serviceContext:processLevelDependencies:]
+ -[UBUnblockReactiveRecovery(ThreadExhaustion) selectThreadExhaustionBlockingTask:serviceContext:processLevelDependencies:].cold.1
+ -[UBUnblockReactiveRecovery(ThreadExhaustion) selectThreadExhaustionInAllThreadExhaustionsWithServiceContext:]
+ -[UBUnblockService(XPCHandling) handleIncomingMessage:].cold.4
+ -[UBUnblockService(XPCHandling) handleReactiveRecoveryRequest:].cold.5
+ -[UBUnblockService(XPCHandling) openListenerConnection].cold.4
+ GCC_except_table46
+ GCC_except_table70
+ _FindLastDependency
+ _IsSecondTaskHigherJetsamPriority
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _UBRecoveryStatusCopyDescription
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_CLASS_PROTOCOLS_$_UBDeadlockInfo
+ __OBJC_CLASS_PROTOCOLS_$_UBThreadExhaustionInfo
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_$_NSCopying
+ ___106-[UBUnblockReactiveRecovery(ThreadExhaustion) threadExhaustionsAboveLimit:threadIDToThreadExhaustionDict:]_block_invoke.154
+ ___164-[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:suspendedTaskSelected:threadExhaustions:processLevelDependencies:options:]_block_invoke
+ ___164-[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:suspendedTaskSelected:threadExhaustions:processLevelDependencies:options:]_block_invoke.205
+ ___block_literal_global.208
+ ___block_literal_global.291
+ ___block_literal_global.294
+ _objc_msgSend$allKeys
+ _objc_msgSend$fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:suspendedTaskSelected:threadExhaustions:processLevelDependencies:options:
+ _objc_msgSend$lt:
+ _objc_msgSend$reasonToAvoidKillingTask:options:
+ _objc_msgSend$selectNodeInDeadlocksBlockingTask:preferredMinimumDuration:serviceContext:processLevelDependencies:
+ _objc_msgSend$selectTaskInThreadDependencyChainWithServiceContext:
+ _objc_msgSend$selectTaskInvolvedInAnyIssueWithServiceContext:ignoreMinTimeBlocked:
+ _objc_msgSend$selectThreadExhaustionBlockingTask:serviceContext:processLevelDependencies:
+ _objc_msgSend$selectThreadExhaustionInAllThreadExhaustionsWithServiceContext:
+ _objc_msgSend$startTimestamp
+ _objc_msgSend$suppressTelemetry
+ _objc_retainAutoreleasedReturnValue
+ _proc_pidinfo
- -[UBUnblockReactiveRecovery avoidKillingTask:options:].cold.1
- -[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:options:]
- -[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:options:].cold.1
- -[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:options:].cold.2
- -[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:options:].cold.3
- -[UBUnblockReactiveRecovery selectTaskInDefinitiveIssuesWithServiceContext:]
- -[UBUnblockReactiveRecovery selectTaskInDefinitiveIssuesWithServiceContext:].cold.1
- -[UBUnblockReactiveRecovery selectTaskInvolvedInAnyIssueWithServiceContext:]
- -[UBUnblockReactiveRecovery selectTaskInvolvedInAnyIssueWithServiceContext:].cold.1
- -[UBUnblockReactiveRecovery selectTaskInvolvedInAnyIssueWithServiceContext:].cold.2
- -[UBUnblockReactiveRecovery taskIs3PApp:options:].cold.2
- -[UBUnblockReactiveRecovery(Deadlock) selectNodeInDeadlocksBlockingTask:preferredMinimumDuration:serviceContext:]
- -[UBUnblockReactiveRecovery(ThreadExhaustion) selectThreadExhaustionBlockingTask:serviceContext:]
- GCC_except_table43
- GCC_except_table67
- GCC_except_table68
- ___106-[UBUnblockReactiveRecovery(ThreadExhaustion) threadExhaustionsAboveLimit:threadIDToThreadExhaustionDict:]_block_invoke.148
- ___117-[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:options:]_block_invoke
- ___117-[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:options:]_block_invoke.195
- ___49-[UBUnblockReactiveRecovery taskIs3PApp:options:]_block_invoke
- ___block_descriptor_52_e8_32s40w_e5_v8?0lw40l8s32l8
- ___block_literal_global.198
- ___block_literal_global.279
- ___block_literal_global.282
- __dispatch_source_type_proc
- _dispatch_activate
- _dispatch_get_global_queue
- _dispatch_source_cancel
- _dispatch_source_create
- _dispatch_source_set_event_handler
- _objc_claimAutoreleasedReturnValue
- _objc_copyWeak
- _objc_destroyWeak
- _objc_initWeak
- _objc_loadWeakRetained
- _objc_msgSend$fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:options:
- _objc_msgSend$selectNodeInDeadlocksBlockingTask:preferredMinimumDuration:serviceContext:
- _objc_msgSend$selectTaskInDefinitiveIssuesWithServiceContext:
- _objc_msgSend$selectTaskInvolvedInAnyIssueWithServiceContext:
- _objc_msgSend$selectThreadExhaustionBlockingTask:serviceContext:
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
CStrings:
+ "\n%@\n\n%@"
+ "%@ [%d] does not have thread 0x%llx."
+ "@24@0:8^{_NSZone=}16"
+ "@28@0:8@16B24"
+ "@40@0:8@16@24o^@32"
+ "@48@0:8@16d24@32o^@40"
+ "Candidate task %{public}@ [%d] is unblock server, not eligible for termination"
+ "Failed to create reply for watchdog services"
+ "Multiple issues selected"
+ "NSCopying"
+ "No dependency graph node for thread blocked by deadlock, unable to record process-level dependency"
+ "No dependency graph node for thread blocked by thread exhaustion, unable to record process-level dependency"
+ "Sending reply"
+ "Service <%{public}@ [%d] tid[%llx] time-elapsed[%fs]>: %{public}@ [%d] higher jetsam priority (%d) than service (%d), checking for other issues"
+ "Service <%{public}@ [%d] tid[%llx] time-elapsed[%fs]>: Analyzing if impacted by suspension."
+ "Service <%{public}@ [%d] tid[%llx] time-elapsed[%fs]>: Best option is non-killable process %{public}@ [%d] with reason %@"
+ "Service <%{public}@ [%d] tid[%llx] time-elapsed[%fs]>: Best option is opportunistic (process %{public}@ [%d])"
+ "Service <%{public}@ [%d] tid[%llx] time-elapsed[%fs]>: Best option is process being debugged"
+ "Service <%{public}@ [%d] tid[%llx] time-elapsed[%fs]>: Best option is suspended process"
+ "Service <%{public}@ [%d] tid[%llx] time-elapsed[%fs]>: Correlated deadlocks involve only processes of higher jetsam priority (lowest is %{public}@ [%d] at %d) than service (%d)"
+ "Service <%{public}@ [%d] tid[%llx] time-elapsed[%fs]>: Impacted by suspension of %{public}@ [%d]"
+ "Service <%{public}@ [%d] tid[%llx] time-elapsed[%fs]>: Not impacted directly by process suspension"
+ "Service <%{public}@ [%d] tid[%llx] time-elapsed[%fs]>: Time-correlated issues involve only processes of higher jetsam priority (lowest %d) than service (%d)"
+ "Service <%{public}@ [%d] tid[%llx]>: Could not find any relevant issues affecting it."
+ "allKeys"
+ "copyWithZone:"
+ "fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:suspendedTaskSelected:threadExhaustions:processLevelDependencies:options:"
+ "lt:"
+ "processesAndThreadsInvolved %@ does not contain selected node %@"
+ "q32@0:8@16Q24"
+ "reasonToAvoidKillingTask:options:"
+ "selectNodeInDeadlocksBlockingTask:preferredMinimumDuration:serviceContext:processLevelDependencies:"
+ "selectTaskInThreadDependencyChainWithServiceContext:"
+ "selectTaskInvolvedInAnyIssueWithServiceContext:ignoreMinTimeBlocked:"
+ "selectThreadExhaustionBlockingTask:serviceContext:processLevelDependencies:"
+ "selectThreadExhaustionInAllThreadExhaustionsWithServiceContext:"
+ "startTimestamp"
+ "suppressTelemetry"
+ "v72@0:8@16@24@32@40@48@56Q64"
- "\n%@\n%@"
- "Service <%{public}@ [%d] tid[%llx] time-elapsed[%fs]>: Best option is non-killable process %{public}@ [%d]"
- "Service <%{public}@ [%d] tid[%llx] time-elapsed[%fs]>: Correlated deadlocks involve only processes of higher jetsam priority (lowest %d) than service (%d)"
- "Service <%{public}@ [%d] tid[%llx]>: Could not find any relevant unrecoverable issues affecting it."
- "Unable to create task exit source for [%d]"
- "both deadlock and thread exhaustion selected"
- "fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:options:"
- "selectNodeInDeadlocksBlockingTask:preferredMinimumDuration:serviceContext:"
- "selectTaskInDefinitiveIssuesWithServiceContext:"
- "selectTaskInvolvedInAnyIssueWithServiceContext:"
- "selectThreadExhaustionBlockingTask:serviceContext:"
- "v56@0:8@16@24@32@40Q48"

```
