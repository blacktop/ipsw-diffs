## LocalAuthenticationCore

> `/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`

```diff

-2005.0.31.0.0
-  __TEXT.__text: 0xf5454
-  __TEXT.__auth_stubs: 0x23f0
-  __TEXT.__objc_methlist: 0x97e0
-  __TEXT.__const: 0x4ae4
-  __TEXT.__gcc_except_tab: 0x19f0
-  __TEXT.__oslogstring: 0x6381
-  __TEXT.__cstring: 0xde07
+2005.0.40.0.0
+  __TEXT.__text: 0xf8bd0
+  __TEXT.__auth_stubs: 0x2400
+  __TEXT.__objc_methlist: 0x9a98
+  __TEXT.__const: 0x4b14
+  __TEXT.__gcc_except_tab: 0x1a8c
+  __TEXT.__oslogstring: 0x6841
+  __TEXT.__cstring: 0xe017
   __TEXT.__dlopen_cstrs: 0x4bb
   __TEXT.__swift5_typeref: 0x1938
   __TEXT.__constg_swiftt: 0xf7c

   __TEXT.__swift5_fieldmd: 0xa40
   __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_assocty: 0x210
-  __TEXT.__swift5_capture: 0xc5c
+  __TEXT.__swift5_capture: 0xc8c
   __TEXT.__swift5_proto: 0x164
   __TEXT.__swift5_types: 0xd4
   __TEXT.__swift_as_entry: 0xd4
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift_as_ret: 0xd8
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x41d0
-  __TEXT.__eh_frame: 0x22c0
-  __TEXT.__objc_classname: 0x21c5
-  __TEXT.__objc_methname: 0xf7e2
-  __TEXT.__objc_methtype: 0x4769
-  __TEXT.__objc_stubs: 0xa400
-  __DATA_CONST.__got: 0xae8
-  __DATA_CONST.__const: 0x4870
-  __DATA_CONST.__objc_classlist: 0x818
-  __DATA_CONST.__objc_protolist: 0x618
+  __TEXT.__unwind_info: 0x43d8
+  __TEXT.__eh_frame: 0x2310
+  __TEXT.__objc_classname: 0x2260
+  __TEXT.__objc_methname: 0xfbc5
+  __TEXT.__objc_methtype: 0x48d2
+  __TEXT.__objc_stubs: 0xa760
+  __DATA_CONST.__got: 0xb08
+  __DATA_CONST.__const: 0x49e0
+  __DATA_CONST.__objc_classlist: 0x830
+  __DATA_CONST.__objc_protolist: 0x630
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a98
-  __DATA_CONST.__objc_protorefs: 0x260
-  __DATA_CONST.__objc_superrefs: 0x4c0
+  __DATA_CONST.__objc_selrefs: 0x3b88
+  __DATA_CONST.__objc_protorefs: 0x270
+  __DATA_CONST.__objc_superrefs: 0x4e0
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x1208
-  __AUTH_CONST.__const: 0x39a0
-  __AUTH_CONST.__cfstring: 0x6380
-  __AUTH_CONST.__objc_const: 0x38bf8
+  __AUTH_CONST.__auth_got: 0x1210
+  __AUTH_CONST.__const: 0x3a38
+  __AUTH_CONST.__cfstring: 0x65a0
+  __AUTH_CONST.__objc_const: 0x39bc0
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x3128
+  __AUTH.__objc_data: 0x3218
   __AUTH.__data: 0xbf0
-  __DATA.__objc_ivar: 0x80c
-  __DATA.__data: 0x4ea0
-  __DATA.__bss: 0x2ca1
+  __DATA.__objc_ivar: 0x834
+  __DATA.__data: 0x4fc0
+  __DATA.__bss: 0x2cb1
   __DATA.__common: 0xa0
   __DATA_DIRTY.__objc_data: 0x2828
   __DATA_DIRTY.__data: 0x4e0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 225EEA0D-EB93-3BAE-AE2F-04F115079CB3
-  Functions: 6300
-  Symbols:   21871
-  CStrings:  6746
+  UUID: DEDB90F2-09EC-38CA-9D13-039BE6AD051F
+  Functions: 6375
+  Symbols:   22145
+  CStrings:  6860
 
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
+ GCC_except_table22
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC24loadPersistedEvaluations10completionyySayAA020LACDTOMutablePendingeF0CGSg_s5Error_pSgtc_tFyyYacfU_TA.53
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC24loadPersistedEvaluations10completionyySayAA020LACDTOMutablePendingeF0CGSg_s5Error_pSgtc_tFyyYacfU_TA.53TQ0_
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC24loadPersistedEvaluations10completionyySayAA020LACDTOMutablePendingeF0CGSg_s5Error_pSgtc_tFyyYacfU_TA.53Tu
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC7persist33_2F3A14333F740D7E8D468D748269021ELLyyFyyYacfU_TA.58
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC7persist33_2F3A14333F740D7E8D468D748269021ELLyyFyyYacfU_TA.58TQ0_
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC7persist33_2F3A14333F740D7E8D468D748269021ELLyyFyyYacfU_TA.58Tu
+ _$sSS11utf8CStrings15ContiguousArrayVys4Int8VGvg
+ _$sScPSgWOc
+ _$sScTss5NeverORs_rlE4name8priority9operationScTyxABGSSSg_ScPSgxyYaYAcntcfCyt_Tt2g5
+ _$sScTss5NeverORs_rlE4name8priority9operationScTyxABGSSSg_ScPSgxyYaYAcntcfCyt_Tt2gq5
+ _$sScTss5NeverORs_rlE8detached4name8priority9operationScTyxABGSSSg_ScPSgxyYaYAcntFZyt_Tt2g5
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5TA.41
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5TA.41TQ0_
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5TA.41Tu
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5TA.83
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5TA.83TQ0_
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5TA.83Tu
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TA.40
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TA.40TQ0_
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TA.40Tu
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
+ ___block_literal_global.151
+ _block_copy_helper.44
+ _block_copy_helper.48
+ _block_copy_helper.51
+ _block_copy_helper.54
+ _block_copy_helper.57
+ _block_copy_helper.60
+ _block_copy_helper.68
+ _block_descriptor.46
+ _block_descriptor.50
+ _block_descriptor.53
+ _block_descriptor.56
+ _block_descriptor.59
+ _block_descriptor.62
+ _block_descriptor.70
+ _block_destroy_helper.45
+ _block_destroy_helper.49
+ _block_destroy_helper.52
+ _block_destroy_helper.55
+ _block_destroy_helper.58
+ _block_destroy_helper.61
+ _block_destroy_helper.69
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
+ _objc_msgSend$sessionForContextUUID:
+ _objc_msgSend$startSessionForContext:dialogID:bundleID:reply:
+ _objc_msgSend$untrackEvaluationAnalytics:
+ _objc_msgSend$updateContextUUID:reply:
+ _objc_msgSend$weakObjectsPointerArray
+ _objectdestroy.62Tm
- -[LACAnalyticsData authenticationAction:dismissing:]
- -[LACAnalyticsData authenticationResult:event:]
- -[LACAnalyticsData session]
- -[LACAnalyticsData setSession:]
- -[LACAnalyticsSession dirty]
- -[LACAnalyticsSession setAnalyticsData:]
- -[LACAnalyticsSession setDirty:]
- -[LACBiomeDialogEvent addAction:dismissing:]
- _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC24loadPersistedEvaluations10completionyySayAA020LACDTOMutablePendingeF0CGSg_s5Error_pSgtc_tFyyYacfU_TA.48
- _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC24loadPersistedEvaluations10completionyySayAA020LACDTOMutablePendingeF0CGSg_s5Error_pSgtc_tFyyYacfU_TA.48TQ0_
- _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC24loadPersistedEvaluations10completionyySayAA020LACDTOMutablePendingeF0CGSg_s5Error_pSgtc_tFyyYacfU_TA.48Tu
- _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC7persist33_2F3A14333F740D7E8D468D748269021ELLyyFyyYacfU_TA.53
- _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC7persist33_2F3A14333F740D7E8D468D748269021ELLyyFyyYacfU_TA.53TQ0_
- _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC7persist33_2F3A14333F740D7E8D468D748269021ELLyyFyyYacfU_TA.53Tu
- _$sScTss5NeverORs_rlE8detached8priority9operationScTyxABGScPSg_xyYaYAcntFZyt_Tt1g5
- _$sScTss5NeverORs_rlE8priority9operationScTyxABGScPSg_xyYaYAcntcfCyt_Tt1g5
- _$sScTss5NeverORs_rlE8priority9operationScTyxABGScPSg_xyYaYAcntcfCyt_Tt1gq5
- _LACBiomeDialogIDViewController
- _OBJC_IVAR_$_LACAnalyticsData._session
- _OBJC_IVAR_$_LACAnalyticsSession._dirty
- _block_copy_helper.43
- _block_copy_helper.49
- _block_copy_helper.52
- _block_copy_helper.55
- _block_copy_helper.63
- _block_descriptor.45
- _block_descriptor.51
- _block_descriptor.54
- _block_descriptor.57
- _block_descriptor.65
- _block_destroy_helper.44
- _block_destroy_helper.50
- _block_destroy_helper.53
- _block_destroy_helper.56
- _block_destroy_helper.64
- _objc_msgSend$addAction:dismissing:
- _objc_msgSend$dirty
- _objc_msgSend$setAnalyticsData:
- _objc_msgSend$setDirty:
- _objectdestroy.57Tm
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
+ "@\"<LACContext>\""
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
