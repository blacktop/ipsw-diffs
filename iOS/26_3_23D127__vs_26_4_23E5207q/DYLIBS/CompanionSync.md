## CompanionSync

> `/System/Library/PrivateFrameworks/CompanionSync.framework/CompanionSync`

```diff

-272.0.0.0.0
-  __TEXT.__text: 0x9c668
-  __TEXT.__auth_stubs: 0x1110
-  __TEXT.__objc_methlist: 0x8cd8
-  __TEXT.__cstring: 0x7530
+275.0.0.0.0
+  __TEXT.__text: 0xa034c
+  __TEXT.__auth_stubs: 0x10d0
+  __TEXT.__objc_methlist: 0x8db0
+  __TEXT.__cstring: 0x7746
   __TEXT.__const: 0x1c0
-  __TEXT.__oslogstring: 0x9502
-  __TEXT.__gcc_except_tab: 0x36cc
-  __TEXT.__unwind_info: 0x29a8
-  __TEXT.__objc_classname: 0xd60
-  __TEXT.__objc_methname: 0xd08a
-  __TEXT.__objc_methtype: 0x2a33
-  __TEXT.__objc_stubs: 0xa560
+  __TEXT.__oslogstring: 0x9512
+  __TEXT.__gcc_except_tab: 0x35e0
+  __TEXT.__unwind_info: 0x2e28
+  __TEXT.__objc_classname: 0xd61
+  __TEXT.__objc_methname: 0xd3ab
+  __TEXT.__objc_methtype: 0x2a52
+  __TEXT.__objc_stubs: 0xa700
   __DATA_CONST.__got: 0x5f8
-  __DATA_CONST.__const: 0x1fb8
+  __DATA_CONST.__const: 0x2020
   __DATA_CONST.__objc_classlist: 0x388
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3518
+  __DATA_CONST.__objc_selrefs: 0x3580
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x898
-  __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x36a0
-  __AUTH_CONST.__objc_const: 0x146e0
+  __AUTH_CONST.__auth_got: 0x878
+  __AUTH_CONST.__const: 0x4c0
+  __AUTH_CONST.__cfstring: 0x3920
+  __AUTH_CONST.__objc_const: 0x14890
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1fe0
-  __DATA.__objc_ivar: 0xc4c
+  __DATA.__objc_ivar: 0xc70
   __DATA.__data: 0xb68
-  __DATA.__bss: 0x140
+  __DATA.__bss: 0x130
   __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__common: 0x50
-  __DATA_DIRTY.__bss: 0x68
+  __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 97CEF3D6-6DEC-310E-984F-F0CB1B766CDB
-  Functions: 3737
-  Symbols:   13922
-  CStrings:  5030
+  UUID: 43A939E3-BE59-3F53-B5F3-FE6592946127
+  Functions: 3786
+  Symbols:   14132
+  CStrings:  5097
 
Symbols:
+ -[SYLogServiceState dictionaryRepresentation].cold.1
+ -[SYLogServiceState hasStateChangeDequeuedState]
+ -[SYLogServiceState hasStateChangeEnqueuedState]
+ -[SYLogServiceState sessionStateAsString:]
+ -[SYLogServiceState setStateChangeDequeuedDate:]
+ -[SYLogServiceState setStateChangeDequeuedState:]
+ -[SYLogServiceState setStateChangeEnqueuedDate:]
+ -[SYLogServiceState setStateChangeEnqueuedState:]
+ -[SYLogServiceState stateChangeDequeuedDate]
+ -[SYLogServiceState stateChangeDequeuedState]
+ -[SYLogServiceState stateChangeEnqueuedDate]
+ -[SYLogServiceState stateChangeEnqueuedState]
+ -[SYService _chooseBetweenCollidingSessions::].cold.4
+ -[SYService _chooseBetweenCollidingSessions::].cold.5
+ -[SYService stateChangeDequeued:]
+ -[SYService stateChangeDequeuedDate]
+ -[SYService stateChangeDequeuedState]
+ -[SYService stateChangeEnqueued:]
+ -[SYService stateChangeEnqueuedDate]
+ -[SYService stateChangeEnqueuedState]
+ -[SYSession _onSessionStateChangedFromNotStarted:]
+ -[SYSession _onSessionStateChangedFromNotStarted:].cold.1
+ -[SYSession hasRejectedPeerSessionForAge]
+ -[SYSession setHasRejectedPeerSessionForAge:]
+ -[SYSession startDate]
+ GCC_except_table121
+ GCC_except_table125
+ GCC_except_table129
+ GCC_except_table167
+ GCC_except_table169
+ GCC_except_table178
+ GCC_except_table179
+ GCC_except_table182
+ GCC_except_table187
+ GCC_except_table190
+ GCC_except_table273
+ GCC_except_table278
+ GCC_except_table280
+ _OBJC_IVAR_$_SYLogServiceState._stateChangeDequeuedDate
+ _OBJC_IVAR_$_SYLogServiceState._stateChangeDequeuedState
+ _OBJC_IVAR_$_SYLogServiceState._stateChangeEnqueuedDate
+ _OBJC_IVAR_$_SYLogServiceState._stateChangeEnqueuedState
+ _OBJC_IVAR_$_SYService._stateChangeDequeuedDate
+ _OBJC_IVAR_$_SYService._stateChangeDequeuedState
+ _OBJC_IVAR_$_SYService._stateChangeEnqueuedDate
+ _OBJC_IVAR_$_SYService._stateChangeEnqueuedState
+ _OBJC_IVAR_$_SYSession._hasRejectedPeerSessionForAge
+ _OBJC_IVAR_$_SYSession._hasRejectedPeerSessionForNoGeneration
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ ___28-[SYReceivingSession start:]_block_invoke.18
+ ___28-[SYReceivingSession start:]_block_invoke.18.cold.1
+ ___28-[SYReceivingSession start:]_block_invoke.18.cold.2
+ ___28-[SYReceivingSession start:]_block_invoke.18.cold.3
+ ___28-[SYReceivingSession start:]_block_invoke.18.cold.4
+ ___28-[SYReceivingSession start:]_block_invoke.18.cold.5
+ ___28-[SYReceivingSession start:]_block_invoke.20
+ ___28-[SYReceivingSession start:]_block_invoke.20.cold.1
+ ___28-[SYReceivingSession start:]_block_invoke.20.cold.2
+ ___36-[SYReceivingSession _installTimers]_block_invoke.9
+ ___36-[SYReceivingSession _installTimers]_block_invoke.9.cold.1
+ ___36-[SYReceivingSession _installTimers]_block_invoke.9.cold.2
+ ___36-[SYReceivingSession _installTimers]_block_invoke.9.cold.3
+ ___44-[SYService _handleStartSession:completion:]_block_invoke.186
+ ___44-[SYService _handleStartSession:completion:]_block_invoke.186.cold.1
+ ___44-[SYService _handleStartSession:completion:]_block_invoke.187
+ ___44-[SYService _handleStartSession:completion:]_block_invoke.187.cold.1
+ ___44-[SYService _handleStartSession:completion:]_block_invoke.187.cold.2
+ ___44-[SYService _handleStartSession:completion:]_block_invoke.187.cold.3
+ ___44-[SYService _handleStartSession:completion:]_block_invoke.187.cold.4
+ ___45-[SYLogServiceState dictionaryRepresentation]_block_invoke
+ ___50-[SYSession _onSessionStateChangedFromNotStarted:]_block_invoke
+ ___59-[SYReceivingSession _handleSyncBatch:response:completion:]_block_invoke.22
+ ___59-[SYReceivingSession _handleSyncBatch:response:completion:]_block_invoke.22.cold.1
+ ___59-[SYReceivingSession _handleSyncBatch:response:completion:]_block_invoke.24
+ ___59-[SYReceivingSession _handleSyncBatch:response:completion:]_block_invoke.24.cold.1
+ ___59-[SYReceivingSession _handleSyncBatch:response:completion:]_block_invoke.25.cold.2
+ ___59-[SYReceivingSession _handleSyncBatch:response:completion:]_block_invoke.25.cold.3
+ ___64-[SYReceivingSession _handleRestartSession:response:completion:]_block_invoke.26
+ ___64-[SYReceivingSession _handleRestartSession:response:completion:]_block_invoke.26.cold.1
+ ___64-[SYReceivingSession _handleRestartSession:response:completion:]_block_invoke.27.cold.2
+ ___70-[SYService(CompanionSyncProtoV1) _v1_handleChangeMessage:completion:]_block_invoke.518
+ ___71-[SYService(CompanionSyncProtoV1) _v1_handleBatchSyncStart:completion:]_block_invoke.515
+ ___71-[SYService(CompanionSyncProtoV1) _v1_handleSyncAllObjects:completion:]_block_invoke.512
+ ___71-[SYService(CompanionSyncProtoV1) _v1_handleSyncAllObjects:completion:]_block_invoke.512.cold.1
+ ___block_descriptor_64_e8_32s40s48s56bs_e8_v12?0I8ls32l8s56l8s40l8s48l8
+ _objc_msgSend$_onSessionStateChangedFromNotStarted:
+ _objc_msgSend$hasRejectedPeerSessionForAge
+ _objc_msgSend$hasStateChangeDequeuedState
+ _objc_msgSend$hasStateChangeEnqueuedState
+ _objc_msgSend$sessionStateAsString:
+ _objc_msgSend$setHasRejectedPeerSessionForAge:
+ _objc_msgSend$setStateChangeDequeuedDate:
+ _objc_msgSend$setStateChangeDequeuedState:
+ _objc_msgSend$setStateChangeEnqueuedDate:
+ _objc_msgSend$setStateChangeEnqueuedState:
+ _objc_msgSend$startDate
+ _objc_msgSend$stateChangeDequeued:
+ _objc_msgSend$stateChangeDequeuedDate
+ _objc_msgSend$stateChangeDequeuedState
+ _objc_msgSend$stateChangeEnqueued:
+ _objc_msgSend$stateChangeEnqueuedDate
+ _objc_msgSend$stateChangeEnqueuedState
- -[SYService _handleStartSession:completion:].cold.14
- -[SYSession _onSessionStateChangedTo:do:]
- -[SYSession _onSessionStateChangedTo:do:].cold.1
- -[SYSession hasRejectedPeerSession]
- -[SYSession setHasRejectedPeerSession:]
- GCC_except_table119
- GCC_except_table123
- GCC_except_table127
- GCC_except_table157
- GCC_except_table172
- GCC_except_table176
- GCC_except_table181
- GCC_except_table184
- GCC_except_table267
- GCC_except_table272
- _OBJC_IVAR_$_SYSession._rejectedNewSessionFromSamePeer
- ___28-[SYReceivingSession start:]_block_invoke.19
- ___28-[SYReceivingSession start:]_block_invoke.19.cold.1
- ___28-[SYReceivingSession start:]_block_invoke.19.cold.2
- ___28-[SYReceivingSession start:]_block_invoke.19.cold.3
- ___28-[SYReceivingSession start:]_block_invoke.19.cold.4
- ___28-[SYReceivingSession start:]_block_invoke.19.cold.5
- ___28-[SYReceivingSession start:]_block_invoke.21
- ___28-[SYReceivingSession start:]_block_invoke.21.cold.1
- ___28-[SYReceivingSession start:]_block_invoke.21.cold.2
- ___36-[SYReceivingSession _installTimers]_block_invoke.10
- ___36-[SYReceivingSession _installTimers]_block_invoke.10.cold.1
- ___36-[SYReceivingSession _installTimers]_block_invoke.10.cold.2
- ___36-[SYReceivingSession _installTimers]_block_invoke.10.cold.3
- ___41-[SYSession _onSessionStateChangedTo:do:]_block_invoke
- ___44-[SYService _handleStartSession:completion:]_block_invoke.184
- ___44-[SYService _handleStartSession:completion:]_block_invoke.184.cold.1
- ___44-[SYService _handleStartSession:completion:]_block_invoke.185
- ___44-[SYService _handleStartSession:completion:]_block_invoke.185.cold.1
- ___44-[SYService _handleStartSession:completion:]_block_invoke.185.cold.2
- ___44-[SYService _handleStartSession:completion:]_block_invoke.185.cold.3
- ___44-[SYService _handleStartSession:completion:]_block_invoke.185.cold.4
- ___59-[SYReceivingSession _handleSyncBatch:response:completion:]_block_invoke.23
- ___59-[SYReceivingSession _handleSyncBatch:response:completion:]_block_invoke.23.cold.1
- ___59-[SYReceivingSession _handleSyncBatch:response:completion:]_block_invoke.26
- ___59-[SYReceivingSession _handleSyncBatch:response:completion:]_block_invoke.26.cold.1
- ___59-[SYReceivingSession _handleSyncBatch:response:completion:]_block_invoke.26.cold.2
- ___59-[SYReceivingSession _handleSyncBatch:response:completion:]_block_invoke.26.cold.3
- ___64-[SYReceivingSession _handleRestartSession:response:completion:]_block_invoke.28.cold.2
- ___64-[SYReceivingSession _handleRestartSession:response:completion:]_block_invoke.29
- ___64-[SYReceivingSession _handleRestartSession:response:completion:]_block_invoke.29.cold.1
- ___70-[SYService(CompanionSyncProtoV1) _v1_handleChangeMessage:completion:]_block_invoke.496
- ___71-[SYService(CompanionSyncProtoV1) _v1_handleBatchSyncStart:completion:]_block_invoke.493
- ___71-[SYService(CompanionSyncProtoV1) _v1_handleSyncAllObjects:completion:]_block_invoke.490
- ___71-[SYService(CompanionSyncProtoV1) _v1_handleSyncAllObjects:completion:]_block_invoke.490.cold.1
- ___block_descriptor_52_e8_32s40bs_e5_v8?0ls32l8s40l8
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_onSessionStateChangedTo:do:
- _objc_msgSend$hasRejectedPeerSession
- _objc_msgSend$initWithObjects:
- _objc_msgSend$setHasRejectedPeerSession:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ "%@ (%d)"
+ "%@%@"
+ "-[SYSession _onSessionStateChangedFromNotStarted:]"
+ "@\"NSNumber\""
+ "Colliding receive sessions (%{public}@, %{public}@) have the same date!"
+ "P"
+ "SYSessionStateCancel"
+ "SYSessionStateContinue"
+ "SYSessionStateError"
+ "SYSessionStateErrorOccurredWhileWaitingForCompletion"
+ "SYSessionStateNotStarted"
+ "SYSessionStateRestart"
+ "SYSessionStateSendComplete"
+ "SYSessionStateSyncComplete"
+ "SYSessionStateWaitingForApplyCompletion"
+ "SYSessionStateWaitingForBatchEnqueue"
+ "SYSessionStateWaitingForCompletionConfirmation"
+ "SYSessionStateWaitingForResetCompletion"
+ "SYSessionStateWaitingForStartConfirmation"
+ "T@\"NSDate\",&,N,V_stateChangeDequeuedDate"
+ "T@\"NSDate\",&,N,V_stateChangeEnqueuedDate"
+ "T@\"NSDate\",R,N,V_stateChangeDequeuedDate"
+ "T@\"NSDate\",R,N,V_stateChangeEnqueuedDate"
+ "T@\"NSNumber\",R,N,V_stateChangeDequeuedState"
+ "T@\"NSNumber\",R,N,V_stateChangeEnqueuedState"
+ "TI,N,V_stateChangeDequeuedState"
+ "TI,N,V_stateChangeEnqueuedState"
+ "Unknown"
+ "_hasRejectedPeerSessionForAge"
+ "_hasRejectedPeerSessionForNoGeneration"
+ "_onSessionStateChangedFromNotStarted:"
+ "_stateChangeDequeuedDate"
+ "_stateChangeDequeuedState"
+ "_stateChangeEnqueuedDate"
+ "_stateChangeEnqueuedState"
+ "hasRejectedPeerSessionForAge"
+ "hasStateChangeDequeuedState"
+ "hasStateChangeEnqueuedState"
+ "sessionStateAsString:"
+ "setHasRejectedPeerSessionForAge:"
+ "setStateChangeDequeuedDate:"
+ "setStateChangeDequeuedState:"
+ "setStateChangeEnqueuedDate:"
+ "setStateChangeEnqueuedState:"
+ "startDate"
+ "stateChangeDequeued:"
+ "stateChangeDequeuedDate"
+ "stateChangeDequeuedState"
+ "stateChangeEnqueued:"
+ "stateChangeEnqueuedDate"
+ "stateChangeEnqueuedState"
+ "v12@?0I8"
+ "{?=\"serviceType\"b1\"enqueuedState\"b1\"dequeuedState\"b1}"
- "'P'yyyy-MM-dd'T'HH:mm:ss.SSS"
- "-[SYSession _onSessionStateChangedTo:do:]"
- "Issuing immediate rejection of incoming session request"
- "_onSessionStateChangedTo:do:"
- "_rejectedNewSessionFromSamePeer"
- "hasRejectedPeerSession"
- "initWithObjects:"
- "setHasRejectedPeerSession:"
- "v28@0:8I16@?20"
- "{?=\"serviceType\"b1}"

```
