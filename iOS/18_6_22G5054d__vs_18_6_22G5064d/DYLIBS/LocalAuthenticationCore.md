## LocalAuthenticationCore

> `/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`

```diff

-1656.140.3.0.0
-  __TEXT.__text: 0xce414
+1656.140.4.0.0
+  __TEXT.__text: 0xd158c
   __TEXT.__auth_stubs: 0x2020
-  __TEXT.__objc_methlist: 0x7cd8
-  __TEXT.__const: 0x3f44
-  __TEXT.__cstring: 0xb14b
-  __TEXT.__oslogstring: 0x5029
-  __TEXT.__gcc_except_tab: 0x1468
+  __TEXT.__objc_methlist: 0x7f90
+  __TEXT.__const: 0x3f54
+  __TEXT.__cstring: 0xb34b
+  __TEXT.__oslogstring: 0x54e9
+  __TEXT.__gcc_except_tab: 0x1504
   __TEXT.__dlopen_cstrs: 0x3ac
   __TEXT.__swift5_typeref: 0x1493
   __TEXT.__constg_swiftt: 0xd84

   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift_as_ret: 0xd4
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x3960
+  __TEXT.__unwind_info: 0x3a38
   __TEXT.__eh_frame: 0x20e8
-  __TEXT.__objc_classname: 0x1dbc
-  __TEXT.__objc_methname: 0xc93b
-  __TEXT.__objc_methtype: 0x36bf
-  __TEXT.__objc_stubs: 0x8e00
-  __DATA_CONST.__got: 0x8d8
-  __DATA_CONST.__const: 0x3f98
-  __DATA_CONST.__objc_classlist: 0x710
-  __DATA_CONST.__objc_protolist: 0x530
+  __TEXT.__objc_classname: 0x1e57
+  __TEXT.__objc_methname: 0xcd34
+  __TEXT.__objc_methtype: 0x3818
+  __TEXT.__objc_stubs: 0x9180
+  __DATA_CONST.__got: 0x8f8
+  __DATA_CONST.__const: 0x4108
+  __DATA_CONST.__objc_classlist: 0x728
+  __DATA_CONST.__objc_protolist: 0x548
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3038
-  __DATA_CONST.__objc_protorefs: 0x210
-  __DATA_CONST.__objc_superrefs: 0x450
+  __DATA_CONST.__objc_selrefs: 0x3130
+  __DATA_CONST.__objc_protorefs: 0x220
+  __DATA_CONST.__objc_superrefs: 0x470
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x1020
   __AUTH_CONST.__const: 0x3118
-  __AUTH_CONST.__cfstring: 0x5600
-  __AUTH_CONST.__objc_const: 0x31340
+  __AUTH_CONST.__cfstring: 0x5820
+  __AUTH_CONST.__objc_const: 0x32308
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x9d8
+  __AUTH.__objc_data: 0xac8
   __AUTH.__data: 0x188
-  __DATA.__objc_ivar: 0x73c
-  __DATA.__data: 0x3f78
+  __DATA.__objc_ivar: 0x764
+  __DATA.__data: 0x4098
   __DATA.__bss: 0x1fa9
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x4410

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: F4AC84D8-7E01-3AD8-BF59-962AA38E8131
-  Functions: 5267
-  Symbols:   18658
-  CStrings:  5631
+  UUID: 09115765-31C2-3E78-86CF-C9C88B9F8AAB
+  Functions: 5333
+  Symbols:   18907
+  CStrings:  5744
 
Symbols:
+ -[LACAnalyticsData authenticationAction:failing:]
+ -[LACAnalyticsData authenticationAttemptFailedForEvent:]
+ -[LACAnalyticsData authenticationSuccessfulForEvent:]
+ -[LACAnalyticsData description]
+ -[LACAnalyticsData mergeAnalyticsData:]
+ -[LACAnalyticsProcessor .cxx_destruct]
+ -[LACAnalyticsProcessor _donateDialogEvent:request:]
+ -[LACAnalyticsProcessor initWithAnalyticsSession:]
+ -[LACAnalyticsServiceXPCHost .cxx_destruct]
+ -[LACAnalyticsServiceXPCHost connectSessionForContext:reply:]
+ -[LACAnalyticsServiceXPCHost initWithWorkQueue:]
+ -[LACAnalyticsServiceXPCHost sessionForContextUUID:]
+ -[LACAnalyticsServiceXPCHost startSessionForContext:dialogID:bundleID:reply:]
+ -[LACAnalyticsSession authenticationAction:failing:]
+ -[LACAnalyticsSession authenticationAttemptFailedForEvent:]
+ -[LACAnalyticsSession authenticationStartedForEvent:]
+ -[LACAnalyticsSession authenticationSuccessfulForEvent:]
+ -[LACAnalyticsSession finished]
+ -[LACAnalyticsSession mergeEvaluationAnalytics:]
+ -[LACAnalyticsSession mergeEvaluationAnalytics:].cold.1
+ -[LACAnalyticsSession trackEvaluationAnalytics:]
+ -[LACAnalyticsSession untrackEvaluationAnalytics:]
+ -[LACAnalyticsSessionClient .cxx_destruct]
+ -[LACAnalyticsSessionClient _bootstrapServiceWithError:]
+ -[LACAnalyticsSessionClient _callBlockOnSynchronousRemoteObjectProxy:]
+ -[LACAnalyticsSessionClient _connectionDidClose:]
+ -[LACAnalyticsSessionClient _connectionWithError:]
+ -[LACAnalyticsSessionClient authenticationAction:failing:]
+ -[LACAnalyticsSessionClient authenticationAction:failing:].cold.1
+ -[LACAnalyticsSessionClient authenticationAttemptFailedForEvent:]
+ -[LACAnalyticsSessionClient authenticationAttemptFailedForEvent:].cold.1
+ -[LACAnalyticsSessionClient authenticationStartedForEvent:]
+ -[LACAnalyticsSessionClient authenticationStartedForEvent:].cold.1
+ -[LACAnalyticsSessionClient authenticationSuccessfulForEvent:]
+ -[LACAnalyticsSessionClient authenticationSuccessfulForEvent:].cold.1
+ -[LACAnalyticsSessionClient connectToExistingSession]
+ -[LACAnalyticsSessionClient context]
+ -[LACAnalyticsSessionClient finishSession]
+ -[LACAnalyticsSessionClient finishSession].cold.1
+ -[LACAnalyticsSessionClient initWithContext:]
+ -[LACAnalyticsSessionClient setContext:]
+ -[LACAnalyticsSessionClient setContext:].cold.1
+ -[LACAnalyticsSessionClient setContext:].cold.2
+ -[LACAnalyticsSessionClient startSessionForDialogID:bundleID:]
+ -[LACAnalyticsSessionXPCHost .cxx_destruct]
+ -[LACAnalyticsSessionXPCHost _checkQueueAndSessionWithAction:replyOnFailure:]
+ -[LACAnalyticsSessionXPCHost authenticationAction:failing:reply:]
+ -[LACAnalyticsSessionXPCHost authenticationAttemptFailedForEvent:reply:]
+ -[LACAnalyticsSessionXPCHost authenticationStartedForEvent:reply:]
+ -[LACAnalyticsSessionXPCHost authenticationSuccessfulForEvent:reply:]
+ -[LACAnalyticsSessionXPCHost contextUUID]
+ -[LACAnalyticsSessionXPCHost finishWithReply:]
+ -[LACAnalyticsSessionXPCHost initWithSession:contextUUID:connected:workQueue:]
+ -[LACAnalyticsSessionXPCHost session]
+ -[LACAnalyticsSessionXPCHost updateContextUUID:reply:]
+ -[LACBiomeDialogEvent addAction:failing:]
+ -[LACBiomeDialogEvent mergeBiomeEvent:]
+ GCC_except_table24
+ _LACLogAnalytics
+ _LACLogAnalytics.__logObj
+ _LACLogAnalytics.cold.1
+ _LACLogAnalytics.onceToken
+ _NSStringFromLACAnalyticsAction
+ _OBJC_CLASS_$_LACAnalyticsServiceXPCHost
+ _OBJC_CLASS_$_LACAnalyticsSessionClient
+ _OBJC_CLASS_$_LACAnalyticsSessionXPCHost
+ _OBJC_CLASS_$_NSPointerArray
+ _OBJC_IVAR_$_LACAnalyticsProcessor._analyticsSession
+ _OBJC_IVAR_$_LACAnalyticsServiceXPCHost._sessions
+ _OBJC_IVAR_$_LACAnalyticsServiceXPCHost._workQueue
+ _OBJC_IVAR_$_LACAnalyticsSession._evaluationAnalytics
+ _OBJC_IVAR_$_LACAnalyticsSession._finished
+ _OBJC_IVAR_$_LACAnalyticsSessionClient._connection
+ _OBJC_IVAR_$_LACAnalyticsSessionClient._context
+ _OBJC_IVAR_$_LACAnalyticsSessionClient._session
+ _OBJC_IVAR_$_LACAnalyticsSessionXPCHost._connected
+ _OBJC_IVAR_$_LACAnalyticsSessionXPCHost._contextUUID
+ _OBJC_IVAR_$_LACAnalyticsSessionXPCHost._session
+ _OBJC_IVAR_$_LACAnalyticsSessionXPCHost._workQueue
+ _OBJC_METACLASS_$_LACAnalyticsServiceXPCHost
+ _OBJC_METACLASS_$_LACAnalyticsSessionClient
+ _OBJC_METACLASS_$_LACAnalyticsSessionXPCHost
+ __OBJC_$_INSTANCE_METHODS_LACAnalyticsServiceXPCHost
+ __OBJC_$_INSTANCE_METHODS_LACAnalyticsSessionClient
+ __OBJC_$_INSTANCE_METHODS_LACAnalyticsSessionXPCHost
+ __OBJC_$_INSTANCE_VARIABLES_LACAnalyticsProcessor
+ __OBJC_$_INSTANCE_VARIABLES_LACAnalyticsServiceXPCHost
+ __OBJC_$_INSTANCE_VARIABLES_LACAnalyticsSessionClient
+ __OBJC_$_INSTANCE_VARIABLES_LACAnalyticsSessionXPCHost
+ __OBJC_$_PROP_LIST_LACAnalyticsSessionClient
+ __OBJC_$_PROP_LIST_LACAnalyticsSessionXPCHost
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACAnalyticsCollecting
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACAnalyticsServiceXPC
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACAnalyticsSessionXPC
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACAnalyticsCollecting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACAnalyticsServiceXPC
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACAnalyticsSessionXPC
+ __OBJC_$_PROTOCOL_REFS_LACAnalyticsCollecting
+ __OBJC_CLASS_PROTOCOLS_$_LACAnalyticsData
+ __OBJC_CLASS_PROTOCOLS_$_LACAnalyticsServiceXPCHost
+ __OBJC_CLASS_PROTOCOLS_$_LACAnalyticsSession
+ __OBJC_CLASS_PROTOCOLS_$_LACAnalyticsSessionClient
+ __OBJC_CLASS_PROTOCOLS_$_LACAnalyticsSessionXPCHost
+ __OBJC_CLASS_RO_$_LACAnalyticsServiceXPCHost
+ __OBJC_CLASS_RO_$_LACAnalyticsSessionClient
+ __OBJC_CLASS_RO_$_LACAnalyticsSessionXPCHost
+ __OBJC_LABEL_PROTOCOL_$_LACAnalyticsCollecting
+ __OBJC_LABEL_PROTOCOL_$_LACAnalyticsServiceXPC
+ __OBJC_LABEL_PROTOCOL_$_LACAnalyticsSessionXPC
+ __OBJC_METACLASS_RO_$_LACAnalyticsServiceXPCHost
+ __OBJC_METACLASS_RO_$_LACAnalyticsSessionClient
+ __OBJC_METACLASS_RO_$_LACAnalyticsSessionXPCHost
+ __OBJC_PROTOCOL_$_LACAnalyticsCollecting
+ __OBJC_PROTOCOL_$_LACAnalyticsServiceXPC
+ __OBJC_PROTOCOL_$_LACAnalyticsSessionXPC
+ __OBJC_PROTOCOL_REFERENCE_$_LACAnalyticsServiceXPC
+ __OBJC_PROTOCOL_REFERENCE_$_LACAnalyticsSessionXPC
+ ___40-[LACAnalyticsSessionClient setContext:]_block_invoke
+ ___42-[LACAnalyticsSessionClient finishSession]_block_invoke
+ ___50-[LACAnalyticsSessionClient _connectionWithError:]_block_invoke
+ ___50-[LACAnalyticsSessionClient _connectionWithError:]_block_invoke_2
+ ___53-[LACAnalyticsSessionClient connectToExistingSession]_block_invoke
+ ___53-[LACAnalyticsSessionClient connectToExistingSession]_block_invoke_2
+ ___56-[LACAnalyticsSessionClient _bootstrapServiceWithError:]_block_invoke
+ ___58-[LACAnalyticsSessionClient authenticationAction:failing:]_block_invoke
+ ___59-[LACAnalyticsSessionClient authenticationStartedForEvent:]_block_invoke
+ ___62-[LACAnalyticsSessionClient authenticationSuccessfulForEvent:]_block_invoke
+ ___62-[LACAnalyticsSessionClient startSessionForDialogID:bundleID:]_block_invoke
+ ___62-[LACAnalyticsSessionClient startSessionForDialogID:bundleID:]_block_invoke_2
+ ___65-[LACAnalyticsSessionClient authenticationAttemptFailedForEvent:]_block_invoke
+ ___70-[LACAnalyticsSessionClient _callBlockOnSynchronousRemoteObjectProxy:]_block_invoke
+ ___LACLogAnalytics_block_invoke
+ ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_48_e8_32r40r_e43_v24?0"NSXPCListenerEndpoint"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e34_v16?0"<LACAnalyticsServiceXPC>"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e46_v24?0"<LACAnalyticsSessionXPC>"8"NSError"16ls32l8r40l8
+ ___block_descriptor_48_e8_32s_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_49_e8_32s_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_64_e8_32s40s48s56r_e34_v16?0"<LACAnalyticsServiceXPC>"8ls32l8s40l8s48l8r56l8
+ ___block_descriptor_64_e8_32s40s48s56r_e46_v24?0"<LACAnalyticsSessionXPC>"8"NSError"16ls32l8s40l8s48l8r56l8
+ _objc_msgSend$_bootstrapServiceWithError:
+ _objc_msgSend$_callBlockOnSynchronousRemoteObjectProxy:
+ _objc_msgSend$_checkQueueAndSessionWithAction:replyOnFailure:
+ _objc_msgSend$_connectionDidClose:
+ _objc_msgSend$_connectionWithError:
+ _objc_msgSend$_donateDialogEvent:request:
+ _objc_msgSend$addAction:failing:
+ _objc_msgSend$addPointer:
+ _objc_msgSend$arrayByAddingObjectsFromArray:
+ _objc_msgSend$authenticationAction:failing:
+ _objc_msgSend$authenticationAction:failing:reply:
+ _objc_msgSend$authenticationAttemptFailedForEvent:
+ _objc_msgSend$authenticationAttemptFailedForEvent:reply:
+ _objc_msgSend$authenticationStartedForEvent:
+ _objc_msgSend$authenticationStartedForEvent:reply:
+ _objc_msgSend$authenticationSuccessfulForEvent:
+ _objc_msgSend$authenticationSuccessfulForEvent:reply:
+ _objc_msgSend$compact
+ _objc_msgSend$connectSessionForContext:reply:
+ _objc_msgSend$finishWithReply:
+ _objc_msgSend$finished
+ _objc_msgSend$initWithDialogID:bundleID:
+ _objc_msgSend$initWithSession:contextUUID:connected:workQueue:
+ _objc_msgSend$mergeAnalyticsData:
+ _objc_msgSend$mergeBiomeEvent:
+ _objc_msgSend$mergeEvaluationAnalytics:
+ _objc_msgSend$remoteObjectInterface
+ _objc_msgSend$sessionForContextUUID:
+ _objc_msgSend$startSessionForContext:dialogID:bundleID:reply:
+ _objc_msgSend$untrackEvaluationAnalytics:
+ _objc_msgSend$updateContextUUID:reply:
+ _objc_msgSend$weakObjectsPointerArray
- -[LACAnalyticsData authenticationAction:dismissing:]
- -[LACAnalyticsData authenticationResult:event:]
- -[LACAnalyticsData session]
- -[LACAnalyticsData setSession:]
- -[LACAnalyticsSession dirty]
- -[LACAnalyticsSession setAnalyticsData:]
- -[LACAnalyticsSession setDirty:]
- -[LACBiomeDialogEvent addAction:dismissing:]
- _LACBiomeDialogIDViewController
- _LACLogBiome
- _LACLogBiome.__logObj
- _LACLogBiome.cold.1
- _LACLogBiome.onceToken
- _OBJC_IVAR_$_LACAnalyticsData._session
- _OBJC_IVAR_$_LACAnalyticsSession._dirty
- ___LACLogBiome_block_invoke
- _objc_msgSend$addAction:dismissing:
- _objc_msgSend$dirty
- _objc_msgSend$setAnalyticsData:
- _objc_msgSend$setDirty:
CStrings:
+ "%{public}@ created: %{public}@"
+ "%{public}@ found %{public}@ %{public}s"
+ "%{public}@ has merged %{public}@"
+ "%{public}@ is no longer tracking %{public}@"
+ "%{public}@ is now tracking %{public}@"
+ "%{public}@: no context for session update"
+ "%{public}@: no session for authentication action"
+ "%{public}@: no session for failed authentication attempt"
+ "%{public}@: no session for starting authentication"
+ "%{public}@: no session for successful authentication"
+ "%{public}@: no session for updated context"
+ "%{public}@: no session to finish"
+ "<LACAnalyticsData %p; %@>"
+ "<LACAnalyticsSession %p; dialogID: %@, evaluationAnalytics: %u>"
+ "@\"<LACAnalyticsSessionXPC>\""
+ "@\"NSPointerArray\""
+ "@44@0:8@16@24B32@36"
+ "Allow"
+ "Analytics"
+ "B32@0:8@16@?24"
+ "Can't merge %{public}@ into %{public}@, data is not tracked by this session."
+ "Cancel"
+ "ConfirmedPassword"
+ "Connected to %{public}@ for contextUUID: %{public}@"
+ "Deny"
+ "Fallback"
+ "FallbackInternal"
+ "Invalid LACAnalyticsAction value: %d"
+ "LACAnalyticsCollecting"
+ "LACAnalyticsServiceXPC"
+ "LACAnalyticsServiceXPCHost"
+ "LACAnalyticsSessionClient"
+ "LACAnalyticsSessionXPC"
+ "LACAnalyticsSessionXPCHost"
+ "No active analytics session for %@"
+ "No session exists for this context"
+ "Session already exists for this context"
+ "Started %{public}@ for contextUUID: %{public}@"
+ "T@\"<LACContext>\",&,N"
+ "T@\"LACAnalyticsData\",R,N,V_analyticsData"
+ "T@\"LACAnalyticsSession\",R,N,V_session"
+ "T@\"NSUUID\",R,N,V_contextUUID"
+ "TB,R,N,V_finished"
+ "UpdatedUserName"
+ "_analyticsSession"
+ "_bootstrapServiceWithError:"
+ "_callBlockOnSynchronousRemoteObjectProxy:"
+ "_checkQueueAndSessionWithAction:replyOnFailure:"
+ "_connected"
+ "_connectionDidClose:"
+ "_connectionWithError:"
+ "_donateDialogEvent:request:"
+ "_evaluationAnalytics"
+ "_finished"
+ "_sessions"
+ "addAction:failing:"
+ "addPointer:"
+ "arrayByAddingObjectsFromArray:"
+ "authenticationAction:%{public}@ failing:%d for %{public}@: %{public}@"
+ "authenticationAction:failing:"
+ "authenticationAction:failing:reply:"
+ "authenticationAttemptFailedForEvent:"
+ "authenticationAttemptFailedForEvent:%{public}@ for %{public}@: %{public}@"
+ "authenticationAttemptFailedForEvent:reply:"
+ "authenticationStartedForEvent:%{public}@ for %{public}@: %{public}@"
+ "authenticationStartedForEvent:reply:"
+ "authenticationSuccessfulForEvent:"
+ "authenticationSuccessfulForEvent:%{public}@ for %{public}@: %{public}@"
+ "authenticationSuccessfulForEvent:reply:"
+ "compact"
+ "connectSessionForContext:%{public}@ on %{public}@: %{public}@"
+ "connectSessionForContext:reply:"
+ "connectToExistingSession"
+ "finishSession"
+ "finishSession for %{public}@: %{public}@"
+ "finishWithReply:"
+ "finished"
+ "finishing"
+ "initWithAnalyticsSession:"
+ "initWithContext:"
+ "initWithSession:contextUUID:connected:workQueue:"
+ "interrupted"
+ "invalidated"
+ "kLAServiceTypeAnalytics"
+ "mergeAnalyticsData:"
+ "mergeBiomeEvent:"
+ "mergeEvaluationAnalytics:"
+ "recording authentication action"
+ "recording authentication success"
+ "recording failed authentication attempt"
+ "recording start of authentication"
+ "remoteObjectInterface"
+ "sessionForContextUUID:"
+ "setContext:"
+ "startSessionForContext:%{public}@ dialogID:%{public}@ bundleID:%{private}@ on %{public}@: %{public}@"
+ "startSessionForContext:dialogID:bundleID:reply:"
+ "startSessionForDialogID:bundleID:"
+ "trackEvaluationAnalytics:"
+ "untrackEvaluationAnalytics:"
+ "updateContext:%{public}@: %{public}@"
+ "updateContextUUID:reply:"
+ "v16@?0@\"<LACAnalyticsServiceXPC>\"8"
+ "v24@?0@\"<LACAnalyticsSessionXPC>\"8@\"NSError\"16"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"<LACAnalyticsSessionXPC>\"@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8q16@?<v@?B@\"NSError\">24"
+ "v36@0:8q16B24@?28"
+ "v36@0:8q16B24@?<v@?B@\"NSError\">28"
+ "v48@0:8@\"NSUUID\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"<LACAnalyticsSessionXPC>\"@\"NSError\">40"
+ "weakObjectsPointerArray"
- "<LACAnalyticsSession %p; dialogID: %@>"
- "Biome"
- "T@\"LACAnalyticsData\",&,N,V_analyticsData"
- "T@\"LACAnalyticsSession\",W,N,V_session"
- "TB,N,V_dirty"
- "_dirty"
- "addAction:dismissing:"
- "authenticationAction:dismissing:"
- "authenticationResult:event:"
- "com.apple.LocalAuthentication.ViewController"
- "dirty"
- "setDirty:"
- "setSession:"
- "v32@0:8q16q24"

```
