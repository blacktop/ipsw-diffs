## LocalAuthenticationCore

> `/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/Versions/A/LocalAuthenticationCore`

```diff

-1656.0.58.0.1
-  __TEXT.__text: 0xa3b78
-  __TEXT.__auth_stubs: 0x1b30
-  __TEXT.__objc_methlist: 0x4a90
-  __TEXT.__const: 0x2fe4
-  __TEXT.__cstring: 0xa3f9
-  __TEXT.__oslogstring: 0x253e
-  __TEXT.__gcc_except_tab: 0xdc8
+1656.0.75.0.0
+  __TEXT.__text: 0xa6204
+  __TEXT.__auth_stubs: 0x1b90
+  __TEXT.__objc_methlist: 0x4d50
+  __TEXT.__const: 0x3014
+  __TEXT.__cstring: 0xa5d9
+  __TEXT.__oslogstring: 0x27b6
+  __TEXT.__gcc_except_tab: 0xe80
   __TEXT.__dlopen_cstrs: 0xa2
-  __TEXT.__swift5_typeref: 0xfd2
-  __TEXT.__constg_swiftt: 0xa30
-  __TEXT.__swift5_reflstr: 0x627
-  __TEXT.__swift5_fieldmd: 0x724
+  __TEXT.__swift5_typeref: 0xfc2
+  __TEXT.__constg_swiftt: 0xa48
+  __TEXT.__swift5_reflstr: 0x617
+  __TEXT.__swift5_fieldmd: 0x730
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_assocty: 0x108
-  __TEXT.__swift5_capture: 0x7a0
+  __TEXT.__swift5_capture: 0x778
   __TEXT.__swift5_proto: 0xcc
   __TEXT.__swift5_types: 0x8c
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x2d00
+  __TEXT.__unwind_info: 0x2d78
   __TEXT.__eh_frame: 0x17a8
-  __TEXT.__objc_classname: 0x16ad
-  __TEXT.__objc_methname: 0x88f8
-  __TEXT.__objc_methtype: 0x2824
-  __TEXT.__objc_stubs: 0x6340
-  __DATA_CONST.__got: 0x760
-  __DATA_CONST.__const: 0x1d30
-  __DATA_CONST.__objc_classlist: 0x590
-  __DATA_CONST.__objc_protolist: 0x3c8
+  __TEXT.__objc_classname: 0x1778
+  __TEXT.__objc_methname: 0x8fb2
+  __TEXT.__objc_methtype: 0x2948
+  __TEXT.__objc_stubs: 0x6740
+  __DATA_CONST.__got: 0x770
+  __DATA_CONST.__const: 0x1d48
+  __DATA_CONST.__objc_classlist: 0x5a8
+  __DATA_CONST.__objc_protolist: 0x3e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x20f0
+  __DATA_CONST.__objc_selrefs: 0x2208
   __DATA_CONST.__objc_protorefs: 0x168
-  __DATA_CONST.__objc_superrefs: 0x388
+  __DATA_CONST.__objc_superrefs: 0x398
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0xda8
-  __AUTH_CONST.__auth_ptr: 0x388
+  __AUTH_CONST.__auth_got: 0xdd8
+  __AUTH_CONST.__auth_ptr: 0x378
   __AUTH_CONST.__const: 0x3ad8
-  __AUTH_CONST.__cfstring: 0x3580
-  __AUTH_CONST.__objc_const: 0x27a08
+  __AUTH_CONST.__cfstring: 0x3700
+  __AUTH_CONST.__objc_const: 0x28c98
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x3d38
-  __AUTH.__data: 0xb18
-  __DATA.__objc_ivar: 0x590
-  __DATA.__data: 0x33c0
-  __DATA.__bss: 0x19f1
+  __AUTH.__objc_data: 0x3e40
+  __AUTH.__data: 0xb08
+  __DATA.__objc_ivar: 0x5d8
+  __DATA.__data: 0x3560
+  __DATA.__bss: 0x1a01
   __DATA.__common: 0xb0
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3877
-  Symbols:   10556
-  CStrings:  1407
+  Functions: 3938
+  Symbols:   10757
+  CStrings:  1421
 
Symbols:
+ $s23LocalAuthenticationCore25LACOnenessControllerModelC18postProcessRequest_6result10completionySo013LACEvaluationI0_p_So0L6ResultCyAIctFys5Error_pSgcfU_TA.25
+ $s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC13isInvalidatedSbvM.resume.0
+ $sSo19LACEvaluationResultCIeyBy_ABIegg_TRTA.32
+ +[LACDTOMutableNotificationAction doNotStartNewDelayAction]
+ +[LACDTOMutableNotificationAction startNewDelayAction]
+ +[LACDTOMutableNotificationCategory newSecurityDelayRequiredCategory]
+ +[LACDTOMutableNotificationCategory securityDelayEndedCategory]
+ +[LACEnvironmentMechanism environmentMechanismForUser:auditToken:dependencies:error:]
+ +[LACEnvironmentMechanismBiometry environmentMechanismForUser:auditToken:dependencies:error:]
+ +[LACEnvironmentMechanismUserPassword environmentMechanismForUser:auditToken:dependencies:error:]
+ +[LACEnvironmentState environmentStateForUser:auditToken:dependencies:error:]
+ +[LACPreboardAMFIHelper completeCurrentBootModeWithSuccess:]
+ +[LACPreboardAMFIHelper useCase]
+ -[LACDTOMutableNotificationAction .cxx_destruct]
+ -[LACDTOMutableNotificationAction identifier]
+ -[LACDTOMutableNotificationAction initWithIdentifier:title:isTitleLocalized:isDestructive:]
+ -[LACDTOMutableNotificationAction isDestructive]
+ -[LACDTOMutableNotificationAction isTitleLocalized]
+ -[LACDTOMutableNotificationAction setIdentifier:]
+ -[LACDTOMutableNotificationAction setIsDestructive:]
+ -[LACDTOMutableNotificationAction setIsTitleLocalized:]
+ -[LACDTOMutableNotificationAction setTitle:]
+ -[LACDTOMutableNotificationAction title]
+ -[LACDTOMutableNotificationCategory .cxx_destruct]
+ -[LACDTOMutableNotificationCategory actions]
+ -[LACDTOMutableNotificationCategory hiddenPreviewShowsTitle]
+ -[LACDTOMutableNotificationCategory identifier]
+ -[LACDTOMutableNotificationCategory initWithIdentifier:actions:hiddenPreviewShowsTitle:]
+ -[LACDTOMutableNotificationCategory setActions:]
+ -[LACDTOMutableNotificationCategory setHiddenPreviewShowsTitle:]
+ -[LACDTOMutableNotificationCategory setIdentifier:]
+ -[LACDTOMutablePolicyEvaluationRequest payload]
+ -[LACDTOMutablePolicyEvaluationRequest setPayload:]
+ -[LACDTOMutablePolicyEvaluationRequest updatePayload:]
+ -[LACDTONotificationFactory _securityDelayEndedNotificationWithIdentifier:body:callbackURL:after:maxAge:]
+ -[LACDTONotificationFactory newSecurityDelayRequiredNotification]
+ -[LACDTONotificationFactory securityDelayEndedNotificationForPendingEvaluation:after:validity:]
+ -[LACDTONotificationManager _securityDelayManager]
+ -[LACDTONotificationManager cancelPreviousNewSecurityDelayRequiredNotificationWithCompletion:]
+ -[LACDTONotificationManager cancelPreviousSecurityDelayFinishedNotificationForPendingEvaluation:scheduledOnly:completion:]
+ -[LACDTONotificationManager delegate]
+ -[LACDTONotificationManager notificationManager:didRespondToNotification:fromCategory:withAction:completionHandler:]
+ -[LACDTONotificationManager postNewSecurityDelayRequiredNotificationWithCompletion:]
+ -[LACDTONotificationManager scheduleSecurityDelayFinishedNotificationForPendingEvaluation:after:validity:completion:]
+ -[LACDTONotificationManager setDelegate:]
+ -[LACDTOPendingPolicyEvaluationController _cancelPreviousNotificationForPendingEvaluationRecord:scheduledOnly:]
+ -[LACDTOPendingPolicyEvaluationController _cancelPreviousNotificationForRatchetRestartWithRatchetState:]
+ -[LACDTOPendingPolicyEvaluationController _isRatchetRestartRequest:]
+ -[LACDTOPendingPolicyEvaluationController _postNotificationForRatchetRestartIfNeeded]
+ -[LACDTOPendingPolicyEvaluationController _postNotificationForRatchetRestartIfNeeded].cold.1
+ -[LACDTOPendingPolicyEvaluationController _pruneInvalidatedEvaluations]
+ -[LACDTOPendingPolicyEvaluationController _registerNotificationObservers]
+ -[LACDTOPendingPolicyEvaluationController _removePendingEvaluationRecordForRequest:completion:]
+ -[LACDTOPendingPolicyEvaluationController _restartRatchetForInvalidatedEvaluations]
+ -[LACDTOPendingPolicyEvaluationController _scheduleNotificationForPendingEvaluationRecord:after:validity:]
+ -[LACDTOPendingPolicyEvaluationController _scheduleNotificationForRatchetRestart]
+ -[LACDTOPendingPolicyEvaluationController initWithRatchetStateProvider:ratchetHandler:device:evaluationIdentifierFactory:persistentStore:workQueue:]
+ -[LACDTOPendingPolicyEvaluationController notificationManager:didReceiveUserAction:completionHandler:]
+ -[LACEnvironmentDependencies .cxx_destruct]
+ -[LACEnvironmentDependencies biometryHelper]
+ -[LACEnvironmentDependencies onenessSessionMonitor]
+ -[LACEnvironmentDependencies passcodeHelper]
+ -[LACEnvironmentDependencies setBiometryHelper:]
+ -[LACEnvironmentDependencies setOnenessSessionMonitor:]
+ -[LACEnvironmentDependencies setPasscodeHelper:]
+ -[LACEnvironmentServiceXPCHost initWithDependencies:workQueue:]
+ -[LACFlags flagCompanionMockDevicesKey]
+ -[LACFlags valueForFlagCompanionMockDevices]
+ -[LACUNManager cancelNotificationsWithIdentifiers:scheduledOnly:completion:]
+ -[LACUNManager delegate]
+ -[LACUNManager initWithBundleIdentifier:categories:]
+ -[LACUNManager setDelegate:]
+ -[LACUNManagerPool sharedInstanceWithBundleIdentifier:categories:replyQueue:]
+ -[LACUNManagerQueueDecorator cancelNotificationsWithIdentifiers:scheduledOnly:completion:]
+ -[LACUNManagerQueueDecorator delegate]
+ -[LACUNManagerQueueDecorator notificationManager:didRespondToNotification:fromCategory:withAction:completionHandler:]
+ -[LACUNManagerQueueDecorator setDelegate:]
+ -[LACUNMutableNotification setShouldDisplayActionsInline:]
+ -[LACUNMutableNotification shouldDisplayActionsInline]
+ GCC_except_table23
+ GCC_except_table33
+ GCC_except_table49
+ GCC_except_table57
+ GCC_except_table65
+ GCC_except_table75
+ GCC_except_table77
+ GCC_except_table82
+ GCC_except_table86
+ GCC_except_table87
+ LACLogContext.__logObj
+ LACLogContext.onceToken
+ OBJC_IVAR_$_LACDTOMutableNotificationAction._identifier
+ OBJC_IVAR_$_LACDTOMutableNotificationAction._isDestructive
+ OBJC_IVAR_$_LACDTOMutableNotificationAction._isTitleLocalized
+ OBJC_IVAR_$_LACDTOMutableNotificationAction._title
+ OBJC_IVAR_$_LACDTOMutableNotificationCategory._actions
+ OBJC_IVAR_$_LACDTOMutableNotificationCategory._hiddenPreviewShowsTitle
+ OBJC_IVAR_$_LACDTOMutableNotificationCategory._identifier
+ OBJC_IVAR_$_LACDTOMutablePolicyEvaluationRequest._payload
+ OBJC_IVAR_$_LACDTONotificationManager._delegate
+ OBJC_IVAR_$_LACDTOPendingPolicyEvaluationController._device
+ OBJC_IVAR_$_LACDTOPendingPolicyEvaluationController._shouldPostRestartRatchetPrompt
+ OBJC_IVAR_$_LACEnvironmentDependencies._biometryHelper
+ OBJC_IVAR_$_LACEnvironmentDependencies._onenessSessionMonitor
+ OBJC_IVAR_$_LACEnvironmentDependencies._passcodeHelper
+ OBJC_IVAR_$_LACEnvironmentServiceXPCHost._dependencies
+ OBJC_IVAR_$_LACUNManager.delegate
+ OBJC_IVAR_$_LACUNManagerQueueDecorator._delegate
+ OBJC_IVAR_$_LACUNMutableNotification._shouldDisplayActionsInline
+ _$s23LocalAuthenticationCore25LACOnenessControllerModelC19handleSessionUpdate019_CCCEE7302AA4D596C7M12F88F5FCDE119LLyyF
+ _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC02isE6ActiveSbvg
+ _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC02isE6ActiveSbvgTo
+ _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC02isE6ActiveSbvpMV
+ _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC15sessionProvider10replyQueueAcA0dE9Providing_p_So17OS_dispatch_queueCtcfCTfq4enn_nTf4ggn_n
+ _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC15sessionProvider10replyQueueAcA0dE9Providing_p_So17OS_dispatch_queueCtcfcTf4enn_nAA0deI3AKSC_Tg5Tf4ngn_n
+ _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC15sessionProvider10replyQueueAcA0dE9Providing_p_So17OS_dispatch_queueCtcfcTf4enn_nTf4ngn_n
+ _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC3addyySo0deF8Observer_pF
+ _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC3addyySo0deF8Observer_pFTm
+ _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC3addyySo0deF8Observer_pFTo
+ _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC3addyySo0deF8Observer_pFToTm
+ _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC3addyySo0deF8Observer_pFyyYbcfU_TA
+ _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC3addyySo0deF8Observer_pFyyYbcfU_Tm
+ _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC6removeyySo0deF8Observer_pF
+ _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC6removeyySo0deF8Observer_pFTo
+ _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC6removeyySo0deF8Observer_pFyyYbcfU_TA
+ _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC9observers33_E311F17ECB56FF89C3803330CB7C7A9DLLSo11NSHashTableCySo0deF8Observer_pGvpWvd
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC13isInvalidatedSbvM
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC13isInvalidatedSbvMTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC13isInvalidatedSbvMTq
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC13isInvalidatedSbvg
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC13isInvalidatedSbvgTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC13isInvalidatedSbvgTo
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC13isInvalidatedSbvgTq
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC13isInvalidatedSbvpMV
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC13isInvalidatedSbvpWvd
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC13isInvalidatedSbvs
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC13isInvalidatedSbvsTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC13isInvalidatedSbvsTo
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC13isInvalidatedSbvsTq
+ _$sSS10describingSSx_tclufC
+ _$sSo24LACOnenessSessionMonitorC23LocalAuthenticationCoreE02isB6ActiveSbvg
+ _$sSo24LACOnenessSessionMonitorC23LocalAuthenticationCoreE02isB6ActiveSbvgTo
+ _$sSo24LACOnenessSessionMonitorC23LocalAuthenticationCoreE02isB6ActiveSbvpMV
+ _$sSo24LACOnenessSessionMonitorC23LocalAuthenticationCoreE12isMonitoringSbvgTm
+ _$sSo24LACOnenessSessionMonitorC23LocalAuthenticationCoreE12isMonitoringSbvgToTm
+ _$sSo24LACOnenessSessionMonitorC23LocalAuthenticationCoreE3addyySo0abC8Observer_pF
+ _$sSo24LACOnenessSessionMonitorC23LocalAuthenticationCoreE3addyySo0abC8Observer_pFTm
+ _$sSo24LACOnenessSessionMonitorC23LocalAuthenticationCoreE3addyySo0abC8Observer_pFTo
+ _$sSo24LACOnenessSessionMonitorC23LocalAuthenticationCoreE3addyySo0abC8Observer_pFToTm
+ _$sSo24LACOnenessSessionMonitorC23LocalAuthenticationCoreE6removeyySo0abC8Observer_pF
+ _$sSo24LACOnenessSessionMonitorC23LocalAuthenticationCoreE6removeyySo0abC8Observer_pFTo
+ _$sSo32LACOnenessSessionMonitorObserver_pMD
+ _$ss22KeyedDecodingContainerV6decode_6forKeyS2bm_xtKF
+ _$ss22KeyedEncodingContainerV6encode_6forKeyySb_xtKF
+ _LACDTONotificationActionIdentifierDoNotStartNewDelay
+ _LACDTONotificationActionIdentifierStartNewDelay
+ _LACDTONotificationCategoryIdentifierNewSecurityDelayRequired
+ _LACDTONotificationCategoryIdentifierSecurityDelayEnded
+ _LACDTONotificationNewSecurityDelayRequired
+ _LACDTOPolicyEvaluationRequestPayloadKeyAssociatedIdentifiers
+ _LACLogContext
+ _LACPolicyOptionBeginRatchetStrictModeLocalizedText
+ _OBJC_$_PROP_LIST_LACUNManager.71
+ _OBJC_CLASS_$_LACDTOMutableNotificationAction
+ _OBJC_CLASS_$_LACDTOMutableNotificationCategory
+ _OBJC_CLASS_$_LACEnvironmentDependencies
+ _OBJC_METACLASS_$_LACDTOMutableNotificationAction
+ _OBJC_METACLASS_$_LACDTOMutableNotificationCategory
+ _OBJC_METACLASS_$_LACEnvironmentDependencies
+ _PROTOCOLS__TtC23LocalAuthenticationCore29LACOnenessSessionMonitorModel.13
+ _PROTOCOLS__TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation.14
+ __106-[LACDTOPendingPolicyEvaluationController _scheduleNotificationForPendingEvaluationRecord:after:validity:]_block_invoke.cold.1
+ __117-[LACDTONotificationManager scheduleSecurityDelayFinishedNotificationForPendingEvaluation:after:validity:completion:]_block_invoke.cold.1
+ __66-[LACDTOPendingPolicyEvaluationController _loadPendingEvaluations]_block_invoke.79
+ __66-[LACDTOPendingPolicyEvaluationController _loadPendingEvaluations]_block_invoke.79.cold.1
+ __84-[LACDTONotificationManager postNewSecurityDelayRequiredNotificationWithCompletion:]_block_invoke.cold.1
+ __85-[LACDTOPendingPolicyEvaluationController _postNotificationForRatchetRestartIfNeeded]_block_invoke.cold.1
+ __85-[LACDTOPendingPolicyEvaluationController notificationCenter:didReceiveNotification:]_block_invoke.10
+ __94-[LACDTOPendingPolicyEvaluationController _addPendingEvaluationRecordForRequest:currentState:]_block_invoke.35
+ __95-[LACDTOPendingPolicyEvaluationController _removePendingEvaluationRecordForRequest:completion:]_block_invoke.43
+ __99-[LACDTOPendingPolicyEvaluationController _removePendingEvaluationRecordWithIdentifier:completion:]_block_invoke.46
+ __OBJC_$_CLASS_METHODS_LACDTOMutableNotificationAction
+ __OBJC_$_CLASS_METHODS_LACDTOMutableNotificationCategory
+ __OBJC_$_CLASS_PROP_LIST_LACPreboardAMFIHelper
+ __OBJC_$_INSTANCE_METHODS_LACDTOMutableNotificationAction
+ __OBJC_$_INSTANCE_METHODS_LACDTOMutableNotificationCategory
+ __OBJC_$_INSTANCE_METHODS_LACEnvironmentDependencies
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOMutableNotificationAction
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOMutableNotificationCategory
+ __OBJC_$_INSTANCE_VARIABLES_LACEnvironmentDependencies
+ __OBJC_$_PROP_LIST_LACDTOMutableNotificationAction
+ __OBJC_$_PROP_LIST_LACDTOMutableNotificationCategory
+ __OBJC_$_PROP_LIST_LACDTONotificationManager
+ __OBJC_$_PROP_LIST_LACEnvironmentDependencies
+ __OBJC_$_PROP_LIST_LACUNNotificationAction
+ __OBJC_$_PROP_LIST_LACUNNotificationCategory
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTONotificationManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACOnenessSessionMonitorObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACOnenessSessionMonitorObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACOnenessSessionMonitorObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACUNManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACUNManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACUNNotificationAction
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACUNNotificationCategory
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTONotificationManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACOnenessSessionMonitorObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACOnenessSessionMonitorObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACOnenessSessionMonitorObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACUNManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACUNManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACUNNotificationAction
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACUNNotificationCategory
+ __OBJC_$_PROTOCOL_REFS_LACDTONotificationManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_LACOnenessSessionMonitorObserver
+ __OBJC_$_PROTOCOL_REFS_LACOnenessSessionMonitorObserver
+ __OBJC_$_PROTOCOL_REFS_LACOnenessSessionMonitorObserver
+ __OBJC_$_PROTOCOL_REFS_LACUNManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_LACUNManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_LACUNNotificationAction
+ __OBJC_$_PROTOCOL_REFS_LACUNNotificationCategory
+ __OBJC_CLASS_PROTOCOLS_$_LACDTOMutableNotificationAction
+ __OBJC_CLASS_PROTOCOLS_$_LACDTOMutableNotificationCategory
+ __OBJC_CLASS_PROTOCOLS_$_LACDTONotificationManager
+ __OBJC_CLASS_RO_$_LACDTOMutableNotificationAction
+ __OBJC_CLASS_RO_$_LACDTOMutableNotificationCategory
+ __OBJC_CLASS_RO_$_LACEnvironmentDependencies
+ __OBJC_LABEL_PROTOCOL_$_LACDTONotificationManagerDelegate
+ __OBJC_LABEL_PROTOCOL_$_LACOnenessSessionMonitorObserver
+ __OBJC_LABEL_PROTOCOL_$_LACUNManagerDelegate
+ __OBJC_LABEL_PROTOCOL_$_LACUNNotificationAction
+ __OBJC_LABEL_PROTOCOL_$_LACUNNotificationCategory
+ __OBJC_METACLASS_RO_$_LACDTOMutableNotificationAction
+ __OBJC_METACLASS_RO_$_LACDTOMutableNotificationCategory
+ __OBJC_METACLASS_RO_$_LACEnvironmentDependencies
+ __OBJC_PROTOCOL_$_LACDTONotificationManagerDelegate
+ __OBJC_PROTOCOL_$_LACOnenessSessionMonitorObserver
+ __OBJC_PROTOCOL_$_LACUNManagerDelegate
+ __OBJC_PROTOCOL_$_LACUNNotificationAction
+ __OBJC_PROTOCOL_$_LACUNNotificationCategory
+ ___104-[LACDTOPendingPolicyEvaluationController _cancelPreviousNotificationForRatchetRestartWithRatchetState:]_block_invoke
+ ___106-[LACDTOPendingPolicyEvaluationController _scheduleNotificationForPendingEvaluationRecord:after:validity:]_block_invoke
+ ___111-[LACDTOPendingPolicyEvaluationController _cancelPreviousNotificationForPendingEvaluationRecord:scheduledOnly:]_block_invoke
+ ___117-[LACDTONotificationManager scheduleSecurityDelayFinishedNotificationForPendingEvaluation:after:validity:completion:]_block_invoke
+ ___117-[LACUNManagerQueueDecorator notificationManager:didRespondToNotification:fromCategory:withAction:completionHandler:]_block_invoke
+ ___122-[LACDTONotificationManager cancelPreviousSecurityDelayFinishedNotificationForPendingEvaluation:scheduledOnly:completion:]_block_invoke
+ ___44-[LACFlags valueForFlagCompanionMockDevices]_block_invoke
+ ___77-[LACUNManagerPool sharedInstanceWithBundleIdentifier:categories:replyQueue:]_block_invoke
+ ___84-[LACDTONotificationManager postNewSecurityDelayRequiredNotificationWithCompletion:]_block_invoke
+ ___85-[LACDTOPendingPolicyEvaluationController _postNotificationForRatchetRestartIfNeeded]_block_invoke
+ ___90-[LACUNManagerQueueDecorator cancelNotificationsWithIdentifiers:scheduledOnly:completion:]_block_invoke
+ ___90-[LACUNManagerQueueDecorator cancelNotificationsWithIdentifiers:scheduledOnly:completion:]_block_invoke_2
+ ___90-[LACUNManagerQueueDecorator cancelNotificationsWithIdentifiers:scheduledOnly:completion:]_block_invoke_3
+ ___93+[LACEnvironmentMechanismBiometry environmentMechanismForUser:auditToken:dependencies:error:]_block_invoke
+ ___94-[LACDTONotificationManager cancelPreviousNewSecurityDelayRequiredNotificationWithCompletion:]_block_invoke
+ ___95-[LACDTOPendingPolicyEvaluationController _removePendingEvaluationRecordForRequest:completion:]_block_invoke
+ ___LACLogContext_block_invoke
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32bs40r_e5_v8?0l
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8l
+ ___block_descriptor_57_e8_32s40bs48w_e5_v8?0l
+ ___block_descriptor_80_e8_32s40s48s56s64bs72w_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56s64b72w
+ ___destroy_helper_block_e8_32s40s48s56s64s72w
+ __block_literal_global.106
+ __block_literal_global.65
+ __block_literal_global.86
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _flat unique So32LACOnenessSessionMonitorObserver_p
+ _objc_msgSend$_cancelPreviousNotificationForPendingEvaluationRecord:scheduledOnly:
+ _objc_msgSend$_cancelPreviousNotificationForRatchetRestartWithRatchetState:
+ _objc_msgSend$_isRatchetRestartRequest:
+ _objc_msgSend$_postNotificationForRatchetRestartIfNeeded
+ _objc_msgSend$_pruneInvalidatedEvaluations
+ _objc_msgSend$_registerNotificationObservers
+ _objc_msgSend$_removePendingEvaluationRecordForRequest:completion:
+ _objc_msgSend$_restartRatchetForInvalidatedEvaluations
+ _objc_msgSend$_scheduleNotificationForPendingEvaluationRecord:after:validity:
+ _objc_msgSend$_scheduleNotificationForRatchetRestart
+ _objc_msgSend$_securityDelayEndedNotificationWithIdentifier:body:callbackURL:after:maxAge:
+ _objc_msgSend$_securityDelayManager
+ _objc_msgSend$biometryHelper
+ _objc_msgSend$cancelNotificationsWithIdentifiers:scheduledOnly:completion:
+ _objc_msgSend$cancelPreviousNewSecurityDelayRequiredNotificationWithCompletion:
+ _objc_msgSend$cancelPreviousSecurityDelayFinishedNotificationForPendingEvaluation:scheduledOnly:completion:
+ _objc_msgSend$doNotStartNewDelayAction
+ _objc_msgSend$environmentMechanismForUser:auditToken:dependencies:error:
+ _objc_msgSend$environmentStateForUser:auditToken:dependencies:error:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$initWithBundleIdentifier:categories:
+ _objc_msgSend$initWithIdentifier:actions:hiddenPreviewShowsTitle:
+ _objc_msgSend$initWithIdentifier:title:isTitleLocalized:isDestructive:
+ _objc_msgSend$isInvalidated
+ _objc_msgSend$isSessionActive
+ _objc_msgSend$newSecurityDelayRequiredCategory
+ _objc_msgSend$newSecurityDelayRequiredNotification
+ _objc_msgSend$notificationManager:didReceiveUserAction:completionHandler:
+ _objc_msgSend$notificationManager:didRespondToNotification:fromCategory:withAction:completionHandler:
+ _objc_msgSend$onenessSessionMonitor
+ _objc_msgSend$passcodeHelper
+ _objc_msgSend$postNewSecurityDelayRequiredNotificationWithCompletion:
+ _objc_msgSend$restartRatchetWithIdentifier:
+ _objc_msgSend$scheduleSecurityDelayFinishedNotificationForPendingEvaluation:after:validity:completion:
+ _objc_msgSend$securityDelayEndedCategory
+ _objc_msgSend$securityDelayEndedNotificationForPendingEvaluation:after:validity:
+ _objc_msgSend$setActions:
+ _objc_msgSend$setHiddenPreviewShowsTitle:
+ _objc_msgSend$setIsDestructive:
+ _objc_msgSend$setIsInvalidated:
+ _objc_msgSend$setPayload:
+ _objc_msgSend$setShouldDisplayActionsInline:
+ _objc_msgSend$sharedInstanceWithBundleIdentifier:categories:replyQueue:
+ _objc_msgSend$shouldDisplayActionsInline
+ _objc_msgSend$startNewDelayAction
+ _symbolic So11NSHashTableCy______pG So32LACOnenessSessionMonitorObserverP
+ _symbolic _____SgXwz_Xx 23LocalAuthenticationCore29LACOnenessSessionMonitorModelC
+ _symbolic ______p So32LACOnenessSessionMonitorObserverP
+ block_copy_helper.18
+ block_copy_helper.26
+ block_copy_helper.36
+ block_copy_helper.45
+ block_copy_helper.61
+ block_copy_helper.9
+ block_descriptor.11
+ block_descriptor.20
+ block_descriptor.28
+ block_descriptor.38
+ block_descriptor.63
+ block_destroy_helper.10
+ block_destroy_helper.19
+ block_destroy_helper.27
+ block_destroy_helper.37
+ block_destroy_helper.46
+ block_destroy_helper.62
+ objectdestroy.3Tm
- $s23LocalAuthenticationCore25LACOnenessControllerModelC18postProcessRequest_6result10completionySo013LACEvaluationI0_p_So0L6ResultCyAIctFys5Error_pSgcfU_TA.42
- $s23LocalAuthenticationCore25LACOnenessControllerModelC19handleSessionUpdate019_CCCEE7302AA4D596C7M12F88F5FCDE119LLyyFySbcfU_TA.32
- $s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC8delegateSo0deF8Delegate_pSgvM.resume.0
- $sSo19LACEvaluationResultCIeyBy_ABIegg_TRTA.49
- +[LACEnvironmentMechanism environmentMechanismForUser:auditToken:error:]
- +[LACEnvironmentMechanismBiometry environmentMechanismForUser:auditToken:error:]
- +[LACEnvironmentMechanismUserPassword environmentMechanismForUser:auditToken:error:]
- +[LACEnvironmentState environmentStateForUser:auditToken:error:]
- +[LACOnenessSignpostEvent availabilityRequestDidFinish]
- +[LACOnenessSignpostEvent availabilityRequestWillStart]
- -[LACDTONotificationFactory securityDelayEndedNotificationForPendingEvaluation:after:maxAge:]
- -[LACDTONotificationFactory securityDelayEndedNotificationWithIdentifier:body:callbackURL:]
- -[LACDTONotificationFactory securityDelayEndedNotificationWithIdentifier:body:callbackURL:after:maxAge:]
- -[LACDTONotificationManager _securityDelayEndedManager]
- -[LACDTONotificationManager cancelPreviousSecurityDelayFinishedNotificationForPendingEvaluation:completion:]
- -[LACDTONotificationManager scheduleSecurityDelayFinishedNotificationForPendingEvaluation:after:maxAge:completion:]
- -[LACDTOPendingPolicyEvaluationController _cancelPreviousNotificationForPendingEvaluationRecord:]
- -[LACDTOPendingPolicyEvaluationController _registerObserverForTimeChanges]
- -[LACDTOPendingPolicyEvaluationController _scheduleNotificationForPendingEvaluationRecord:after:maxAge:]
- -[LACDTOPendingPolicyEvaluationController initWithRatchetStateProvider:ratchetHandler:evaluationIdentifierFactory:persistentStore:workQueue:]
- -[LACEnvironmentServiceXPCHost initWithWorkQueue:]
- -[LACFlags flagCompanionSessionMockDevicesKey]
- -[LACFlags valueForFlagCompanionSessionMockDevices]
- -[LACUNManager cancelNotificationsWithIdentifiers:completion:]
- -[LACUNManager initWithBundleIdentifier:categoryIdentifier:]
- -[LACUNManagerPool sharedInstanceWithBundleIdentifier:categoryIdentifier:replyQueue:]
- -[LACUNManagerQueueDecorator cancelNotificationsWithIdentifiers:completion:]
- GCC_except_table20
- GCC_except_table54
- GCC_except_table61
- GCC_except_table66
- GCC_except_table69
- GCC_except_table70
- _$s10ObjectiveC8ObjCBoolVIeyBy_SbIegy_TR
- _$s10ObjectiveC8ObjCBoolVIeyBy_SbIegy_TRTA
- _$s10ObjectiveC8ObjCBoolVMn
- _$s23LocalAuthenticationCore25LACOnenessControllerModelC15isSessionActiveSbvgySbcfU_TA
- _$s23LocalAuthenticationCore25LACOnenessControllerModelC19handleSessionUpdate019_CCCEE7302AA4D596C7M12F88F5FCDE119LLyyFySbcfU_
- _$s23LocalAuthenticationCore25LACOnenessControllerModelC19handleSessionUpdate019_CCCEE7302AA4D596C7M12F88F5FCDE119LLyyFySbcfU_TA
- _$s23LocalAuthenticationCore25LACOnenessControllerModelC25processAndEvaluateRequest019_CCCEE7302AA4D596C7N12F88F5FCDE119LL4withy10Foundation4UUIDV_tFySbcfU_
- _$s23LocalAuthenticationCore25LACOnenessControllerModelC25processAndEvaluateRequest019_CCCEE7302AA4D596C7N12F88F5FCDE119LL4withy10Foundation4UUIDV_tFySbcfU_TA
- _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC02isE6Active5replyyySbc_tF
- _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC02isE6Active5replyyySbc_tFTo
- _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC15sessionProvider10replyQueueAcA0dE9Providing_p_So17OS_dispatch_queueCtcfCTfq4enn_nTf4gnn_n
- _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC15sessionProvider10replyQueueAcA0dE9Providing_p_So17OS_dispatch_queueCtcfcTf4enn_n
- _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC15sessionProvider10replyQueueAcA0dE9Providing_p_So17OS_dispatch_queueCtcfcTf4enn_nAA0deI3AKSC_Tg5
- _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC23registeredReplyClosures33_E311F17ECB56FF89C3803330CB7C7A9DLLSayySbcGvpWvd
- _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC8delegateSo0deF8Delegate_pSgvM
- _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC8delegateSo0deF8Delegate_pSgvg
- _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC8delegateSo0deF8Delegate_pSgvgTo
- _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC8delegateSo0deF8Delegate_pSgvpMV
- _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC8delegateSo0deF8Delegate_pSgvpWvd
- _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC8delegateSo0deF8Delegate_pSgvs
- _$s23LocalAuthenticationCore29LACOnenessSessionMonitorModelC8delegateSo0deF8Delegate_pSgvsTo
- _$s7Combine11SubscribersO10CompletionOMn
- _$s7Combine11SubscribersO10CompletionOy_s5NeverOGIegy_AHIegn_TRTA
- _$sSbIegy_SbIeyBy_TR
- _$sSo24LACOnenessSessionMonitorC23LocalAuthenticationCoreE02isB6Active5replyyySbc_tF
- _$sSo24LACOnenessSessionMonitorC23LocalAuthenticationCoreE02isB6Active5replyyySbc_tFTo
- _$sSo24LACOnenessSessionMonitorC23LocalAuthenticationCoreE8delegateSo0abC8Delegate_pSgvg
- _$sSo24LACOnenessSessionMonitorC23LocalAuthenticationCoreE8delegateSo0abC8Delegate_pSgvgTo
- _$sSo24LACOnenessSessionMonitorC23LocalAuthenticationCoreE8delegateSo0abC8Delegate_pSgvpMV
- _$sSo24LACOnenessSessionMonitorC23LocalAuthenticationCoreE8delegateSo0abC8Delegate_pSgvs
- _$sSo24LACOnenessSessionMonitorC23LocalAuthenticationCoreE8delegateSo0abC8Delegate_pSgvsTo
- _$sSo32LACOnenessSessionMonitorDelegate_pSgMD
- _$sSo32LACOnenessSessionMonitorDelegate_pSgXwWOh
- _LACDTONotificationCategorySecurityDelayEnded
- _PROTOCOLS__TtC23LocalAuthenticationCore29LACOnenessSessionMonitorModel.2
- _PROTOCOLS__TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation.12
- __104-[LACDTOPendingPolicyEvaluationController _scheduleNotificationForPendingEvaluationRecord:after:maxAge:]_block_invoke.cold.1
- __115-[LACDTONotificationManager scheduleSecurityDelayFinishedNotificationForPendingEvaluation:after:maxAge:completion:]_block_invoke.cold.1
- __66-[LACDTOPendingPolicyEvaluationController _loadPendingEvaluations]_block_invoke.69
- __66-[LACDTOPendingPolicyEvaluationController _loadPendingEvaluations]_block_invoke.69.cold.1
- __94-[LACDTOPendingPolicyEvaluationController _addPendingEvaluationRecordForRequest:currentState:]_block_invoke.30
- __99-[LACDTOPendingPolicyEvaluationController _removePendingEvaluationRecordWithIdentifier:completion:]_block_invoke.39
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACOnenessSessionMonitorDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACOnenessSessionMonitorDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACOnenessSessionMonitorDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_LACOnenessSessionMonitorDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_LACOnenessSessionMonitorDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_LACOnenessSessionMonitorDelegate
- __OBJC_$_PROTOCOL_REFS_LACOnenessSessionMonitorDelegate
- __OBJC_$_PROTOCOL_REFS_LACOnenessSessionMonitorDelegate
- __OBJC_$_PROTOCOL_REFS_LACOnenessSessionMonitorDelegate
- __OBJC_LABEL_PROTOCOL_$_LACOnenessSessionMonitorDelegate
- __OBJC_PROTOCOL_$_LACOnenessSessionMonitorDelegate
- ___104-[LACDTOPendingPolicyEvaluationController _scheduleNotificationForPendingEvaluationRecord:after:maxAge:]_block_invoke
- ___108-[LACDTONotificationManager cancelPreviousSecurityDelayFinishedNotificationForPendingEvaluation:completion:]_block_invoke
- ___115-[LACDTONotificationManager scheduleSecurityDelayFinishedNotificationForPendingEvaluation:after:maxAge:completion:]_block_invoke
- ___51-[LACFlags valueForFlagCompanionSessionMockDevices]_block_invoke
- ___55+[LACOnenessSignpostEvent availabilityRequestDidFinish]_block_invoke_2
- ___55+[LACOnenessSignpostEvent availabilityRequestWillStart]_block_invoke_2
- ___76-[LACUNManagerQueueDecorator cancelNotificationsWithIdentifiers:completion:]_block_invoke
- ___76-[LACUNManagerQueueDecorator cancelNotificationsWithIdentifiers:completion:]_block_invoke_2
- ___76-[LACUNManagerQueueDecorator cancelNotificationsWithIdentifiers:completion:]_block_invoke_3
- ___80+[LACEnvironmentMechanismBiometry environmentMechanismForUser:auditToken:error:]_block_invoke
- ___85-[LACUNManagerPool sharedInstanceWithBundleIdentifier:categoryIdentifier:replyQueue:]_block_invoke
- ___97-[LACDTOPendingPolicyEvaluationController _cancelPreviousNotificationForPendingEvaluationRecord:]_block_invoke
- __block_literal_global.66
- _flat unique So32LACOnenessSessionMonitorDelegate_p
- _keypath_get_selector_delegate
- _objc_msgSend$_cancelPreviousNotificationForPendingEvaluationRecord:
- _objc_msgSend$_registerObserverForTimeChanges
- _objc_msgSend$_scheduleNotificationForPendingEvaluationRecord:after:maxAge:
- _objc_msgSend$_securityDelayEndedManager
- _objc_msgSend$cancelNotificationsWithIdentifiers:completion:
- _objc_msgSend$cancelPreviousSecurityDelayFinishedNotificationForPendingEvaluation:completion:
- _objc_msgSend$environmentMechanismForUser:auditToken:error:
- _objc_msgSend$environmentStateForUser:auditToken:error:
- _objc_msgSend$initWithBundleIdentifier:categoryIdentifier:
- _objc_msgSend$scheduleSecurityDelayFinishedNotificationForPendingEvaluation:after:maxAge:completion:
- _objc_msgSend$securityDelayEndedNotificationForPendingEvaluation:after:maxAge:
- _objc_msgSend$securityDelayEndedNotificationWithIdentifier:body:callbackURL:after:maxAge:
- _objc_msgSend$sharedInstanceWithBundleIdentifier:categoryIdentifier:replyQueue:
- _swift_unknownObjectWeakAssign
- _symbolic SayySbcG
- _symbolic _____IeyBy_ 10ObjectiveC8ObjCBoolV
- _symbolic ______pSg So32LACOnenessSessionMonitorDelegateP
- _symbolic ______pSgXw So32LACOnenessSessionMonitorDelegateP
- _symbolic _____y______GIegy_ 7Combine11SubscribersO10CompletionO s5NeverO
- block_copy_helper.13
- block_copy_helper.33
- block_copy_helper.43
- block_copy_helper.53
- block_copy_helper.60
- block_copy_helper.67
- block_copy_helper.83
- block_descriptor.15
- block_descriptor.35
- block_descriptor.55
- block_descriptor.62
- block_descriptor.69
- block_descriptor.85
- block_destroy_helper.14
- block_destroy_helper.34
- block_destroy_helper.44
- block_destroy_helper.54
- block_destroy_helper.61
- block_destroy_helper.68
- block_destroy_helper.84
- objectdestroy.58Tm
- objectdestroy.5Tm
CStrings:
+ " - session not active"
+ ". Informing observer "
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "Companion session is active"
+ "Context"
+ "NEW_SECURITY_DELAY_REQUIRED_BODY"
+ "NEW_SECURITY_DELAY_REQUIRED_TITLE"
+ "NOT_NOW_ACTION"
+ "START_SECURITY_DELAY_ACTION"
+ "TB,N,VisInvalidated"
+ "com.apple.coreauthd.dto.request.identifier.restart"
+ "com.apple.coreauthd.notifications.action.securityDelay.dismiss"
+ "com.apple.coreauthd.notifications.action.securityDelay.start"
+ "com.apple.coreauthd.notifications.category.securityDelay.ended"
+ "com.apple.coreauthd.notifications.category.securityDelay.required"
+ "com.apple.coreauthd.notifications.newSecurityDelayRequired"
+ "isInvalidated"
+ "kLACDTOPolicyEvaluationRequestPayloadKeyAssociatedIdentifiers"
+ "lock.fill"
+ "observers"
+ "shouldDisplayActionsInline"
- ". Informing delegate "
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "T@\"<LACOnenessSessionMonitorDelegate>\",N,W"
- "T@\"<LACOnenessSessionMonitorDelegate>\",N,W,Vdelegate"
- "com.apple.coreauthd.notifications.ratchetCoolOff"
- "macbook"
- "registeredReplyClosures"

```
