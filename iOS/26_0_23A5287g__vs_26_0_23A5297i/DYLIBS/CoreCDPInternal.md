## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-409.0.0.0.0
-  __TEXT.__text: 0x922d4
+410.1.0.0.0
+  __TEXT.__text: 0x927f8
   __TEXT.__auth_stubs: 0x1110
-  __TEXT.__objc_methlist: 0x552c
+  __TEXT.__objc_methlist: 0x5534
   __TEXT.__const: 0x8c4
-  __TEXT.__oslogstring: 0x14066
-  __TEXT.__cstring: 0xcdfe
+  __TEXT.__oslogstring: 0x14096
+  __TEXT.__cstring: 0xdaae
   __TEXT.__gcc_except_tab: 0xc84
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x341

   __TEXT.__unwind_info: 0x1d48
   __TEXT.__eh_frame: 0x8d0
   __TEXT.__objc_classname: 0xcbd
-  __TEXT.__objc_methname: 0xf2b6
+  __TEXT.__objc_methname: 0xf30c
   __TEXT.__objc_methtype: 0x2987
-  __TEXT.__objc_stubs: 0xc4c0
-  __DATA_CONST.__got: 0x1090
+  __TEXT.__objc_stubs: 0xc500
+  __DATA_CONST.__got: 0x1098
   __DATA_CONST.__const: 0x2630
   __DATA_CONST.__objc_classlist: 0x288
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3770
+  __DATA_CONST.__objc_selrefs: 0x3780
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x168
-  __DATA_CONST.__objc_arraydata: 0x90
+  __DATA_CONST.__objc_arraydata: 0xd0
   __AUTH_CONST.__auth_got: 0x898
   __AUTH_CONST.__const: 0xbc8
-  __AUTH_CONST.__cfstring: 0x8280
+  __AUTH_CONST.__cfstring: 0x8ac0
   __AUTH_CONST.__objc_const: 0xfc90
   __AUTH_CONST.__objc_intobj: 0x180
-  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0xfd8
   __AUTH.__data: 0x58
   __DATA.__objc_ivar: 0x3b0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: AAFB9023-E95B-3560-B042-15195567BE9F
-  Functions: 3111
-  Symbols:   10061
-  CStrings:  6264
+  UUID: 060FB4CE-1A08-3C8D-A0FE-E9CB1BA6C65C
+  Functions: 3113
+  Symbols:   10068
+  CStrings:  6399
 
Symbols:
+ -[CDPDAnalyticsTransport _renewMissingDeviceSessionIDIfNeeded:manager:account:]
+ -[CDPDAnalyticsTransport _renewMissingDeviceSessionIDIfNeeded:manager:account:].cold.1
+ _AKTelemetryMissingDeviceSessionID
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2116
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2116.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2117
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2117.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2180
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2180.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2180.cold.2
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.2181
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2183
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2183.cold.1
+ ___block_literal_global.1011
+ ___block_literal_global.1022
+ ___block_literal_global.1126
+ ___block_literal_global.1173
+ ___block_literal_global.1253
+ ___block_literal_global.1282
+ ___block_literal_global.2085
+ ___block_literal_global.2097
+ ___block_literal_global.2113
+ ___block_literal_global.2185
+ ___block_literal_global.508
+ _objc_msgSend$_renewMissingDeviceSessionIDIfNeeded:manager:account:
+ _objc_msgSend$renewDeviceSessionIDForAccount:
- GCC_except_table54
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1915
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1915.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1916
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1916.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1979
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1979.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1979.cold.2
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.1980
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.1982
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.1982.cold.1
- ___block_literal_global.1052
- ___block_literal_global.1081
- ___block_literal_global.1884
- ___block_literal_global.1896
- ___block_literal_global.1912
- ___block_literal_global.1984
- ___block_literal_global.496
- ___block_literal_global.813
- ___block_literal_global.824
- ___block_literal_global.925
- ___block_literal_global.972
CStrings:
+ "AACustodianSystemStateError"
+ "Renewing missing device session ID for event: %@"
+ "_renewMissingDeviceSessionIDIfNeeded:manager:account:"
+ "com.apple.appleaccount.custodian.setup.askedToPresentUpsellByServer"
+ "com.apple.appleaccount.custodian.setup.fetchSuggestedContacts.signpost.begin"
+ "com.apple.appleaccount.custodian.setup.fetchSuggestedContactsFromDeviceIntelligence"
+ "com.apple.appleaccount.custodian.setup.fetchSuggestedContactsFromFamilyMembers"
+ "com.apple.appleaccount.custodian.setup.newCustodian.signpost.begin"
+ "com.apple.appleaccount.custodian.setup.processFinalizeSetupMessage.begin"
+ "com.apple.appleaccount.custodian.setup.processInvitation.signpost.begin"
+ "com.apple.appleaccount.custodian.setup.processInvitationResponse.signpost.begin"
+ "com.apple.appleaccount.custodian.setup.processSharedRecoveryInfosignpost.begin"
+ "com.apple.appleaccount.custodian.setup.respondToInvite.signpost.begin"
+ "com.apple.appleaccount.custodian.setup.success"
+ "com.apple.appleaccount.custodian.setupFailSafe"
+ "com.apple.appleaccount.custodian.setupFailSafe.gracePeriodExpired"
+ "com.apple.appleaccount.custodian.setupFailSafe.healthCheckRun"
+ "com.apple.appleaccount.custodian.setupFailSafe.pending"
+ "com.apple.appleaccount.custodian.setupFailSafe.ready"
+ "com.apple.appleaccount.custodian.setupFailSafe.tearDown"
+ "com.apple.appleaccount.custodian.ui.setup.presentSuggestedContactList"
+ "com.apple.appleaccount.custodian.ui.setup.skippedSuggestionList"
+ "com.apple.appleaccount.custodian.ui.setup.userSelectSuggestedContactFromDeviceIntelligence"
+ "com.apple.appleaccount.custodian.ui.setup.userSelectSuggestedContactFromFamily"
+ "com.apple.authkit.authMasterKey"
+ "com.apple.authkit.authMasterKeyStart"
+ "com.apple.authkit.authServerUI"
+ "com.apple.authkit.authServerUIStart"
+ "com.apple.authkit.authentication"
+ "com.apple.authkit.authenticationStart"
+ "com.apple.authkit.biometricAuth"
+ "com.apple.authkit.deviceAuth"
+ "com.apple.authkit.deviceAuthStart"
+ "com.apple.authkit.federatedAuth"
+ "com.apple.authkit.federatedAuthStart"
+ "com.apple.authkit.interactiveAuth"
+ "com.apple.authkit.interactiveAuthStart"
+ "com.apple.authkit.passcodeAuth"
+ "com.apple.authkit.passwordlessAuth"
+ "com.apple.authkit.passwordlessAuthStart"
+ "com.apple.authkit.piggybackingAccepting"
+ "com.apple.authkit.piggybackingAcceptingStart"
+ "com.apple.authkit.piggybackingCancellation"
+ "com.apple.authkit.piggybackingCircleRequest"
+ "com.apple.authkit.piggybackingCircleRequestStart"
+ "com.apple.authkit.piggybackingEscapeHatch"
+ "com.apple.authkit.piggybackingProcessPushPayload"
+ "com.apple.authkit.piggybackingProcessPushPayloadStart"
+ "com.apple.authkit.piggybackingProximityDetection"
+ "com.apple.authkit.piggybackingProximityDetectionStart"
+ "com.apple.authkit.piggybackingRequesting"
+ "com.apple.authkit.piggybackingRequestingStart"
+ "com.apple.authkit.piggybackingSecretGeneration"
+ "com.apple.authkit.piggybackingVerificationFailure"
+ "com.apple.authkit.secondFactorPrompt"
+ "com.apple.authkit.secondFactorPromptStart"
+ "com.apple.authkit.secondFactorValidation"
+ "com.apple.authkit.secondFactorValidationStart"
+ "com.apple.authkit.securityUpgrade"
+ "com.apple.authkit.securityUpgradeStart"
+ "com.apple.authkit.shouldContinueAuth"
+ "com.apple.authkit.shouldContinueAuthStart"
+ "com.apple.authkit.srpAuthentication"
+ "com.apple.authkit.srpAuthenticationStart"
+ "com.apple.security.acceptorChannelSecured"
+ "com.apple.security.acceptorPreVersion3Change"
+ "com.apple.security.initiatorChannelSecured"
+ "com.apple.security.initiatorPreVersion3Change"
+ "renewDeviceSessionIDForAccount:"

```
