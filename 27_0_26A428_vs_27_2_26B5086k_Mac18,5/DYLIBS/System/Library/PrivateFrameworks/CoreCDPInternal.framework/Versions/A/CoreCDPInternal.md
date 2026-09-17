## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/Versions/A/CoreCDPInternal`

```diff

-447.0.0.0.0
-  __TEXT.__text: 0x918f4
-  __TEXT.__objc_methlist: 0x555c
+448.125.5.1.0
+  __TEXT.__text: 0x93488
+  __TEXT.__objc_methlist: 0x5644
   __TEXT.__const: 0x890
-  __TEXT.__oslogstring: 0x1463a
-  __TEXT.__cstring: 0xdb56
+  __TEXT.__oslogstring: 0x14bda
+  __TEXT.__cstring: 0xe056
   __TEXT.__gcc_except_tab: 0xb1c
   __TEXT.__dlopen_cstrs: 0xbc
   __TEXT.__constg_swiftt: 0x1e4

   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift_as_cont: 0x68
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2e38
+  __TEXT.__unwind_info: 0x2ec8
   __TEXT.__eh_frame: 0x8f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3878
+  __DATA_CONST.__objc_selrefs: 0x3928
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x220
-  __DATA_CONST.__got: 0x10c0
-  __AUTH_CONST.__const: 0x2d90
-  __AUTH_CONST.__cfstring: 0x9140
-  __AUTH_CONST.__objc_const: 0xfb08
+  __DATA_CONST.__got: 0x10f8
+  __AUTH_CONST.__const: 0x2dc0
+  __AUTH_CONST.__cfstring: 0x94c0
+  __AUTH_CONST.__objc_const: 0xfb48
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__auth_got: 0x7f8
+  __AUTH_CONST.__auth_got: 0x800
   __AUTH.__objc_data: 0x120
-  __DATA.__objc_ivar: 0x3a4
+  __DATA.__objc_ivar: 0x3ac
   __DATA.__data: 0x1190
   __DATA_DIRTY.__objc_data: 0x1910
   __DATA_DIRTY.__data: 0x208

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3172
-  Symbols:   5878
-  CStrings:  2756
+  Functions: 3209
+  Symbols:   5939
+  CStrings:  2802
 
Symbols:
+ +[CDPDPCSController _flagsForValidateTelemetry:]
+ +[CDPDPCSController passwordVersionsWereComparedForValidateTelemetry:]
+ +[CDPDPCSController primaryAttemptsRemainingForValidateTelemetry:]
+ +[CDPDPCSController recordGenerationIsAheadOfAccountForValidateTelemetry:]
+ +[CDPDPCSController wrappingKeyNeededRepairForValidateTelemetry:]
+ +[CDPDPCSController wrappingKeyWasRebuiltForValidateTelemetry:]
+ +[CDPDXPCListener _isAppleBinaryOrInternalBuildWithCodeSignFlags:isInternalBuild:]
+ -[CDPContext(Daemon) hasConfirmedPDPIneligibility]
+ -[CDPDPDPRecoveryController retirePDPFollowUpIfAccountConfirmedIneligible]
+ -[CDPDStateMachine _attemptLegacyIntermissionFallbackWithCompletion:]
+ -[CDPDStateMachine _attemptNativeIntermissionSalvageAfterSetupError:completion:]
+ -[CDPDStateMachine _attemptPreOctagonPDPSetupWithCompletion:continuation:]
+ -[CDPDStateMachine _finishSignInWithSecretTeardownShouldComplete:cloudDataProtectionEnabled:error:completion:]
+ -[CDPDStateMachine _makeDeferredSOSStateMachineWithContext:]
+ -[CDPDStateMachine _markRepairPairReported]
+ -[CDPDStateMachine _sendDBRDetectionEventsWithDetails:healthState:]
+ -[CDPDStateMachine _sendDBRRepairEntryEventWithDetails:validationError:includeRepairContext:]
+ -[CDPDXPCListener _isAppleBinaryOrInternalBuildConnection:]
+ GCC_except_table128
+ GCC_except_table60
+ OBJC_IVAR_$_CDPDStateMachine._pdpDetectionEventsAlreadySent
+ OBJC_IVAR_$_CDPDStateMachine._pdpRepairPairAlreadySent
+ _OUTLINED_FUNCTION_11
+ _SecTaskGetCodeSignStatus
+ __110-[CDPDStateMachine _finishSignInWithSecretTeardownShouldComplete:cloudDataProtectionEnabled:error:completion:]_block_invoke
+ __69-[CDPDStateMachine _attemptLegacyIntermissionFallbackWithCompletion:]_block_invoke
+ __70-[CDPDClientHandler setUserVisibleKeychainSyncEnabled:withCompletion:]_block_invoke
+ __74-[CDPDStateMachine _attemptPreOctagonPDPSetupWithCompletion:continuation:]_block_invoke
+ __77-[CDPDClientHandler removeNonViewAwarePeersFromCircleWithContext:completion:]_block_invoke
+ __80-[CDPDStateMachine _attemptNativeIntermissionSalvageAfterSetupError:completion:]_block_invoke
+ __OBJC_$_CLASS_METHODS_CDPDPCSController
+ ___110-[CDPDStateMachine _finishSignInWithSecretTeardownShouldComplete:cloudDataProtectionEnabled:error:completion:]_block_invoke
+ ___69-[CDPDStateMachine _attemptLegacyIntermissionFallbackWithCompletion:]_block_invoke
+ ___74-[CDPDStateMachine _attemptPreOctagonPDPSetupWithCompletion:continuation:]_block_invoke
+ ___80-[CDPDStateMachine _attemptNativeIntermissionSalvageAfterSetupError:completion:]_block_invoke
+ ___block_descriptor_57_e8_32s40s48bs_e20_v20?0"NSError"8B16l
+ ___block_descriptor_64_e8_32s40s48bs56bs_e20_v20?0"NSError"8B16l
+ _kCDPAnalyticsPDPRecordGenerationAheadEvent
+ _kCDPAnalyticsPDPRecordGenerationCheckSkippedEvent
+ _kCDPAnalyticsPDPWrappingKeyRepairEvent
+ _kPCSDBRTelemetryFlags
+ _kPCSDBRTelemetryLocalPasswordVersion
+ _kPCSDBRTelemetryPrimaryAttemptsRemaining
+ _kPCSDBRTelemetryRecordPasswordVersion
+ _objc_msgSend$_attemptLegacyIntermissionFallbackWithCompletion:
+ _objc_msgSend$_attemptNativeIntermissionSalvageAfterSetupError:completion:
+ _objc_msgSend$_attemptPreOctagonPDPSetupWithCompletion:continuation:
+ _objc_msgSend$_finishSignInWithSecretTeardownShouldComplete:cloudDataProtectionEnabled:error:completion:
+ _objc_msgSend$_flagsForValidateTelemetry:
+ _objc_msgSend$_isAppleBinaryOrInternalBuildConnection:
+ _objc_msgSend$_isAppleBinaryOrInternalBuildWithCodeSignFlags:isInternalBuild:
+ _objc_msgSend$_makeDeferredSOSStateMachineWithContext:
+ _objc_msgSend$_markRepairPairReported
+ _objc_msgSend$_sendDBRDetectionEventsWithDetails:healthState:
+ _objc_msgSend$_sendDBRRepairEntryEventWithDetails:validationError:includeRepairContext:
+ _objc_msgSend$hasConfirmedPDPIneligibility
+ _objc_msgSend$isDBRInlineSignInHealEnabled
+ _objc_msgSend$isEntitlementEnforcementEnabled
+ _objc_msgSend$multiUserManateeAllowed
+ _objc_msgSend$passwordVersionsWereComparedForValidateTelemetry:
+ _objc_msgSend$populateDBRDetectionDetailWithRemainingAttempts:detectionError:
+ _objc_msgSend$primaryAttemptsRemainingForValidateTelemetry:
+ _objc_msgSend$recordGenerationIsAheadOfAccountForValidateTelemetry:
+ _objc_msgSend$retirePDPFollowUpIfAccountConfirmedIneligible
+ _objc_msgSend$wrappingKeyNeededRepairForValidateTelemetry:
+ _objc_msgSend$wrappingKeyWasRebuiltForValidateTelemetry:
- GCC_except_table130
- GCC_except_table59
- ___70-[CDPDClientHandler setUserVisibleKeychainSyncEnabled:withCompletion:]_block_invoke_2
- ___77-[CDPDClientHandler removeNonViewAwarePeersFromCircleWithContext:completion:]_block_invoke_2
- ___block_descriptor_56_e8_32s40s48bs_e20_v20?0"NSError"8B16l
CStrings:
+ "CDPDStateMachine: Active PDP user PDP fallback failed — blocking sign-in directly (bypassing localCompletion head)"
+ "CDPDStateMachine: Attempting native intermission for active DBR user"
+ "CDPDStateMachine: Attempting post-Octagon PDP setup"
+ "CDPDStateMachine: Intermission ineligible (non-active PDP user): %@"
+ "CDPDStateMachine: Native intermission succeeded, processing temporary stingray record"
+ "CDPDStateMachine: Post-Octagon PDP fallback should not be attempted on HomePod"
+ "CDPDStateMachine: Skipping post-Octagon PDP setup due to forced Manatee reset"
+ "CDPDStateMachine: TTSU recovery, bypassing password-based PDP setup; routing to native intermission"
+ "CDPDStateMachine: post-Octagon setupPDPState did %@ set up with error=%@"
+ "Denying hasLocalSecret: missing cdp.utility entitlement."
+ "Denying isICDPEnabledForDSID: missing cdp.utility entitlement."
+ "Denying isUserVisibleKeychainSyncEnabled: missing cdp.statemachine entitlement."
+ "Denying new connection %@: caller is not an Apple-signed binary or an internal build."
+ "Denying removeNonViewAwarePeersFromCircle: missing cdp.statemachine entitlement."
+ "Denying setUserVisibleKeychainSyncEnabled: missing cdp.statemachine entitlement."
+ "Denying synchronizeUserVisibleKeychainSyncEligibility: missing cdp.statemachine entitlement."
+ "Denying verifyRecoveryKeyObservingSystemsHaveMatchingState: missing cdp.recoverykey entitlement."
+ "PDP: Account is ineligible for PDP, retiring the PDP repair CFU it can no longer satisfy"
+ "PDP: Cannot attribute the PDP repair CFU to this account, leaving it in place"
+ "RUIHTTPRequestErrorDomain"
+ "ak-button"
+ "com.apple.appleaccounttransparency.cachedEventsFetched"
+ "com.apple.appleaccounttransparency.metadataGenerated"
+ "com.apple.appleaccounttransparency.metadataGenerated.hook"
+ "com.apple.appleaccounttransparency.pushReceived"
+ "com.apple.appleaccounttransparency.syncTriggered"
+ "com.apple.authkit.TDIDTrustLoss"
+ "com.apple.authkit.TDLChangePushReceived"
+ "com.apple.authkit.TDLTDIDAvailability"
+ "com.apple.authkit.signoutEnd"
+ "com.apple.authkit.signoutStart"
+ "com.apple.remoteUI.loadURLComplete"
+ "com.apple.remoteui.appleid_settings_account_manage_security"
+ "com.apple.remoteui.appleid_settings_account_manage_security_password"
+ "com.apple.remoteui.appleid_settings_account_manage_security_password_put"
+ "com.apple.remoteui.appleid_settings_account_manage_security_password_signout_put"
+ "com.apple.remoteui.auth"
+ "com.apple.remoteui.auth_verify_passcode"
+ "com.apple.remoteui.auth_verify_phone_1_put"
+ "com.apple.remoteui.auth_verify_phone_securitycode"
+ "com.apple.security.RKSponsorSelection"
+ "com.apple.security.TLKProofInvalid"
+ "com.apple.security.anyPotentialRKSponsorsWithFlagSet"
+ "com.apple.security.joinWithCircleReset"
+ "com.apple.security.prepareTDIDPresence"
+ "com.apple.security.recoverRKTLKShares.fetchRKTLKSharesForRecovery"
+ "com.apple.security.recoverRKTLKShares.recoveredRKTLKShares"
+ "com.apple.security.tdlTDIDDuplicates"
+ "com.apple.security.tdlTDIDReappearance"
+ "com.apple.security.tdlTDIDStability"
+ "com.apple.security.vouchWithRecoveryKeyOperation"
- "CDPDStateMachine: PDP fallback (native intermission) should not be attempted on HomePod"
- "com.apple.authkit.StableIDAvailability"
- "com.apple.authkit.TDIDAvailability"
- "com.apple.authkit.TDIDAvailability.signin"
- "com.apple.authkit.TDIDAvailability.upgrade"
```
