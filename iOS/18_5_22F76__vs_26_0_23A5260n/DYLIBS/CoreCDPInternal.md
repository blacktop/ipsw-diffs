## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-386.458.1.0.0
-  __TEXT.__text: 0x8e8d8
-  __TEXT.__auth_stubs: 0x10f0
-  __TEXT.__objc_methlist: 0x537c
-  __TEXT.__const: 0x734
-  __TEXT.__oslogstring: 0x135a8
-  __TEXT.__cstring: 0x8905
-  __TEXT.__gcc_except_tab: 0xba4
+404.0.0.0.0
+  __TEXT.__text: 0x90b5c
+  __TEXT.__auth_stubs: 0x1100
+  __TEXT.__objc_methlist: 0x54e4
+  __TEXT.__const: 0x8c4
+  __TEXT.__oslogstring: 0x14036
+  __TEXT.__cstring: 0x8c9e
+  __TEXT.__gcc_except_tab: 0xc78
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x341
-  __TEXT.__swift5_fieldmd: 0x80
+  __TEXT.__swift5_fieldmd: 0x98
   __TEXT.__constg_swiftt: 0x1d0
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x6e
+  __TEXT.__swift5_reflstr: 0x81
   __TEXT.__swift5_assocty: 0xa8
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x44

   __TEXT.__swift5_capture: 0x1b8
   __TEXT.__swift_as_entry: 0x5c
   __TEXT.__swift_as_ret: 0x60
-  __TEXT.__unwind_info: 0x1cb8
-  __TEXT.__eh_frame: 0x9a0
-  __TEXT.__objc_classname: 0xc79
-  __TEXT.__objc_methname: 0xeb97
-  __TEXT.__objc_methtype: 0x28e1
-  __TEXT.__objc_stubs: 0xbec0
-  __DATA_CONST.__got: 0xff0
-  __DATA_CONST.__const: 0x24e0
-  __DATA_CONST.__objc_classlist: 0x280
+  __TEXT.__unwind_info: 0x1d40
+  __TEXT.__eh_frame: 0x8d0
+  __TEXT.__objc_classname: 0xcbd
+  __TEXT.__objc_methname: 0xf1be
+  __TEXT.__objc_methtype: 0x2987
+  __TEXT.__objc_stubs: 0xc3e0
+  __DATA_CONST.__got: 0x1030
+  __DATA_CONST.__const: 0x2650
+  __DATA_CONST.__objc_classlist: 0x288
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x168
+  __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35c8
-  __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x160
+  __DATA_CONST.__objc_selrefs: 0x3738
+  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x888
-  __AUTH_CONST.__const: 0xaf8
-  __AUTH_CONST.__cfstring: 0x59a0
-  __AUTH_CONST.__objc_const: 0xfb30
+  __AUTH_CONST.__auth_got: 0x890
+  __AUTH_CONST.__const: 0xb60
+  __AUTH_CONST.__cfstring: 0x5bc0
+  __AUTH_CONST.__objc_const: 0xfc90
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0x1050
+  __AUTH.__objc_data: 0xfd8
   __AUTH.__data: 0x58
-  __DATA.__objc_ivar: 0x3a0
-  __DATA.__data: 0x12a8
-  __DATA.__bss: 0x8a0
-  __DATA_DIRTY.__objc_data: 0x970
-  __DATA_DIRTY.__data: 0x68
+  __DATA.__objc_ivar: 0x3b0
+  __DATA.__data: 0x1198
+  __DATA.__bss: 0x8c0
+  __DATA_DIRTY.__objc_data: 0xa38
+  __DATA_DIRTY.__data: 0x78
   __DATA_DIRTY.__bss: 0x138
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: DF4350B6-6C96-365E-A566-276E21F167EE
-  Functions: 3036
-  Symbols:   9865
-  CStrings:  5495
+  UUID: C6592813-04A2-325D-AF0F-82EEB6AC0078
+  Functions: 3097
+  Symbols:   10019
+  CStrings:  5636
 
Symbols:
+ +[CDPDAnalyticsTransport getAllowedAccountAccessEvents]
+ +[CDPDAnalyticsTransport getAllowedAccountAccessEvents].cold.1
+ +[CDPDAnalyticsTransport getApprovedEventsForAll]
+ -[CDPADPRegionAvailabilityProvider .cxx_destruct]
+ -[CDPADPRegionAvailabilityProvider initWithWalrusConfigProvider:]
+ -[CDPADPRegionAvailabilityProvider isWalrusEnabledForPrimaryAccountWithCompletionHandler:]
+ -[CDPDAnalyticsTransport _enforceIdentifiableDataPrivacyComplianceOnEvent:manager:]
+ -[CDPDAnalyticsTransport _enforceIdentifiableDataPrivacyComplianceOnEvent:manager:].cold.1
+ -[CDPDAnalyticsTransport _enforceIdentifiableDataPrivacyComplianceOnEvent:manager:].cold.2
+ -[CDPDAnalyticsTransport _isEventPrivacyApprovedIdentifiable:]
+ -[CDPDAnalyticsTransport _replaceClientNameWithEvent:]
+ -[CDPDClientHandler anyRecoveryKeysAreOctagonDistrustedWithContext:completion:]
+ -[CDPDClientHandler anyRecoveryKeysAreOctagonDistrustedWithContext:completion:].cold.1
+ -[CDPDClientHandler escrowCheckForContext:isBackground:completion:]
+ -[CDPDClientHandler escrowCheckForContext:isBackground:completion:].cold.1
+ -[CDPDClientHandler localSecretChangedTo:secretType:context:uiProvider:completion:].cold.2
+ -[CDPDEscrowRecordController _deviceCircleStatusUsingCache:completion:]
+ -[CDPDEscrowRecordController _hasLocalSecret]
+ -[CDPDEscrowRecordController _reauthenticateAndPerformEscrowCheckWithIsBackground:completion:]
+ -[CDPDEscrowRecordController _reauthenticateAndPerformEscrowCheckWithIsBackground:completion:].cold.1
+ -[CDPDEscrowRecordController escrowCheckWithIsBackground:completion:]
+ -[CDPDFollowUpFactory _anyRecoveryKeysAreDistrusted]
+ -[CDPDFollowUpFactory _anyRecoveryKeysAreDistrusted].cold.1
+ -[CDPDFollowUpFactory _approvedCustodianCountForAltDSID:]
+ -[CDPDKeychainSync isUserVisibleKeychainSyncEnabled].cold.3
+ -[CDPDKeychainSync isUserVisibleKeychainSyncEnabled].cold.4
+ -[CDPDKeychainSync isUserVisibleKeychainSyncEnabled].cold.5
+ -[CDPDKeychainSync isUserVisibleKeychainSyncEnabled].cold.6
+ -[CDPDOctagonTrustProxyImpl _cdpEscrowRecordViabilityStateFromRepairReason:]
+ -[CDPDOctagonTrustProxyImpl escrowCheckWithIsBackground:completion:]
+ -[CDPDRecoveryKeyController anyRecoveryKeysAreOctagonDistrustedWithError:]
+ -[CDPDRecoveryKeyController anyRecoveryKeysAreOctagonDistrustedWithError:].cold.1
+ -[CDPDRecoveryKeyController anyRecoveryKeysAreOctagonDistrustedWithError:].cold.2
+ -[CDPDRecoveryKeyController anyRecoveryKeysAreOctagonDistrustedWithError:].cold.3
+ -[CDPDRecoveryValidatedJoinFlowController _isSingleICSC:]
+ -[CDPDRecoveryValidatedJoinFlowController shouldOfferPiggybackingBasedRecovery:]
+ -[CDPDRecoveryValidatedJoinFlowController shouldOfferPiggybackingBasedRecovery:].cold.1
+ -[CDPDSecureChannelController _startListeningWithProxy:completion:]
+ -[CDPDSecureChannelController _startListeningWithProxy:completion:].cold.1
+ -[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:completion:]
+ -[CDPDSecureChannelController startCircleApplicationApprovalServerWithContext:serverStarted:completion:]
+ -[CDPInternalWalrusStateController _reportWalrusRepairFinishEventWithCombinedWalrusStatus:error:]
+ -[CDPInternalWalrusStateController _reportWalrusRepairStartEventWithCombinedWalrusStatus:]
+ -[CDPInternalWalrusStateController initWithAccount:cdpdAccount:securityProxy:pcsProxy:accountStore:sbProxy:]
+ -[CDPInternalWalrusStateController initWithAccount:cdpdAccount:securityProxy:pcsProxy:sbProxy:]
+ GCC_except_table100
+ GCC_except_table30
+ GCC_except_table48
+ _OBJC_CLASS_$_CDPADPRegionAvailabilityProvider
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$_OTEscrowCheckCallResult
+ _OBJC_IVAR_$_CDPADPRegionAvailabilityProvider._configProvider
+ _OBJC_IVAR_$_CDPDClientHandler._proxService
+ _OBJC_IVAR_$_CDPInternalWalrusStateController._context
+ _OBJC_IVAR_$_CDPInternalWalrusStateController._sbProxy
+ _OBJC_METACLASS_$_CDPADPRegionAvailabilityProvider
+ __OBJC_$_INSTANCE_METHODS_CDPADPRegionAvailabilityProvider
+ __OBJC_$_INSTANCE_VARIABLES_CDPADPRegionAvailabilityProvider
+ __OBJC_$_PROP_LIST_CDPProximityPairingServiceProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CDPProximityPairingServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CDPProximityPairingServiceProtocol
+ __OBJC_CLASS_RO_$_CDPADPRegionAvailabilityProvider
+ __OBJC_LABEL_PROTOCOL_$_CDPProximityPairingServiceProtocol
+ __OBJC_METACLASS_RO_$_CDPADPRegionAvailabilityProvider
+ __OBJC_PROTOCOL_$_CDPProximityPairingServiceProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_CDPProximityPairingServiceProtocol
+ ___102-[CDPDSecureBackupController _authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:]_block_invoke.117
+ ___102-[CDPDSecureBackupController _authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:]_block_invoke.117.cold.1
+ ___102-[CDPDSecureBackupController _authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:]_block_invoke.117.cold.2
+ ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.62
+ ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.62.cold.1
+ ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.63
+ ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.64
+ ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.64.cold.1
+ ___104-[CDPDSecureChannelController startCircleApplicationApprovalServerWithContext:serverStarted:completion:]_block_invoke
+ ___108-[CDPDRecoveryValidatedJoinFlowController _escapeOfferForDevices:remoteApproval:forMultipleICSC:completion:]_block_invoke
+ ___113-[CDPInternalWalrusStateController _updateWalrusStateAndPerformPostEnablementActions:context:account:completion:]_block_invoke.85
+ ___113-[CDPInternalWalrusStateController _updateWalrusStateAndPerformPostEnablementActions:context:account:completion:]_block_invoke.85.cold.1
+ ___113-[CDPInternalWalrusStateController _updateWalrusStateAndPerformPostEnablementActions:context:account:completion:]_block_invoke.87
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.153
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.153.cold.1
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.153.cold.2
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.153.cold.3
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.154
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.154.cold.1
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.154.cold.2
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.154.cold.3
+ ___119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.190
+ ___119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.191
+ ___119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.192
+ ___156-[CDPDStateMachine _attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.193
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1045
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1045.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1045.cold.2
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.981
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.981.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.982
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.982.cold.1
+ ___38-[CDPDStateMachine _attemptCDPEnable:]_block_invoke.136
+ ___49+[CDPDAnalyticsTransport getApprovedEventsForAll]_block_invoke
+ ___55+[CDPDAnalyticsTransport getAllowedAccountAccessEvents]_block_invoke
+ ___55-[CDPDSecureBackupController checkForAnyOctagonRecord:]_block_invoke.90
+ ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.128
+ ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.132
+ ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.132.cold.1
+ ___57-[CDPDRecoveryValidatedJoinFlowController _isSingleICSC:]_block_invoke
+ ___58-[CDPDStateMachine _handleBeneficiaryTrustWithCompletion:]_block_invoke.113
+ ___61-[CDPDStateMachine _promptForEDPRecoveryTokenWithCompletion:]_block_invoke.62
+ ___61-[CDPDStateMachine _promptForEDPRecoveryTokenWithCompletion:]_block_invoke.67
+ ___63-[CDPDSecureBackupController disableRecoveryKeyWithCompletion:]_block_invoke.159
+ ___65-[CDPDClientHandler attemptToEscrowPreRecord:context:completion:]_block_invoke.94
+ ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.133
+ ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.134
+ ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.123.cold.1
+ ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.124
+ ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.125
+ ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.126
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.103
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.103.cold.1
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.77
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.82
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.89
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.91
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.95
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke_2.96
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke_2.96.cold.1
+ ___65-[CDPDStateMachine repairCloudDataProtectionStateWithCompletion:]_block_invoke.171
+ ___65-[CDPDStateMachine repairCloudDataProtectionStateWithCompletion:]_block_invoke.171.cold.1
+ ___65-[CDPDStateMachine repairCloudDataProtectionStateWithCompletion:]_block_invoke.171.cold.2
+ ___65-[CDPDStateMachine repairCloudDataProtectionStateWithCompletion:]_block_invoke.172
+ ___65-[CDPDStateMachine repairCloudDataProtectionStateWithCompletion:]_block_invoke.173
+ ___66-[CDPDStateMachine _handleCloudDataProtectionStateWithCompletion:]_block_invoke.110
+ ___66-[CDPDStateMachine _handleCloudDataProtectionStateWithCompletion:]_block_invoke.111
+ ___67-[CDPDClientHandler escrowCheckForContext:isBackground:completion:]_block_invoke
+ ___67-[CDPDSecureBackupController deleteAllBackupRecordsWithCompletion:]_block_invoke.156
+ ___67-[CDPDSecureBackupController deleteSingleICSCBackupWithCompletion:]_block_invoke.157
+ ___67-[CDPDSecureChannelController _startListeningWithProxy:completion:]_block_invoke
+ ___68-[CDPDOctagonTrustProxyImpl escrowCheckWithIsBackground:completion:]_block_invoke
+ ___68-[CDPDOctagonTrustProxyImpl escrowCheckWithIsBackground:completion:]_block_invoke.50
+ ___68-[CDPDOctagonTrustProxyImpl escrowCheckWithIsBackground:completion:]_block_invoke.cold.1
+ ___68-[CDPDOctagonTrustProxyImpl escrowCheckWithIsBackground:completion:]_block_invoke.cold.2
+ ___68-[CDPDOctagonTrustProxyImpl escrowCheckWithIsBackground:completion:]_block_invoke_2
+ ___69-[CDPDEscrowRecordController escrowCheckWithIsBackground:completion:]_block_invoke
+ ___70-[CDPDCircleController _joinCircleIgnoringBackups:context:completion:]_block_invoke.52
+ ___70-[CDPDCircleController _joinCircleIgnoringBackups:context:completion:]_block_invoke.53
+ ___70-[CDPDCircleController _joinCircleIgnoringBackups:context:completion:]_block_invoke.53.cold.1
+ ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.201
+ ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.202
+ ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.202.cold.1
+ ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.203
+ ___72-[CDPDStateMachine _recoverSecureBackupWithCircleJoinResult:completion:]_block_invoke.179
+ ___73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.66
+ ___73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.66.cold.1
+ ___73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.66.cold.2
+ ___73-[CDPDClientHandler shouldPerformRepairForContext:forceFetch:completion:]_block_invoke.91
+ ___74-[CDPDSecureBackupController checkForExistingRecordWithPeerId:completion:]_block_invoke.93
+ ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.198
+ ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.198.cold.1
+ ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.199
+ ___75-[CDPDSecureBackupController enableSecureBackupWithRecoveryKey:completion:]_block_invoke.114
+ ___75-[CDPDTermsInfoBackupController fetchTermsAcceptanceForAccount:completion:]_block_invoke_2
+ ___75-[CDPDTermsInfoBackupController fetchTermsAcceptanceForAccount:completion:]_block_invoke_2.cold.1
+ ___76-[CDPDEscrowRecordController _deviceEscrowRecordStateUsingCache:completion:]_block_invoke.80
+ ___76-[CDPDEscrowRecordController _deviceEscrowRecordStateUsingCache:completion:]_block_invoke.80.cold.1
+ ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.109
+ ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.109.cold.1
+ ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.109.cold.2
+ ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.109.cold.3
+ ___77-[CDPDEscrowRecordController _performSilentEscrowRecordRepairWithCompletion:]_block_invoke.70
+ ___79-[CDPDCircleController _joinCircleFallbackWithResult:ignoreBackups:completion:]_block_invoke.56
+ ___79-[CDPDCircleController _requestCircleJoinWithObserver:requestBlock:completion:]_block_invoke.66
+ ___79-[CDPDClientHandler fetchEscrowRecordDevicesWithContext:usingCache:completion:]_block_invoke.53
+ ___79-[CDPInternalWalrusStateController setWalrusStatusEnabled:password:completion:]_block_invoke.78
+ ___79-[CDPInternalWalrusStateController setWalrusStatusEnabled:password:completion:]_block_invoke.78.cold.1
+ ___79-[CDPInternalWalrusStateController setWalrusStatusEnabled:password:completion:]_block_invoke.79
+ ___80-[CDPDClientHandler startCircleApplicationApprovalServerWithContext:completion:]_block_invoke.83
+ ___80-[CDPDClientHandler startCircleApplicationApprovalServerWithContext:completion:]_block_invoke_2.84
+ ___80-[CDPDRecoveryValidatedJoinFlowController shouldOfferPiggybackingBasedRecovery:]_block_invoke
+ ___80-[CDPDRecoveryValidatedJoinFlowController shouldOfferPiggybackingBasedRecovery:]_block_invoke.cold.1
+ ___80-[CDPDStateMachine _continueShouldPerformRepairWithOptionForceFetch:completion:]_block_invoke.160
+ ___80-[CDPDStateMachine _continueShouldPerformRepairWithOptionForceFetch:completion:]_block_invoke.161
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.1046
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.1048
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.1048.cold.1
+ ___82-[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:completion:]_block_invoke
+ ___82-[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:completion:]_block_invoke.84
+ ___82-[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:completion:]_block_invoke.86
+ ___82-[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:completion:]_block_invoke.cold.1
+ ___82-[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:completion:]_block_invoke.cold.2
+ ___82-[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:completion:]_block_invoke_2
+ ___82-[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:completion:]_block_invoke_2.cold.1
+ ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.180
+ ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.180.cold.1
+ ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.182
+ ___83-[CDPDClientHandler localSecretChangedTo:secretType:context:uiProvider:completion:]_block_invoke.95
+ ___84-[CDPDEscrowRecordController _continueSilentEscrowRecordRepairWithState:completion:]_block_invoke.87
+ ___84-[CDPDEscrowRecordController _continueSilentEscrowRecordRepairWithState:completion:]_block_invoke.87.cold.1
+ ___85-[CDPDClientHandler _startObservingConnectionStateForRepairWithStateMachine:context:]_block_invoke.86
+ ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.96
+ ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.96.cold.1
+ ___85-[CDPDClientHandler handleCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.69
+ ___85-[CDPDClientHandler repairCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.72
+ ___85-[CDPDRecoveryValidatedJoinFlowController _accountResetRecoveryOptionWithCompletion:]_block_invoke.74
+ ___85-[CDPDStateMachine _attemptBeneficiaryTrustWithInheritanceKey:retryCount:completion:]_block_invoke.122
+ ___86-[CDPDClientHandler shouldPerformAuthenticatedRepairForContext:forceFetch:completion:]_block_invoke.92
+ ___86-[CDPDRecoveryValidatedJoinFlowController _handleNoRecoveryFactorsWithMask:validator:]_block_invoke.243
+ ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.97
+ ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.97.cold.1
+ ___90-[CDPADPRegionAvailabilityProvider isWalrusEnabledForPrimaryAccountWithCompletionHandler:]_block_invoke
+ ___90-[CDPADPRegionAvailabilityProvider isWalrusEnabledForPrimaryAccountWithCompletionHandler:]_block_invoke.16
+ ___90-[CDPADPRegionAvailabilityProvider isWalrusEnabledForPrimaryAccountWithCompletionHandler:]_block_invoke.cold.1
+ ___90-[CDPADPRegionAvailabilityProvider isWalrusEnabledForPrimaryAccountWithCompletionHandler:]_block_invoke.cold.2
+ ___90-[CDPADPRegionAvailabilityProvider isWalrusEnabledForPrimaryAccountWithCompletionHandler:]_block_invoke.cold.3
+ ___90-[CDPDEscrowRecordController _shouldPerformSilentEscrowRecordRepairUsingCache:completion:]_block_invoke_2
+ ___91-[CDPDStateMachine _isEligibleForRecoveryTokenWithContext:cdpStateMachineError:completion:]_block_invoke.46
+ ___92-[CDPDSecureBackupController checkForExistingRecordMatchingPredicate:forceFetch:completion:]_block_invoke.95
+ ___92-[CDPDSecureBackupController checkForExistingRecordMatchingPredicate:forceFetch:completion:]_block_invoke.95.cold.1
+ ___93-[CDPDSecureBackupController upgradeICSCRecordsThenEnableSecureBackupWithContext:completion:]_block_invoke.88
+ ___93-[CDPDSecureBackupController upgradeICSCRecordsThenEnableSecureBackupWithContext:completion:]_block_invoke.88.cold.1
+ ___93-[CDPDSecureBackupController upgradeICSCRecordsThenEnableSecureBackupWithContext:completion:]_block_invoke_2.86
+ ___93-[CDPDSecureBackupController upgradeICSCRecordsThenEnableSecureBackupWithContext:completion:]_block_invoke_2.86.cold.1
+ ___93-[CDPDSecureBackupController upgradeICSCRecordsThenEnableSecureBackupWithContext:completion:]_block_invoke_2.86.cold.2
+ ___94-[CDPDEscrowRecordController _reauthenticateAndPerformEscrowCheckWithIsBackground:completion:]_block_invoke
+ ___98-[CDPDSecureBackupController _getOctagonEscrowBackupRecordDevicesWithOptionForceFetch:completion:]_block_invoke.60
+ ___98-[CDPDSecureBackupController _getOctagonEscrowBackupRecordDevicesWithOptionForceFetch:completion:]_block_invoke.60.cold.1
+ ___98-[CDPDSecureBackupController _getOctagonEscrowBackupRecordDevicesWithOptionForceFetch:completion:]_block_invoke.61
+ ___block_descriptor_40_e8_32bs_e36_v24?0"AKWalrusConfig"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32bs40r_e8_v12?0B8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_49_e8_32s40bs_e20_v24?0Q8"NSError"16ls32l8s40l8
+ ___block_descriptor_50_e8_32s40bs_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_57_e8_32s40r48r_e50_v16?0?<v?"OTEscrowCheckCallResult""NSError">8lr40l8s32l8r48l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e45_v24?0"OTEscrowCheckCallResult"8"NSError"16lr48l8s32l8r56l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e23_v24?0B8B12"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e24_v32?0"NSData"8^16^24ls32l8s40l8s64l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e34_v24?0"NSDictionary"8"NSError"16ls32l8r80l8s40l8s48l8s72l8s56l8s64l8
+ ___block_literal_global.105
+ ___block_literal_global.1050
+ ___block_literal_global.170
+ ___block_literal_global.48
+ ___block_literal_global.490
+ ___block_literal_global.50
+ ___block_literal_global.72
+ ___block_literal_global.789
+ ___block_literal_global.79
+ ___block_literal_global.800
+ ___block_literal_global.802
+ ___block_literal_global.903
+ ___block_literal_global.93
+ ___block_literal_global.950
+ ___block_literal_global.962
+ ___block_literal_global.978
+ ___swift_memcpy1_1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_CoreCDPInternal
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_CoreCDPInternal
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_CoreCDPInternal
+ _getAllowedADPEvents.approvedADPEvents
+ _getAllowedAccountAccessEvents.approvedAccountAccessEvents
+ _getAllowedAccountAccessEvents.onceToken
+ _getAllowedDNUEvents.approvedDNUEvents
+ _getApprovedEventsForAll.approvedEvents
+ _getApprovedEventsForAll.onceToken
+ _kAAAPendingCFUTypes
+ _kCDPAnalyticsEscrowWalrusStatus
+ _kCDPAnalyticsOctagonWalrusStatus
+ _kCDPAnalyticsPCSWalrusStatus
+ _kCDPAnalyticsWalrusRepairFinishEvent
+ _kCDPAnalyticsWalrusRepairStartEvent
+ _objc_msgSend$_anyRecoveryKeysAreDistrusted
+ _objc_msgSend$_approvedCustodianCountForAltDSID:
+ _objc_msgSend$_cdpEscrowRecordViabilityStateFromRepairReason:
+ _objc_msgSend$_deviceCircleStatusUsingCache:completion:
+ _objc_msgSend$_enforceIdentifiableDataPrivacyComplianceOnEvent:manager:
+ _objc_msgSend$_hasLocalSecret
+ _objc_msgSend$_isEventPrivacyApprovedIdentifiable:
+ _objc_msgSend$_isSingleICSC:
+ _objc_msgSend$_reauthenticateAndPerformEscrowCheckWithIsBackground:completion:
+ _objc_msgSend$_replaceClientNameWithEvent:
+ _objc_msgSend$_reportWalrusRepairFinishEventWithCombinedWalrusStatus:error:
+ _objc_msgSend$_reportWalrusRepairStartEventWithCombinedWalrusStatus:
+ _objc_msgSend$_startListeningWithProxy:completion:
+ _objc_msgSend$_startListeningWithProxyWithEnforcedQoS:completion:
+ _objc_msgSend$anyRecoveryKeysAreOctagonDistrustedWithError:
+ _objc_msgSend$areRecoveryKeysDistrusted:error:
+ _objc_msgSend$escrowCheck:isBackgroundCheck:error:
+ _objc_msgSend$escrowCheckWithIsBackground:completion:
+ _objc_msgSend$escrowWalrusStatus
+ _objc_msgSend$featureStatus
+ _objc_msgSend$getAllowedAccountAccessEvents
+ _objc_msgSend$getApprovedEventsForAll
+ _objc_msgSend$getWalrusConfigWithCompletion:
+ _objc_msgSend$initWithAccount:cdpdAccount:securityProxy:pcsProxy:accountStore:sbProxy:
+ _objc_msgSend$initWithAccount:cdpdAccount:securityProxy:pcsProxy:sbProxy:
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$initWithServiceName:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$invalidate
+ _objc_msgSend$isMainThread
+ _objc_msgSend$isRecoverableError
+ _objc_msgSend$isSEPBasedICSCHealingEnabled
+ _objc_msgSend$needsReenroll
+ _objc_msgSend$octagonTrusted
+ _objc_msgSend$octagonWalrusStatus
+ _objc_msgSend$pcsWalrusStatus
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$repairReason
+ _objc_msgSend$secureTermsNeeded
+ _objc_msgSend$setOnProxCompletion:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$shouldOfferPiggybackingBasedRecovery:
+ _objc_msgSend$sosCircleProxy
+ _objc_msgSend$sosCompatibilityEnabled
+ _objc_msgSend$startCircleApplicationApprovalServerWithContext:serverStarted:
+ _objc_msgSend$telemetryDeviceSessionIDForAccount:
+ _objc_msgSend$viewMemberForAllUserFacingViews:
+ _objc_retain_x6
+ _swift_setDeallocating
- -[CDPDRecoveryValidatedJoinFlowController shouldOfferPiggybackingBasedRecovery]
- -[CDPDRecoveryValidatedJoinFlowController shouldOfferPiggybackingBasedRecovery].cold.1
- -[CDPDSecureChannelController _startListeningWithProxy:]
- -[CDPDSecureChannelController _startListeningWithProxy:].cold.1
- -[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:]
- -[CDPDSecureChannelController startCircleApplicationApprovalServerWithContext:completion:]
- -[CDPInternalWalrusStateController initWithAccount:cdpdAccount:securityProxy:pcsProxy:]
- -[CDPInternalWalrusStateController initWithAccount:cdpdAccount:securityProxy:pcsProxy:accountStore:]
- GCC_except_table28
- GCC_except_table41
- ___102-[CDPDSecureBackupController _authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:]_block_invoke.114
- ___102-[CDPDSecureBackupController _authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:]_block_invoke.114.cold.1
- ___102-[CDPDSecureBackupController _authenticatedEnableSecureBackupIncludingFallbackWithContext:completion:]_block_invoke.114.cold.2
- ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.59
- ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.59.cold.1
- ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.60
- ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.61
- ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.61.cold.1
- ___113-[CDPInternalWalrusStateController _updateWalrusStateAndPerformPostEnablementActions:context:account:completion:]_block_invoke.79
- ___113-[CDPInternalWalrusStateController _updateWalrusStateAndPerformPostEnablementActions:context:account:completion:]_block_invoke.79.cold.1
- ___113-[CDPInternalWalrusStateController _updateWalrusStateAndPerformPostEnablementActions:context:account:completion:]_block_invoke.81
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.150
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.150.cold.1
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.150.cold.2
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.150.cold.3
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.151
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.151.cold.1
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.151.cold.2
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.151.cold.3
- ___119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.187
- ___119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.188
- ___119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.189
- ___156-[CDPDStateMachine _attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.190
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.928
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.928.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.929
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.929.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.992
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.992.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.992.cold.2
- ___38-[CDPDStateMachine _attemptCDPEnable:]_block_invoke.133
- ___55-[CDPDSecureBackupController checkForAnyOctagonRecord:]_block_invoke.87
- ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.125
- ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.126
- ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.129.cold.1
- ___56-[CDPDSecureChannelController _startListeningWithProxy:]_block_invoke
- ___58-[CDPDStateMachine _handleBeneficiaryTrustWithCompletion:]_block_invoke.110
- ___61-[CDPDStateMachine _promptForEDPRecoveryTokenWithCompletion:]_block_invoke.58
- ___61-[CDPDStateMachine _promptForEDPRecoveryTokenWithCompletion:]_block_invoke.59
- ___63-[CDPDSecureBackupController disableRecoveryKeyWithCompletion:]_block_invoke.156
- ___65-[CDPDClientHandler attemptToEscrowPreRecord:context:completion:]_block_invoke.75
- ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.130
- ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.131
- ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.120
- ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.120.cold.1
- ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.121
- ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.122
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.100
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.100.cold.1
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.71
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.79
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.86
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.88
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.92
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke_2.93
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke_2.93.cold.1
- ___65-[CDPDStateMachine repairCloudDataProtectionStateWithCompletion:]_block_invoke.168
- ___65-[CDPDStateMachine repairCloudDataProtectionStateWithCompletion:]_block_invoke.168.cold.1
- ___65-[CDPDStateMachine repairCloudDataProtectionStateWithCompletion:]_block_invoke.168.cold.2
- ___65-[CDPDStateMachine repairCloudDataProtectionStateWithCompletion:]_block_invoke.169
- ___65-[CDPDStateMachine repairCloudDataProtectionStateWithCompletion:]_block_invoke.170
- ___66-[CDPDStateMachine _handleCloudDataProtectionStateWithCompletion:]_block_invoke.107
- ___66-[CDPDStateMachine _handleCloudDataProtectionStateWithCompletion:]_block_invoke.108
- ___67-[CDPDSecureBackupController deleteAllBackupRecordsWithCompletion:]_block_invoke.153
- ___67-[CDPDSecureBackupController deleteSingleICSCBackupWithCompletion:]_block_invoke.154
- ___70-[CDPDCircleController _joinCircleIgnoringBackups:context:completion:]_block_invoke.49
- ___70-[CDPDCircleController _joinCircleIgnoringBackups:context:completion:]_block_invoke.50
- ___70-[CDPDCircleController _joinCircleIgnoringBackups:context:completion:]_block_invoke.50.cold.1
- ___71-[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:]_block_invoke
- ___71-[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:]_block_invoke.84
- ___71-[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:]_block_invoke.86
- ___71-[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:]_block_invoke.cold.1
- ___71-[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:]_block_invoke.cold.2
- ___71-[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:]_block_invoke_2
- ___71-[CDPDSecureChannelController _startListeningWithProxyWithEnforcedQoS:]_block_invoke_2.cold.1
- ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.198
- ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.199
- ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.199.cold.1
- ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.200
- ___72-[CDPDStateMachine _recoverSecureBackupWithCircleJoinResult:completion:]_block_invoke.176
- ___73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.57
- ___73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.57.cold.1
- ___73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.57.cold.2
- ___73-[CDPDClientHandler shouldPerformRepairForContext:forceFetch:completion:]_block_invoke.72
- ___74-[CDPDSecureBackupController checkForExistingRecordWithPeerId:completion:]_block_invoke.90
- ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.195
- ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.195.cold.1
- ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.196
- ___75-[CDPDSecureBackupController enableSecureBackupWithRecoveryKey:completion:]_block_invoke.111
- ___75-[CDPDTermsInfoBackupController fetchTermsAcceptanceForAccount:completion:]_block_invoke.28
- ___75-[CDPDTermsInfoBackupController fetchTermsAcceptanceForAccount:completion:]_block_invoke.28.cold.1
- ___76-[CDPDEscrowRecordController _deviceEscrowRecordStateUsingCache:completion:]_block_invoke.71
- ___76-[CDPDEscrowRecordController _deviceEscrowRecordStateUsingCache:completion:]_block_invoke.71.cold.1
- ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.106
- ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.106.cold.1
- ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.106.cold.2
- ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.106.cold.3
- ___77-[CDPDEscrowRecordController _performSilentEscrowRecordRepairWithCompletion:]_block_invoke.61
- ___79-[CDPDCircleController _joinCircleFallbackWithResult:ignoreBackups:completion:]_block_invoke.53
- ___79-[CDPDCircleController _requestCircleJoinWithObserver:requestBlock:completion:]_block_invoke.63
- ___79-[CDPDClientHandler fetchEscrowRecordDevicesWithContext:usingCache:completion:]_block_invoke.44
- ___79-[CDPInternalWalrusStateController setWalrusStatusEnabled:password:completion:]_block_invoke.72
- ___79-[CDPInternalWalrusStateController setWalrusStatusEnabled:password:completion:]_block_invoke.72.cold.1
- ___79-[CDPInternalWalrusStateController setWalrusStatusEnabled:password:completion:]_block_invoke.73
- ___80-[CDPDStateMachine _continueShouldPerformRepairWithOptionForceFetch:completion:]_block_invoke.157
- ___80-[CDPDStateMachine _continueShouldPerformRepairWithOptionForceFetch:completion:]_block_invoke.158
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.993
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.995
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.995.cold.1
- ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.177
- ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.177.cold.1
- ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.179
- ___83-[CDPDClientHandler localSecretChangedTo:secretType:context:uiProvider:completion:]_block_invoke.76
- ___84-[CDPDEscrowRecordController _continueSilentEscrowRecordRepairWithState:completion:]_block_invoke.78
- ___84-[CDPDEscrowRecordController _continueSilentEscrowRecordRepairWithState:completion:]_block_invoke.78.cold.1
- ___85-[CDPDClientHandler _startObservingConnectionStateForRepairWithStateMachine:context:]_block_invoke.68
- ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.77
- ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.77.cold.1
- ___85-[CDPDClientHandler handleCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.60
- ___85-[CDPDClientHandler repairCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.63
- ___85-[CDPDRecoveryValidatedJoinFlowController _accountResetRecoveryOptionWithCompletion:]_block_invoke.70
- ___85-[CDPDStateMachine _attemptBeneficiaryTrustWithInheritanceKey:retryCount:completion:]_block_invoke.119
- ___86-[CDPDClientHandler shouldPerformAuthenticatedRepairForContext:forceFetch:completion:]_block_invoke.73
- ___86-[CDPDRecoveryValidatedJoinFlowController _handleNoRecoveryFactorsWithMask:validator:]_block_invoke.239
- ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.78
- ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.78.cold.1
- ___90-[CDPDSecureChannelController startCircleApplicationApprovalServerWithContext:completion:]_block_invoke
- ___91-[CDPDStateMachine _isEligibleForRecoveryTokenWithContext:cdpStateMachineError:completion:]_block_invoke.43
- ___92-[CDPDSecureBackupController checkForExistingRecordMatchingPredicate:forceFetch:completion:]_block_invoke.92
- ___92-[CDPDSecureBackupController checkForExistingRecordMatchingPredicate:forceFetch:completion:]_block_invoke.92.cold.1
- ___93-[CDPDSecureBackupController upgradeICSCRecordsThenEnableSecureBackupWithContext:completion:]_block_invoke.82
- ___93-[CDPDSecureBackupController upgradeICSCRecordsThenEnableSecureBackupWithContext:completion:]_block_invoke.85.cold.1
- ___93-[CDPDSecureBackupController upgradeICSCRecordsThenEnableSecureBackupWithContext:completion:]_block_invoke_2.83
- ___93-[CDPDSecureBackupController upgradeICSCRecordsThenEnableSecureBackupWithContext:completion:]_block_invoke_2.83.cold.1
- ___93-[CDPDSecureBackupController upgradeICSCRecordsThenEnableSecureBackupWithContext:completion:]_block_invoke_2.83.cold.2
- ___98-[CDPDSecureBackupController _getOctagonEscrowBackupRecordDevicesWithOptionForceFetch:completion:]_block_invoke.57
- ___98-[CDPDSecureBackupController _getOctagonEscrowBackupRecordDevicesWithOptionForceFetch:completion:]_block_invoke.57.cold.1
- ___98-[CDPDSecureBackupController _getOctagonEscrowBackupRecordDevicesWithOptionForceFetch:completion:]_block_invoke.58
- ___block_descriptor_64_e8_32s40s48s56s_e24_v32?0"NSData"8^16^24ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56bs64r_e34_v24?0"NSDictionary"8"NSError"16ls32l8r64l8s56l8s40l8s48l8
- ___block_literal_global.102
- ___block_literal_global.167
- ___block_literal_global.44
- ___block_literal_global.45
- ___block_literal_global.69
- ___block_literal_global.739
- ___block_literal_global.750
- ___block_literal_global.752
- ___block_literal_global.76
- ___block_literal_global.853
- ___block_literal_global.90
- ___block_literal_global.900
- ___block_literal_global.912
- ___block_literal_global.925
- ___block_literal_global.997
- ___swift_memcpy0_1
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_CoreCDPInternal
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_CoreCDPInternal
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_CoreCDPInternal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_CoreCDPInternal
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_CoreCDPInternal
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_CoreCDPInternal
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_CoreCDPInternal
- _getAllowedADPEvents.approvedEvents
- _getAllowedDNUEvents.approvedEvents
- _objc_msgSend$_startListeningWithProxy:
- _objc_msgSend$_startListeningWithProxyWithEnforcedQoS:
- _objc_msgSend$initWithAccount:cdpdAccount:securityProxy:pcsProxy:
- _objc_msgSend$initWithAccount:cdpdAccount:securityProxy:pcsProxy:accountStore:
- _objc_msgSend$shouldOfferPiggybackingBasedRecovery
- _objc_msgSend$startCircleApplicationApprovalServerWithContext:completion:
- _swift_bridgeObjectRetain_n
CStrings:
+ "%@: Cannot determine circle status for unknown account with altDSID (%{mask.hash}@)"
+ "%@: Cannot silently repair circle status due to rate limiting"
+ "%@: Minibuddy silent burn ineligible for context type"
+ "%@: SOS compatible mode is off: otViewEnabled=%{BOOL}d"
+ "%@: SOS compatible mode is on: sosViewEnabled=%{BOOL}d and otViewEnabled=%{BOOL}d"
+ "%@: Will not determine circle status for device without local secret (not eligible)"
+ "%@: fetchUserControllableViewsSyncingEnabled when checking if OT views are enabled finished with error:%@"
+ "%@: isUserVisibleKeychainSyncEnabled: sosCompatibilityEnabled=YES SOSCompatibilityTypeOptInNeeded=YES"
+ "%@: viewMemberForAllUserFacingViews when checking all SOS user facing views are enabled finished with error:%@"
+ "@\"AKWalrusConfigProvider\""
+ "@64@0:8@16@24@32@40@48@56"
+ "@?<v@?B@\"NSError\">16@0:8"
+ "AnyRKAreOctagonDistrusted"
+ "Attempting to persist verifier for keyType: %ld for %{mask.hash}@"
+ "Attempting to persist verifier: %@ for %{mask.hash}@"
+ "BEGIN [%lld]: AnyRKAreOctagonDistrusted  enableTelemetry=YES "
+ "CDP Enabled on requestor after Prox flow: %{BOOL}d and error: %@"
+ "CDPADPRegionAvailabilityProvider"
+ "CDPContext is nil"
+ "CDPProximityPairingServiceProtocol"
+ "Context for primary account is also nil. Returning early."
+ "Context is nil, using context for primary account"
+ "Could not fetch walrus availability configuration. Error: %@"
+ "END [%lld] %fs: AnyRKAreOctagonDistrusted  Error=%{public,signpost.telemetry:number1,name=Error}d "
+ "Error while checking RK distrusted. Assuming no recovery keys are distrusted."
+ "Escrow check - Failed to perform escrow check because octagon untrusted"
+ "Escrow check - Failed to perform escrow check because secure terms needed"
+ "Escrow check - Failed to perform escrow check with error: %@"
+ "Escrow check - No error and also no result"
+ "Escrow check - needs reenroll with viability state: %lu"
+ "Escrow check - recoverable with repairReason: %ld"
+ "Escrow check completed with repair reason: %ld and viabilityState: %lu"
+ "Failed to perform escrow check with error: %@"
+ "Ledger: EDP State access failed - context is nil"
+ "Ledger: edpRPDBlockingError - context is nil"
+ "Ledger: isForcedReset force set to false since context is nil"
+ "Ledger: isRepairFlow - context is nil"
+ "Ledger: manateeRPDBlockingError - context is nil"
+ "Ledger: probationEnded - context is nil"
+ "NaturalUI"
+ "Nil context provided. Creating context for primary account"
+ "Octagon reports hasDistrustedRKs=%{BOOL}d with error: %@"
+ "OnBoardingKit"
+ "Q24@0:8q16"
+ "Received isSingleICSC = %d"
+ "Recovery flow context is nil"
+ "Requesting server suppress filtering"
+ "Setting walrus feature availability status for primary account - %ld"
+ "Silent auth requested for escrow check with isBackground: %@"
+ "Solarium"
+ "Successfully performed escrow check. viabilityState: %lu"
+ "SwiftUI"
+ "T@?,C,N"
+ "There is no walrus config."
+ "Unapproved CFUType %@ received in telemetry for %@ attribute"
+ "Vv36@0:8@\"CDPContext\"16B24@?<v@?Q@\"NSError\">28"
+ "_anyRecoveryKeysAreDistrusted"
+ "_approvedCustodianCountForAltDSID:"
+ "_cdpEscrowRecordViabilityStateFromRepairReason:"
+ "_configProvider"
+ "_deviceCircleStatusUsingCache:completion:"
+ "_enforceIdentifiableDataPrivacyComplianceOnEvent:manager:"
+ "_hasLocalSecret"
+ "_isEventPrivacyApprovedIdentifiable:"
+ "_isSingleICSC:"
+ "_proxService"
+ "_reauthenticateAndPerformEscrowCheckWithIsBackground:completion:"
+ "_replaceClientNameWithEvent:"
+ "_reportWalrusRepairFinishEventWithCombinedWalrusStatus:error:"
+ "_reportWalrusRepairStartEventWithCombinedWalrusStatus:"
+ "_startListeningWithProxy:completion:"
+ "_startListeningWithProxyWithEnforcedQoS:completion:"
+ "anyRecoveryKeysAreOctagonDistrustedWithContext:completion:"
+ "anyRecoveryKeysAreOctagonDistrustedWithError:"
+ "areRecoveryKeysDistrusted:error:"
+ "com.apple.CDPProximityPairingService"
+ "com.apple.security.clearCliqueFromAccount"
+ "com.apple.security.fetchAccountWideSettings"
+ "com.apple.security.fetchAccountWideSettingsTPH"
+ "com.apple.security.oTBecomeReadyOperation"
+ "com.apple.security.oTLocalCKKSResetOperation"
+ "com.apple.security.oTResetOperation"
+ "com.apple.security.oTSetCDPBitOperation"
+ "com.apple.security.oTTriggerEscrowUpdateOperation"
+ "com.apple.security.performCKServerUnreadableDataRemoval"
+ "com.apple.security.performCKServerUnreadableDataRemovalTPH"
+ "com.apple.security.resetCKKSZonesLackingTLKsOperation"
+ "com.apple.security.resetProtectedData"
+ "com.apple.security.resetSOS"
+ "com.apple.security.resetTPH"
+ "escrowCheck:isBackgroundCheck:error:"
+ "escrowCheckForContext:isBackground:completion:"
+ "escrowCheckWithIsBackground:completion:"
+ "escrowWalrusStatus"
+ "event (%@) is approved for identifiable data collection but deviceSessionID is not found on the event. Attaching..."
+ "event (%@) is not approved for identifiable data collection but deviceSessionID is found on the event. Removing..."
+ "featureStatus"
+ "getAllowedAccountAccessEvents"
+ "getApprovedEventsForAll"
+ "getWalrusConfigWithCompletion:"
+ "initWithAccount:cdpdAccount:securityProxy:pcsProxy:accountStore:sbProxy:"
+ "initWithAccount:cdpdAccount:securityProxy:pcsProxy:sbProxy:"
+ "initWithDictionary:"
+ "initWithServiceName:"
+ "initWithWalrusConfigProvider:"
+ "interfaceWithProtocol:"
+ "invalidate"
+ "isMainThread"
+ "isSEPBasedICSCHealing enabled, this SPI is deprecated because iCSC creation is handled by SEAR"
+ "isSEPBasedICSCHealingEnabled"
+ "isWalrusEnabledForPrimaryAccountWithCompletionHandler:"
+ "needsReenroll"
+ "octagonTrusted"
+ "octagonWalrusStatus"
+ "onProxCompletion"
+ "pcsWalrusStatus"
+ "pendingCFUTypes"
+ "remoteObjectProxyWithErrorHandler:"
+ "repairReason"
+ "rkDistrustedInOctagon"
+ "secureTermsNeeded"
+ "setOnProxCompletion:"
+ "setRemoteObjectInterface:"
+ "shouldOfferPiggybackingBasedRecovery:"
+ "sosCompatibilityEnabled"
+ "startCircleApplicationApprovalServerWithContext:serverStarted:"
+ "startCircleApplicationApprovalServerWithContext:serverStarted:completion:"
+ "telemetryDeviceSessionIDForAccount:"
+ "v16@?0@?<v@?@\"OTEscrowCheckCallResult\"@\"NSError\">8"
+ "v24@?0@\"AKWalrusConfig\"8@\"NSError\"16"
+ "v24@?0@\"OTEscrowCheckCallResult\"8@\"NSError\"16"
+ "v28@0:8B16@?<v@?Q@\"NSError\">20"
+ "viewMemberForAllUserFacingViews:"
- "Attempting to persist verifier for keyType: %ld for %@"
- "Attempting to persist verifier: %@ for %@"
- "Fetched accepted terms with result: %@"
- "Older, non-view-aware peers are present therefore user visible keychain is implicitly enabled despite the state of views"
- "_startListeningWithProxy:"
- "_startListeningWithProxyWithEnforcedQoS:"
- "initWithAccount:cdpdAccount:securityProxy:pcsProxy:"
- "initWithAccount:cdpdAccount:securityProxy:pcsProxy:accountStore:"
- "shouldOfferPiggybackingBasedRecovery"

```
