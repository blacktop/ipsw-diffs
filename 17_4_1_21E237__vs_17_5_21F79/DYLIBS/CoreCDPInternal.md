## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-359.13.0.0.0
-  __TEXT.__text: 0x66d58
-  __TEXT.__auth_stubs: 0xab0
-  __TEXT.__objc_methlist: 0x3ab0
+359.21.0.0.0
+  __TEXT.__text: 0x68130
+  __TEXT.__auth_stubs: 0xac0
+  __TEXT.__objc_methlist: 0x3b30
   __TEXT.__const: 0x90
-  __TEXT.__oslogstring: 0xfb6d
-  __TEXT.__cstring: 0x49b2
+  __TEXT.__oslogstring: 0xfcd2
+  __TEXT.__cstring: 0x4be6
   __TEXT.__gcc_except_tab: 0x78c
-  __TEXT.__unwind_info: 0x1494
-  __TEXT.__objc_classname: 0xb63
-  __TEXT.__objc_methname: 0xc3be
-  __TEXT.__objc_methtype: 0x228a
-  __TEXT.__objc_stubs: 0xa1c0
-  __DATA_CONST.__got: 0x868
-  __DATA_CONST.__const: 0x1aa0
-  __DATA_CONST.__objc_classlist: 0x240
+  __TEXT.__unwind_info: 0x1484
+  __TEXT.__objc_classname: 0xb75
+  __TEXT.__objc_methname: 0xc670
+  __TEXT.__objc_methtype: 0x22b3
+  __TEXT.__objc_stubs: 0xa440
+  __DATA_CONST.__got: 0x8d0
+  __DATA_CONST.__const: 0x1af0
+  __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xd830
-  __DATA_CONST.__objc_selrefs: 0x2c88
+  __DATA_CONST.__objc_const: 0xd8a8
+  __DATA_CONST.__objc_selrefs: 0x2d38
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_classrefs: 0x488
+  __DATA_CONST.__objc_classrefs: 0x4a8
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__objc_const: 0x19f0
-  __AUTH_CONST.__cfstring: 0x39e0
+  __AUTH_CONST.__objc_const: 0x1a38
+  __AUTH_CONST.__cfstring: 0x3ca0
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x568
-  __AUTH.__objc_data: 0x1018
+  __AUTH_CONST.__auth_got: 0x570
+  __AUTH.__objc_data: 0xf28
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x36c
+  __DATA.__objc_ivar: 0x370
   __DATA.__data: 0xcf0
-  __DATA.__bss: 0xc8
-  __DATA_DIRTY.__objc_data: 0x668
-  __DATA_DIRTY.__bss: 0xf0
+  __DATA.__bss: 0xa8
+  __DATA_DIRTY.__objc_data: 0x7a8
+  __DATA_DIRTY.__bss: 0x110
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D9F92165-6D5B-3F23-AC8D-06E17BDA5127
-  Functions: 2374
-  Symbols:   8052
-  CStrings:  4277
+  UUID: 62BA1309-E1E3-3B7F-BA3B-B51D98F5DEEA
+  Functions: 2391
+  Symbols:   8137
+  CStrings:  4355
 
Symbols:
+ -[CDPDAnalyticsTransport setTtrController:]
+ -[CDPDAnalyticsTransport ttrController]
+ -[CDPDClientHandler sendEvent:].cold.2
+ -[CDPDTTRController _componentIDForEvent:forTTRConfigSupportedErrors:]
+ -[CDPDTTRController _componentIDForEvent:forTTRConfigSupportedErrors:].cold.1
+ -[CDPDTTRController _componentIDForEventErrorDict:inTTRConfigSupportedErrors:]
+ -[CDPDTTRController _isTTREnabledForDict:]
+ -[CDPDTTRController _isTTREnabledForDict:].cold.1
+ -[CDPDTTRController _normalizedTTRErrorForEvent:]
+ -[CDPDTTRController _performTTRForRequest:completion:]
+ -[CDPDTTRController _triggerTTRForEvent:componentName:componentVersion:componentID:]
+ -[CDPDTTRController requestTTRIfSupportedForEvent:]
+ -[CDPDTTRController requestTTRIfSupportedForEvent:].cold.1
+ -[CDPDTTRController requestTTRWithTitle:message:componentName:componentVersion:componentID:keywords:completion:]
+ _AKSilentTTRErrorDomain
+ _CDPFollowUpUIExtensionIdentifier
+ _CDPRPDExtendedProbationTimeInterval
+ _CDPRPDProbationTimeInterval
+ _CDP_FOLLOWUP_ADP_UPSELL
+ _OBJC_CLASS_$_AAFTapToRadarHelper
+ _OBJC_CLASS_$_AAFTapToRadarRequest
+ _OBJC_CLASS_$_AKURLBag
+ _OBJC_CLASS_$_CDPDTTRController
+ _OBJC_IVAR_$_CDPDAnalyticsTransport._ttrController
+ _OBJC_METACLASS_$_CDPDTTRController
+ __AKLogSystem
+ __OBJC_$_INSTANCE_METHODS_CDPDTTRController
+ __OBJC_CLASS_RO_$_CDPDTTRController
+ __OBJC_METACLASS_RO_$_CDPDTTRController
+ ___102-[CDPDSecureBackupController _authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:]_block_invoke.103
+ ___102-[CDPDSecureBackupController _authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:]_block_invoke.103.cold.1
+ ___102-[CDPDSecureBackupController _authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:]_block_invoke.103.cold.2
+ ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.49
+ ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.49.cold.1
+ ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.50
+ ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.51
+ ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.51.cold.1
+ ___113-[CDPInternalWalrusStateController _updateWalrusStateAndPerformPostEnablementActions:context:account:completion:]_block_invoke.64
+ ___113-[CDPInternalWalrusStateController _updateWalrusStateAndPerformPostEnablementActions:context:account:completion:]_block_invoke.64.cold.1
+ ___113-[CDPInternalWalrusStateController _updateWalrusStateAndPerformPostEnablementActions:context:account:completion:]_block_invoke.66
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.141
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.141.cold.1
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.141.cold.2
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.141.cold.3
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.142
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.142.cold.1
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.142.cold.2
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.142.cold.3
+ ___119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.155
+ ___119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.156
+ ___119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.157
+ ___156-[CDPDStateMachine _attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.160
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.435
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.435.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.436
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.436.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.499
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.499.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.499.cold.2
+ ___38-[CDPDStateMachine _attemptCDPEnable:]_block_invoke.111
+ ___54-[CDPDTTRController _performTTRForRequest:completion:]_block_invoke
+ ___55-[CDPDSecureBackupController checkForAnyOctagonRecord:]_block_invoke.78
+ ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.106
+ ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.107
+ ___58-[CDPDStateMachine _handleBeneficiaryTrustWithCompletion:]_block_invoke.78
+ ___62-[CDPDCircleController _joinCircleIgnoringBackups:completion:]_block_invoke.39
+ ___62-[CDPDCircleController _joinCircleIgnoringBackups:completion:]_block_invoke.40
+ ___62-[CDPDCircleController _joinCircleIgnoringBackups:completion:]_block_invoke.40.cold.1
+ ___63-[CDPDSecureBackupController disableRecoveryKeyWithCompletion:]_block_invoke.147
+ ___65-[CDPDClientHandler attemptToEscrowPreRecord:context:completion:]_block_invoke.60
+ ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.108
+ ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.109
+ ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.101
+ ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.88
+ ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.88.cold.1
+ ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.89
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.36
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.36.cold.1
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.36.cold.2
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.39
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.56
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.58
+ ___66-[CDPDStateMachine _handleCloudDataProtectionStateWithCompletion:]_block_invoke.75
+ ___66-[CDPDStateMachine _handleCloudDataProtectionStateWithCompletion:]_block_invoke.76
+ ___67-[CDPDSecureBackupController deleteAllBackupRecordsWithCompletion:]_block_invoke.144
+ ___67-[CDPDSecureBackupController deleteSingleICSCBackupWithCompletion:]_block_invoke.145
+ ___70-[CDPInternalWalrusStateController setWalrusStatusEnabled:completion:]_block_invoke.55
+ ___70-[CDPInternalWalrusStateController setWalrusStatusEnabled:completion:]_block_invoke.55.cold.1
+ ___70-[CDPInternalWalrusStateController setWalrusStatusEnabled:completion:]_block_invoke.56
+ ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.168
+ ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.169
+ ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.169.cold.1
+ ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.170
+ ___72-[CDPDStateMachine _recoverSecureBackupWithCircleJoinResult:completion:]_block_invoke.142
+ ___73-[CDPDClientHandler shouldPerformRepairForContext:forceFetch:completion:]_block_invoke.57
+ ___74-[CDPDSecureBackupController checkForExistingRecordWithPeerId:completion:]_block_invoke.81
+ ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.165
+ ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.165.cold.1
+ ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.166
+ ___75-[CDPDSecureBackupController enableSecureBackupWithRecoveryKey:completion:]_block_invoke.100
+ ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.97
+ ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.97.cold.1
+ ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.97.cold.2
+ ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.97.cold.3
+ ___77-[CDPDEscrowRecordController _performSilentEscrowRecordRepairWithCompletion:]_block_invoke.52
+ ___78-[CDPDTTRController _componentIDForEventErrorDict:inTTRConfigSupportedErrors:]_block_invoke
+ ___79-[CDPDCircleController _joinCircleFallbackWithResult:ignoreBackups:completion:]_block_invoke.43
+ ___79-[CDPDCircleController _requestCircleJoinWithObserver:requestBlock:completion:]_block_invoke.53
+ ___79-[CDPDClientHandler fetchEscrowRecordDevicesWithContext:usingCache:completion:]_block_invoke.34
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.500
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.502
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.502.cold.1
+ ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.143
+ ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.143.cold.1
+ ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.145
+ ___83-[CDPDClientHandler localSecretChangedTo:secretType:context:uiProvider:completion:]_block_invoke.61
+ ___84-[CDPDEscrowRecordController _continueSilentEscrowRecordRepairWithState:completion:]_block_invoke.69
+ ___84-[CDPDEscrowRecordController _continueSilentEscrowRecordRepairWithState:completion:]_block_invoke.69.cold.1
+ ___84-[CDPDTTRController _triggerTTRForEvent:componentName:componentVersion:componentID:]_block_invoke
+ ___85-[CDPDClientHandler _startObservingConnectionStateForRepairWithStateMachine:context:]_block_invoke.53
+ ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.62
+ ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.62.cold.1
+ ___85-[CDPDClientHandler handleCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.44
+ ___85-[CDPDClientHandler repairCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.48
+ ___85-[CDPDRecoveryValidatedJoinFlowController _accountResetRecoveryOptionWithCompletion:]_block_invoke.44
+ ___85-[CDPDStateMachine _attemptBeneficiaryTrustWithInheritanceKey:retryCount:completion:]_block_invoke.87
+ ___86-[CDPDClientHandler shouldPerformAuthenticatedRepairForContext:forceFetch:completion:]_block_invoke.58
+ ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.63
+ ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.63.cold.1
+ ___92-[CDPDSecureBackupController checkForExistingRecordMatchingPredicate:forceFetch:completion:]_block_invoke.83
+ ___92-[CDPDSecureBackupController checkForExistingRecordMatchingPredicate:forceFetch:completion:]_block_invoke.83.cold.1
+ ___93-[CDPDSecureBackupController upgradeICSCRecordsThenEnableSecureBackupWithContext:completion:]_block_invoke.73
+ ___93-[CDPDSecureBackupController upgradeICSCRecordsThenEnableSecureBackupWithContext:completion:]_block_invoke.76
+ ___93-[CDPDSecureBackupController upgradeICSCRecordsThenEnableSecureBackupWithContext:completion:]_block_invoke.76.cold.1
+ ___93-[CDPDSecureBackupController upgradeICSCRecordsThenEnableSecureBackupWithContext:completion:]_block_invoke_2.74
+ ___93-[CDPDSecureBackupController upgradeICSCRecordsThenEnableSecureBackupWithContext:completion:]_block_invoke_2.74.cold.1
+ ___93-[CDPDSecureBackupController upgradeICSCRecordsThenEnableSecureBackupWithContext:completion:]_block_invoke_2.74.cold.2
+ ___98-[CDPDSecureBackupController _getOctagonEscrowBackupRecordDevicesWithOptionForceFetch:completion:]_block_invoke.47
+ ___98-[CDPDSecureBackupController _getOctagonEscrowBackupRecordDevicesWithOptionForceFetch:completion:]_block_invoke.47.cold.1
+ ___98-[CDPDSecureBackupController _getOctagonEscrowBackupRecordDevicesWithOptionForceFetch:completion:]_block_invoke.48
+ ___NSArray0__struct
+ ___block_descriptor_48_e8_32s40s_e25_B24?0"NSDictionary"8Q16ls32l8s40l8
+ ___block_literal_global.258
+ ___block_literal_global.269
+ ___block_literal_global.271
+ ___block_literal_global.356
+ ___block_literal_global.366
+ ___block_literal_global.407
+ ___block_literal_global.419
+ ___block_literal_global.42
+ ___block_literal_global.432
+ ___block_literal_global.504
+ ___block_literal_global.60
+ _kAAFErrorCode
+ _kAAFNumberOfUnderlyingErrors
+ _kAAFUnderlyingErrorCode
+ _kAAFUnderlyingErrorDomain
+ _kADPEnrollAction
+ _kADPUpsellCFURejected
+ _kADPUpsellCFUTriggered
+ _kADPUpsellItemIdentifier
+ _kADPUpsellLandingPageSetUpLaterIniCloudSettingsEscapeOffer
+ _kADPUpsellLandingPageTurnOnEscapeOffer
+ _kADPUpsellLandingPageViewed
+ _kADPUpsellTearDownAction
+ _kCDPAKFollowUpURLKey
+ _kCDPAKNativeActionKey
+ _objc_msgSend$_componentIDForEvent:forTTRConfigSupportedErrors:
+ _objc_msgSend$_componentIDForEventErrorDict:inTTRConfigSupportedErrors:
+ _objc_msgSend$_isTTREnabledForDict:
+ _objc_msgSend$_normalizedTTRErrorForEvent:
+ _objc_msgSend$_performTTRForRequest:completion:
+ _objc_msgSend$_triggerTTRForEvent:componentName:componentVersion:componentID:
+ _objc_msgSend$aaf_filter:
+ _objc_msgSend$configurationAtKey:
+ _objc_msgSend$isEqualToDictionary:
+ _objc_msgSend$reportData
+ _objc_msgSend$requestTTRIfSupportedForEvent:
+ _objc_msgSend$requestTTRWithTitle:message:componentName:componentVersion:componentID:keywords:completion:
+ _objc_msgSend$setComponentID:
+ _objc_msgSend$setComponentName:
+ _objc_msgSend$setComponentVersion:
+ _objc_msgSend$setKeywords:
+ _objc_msgSend$setRadarDescription:
+ _objc_msgSend$setRadarTitle:
+ _objc_msgSend$sharedBag
+ _objc_msgSend$silentTapToRadarWithRequest:completion:
- ___102-[CDPDSecureBackupController _authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:]_block_invoke.97
- ___102-[CDPDSecureBackupController _authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:]_block_invoke.97.cold.1
- ___102-[CDPDSecureBackupController _authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:]_block_invoke.97.cold.2
- ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.43
- ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.43.cold.1
- ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.44
- ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.45
- ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.45.cold.1
- ___113-[CDPInternalWalrusStateController _updateWalrusStateAndPerformPostEnablementActions:context:account:completion:]_block_invoke.58
- ___113-[CDPInternalWalrusStateController _updateWalrusStateAndPerformPostEnablementActions:context:account:completion:]_block_invoke.58.cold.1
- ___113-[CDPInternalWalrusStateController _updateWalrusStateAndPerformPostEnablementActions:context:account:completion:]_block_invoke.60
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.135
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.135.cold.1
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.135.cold.2
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.135.cold.3
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.136
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.136.cold.1
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.136.cold.2
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.136.cold.3
- ___119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.149
- ___119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.150
- ___119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.151
- ___156-[CDPDStateMachine _attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.154
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.413
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.413.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.414
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.414.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.477
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.477.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.477.cold.2
- ___38-[CDPDStateMachine _attemptCDPEnable:]_block_invoke.105
- ___55-[CDPDSecureBackupController checkForAnyOctagonRecord:]_block_invoke.72
- ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.100
- ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.101
- ___58-[CDPDStateMachine _handleBeneficiaryTrustWithCompletion:]_block_invoke.71
- ___62-[CDPDCircleController _joinCircleIgnoringBackups:completion:]_block_invoke.33
- ___62-[CDPDCircleController _joinCircleIgnoringBackups:completion:]_block_invoke.34
- ___62-[CDPDCircleController _joinCircleIgnoringBackups:completion:]_block_invoke.34.cold.1
- ___63-[CDPDSecureBackupController disableRecoveryKeyWithCompletion:]_block_invoke.141
- ___65-[CDPDClientHandler attemptToEscrowPreRecord:context:completion:]_block_invoke.54
- ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.102
- ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.103
- ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.81
- ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.81.cold.1
- ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.82
- ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.94
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.30
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.30.cold.1
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.30.cold.2
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.33
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.49
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.51
- ___66-[CDPDStateMachine _handleCloudDataProtectionStateWithCompletion:]_block_invoke.68
- ___66-[CDPDStateMachine _handleCloudDataProtectionStateWithCompletion:]_block_invoke.69
- ___67-[CDPDSecureBackupController deleteAllBackupRecordsWithCompletion:]_block_invoke.138
- ___67-[CDPDSecureBackupController deleteSingleICSCBackupWithCompletion:]_block_invoke.139
- ___70-[CDPInternalWalrusStateController setWalrusStatusEnabled:completion:]_block_invoke.49
- ___70-[CDPInternalWalrusStateController setWalrusStatusEnabled:completion:]_block_invoke.49.cold.1
- ___70-[CDPInternalWalrusStateController setWalrusStatusEnabled:completion:]_block_invoke.50
- ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.162
- ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.163
- ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.163.cold.1
- ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.164
- ___72-[CDPDStateMachine _recoverSecureBackupWithCircleJoinResult:completion:]_block_invoke.136
- ___73-[CDPDClientHandler shouldPerformRepairForContext:forceFetch:completion:]_block_invoke.51
- ___74-[CDPDSecureBackupController checkForExistingRecordWithPeerId:completion:]_block_invoke.75
- ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.159
- ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.159.cold.1
- ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.160
- ___75-[CDPDSecureBackupController enableSecureBackupWithRecoveryKey:completion:]_block_invoke.94
- ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.91
- ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.91.cold.1
- ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.91.cold.2
- ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.91.cold.3
- ___77-[CDPDEscrowRecordController _performSilentEscrowRecordRepairWithCompletion:]_block_invoke.46
- ___79-[CDPDCircleController _joinCircleFallbackWithResult:ignoreBackups:completion:]_block_invoke.37
- ___79-[CDPDCircleController _requestCircleJoinWithObserver:requestBlock:completion:]_block_invoke.47
- ___79-[CDPDClientHandler fetchEscrowRecordDevicesWithContext:usingCache:completion:]_block_invoke.28
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.478
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.480
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.480.cold.1
- ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.137
- ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.137.cold.1
- ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.139
- ___83-[CDPDClientHandler localSecretChangedTo:secretType:context:uiProvider:completion:]_block_invoke.55
- ___84-[CDPDEscrowRecordController _continueSilentEscrowRecordRepairWithState:completion:]_block_invoke.63
- ___84-[CDPDEscrowRecordController _continueSilentEscrowRecordRepairWithState:completion:]_block_invoke.63.cold.1
- ___85-[CDPDClientHandler _startObservingConnectionStateForRepairWithStateMachine:context:]_block_invoke.47
- ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.56
- ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.56.cold.1
- ___85-[CDPDClientHandler handleCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.38
- ___85-[CDPDClientHandler repairCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.42
- ___85-[CDPDRecoveryValidatedJoinFlowController _accountResetRecoveryOptionWithCompletion:]_block_invoke.38
- ___85-[CDPDStateMachine _attemptBeneficiaryTrustWithInheritanceKey:retryCount:completion:]_block_invoke.80
- ___86-[CDPDClientHandler shouldPerformAuthenticatedRepairForContext:forceFetch:completion:]_block_invoke.52
- ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.57
- ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.57.cold.1
- ___92-[CDPDSecureBackupController checkForExistingRecordMatchingPredicate:forceFetch:completion:]_block_invoke.77
- ___92-[CDPDSecureBackupController checkForExistingRecordMatchingPredicate:forceFetch:completion:]_block_invoke.77.cold.1
- ___93-[CDPDSecureBackupController upgradeICSCRecordsThenEnableSecureBackupWithContext:completion:]_block_invoke.67
- ___93-[CDPDSecureBackupController upgradeICSCRecordsThenEnableSecureBackupWithContext:completion:]_block_invoke.70
- ___93-[CDPDSecureBackupController upgradeICSCRecordsThenEnableSecureBackupWithContext:completion:]_block_invoke.70.cold.1
- ___93-[CDPDSecureBackupController upgradeICSCRecordsThenEnableSecureBackupWithContext:completion:]_block_invoke_2.68
- ___93-[CDPDSecureBackupController upgradeICSCRecordsThenEnableSecureBackupWithContext:completion:]_block_invoke_2.68.cold.1
- ___93-[CDPDSecureBackupController upgradeICSCRecordsThenEnableSecureBackupWithContext:completion:]_block_invoke_2.68.cold.2
- ___98-[CDPDSecureBackupController _getOctagonEscrowBackupRecordDevicesWithOptionForceFetch:completion:]_block_invoke.41
- ___98-[CDPDSecureBackupController _getOctagonEscrowBackupRecordDevicesWithOptionForceFetch:completion:]_block_invoke.41.cold.1
- ___98-[CDPDSecureBackupController _getOctagonEscrowBackupRecordDevicesWithOptionForceFetch:completion:]_block_invoke.42
- ___block_literal_global.236
- ___block_literal_global.247
- ___block_literal_global.249
- ___block_literal_global.28
- ___block_literal_global.30
- ___block_literal_global.344
- ___block_literal_global.385
- ___block_literal_global.397
- ___block_literal_global.410
- ___block_literal_global.482
- ___block_literal_global.53
CStrings:
+ "\"Missing ttr configs for event - %@\""
+ "\"TTR filed for event - %@ with status - %d and error - %@\""
+ "%@ \nEvent Details - \n%@"
+ "@\"CDPDTTRController\""
+ "AAA team is analyzing an issue for the event %@. It will be very helpful if you can complete the TTR and file the radar with sysdiagnose. Thank you for your help, have a wonderful day."
+ "AKFollowUpServerURL"
+ "Analyzing error for the event %@"
+ "B24@?0@\"NSDictionary\"8Q16"
+ "CDPDTTRController"
+ "CoreCDP received request for TTR on non-internal build, ignoring."
+ "Dropping event (On Shared iPad), not supported: %@"
+ "T@\"CDPDTTRController\",&,N,V_ttrController"
+ "Unable to send TTR for event %@. Component ID - %@, name - %@, version - %@"
+ "[%@] [%@] DELIVERY BEGIN"
+ "_componentIDForEvent:forTTRConfigSupportedErrors:"
+ "_componentIDForEventErrorDict:inTTRConfigSupportedErrors:"
+ "_isTTREnabledForDict:"
+ "_normalizedTTRErrorForEvent:"
+ "_performTTRForRequest:completion:"
+ "_triggerTTRForEvent:componentName:componentVersion:componentID:"
+ "_ttrController"
+ "aaf_filter:"
+ "adpEnroll"
+ "adpUpsell"
+ "adpUpsellTearDown"
+ "ak-native-action"
+ "cid"
+ "cn"
+ "com.apple.appleaccount.custodianFirstTimeSetup"
+ "com.apple.appleaccount.custodianInviteSent"
+ "com.apple.appleaccount.familyCustodianAdded"
+ "com.apple.authkit.token.ck.delete"
+ "com.apple.authkit.token.prk.delete"
+ "componentInfo"
+ "configurationAtKey:"
+ "cv"
+ "ec"
+ "ed"
+ "isEqualToDictionary:"
+ "pt"
+ "reportData"
+ "requestTTRIfSupportedForEvent:"
+ "requestTTRWithTitle:message:componentName:componentVersion:componentID:keywords:completion:"
+ "setComponentID:"
+ "setComponentName:"
+ "setComponentVersion:"
+ "setKeywords:"
+ "setRadarDescription:"
+ "setRadarTitle:"
+ "setTtrController:"
+ "sharedBag"
+ "silentTapToRadarWithRequest:completion:"
+ "ttr-cfgs normalized mid drift ttrFrequency - %ld and  randomNumber - %ld"
+ "ttr-cfgs-v2"
+ "ttrController"
+ "uec%lu"
+ "ued%lu"
+ "v48@0:8@16@24@32@40"
- "[%@] [%@] DELIVERY BEGIN - %@"
- "com.apple.CoreCDPUI.CDPFollowUpExtension"

```
