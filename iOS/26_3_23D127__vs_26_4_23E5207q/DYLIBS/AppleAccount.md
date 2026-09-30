## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

```diff

-1037.325.3.0.0
-  __TEXT.__text: 0xeb984
-  __TEXT.__auth_stubs: 0x1180
-  __TEXT.__objc_methlist: 0xaeec
-  __TEXT.__const: 0x23e0
-  __TEXT.__gcc_except_tab: 0x24cc
-  __TEXT.__oslogstring: 0xffad
-  __TEXT.__cstring: 0xf34c
+1037.475.9.0.0
+  __TEXT.__text: 0xf9698
+  __TEXT.__auth_stubs: 0x1160
+  __TEXT.__objc_methlist: 0xaf24
+  __TEXT.__const: 0x2230
+  __TEXT.__gcc_except_tab: 0x24ec
+  __TEXT.__oslogstring: 0x1008d
+  __TEXT.__cstring: 0xf077
   __TEXT.__dlopen_cstrs: 0x325
-  __TEXT.__constg_swiftt: 0x2d8
-  __TEXT.__swift5_typeref: 0x2ed
+  __TEXT.__constg_swiftt: 0x2cc
+  __TEXT.__swift5_typeref: 0x2e7
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0xc4
-  __TEXT.__swift5_fieldmd: 0x1cc
-  __TEXT.__swift5_assocty: 0x78
-  __TEXT.__swift5_proto: 0x64
+  __TEXT.__swift5_reflstr: 0xab
+  __TEXT.__swift5_fieldmd: 0x1b4
+  __TEXT.__swift5_assocty: 0x48
+  __TEXT.__swift5_proto: 0x5c
   __TEXT.__swift5_types: 0x34
   __TEXT.__swift5_capture: 0x90
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0x2fa0
+  __TEXT.__unwind_info: 0x3060
   __TEXT.__eh_frame: 0x3e8
-  __TEXT.__objc_classname: 0x1fc6
-  __TEXT.__objc_methname: 0x15e12
-  __TEXT.__objc_methtype: 0x30f8
-  __TEXT.__objc_stubs: 0xc440
+  __TEXT.__objc_classname: 0x20f9
+  __TEXT.__objc_methname: 0x1613f
+  __TEXT.__objc_methtype: 0x3258
+  __TEXT.__objc_stubs: 0xc5c0
   __DATA_CONST.__got: 0xd80
-  __DATA_CONST.__const: 0x3af8
+  __DATA_CONST.__const: 0x3b90
   __DATA_CONST.__objc_classlist: 0x7f8
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4ee8
+  __DATA_CONST.__objc_selrefs: 0x4f20
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x578
   __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__auth_got: 0x8d0
-  __AUTH_CONST.__const: 0x7160
-  __AUTH_CONST.__cfstring: 0xd040
-  __AUTH_CONST.__objc_const: 0x23890
+  __AUTH_CONST.__auth_got: 0x8c0
+  __AUTH_CONST.__const: 0x6b80
+  __AUTH_CONST.__cfstring: 0xd0e0
+  __AUTH_CONST.__objc_const: 0x238a0
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH.__objc_data: 0xbd8
-  __AUTH.__data: 0x1d8
-  __DATA.__objc_ivar: 0xba8
-  __DATA.__data: 0x1a80
-  __DATA.__bss: 0x10a0
-  __DATA.__common: 0x91
-  __DATA_DIRTY.__objc_data: 0x4600
-  __DATA_DIRTY.__data: 0x90
+  __AUTH.__objc_data: 0x998
+  __AUTH.__data: 0x1e8
+  __DATA.__objc_ivar: 0xbac
+  __DATA.__data: 0x1a98
+  __DATA.__bss: 0xfa0
+  __DATA.__common: 0x78
+  __DATA_DIRTY.__objc_data: 0x4830
+  __DATA_DIRTY.__data: 0x88
   __DATA_DIRTY.__bss: 0x200
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: C5CBD734-4D03-3D55-8DC5-DD1DBED244C1
-  Functions: 4946
-  Symbols:   16348
-  CStrings:  9026
+  UUID: A6852DC4-2347-37C9-BCA3-082C7A7FAC68
+  Functions: 4956
+  Symbols:   16666
+  CStrings:  9036
 
Symbols:
+ -[AAAuthenticationResponse cloudKitVideoToken]
+ -[AACustodianController _retryingStartHealthCheckWithCompletion:]
+ -[AASignInFlowController _delegate_presentDataclassActionsForAccount:withAuthResults:completion:]
+ -[AASignInFlowController _delegate_presentDataclassActionsForAccount:withAuthResults:completion:].cold.1
+ -[AASignInFlowController _delegate_presentDataclassActionsForAccount:withAuthResults:completion:].cold.2
+ -[AASignInFlowController _delegate_presentDataclassActionsForAccount:withAuthResults:completion:].cold.3
+ -[AASignInFlowController _onqueue_verifyLoginResponseForiCloudAccount:withAuthResults:withSuccess:error:completion:].cold.1
+ -[AASignInFlowController _previouslySignedOutAccountMatchesAccount:lastSignedOutAccountAltDSID:withAuthResults:]
+ -[AASignInFlowController _previouslySignedOutAccountMatchesAccount:lastSignedOutAccountAltDSID:withAuthResults:].cold.1
+ -[AASignInFlowController _previouslySignedOutAccountMatchesAccount:lastSignedOutAccountAltDSID:withAuthResults:].cold.2
+ -[AASignInFlowController aaAnalyticsRTCReporter]
+ -[AASignInFlowController setAaAnalyticsRTCReporter:]
+ -[ACAccount(AppleAccount) aa_cloudKitVideoToken]
+ -[ACAccount(AppleAccount) aa_setCloudKitVideoToken:]
+ -[NSError(AppleAccount) aa_isXPCConnectionInterruptedError]
+ GCC_except_table106
+ GCC_except_table109
+ GCC_except_table118
+ _OBJC_IVAR_$_AASignInFlowController._aaAnalyticsRTCReporter
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_9
+ __PROTOCOLS_AADOBRepairStateUpdater.2
+ ___103-[AASignInFlowController _delegate_presentGenericTermsUIforAccount:authResults:serverError:completion:]_block_invoke.153
+ ___116-[AASignInFlowController _onqueue_verifyLoginResponseForiCloudAccount:withAuthResults:withSuccess:error:completion:]_block_invoke.111
+ ___116-[AASignInFlowController _onqueue_verifyLoginResponseForiCloudAccount:withAuthResults:withSuccess:error:completion:]_block_invoke.111.cold.1
+ ___116-[AASignInFlowController _onqueue_verifyLoginResponseForiCloudAccount:withAuthResults:withSuccess:error:completion:]_block_invoke.111.cold.2
+ ___131-[AASignInFlowController _onqueue_saveAccount:withAuthResults:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:]_block_invoke.143
+ ___53-[AACustodianController repairCustodians:completion:]_block_invoke.109
+ ___53-[AACustodianController repairCustodians:completion:]_block_invoke.109.cold.1
+ ___53-[AACustodianController repairCustodians:completion:]_block_invoke.110
+ ___53-[AACustodianController repairCustodians:completion:]_block_invoke.110.cold.1
+ ___56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.85
+ ___56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke_2
+ ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.88
+ ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.88.cold.1
+ ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.89
+ ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.89.cold.1
+ ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.107
+ ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.107.cold.1
+ ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.108
+ ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.108.cold.1
+ ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.94
+ ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.94.cold.1
+ ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.95
+ ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.95.cold.1
+ ___65-[AACustodianController _retryingStartHealthCheckWithCompletion:]_block_invoke
+ ___65-[AACustodianController _retryingStartHealthCheckWithCompletion:]_block_invoke.87
+ ___65-[AACustodianController _retryingStartHealthCheckWithCompletion:]_block_invoke.87.cold.1
+ ___65-[AACustodianController _retryingStartHealthCheckWithCompletion:]_block_invoke.cold.1
+ ___66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.111
+ ___66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.111.cold.1
+ ___66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.112
+ ___66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.112.cold.1
+ ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.92
+ ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.92.cold.1
+ ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.93
+ ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.93.cold.1
+ ___71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.90
+ ___71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.90.cold.1
+ ___71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.91
+ ___79-[AASignInFlowController _preflightSaveWithAuthResults:account:withCompletion:]_block_invoke.119
+ ___79-[AASignInFlowController _preflightSaveWithAuthResults:account:withCompletion:]_block_invoke.119.cold.1
+ ___86-[AASignInFlowController _onqueue_enrollCDPStateForAccount:withCDPContext:completion:]_block_invoke.137
+ ___97-[AASignInFlowController _delegate_presentDataclassActionsForAccount:withAuthResults:completion:]_block_invoke
+ ___98-[AASignInFlowController _onqueue_validateAndEnrollCDPStateForAccount:withAuthResults:completion:]_block_invoke.118
+ ___98-[AASignInFlowController _onqueue_validateAndEnrollCDPStateForAccount:withAuthResults:completion:]_block_invoke.118.cold.1
+ ___block_descriptor_32_e17_B16?0"NSError"8l
+ ___block_descriptor_40_e8_32w_e25_v16?0?<v?"NSError">8lw32l8
+ ___block_literal_global.353
+ ___block_literal_global.379
+ ___block_literal_global.449
+ ___block_literal_global.518
+ ___block_literal_global.688
+ ___block_literal_global.765
+ ___block_literal_global.770
+ __privacySensitiveKeys.keysToRedact.350
+ __privacySensitiveKeys.keysToRedact.376
+ __privacySensitiveKeys.keysToRedact.515
+ __privacySensitiveKeys.keysToRedact.685
+ __privacySensitiveKeys.onceToken.351
+ __privacySensitiveKeys.onceToken.377
+ __privacySensitiveKeys.onceToken.516
+ __privacySensitiveKeys.onceToken.686
+ _kAAAnalyticsEventSignInToDifferentAccount
+ _kAAAnalyticsEventSignInToSameAccount
+ _kAAProtocolCloudKitVideoTokenKey
+ _objc_msgSend$_delegate_presentDataclassActionsForAccount:withAuthResults:completion:
+ _objc_msgSend$_previouslySignedOutAccountMatchesAccount:lastSignedOutAccountAltDSID:withAuthResults:
+ _objc_msgSend$_retryingStartHealthCheckWithCompletion:
+ _objc_msgSend$aaAnalyticsRTCReporter
+ _objc_msgSend$aa_cloudKitVideoToken
+ _objc_msgSend$aa_isXPCConnectionInterruptedError
+ _objc_msgSend$aa_setCloudKitVideoToken:
+ _objc_msgSend$cancelButtonText
+ _objc_msgSend$cloudKitVideoToken
+ _objc_msgSend$fetchIdentityFor:completionHandler:
+ _objc_msgSend$initWithCoder:
+ _objc_msgSend$primaryButtonText
+ _objc_msgSend$secondaryButtonText
+ _swift_unknownObjectRelease_n
+ _symbolic _____ 10Foundation20PersonNameComponentsV
+ _symbolic _____ 10Foundation4DataV
- +[AAPreferences shouldEnableFastSignIn]
- -[AASignInFlowController _delegate_presentDataclassActionsForAccount:completion:]
- -[AASignInFlowController _delegate_presentDataclassActionsForAccount:completion:].cold.1
- -[AASignInFlowController _delegate_presentDataclassActionsForAccount:completion:].cold.2
- -[AASignInFlowController _delegate_presentDataclassActionsForAccount:completion:].cold.3
- -[AASignInFlowController _delegate_presentDataclassActionsForAccount:completion:].cold.4
- -[AASignInFlowController _delegate_presentDataclassActionsForAccount:completion:].cold.5
- GCC_except_table105
- GCC_except_table86
- __PROTOCOLS_AADOBRepairStateUpdater.4
- ___103-[AASignInFlowController _delegate_presentGenericTermsUIforAccount:authResults:serverError:completion:]_block_invoke.151
- ___116-[AASignInFlowController _onqueue_verifyLoginResponseForiCloudAccount:withAuthResults:withSuccess:error:completion:]_block_invoke.109
- ___116-[AASignInFlowController _onqueue_verifyLoginResponseForiCloudAccount:withAuthResults:withSuccess:error:completion:]_block_invoke.109.cold.1
- ___116-[AASignInFlowController _onqueue_verifyLoginResponseForiCloudAccount:withAuthResults:withSuccess:error:completion:]_block_invoke.109.cold.2
- ___131-[AASignInFlowController _onqueue_saveAccount:withAuthResults:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:]_block_invoke.141
- ___53-[AACustodianController repairCustodians:completion:]_block_invoke.106
- ___53-[AACustodianController repairCustodians:completion:]_block_invoke.106.cold.1
- ___53-[AACustodianController repairCustodians:completion:]_block_invoke.107
- ___53-[AACustodianController repairCustodians:completion:]_block_invoke.107.cold.1
- ___56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.83.cold.1
- ___56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.84
- ___56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.84.cold.1
- ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.85
- ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.85.cold.1
- ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.86
- ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.86.cold.1
- ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.104
- ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.104.cold.1
- ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.105
- ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.105.cold.1
- ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.91
- ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.91.cold.1
- ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.92
- ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.92.cold.1
- ___66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.108
- ___66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.108.cold.1
- ___66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.109
- ___66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.109.cold.1
- ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.89
- ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.89.cold.1
- ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.90
- ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.90.cold.1
- ___71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.87
- ___71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.87.cold.1
- ___71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.88
- ___79-[AASignInFlowController _preflightSaveWithAuthResults:account:withCompletion:]_block_invoke.117
- ___79-[AASignInFlowController _preflightSaveWithAuthResults:account:withCompletion:]_block_invoke.117.cold.1
- ___81-[AASignInFlowController _delegate_presentDataclassActionsForAccount:completion:]_block_invoke
- ___86-[AASignInFlowController _onqueue_enrollCDPStateForAccount:withCDPContext:completion:]_block_invoke.135
- ___98-[AASignInFlowController _onqueue_validateAndEnrollCDPStateForAccount:withAuthResults:completion:]_block_invoke.116
- ___98-[AASignInFlowController _onqueue_validateAndEnrollCDPStateForAccount:withAuthResults:completion:]_block_invoke.116.cold.1
- ___block_literal_global.351
- ___block_literal_global.377
- ___block_literal_global.447
- ___block_literal_global.516
- ___block_literal_global.686
- ___block_literal_global.763
- ___block_literal_global.768
- __privacySensitiveKeys.keysToRedact.348
- __privacySensitiveKeys.keysToRedact.374
- __privacySensitiveKeys.keysToRedact.513
- __privacySensitiveKeys.keysToRedact.683
- __privacySensitiveKeys.onceToken.349
- __privacySensitiveKeys.onceToken.375
- __privacySensitiveKeys.onceToken.514
- __privacySensitiveKeys.onceToken.684
- __swiftImmortalRefCount
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_delegate_presentDataclassActionsForAccount:completion:
- _objc_retain_x5
- _symbolic SS
- _symbolic _____ 10Foundation4UUIDV
- _symbolic _____Sg 10Foundation4DataV
CStrings:
+ "AASignInFlowController's delegate does not respond to selector: setTelemetryFlowID:"
+ "B16@?0@\"NSError\"8"
+ "B40@0:8@16@24@32"
+ "Cannot call daemon to start health check as custodian controller is deallocated"
+ "Scheduling health check through retry scheduler"
+ "Setting CKVT"
+ "T@\"<AAAnalyticsReporting>\",&,N,V_aaAnalyticsRTCReporter"
+ "^p(0[1-9]|[1-9][0-9]|[1-9][0-9]{2})-setup\\.icloud\\.com(\\.cn)?\\z"
+ "_aaAnalyticsRTCReporter"
+ "_delegate_presentDataclassActionsForAccount:withAuthResults:completion:"
+ "_previouslySignedOutAccountMatchesAccount:lastSignedOutAccountAltDSID:withAuthResults:"
+ "_retryingStartHealthCheckWithCompletion:"
+ "aaAnalyticsRTCReporter"
+ "aa_cloudKitVideoToken"
+ "aa_isXPCConnectionInterruptedError"
+ "aa_setCloudKitVideoToken:"
+ "cloudKitVideoToken"
+ "cloudkit-video-token"
+ "cloudkitVideoToken"
+ "com.apple.appleaccount.signIn.differentAccount"
+ "com.apple.appleaccount.signIn.sameAccount"
+ "fetchIdentityForAccount:withCompletion:"
+ "nameComponents"
+ "setAaAnalyticsRTCReporter:"
+ "setup.icloud.com.cn"
- "FastSignIn"
- "T@\"NSUUID\",N,R"
- "^p(0[1-9]|[1-9][0-9]|[1-9][0-9]{2})-setup\\.icloud\\.com\\z"
- "_delegate_presentDataclassActionsForAccount:completion:"
- "initWithIdentifier:imageData:cropRect:"
- "shouldEnableFastSignIn"

```
