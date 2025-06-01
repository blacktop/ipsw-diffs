## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-359.2.0.0.0
-  __TEXT.__text: 0x62ce0
+359.4.3.0.0
+  __TEXT.__text: 0x63ce0
   __TEXT.__auth_stubs: 0xa90
-  __TEXT.__objc_methlist: 0x3984
+  __TEXT.__objc_methlist: 0x3978
   __TEXT.__const: 0x90
-  __TEXT.__oslogstring: 0xede7
-  __TEXT.__cstring: 0x3af5
-  __TEXT.__gcc_except_tab: 0x790
-  __TEXT.__unwind_info: 0x13e4
+  __TEXT.__oslogstring: 0xf274
+  __TEXT.__cstring: 0x3ba5
+  __TEXT.__gcc_except_tab: 0x7a0
+  __TEXT.__unwind_info: 0x1400
   __TEXT.__objc_classname: 0xb4b
-  __TEXT.__objc_methname: 0xbe58
+  __TEXT.__objc_methname: 0xbecc
   __TEXT.__objc_methtype: 0x2232
-  __TEXT.__objc_stubs: 0x9d60
-  __DATA_CONST.__got: 0x7f0
-  __DATA_CONST.__const: 0x1a60
+  __TEXT.__objc_stubs: 0x9d80
+  __DATA_CONST.__got: 0x820
+  __DATA_CONST.__const: 0x1a28
   __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xd680
-  __DATA_CONST.__objc_selrefs: 0x2b68
+  __DATA_CONST.__objc_const: 0xd700
+  __DATA_CONST.__objc_selrefs: 0x2b78
   __DATA_CONST.__objc_arraydata: 0x68
   __AUTH_CONST.__objc_const: 0x19f0
-  __AUTH_CONST.__cfstring: 0x2fc0
+  __AUTH_CONST.__cfstring: 0x3060
   __AUTH_CONST.__const: 0x360
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x30

   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x488
   __DATA.__objc_superrefs: 0x150
-  __DATA.__objc_ivar: 0x364
+  __DATA.__objc_ivar: 0x36c
   __DATA.__data: 0xc90
   __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0x618

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8F2EE22C-0458-3074-A0DC-57B828E6E67C
-  Functions: 2279
-  Symbols:   7791
-  CStrings:  4011
+  UUID: 53ED7CA9-3D0C-3C51-8BE7-BC24939A3332
+  Functions: 2286
+  Symbols:   7813
+  CStrings:  4041
 
Symbols:
+ -[CDPDAnalyticsTransport initWithClientType:clientBundleId:clientName:].cold.1
+ -[CDPDEscrowRecordController _checkFirstUsableRecordForDeviceFromSource:completion:]
+ -[CDPDRecoveryValidatedJoinFlowController _isWalrusEnabled]
+ -[CDPDSecureBackupController _authenticatedEnableSecureBackupWithContext:completion:].cold.10
+ -[CDPTTSUChannel telemetryFlowIDFromRequester]
+ GCC_except_table20
+ GCC_except_table41
+ _OBJC_IVAR_$_CDPTTSUChannel._cdpContext
+ _OBJC_IVAR_$_CDPTTSUChannel._telemetryFlowIDFromRequester
+ __OBJC_$_PROP_LIST_CDPSecureChannelApprovingProxy
+ ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.43
+ ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.43.cold.1
+ ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.45.cold.1
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.133
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.133.cold.1
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.133.cold.2
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.133.cold.3
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.134
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.134.cold.1
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.134.cold.2
+ ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.134.cold.3
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.201
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.201.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.202
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.202.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.205
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.216
+ ___55-[CDPContext(Daemon) reauthenticateUserWithCompletion:]_block_invoke.18
+ ___55-[CDPContext(Daemon) reauthenticateUserWithCompletion:]_block_invoke.18.cold.1
+ ___55-[CDPContext(Daemon) reauthenticateUserWithCompletion:]_block_invoke.18.cold.2
+ ___55-[CDPContext(Daemon) reauthenticateUserWithCompletion:]_block_invoke.cold.2
+ ___56-[CDPDSecureChannelController _startListeningWithProxy:]_block_invoke.77
+ ___56-[CDPDSecureChannelController _startListeningWithProxy:]_block_invoke.cold.2
+ ___62-[CDPDCircleController _joinCircleIgnoringBackups:completion:]_block_invoke.33
+ ___62-[CDPDCircleController _joinCircleIgnoringBackups:completion:]_block_invoke.34
+ ___62-[CDPDCircleController _joinCircleIgnoringBackups:completion:]_block_invoke.34.cold.1
+ ___63-[CDPDSecureBackupController disableRecoveryKeyWithCompletion:]_block_invoke.139
+ ___65-[CDPDClientHandler attemptToEscrowPreRecord:context:completion:]_block_invoke.54
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.27.cold.2
+ ___67-[CDPDSecureBackupController deleteAllBackupRecordsWithCompletion:]_block_invoke.136
+ ___67-[CDPDSecureBackupController deleteSingleICSCBackupWithCompletion:]_block_invoke.137
+ ___73-[CDPDClientHandler shouldPerformRepairForContext:forceFetch:completion:]_block_invoke.51
+ ___75-[CDPDSecureBackupController enableSecureBackupWithRecoveryKey:completion:]_block_invoke.94
+ ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.91
+ ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.91.cold.1
+ ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.91.cold.2
+ ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.91.cold.3
+ ___77-[CDPDEscrowRecordController _performSilentEscrowRecordRepairWithCompletion:]_block_invoke.46
+ ___79-[CDPDCircleController _joinCircleFallbackWithResult:ignoreBackups:completion:]_block_invoke.37
+ ___79-[CDPDCircleController _requestCircleJoinWithObserver:requestBlock:completion:]_block_invoke.47
+ ___80-[CDPDClientHandler startCircleApplicationApprovalServerWithContext:completion:]_block_invoke_2
+ ___83-[CDPDClientHandler localSecretChangedTo:secretType:context:uiProvider:completion:]_block_invoke.55
+ ___84-[CDPDEscrowRecordController _checkAllRecordsForCurrentDeviceUsingCache:completion:]_block_invoke
+ ___84-[CDPDEscrowRecordController _checkFirstUsableRecordForDeviceFromSource:completion:]_block_invoke
+ ___84-[CDPDEscrowRecordController _checkFirstUsableRecordForDeviceFromSource:completion:]_block_invoke.cold.1
+ ___85-[CDPDClientHandler _startObservingConnectionStateForRepairWithStateMachine:context:]_block_invoke.47
+ ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.56
+ ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.56.cold.1
+ ___86-[CDPDClientHandler shouldPerformAuthenticatedRepairForContext:forceFetch:completion:]_block_invoke.52
+ ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.57
+ ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.57.cold.1
+ ___block_descriptor_40_e8_32bs_e36_v24?0"OTEscrowRecord"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e79_v32?0"NSDictionary"8"NSDictionary"16?<v?i"NSDictionary""NSDictionary">24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e32_v24?0"CDPContext"8"NSError"16lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48s_e24_v32?0"NSData"8^16^24ls32l8s40l8s48l8
+ ___block_literal_global.131
+ ___block_literal_global.172
+ ___block_literal_global.184
+ ___block_literal_global.197
+ ___block_literal_global.26
+ ___block_literal_global.44
+ ___block_literal_global.55
+ ___block_literal_global.57
+ _kCDPAnalyticsDevicePosture
+ _kCDPAnalyticsRPDProbationEvent
+ _kCDPAnalyticsSecureChannelProcessApprovalEvent
+ _kCDPAnalyticsWaitForPriorityViewKeychainDataRecovery
+ _kSecureBackupDeviceSessionIDKey
+ _kSecureBackupFlowIDKey
+ _objc_msgSend$_checkFirstUsableRecordForDeviceFromSource:completion:
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$isDemoDevice
+ _objc_msgSend$setDeviceSessionID:
+ _objc_msgSend$setFlowID:
+ _objc_msgSend$telemetryFlowIDFromRequester
- -[CDPDEscrowRecordController _checkAllRecordsForDeviceMatchingPredicate:source:completion:]
- -[CDPDEscrowRecordController _predicateForRecordWithPeerID:]
- -[CDPPiggybackingPayloadProvider supportsInteractiveAuth]
- -[CDPTTSUPayloadProvider supportsInteractiveAuth]
- GCC_except_table19
- GCC_except_table42
- ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.44.cold.1
- ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.46
- ___103-[CDPDCircleController resetCircleIncludingCloudKitData:cloudKitResetReasonDescription:withCompletion:]_block_invoke.46.cold.1
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.129
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.129.cold.1
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.129.cold.2
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.129.cold.3
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.130
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.130.cold.1
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.130.cold.2
- ___114-[CDPDSecureBackupController validateAndRepairRecoveryKeyMismatchWithContext:authProvider:circleProxy:completion:]_block_invoke.130.cold.3
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.195
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.196
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.196.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.199
- ___55-[CDPContext(Daemon) reauthenticateUserWithCompletion:]_block_invoke.17
- ___55-[CDPContext(Daemon) reauthenticateUserWithCompletion:]_block_invoke.17.cold.1
- ___56-[CDPDSecureChannelController _startListeningWithProxy:]_block_invoke.75
- ___60-[CDPDEscrowRecordController _predicateForRecordWithPeerID:]_block_invoke
- ___62-[CDPDCircleController _joinCircleIgnoringBackups:completion:]_block_invoke.32
- ___62-[CDPDCircleController _joinCircleIgnoringBackups:completion:]_block_invoke.35
- ___62-[CDPDCircleController _joinCircleIgnoringBackups:completion:]_block_invoke.36
- ___62-[CDPDCircleController _joinCircleIgnoringBackups:completion:]_block_invoke.36.cold.1
- ___63-[CDPDSecureBackupController disableRecoveryKeyWithCompletion:]_block_invoke.135
- ___65-[CDPDClientHandler attemptToEscrowPreRecord:context:completion:]_block_invoke.53
- ___67-[CDPDSecureBackupController deleteAllBackupRecordsWithCompletion:]_block_invoke.132
- ___67-[CDPDSecureBackupController deleteSingleICSCBackupWithCompletion:]_block_invoke.133
- ___73-[CDPDClientHandler shouldPerformRepairForContext:forceFetch:completion:]_block_invoke.50
- ___75-[CDPDSecureBackupController enableSecureBackupWithRecoveryKey:completion:]_block_invoke.90
- ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.87
- ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.87.cold.1
- ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.87.cold.2
- ___76-[CDPDSecureBackupController _retryRepairWithContext:retryCount:completion:]_block_invoke.87.cold.3
- ___77-[CDPDEscrowRecordController _performSilentEscrowRecordRepairWithCompletion:]_block_invoke.45
- ___79-[CDPDCircleController _joinCircleFallbackWithResult:ignoreBackups:completion:]_block_invoke.39
- ___79-[CDPDCircleController _requestCircleJoinWithObserver:requestBlock:completion:]_block_invoke.48
- ___83-[CDPDClientHandler localSecretChangedTo:secretType:context:uiProvider:completion:]_block_invoke.54
- ___85-[CDPDClientHandler _startObservingConnectionStateForRepairWithStateMachine:context:]_block_invoke.46
- ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.55
- ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.55.cold.1
- ___86-[CDPDClientHandler shouldPerformAuthenticatedRepairForContext:forceFetch:completion:]_block_invoke.51
- ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.56
- ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.56.cold.1
- ___91-[CDPDEscrowRecordController _checkAllRecordsForDeviceMatchingPredicate:source:completion:]_block_invoke
- ___91-[CDPDEscrowRecordController _checkAllRecordsForDeviceMatchingPredicate:source:completion:]_block_invoke.61
- ___91-[CDPDEscrowRecordController _checkAllRecordsForDeviceMatchingPredicate:source:completion:]_block_invoke.cold.1
- ___block_descriptor_40_e8_32s_e22_B24?0"CDPDevice"816ls32l8
- ___block_descriptor_40_e8_32s_e31_v32?0"OTEscrowRecord"8Q16^B24ls32l8
- ___block_descriptor_48_e8_32bs40w_e32_v24?0"CDPContext"8"NSError"16lw40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e79_v32?0"NSDictionary"8"NSDictionary"16?<v?i"NSDictionary""NSDictionary">24ls40l8s32l8
- ___block_descriptor_48_e8_32s40s_e24_v32?0"NSData"8^16^24ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e23_v28?0Q8B16"NSError"20ls32l8s40l8s48l8
- ___block_literal_global.125
- ___block_literal_global.166
- ___block_literal_global.178
- ___block_literal_global.191
- ___block_literal_global.23
- ___block_literal_global.38
- ___block_literal_global.49
- ___block_literal_global.51
- _kCDP_kSecureBackupDeviceSessionIDKey
- _kCDP_kSecureBackupFlowIDKey
- _objc_msgSend$_checkAllRecordsForDeviceMatchingPredicate:source:completion:
- _objc_msgSend$_predicateForRecordWithPeerID:
- _objc_msgSend$arrayWithCapacity:
- _objc_msgSend$promptForCredentials:
- _objc_msgSend$supportsInteractiveAuth
CStrings:
+ "\"%@: Could not find a record matching serial number (%@) with source (%{public}ld).\""
+ "\"%@: First usable record matching the serial number (%@) with source (%{public}ld) is (%@)\""
+ "\"Adding telemetry flow ID %{public}@ and session ID %{public}@ to recoveryInfo\""
+ "\"Application server completed result %{BOOL}d and error: %@\""
+ "\"CDP Reauth on HomePod failed. Error: %@\""
+ "\"CDP Reauthentication on HomePod failed. Error: %@\""
+ "\"CDPTTSUChannel: Flow ID exists on the requesting proxy, attaching to payload.\""
+ "\"Flow ID was received from the requesting proxy, setting on the approving proxy.\""
+ "\"HomePod failed CDP join with AuthKit error: %@\""
+ "\"No explicit error, falling back to CDPStateErrorCouldNotApplyToJoinCircleNoFallback\""
+ "\"Passing telemetry flow ID %{public}@ and deviceSession ID %{public}@ to secureBackupProxy\""
+ "\"Passing telemetry flow ID %{public}@ and session ID %{public}@ to OTClique performEscrowRecoveryWithContextData\""
+ "\"Setting requester's flowID on kCDPAnalyticsSecureChannelProcessApprovalEvent\""
+ "\"Showing RPD error alert for Walrus user. RecoveryMap is %@\""
+ "\"Showing RPD error alert for non-Walrus user. RecoveryMap is %@\""
+ "\"Showing RPD unrecoverable error alert for Walrus user\""
+ "\"Showing RPD unrecoverable error alert for non-Walrus user\""
+ "\"Underlying transport is nil. clientType = %@, clientBundleId = %@, clientName = %@\""
+ "\"Walrus status on recovery context is %ld\""
+ "\"clientBundleID is nil, transport will not be initialized properly. clientType = %@, clientName = %@\""
+ "3"
+ "@\"Transport is nil, event: %@ will not be sent.\""
+ "CDPChannelTTSUTelemetryFlowId"
+ "Demo"
+ "RPD_CONFIRMATION_STEP_2_MESSAGE"
+ "RPD_CONFIRMATION_STEP_2_TITLE"
+ "T@\"NSString\",R,N"
+ "T@\"NSString\",R,N,V_telemetryFlowIDFromRequester"
+ "WALRUS_ALERT_BUTTON_TITLE_DELETE_ICLOUD_DATA"
+ "WALRUS_STORAGE_LIST_UNAVAILABLE_CONFIRMATION_DELETE_BUTTON_TITLE"
+ "_checkFirstUsableRecordForDeviceFromSource:completion:"
+ "_telemetryFlowIDFromRequester"
+ "com.apple.appleaccount.iCloudAccountAdd"
+ "dictionaryWithDictionary:"
+ "isDemoDevice"
+ "setDeviceSessionID:"
+ "setFlowID:"
+ "telemetryFlowIDFromRequester"
+ "v24@?0@\"OTEscrowRecord\"8@\"NSError\"16"
- "\"%@: Checking all escrow records for a device matching predicate (%@) with source (%ld)\""
- "\"%@: Checking all escrow records matching peerID (%@) from source (%ld)\""
- "\"Circle resume failed, re-authentication requested!\""
- "\"Found matching devices by checking all records, will return first: %@\""
- "\"No explicit error, falling back to CouldNotApplyToJoinCircle\""
- "1"
- "B24@?0@\"CDPDevice\"8@16"
- "SecureBackupDeviceSessionIDKey"
- "SecureBackupFlowIDKey"
- "_checkAllRecordsForDeviceMatchingPredicate:source:completion:"
- "_predicateForRecordWithPeerID:"
- "arrayWithCapacity:"
- "supportsInteractiveAuth"
- "v32@?0@\"OTEscrowRecord\"8Q16^B24"

```
