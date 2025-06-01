## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-353.1.1.4.0
-  __TEXT.__text: 0x61880
-  __TEXT.__auth_stubs: 0xa70
-  __TEXT.__objc_methlist: 0x392c
+359.2.0.0.0
+  __TEXT.__text: 0x62ce0
+  __TEXT.__auth_stubs: 0xa90
+  __TEXT.__objc_methlist: 0x3984
   __TEXT.__const: 0x90
-  __TEXT.__oslogstring: 0xebd3
-  __TEXT.__cstring: 0x3921
-  __TEXT.__gcc_except_tab: 0x780
-  __TEXT.__unwind_info: 0x13b0
+  __TEXT.__oslogstring: 0xede7
+  __TEXT.__cstring: 0x3af5
+  __TEXT.__gcc_except_tab: 0x790
+  __TEXT.__unwind_info: 0x13e4
   __TEXT.__objc_classname: 0xb4b
-  __TEXT.__objc_methname: 0xbcc6
-  __TEXT.__objc_methtype: 0x21da
-  __TEXT.__objc_stubs: 0x9c60
-  __DATA_CONST.__got: 0x7d8
+  __TEXT.__objc_methname: 0xbe58
+  __TEXT.__objc_methtype: 0x2232
+  __TEXT.__objc_stubs: 0x9d60
+  __DATA_CONST.__got: 0x7f0
   __DATA_CONST.__const: 0x1a60
   __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xd640
-  __DATA_CONST.__objc_selrefs: 0x2b18
+  __DATA_CONST.__objc_const: 0xd680
+  __DATA_CONST.__objc_selrefs: 0x2b68
   __DATA_CONST.__objc_arraydata: 0x68
   __AUTH_CONST.__objc_const: 0x19f0
-  __AUTH_CONST.__cfstring: 0x2e00
+  __AUTH_CONST.__cfstring: 0x2fc0
   __AUTH_CONST.__const: 0x360
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x548
+  __AUTH_CONST.__auth_got: 0x558
   __AUTH.__objc_data: 0x1068
   __AUTH.__data: 0x10
   __DATA.__objc_protorefs: 0x10

   __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
+  - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8B3FDDDB-55A7-35C8-99DD-4ECBB01F43EF
-  Functions: 2259
-  Symbols:   7738
-  CStrings:  3960
+  UUID: 8F2EE22C-0458-3074-A0DC-57B828E6E67C
+  Functions: 2279
+  Symbols:   7791
+  CStrings:  4011
 
Symbols:
+ -[CDPDCircleController _joinCircleIgnoringBackups:completion:].cold.5
+ -[CDPDCircleController _joinCircleIgnoringBackups:completion:].cold.6
+ -[CDPDClientHandler circleStatusForContext:completion:]
+ -[CDPDClientHandler circleStatusForContext:completion:].cold.1
+ -[CDPDClientHandler circleStatusForContext:completion:].cold.2
+ -[CDPDClientHandler cliqueStatusForContext:completion:]
+ -[CDPDClientHandler cliqueStatusForContext:completion:].cold.1
+ -[CDPDClientHandler cliqueStatusForContext:completion:].cold.2
+ -[CDPDRecoveryValidatedJoinFlowController _custodianRecoveryOptionWithCompletion:]
+ -[CDPDRecoveryValidatedJoinFlowController _entryLimitCustodianRecoveryAvailableBodyForDevice:]
+ -[CDPDRecoveryValidatedJoinFlowController _entryLimitRecoveryKeyAndCustodianRecoveryAvailableBodyForDevice:]
+ -[CDPDRecoveryValidatedJoinFlowController _fallbackRecoveryOptionsWithCompletion:]
+ -[CDPDRecoveryValidatedJoinFlowController _populateUserInfo:recoveryIndexHandlers:withRecoveryOptions:]
+ -[CDPDRecoveryValidatedJoinFlowController _recoveryKeyRecoveryOptionWithCompletion:]
+ -[CDPDStateMachine initWithContext:uiProvider:connection:]
+ GCC_except_table17
+ GCC_except_table88
+ _CFPreferencesCopyAppValue
+ _NSSQLiteErrorDomain
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.195
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.196
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.196.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.199
+ ___38-[CDPDStateMachine _attemptCDPEnable:]_block_invoke.90
+ ___41-[CDPTTSUChannel sendPayload:completion:]_block_invoke.cold.3
+ ___41-[CDPTTSUChannel sendPayload:completion:]_block_invoke.cold.4
+ ___41-[CDPTTSUChannel sendPayload:completion:]_block_invoke.cold.5
+ ___42-[CDPDSecureChannelController joinCircle:]_block_invoke.19.cold.2
+ ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.86
+ ___56-[CDPDSecureChannelController _startListeningWithProxy:]_block_invoke.75
+ ___58-[CDPDStateMachine _handleBeneficiaryTrustWithCompletion:]_block_invoke.68
+ ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.88
+ ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.78.cold.1
+ ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.80
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.46
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.48
+ ___66-[CDPDStateMachine _handleCloudDataProtectionStateWithCompletion:]_block_invoke.66
+ ___77-[CDPDEscrowRecordController _performSilentEscrowRecordRepairWithCompletion:]_block_invoke.45
+ ___82-[CDPDRecoveryValidatedJoinFlowController _custodianRecoveryOptionWithCompletion:]_block_invoke
+ ___84-[CDPDRecoveryValidatedJoinFlowController _recoveryKeyRecoveryOptionWithCompletion:]_block_invoke
+ ___85-[CDPDRecoveryValidatedJoinFlowController _accountResetRecoveryOptionWithCompletion:]_block_invoke.38
+ ___85-[CDPDStateMachine _attemptBeneficiaryTrustWithInheritanceKey:retryCount:completion:]_block_invoke.77
+ ___91-[CDPDEscrowRecordController _checkAllRecordsForDeviceMatchingPredicate:source:completion:]_block_invoke.61
+ ___block_literal_global.125
+ ___block_literal_global.166
+ ___block_literal_global.178
+ ___block_literal_global.191
+ ___block_literal_global.38
+ ___block_literal_global.50
+ ___block_literal_global.51
+ _kAAFTestSignature
+ _kCDPAnalyticsEscrowRecordFetchSource
+ _kCDPAnalyticsFetchEscrowRecordsEvent
+ _objc_msgSend$_custodianRecoveryOptionWithCompletion:
+ _objc_msgSend$_entryLimitCustodianRecoveryAvailableBodyForDevice:
+ _objc_msgSend$_entryLimitRecoveryKeyAndCustodianRecoveryAvailableBodyForDevice:
+ _objc_msgSend$_fallbackRecoveryOptionsWithCompletion:
+ _objc_msgSend$_populateUserInfo:recoveryIndexHandlers:withRecoveryOptions:
+ _objc_msgSend$_recoveryKeyRecoveryOptionWithCompletion:
+ _objc_msgSend$initWithContext:uiProvider:connection:
+ _objc_msgSend$intValue
+ _objc_msgSend$isSilentEscrowRecordRepairEnabledV2
+ _objc_msgSend$localizedDescription
+ _sel_getName
- -[CDPDRecoveryValidatedJoinFlowController _fallbackRecoveryOptionWithCompletion:]
- -[CDPDRecoveryValidatedJoinFlowController _populateUserInfo:recoveryIndexHandlers:withRecoveryOption:]
- GCC_except_table16
- GCC_except_table87
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.170
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.170.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.171
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.171.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.174
- ___38-[CDPDStateMachine _attemptCDPEnable:]_block_invoke.89
- ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.84
- ___56-[CDPDSecureChannelController _startListeningWithProxy:]_block_invoke.74
- ___58-[CDPDStateMachine _handleBeneficiaryTrustWithCompletion:]_block_invoke.67
- ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.86
- ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.77
- ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.77.cold.1
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.45
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.47
- ___66-[CDPDStateMachine _handleCloudDataProtectionStateWithCompletion:]_block_invoke.64
- ___77-[CDPDEscrowRecordController _performSilentEscrowRecordRepairWithCompletion:]_block_invoke.42
- ___81-[CDPDRecoveryValidatedJoinFlowController _fallbackRecoveryOptionWithCompletion:]_block_invoke
- ___85-[CDPDRecoveryValidatedJoinFlowController _accountResetRecoveryOptionWithCompletion:]_block_invoke.40
- ___85-[CDPDStateMachine _attemptBeneficiaryTrustWithInheritanceKey:retryCount:completion:]_block_invoke.76
- ___91-[CDPDEscrowRecordController _checkAllRecordsForDeviceMatchingPredicate:source:completion:]_block_invoke.55
- ___block_literal_global.139
- ___block_literal_global.151
- ___block_literal_global.164
- ___block_literal_global.46
- ___block_literal_global.48
- ___block_literal_global.98
- _kCDPAnalyticsNumberOfOTPeers
- _objc_msgSend$_fallbackRecoveryOptionWithCompletion:
- _objc_msgSend$isSilentEscrowRecordRepairEnabled
CStrings:
+ "\"%@: Used precomputed escrowRecordHealthCheckFailureCount bit and determined escrow record state is %s.\""
+ "\"%s: Did not recieve a context, failing!\""
+ "\"%s: Missing entitlement, failing!\""
+ "\"CDPTTSUChannel: Received error: %@\""
+ "\"Creating recovery option: Custodian\""
+ "\"Detected a pref to require all failures to be fatal or platform is HomePod, failing out...\""
+ "\"No explicit error, falling back to CouldNotApplyToJoinCircle\""
+ "\"No secure channel\""
+ "\"We dont support RPD during signin flow\""
+ "@\"CDPTTSUChannel: No response data or error receieved\""
+ "@\"CDPTTSUChannel: Recieved reply: %@\""
+ "@\"Failed to process and reply message with replyError: %@\""
+ "AKAuthenticationServerError"
+ "AOSErrorDomain"
+ "CUSTODIAN_RECOVERY_HELP_PROMPT_MESSAGE"
+ "RECOVERY_KEY_CUSTODIAN_RECOVERY_HELP_PROMPT_MESSAGE"
+ "REMOTE_SECRET_ENTRY_FORGOT_CODE_DIALOG_CUSTODIAN"
+ "TelemetryInternalSignature"
+ "Vv32@0:8@\"CDPContext\"16@?<v@?i@\"NSError\">24"
+ "Vv32@0:8@\"CDPContext\"16@?<v@?q@\"NSError\">24"
+ "_custodianRecoveryOptionWithCompletion:"
+ "_entryLimitCustodianRecoveryAvailableBodyForDevice:"
+ "_entryLimitRecoveryKeyAndCustodianRecoveryAvailableBodyForDevice:"
+ "_fallbackRecoveryOptionsWithCompletion:"
+ "_populateUserInfo:recoveryIndexHandlers:withRecoveryOptions:"
+ "_recoveryKeyRecoveryOptionWithCompletion:"
+ "circleStatusForContext:completion:"
+ "cliqueStatusForContext:completion:"
+ "com.apple.AAAFoundation"
+ "com.apple.AppleAccount.Error"
+ "com.apple.accounts.keychain"
+ "com.apple.appleid.accountHealthEvent"
+ "com.apple.security.kcparingchannel"
+ "com.apple.security.trustedpeers.peerstatus"
+ "com.apple.utilities.sqlite3"
+ "initWithContext:uiProvider:connection:"
+ "intValue"
+ "isSilentEscrowRecordRepairEnabledV2"
+ "localizedDescription"
+ "non-viable or not found"
+ "securityd"
- "\"Detected a pref to require all failures to be fatal, failing out...\""
- "\"Event process name: %@\""
- "_fallbackRecoveryOptionWithCompletion:"
- "isSilentEscrowRecordRepairEnabled"

```
