## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-359.4.6.0.0
-  __TEXT.__text: 0x63d80
-  __TEXT.__auth_stubs: 0xa90
-  __TEXT.__objc_methlist: 0x3988
+359.13.0.0.0
+  __TEXT.__text: 0x66d58
+  __TEXT.__auth_stubs: 0xab0
+  __TEXT.__objc_methlist: 0x3ab0
   __TEXT.__const: 0x90
-  __TEXT.__oslogstring: 0xf274
-  __TEXT.__cstring: 0x3ba8
-  __TEXT.__gcc_except_tab: 0x7a0
-  __TEXT.__unwind_info: 0x1400
-  __TEXT.__objc_classname: 0xb4b
-  __TEXT.__objc_methname: 0xbef6
-  __TEXT.__objc_methtype: 0x2232
-  __TEXT.__objc_stubs: 0x9dc0
-  __DATA_CONST.__got: 0x820
-  __DATA_CONST.__const: 0x1a28
+  __TEXT.__oslogstring: 0xfb6d
+  __TEXT.__cstring: 0x49b2
+  __TEXT.__gcc_except_tab: 0x78c
+  __TEXT.__unwind_info: 0x1494
+  __TEXT.__objc_classname: 0xb63
+  __TEXT.__objc_methname: 0xc3be
+  __TEXT.__objc_methtype: 0x228a
+  __TEXT.__objc_stubs: 0xa1c0
+  __DATA_CONST.__got: 0x868
+  __DATA_CONST.__const: 0x1aa0
   __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x108
+  __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xd700
-  __DATA_CONST.__objc_selrefs: 0x2b88
+  __DATA_CONST.__objc_const: 0xd830
+  __DATA_CONST.__objc_selrefs: 0x2c88
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x488
+  __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x68
   __AUTH_CONST.__objc_const: 0x19f0
-  __AUTH_CONST.__cfstring: 0x3080
-  __AUTH_CONST.__const: 0x360
+  __AUTH_CONST.__cfstring: 0x39e0
+  __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x558
-  __AUTH.__objc_data: 0x1068
+  __AUTH_CONST.__auth_got: 0x568
+  __AUTH.__objc_data: 0x1018
   __AUTH.__data: 0x10
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x488
-  __DATA.__objc_superrefs: 0x150
   __DATA.__objc_ivar: 0x36c
-  __DATA.__data: 0xc90
-  __DATA.__bss: 0x120
-  __DATA_DIRTY.__objc_data: 0x618
-  __DATA_DIRTY.__bss: 0x68
+  __DATA.__data: 0xcf0
+  __DATA.__bss: 0xc8
+  __DATA_DIRTY.__objc_data: 0x668
+  __DATA_DIRTY.__bss: 0xf0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2287
-  Symbols:   7817
-  CStrings:  3657
+  Functions: 2374
+  Symbols:   8052
+  CStrings:  3814
 
Symbols:
+ +[CDPDAnalyticsTransport flushCaches].cold.1
+ +[CDPDAnalyticsTransport flushCaches].cold.2
+ +[CDPDAnalyticsTransport flushTransportCache]
+ +[CDPDAnalyticsTransport flushTransportCache].cold.1
+ +[CDPDAnalyticsTransport flushTransportCache].cold.2
+ +[CDPDAnalyticsTransport getAllowedADPEvents]
+ +[CDPDAnalyticsTransport getAllowedDNUEvents]
+ +[CDPDAnalyticsTransport getAllowedSecurityEvents]
+ +[CDPDAnalyticsTransport getApprovedEvents:]
+ +[CDPDAnalyticsTransport getApprovedEventsForADPAndDNU]
+ +[CDPDAnalyticsTransport isEventPrivacyApproved:]
+ -[CDPDAnalyticsTransport _sendEvent:]
+ -[CDPDAnalyticsTransport _sendEvent:].cold.1
+ -[CDPDAnalyticsTransport _sendEvent:].cold.2
+ -[CDPDAnalyticsTransport _sendEvent:].cold.3
+ -[CDPDAnalyticsTransport _updateEventWithDefaultMetadata:]
+ -[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]
+ -[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:].cold.1
+ -[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:].cold.2
+ -[CDPDAnalyticsTransport sendEvent:].cold.2
+ -[CDPDClientHandler _localDeviceHasLocalSecret]
+ -[CDPDClientHandler _shouldForceUseSecureBackupCachedPassphraseWithContext:clientType:]
+ -[CDPDClientHandler _shouldForceUseSecureBackupCachedPassphraseWithContext:clientType:].cold.1
+ -[CDPDClientHandler handleCloudDataProtectionStateWithContext:uiProvider:completion:].cold.2
+ -[CDPDEscrowRecordController _cdpStateMachineWithNilUIProvider]
+ -[CDPDRecoveryValidatedJoinFlowController .cxx_destruct]
+ -[CDPDRecoveryValidatedJoinFlowController _deviceSelectionRecoveryOptionWithCompletion:]
+ -[CDPDRecoveryValidatedJoinFlowController _entryLimitDeviceSelectionAvailableBodyForDevice:]
+ -[CDPDRecoveryValidatedJoinFlowController _tryAgainLaterOptionWithCompletion:]
+ -[CDPDRecoveryValidatedJoinFlowController cdpDevices]
+ -[CDPDRecoveryValidatedJoinFlowController setCdpDevices:]
+ -[CDPDSOSSecureBackupController _recoverBackupDictionaryWithContext:fallbackState:error:]
+ -[CDPDSOSSecureBackupController _recoverBackupDictionaryWithContext:fallbackState:error:].cold.1
+ -[CDPDSOSSecureBackupController _recoverBackupDictionaryWithContext:fallbackState:error:].cold.2
+ -[CDPDSOSSecureBackupController _recoverBackupDictionaryWithContext:fallbackState:error:].cold.3
+ -[CDPDSOSSecureBackupController _recoverBackupDictionaryWithContext:fallbackState:error:].cold.4
+ -[CDPDSOSSecureBackupController _recoveryInfoDictionaryFromContext:usePreviouslyCachedSecret:]
+ -[CDPDSOSSecureBackupController _shouldUseSBDCacheWithSecureBackupContext:fallbackState:]
+ -[CDPDSOSSecureBackupController _shouldUseSBDCacheWithSecureBackupContext:fallbackState:].cold.1
+ -[CDPDSecureBackupController _authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:]
+ -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:fallbackState:completion:]
+ -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:fallbackState:completion:].cold.1
+ -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:fallbackState:completion:].cold.10
+ -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:fallbackState:completion:].cold.11
+ -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:fallbackState:completion:].cold.2
+ -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:fallbackState:completion:].cold.3
+ -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:fallbackState:completion:].cold.4
+ -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:fallbackState:completion:].cold.5
+ -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:fallbackState:completion:].cold.6
+ -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:fallbackState:completion:].cold.7
+ -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:fallbackState:completion:].cold.8
+ -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:fallbackState:completion:].cold.9
+ -[CDPDSecureBackupController _disableSecureBackupWithEnableInfo:error:].cold.3
+ -[CDPDSecureBackupController _handleSecureBackupEnablementError:fallbackState:context:delegate:completion:]
+ -[CDPDSecureBackupController _handleSecureBackupEnablementError:fallbackState:context:delegate:completion:].cold.1
+ -[CDPDSecureBackupController _handleSecureBackupEnablementError:fallbackState:context:delegate:completion:].cold.2
+ -[CDPDSecureBackupController _handleSecureBackupEnablementError:fallbackState:context:delegate:completion:].cold.3
+ -[CDPDSecureBackupController _handleSecureBackupEnablementError:fallbackState:context:delegate:completion:].cold.4
+ -[CDPDSecureBackupController _handleSecureBackupEnablementError:fallbackState:context:delegate:completion:].cold.5
+ -[CDPDSecureBackupController _handleSecureBackupEnablementError:fallbackState:context:delegate:completion:].cold.6
+ -[CDPDSecureBackupController _performEscrowRecoveryWithRecoveryContext:fallbackState:error:]
+ -[CDPDSecureBackupController _performEscrowRecoveryWithRecoveryContext:fallbackState:error:].cold.1
+ -[CDPDSecureBackupController _performEscrowRecoveryWithRecoveryContext:fallbackState:error:].cold.10
+ -[CDPDSecureBackupController _performEscrowRecoveryWithRecoveryContext:fallbackState:error:].cold.11
+ -[CDPDSecureBackupController _performEscrowRecoveryWithRecoveryContext:fallbackState:error:].cold.12
+ -[CDPDSecureBackupController _performEscrowRecoveryWithRecoveryContext:fallbackState:error:].cold.13
+ -[CDPDSecureBackupController _performEscrowRecoveryWithRecoveryContext:fallbackState:error:].cold.2
+ -[CDPDSecureBackupController _performEscrowRecoveryWithRecoveryContext:fallbackState:error:].cold.3
+ -[CDPDSecureBackupController _performEscrowRecoveryWithRecoveryContext:fallbackState:error:].cold.4
+ -[CDPDSecureBackupController _performEscrowRecoveryWithRecoveryContext:fallbackState:error:].cold.5
+ -[CDPDSecureBackupController _performEscrowRecoveryWithRecoveryContext:fallbackState:error:].cold.6
+ -[CDPDSecureBackupController _performEscrowRecoveryWithRecoveryContext:fallbackState:error:].cold.7
+ -[CDPDSecureBackupController _performEscrowRecoveryWithRecoveryContext:fallbackState:error:].cold.8
+ -[CDPDSecureBackupController _performEscrowRecoveryWithRecoveryContext:fallbackState:error:].cold.9
+ -[CDPDSecureBackupController _recoverBackupDictionaryWithContext:fallbackState:error:]
+ -[CDPDSecureBackupController _recoverBackupDictionaryWithContext:fallbackState:error:].cold.1
+ -[CDPDSecureBackupController _recoverBackupDictionaryWithContext:fallbackState:error:].cold.2
+ -[CDPDSecureBackupController _recoverBackupDictionaryWithContext:fallbackState:error:].cold.3
+ -[CDPDSecureBackupController _recoverBackupDictionaryWithContext:fallbackState:error:].cold.4
+ -[CDPDSecureBackupController _recoveryInfoDictionaryFromContext:usePreviouslyCachedSecret:]
+ -[CDPDSecureBackupController _recoveryInfoDictionaryFromContext:usePreviouslyCachedSecret:].cold.1
+ -[CDPDSecureBackupController _shouldUseSBDCacheWithSecureBackupContext:fallbackState:]
+ -[CDPDSecureBackupController _shouldUseSBDCacheWithSecureBackupContext:fallbackState:].cold.1
+ -[CDPDSecureBackupProxyImpl _cleanUpPostEscrowCreationStates]
+ -[CDPDSecureBackupProxyImpl _cleanUpPostEscrowCreationStates].cold.1
+ -[CDPDStateMachine _attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useSecureBackupCachedSecret:circleJoinResult:completion:]
+ -[CDPDStateMachine _attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useSecureBackupCachedSecret:circleJoinResult:completion:].cold.1
+ -[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]
+ -[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:].cold.1
+ -[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:].cold.2
+ -[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:].cold.3
+ -[CDPDStateMachine _checkSecureBackupCachedSecretValue]
+ -[CDPDStateMachine _recoveryFlowControllerForKeychainSyncSystem:recoveryContext:]
+ -[CDPDStateMachine secureBackupEnableController]
+ -[CDPDStateMachine setSecureBackupEnableController:]
+ -[NSError(SecureBackup) indicatesRecoveryCanBeRetried]
+ -[NSError(SecureBackup) isMissingCachedPassphraseError]
+ GCC_except_table40
+ GCC_except_table77
+ GCC_except_table83
+ GCC_except_table85
+ GCC_except_table90
+ GCC_except_table91
+ _OBJC_IVAR_$_CDPDRecoveryValidatedJoinFlowController._cdpDevices
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ __CDPLogSystemAnalytics
+ __OBJC_$_INSTANCE_VARIABLES_CDPDRecoveryValidatedJoinFlowController
+ __OBJC_$_PROP_LIST_AAFAnalyticstRTCTransport
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AAFAnalyticstRTCTransport
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AAFAnalyticstRTCTransport
+ __OBJC_$_PROTOCOL_REFS_AAFAnalyticstRTCTransport
+ __OBJC_LABEL_PROTOCOL_$_AAFAnalyticstRTCTransport
+ __OBJC_PROTOCOL_$_AAFAnalyticstRTCTransport
+ __OBJC_PROTOCOL_REFERENCE_$_AAFAnalyticstRTCTransport
+ ___102-[CDPDSecureBackupController _authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:]_block_invoke
+ ___102-[CDPDSecureBackupController _authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:]_block_invoke.97
+ ___102-[CDPDSecureBackupController _authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:]_block_invoke.97.cold.1
+ ___102-[CDPDSecureBackupController _authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:]_block_invoke.97.cold.2
+ ___102-[CDPDSecureBackupController _authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:]_block_invoke.cold.1
+ ___102-[CDPDSecureBackupController _authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:]_block_invoke.cold.2
+ ___102-[CDPDSecureBackupController _authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:]_block_invoke.cold.3
+ ___102-[CDPDSecureBackupController _authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:]_block_invoke.cold.4
+ ___102-[CDPDSecureBackupController _authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:]_block_invoke.cold.5
+ ___107-[CDPDSecureBackupController _handleSecureBackupEnablementError:fallbackState:context:delegate:completion:]_block_invoke
+ ___107-[CDPDSecureBackupController _handleSecureBackupEnablementError:fallbackState:context:delegate:completion:]_block_invoke.cold.1
+ ___107-[CDPDSecureBackupController _handleSecureBackupEnablementError:fallbackState:context:delegate:completion:]_block_invoke.cold.2
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.135
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.135.cold.1
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.135.cold.2
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.135.cold.3
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.136
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.136.cold.1
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.136.cold.2
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.136.cold.3
+ ___119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke
+ ___119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.149
+ ___119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.150
+ ___119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.151
+ ___156-[CDPDStateMachine _attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke
+ ___156-[CDPDStateMachine _attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.154
+ ___156-[CDPDStateMachine _attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.413
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.413.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.414
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.414.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.477
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.477.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.477.cold.2
+ ___37-[CDPDAnalyticsTransport _sendEvent:]_block_invoke
+ ___38-[CDPDStateMachine _attemptCDPEnable:]_block_invoke.105
+ ___45+[CDPDAnalyticsTransport getAllowedADPEvents]_block_invoke
+ ___45+[CDPDAnalyticsTransport getAllowedDNUEvents]_block_invoke
+ ___50+[CDPDAnalyticsTransport getAllowedSecurityEvents]_block_invoke
+ ___55+[CDPDAnalyticsTransport getApprovedEventsForADPAndDNU]_block_invoke
+ ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.100
+ ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.101
+ ___56-[CDPDSecureChannelController _startListeningWithProxy:]_block_invoke.79
+ ___58-[CDPDAnalyticsTransport _updateEventWithDefaultMetadata:]_block_invoke
+ ___58-[CDPDAnalyticsTransport _updateEventWithDefaultMetadata:]_block_invoke.cold.1
+ ___58-[CDPDStateMachine _handleBeneficiaryTrustWithCompletion:]_block_invoke.71
+ ___63-[CDPDSecureBackupController disableRecoveryKeyWithCompletion:]_block_invoke.141
+ ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.102
+ ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.103
+ ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.81
+ ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.81.cold.1
+ ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.82
+ ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.94
+ ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke_2
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.30.cold.1
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.30.cold.2
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.33
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.49
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.51
+ ___66-[CDPDStateMachine _handleCloudDataProtectionStateWithCompletion:]_block_invoke.68
+ ___66-[CDPDStateMachine _handleCloudDataProtectionStateWithCompletion:]_block_invoke.69
+ ___67-[CDPDSecureBackupController deleteAllBackupRecordsWithCompletion:]_block_invoke.138
+ ___67-[CDPDSecureBackupController deleteSingleICSCBackupWithCompletion:]_block_invoke.139
+ ___70-[CDPDKeychainSync _setUserVisibleKeychainSyncEnabled:withCompletion:]_block_invoke.107
+ ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.162
+ ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.163
+ ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.163.cold.1
+ ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.164
+ ___72-[CDPDStateMachine _recoverSecureBackupWithCircleJoinResult:completion:]_block_invoke.136
+ ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.159
+ ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.159.cold.1
+ ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.160
+ ___78-[CDPDRecoveryValidatedJoinFlowController _tryAgainLaterOptionWithCompletion:]_block_invoke
+ ___78-[CDPDRecoveryValidatedJoinFlowController _tryAgainLaterOptionWithCompletion:]_block_invoke.cold.1
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.478
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.480
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.480.cold.1
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.cold.1
+ ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.137
+ ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.137.cold.1
+ ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.139
+ ___84-[CDPDEscrowRecordController _continueSilentEscrowRecordRepairWithState:completion:]_block_invoke.63
+ ___84-[CDPDEscrowRecordController _continueSilentEscrowRecordRepairWithState:completion:]_block_invoke.63.cold.1
+ ___85-[CDPDClientHandler handleCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.38
+ ___85-[CDPDClientHandler repairCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.42
+ ___85-[CDPDStateMachine _attemptBeneficiaryTrustWithInheritanceKey:retryCount:completion:]_block_invoke.80
+ ___88-[CDPDRecoveryValidatedJoinFlowController _deviceSelectionRecoveryOptionWithCompletion:]_block_invoke
+ ___88-[CDPDRecoveryValidatedJoinFlowController _deviceSelectionRecoveryOptionWithCompletion:]_block_invoke.cold.1
+ ___block_descriptor_40_e8_32bs_e34_v32?0"AAFAnalyticsEvent"8Q16^B24ls32l8
+ ___block_descriptor_48_e8_32s40s_e27_v16?0"AAFAnalyticsEvent"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e24_v32?0"NSData"8^16^24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e20_v20?0B8"NSError"12lr56l8r64l8s32l8s40l8s48l8
+ ___block_literal_global.236
+ ___block_literal_global.247
+ ___block_literal_global.249
+ ___block_literal_global.28
+ ___block_literal_global.36
+ ___block_literal_global.385
+ ___block_literal_global.397
+ ___block_literal_global.410
+ ___block_literal_global.482
+ ___block_literal_global.53
+ _getAllowedADPEvents.approvedEvents
+ _getAllowedADPEvents.onceToken
+ _getAllowedDNUEvents.approvedEvents
+ _getAllowedDNUEvents.onceToken
+ _getAllowedSecurityEvents.approvedSecurityEvents
+ _getAllowedSecurityEvents.onceToken
+ _getApprovedEventsForADPAndDNU.approvedEvents
+ _getApprovedEventsForADPAndDNU.onceToken
+ _kAACustodianPostRepairCFUEvent
+ _kAACustodianPreflightEvent
+ _kAACustodianRemoveEvent
+ _kAACustodianRepairCFUActionBeginEvent
+ _kAACustodianRepairCFUActionEndEvent
+ _kAACustodianRepairEvent
+ _kAAFDeviceSessionIdString
+ _kAAFFlowIdString
+ _kAAFTestSignatureString
+ _kAATrustedContactsPreflightBeginEvent
+ _kAATrustedContactsPreflightEndEvent
+ _objc_msgSend$DSIDForAccount:
+ _objc_msgSend$_attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useSecureBackupCachedSecret:circleJoinResult:completion:
+ _objc_msgSend$_attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:
+ _objc_msgSend$_authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:
+ _objc_msgSend$_authenticatedEnableSecureBackupWithContext:fallbackState:completion:
+ _objc_msgSend$_cdpStateMachineWithNilUIProvider
+ _objc_msgSend$_checkSecureBackupCachedSecretValue
+ _objc_msgSend$_cleanUpPostEscrowCreationStates
+ _objc_msgSend$_deviceSelectionRecoveryOptionWithCompletion:
+ _objc_msgSend$_entryLimitDeviceSelectionAvailableBodyForDevice:
+ _objc_msgSend$_handleSecureBackupEnablementError:fallbackState:context:delegate:completion:
+ _objc_msgSend$_performEscrowRecoveryWithRecoveryContext:fallbackState:error:
+ _objc_msgSend$_recoverBackupDictionaryWithContext:fallbackState:error:
+ _objc_msgSend$_recoveryFlowControllerForKeychainSyncSystem:recoveryContext:
+ _objc_msgSend$_recoveryInfoDictionaryFromContext:usePreviouslyCachedSecret:
+ _objc_msgSend$_sendEvent:
+ _objc_msgSend$_shouldForceUseSecureBackupCachedPassphraseWithContext:clientType:
+ _objc_msgSend$_shouldUseSBDCacheWithSecureBackupContext:fallbackState:
+ _objc_msgSend$_tryAgainLaterOptionWithCompletion:
+ _objc_msgSend$_updateEventWithDefaultMetadata:
+ _objc_msgSend$configureReportingSessionWithCompletion:
+ _objc_msgSend$configureSessionForEvent:sendEventBlock:telemetryQueue:
+ _objc_msgSend$deleteCreatePasscodeFollowUp
+ _objc_msgSend$eventQueue
+ _objc_msgSend$flushTransportCache
+ _objc_msgSend$getAllowedADPEvents
+ _objc_msgSend$getAllowedDNUEvents
+ _objc_msgSend$getAllowedSecurityEvents
+ _objc_msgSend$getApprovedEvents:
+ _objc_msgSend$getApprovedEventsForADPAndDNU
+ _objc_msgSend$indicatesRecoveryCanBeRetried
+ _objc_msgSend$isEventPrivacyApproved:
+ _objc_msgSend$isLocalSecretCached
+ _objc_msgSend$isMissingCachedPassphraseError
+ _objc_msgSend$isSilentBurnCDPRepairEnabled
+ _objc_msgSend$isSilentBurnInMiniBuddyEnabled
+ _objc_msgSend$sessionGracePeriod
+ _objc_msgSend$sessionState
+ _objc_msgSend$setSessionState:
+ _objc_msgSend$setWithSet:
+ _objc_msgSend$transport
+ _objc_msgSend$unionSet:
+ _objc_msgSend$useCDPContextSecretInsteadOfSBDSecretFeatureEnabled
+ _objc_release_x3
- +[CDPDAnalyticsTransport getAllowedEvents]
- -[CDPDAnalyticsTransport setShouldSendAnalyticsData:]
- -[CDPDAnalyticsTransport shouldSendAnalyticsData]
- -[CDPDRecoveryValidatedJoinFlowController _entryLimitRecoveryKeyAndCustodianRecoveryAvailableBodyForDevice:]
- -[CDPDRecoveryValidatedJoinFlowController _hardLimitUserInfoForDevice:]
- -[CDPDSOSSecureBackupController _recoverBackupDictionaryWithContext:error:]
- -[CDPDSOSSecureBackupController _recoverBackupDictionaryWithContext:error:].cold.1
- -[CDPDSOSSecureBackupController _recoverBackupDictionaryWithContext:error:].cold.2
- -[CDPDSOSSecureBackupController _recoverBackupDictionaryWithContext:error:].cold.3
- -[CDPDSOSSecureBackupController _recoverBackupDictionaryWithContext:error:].cold.4
- -[CDPDSOSSecureBackupController _recoveryInfoDictionaryFromContext:]
- -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:completion:]
- -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:completion:].cold.1
- -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:completion:].cold.10
- -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:completion:].cold.2
- -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:completion:].cold.3
- -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:completion:].cold.4
- -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:completion:].cold.5
- -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:completion:].cold.6
- -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:completion:].cold.7
- -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:completion:].cold.8
- -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:completion:].cold.9
- -[CDPDSecureBackupController _handleSecureBackupEnablementError:context:delegate:completion:]
- -[CDPDSecureBackupController _handleSecureBackupEnablementError:context:delegate:completion:].cold.1
- -[CDPDSecureBackupController _handleSecureBackupEnablementError:context:delegate:completion:].cold.2
- -[CDPDSecureBackupController _handleSecureBackupEnablementError:context:delegate:completion:].cold.3
- -[CDPDSecureBackupController _handleSecureBackupEnablementError:context:delegate:completion:].cold.4
- -[CDPDSecureBackupController _handleSecureBackupEnablementError:context:delegate:completion:].cold.5
- -[CDPDSecureBackupController _recoverBackupDictionaryWithContext:error:]
- -[CDPDSecureBackupController _recoverBackupDictionaryWithContext:error:].cold.1
- -[CDPDSecureBackupController _recoverBackupDictionaryWithContext:error:].cold.2
- -[CDPDSecureBackupController _recoverBackupDictionaryWithContext:error:].cold.3
- -[CDPDSecureBackupController _recoverBackupDictionaryWithContext:error:].cold.4
- -[CDPDSecureBackupController _recoveryInfoDictionaryFromContext:]
- -[CDPDSecureBackupController performEscrowRecoveryWithRecoveryContext:error:].cold.1
- -[CDPDSecureBackupController performEscrowRecoveryWithRecoveryContext:error:].cold.10
- -[CDPDSecureBackupController performEscrowRecoveryWithRecoveryContext:error:].cold.11
- -[CDPDSecureBackupController performEscrowRecoveryWithRecoveryContext:error:].cold.12
- -[CDPDSecureBackupController performEscrowRecoveryWithRecoveryContext:error:].cold.13
- -[CDPDSecureBackupController performEscrowRecoveryWithRecoveryContext:error:].cold.2
- -[CDPDSecureBackupController performEscrowRecoveryWithRecoveryContext:error:].cold.3
- -[CDPDSecureBackupController performEscrowRecoveryWithRecoveryContext:error:].cold.4
- -[CDPDSecureBackupController performEscrowRecoveryWithRecoveryContext:error:].cold.5
- -[CDPDSecureBackupController performEscrowRecoveryWithRecoveryContext:error:].cold.6
- -[CDPDSecureBackupController performEscrowRecoveryWithRecoveryContext:error:].cold.7
- -[CDPDSecureBackupController performEscrowRecoveryWithRecoveryContext:error:].cold.8
- -[CDPDSecureBackupController performEscrowRecoveryWithRecoveryContext:error:].cold.9
- -[CDPDSecureBackupProxyImpl _resetEscrowMissingPromptDebounceCount]
- -[CDPDSecureBackupProxyImpl _resetEscrowMissingPromptDebounceCount].cold.1
- -[CDPDStateMachine _attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useCachedSecret:circleJoinResult:completion:]
- -[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useCachedSecret:circleJoinResult:completion:]
- -[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useCachedSecret:circleJoinResult:completion:].cold.1
- -[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useCachedSecret:circleJoinResult:completion:].cold.2
- GCC_except_table20
- GCC_except_table23
- GCC_except_table26
- GCC_except_table69
- GCC_except_table78
- GCC_except_table80
- GCC_except_table86
- GCC_except_table88
- _OBJC_IVAR_$_CDPDAnalyticsTransport._shouldSendAnalyticsData
- ___107-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useCachedSecret:circleJoinResult:completion:]_block_invoke
- ___107-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useCachedSecret:circleJoinResult:completion:]_block_invoke.134
- ___107-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useCachedSecret:circleJoinResult:completion:]_block_invoke.135
- ___107-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useCachedSecret:circleJoinResult:completion:]_block_invoke.136
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.133
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.133.cold.1
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.133.cold.2
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.133.cold.3
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.134
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.134.cold.1
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.134.cold.2
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.134.cold.3
- ___144-[CDPDStateMachine _attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useCachedSecret:circleJoinResult:completion:]_block_invoke
- ___144-[CDPDStateMachine _attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useCachedSecret:circleJoinResult:completion:]_block_invoke.141
- ___144-[CDPDStateMachine _attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useCachedSecret:circleJoinResult:completion:]_block_invoke.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.201
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.201.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.202
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.202.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.205
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.219
- ___38-[CDPDStateMachine _attemptCDPEnable:]_block_invoke.90
- ___42+[CDPDAnalyticsTransport getAllowedEvents]_block_invoke
- ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.85
- ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.86
- ___56-[CDPDSecureChannelController _startListeningWithProxy:]_block_invoke.77
- ___58-[CDPDStateMachine _handleBeneficiaryTrustWithCompletion:]_block_invoke.68
- ___63-[CDPDSecureBackupController disableRecoveryKeyWithCompletion:]_block_invoke.139
- ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.87
- ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.88
- ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.78
- ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.78.cold.1
- ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.79
- ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.80
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.27
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.27.cold.1
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.27.cold.2
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.46
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.48
- ___66-[CDPDStateMachine _handleCloudDataProtectionStateWithCompletion:]_block_invoke.65
- ___66-[CDPDStateMachine _handleCloudDataProtectionStateWithCompletion:]_block_invoke.66
- ___67-[CDPDSecureBackupController deleteAllBackupRecordsWithCompletion:]_block_invoke.136
- ___67-[CDPDSecureBackupController deleteSingleICSCBackupWithCompletion:]_block_invoke.137
- ___70-[CDPDKeychainSync _setUserVisibleKeychainSyncEnabled:withCompletion:]_block_invoke.106
- ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.147
- ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.148
- ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.148.cold.1
- ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.149
- ___72-[CDPDStateMachine _recoverSecureBackupWithCircleJoinResult:completion:]_block_invoke.121
- ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.144
- ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.144.cold.1
- ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.145
- ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.122
- ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.122.cold.1
- ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.124
- ___84-[CDPDEscrowRecordController _continueSilentEscrowRecordRepairWithState:completion:]_block_invoke.cold.1
- ___85-[CDPDClientHandler handleCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.39
- ___85-[CDPDClientHandler repairCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.41
- ___85-[CDPDStateMachine _attemptBeneficiaryTrustWithInheritanceKey:retryCount:completion:]_block_invoke.77
- ___93-[CDPDSecureBackupController _handleSecureBackupEnablementError:context:delegate:completion:]_block_invoke
- ___93-[CDPDSecureBackupController _handleSecureBackupEnablementError:context:delegate:completion:]_block_invoke.cold.1
- ___93-[CDPDSecureBackupController _handleSecureBackupEnablementError:context:delegate:completion:]_block_invoke.cold.2
- ___block_descriptor_56_e8_32s40s48s_e24_v32?0"NSData"8^16^24ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_literal_global.131
- ___block_literal_global.172
- ___block_literal_global.184
- ___block_literal_global.197
- ___block_literal_global.26
- ___block_literal_global.33
- ___block_literal_global.44
- ___block_literal_global.50
- ___block_literal_global.55
- ___block_literal_global.57
- _getAllowedEvents.approvedEvents
- _getAllowedEvents.onceToken
- _kAAFEventName
- _kAAFTestSignature
- _objc_msgSend$_attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useCachedSecret:circleJoinResult:completion:
- _objc_msgSend$_attemptBackupRecoveryWithLocalSecret:type:useCachedSecret:circleJoinResult:completion:
- _objc_msgSend$_authenticatedEnableSecureBackupWithContext:completion:
- _objc_msgSend$_entryLimitRecoveryKeyAndCustodianRecoveryAvailableBodyForDevice:
- _objc_msgSend$_handleSecureBackupEnablementError:context:delegate:completion:
- _objc_msgSend$_recoverBackupDictionaryWithContext:error:
- _objc_msgSend$_recoveryInfoDictionaryFromContext:
- _objc_msgSend$_resetEscrowMissingPromptDebounceCount
- _objc_msgSend$cachedPassphraseMissing
- _objc_msgSend$clientBundleId
- _objc_msgSend$getAllowedEvents
CStrings:
+ "\"%@: Cannot determine escrow record for unknown account with altDSID (%{mask.hash}@)\""
+ "\"%@: Cannot perform silent burn in mini-buddy due to server-side disablement\""
+ "\"%@: Device not in circle; will try a silent burn recovery...\""
+ "\"%@: Silent burn recovery can be perfomed for missing circle state\""
+ "\"%@: silent repair with state machine completed with result: %{BOOL}d error: %@\""
+ "\"%s: Attempting to add local secret info for empty, non-nil string\""
+ "\"%s: Attempting to set passphrase key with empty, non-nil string\""
+ "\"%s: Attempting to set recovery secret key with empty, non-nil string\""
+ "\"%s: useSecureBackupCachedSecret=%{BOOL}d, circleJoinResult=%@\""
+ "\"Account preflight failed - Primary account DSID (%{mask.hash}@) does not match the DSID specified in the context (%{mask.hash}@)\""
+ "\"Adding non-viable throttle header in silent burn in mini-buddy flow\""
+ "\"CDPDLocalSecretController: updated context with context type: %ld, appleID: %{mask.hash}@, dsid: %{mask.hash}@, adsid: %{mask.hash}@\""
+ "\"Creating recovery option: Choose Another Device\""
+ "\"Creating recovery option: Try Again\""
+ "\"Error while performing RPD: %@\""
+ "\"Errors that aren't the missing cached passphrase error don't get fallback logic.\""
+ "\"Even if the error is the missing cached passphrase error, we only add fallback logic with the feature flag turned on.\""
+ "\"Failed to enable with CDPContext local secret. Let's try again with SBD cached secret.\""
+ "\"Forcing _useSecureBackupCachedPassphrase=YES\""
+ "\"MUM: CDPDLocalSecretFollowUpProviderImpl init'ed with altDSID %{mask.hash}@\""
+ "\"Nested _authenticatedEnableSecureBackupWithContext failed with error: %@\""
+ "\"Non-conforming transport protocol passed to the telemetry system.  Likely build mismatch with AAAFoundation\""
+ "\"Retrying _authenticatedEnableSecureBackupWithContext by falling back to SBD cache.\""
+ "\"Setting _useSecureBackupCachedPassphrase=NO\""
+ "\"User elected to: Select Device\""
+ "\"User elected to: Try Again\""
+ "\"Will show RPD completed alert\""
+ "\"Within retry, _authenticatedEnableSecureBackupWithContext failed with error: %@\""
+ "\"Within retry, _authenticatedEnableSecureBackupWithContext succeeded.\""
+ "\"_authenticatedEnableSecureBackupIncludingFallbackWithContext failed with error: %@\""
+ "\"_authenticatedEnableSecureBackupIncludingFallbackWithContext succeeded\""
+ "\"_authenticatedEnableSecureBackupWithContext succeeded after falling back to SBD cached secret\""
+ "\"_refreshAndAuthenticateWithContext: context type: %ld, appleID: %{mask.hash}@, dsid: %{mask.hash}@, adsid: %{mask.hash}@\""
+ "\"_shouldForceUseSecureBackupCachedPassphrase: clientTypeIsBuddy=%{BOOL}d, hasSecret=%{BOOL}d\""
+ "\"cdp: Attempting to perform authenticated enable with context: %@, fallbackState=%ld\""
+ "\"deleteConfirmExistingSecretFollowUp: altDSID:%{mask.hash}@\""
+ "\"deleteLocalSecretChangeFollowUp: altDSID:%{mask.hash}@\""
+ "\"performEscrowRecoveryWithRecoveryContext: invoked with fallbackState=%ld\""
+ "\"postConfirmExistingSecretFollowUp: altDSID:%{mask.hash}@\""
+ "\"postLocalSecretChangeFollowUp: altDSID:%{mask.hash}@\""
+ "%@;%@"
+ "-[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:fallbackState:completion:]"
+ "-[CDPDSecureBackupController _recoveryInfoDictionaryFromContext:usePreviouslyCachedSecret:]"
+ "-[CDPDStateMachine _attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useSecureBackupCachedSecret:circleJoinResult:completion:]"
+ "-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]"
+ "@\"NSMutableArray\"16@0:8"
+ "@32@0:8q16@24"
+ "@40@0:8@16Q24^@32"
+ "AACustodianErrors"
+ "AACustodianRecoveryErrors"
+ "AAFAnalyticstRTCTransport"
+ "Adding event to queue: %@"
+ "B32@0:8@16Q24"
+ "CKKSResultOperationDescriptionError"
+ "DATA_RECOVERY_RESET_FAILED_MESSAGE"
+ "DATA_RECOVERY_RESET_FAILED_TITLE"
+ "DSIDForAccount:"
+ "Dispatching event to telemetry queue: %@"
+ "Enabling Opt-In collection for event: %@"
+ "Event added to the queue, current queue size: %lu"
+ "Event sequence map: %@"
+ "Fetching Analytics transport for key: %@"
+ "Fetching telemetry transport for event: %@"
+ "Flushed transport and sequence caches"
+ "Flushed transport caches"
+ "Flushing transport and sequence caches"
+ "Flushing transport caches"
+ "REMOTE_SECRET_ENTRY_FORGOT_CODE_DIALOG_CUSTODIAN_TRY_LATER"
+ "REMOTE_SECRET_ENTRY_FORGOT_CODE_DIALOG_MESSAGE_ANOTHER_DEVICE"
+ "REMOTE_SECRET_ENTRY_MULTIPLE_INCORRECT_BUTTON_CHOOSE_ANOTHER_DEVICE"
+ "Releasing analytics transaction upon timeout"
+ "Returning transport for key: %@ - %@"
+ "Session configuration required..."
+ "Session is configured... event queue size: %lu"
+ "Session is still being configured... queuing event: %@"
+ "Session state is (%lu), proceeding with send..."
+ "T@\"<CDPDSecureBackupEnableCapable>\",&,N,V_secureBackupEnableController"
+ "T@\"NSArray\",&,N,V_cdpDevices"
+ "T@\"NSMutableArray\",R,N"
+ "T@\"NSString\",?,R,C"
+ "Telemetry grace period timeout expired"
+ "[%@] [%@] DELIVERY BEGIN - %@"
+ "[%@] [%@] DELIVERY END"
+ "_attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useSecureBackupCachedSecret:circleJoinResult:completion:"
+ "_attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:"
+ "_authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:"
+ "_authenticatedEnableSecureBackupWithContext:fallbackState:completion:"
+ "_cdpDevices"
+ "_cdpStateMachineWithNilUIProvider"
+ "_checkSecureBackupCachedSecretValue"
+ "_cleanUpPostEscrowCreationStates"
+ "_deviceSelectionRecoveryOptionWithCompletion:"
+ "_entryLimitDeviceSelectionAvailableBodyForDevice:"
+ "_handleSecureBackupEnablementError:fallbackState:context:delegate:completion:"
+ "_performEscrowRecoveryWithRecoveryContext:fallbackState:error:"
+ "_recoverBackupDictionaryWithContext:fallbackState:error:"
+ "_recoveryFlowControllerForKeychainSyncSystem:recoveryContext:"
+ "_recoveryInfoDictionaryFromContext:usePreviouslyCachedSecret:"
+ "_sendEvent:"
+ "_shouldForceUseSecureBackupCachedPassphraseWithContext:clientType:"
+ "_shouldUseSBDCacheWithSecureBackupContext:fallbackState:"
+ "_tryAgainLaterOptionWithCompletion:"
+ "_updateEventWithDefaultMetadata:"
+ "cdpDevices"
+ "com.apple.MobileActivation.ErrorDomain"
+ "com.apple.appleaccount.inheritance.preflightCheckEvent"
+ "com.apple.authkit.baa.signing"
+ "com.apple.authkit.baa.signing.cached"
+ "com.apple.authkit.baa.signing.host"
+ "com.apple.security.acceptorCreatesPacket2"
+ "com.apple.security.acceptorCreatesPacket4"
+ "com.apple.security.acceptorCreatesPacket5"
+ "com.apple.security.acceptorCreatesVoucher"
+ "com.apple.security.acceptorFetchesInitialSyncData"
+ "com.apple.security.cKKSTLKFetch"
+ "com.apple.security.ckks.CKAccountLogin"
+ "com.apple.security.ckks.contentSyncFinish"
+ "com.apple.security.ckks.deviceLocked"
+ "com.apple.security.ckks.deviceUnlocked"
+ "com.apple.security.ckks.firstManateeKeyFetch"
+ "com.apple.security.ckks.healKeyHierarchy"
+ "com.apple.security.ckks.healKeyHierarchy.healBrokenRecords"
+ "com.apple.security.ckks.healKeyHierarchy.uploadHealedTLKShares"
+ "com.apple.security.ckks.healTLKShares"
+ "com.apple.security.ckks.healTLKShares.createMissingTLKShares"
+ "com.apple.security.ckks.healTLKShares.uploadMissingTLKShares"
+ "com.apple.security.ckks.launchStart"
+ "com.apple.security.ckks.localReset"
+ "com.apple.security.ckks.localSyncFinish"
+ "com.apple.security.ckks.processIncomingQueue"
+ "com.apple.security.ckks.processIncomingQueue.fixMismatchedViewItems"
+ "com.apple.security.ckks.processIncomingQueue.loadAndProcessIQEs"
+ "com.apple.security.ckks.processOutgoingQueue"
+ "com.apple.security.ckks.processOutgoingQueue.saveCKMirrorEntries"
+ "com.apple.security.ckks.processOutgoingQueue.uploadOQEstoCK"
+ "com.apple.security.ckks.processReceivedKeys"
+ "com.apple.security.ckks.scanLocalItems"
+ "com.apple.security.ckks.scanLocalItems.onboardMissingItems"
+ "com.apple.security.ckks.scanLocalItems.querySyncableItems"
+ "com.apple.security.ckks.syncingPolicySet"
+ "com.apple.security.ckks.trustGain"
+ "com.apple.security.ckks.trustLoss"
+ "com.apple.security.ckks.zoneChangeFetch"
+ "com.apple.security.ckks.zoneCreation"
+ "com.apple.security.cloudKitAccountAvailability"
+ "com.apple.security.createSOSApplication"
+ "com.apple.security.createSOSCircleBlob"
+ "com.apple.security.fetchAndPersistChanges"
+ "com.apple.security.fetchMachineID"
+ "com.apple.security.fetchPolicyDocument"
+ "com.apple.security.flush"
+ "com.apple.security.idMSSecurityLevel"
+ "com.apple.security.initaitorJoinSOS"
+ "com.apple.security.initiatorCreatesPacket1"
+ "com.apple.security.initiatorCreatesPacket3"
+ "com.apple.security.initiatorImportsInitialSyncData"
+ "com.apple.security.initiatorJoinsTrustSystems"
+ "com.apple.security.initiatorWaitsForUpgrade"
+ "com.apple.security.join"
+ "com.apple.security.kVSSyncAndWait"
+ "com.apple.security.octagon.state"
+ "com.apple.security.preApprovedJoin"
+ "com.apple.security.prepareIdentityInTPH"
+ "com.apple.security.primaryAccountAdded"
+ "com.apple.security.trustedDeviceListRefresh"
+ "com.apple.security.trustedpeers.RecoveryKeySetError"
+ "com.apple.security.updateTDL"
+ "com.apple.security.updateTrust"
+ "com.apple.security.validatedStashedAccountCredential"
+ "com.apple.security.verifySOSApplication"
+ "com.appple.ckks.state"
+ "configureReportingSessionWithCompletion:"
+ "configureSessionForEvent:sendEventBlock:telemetryQueue:"
+ "eventQueue"
+ "flushTransportCache"
+ "getAllowedADPEvents"
+ "getAllowedDNUEvents"
+ "getAllowedSecurityEvents"
+ "getApprovedEvents:"
+ "getApprovedEventsForADPAndDNU"
+ "indicatesRecoveryCanBeRetried"
+ "isEventPrivacyApproved:"
+ "isLocalSecretCached"
+ "isMissingCachedPassphraseError"
+ "isSilentBurnCDPRepairEnabled"
+ "isSilentBurnInMiniBuddyEnabled"
+ "secureBackupEnableController"
+ "sessionGracePeriod"
+ "sessionState"
+ "setCdpDevices:"
+ "setSecureBackupEnableController:"
+ "setSessionGracePeriod:"
+ "setSessionState:"
+ "setWithSet:"
+ "unionSet:"
+ "useCDPContextSecretInsteadOfSBDSecretFeatureEnabled"
+ "v16@?0@\"AAFAnalyticsEvent\"8"
+ "v32@?0@\"AAFAnalyticsEvent\"8Q16^B24"
+ "v40@0:8@16@?24@32"
- "\x14"
- "\"%@: Cannot determine escrow record for unknown account with altDSID (%@)\""
- "\"%@: Cannot determine escrow record state for device not in circle (%lu) with error (%@)\""
- "\"Account preflight failed - Primary account DSID (%@) does not match the DSID specified in the context (%@)\""
- "\"CDPDLocalSecretController: updated context with context type: %ld, appleID: %@, dsid: %@, adsid: %@\""
- "\"Dispatching event to telemetry queue: %@\""
- "\"Enabling Opt-In collection for event: %@\""
- "\"Event sequence map: %@\""
- "\"Fetching Analytics transport for key: %@\""
- "\"Fetching telemetry transport for event: %@\""
- "\"Forcing _useSecureBackupCachedPassphrase=YES for iOS/watchOS Buddy on a device with a local secret present\""
- "\"MUM: CDPDLocalSecretFollowUpProviderImpl init'ed with altDSID %@\""
- "\"Returning transport for key: %@ - %@\""
- "\"User does not have W enabled, signaling completion\""
- "\"User has W enabled, will show RPD completed alert\""
- "\"[%@] [%@] DELIVERY BEGIN - %@\""
- "\"[%@] [%@] DELIVERY END - %@\""
- "\"_authenticatedEnableSecureBackupWithContext succeeded.\""
- "\"_refreshAndAuthenticateWithContext: context type: %ld, appleID: %@, dsid: %@\""
- "\"cdp: Attempting to perform authenticated enable with context: %@\""
- "\"deleteConfirmExistingSecretFollowUp: altDSID:%@\""
- "\"deleteLocalSecretChangeFollowUp: altDSID:%@\""
- "\"performEscrowRecoveryWithRecoveryContext: invoked\""
- "\"postConfirmExistingSecretFollowUp: altDSID:%@\""
- "\"postLocalSecretChangeFollowUp: altDSID:%@\""
- "-[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:completion:]"
- "RECOVERY_KEY_CUSTODIAN_RECOVERY_HELP_PROMPT_MESSAGE"
- "TB,N,V_shouldSendAnalyticsData"
- "_attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useCachedSecret:circleJoinResult:completion:"
- "_attemptBackupRecoveryWithLocalSecret:type:useCachedSecret:circleJoinResult:completion:"
- "_authenticatedEnableSecureBackupWithContext:completion:"
- "_entryLimitRecoveryKeyAndCustodianRecoveryAvailableBodyForDevice:"
- "_handleSecureBackupEnablementError:context:delegate:completion:"
- "_hardLimitUserInfoForDevice:"
- "_recoverBackupDictionaryWithContext:error:"
- "_recoveryInfoDictionaryFromContext:"
- "_resetEscrowMissingPromptDebounceCount"
- "_shouldSendAnalyticsData"
- "cachedPassphraseMissing"
- "getAllowedEvents"
- "setShouldSendAnalyticsData:"
- "shouldSendAnalyticsData"

```
