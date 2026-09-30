## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/Versions/A/CoreCDPInternal`

```diff

-386.234.0.0.0
-  __TEXT.__text: 0x97548
-  __TEXT.__auth_stubs: 0xef0
-  __TEXT.__objc_methlist: 0x4364
-  __TEXT.__const: 0x722
-  __TEXT.__oslogstring: 0x1311a
-  __TEXT.__cstring: 0x7103
+386.457.0.0.0
+  __TEXT.__text: 0x983f4
+  __TEXT.__auth_stubs: 0xeb0
+  __TEXT.__objc_methlist: 0x5254
+  __TEXT.__const: 0x712
+  __TEXT.__oslogstring: 0x1316a
+  __TEXT.__cstring: 0x8373
   __TEXT.__gcc_except_tab: 0xb58
   __TEXT.__dlopen_cstrs: 0xbc
-  __TEXT.__constg_swiftt: 0x1b0
-  __TEXT.__swift5_typeref: 0x302
-  __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0x79
-  __TEXT.__swift5_fieldmd: 0x8c
-  __TEXT.__swift5_assocty: 0x90
-  __TEXT.__swift5_proto: 0x40
-  __TEXT.__swift5_types: 0x20
+  __TEXT.__constg_swiftt: 0x1d0
+  __TEXT.__swift5_typeref: 0x342
+  __TEXT.__swift5_builtin: 0x78
+  __TEXT.__swift5_reflstr: 0x6e
+  __TEXT.__swift5_fieldmd: 0x80
+  __TEXT.__swift5_assocty: 0xa8
+  __TEXT.__swift5_proto: 0x44
+  __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_capture: 0x1b8
+  __TEXT.__swift_as_entry: 0x5c
+  __TEXT.__swift_as_ret: 0x60
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1cc0
-  __TEXT.__eh_frame: 0x8e0
+  __TEXT.__unwind_info: 0x1ce8
+  __TEXT.__eh_frame: 0x9a0
   __TEXT.__objc_classname: 0xc2e
-  __TEXT.__objc_methname: 0xe838
+  __TEXT.__objc_methname: 0xe879
   __TEXT.__objc_methtype: 0x28b7
-  __TEXT.__objc_stubs: 0xbb80
-  __DATA_CONST.__got: 0xfd0
-  __DATA_CONST.__const: 0x590
+  __TEXT.__objc_stubs: 0xbba0
+  __DATA_CONST.__got: 0xfc0
+  __DATA_CONST.__const: 0x510
   __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3480
+  __DATA_CONST.__objc_selrefs: 0x3528
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x150
-  __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0x788
-  __AUTH_CONST.__const: 0x2bb8
-  __AUTH_CONST.__cfstring: 0x4a80
-  __AUTH_CONST.__objc_const: 0x11100
+  __DATA_CONST.__objc_arraydata: 0x90
+  __AUTH_CONST.__auth_got: 0x768
+  __AUTH_CONST.__const: 0x2c98
+  __AUTH_CONST.__cfstring: 0x55a0
+  __AUTH_CONST.__objc_const: 0xf588
   __AUTH_CONST.__objc_intobj: 0x168
-  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x980
   __AUTH.__data: 0x88
   __DATA.__objc_ivar: 0x394
-  __DATA.__data: 0x1250
-  __DATA.__bss: 0x910
+  __DATA.__data: 0x1270
+  __DATA.__bss: 0x990
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xfa0
   __DATA_DIRTY.__bss: 0x48

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 5CD52EFC-2005-3503-B839-FF2AE49E6257
-  Functions: 3032
-  Symbols:   6807
-  CStrings:  5218
+  UUID: DF8B8758-BF5A-3730-BD4D-4425144FC6D4
+  Functions: 3051
+  Symbols:   6841
+  CStrings:  5382
 
Symbols:
+ +[CDPDAnalyticsTransport approvedRecoveryContactEventsForADPAndDNU]
+ +[CDPDAnalyticsTransport getAllowedCfuType].cold.1
+ +[CDPDAnalyticsTransport getAllowedErrorDomain].cold.1
+ +[CDPDAnalyticsTransport getAllowedEscapeOffer].cold.1
+ +[CDPDAnalyticsTransport getAllowedLocalSecretType].cold.1
+ +[CDPDAnalyticsTransport getAllowedSecurityEvents].cold.1
+ +[CDPDAnalyticsTransport getAllowedStringsForTelemetry].cold.1
+ +[CDPDAnalyticsTransport transportForClientType:clientBundleId:clientName:].cold.2
+ +[CDPDEDPRecoveryTokenSynchronizeActivity sharedActivity].cold.1
+ +[CDPDFollowUpController _identifiersAllowedForTelemetry].cold.1
+ +[CDPDFollowUpController sharedInstance].cold.1
+ +[CDPDFollowUpFactory contextToIdentifierMap].cold.1
+ +[CDPDKeychainSync _defaultUserVisibleViewSet].cold.1
+ +[CDPDNetworkObserver sharedInstance].cold.1
+ +[CDPDSecureBackupConfiguration configurationWithContext:].cold.1
+ +[CDPDXPCListener sharedInstance].cold.1
+ +[CDPPiggybackingPayloadProvider proxyWithContext:error:]
+ +[CDPRecoveryKeyCache sharedInstance].cold.1
+ -[CDPDAnalyticsTransport sendEvent:].cold.3
+ -[CDPDEDPRecoveryController performInteractiveEDPRepairWithCompletion:]
+ -[CDPDEDPRecoveryController performInteractiveEDPRepairWithCompletion:].cold.1
+ -[CDPDPCSController _shoudAllowKeyFetchForService:].cold.1
+ -[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:].cold.3
+ CDPRecoveryStatusFromOTRecoveryStatus.cold.1
+ GCC_except_table12
+ GCC_except_table51
+ _CDPRecoveryStatusFromOTRecoveryStatus
+ _FLNotificationOptionKeepOnLockscreen
+ __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.910
+ __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.910.cold.1
+ __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.911
+ __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.911.cold.1
+ __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.974
+ __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.974.cold.1
+ __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.974.cold.2
+ __65-[CDPDClientHandler attemptToEscrowPreRecord:context:completion:]_block_invoke.76
+ __71-[CDPDEDPRecoveryController performInteractiveEDPRepairWithCompletion:]_block_invoke.cold.1
+ __71-[CDPDEDPRecoveryController performInteractiveEDPRepairWithCompletion:]_block_invoke.cold.2
+ __73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.53
+ __73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.53.cold.1
+ __73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.53.cold.2
+ __73-[CDPDClientHandler shouldPerformRepairForContext:forceFetch:completion:]_block_invoke.73
+ __79-[CDPDClientHandler fetchEscrowRecordDevicesWithContext:usingCache:completion:]_block_invoke.34
+ __81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.975
+ __81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.979
+ __81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.979.cold.1
+ __83-[CDPDClientHandler localSecretChangedTo:secretType:context:uiProvider:completion:]_block_invoke.77
+ __85-[CDPDClientHandler _startObservingConnectionStateForRepairWithStateMachine:context:]_block_invoke.68
+ __85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.78
+ __85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.78.cold.1
+ __85-[CDPDClientHandler handleCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.56
+ __85-[CDPDClientHandler repairCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.61
+ __86-[CDPDClientHandler shouldPerformAuthenticatedRepairForContext:forceFetch:completion:]_block_invoke.74
+ __89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.79
+ __89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.79.cold.1
+ ___71-[CDPDEDPRecoveryController performInteractiveEDPRepairWithCompletion:]_block_invoke
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_memcpy0_1
+ ___swift_project_boxed_opaque_existential_0
+ __block_literal_global.721
+ __block_literal_global.732
+ __block_literal_global.734
+ __block_literal_global.835
+ __block_literal_global.882
+ __block_literal_global.894
+ __block_literal_global.907
+ __block_literal_global.981
+ _kCDPAnalyticsEscrowRecordCreationStartEvent
+ _objc_msgSend$approvedRecoveryContactEventsForADPAndDNU
+ _objc_msgSend$hasSecureBackupUsesMultipleIcscs
+ _objc_msgSend$performInteractiveEDPRepairWithCompletion:
+ _objc_msgSend$proxyWithContext:error:
+ _objc_msgSend$sessionWithCircleDelegate:session:altDSID:flowID:deviceSessionID:error:
+ _symbolic SccySDySS___________pGSg______pG So14NSSecureCodingP So8NSObjectP s5ErrorP
+ _symbolic SccySb______pG s5ErrorP
+ _symbolic Sccy__________G So17CDPEDPHealthStateV s5NeverO
+ _symbolic _____ So17CDPEDPHealthStateV
+ _symbolic _____So7NSErrorCSgIeyByy_Sg So10CDPRPDTypeV
+ block_copy_helper.106
+ block_copy_helper.15
+ block_copy_helper.18
+ block_copy_helper.21
+ block_copy_helper.25
+ block_copy_helper.85
+ block_copy_helper.95
+ block_descriptor.108
+ block_descriptor.20
+ block_descriptor.23
+ block_descriptor.27
+ block_descriptor.87
+ block_descriptor.97
+ block_destroy_helper.107
+ block_destroy_helper.16
+ block_destroy_helper.19
+ block_destroy_helper.22
+ block_destroy_helper.26
+ block_destroy_helper.86
+ block_destroy_helper.96
- +[CDPPiggybackingPayloadProvider proxyWithSession:error:]
- -[CDPDEDPRecoveryController performInitialInteractiveEDPRepairWithCompletion:]
- -[CDPDEDPRecoveryController performInitialInteractiveEDPRepairWithCompletion:].cold.1
- -[CDPDSecureBackupProxyImpl enableWithInfo:completionBlock:]
- GCC_except_table16
- GCC_except_table50
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.633
- __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.633.cold.1
- __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.634
- __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.634.cold.1
- __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.697
- __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.697.cold.1
- __36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.697.cold.2
- __65-[CDPDClientHandler attemptToEscrowPreRecord:context:completion:]_block_invoke.75
- __73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.52
- __73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.52.cold.1
- __73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.52.cold.2
- __73-[CDPDClientHandler shouldPerformRepairForContext:forceFetch:completion:]_block_invoke.72
- __78-[CDPDEDPRecoveryController performInitialInteractiveEDPRepairWithCompletion:]_block_invoke.cold.1
- __78-[CDPDEDPRecoveryController performInitialInteractiveEDPRepairWithCompletion:]_block_invoke.cold.2
- __79-[CDPDClientHandler fetchEscrowRecordDevicesWithContext:usingCache:completion:]_block_invoke.33
- __81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.698
- __81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.702
- __81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.702.cold.1
- __83-[CDPDClientHandler localSecretChangedTo:secretType:context:uiProvider:completion:]_block_invoke.76
- __85-[CDPDClientHandler _startObservingConnectionStateForRepairWithStateMachine:context:]_block_invoke.67
- __85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.77
- __85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.77.cold.1
- __85-[CDPDClientHandler handleCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.55
- __85-[CDPDClientHandler repairCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.60
- __86-[CDPDClientHandler shouldPerformAuthenticatedRepairForContext:forceFetch:completion:]_block_invoke.73
- __89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.78
- __89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.78.cold.1
- ___60-[CDPDSecureBackupProxyImpl enableWithInfo:completionBlock:]_block_invoke
- ___78-[CDPDEDPRecoveryController performInitialInteractiveEDPRepairWithCompletion:]_block_invoke
- ___block_descriptor_64_e8_32s40bs_e17_v16?0"NSError"8l
- ___swift_destroy_boxed_opaque_existential_1
- ___swift_memcpy1_1
- __block_literal_global.444
- __block_literal_global.455
- __block_literal_global.457
- __block_literal_global.558
- __block_literal_global.605
- __block_literal_global.617
- __block_literal_global.630
- __block_literal_global.704
- _kCDPAnalyticsFetchCustodianRecoveryInfoEvent
- _kCDPAnalyticsRecoveryCreateSessionEvent
- _kCDPAnalyticsValidateRecoveryCodeEvent
- _objc_msgSend$containsString:
- _objc_msgSend$enableWithCompletionBlock:
- _objc_msgSend$performInitialInteractiveEDPRepairWithCompletion:
- _objc_msgSend$proxyWithSession:error:
- _symbolic _____So7NSErrorCSgIeyByy_ So10CDPRPDTypeV
- _symbolic ______pSg 15CoreCDPInternal12EscrowRecordP
- block_copy_helper.104
- block_copy_helper.93
- block_descriptor.106
- block_descriptor.15
- block_descriptor.16
- block_descriptor.19
- block_descriptor.85
- block_descriptor.95
- block_destroy_helper.105
- block_destroy_helper.94
CStrings:
+ "/System/AppleInternal/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication"
+ "/System/AppleInternal/Library/Frameworks/UserManagement.framework/UserManagement"
+ "ACCOUNT_RECOVERY_HARD_LIMIT_REACHED_MESSAGE_GLOBAL_REBRAND"
+ "ACCOUNT_RECOVERY_HARD_LIMIT_REACHED_MESSAGE_SINGLE_REBRAND"
+ "CDPDRecoveryValidatedJoinFlowController: Did not request reset. Canceling flow."
+ "Denying access to fetchEDPRecoveryToken due to edp ineligibility with value: %@"
+ "FOLLOWUP_VERIFY_PASSCODE_MESSAGE_REBRAND"
+ "FOLLOWUP_VERIFY_PASSCODE_NOTIFICATION_MESSAGE_REBRAND"
+ "Unexpected Octagon recovery status found (%@), defaulting to `CDPRecoveryStatusValid`"
+ "approvedRecoveryContactEventsForADPAndDNU"
+ "com.apple.appleaccount.custodian.accountRecovery"
+ "com.apple.appleaccount.custodian.dataRecovery"
+ "com.apple.appleaccount.custodian.decodeIDSMessage"
+ "com.apple.appleaccount.custodian.healthcheck.custodian"
+ "com.apple.appleaccount.custodian.healthcheck.incompleteinvitation.custodianResendInvitationAcceptanceMessage"
+ "com.apple.appleaccount.custodian.healthcheck.owner"
+ "com.apple.appleaccount.custodian.healthcheck.owner.confirmCustodianWithServer"
+ "com.apple.appleaccount.custodian.healthcheck.owner.finalizeSetupWithServer"
+ "com.apple.appleaccount.custodian.healthcheck.owner.sendRecoveryInfoMessage"
+ "com.apple.appleaccount.custodian.healthcheck.ownerUpdatedCustodianRecord"
+ "com.apple.appleaccount.custodian.recovery.cancel"
+ "com.apple.appleaccount.custodian.recovery.experimental.deviceHasCachedCustodianList"
+ "com.apple.appleaccount.custodian.recovery.experimental.recoveryInfoNotFoundFetchFromCloud"
+ "com.apple.appleaccount.custodian.recovery.fetchAPSToken"
+ "com.apple.appleaccount.custodian.recovery.initializeSessionWithServer"
+ "com.apple.appleaccount.custodian.recovery.ownerCreateSession"
+ "com.apple.appleaccount.custodian.recovery.ownerFetchCustodianRecoveryKeys"
+ "com.apple.appleaccount.custodian.recovery.ownerValidateCode"
+ "com.apple.appleaccount.custodian.setup.acceptSharedRecoveryInfo"
+ "com.apple.appleaccount.custodian.setup.accountEligibilityCheck"
+ "com.apple.appleaccount.custodian.setup.accountNotEligible"
+ "com.apple.appleaccount.custodian.setup.cleanup.deleteCustodianshipRecordFromCloud"
+ "com.apple.appleaccount.custodian.setup.cleanup.deleteRecoveryKeyByCustodianIDFromSecurity"
+ "com.apple.appleaccount.custodian.setup.cleanup.deleteRecoveryKeyByOctagonIDFromSecurity"
+ "com.apple.appleaccount.custodian.setup.cleanup.revokeCustodianFromServer"
+ "com.apple.appleaccount.custodian.setup.custodianUpdatedCustodianshipRecord"
+ "com.apple.appleaccount.custodian.setup.familyMemberCheck"
+ "com.apple.appleaccount.custodian.setup.finalizeSetupWithServer"
+ "com.apple.appleaccount.custodian.setup.invitationProcessedForManualAccept"
+ "com.apple.appleaccount.custodian.setup.newCustodian"
+ "com.apple.appleaccount.custodian.setup.ownerGenerateCustodianRecoveryKey"
+ "com.apple.appleaccount.custodian.setup.ownerGenerateEncryptedCPRK"
+ "com.apple.appleaccount.custodian.setup.ownerStoredCustodianRecordToCloud"
+ "com.apple.appleaccount.custodian.setup.ownerUpdatedCustodianRecord"
+ "com.apple.appleaccount.custodian.setup.processAccept.createRecoveryInfoShare"
+ "com.apple.appleaccount.custodian.setup.processAccept.fetchRecoveryInfo"
+ "com.apple.appleaccount.custodian.setup.processAccept.sendRecoveryInfoMessage"
+ "com.apple.appleaccount.custodian.setup.processDecline.cleanup"
+ "com.apple.appleaccount.custodian.setup.processFinalizeSetupMessage"
+ "com.apple.appleaccount.custodian.setup.processInvitation"
+ "com.apple.appleaccount.custodian.setup.processInvitationAcceptanceResponse"
+ "com.apple.appleaccount.custodian.setup.processInvitationDeclineResponse"
+ "com.apple.appleaccount.custodian.setup.processNotReachable"
+ "com.apple.appleaccount.custodian.setup.processRemoveCustodian"
+ "com.apple.appleaccount.custodian.setup.processSharedRecoveryInfo"
+ "com.apple.appleaccount.custodian.setup.remove.sendRemovalMessageToCustodian"
+ "com.apple.appleaccount.custodian.setup.resendInvitation"
+ "com.apple.appleaccount.custodian.setup.respondToInvite"
+ "com.apple.appleaccount.custodian.setup.sendAutoAcceptInvitationMessage"
+ "com.apple.appleaccount.custodian.setup.sendFinalizeSetupMessage"
+ "com.apple.appleaccount.custodian.setup.sendInvitation"
+ "com.apple.appleaccount.custodian.setup.sendInvitationAcceptanceMessage"
+ "com.apple.appleaccount.custodian.setup.sendInvitationDeclineMessage"
+ "com.apple.appleaccount.custodian.setup.stopBeingCustodian"
+ "com.apple.appleaccount.custodian.setup.storeInvitationToCloud"
+ "com.apple.appleaccount.custodian.systemSync"
+ "com.apple.appleaccount.custodian.ui.exitAccountRecovery"
+ "com.apple.appleaccount.custodian.ui.exitCustodianDetails"
+ "com.apple.appleaccount.custodian.ui.openAccountRecovery"
+ "com.apple.appleaccount.custodian.ui.openCustodianDetails"
+ "com.apple.appleaccount.fetchUserInfo"
+ "com.apple.sbd.recoverEscrowWithRequest"
+ "com.apple.sbd.recoverWithRequest"
+ "com.apple.sbd.remoteEscrowRestore"
+ "com.apple.sbd.silentBurn"
+ "com.apple.sbd.sortEscrowRecordsForMatchingPassphrase"
+ "com.apple.security.establish"
+ "com.apple.security.establishOperation"
+ "com.apple.security.fetchAfterEstablish"
+ "com.apple.security.fetchRecoverableTLKShares"
+ "com.apple.security.handleRecoveryResults"
+ "com.apple.security.initiatorJoinSOS"
+ "com.apple.security.joinWithVoucher"
+ "com.apple.security.joinWithVoucherInTPH"
+ "com.apple.security.joinWithVoucherOperation"
+ "com.apple.security.onqueueEstablishTPH"
+ "com.apple.security.performEscrowRecovery"
+ "com.apple.security.performSilentEscrowRecovery"
+ "com.apple.security.piggybackingAcceptorInitialMessage"
+ "com.apple.security.piggybackingAcceptorProcessApplication"
+ "com.apple.security.piggybackingAcceptorProcessMessage"
+ "com.apple.security.piggybackingCircleInitiatorHandleCircleBlobMessage"
+ "com.apple.security.piggybackingCircleInitiatorInitialMessage"
+ "com.apple.security.piggybackingSessionInitiatorHandleChallenge]"
+ "com.apple.security.piggybackingSessionInitiatorHandleVerification]"
+ "com.apple.security.piggybackingSessionInitiatorInitialMessage"
+ "com.apple.security.preflightVouchWithBottle"
+ "com.apple.security.recoverSilentWithCDPContext"
+ "com.apple.security.recoverWithCDPContext"
+ "com.apple.security.recoverWithInfo"
+ "com.apple.security.recoveryResultsResetAndEstablish"
+ "com.apple.security.restoreFromBottleEvent"
+ "com.apple.security.restoreKeychainAsyncWithPassword"
+ "com.apple.security.vouchWithBottle"
+ "com.apple.security.vouchWithBottleTPH"
+ "hasSecureBackupUsesMultipleIcscs"
+ "init()"
+ "performInteractiveEDPRepairWithCompletion:"
+ "proxyWithContext:error:"
+ "sessionWithCircleDelegate:session:altDSID:flowID:deviceSessionID:error:"
- "AABranding"
- "ACCOUNT_RECOVERY_HARD_LIMIT_REACHED_MESSAGE_GLOBAL"
- "ACCOUNT_RECOVERY_HARD_LIMIT_REACHED_MESSAGE_SINGLE"
- "CDPDRecoveryValidatedJoinFlowController: UI Provider is nil, only option is to cancel flow"
- "Denying access to fetchEDPRecoveryToken due to edp ineligiblity with value: %@"
- "FOLLOWUP_VERIFY_PASSCODE_MESSAGE"
- "FOLLOWUP_VERIFY_PASSCODE_NOTIFICATION_MESSAGE"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "REBRAND"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_REBRAND"
- "com.apple.appleaccount.CustodianRecovery"
- "com.apple.security.initaitorJoinSOS"
- "com.apple.security.join"
- "com.apple.security.trustedDeviceListRefresh"
- "containsString:"
- "enableWithCompletionBlock:"
- "enableWithInfo:completionBlock:"
- "invalid Collection: less than 'count' elements in collection"
- "performInitialInteractiveEDPRepairWithCompletion:"
- "proxyWithSession:error:"

```
