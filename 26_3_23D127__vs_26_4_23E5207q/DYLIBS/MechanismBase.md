## MechanismBase

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase`

```diff

-2005.80.10.0.0
-  __TEXT.__text: 0x180a0
-  __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_methlist: 0x1da8
-  __TEXT.__const: 0x128
-  __TEXT.__gcc_except_tab: 0x410
-  __TEXT.__cstring: 0x1070
-  __TEXT.__oslogstring: 0x1554
-  __TEXT.__unwind_info: 0x780
-  __TEXT.__objc_classname: 0x404
-  __TEXT.__objc_methname: 0x4dab
-  __TEXT.__objc_methtype: 0xed3
-  __TEXT.__objc_stubs: 0x3a00
-  __DATA_CONST.__got: 0x288
-  __DATA_CONST.__const: 0x920
-  __DATA_CONST.__objc_classlist: 0xd8
+2005.100.174.0.0
+  __TEXT.__text: 0x1b18c
+  __TEXT.__auth_stubs: 0x4f0
+  __TEXT.__objc_methlist: 0x1d80
+  __TEXT.__const: 0x120
+  __TEXT.__gcc_except_tab: 0x470
+  __TEXT.__cstring: 0xe15
+  __TEXT.__oslogstring: 0x11db
+  __TEXT.__unwind_info: 0x840
+  __TEXT.__objc_classname: 0x3da
+  __TEXT.__objc_methname: 0x47eb
+  __TEXT.__objc_methtype: 0xf2f
+  __TEXT.__objc_stubs: 0x36e0
+  __DATA_CONST.__got: 0x470
+  __DATA_CONST.__const: 0x970
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1210
+  __DATA_CONST.__objc_selrefs: 0x1130
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0xb8
-  __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x308
-  __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0xfe0
-  __AUTH_CONST.__objc_const: 0x53f0
-  __AUTH_CONST.__objc_intobj: 0x318
-  __AUTH_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_arraydata: 0x28
+  __AUTH_CONST.__auth_got: 0x288
+  __AUTH_CONST.__const: 0x260
+  __AUTH_CONST.__cfstring: 0xe60
+  __AUTH_CONST.__objc_const: 0x5558
+  __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x254
+  __DATA.__objc_ivar: 0x260
   __DATA.__data: 0x720
-  __DATA_DIRTY.__objc_data: 0x550
-  __DATA_DIRTY.__bss: 0x48
+  __DATA_DIRTY.__objc_data: 0x4b0
+  __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
-  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/DaemonUtils
   - /System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils
-  - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
-  - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
+  - /System/Library/PrivateFrameworks/LocalAuthenticationCredentialServices.framework/LocalAuthenticationCredentialServices
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
-  - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4DCF24A4-443E-3B6D-92E1-56CCE68C5761
+  UUID: 673AF78A-2634-3D39-8A31-01E5CE477992
   Functions: 629
-  Symbols:   2515
-  CStrings:  1470
+  Symbols:   2540
+  CStrings:  1371
 
Symbols:
+ -[ACMContextRecord contextExternalizer]
+ -[ACMContextRecord initWithACMContext:contextExternalizer:]
+ -[MechanismBase _runWithHints:replyToRun:error:]
+ -[MechanismBase activateWithCompletion:]
+ -[MechanismBase analytics]
+ -[MechanismBase contextExternalizer]
+ -[MechanismBase evaluationMode]
+ -[MechanismBase eventHandler]
+ -[MechanismBase externalizedContext].cold.1
+ -[MechanismBase handleEvaluationEvent:value:]
+ -[MechanismBase handleEvaluationEvent:value:reply:]
+ -[MechanismBase handleEvaluationEvent:value:timeout:reply:]
+ -[MechanismBase initWithEventIdentifier:remoteViewController:contextExternalizer:request:]
+ -[MechanismBase init]
+ -[MechanismBase log]
+ -[MechanismBase runWithHints:eventHandler:activationCompletion:reply:]
+ -[MechanismBase runWithHints:eventHandler:reply:]
+ -[MechanismBase setEvaluationMode:]
+ -[MechanismBase setEventHandler:]
+ -[MechanismBaseComposite contextExternalizer]
+ -[MechanismBiometry failureLimitWasExceeded]
+ -[MechanismBiometry failureLimit]
+ -[MechanismBiometry failuresInfoDictionaryWithError:]
+ -[MechanismBiometry failures]
+ -[MechanismBiometry handleBiometricStatusEventWithValue:completion:]
+ -[MechanismBiometry hasFallback]
+ -[MechanismBiometry hasUI]
+ -[MechanismBiometry setFailureLimit:]
+ -[MechanismBiometry setFailures:]
+ -[MechanismBiometry setHasFallback:]
+ -[MechanismBiometry setHasUI:]
+ -[MechanismCompanion _runWithHints]
+ -[MechanismCompanion _serviceLocator]
+ -[MechanismCompanion runWithHints:eventHandler:activationCompletion:reply:]
+ -[MechanismKofN _runSubmechanismAtIndex:hints:eventHandler:succeeded:failed:results:reply:]
+ -[MechanismKofN contextExternalizer]
+ -[MechanismKofN runWithHints:eventHandler:activationCompletion:reply:]
+ -[MechanismKofNReorganizer runWithHints:eventHandler:reply:]
+ -[MechanismRatchet _serviceLocator]
+ -[MechanismRatchet runWithHints:eventHandler:reply:]
+ -[MechanismUI runWithHints:eventHandler:reply:]
+ -[MechanismUI_PC .cxx_destruct]
+ -[MechanismUI_PC _deviceIsInBioLockoutWithError:]
+ -[MechanismUI_PC _fallbackButtonWouldBeVisibleInBiometryUI]
+ -[MechanismUI_PC _scheduleMechanisms]
+ -[MechanismUI_PC _shouldFinishWithError:]
+ -[MechanismUI_PC _shouldFinishWithResult:]
+ -[MechanismUI_PC _startBackgroundMechanism]
+ -[MechanismUI_PC _startBackgroundMechanism].cold.1
+ -[MechanismUI_PC _startMechanismIfNeeded]
+ -[MechanismUI_PC _terminateBackgroundMechanismWithResult:error:]
+ -[MechanismUI_PC additionalControllerInternalInfo]
+ -[MechanismUI_PC backgroundMechanism]
+ -[MechanismUI_PC backoffCounter]
+ -[MechanismUI_PC companionStateChanged:newState:]
+ -[MechanismUI_PC continueMechanisms]
+ -[MechanismUI_PC defaultFallbackText]
+ -[MechanismUI_PC eventProcessing]
+ -[MechanismUI_PC extendedInternalInfoForRemoteUI]
+ -[MechanismUI_PC externalizedContextWithError:]
+ -[MechanismUI_PC fallbackMechanism]
+ -[MechanismUI_PC fallbackToIdentifier:]
+ -[MechanismUI_PC findMechanismToRetryWithEventIdentifier:]
+ -[MechanismUI_PC findMechanismWithEventIdentifier:]
+ -[MechanismUI_PC finishRunWithResult:error:]
+ -[MechanismUI_PC finishRunWithResult:error:].cold.1
+ -[MechanismUI_PC finishRunWithResult:error:].cold.2
+ -[MechanismUI_PC finishRunWithResult:error:].cold.3
+ -[MechanismUI_PC handleEvaluationEvent:completion:]
+ -[MechanismUI_PC initWithNonUiMechanism:request:uiManager:]
+ -[MechanismUI_PC internalInfoWithReply:]
+ -[MechanismUI_PC nonUiMechanism]
+ -[MechanismUI_PC passcodeShouldBeFirstMechanism]
+ -[MechanismUI_PC passphraseShouldBeFirstMechanism]
+ -[MechanismUI_PC runWithHints:eventHandler:activationCompletion:reply:]
+ -[MechanismUI_PC runWithHints:eventsDelegate:reply:]
+ -[MechanismUI_PC setAdditionalControllerInternalInfo:]
+ -[MechanismUI_PC setBackgroundMechanism:]
+ -[MechanismUI_PC setContinueMechanisms:]
+ -[MechanismUI_PC setFallbackMechanism:]
+ -[MechanismUI_PC shouldFinishRunWithResult:error:]
+ -[MechanismUI_PC subMechanismCanRestart:]
+ -[MechanismUI_PC uiEvent:options:]
+ -[MechanismUI_PC uiMechanism]
+ -[RemoteUIActivator hasInvalidatedUIForRequestIdentifier:]
+ -[RemoteUIActivator invalidateUIForRequestIdentifier:]
+ -[RemoteUIManager connectionToRemoteUIInvalidatedForIdentifier:reply:]
+ -[RemoteUIManager didReceiveError:forRequestIdentifier:]
+ -[_RemoteUIManager _anonymousListenerWithIdentifier:].cold.1
+ -[_RemoteUIManager connectionToRemoteUIInvalidatedForIdentifier:reply:]
+ -[_RemoteUIManager didReceiveError:forRequestIdentifier:]
+ GCC_except_table12
+ GCC_except_table17
+ GCC_except_table18
+ GCC_except_table2
+ GCC_except_table24
+ GCC_except_table28
+ GCC_except_table29
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table43
+ GCC_except_table47
+ GCC_except_table5
+ GCC_except_table50
+ GCC_except_table55
+ GCC_except_table7
+ GCC_except_table77
+ _LACAngelIdentifier
+ _LACAuditTokenUsageDefault
+ _LACAuditTokenUsageLSApplicationIdentity
+ _LACAuditTokenUsageTCC
+ _LACErrorCodeBiometryDeniedForApp
+ _LACErrorCodeBiometryLockout
+ _LACErrorCodeDoublePressRequired
+ _LACErrorCodeNotFound
+ _LACErrorCodeNotSupported
+ _LACErrorCodeRequestFailed
+ _LACErrorCodeRetryAfterFailure
+ _LACErrorCodeUserCancel
+ _LACErrorCodeUserFallback
+ _LACErrorSubcodeBiometryLost
+ _LACErrorSubcodeCanceledByParentMechanismOnFailure
+ _LACErrorSubcodeCanceledByParentMechanismOnSuccess
+ _LACErrorSubcodeFaceIDHighTemperature
+ _LACErrorSubcodeFaceIDLowPower
+ _LACErrorSubcodeFaceIDLowTemperature
+ _LACErrorSubcodeUnsatisfiable
+ _LACEvaluationEventResponseKeyIsShowingUIBeforeFailure
+ _LACEvaluationRequestPayloadKeyConcurrentEvaluationConfig
+ _LACEvaluationRequestPayloadKeyInternalInfo
+ _LACEventCompanion
+ _LACEventOyster
+ _LACEventParamActive
+ _LACEventParamCredentialPresent
+ _LACEventParamError
+ _LACEventParamHostingControllerConfiguration
+ _LACEventParamMirroringToDefaultUI
+ _LACEventParamParent
+ _LACEventParamParentK
+ _LACEventParamParentN
+ _LACEventParamPasscodeVerified
+ _LACEventParamPearlSimpleStatus
+ _LACEventParamPostRequisite
+ _LACEventParamPreRequisite
+ _LACEventPasscode
+ _LACEventPassphrase
+ _LACEventPearl
+ _LACEventProcessingOptionHostingController
+ _LACEventProcessingOptionMirrorDefaultUI
+ _LACEventPushButton
+ _LACEventRatchet
+ _LACEventSimpleStatusFaceIDFaceIn
+ _LACEventSimpleStatusFaceIDFaceOut
+ _LACEventSimpleStatusFaceIDMatch
+ _LACEventSimpleStatusFaceIDNoMatch
+ _LACEventTouchID
+ _LACEventUI
+ _LACLogEnvironment
+ _LACLogEvaluationMechanism
+ _LACMechanismUserInfoKeyMaxFailuresExceeded
+ _LACMechanismUserInfoKeyUnboundMatch
+ _LACMechanismUserInfoKeyUnderlyingError
+ _LACMechanismUserInfoKeyWillTryToRecover
+ _LACPolicyOptionBeginSecurityDelayImmediately
+ _LACPolicyOptionCallerAuditToken
+ _LACPolicyOptionCallerAuditTokenUsage
+ _LACPolicyOptionEventProcessing
+ _LACPolicyOptionNoCountdownUI
+ _LACPolicyOptionNoFailureUI
+ _LACPolicyOptionNoGracePeriodUI
+ _LACPolicyOptionPINFirst
+ _LACPolicyOptionSkipDoublePress
+ _LACResultUpdateACL
+ _LACUserInterfaceBundleIdentifierUIService
+ _OBJC_CLASS_$_EvaluationRequest
+ _OBJC_CLASS_$_LACAuthenticationUINotificationCenter
+ _OBJC_CLASS_$_LACEvaluationEvent
+ _OBJC_CLASS_$_LACMutableEvaluationEventValueActivity
+ _OBJC_CLASS_$_LACMutableEvaluationEventValueBiometricStatus
+ _OBJC_CLASS_$_LACMutableEvaluationEventValuePasscodeStatus
+ _OBJC_CLASS_$_LACMutableEvaluationEventValueRatchetStatus
+ _OBJC_CLASS_$_LACRemoteUIParams
+ _OBJC_CLASS_$_MechanismUI_PC
+ _OBJC_CLASS_$_Request
+ _OBJC_IVAR_$_ACMContextRecord._contextExternalizer
+ _OBJC_IVAR_$_MechanismBase._contextExternalizer
+ _OBJC_IVAR_$_MechanismBase._evaluationMode
+ _OBJC_IVAR_$_MechanismBase._eventHandler
+ _OBJC_IVAR_$_MechanismBiometry._failureLimit
+ _OBJC_IVAR_$_MechanismBiometry._failures
+ _OBJC_IVAR_$_MechanismBiometry._hasFallback
+ _OBJC_IVAR_$_MechanismBiometry._hasUI
+ _OBJC_IVAR_$_MechanismUI_PC._additionalControllerInternalInfo
+ _OBJC_IVAR_$_MechanismUI_PC._alreadyMatchedWaitingForRemoteUi
+ _OBJC_IVAR_$_MechanismUI_PC._backgroundMechanism
+ _OBJC_IVAR_$_MechanismUI_PC._continueMechanisms
+ _OBJC_IVAR_$_MechanismUI_PC._eventProcessing
+ _OBJC_IVAR_$_MechanismUI_PC._fallbackMechanism
+ _OBJC_IVAR_$_MechanismUI_PC._fallbackReason
+ _OBJC_IVAR_$_MechanismUI_PC._internalInfo
+ _OBJC_IVAR_$_MechanismUI_PC._matchCanceledByPasscodeUi
+ _OBJC_IVAR_$_MechanismUI_PC._mechanismIndex
+ _OBJC_IVAR_$_MechanismUI_PC._nonUiMechanism
+ _OBJC_IVAR_$_MechanismUI_PC._policy
+ _OBJC_IVAR_$_MechanismUI_PC._policyOptions
+ _OBJC_IVAR_$_MechanismUI_PC._preservedPearlMechanism
+ _OBJC_IVAR_$_MechanismUI_PC._retryMechanism
+ _OBJC_IVAR_$_MechanismUI_PC._uiManager
+ _OBJC_METACLASS_$_MechanismUI_PC
+ __OBJC_$_INSTANCE_METHODS_MechanismUI_PC
+ __OBJC_$_INSTANCE_VARIABLES_MechanismUI_PC
+ __OBJC_$_PROP_LIST_LACAuthenticationUIProxy
+ __OBJC_$_PROP_LIST_LACUIMechanism
+ __OBJC_$_PROP_LIST_MechanismUI_PC
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACAuthenticationUIEventHandling
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACAuthenticationUIProxy
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACContextUIDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACEvaluationEventHandling
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACRemoteUIManaging
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACAuthenticationUIEventHandling
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACAuthenticationUIProxy
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACContextUIDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACEvaluationEventHandling
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACRemoteUIManaging
+ __OBJC_$_PROTOCOL_REFS_LACAuthenticationUIEventHandling
+ __OBJC_$_PROTOCOL_REFS_LACAuthenticationUIProxy
+ __OBJC_$_PROTOCOL_REFS_LACContextUIDelegate
+ __OBJC_$_PROTOCOL_REFS_LACEvaluationEventHandling
+ __OBJC_$_PROTOCOL_REFS_LACRemoteUIManaging
+ __OBJC_CLASS_PROTOCOLS_$_MechanismUI_PC
+ __OBJC_CLASS_RO_$_MechanismUI_PC
+ __OBJC_LABEL_PROTOCOL_$_LACAuthenticationUIEventHandling
+ __OBJC_LABEL_PROTOCOL_$_LACAuthenticationUIProxy
+ __OBJC_LABEL_PROTOCOL_$_LACContextUIDelegate
+ __OBJC_LABEL_PROTOCOL_$_LACEvaluationEventHandling
+ __OBJC_LABEL_PROTOCOL_$_LACRemoteUIManaging
+ __OBJC_METACLASS_RO_$_MechanismUI_PC
+ __OBJC_PROTOCOL_$_LACAuthenticationUIEventHandling
+ __OBJC_PROTOCOL_$_LACAuthenticationUIProxy
+ __OBJC_PROTOCOL_$_LACContextUIDelegate
+ __OBJC_PROTOCOL_$_LACEvaluationEventHandling
+ __OBJC_PROTOCOL_$_LACRemoteUIManaging
+ ___22-[MechanismUI _showUI]_block_invoke.88
+ ___34-[MechanismUI event:params:reply:]_block_invoke_4
+ ___34-[MechanismUI event:params:reply:]_block_invoke_5
+ ___38-[MechanismBase pause:forEvent:error:]_block_invoke.126
+ ___39-[MechanismUI_PC fallbackToIdentifier:]_block_invoke
+ ___40-[MechanismBase activateWithCompletion:]_block_invoke
+ ___40-[MechanismRatchet _runWithShowUIBlock:]_block_invoke.24
+ ___40-[MechanismRatchet _runWithShowUIBlock:]_block_invoke.24.cold.1
+ ___40-[MechanismRatchet _runWithShowUIBlock:]_block_invoke.26
+ ___40-[MechanismUI _startBackgroundMechanism]_block_invoke.102
+ ___42-[MechanismUI_PC _shouldFinishWithResult:]_block_invoke
+ ___43-[MechanismUI_PC _startBackgroundMechanism]_block_invoke
+ ___43-[MechanismUI_PC _startBackgroundMechanism]_block_invoke.72
+ ___43-[MechanismUI_PC _startBackgroundMechanism]_block_invoke_2
+ ___45-[MechanismBase handleEvaluationEvent:value:]_block_invoke
+ ___49-[MechanismBase runWithHints:eventHandler:reply:]_block_invoke
+ ___52-[MechanismRatchet runWithHints:eventHandler:reply:]_block_invoke
+ ___52-[MechanismRatchet runWithHints:eventHandler:reply:]_block_invoke_2
+ ___56-[RemoteUIManager didReceiveError:forRequestIdentifier:]_block_invoke
+ ___59-[MechanismBase handleEvaluationEvent:value:timeout:reply:]_block_invoke
+ ___59-[MechanismBase handleEvaluationEvent:value:timeout:reply:]_block_invoke_2
+ ___59-[MechanismBase handleEvaluationEvent:value:timeout:reply:]_block_invoke_3
+ ___68-[MechanismBiometry handleBiometricStatusEventWithValue:completion:]_block_invoke
+ ___70-[MechanismKofN runWithHints:eventHandler:activationCompletion:reply:]_block_invoke
+ ___70-[RemoteUIManager connectionToRemoteUIInvalidatedForIdentifier:reply:]_block_invoke
+ ___71-[MechanismUI_PC runWithHints:eventHandler:activationCompletion:reply:]_block_invoke
+ ___75-[MechanismCompanion runWithHints:eventHandler:activationCompletion:reply:]_block_invoke
+ ___91-[MechanismKofN _runSubmechanismAtIndex:hints:eventHandler:succeeded:failed:results:reply:]_block_invoke
+ ___block_descriptor_40_e8_32s_e24_"LACRemoteUIParams"8?0ls32l8
+ ___block_descriptor_48_e8_32bs40w_e34_v24?0"NSDictionary"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e73_v40?0"<LACUIMechanism>"8"<LACBackoffCounter>"16"NSData"24"NSError"32ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e73_v40?0"<LACUIMechanism>"8"<LACBackoffCounter>"16"NSData"24"NSError"32lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs56bs64w_e34_v24?0"NSDictionary"8"NSError"16lw64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.101
+ ___block_literal_global.106
+ ___block_literal_global.124
+ ___block_literal_global.125
+ ___block_literal_global.126
+ ___block_literal_global.128
+ ___block_literal_global.130
+ ___block_literal_global.132
+ ___block_literal_global.15
+ _objc_msgSend$_runSubmechanismAtIndex:hints:eventHandler:succeeded:failed:results:reply:
+ _objc_msgSend$_runWithHints
+ _objc_msgSend$_runWithHints:replyToRun:error:
+ _objc_msgSend$_serviceLocator
+ _objc_msgSend$_shouldFinishWithError:
+ _objc_msgSend$_shouldFinishWithResult:
+ _objc_msgSend$_startMechanismIfNeeded
+ _objc_msgSend$activateWithCompletion:
+ _objc_msgSend$connectionToRemoteUIInvalidatedForIdentifier:reply:
+ _objc_msgSend$contextExternalizer
+ _objc_msgSend$didReceiveError:forRequestIdentifier:
+ _objc_msgSend$evaluationMode
+ _objc_msgSend$eventHandler
+ _objc_msgSend$externalizedContextWithError:
+ _objc_msgSend$failureLimit
+ _objc_msgSend$failureLimitWasExceeded
+ _objc_msgSend$failures
+ _objc_msgSend$failuresInfoDictionaryWithError:
+ _objc_msgSend$featureFlagAllowTouchIDLandscapeEnabled
+ _objc_msgSend$featureFlagPresentationContextEnabled
+ _objc_msgSend$handleEvaluationEvent:completion:
+ _objc_msgSend$handleEvaluationEvent:value:
+ _objc_msgSend$handleEvaluationEvent:value:reply:
+ _objc_msgSend$handleEvaluationEvent:value:timeout:reply:
+ _objc_msgSend$hasInvalidatedUIForRequestIdentifier:
+ _objc_msgSend$idleUIListener
+ _objc_msgSend$initWithMechanism:evaluationMode:eventType:value:
+ _objc_msgSend$invalidateUIForRequestIdentifier:
+ _objc_msgSend$isEventPaused:
+ _objc_msgSend$mechanism:didProduceEvent:
+ _objc_msgSend$runWithHints:eventHandler:activationCompletion:reply:
+ _objc_msgSend$runWithHints:eventHandler:reply:
+ _objc_msgSend$setAuthenticationHints:
+ _objc_msgSend$setEvaluationError:
+ _objc_msgSend$setEvaluationMode:
+ _objc_msgSend$setIsActive:
+ _objc_msgSend$setIsSecurityDelayRunning:
+ _objc_msgSend$setMatchingStatus:
+ _objc_msgSend$setParentK:
+ _objc_msgSend$setParentN:
+ _objc_msgSend$setPostRequisite:
+ _objc_msgSend$setPreRequisite:
+ _objc_msgSend$setSecurityDelayDuration:
+ _objc_msgSend$setUiEventDelegate:
+ _objc_msgSend$setVerificationResult:
+ _objc_retainAutoreleasedReturnValue
- -[ACMContextRecord cachedExternalizationDelegate]
- -[ACMContextRecord initWithACMContext:cachedExternalizationDelegate:]
- -[MechanismBase cachedExternalizationDelegate]
- -[MechanismBase failureLimit]
- -[MechanismBase failuresInfoDictionaryWithError:]
- -[MechanismBase failures]
- -[MechanismBase initWithEventIdentifier:remoteViewController:cachedExternalizationDelegate:request:]
- -[MechanismBase requiresRemoteUIWithEventProcessing:]
- -[MechanismBase requiresRemoteViewControllerUiWithEventProcessing:]
- -[MechanismBase setFailureLimit:]
- -[MechanismBase setFailures:]
- -[MechanismBase willTryToRecover]
- -[MechanismBiometry evaluationMode]
- -[MechanismBiometry setEvaluationMode:]
- -[MechanismKofN _runSubmechanismAtIndex:hints:eventsDelegate:succeeded:failed:results:reply:]
- -[MechanismKofN cachedExternalizationDelegate]
- -[MechanismKofN requiresRemoteViewControllerUiWithEventProcessing:]
- -[MechanismUI _setupMechanismForRemoteViewController:]
- -[MechanismUI authMethodWithReply:]
- -[MechanismUI clientIsUsingCAPI]
- -[MechanismUI externalizedContextWithReply:]
- -[MechanismUINotificationCenter .cxx_destruct]
- -[MechanismUINotificationCenter _checkIsRedundantNotification:]
- -[MechanismUINotificationCenter _identifierForNotification:]
- -[MechanismUINotificationCenter _postDarwinNotificationWithIdentifier:]
- -[MechanismUINotificationCenter lastNotification]
- -[MechanismUINotificationCenter postNotification:]
- -[MechanismUINotificationCenter setLastNotification:]
- -[MechanismUINotificationCenter(RemoteUINotificationCenter) postNotificationUIDidAppear]
- -[MechanismUINotificationCenter(RemoteUINotificationCenter) postNotificationUIDidDisappear]
- -[RemoteUIActivator hasInvalidatedUIForRequest:]
- -[RemoteUIActivator invalidateUIForRequest:]
- -[RemoteUIActivator_Legacy .cxx_destruct]
- -[RemoteUIActivator_Legacy _activateFrontBoardUIWithParams:]
- -[RemoteUIActivator_Legacy _activateFrontBoardUIWithParams:].cold.1
- -[RemoteUIActivator_Legacy _activateRemoteAlertHandle:activationContext:params:]
- -[RemoteUIActivator_Legacy _activateSpringBoardUIWithParams:]
- -[RemoteUIActivator_Legacy _dispatchRemoteAlertHandle:activationContext:params:]
- -[RemoteUIActivator_Legacy _isActivationSuspended]
- -[RemoteUIActivator_Legacy _postNotificationsAndActivateRemoteAlertHandle:activationContext:params:]
- -[RemoteUIActivator_Legacy _postNotificationsAndActivateRemoteAlertHandle:activationContext:params:].cold.1
- -[RemoteUIActivator_Legacy _resumeActivationQueue]
- -[RemoteUIActivator_Legacy _resumeActivationQueue].cold.1
- -[RemoteUIActivator_Legacy _resumeActivationQueue].cold.2
- -[RemoteUIActivator_Legacy _sbHandleWithDefinition:configurationContext:]
- -[RemoteUIActivator_Legacy _sbHandleWithDefinition:configurationContext:].cold.1
- -[RemoteUIActivator_Legacy _suspendActivationQueue]
- -[RemoteUIActivator_Legacy _suspendActivationQueue].cold.1
- -[RemoteUIActivator_Legacy _suspendActivationQueue].cold.2
- -[RemoteUIActivator_Legacy activateUIWithParams:]
- -[RemoteUIActivator_Legacy activatingHandle]
- -[RemoteUIActivator_Legacy activationQueue]
- -[RemoteUIActivator_Legacy activeHandle]
- -[RemoteUIActivator_Legacy delegate]
- -[RemoteUIActivator_Legacy hasInvalidatedUIForRequest:]
- -[RemoteUIActivator_Legacy init]
- -[RemoteUIActivator_Legacy invalidateUIForRequest:]
- -[RemoteUIActivator_Legacy invalidateUIForRequest:].cold.1
- -[RemoteUIActivator_Legacy onActivationTimeout]
- -[RemoteUIActivator_Legacy remoteAlertHandle:didInvalidateWithError:]
- -[RemoteUIActivator_Legacy remoteAlertHandle:didInvalidateWithError:].cold.1
- -[RemoteUIActivator_Legacy remoteAlertHandleDidActivate:]
- -[RemoteUIActivator_Legacy remoteAlertHandleDidActivate:].cold.1
- -[RemoteUIActivator_Legacy remoteAlertHandleDidDeactivate:]
- -[RemoteUIActivator_Legacy remoteAlertHandleDidDeactivate:].cold.1
- -[RemoteUIActivator_Legacy remoteAlertWasInvalidated]
- -[RemoteUIActivator_Legacy setActivatingHandle:]
- -[RemoteUIActivator_Legacy setActivationQueue:]
- -[RemoteUIActivator_Legacy setActiveHandle:]
- -[RemoteUIActivator_Legacy setDelegate:]
- -[RemoteUIActivator_Legacy setOnActivationTimeout:]
- -[RemoteUIActivator_Legacy setRemoteAlertWasInvalidated:]
- -[RemoteUIManager connectionToViewServiceInvalidatedForIdentifier:reply:]
- -[RemoteUIManager didReceiveExpectedError:]
- -[RemoteUIManager didReceiveUnexpectedError:]
- -[RemoteUIParams .cxx_destruct]
- -[RemoteUIParams auditTokenData]
- -[RemoteUIParams description]
- -[RemoteUIParams evaluationRequest]
- -[RemoteUIParams forSiri]
- -[RemoteUIParams forSoftwareUpdate]
- -[RemoteUIParams hostedRemoteController]
- -[RemoteUIParams identifier]
- -[RemoteUIParams initWithMechanism:]
- -[RemoteUIParams initWithMechanism:hostedRemoteController:]
- -[RemoteUIParams lsApplicationIdentity]
- -[RemoteUIParams notificationCenter]
- -[RemoteUIParams pid]
- -[RemoteUIParams remoteUI]
- -[RemoteUIParams requestID]
- -[RemoteUIParams setNotificationCenter:]
- -[RemoteUIParams setRemoteUI:]
- -[RemoteUIParams uiMechanism]
- -[RemoteUIParams userId]
- -[_RemoteUIManager connectionToViewServiceInvalidatedForIdentifier:reply:]
- -[_RemoteUIManager didReceiveExpectedError:]
- -[_RemoteUIManager didReceiveUnexpectedError:]
- GCC_except_table14
- GCC_except_table15
- GCC_except_table21
- GCC_except_table23
- GCC_except_table25
- GCC_except_table33
- GCC_except_table34
- GCC_except_table39
- GCC_except_table41
- GCC_except_table45
- GCC_except_table52
- GCC_except_table56
- GCC_except_table68
- _CFNotificationCenterGetDarwinNotifyCenter
- _CFNotificationCenterPostNotification
- _LACErrorDomain
- _LACEvaluationRequestPayloadKeyConcurrentIdleUIListener
- _LACUserInterfaceBundleIdentifierDefault
- _LA_LOG_MechanismUINotificationCenter
- _LA_LOG_MechanismUINotificationCenter.cold.1
- _LA_LOG_MechanismUINotificationCenter.log
- _LA_LOG_MechanismUINotificationCenter.once
- _OBJC_CLASS_$_FBSOpenApplicationOptions
- _OBJC_CLASS_$_FBSOpenApplicationService
- _OBJC_CLASS_$_LACUserInterfaceFrontBoardAdapter
- _OBJC_CLASS_$_LACUserInterfaceSpringBoardAdapter
- _OBJC_CLASS_$_LAUtils
- _OBJC_CLASS_$_MechanismUINotificationCenter
- _OBJC_CLASS_$_NSConstantIntegerNumber
- _OBJC_CLASS_$_RemoteUIActivator_Legacy
- _OBJC_CLASS_$_RemoteUIParams
- _OBJC_CLASS_$_SBSRemoteAlertConfigurationContext
- _OBJC_CLASS_$_SBSRemoteAlertDefinition
- _OBJC_CLASS_$_SBSRemoteAlertHandle
- _OBJC_IVAR_$_ACMContextRecord._cachedExternalizationDelegate
- _OBJC_IVAR_$_MechanismBase._cachedExternalizationDelegate
- _OBJC_IVAR_$_MechanismBase._failureLimit
- _OBJC_IVAR_$_MechanismBase._failures
- _OBJC_IVAR_$_MechanismBiometry._evaluationMode
- _OBJC_IVAR_$_MechanismUINotificationCenter._lastNotification
- _OBJC_IVAR_$_RemoteUIActivator_Legacy._activatingHandle
- _OBJC_IVAR_$_RemoteUIActivator_Legacy._activationQueue
- _OBJC_IVAR_$_RemoteUIActivator_Legacy._activationSuspended
- _OBJC_IVAR_$_RemoteUIActivator_Legacy._activeHandle
- _OBJC_IVAR_$_RemoteUIActivator_Legacy._activeInterfaces
- _OBJC_IVAR_$_RemoteUIActivator_Legacy._delegate
- _OBJC_IVAR_$_RemoteUIActivator_Legacy._onActivationTimeout
- _OBJC_IVAR_$_RemoteUIActivator_Legacy._remoteAlertWasInvalidated
- _OBJC_IVAR_$_RemoteUIParams._evaluationRequest
- _OBJC_IVAR_$_RemoteUIParams._hostedRemoteController
- _OBJC_IVAR_$_RemoteUIParams._identifier
- _OBJC_IVAR_$_RemoteUIParams._notificationCenter
- _OBJC_IVAR_$_RemoteUIParams._remoteUI
- _OBJC_IVAR_$_RemoteUIParams._uiMechanism
- _OBJC_IVAR_$_RemoteUIParams._uiRequest
- _OBJC_METACLASS_$_MechanismUINotificationCenter
- _OBJC_METACLASS_$_RemoteUIActivator_Legacy
- _OBJC_METACLASS_$_RemoteUIParams
- _SBSRemoteAlertHandleInvalidationErrorDomain
- _SBSUndimScreen
- __OBJC_$_INSTANCE_METHODS_MechanismUINotificationCenter(RemoteUINotificationCenter)
- __OBJC_$_INSTANCE_METHODS_RemoteUIActivator_Legacy
- __OBJC_$_INSTANCE_METHODS_RemoteUIParams
- __OBJC_$_INSTANCE_VARIABLES_MechanismUINotificationCenter
- __OBJC_$_INSTANCE_VARIABLES_RemoteUIActivator_Legacy
- __OBJC_$_INSTANCE_VARIABLES_RemoteUIParams
- __OBJC_$_PROP_LIST_RemoteUIActivator_Legacy
- __OBJC_$_PROP_LIST_RemoteUIParams
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACContextExternalizing
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LAUIDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LACContextExternalizing
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SBSRemoteAlertHandleObserver
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_RemoteUIManaging
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_RemoteUINotificationCenter
- __OBJC_$_PROTOCOL_METHOD_TYPES_LACContextExternalizing
- __OBJC_$_PROTOCOL_METHOD_TYPES_LAUIDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_RemoteUIManaging
- __OBJC_$_PROTOCOL_METHOD_TYPES_RemoteUINotificationCenter
- __OBJC_$_PROTOCOL_METHOD_TYPES_SBSRemoteAlertHandleObserver
- __OBJC_$_PROTOCOL_REFS_LACContextExternalizing
- __OBJC_$_PROTOCOL_REFS_RemoteUIManaging
- __OBJC_$_PROTOCOL_REFS_RemoteUINotificationCenter
- __OBJC_$_PROTOCOL_REFS_SBSRemoteAlertHandleObserver
- __OBJC_CLASS_PROTOCOLS_$_MechanismUINotificationCenter(RemoteUINotificationCenter)
- __OBJC_CLASS_PROTOCOLS_$_RemoteUIActivator_Legacy
- __OBJC_CLASS_RO_$_MechanismUINotificationCenter
- __OBJC_CLASS_RO_$_RemoteUIActivator_Legacy
- __OBJC_CLASS_RO_$_RemoteUIParams
- __OBJC_LABEL_PROTOCOL_$_LACContextExternalizing
- __OBJC_LABEL_PROTOCOL_$_LAUIDelegate
- __OBJC_LABEL_PROTOCOL_$_RemoteUIManaging
- __OBJC_LABEL_PROTOCOL_$_RemoteUINotificationCenter
- __OBJC_LABEL_PROTOCOL_$_SBSRemoteAlertHandleObserver
- __OBJC_METACLASS_RO_$_MechanismUINotificationCenter
- __OBJC_METACLASS_RO_$_RemoteUIActivator_Legacy
- __OBJC_METACLASS_RO_$_RemoteUIParams
- __OBJC_PROTOCOL_$_LACContextExternalizing
- __OBJC_PROTOCOL_$_LAUIDelegate
- __OBJC_PROTOCOL_$_RemoteUIManaging
- __OBJC_PROTOCOL_$_RemoteUINotificationCenter
- __OBJC_PROTOCOL_$_SBSRemoteAlertHandleObserver
- ___22-[MechanismUI _showUI]_block_invoke.107
- ___34-[MechanismUI event:params:reply:]_block_invoke.169
- ___34-[MechanismUI event:params:reply:]_block_invoke_2.172
- ___36-[MechanismBase externalizedContext]_block_invoke
- ___36-[MechanismBase externalizedContext]_block_invoke.cold.1
- ___38-[MechanismBase pause:forEvent:error:]_block_invoke.138
- ___40-[MechanismRatchet _runWithShowUIBlock:]_block_invoke.16
- ___40-[MechanismRatchet _runWithShowUIBlock:]_block_invoke.16.cold.1
- ___40-[MechanismRatchet _runWithShowUIBlock:]_block_invoke.18
- ___40-[MechanismUI _startBackgroundMechanism]_block_invoke.121
- ___43-[RemoteUIManager didReceiveExpectedError:]_block_invoke
- ___45-[RemoteUIManager didReceiveUnexpectedError:]_block_invoke
- ___51-[RemoteUIActivator_Legacy _suspendActivationQueue]_block_invoke
- ___51-[RemoteUIActivator_Legacy _suspendActivationQueue]_block_invoke.cold.1
- ___60-[RemoteUIActivator_Legacy _activateFrontBoardUIWithParams:]_block_invoke
- ___73-[RemoteUIManager connectionToViewServiceInvalidatedForIdentifier:reply:]_block_invoke
- ___80-[RemoteUIActivator_Legacy _dispatchRemoteAlertHandle:activationContext:params:]_block_invoke
- ___93-[MechanismKofN _runSubmechanismAtIndex:hints:eventsDelegate:succeeded:failed:results:reply:]_block_invoke
- ___LA_LOG_MechanismUINotificationCenter_block_invoke
- ___block_descriptor_40_e8_32s_e21_"RemoteUIParams"8?0ls32l8
- ___block_descriptor_48_e8_32s40bs_e62_v32?0"<LACUIMechanism>"8"<LACBackoffCounter>"16"NSError"24ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e37_v24?0"BSProcessHandle"8"NSError"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs48w_e62_v32?0"<LACUIMechanism>"8"<LACBackoffCounter>"16"NSError"24lw48l8s40l8s32l8
- ___block_descriptor_56_e8_32s40s48r_e28_v24?0"NSData"8"NSError"16lr48l8s32l8s40l8
- ___block_literal_global.102
- ___block_literal_global.148
- ___block_literal_global.162
- ___block_literal_global.164
- ___block_literal_global.166
- ___block_literal_global.171
- ___block_literal_global.174
- ___block_literal_global.69
- ___block_literal_global.98
- __os_feature_enabled_impl
- _dispatch_block_cancel
- _dispatch_block_create
- _dispatch_resume
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _dispatch_suspend
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_activateFrontBoardUIWithParams:
- _objc_msgSend$_activateRemoteAlertHandle:activationContext:params:
- _objc_msgSend$_activateSpringBoardUIWithParams:
- _objc_msgSend$_checkIsRedundantNotification:
- _objc_msgSend$_dispatchRemoteAlertHandle:activationContext:params:
- _objc_msgSend$_identifierForNotification:
- _objc_msgSend$_isActivationSuspended
- _objc_msgSend$_nameForRemoteUIController:
- _objc_msgSend$_postDarwinNotificationWithIdentifier:
- _objc_msgSend$_postNotificationsAndActivateRemoteAlertHandle:activationContext:params:
- _objc_msgSend$_resumeActivationQueue
- _objc_msgSend$_runSubmechanismAtIndex:hints:eventsDelegate:succeeded:failed:results:reply:
- _objc_msgSend$_sbHandleWithDefinition:configurationContext:
- _objc_msgSend$_setupMechanismForRemoteViewController:
- _objc_msgSend$_suspendActivationQueue
- _objc_msgSend$activateWithContext:
- _objc_msgSend$activatingHandle
- _objc_msgSend$activationContextWithAuditToken:isAuditTokenApplicationIdentity:isForSiri:
- _objc_msgSend$activationQueue
- _objc_msgSend$activeHandle
- _objc_msgSend$applicationOptionsForPayloadURL:softwareUpdate:
- _objc_msgSend$applicationPayloadURLForBundleID:rootControllerName:parameters:
- _objc_msgSend$auditTokenData
- _objc_msgSend$cachedExternalizationDelegate
- _objc_msgSend$clientAuditTokenData
- _objc_msgSend$clientIsUsingCAPI
- _objc_msgSend$clientProcessId
- _objc_msgSend$connectionToViewServiceInvalidatedForIdentifier:reply:
- _objc_msgSend$createUserInitiatedSerialQueueWithIdentifier:
- _objc_msgSend$didReceiveExpectedError:
- _objc_msgSend$didReceiveUnexpectedError:
- _objc_msgSend$domain
- _objc_msgSend$errorPlatformDoesNotSupportAction:
- _objc_msgSend$errorWithCode:message:suberror:
- _objc_msgSend$errorWithCode:subcode:message:
- _objc_msgSend$externalizedContextWithReply:
- _objc_msgSend$featureFlagLaunchAngelEnabled
- _objc_msgSend$forSiri
- _objc_msgSend$forSoftwareUpdate
- _objc_msgSend$hasInvalidatedUIForRequest:
- _objc_msgSend$hostedRemoteController
- _objc_msgSend$initWithServiceName:viewControllerClassName:
- _objc_msgSend$instanceId
- _objc_msgSend$invalidateUIForRequest:
- _objc_msgSend$isAuditTokenApplicationIdentity
- _objc_msgSend$isForSiri
- _objc_msgSend$isForSoftwareUpdate
- _objc_msgSend$lastNotification
- _objc_msgSend$lsApplicationIdentity
- _objc_msgSend$newHandleWithDefinition:configurationContext:
- _objc_msgSend$onActivationTimeout
- _objc_msgSend$openApplication:withOptions:completion:
- _objc_msgSend$optionsWithDictionary:
- _objc_msgSend$pid
- _objc_msgSend$postNotification:
- _objc_msgSend$registerObserver:
- _objc_msgSend$remoteAlertViewControllerName
- _objc_msgSend$remoteAlertWasInvalidated
- _objc_msgSend$requestID
- _objc_msgSend$requiresRemoteUIWithEventProcessing:
- _objc_msgSend$requiresRemoteViewControllerUiWithEventProcessing:
- _objc_msgSend$secondaryViewControllerClassName
- _objc_msgSend$serviceWithDefaultShellEndpoint
- _objc_msgSend$setActivatingHandle:
- _objc_msgSend$setActiveHandle:
- _objc_msgSend$setLastNotification:
- _objc_msgSend$setRemoteAlertWasInvalidated:
- _objc_msgSend$setSecondaryViewControllerClassName:
- _objc_msgSend$userId
- _objc_msgSend$usesFrontBoardServicesForRemoteUI
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x25
- _objc_retain_x27
- _objc_retain_x4
- _objc_retain_x9
- _objc_sync_enter
- _objc_sync_exit
CStrings:
+ "@\"<LACAuthenticationUIManaging>\""
+ "@\"<LACBackoffCounter>\"16@0:8"
+ "@\"<LACContextUIDelegate>\""
+ "@\"<LACEvaluationEventHandling>\""
+ "@\"<LACEvaluationRequest>\"16@0:8"
+ "@\"<LACRemoteUIEndpointProvider>\""
+ "@\"<LACRemoteUIManaging><RemoteUIActivatorDelegate>\""
+ "@\"LACAuthenticationUINotificationCenter\""
+ "@\"LACRemoteUIParams\""
+ "@\"LACRemoteUIParams\"8@?0"
+ "B24@0:8@\"LACRemoteUIParams\"16"
+ "B24@0:8@\"NSString\"16"
+ "B32@0:8@\"NSDictionary\"16@\"NSError\"24"
+ "B40@0:8@16@?24^@32"
+ "Default UI for %@ is not supported"
+ "Default UI for event %d is not supported"
+ "Ignoring error: %@ for request: %@ - current request mismatch: %@"
+ "LACAuthenticationUIEventHandling"
+ "LACAuthenticationUIProxy"
+ "LACContextUIDelegate"
+ "LACEvaluationEventHandling"
+ "LACRemoteUIManaging"
+ "MechanismUI_PC"
+ "Q\x81T"
+ "Skipping activation in %@"
+ "T@\"<LACBackoffCounter>\",R,N"
+ "T@\"<LACContextExternalizing>\",R,W,N,V_contextExternalizer"
+ "T@\"<LACContextUIDelegate>\",W,N,V_eventsDelegate"
+ "T@\"<LACEvaluationAnalytics>\",R,N"
+ "T@\"<LACEvaluationEventHandling>\",W,N,V_eventHandler"
+ "T@\"<LACEvaluationRequest>\",R,N"
+ "T@\"<LACEvaluationRequest>\",R,N,V_request"
+ "T@\"LACAuthenticationUINotificationCenter\",R,N,V_notificationCenter"
+ "T@\"NSObject<OS_os_log>\",R,N"
+ "TB,N,V_hasFallback"
+ "TB,N,V_hasUI"
+ "Unable to create XPC listener for hosted UI"
+ "Unable to create XPC listener. Endpoint provider is nil."
+ "_contextExternalizer"
+ "_eventHandler"
+ "_hasFallback"
+ "_hasUI"
+ "_runSubmechanismAtIndex:hints:eventHandler:succeeded:failed:results:reply:"
+ "_runWithHints"
+ "_runWithHints:replyToRun:error:"
+ "_serviceLocator"
+ "_shouldFinishWithError:"
+ "_shouldFinishWithResult:"
+ "_startMechanismIfNeeded"
+ "_uiManager"
+ "activateWithCompletion:"
+ "connectionToRemoteUIInvalidatedForIdentifier: %@"
+ "connectionToRemoteUIInvalidatedForIdentifier:reply:"
+ "contextExternalizer"
+ "didReceiveError:forRequestIdentifier:"
+ "eventHandler"
+ "extendedInternalInfoForRemoteUI"
+ "externalizedContextWithError:"
+ "failureLimitWasExceeded"
+ "fallback due to power/thermal"
+ "featureFlagAllowTouchIDLandscapeEnabled"
+ "featureFlagPresentationContextEnabled"
+ "handleBiometricStatusEventWithValue:completion:"
+ "handleEvaluationEvent:completion:"
+ "handleEvaluationEvent:value:"
+ "handleEvaluationEvent:value:reply:"
+ "handleEvaluationEvent:value:timeout:reply:"
+ "hasFallback"
+ "hasInvalidatedUIForRequestIdentifier:"
+ "idleUIListener"
+ "initWithACMContext:contextExternalizer:"
+ "initWithEventIdentifier:remoteViewController:contextExternalizer:request:"
+ "initWithMechanism:evaluationMode:eventType:value:"
+ "initWithNonUiMechanism:request:uiManager:"
+ "invalidateUIForRequestIdentifier:"
+ "isEventPaused:"
+ "mechanism:didProduceEvent:"
+ "runWithHints:eventHandler:activationCompletion:reply:"
+ "runWithHints:eventHandler:reply:"
+ "setAuthenticationHints:"
+ "setEvaluationError:"
+ "setEventHandler:"
+ "setIsActive:"
+ "setIsSecurityDelayRunning:"
+ "setMatchingStatus:"
+ "setParentK:"
+ "setParentN:"
+ "setPostRequisite:"
+ "setPreRequisite:"
+ "setSecurityDelayDuration:"
+ "setUiEventDelegate:"
+ "setVerificationResult:"
+ "shouldFinishRunWithResult:error:"
+ "v24@0:8@\"<LACRemoteUIEndpointProvider>\"16"
+ "v32@0:8@\"LACEvaluationEvent\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8@\"LACRemoteUIParams\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@\"NSError\"24"
+ "v32@0:8@\"NSError\"16@\"NSString\"24"
+ "v40@0:8@\"<LACRemoteUI>\"16@\"NSNumber\"24@?<v@?@\"<LACUIMechanism>\"@\"<LACBackoffCounter>\"@\"NSData\"@\"NSError\">32"
+ "v40@0:8q16@\"<LACUIMechanism><LACRemoteUIHost>\"24@?<v@?@\"NSXPCListener\">32"
+ "v40@0:8q16@\"<LACUIMechanism><LACRemoteUIHost>\"24@?<v@?B@\"NSError\">32"
+ "v40@?0@\"<LACUIMechanism>\"8@\"<LACBackoffCounter>\"16@\"NSData\"24@\"NSError\"32"
+ "v48@0:8@\"<LACRemoteUI>\"16@\"<LACUIMechanism><LACRemoteUIHost>\"24B32B36@?<v@?>40"
+ "v48@0:8@16@24@?32@?40"
+ "v48@0:8q16@24d32@?40"
- "#"
- "%u"
- "%u-%u-%li"
- "%{public}@ didActivate"
- "%{public}@ didDeactivate"
- "%{public}@ didInvalidateWithError: %{public}@"
- "-[RemoteUIActivator_Legacy _activateFrontBoardUIWithParams:]"
- "-[RemoteUIActivator_Legacy _postNotificationsAndActivateRemoteAlertHandle:activationContext:params:]"
- "<RemoteUIParams ID:%@, SU: %d, Siri: %d, uid: %@, pid: %u, lsai: %d>"
- "@\"<LAUIDelegate>\""
- "@\"<RemoteUIEndpointProvider>\""
- "@\"<RemoteUIManaging><RemoteUIActivatorDelegate>\""
- "@\"<RemoteUINotificationCenter>\""
- "@\"EvaluationRequest\""
- "@\"LACUserInterfaceRequest\""
- "@\"MechanismUI<LACUIMechanism><LACRemoteUIHost>\""
- "@\"MechanismUINotificationCenter\""
- "@\"RemoteUIParams\""
- "@\"RemoteUIParams\"8@?0"
- "@\"SBSRemoteAlertHandle\""
- "@32@0:8@16q24"
- "Aborting UI activation because %{public}@ is not running"
- "Activating %{public}@ with %{public}@ for %{public}@"
- "Activating remote UI for %{public}@ via FB with options %{public}@"
- "Activation queue is already resumed"
- "Activation queue is already suspended"
- "Activation queue resumed"
- "Activation queue suspended"
- "Activation queue timeout"
- "Application launch failed with error: %@"
- "Application launch succeeded"
- "B20@0:8I16"
- "B24@0:8@\"RemoteUIParams\"16"
- "CApiOrigin"
- "Default UI for %@"
- "Did post notification with identifier: %{public}@"
- "Did skip notification with identifier: %{public}@"
- "Dispatching %{public}@"
- "Failed to create remote alert handle with %{public}@ and %{public}@"
- "Ignoring deactivation of %{public}@ because %{public}@ is active"
- "Ignoring invalidation of %{public}@ because %{public}@ is active and %{public}@ is activating"
- "Invalidation not implemented in the legacy activator"
- "LACContextExternalizing"
- "LAUIDelegate"
- "LocalAuthentication"
- "MechanismUINotificationCenter"
- "No auth blob on mechanism."
- "Q\x81A\""
- "Remote alert deactivated"
- "Remote alert invalidated"
- "RemoteUIActivator_Legacy"
- "RemoteUIActivator_Legacy.m"
- "RemoteUIManaging"
- "RemoteUINotificationCenter"
- "RemoteUIParams"
- "RemoteViewController requested by: %{public}@"
- "SBSRemoteAlertHandleObserver"
- "Specifying secondary view controller class name %{public}@"
- "T@\"<LACContextExternalizing>\",R,W,N,V_cachedExternalizationDelegate"
- "T@\"<LACEvaluationRequest>\",R,N,V_evaluationRequest"
- "T@\"<LACRemoteUI>\",&,N,V_remoteUI"
- "T@\"<LAUIDelegate>\",W,N,V_eventsDelegate"
- "T@\"<RemoteUINotificationCenter>\",&,N,V_notificationCenter"
- "T@\"EvaluationRequest\",R,N,V_request"
- "T@\"MechanismUI<LACUIMechanism><LACRemoteUIHost>\",R,N,V_uiMechanism"
- "T@\"MechanismUINotificationCenter\",R,N,V_notificationCenter"
- "T@\"NSData\",R,N"
- "T@\"NSNumber\",&,N,V_lastNotification"
- "T@\"NSNumber\",R,N"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_activationQueue"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"SBSRemoteAlertHandle\",W,N,V_activatingHandle"
- "T@\"SBSRemoteAlertHandle\",W,N,V_activeHandle"
- "T@?,C,N,V_onActivationTimeout"
- "TB,N,V_remoteAlertWasInvalidated"
- "Ti,R,N"
- "Tq,R,N,V_hostedRemoteController"
- "Unexpected alert activated: %{public}@ Was expecting: %{public}@"
- "[params notificationCenter]"
- "_activateFrontBoardUIWithParams:"
- "_activateRemoteAlertHandle:activationContext:params:"
- "_activateSpringBoardUIWithParams:"
- "_activatingHandle"
- "_activationQueue"
- "_activationSuspended"
- "_activeHandle"
- "_cachedExternalizationDelegate"
- "_checkIsRedundantNotification:"
- "_dispatchRemoteAlertHandle:activationContext:params:"
- "_evaluationRequest"
- "_hostedRemoteController"
- "_identifier"
- "_identifierForNotification:"
- "_isActivationSuspended"
- "_lastNotification"
- "_onActivationTimeout"
- "_postDarwinNotificationWithIdentifier:"
- "_postNotificationsAndActivateRemoteAlertHandle:activationContext:params:"
- "_remoteAlertWasInvalidated"
- "_resumeActivationQueue"
- "_runSubmechanismAtIndex:hints:eventsDelegate:succeeded:failed:results:reply:"
- "_sbHandleWithDefinition:configurationContext:"
- "_setupMechanismForRemoteViewController:"
- "_suspendActivationQueue"
- "_uiMechanism"
- "_uiRequest"
- "activateWithContext:"
- "activatingHandle"
- "activation"
- "activationContextWithAuditToken:isAuditTokenApplicationIdentity:isForSiri:"
- "activationQueue"
- "activeHandle"
- "allowLandscapeTouchID"
- "applicationOptionsForPayloadURL:softwareUpdate:"
- "applicationPayloadURLForBundleID:rootControllerName:parameters:"
- "auditTokenData"
- "authMethodWithReply:"
- "cachedExternalizationDelegate"
- "clientAuditTokenData"
- "clientIsUsingCAPI"
- "clientProcessId"
- "com.apple.CoreAuthUI"
- "com.apple.LocalAuthentication.ui.dismissed"
- "com.apple.LocalAuthentication.ui.presented"
- "com.apple.LocalAuthenticationUIService"
- "connectionToViewServiceInvalidatedForIdentifier: %@"
- "connectionToViewServiceInvalidatedForIdentifier:reply:"
- "createUserInitiatedSerialQueueWithIdentifier:"
- "default UI for event %d"
- "didReceiveExpectedError:"
- "didReceiveUnexpectedError:"
- "domain"
- "errorPlatformDoesNotSupportAction:"
- "errorWithCode:message:suberror:"
- "errorWithCode:subcode:message:"
- "externalizedContextWithReply:"
- "featureFlagLaunchAngelEnabled"
- "forSiri"
- "forSoftwareUpdate"
- "forciblyInvalidate"
- "hasInvalidatedUIForRequest:"
- "hostedRemoteController"
- "i16@0:8"
- "initWithACMContext:cachedExternalizationDelegate:"
- "initWithEventIdentifier:remoteViewController:cachedExternalizationDelegate:request:"
- "initWithServiceName:viewControllerClassName:"
- "invalidateUIForRequest:"
- "isAuditTokenApplicationIdentity"
- "isForSiri"
- "isForSoftwareUpdate"
- "lastNotification"
- "lsApplicationIdentity"
- "newHandleWithDefinition:configurationContext:"
- "onActivationTimeout"
- "openApplication:withOptions:completion:"
- "optionsWithDictionary:"
- "pid"
- "postNotification:"
- "registerObserver:"
- "remoteAlertHandle:didInvalidateWithError:"
- "remoteAlertHandleDidActivate:"
- "remoteAlertHandleDidDeactivate:"
- "remoteAlertWasInvalidated"
- "requestID"
- "requiresRemoteUIWithEventProcessing:"
- "requiresRemoteViewControllerUiWithEventProcessing:"
- "secondaryViewControllerClassName"
- "serviceWithDefaultShellEndpoint"
- "setActivatingHandle:"
- "setActivationQueue:"
- "setActiveHandle:"
- "setLastNotification:"
- "setOnActivationTimeout:"
- "setRemoteAlertWasInvalidated:"
- "setSecondaryViewControllerClassName:"
- "synchronousExternalizedContextWithError:"
- "usesFrontBoardServicesForRemoteUI"
- "v24@0:8@\"<RemoteUIEndpointProvider>\"16"
- "v24@0:8@\"SBSRemoteAlertHandle\"16"
- "v24@0:8@?<v@?@\"NSData\"@\"NSError\">16"
- "v24@?0@\"BSProcessHandle\"8@\"NSError\"16"
- "v24@?0@\"NSData\"8@\"NSError\"16"
- "v32@0:8@\"RemoteUIParams\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"SBSRemoteAlertHandle\"16@\"NSError\"24"
- "v32@?0@\"<LACUIMechanism>\"8@\"<LACBackoffCounter>\"16@\"NSError\"24"
- "v40@0:8@\"<LACRemoteUI>\"16@\"NSNumber\"24@?<v@?@\"<LACUIMechanism>\"@\"<LACBackoffCounter>\"@\"NSError\">32"
- "v40@0:8q16@\"MechanismUI<LACUIMechanism><LACRemoteUIHost>\"24@?<v@?@\"NSXPCListener\">32"
- "v40@0:8q16@\"MechanismUI<LACUIMechanism><LACRemoteUIHost>\"24@?<v@?B@\"NSError\">32"
- "v48@0:8@\"<LACRemoteUI>\"16@\"MechanismUI<LACUIMechanism><LACRemoteUIHost>\"24B32B36@?<v@?>40"

```
