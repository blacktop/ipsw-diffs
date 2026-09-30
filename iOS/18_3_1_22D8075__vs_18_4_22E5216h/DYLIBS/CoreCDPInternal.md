## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-386.234.0.0.0
-  __TEXT.__text: 0x8db54
-  __TEXT.__auth_stubs: 0x1130
-  __TEXT.__objc_methlist: 0x4474
-  __TEXT.__const: 0x720
-  __TEXT.__oslogstring: 0x13568
-  __TEXT.__cstring: 0x7675
-  __TEXT.__gcc_except_tab: 0xbac
+386.455.0.0.0
+  __TEXT.__text: 0x8d460
+  __TEXT.__auth_stubs: 0x10f0
+  __TEXT.__objc_methlist: 0x52e4
+  __TEXT.__const: 0x734
+  __TEXT.__oslogstring: 0x13428
+  __TEXT.__cstring: 0x8895
+  __TEXT.__gcc_except_tab: 0xba4
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__swift5_typeref: 0x301
-  __TEXT.__swift5_fieldmd: 0x8c
-  __TEXT.__constg_swiftt: 0x1b0
-  __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0x79
-  __TEXT.__swift5_assocty: 0x90
+  __TEXT.__swift5_typeref: 0x341
+  __TEXT.__swift5_fieldmd: 0x80
+  __TEXT.__constg_swiftt: 0x1d0
+  __TEXT.__swift5_builtin: 0x78
+  __TEXT.__swift5_reflstr: 0x6e
+  __TEXT.__swift5_assocty: 0xa8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_proto: 0x40
-  __TEXT.__swift5_types: 0x20
+  __TEXT.__swift5_proto: 0x44
+  __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_capture: 0x1b8
-  __TEXT.__unwind_info: 0x1c90
-  __TEXT.__eh_frame: 0x8e0
+  __TEXT.__swift_as_entry: 0x5c
+  __TEXT.__swift_as_ret: 0x60
+  __TEXT.__unwind_info: 0x1ca0
+  __TEXT.__eh_frame: 0x9a0
   __TEXT.__objc_classname: 0xc79
-  __TEXT.__objc_methname: 0xeb56
-  __TEXT.__objc_methtype: 0x28e1
-  __TEXT.__objc_stubs: 0xbea0
-  __DATA_CONST.__got: 0x1000
-  __DATA_CONST.__const: 0x2588
+  __TEXT.__objc_methname: 0xea53
+  __TEXT.__objc_methtype: 0x284c
+  __TEXT.__objc_stubs: 0xbde0
+  __DATA_CONST.__got: 0xff0
+  __DATA_CONST.__const: 0x2490
   __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3520
+  __DATA_CONST.__objc_selrefs: 0x3598
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x160
-  __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0x8a8
-  __AUTH_CONST.__auth_ptr: 0x1d8
-  __AUTH_CONST.__const: 0x9e8
-  __AUTH_CONST.__cfstring: 0x4e60
-  __AUTH_CONST.__objc_const: 0x116c8
+  __DATA_CONST.__objc_arraydata: 0x90
+  __AUTH_CONST.__auth_got: 0x888
+  __AUTH_CONST.__auth_ptr: 0x1f0
+  __AUTH_CONST.__const: 0xaf8
+  __AUTH_CONST.__cfstring: 0x5920
+  __AUTH_CONST.__objc_const: 0xfa80
   __AUTH_CONST.__objc_intobj: 0x180
-  __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x10a0
+  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH.__objc_data: 0x1050
   __AUTH.__data: 0x58
-  __DATA.__objc_ivar: 0x3a0
-  __DATA.__data: 0x1288
-  __DATA.__bss: 0x840
-  __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x920
-  __DATA_DIRTY.__data: 0x58
-  __DATA_DIRTY.__bss: 0x120
+  __DATA.__objc_ivar: 0x39c
+  __DATA.__data: 0x12a8
+  __DATA.__bss: 0x8a0
+  __DATA_DIRTY.__objc_data: 0x970
+  __DATA_DIRTY.__data: 0x68
+  __DATA_DIRTY.__bss: 0x138
+  __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3016
-  Symbols:   3832
-  CStrings:  4721
+  Functions: 3012
+  Symbols:   3834
+  CStrings:  4775
 
Symbols:
+ _CDPRecoveryStatusFromOTRecoveryStatus
+ _FLNotificationOptionKeepOnLockscreen
+ _kCDPAnalyticsEscrowRecordCreationStartEvent
- _kCDPAnalyticsFetchCustodianRecoveryInfoEvent
- _kCDPAnalyticsRecoveryCreateSessionEvent
- _kCDPAnalyticsValidateRecoveryCodeEvent
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
- "Calling enable without delete due to existing record metadata being present"
- "Check for existing backup failed with error: %@"
- "CheckForExistingRecord"
- "CheckForExistingRecordMatchingPredicate"
- "CheckForExistingRecordWithPeerId"
- "Checking for existing records before enabling secure backup..."
- "Checking if the peer has a secure backup: %@"
- "Denying access to fetchEDPRecoveryToken due to edp ineligiblity with value: %@"
- "FOLLOWUP_VERIFY_PASSCODE_MESSAGE"
- "FOLLOWUP_VERIFY_PASSCODE_NOTIFICATION_MESSAGE"
- "Failed to check for existing records before enabling secure backup with error: %@"
- "Fatal error"
- "Found %@ matching devices"
- "Insufficient space allocated to copy string contents"
- "No existing backup record found, continuing with enable"
- "REBRAND"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "TB,V_requiresEscrowRecordsFetch"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_REBRAND"
- "_requiresEscrowRecordsFetch"
- "checkAndRemoveExistingThenEnableSecureBackupRecordWithContext:completion:"
- "checkForExistingRecord:"
- "checkForExistingRecordMatchingPredicate:forceFetch:completion:"
- "checkForExistingRecordWithPeerId:completion:"
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
- "requiresEscrowRecordsFetch"
- "setRequiresEscrowRecordsFetch:"
- "v24@0:8@?<v@?@\"CDPDevice\"@\"NSError\">16"
- "v32@0:8@\"NSString\"16@?<v@?@\"CDPDevice\"@\"NSError\">24"
- "v36@0:8@\"NSPredicate\"16B24@?<v@?@\"CDPDevice\"@\"NSError\">28"

```
