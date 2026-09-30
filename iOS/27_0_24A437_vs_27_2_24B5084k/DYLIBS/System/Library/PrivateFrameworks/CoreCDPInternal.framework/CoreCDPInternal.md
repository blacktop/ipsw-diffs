## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-447.0.0.0.0
-  __TEXT.__text: 0x8bb58
-  __TEXT.__objc_methlist: 0x568c
+448.125.5.1.0
+  __TEXT.__text: 0x8d554
+  __TEXT.__objc_methlist: 0x5774
   __TEXT.__const: 0x888
-  __TEXT.__oslogstring: 0x14a9e
-  __TEXT.__cstring: 0xe0c5
+  __TEXT.__oslogstring: 0x1503e
+  __TEXT.__cstring: 0xe5b5
   __TEXT.__gcc_except_tab: 0xb68
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x3b7

   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift_as_cont: 0x68
-  __TEXT.__unwind_info: 0x2e28
+  __TEXT.__unwind_info: 0x2eb8
   __TEXT.__eh_frame: 0x8f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x25c8
+  __DATA_CONST.__const: 0x2608
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3908
+  __DATA_CONST.__objc_selrefs: 0x39b8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x220
-  __DATA_CONST.__got: 0x10f0
+  __DATA_CONST.__got: 0x1128
   __AUTH_CONST.__const: 0xad0
-  __AUTH_CONST.__cfstring: 0x9520
-  __AUTH_CONST.__objc_const: 0x100b0
+  __AUTH_CONST.__cfstring: 0x98a0
+  __AUTH_CONST.__objc_const: 0x100f0
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__auth_got: 0x960
+  __AUTH_CONST.__auth_got: 0x968
   __AUTH.__objc_data: 0x120
-  __DATA.__objc_ivar: 0x3b0
+  __DATA.__objc_ivar: 0x3b8
   __DATA.__data: 0x1220
   __DATA_DIRTY.__objc_data: 0x19b0
   __DATA_DIRTY.__data: 0x200

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3159
-  Symbols:   5798
-  CStrings:  2809
+  Functions: 3196
+  Symbols:   5858
+  CStrings:  2855
 
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
+ GCC_except_table120
+ GCC_except_table34
+ GCC_except_table48
+ _OBJC_IVAR_$_CDPDStateMachine._pdpDetectionEventsAlreadySent
+ _OBJC_IVAR_$_CDPDStateMachine._pdpRepairPairAlreadySent
+ _SecTaskGetCodeSignStatus
+ __OBJC_$_CLASS_METHODS_CDPDPCSController
+ ___110-[CDPDStateMachine _finishSignInWithSecretTeardownShouldComplete:cloudDataProtectionEnabled:error:completion:]_block_invoke
+ ___69-[CDPDStateMachine _attemptLegacyIntermissionFallbackWithCompletion:]_block_invoke
+ ___74-[CDPDStateMachine _attemptPreOctagonPDPSetupWithCompletion:continuation:]_block_invoke
+ ___80-[CDPDStateMachine _attemptNativeIntermissionSalvageAfterSetupError:completion:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e37_v32?0Q8"NSDictionary"16"NSError"24ls32l8s40l8
+ ___block_descriptor_57_e8_32s40s48bs_e20_v20?0"NSError"8B16ls48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56bs_e20_v20?0"NSError"8B16ls32l8s40l8s48l8s56l8
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAVFoundation_$_CoreCDPInternal
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_CoreCDPInternal
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftIntents_$_CoreCDPInternal
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
- GCC_except_table121
- GCC_except_table35
- GCC_except_table47
- ___70-[CDPDClientHandler setUserVisibleKeychainSyncEnabled:withCompletion:]_block_invoke_2
- ___77-[CDPDClientHandler removeNonViewAwarePeersFromCircleWithContext:completion:]_block_invoke_2
- ___block_descriptor_48_e8_32s40bs_e37_v32?0Q8"NSDictionary"16"NSError"24ls40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e20_v20?0"NSError"8B16ls32l8s40l8s48l8
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
