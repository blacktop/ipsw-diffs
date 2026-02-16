## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-416.325.4.0.0
-  __TEXT.__text: 0x91800
-  __TEXT.__auth_stubs: 0x11d0
-  __TEXT.__objc_methlist: 0x5584
+416.475.8.0.0
+  __TEXT.__text: 0x954bc
+  __TEXT.__auth_stubs: 0x1150
+  __TEXT.__objc_methlist: 0x55ec
   __TEXT.__const: 0x830
-  __TEXT.__oslogstring: 0x1425e
-  __TEXT.__cstring: 0xda65
-  __TEXT.__gcc_except_tab: 0xc38
+  __TEXT.__oslogstring: 0x1460e
+  __TEXT.__cstring: 0xd5c5
+  __TEXT.__gcc_except_tab: 0xc5c
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x385
   __TEXT.__swift5_fieldmd: 0x80

   __TEXT.__swift5_capture: 0x200
   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
-  __TEXT.__unwind_info: 0x1d48
-  __TEXT.__eh_frame: 0x910
-  __TEXT.__objc_classname: 0xcca
-  __TEXT.__objc_methname: 0xf3ec
-  __TEXT.__objc_methtype: 0x281e
-  __TEXT.__objc_stubs: 0xc520
+  __TEXT.__unwind_info: 0x1f48
+  __TEXT.__eh_frame: 0x958
+  __TEXT.__objc_classname: 0xdbd
+  __TEXT.__objc_methname: 0xf90f
+  __TEXT.__objc_methtype: 0x2a77
+  __TEXT.__objc_stubs: 0xcb60
   __DATA_CONST.__got: 0x1088
-  __DATA_CONST.__const: 0x2528
+  __DATA_CONST.__const: 0x2548
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3818
+  __DATA_CONST.__objc_selrefs: 0x3878
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0xd8
-  __AUTH_CONST.__auth_got: 0x8f8
-  __AUTH_CONST.__const: 0xad0
-  __AUTH_CONST.__cfstring: 0x8bc0
-  __AUTH_CONST.__objc_const: 0x10060
+  __AUTH_CONST.__auth_got: 0x8b8
+  __AUTH_CONST.__const: 0xab0
+  __AUTH_CONST.__cfstring: 0x8da0
+  __AUTH_CONST.__objc_const: 0x10070
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH.__objc_data: 0x1070
   __AUTH.__data: 0x58
   __DATA.__objc_ivar: 0x3ac
-  __DATA.__data: 0x1270
-  __DATA.__bss: 0x4e0
+  __DATA.__data: 0x1230
+  __DATA.__bss: 0x4c0
   __DATA_DIRTY.__objc_data: 0xa60
-  __DATA_DIRTY.__data: 0x140
-  __DATA_DIRTY.__bss: 0x168
+  __DATA_DIRTY.__data: 0x180
+  __DATA_DIRTY.__bss: 0x178
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CCB7BF63-5AB3-3527-8B2A-00E568697E75
-  Functions: 3094
-  Symbols:   10032
-  CStrings:  6437
+  UUID: CFEA817A-42C9-367B-A877-BA7914268893
+  Functions: 3128
+  Symbols:   10328
+  CStrings:  6470
 
Symbols:
+ -[CDPDClientHandler generatePDPBlobWithContext:completion:]
+ -[CDPDClientHandler generatePDPBlobWithContext:completion:].cold.1
+ -[CDPDClientHandler generatePDPBlobWithContext:completion:].cold.2
+ -[CDPDClientHandler generatePDPBlobWithContext:completion:].cold.3
+ -[CDPDClientHandler generatePDPBlobWithContext:completion:].cold.4
+ -[CDPDPCSController generatePDPBlobWithCompletion:]
+ -[CDPDPCSController generatePDPBlobWithCompletion:].cold.1
+ -[CDPDPCSController generatePDPBlobWithCompletion:].cold.2
+ -[CDPDPCSController generatePDPBlobWithCompletion:].cold.3
+ -[CDPDPCSController healBrokenADPEnablementWithCompletion:]
+ -[CDPDPCSController healBrokenADPEnablementWithCompletion:].cold.1
+ -[CDPDPCSController healBrokenADPEnablementWithCompletion:].cold.2
+ -[CDPDPCSController healBrokenADPEnablementWithCompletion:].cold.3
+ -[CDPDPDPRecoveryController _postPDPRepairFollowUp]
+ -[CDPDPDPRecoveryController _postPDPRepairFollowUp].cold.1
+ -[CDPDPDPRecoveryController _postPDPRepairFollowUp].cold.2
+ -[CDPDPDPRecoveryController performADPEnablementHealingWithCompletion:]
+ -[CDPDPDPRecoveryController performADPEnablementHealingWithCompletion:].cold.1
+ -[CDPDPDPRecoveryController performADPEnablementHealingWithCompletion:].cold.2
+ -[CDPDPDPRecoveryController performADPEnablementHealingWithCompletion:].cold.3
+ -[CDPDStateMachine repairCloudDataProtectionStateWithCompletion:].cold.2
+ -[CDPInternalWalrusStateController _containsPCSError:inError:]
+ -[CDPInternalWalrusStateController _createPDPPasswordRequiredErrorWithUnderlyingError:]
+ -[CDPInternalWalrusStateController _isDroppedKeysSuccessForEnablement:error:]
+ -[CDPInternalWalrusStateController _retryWalrusStateUpdate:context:account:completion:]
+ -[CDPInternalWalrusStateController _shouldPromptForPasswordWithError:context:]
+ GCC_except_table120
+ GCC_except_table31
+ GCC_except_table35
+ GCC_except_table40
+ GCC_except_table46
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ ___119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.173
+ ___156-[CDPDStateMachine _attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.175
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2183
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2183.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2184
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2184.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2247
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2247.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2247.cold.2
+ ___38-[CDPDStateMachine _attemptCDPEnable:]_block_invoke.113
+ ___51-[CDPDPCSController generatePDPBlobWithCompletion:]_block_invoke
+ ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.106
+ ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.107
+ ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.110
+ ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.110.cold.1
+ ___56-[CDPDStateMachine _attemptPDPFallbackForProximityFlow:]_block_invoke.199
+ ___58-[CDPDStateMachine _handleBeneficiaryTrustWithCompletion:]_block_invoke.88
+ ___59-[CDPDClientHandler generatePDPBlobWithContext:completion:]_block_invoke
+ ___59-[CDPDPCSController healBrokenADPEnablementWithCompletion:]_block_invoke
+ ___59-[CDPDPCSController healBrokenADPEnablementWithCompletion:]_block_invoke.cold.1
+ ___59-[CDPDPCSController healBrokenADPEnablementWithCompletion:]_block_invoke.cold.2
+ ___62-[CDPDPDPRecoveryController _interactiveRepairWithCompletion:]_block_invoke.77
+ ___62-[CDPDPDPRecoveryController _interactiveRepairWithCompletion:]_block_invoke.77.cold.1
+ ___62-[CDPDPDPRecoveryController _interactiveRepairWithCompletion:]_block_invoke.77.cold.2
+ ___65-[CDPDClientHandler attemptToEscrowPreRecord:context:completion:]_block_invoke.82
+ ___65-[CDPDPDPRecoveryController _silentPasswordChangeWithCompletion:]_block_invoke.70
+ ___65-[CDPDPDPRecoveryController _silentPasswordChangeWithCompletion:]_block_invoke.70.cold.1
+ ___65-[CDPDPDPRecoveryController validatePDPIdentitiesWithCompletion:]_block_invoke.80
+ ___65-[CDPDPDPRecoveryController validatePDPIdentitiesWithCompletion:]_block_invoke.80.cold.1
+ ___65-[CDPDPDPRecoveryController validatePDPIdentitiesWithCompletion:]_block_invoke.80.cold.2
+ ___65-[CDPDPDPRecoveryController validatePDPIdentitiesWithCompletion:]_block_invoke.80.cold.3
+ ___65-[CDPDPDPRecoveryController validatePDPIdentitiesWithCompletion:]_block_invoke.80.cold.4
+ ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.111
+ ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.111.cold.1
+ ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.100
+ ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.101
+ ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.103
+ ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.99
+ ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.99.cold.1
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.51
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.54
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.62
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.65
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.72
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.72.cold.1
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.79
+ ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.79.cold.1
+ ___65-[CDPDStateMachine repairCloudDataProtectionStateWithCompletion:]_block_invoke.154
+ ___66-[CDPDPDPRecoveryController silentlyRepairPDPStateWithCompletion:]_block_invoke.72
+ ___66-[CDPDPDPRecoveryController silentlyRepairPDPStateWithCompletion:]_block_invoke.72.cold.1
+ ___66-[CDPDStateMachine _handleCloudDataProtectionStateWithCompletion:]_block_invoke.85
+ ___66-[CDPDStateMachine _handleCloudDataProtectionStateWithCompletion:]_block_invoke.86
+ ___71-[CDPDPDPRecoveryController performADPEnablementHealingWithCompletion:]_block_invoke
+ ___71-[CDPDPDPRecoveryController performADPEnablementHealingWithCompletion:]_block_invoke.89
+ ___71-[CDPDPDPRecoveryController performADPEnablementHealingWithCompletion:]_block_invoke.89.cold.1
+ ___71-[CDPDPDPRecoveryController performADPEnablementHealingWithCompletion:]_block_invoke.89.cold.2
+ ___71-[CDPDPDPRecoveryController performADPEnablementHealingWithCompletion:]_block_invoke.89.cold.3
+ ___71-[CDPDPDPRecoveryController performADPEnablementHealingWithCompletion:]_block_invoke.89.cold.4
+ ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.184.cold.1
+ ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.185
+ ___72-[CDPDStateMachine _recoverSecureBackupWithCircleJoinResult:completion:]_block_invoke.160
+ ___73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.52
+ ___73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.52.cold.1
+ ___73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.52.cold.2
+ ___73-[CDPDClientHandler shouldPerformRepairForContext:forceFetch:completion:]_block_invoke.79
+ ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.180.cold.1
+ ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.180.cold.2
+ ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.181
+ ___80-[CDPDClientHandler startCircleApplicationApprovalServerWithContext:completion:]_block_invoke.69
+ ___80-[CDPDClientHandler startCircleApplicationApprovalServerWithContext:completion:]_block_invoke_2.70
+ ___80-[CDPDStateMachine _continueShouldPerformRepairWithOptionForceFetch:completion:]_block_invoke.137
+ ___80-[CDPDStateMachine _continueShouldPerformRepairWithOptionForceFetch:completion:]_block_invoke.138
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.2248
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2250
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2250.cold.1
+ ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.161
+ ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.161.cold.1
+ ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.163
+ ___83-[CDPDClientHandler localSecretChangedTo:secretType:context:uiProvider:completion:]_block_invoke.83
+ ___85-[CDPDClientHandler _startObservingConnectionStateForRepairWithStateMachine:context:]_block_invoke.74
+ ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.84
+ ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.84.cold.1
+ ___85-[CDPDClientHandler handleCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.56
+ ___85-[CDPDClientHandler repairCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.58
+ ___85-[CDPDStateMachine _attemptBeneficiaryTrustWithInheritanceKey:retryCount:completion:]_block_invoke.97
+ ___86-[CDPDClientHandler shouldPerformAuthenticatedRepairForContext:forceFetch:completion:]_block_invoke.80
+ ___87-[CDPInternalWalrusStateController _retryWalrusStateUpdate:context:account:completion:]_block_invoke
+ ___87-[CDPInternalWalrusStateController _retryWalrusStateUpdate:context:account:completion:]_block_invoke.cold.1
+ ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.85
+ ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.85.cold.1
+ ___block_descriptor_48_e8_32bs40r_e20_v20?0B8"NSError"12lr40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e20_v20?0B8"NSError"12lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e20_v24?0q8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e20_v24?0q8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48r_e31_v16?0"CDPStateHandlerResult"8ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e31_v16?0"CDPStateHandlerResult"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e20_v24?0q8"NSError"16ls32l8s40l8s48l8
+ ___block_literal_global.1046
+ ___block_literal_global.1057
+ ___block_literal_global.1161
+ ___block_literal_global.1208
+ ___block_literal_global.1243
+ ___block_literal_global.1320
+ ___block_literal_global.1349
+ ___block_literal_global.147
+ ___block_literal_global.2152
+ ___block_literal_global.2164
+ ___block_literal_global.2180
+ ___block_literal_global.2252
+ ___block_literal_global.534
+ ___block_literal_global.67
+ _kCDPAnalyticsADPHealingEvent
+ _objc_msgSend$_containsPCSError:inError:
+ _objc_msgSend$_createPDPPasswordRequiredErrorWithUnderlyingError:
+ _objc_msgSend$_isDroppedKeysSuccessForEnablement:error:
+ _objc_msgSend$_postPDPRepairFollowUp
+ _objc_msgSend$_retryWalrusStateUpdate:context:account:completion:
+ _objc_msgSend$_shouldPromptForPasswordWithError:context:
+ _objc_msgSend$authenticateWithContext:completion:
+ _objc_msgSend$bootSessionID
+ _objc_msgSend$build
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$currentDeviceUnlockedForTheFirstTime
+ _objc_msgSend$currentLockState
+ _objc_msgSend$deviceDidUnlockForTheFirstTime
+ _objc_msgSend$escapeOffersPresented
+ _objc_msgSend$fetchAllEscrowRecords:error:
+ _objc_msgSend$fetchEscrowRecords:error:
+ _objc_msgSend$generatePDPBlob:completion:
+ _objc_msgSend$generatePDPBlobWithCompletion:
+ _objc_msgSend$hasBuild
+ _objc_msgSend$hasDeviceMid
+ _objc_msgSend$hasLabel
+ _objc_msgSend$hasRecordId
+ _objc_msgSend$hasSerialNumber
+ _objc_msgSend$hasValue
+ _objc_msgSend$healBrokenADPEnablementWithAccountIdentifier:parameters:completion:
+ _objc_msgSend$healBrokenADPEnablementWithCompletion:
+ _objc_msgSend$initWithDeviceStatus:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithRecordPresence:isValid:recordId:buildVersion:isForCurrentDevice:hasMachineId:recordViability:localSecretViability:tlkRecoveryViability:sosViability:pcsRecoveryViability:
+ _objc_msgSend$initWithUserDefaults:urlBag:localDevice:bootSessionID:
+ _objc_msgSend$isDBRTwoEnabled
+ _objc_msgSend$isForCurrentDevice
+ _objc_msgSend$isManateeNotificationOnFirstUnlockEnabledUsingURLBag:completion:
+ _objc_msgSend$listeners
+ _objc_msgSend$localDevice
+ _objc_msgSend$localSecretGeneration
+ _objc_msgSend$manateeRPDBlockingError
+ _objc_msgSend$passcodeGeneration
+ _objc_msgSend$pdpPCSDBRRepairIdentities:completion:
+ _objc_msgSend$reactTo:
+ _objc_msgSend$recognizeFirstUnlockWith:
+ _objc_msgSend$recordIsValid
+ _objc_msgSend$rpdBlockingError
+ _objc_msgSend$rpdProbationDuration
+ _objc_msgSend$rpdProbationIsInEffectForDuration:context:
+ _objc_msgSend$savedBootSessionID
+ _objc_msgSend$setListeners:
+ _objc_msgSend$srpVerifier
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$updateSavedBootSessionIDTo:
+ _objc_msgSend$urlBag
+ _objc_msgSend$userDefaults
- -[CDPDFollowUpFactory followUpItemWithContext:].cold.3
- -[CDPDPDPRecoveryController _clearAllPDPFollowUps]
- -[CDPDPDPRecoveryController _clearAllPDPFollowUps].cold.1
- -[CDPDPDPRecoveryController _interactiveRepairWithCompletion:].cold.1
- -[CDPDPDPRecoveryController _postRepairPDPCDPFollowUp]
- -[CDPDPDPRecoveryController _postRepairPDPCDPFollowUp].cold.1
- -[CDPDPDPRecoveryController _postRepairPDPCDPFollowUp].cold.2
- -[CDPDPDPRecoveryController clearCDPPDPFollowUp]
- -[CDPDPDPRecoveryController clearCDPPDPFollowUp].cold.1
- -[CDPDPDPRecoveryController clearCDPPDPFollowUp].cold.2
- -[CDPDPDPRecoveryController performInteractivePDPRepairWithCompletion:].cold.2
- -[CDPDPDPRecoveryController repairPDPStateWithCompletion:].cold.3
- -[CDPDPDPRecoveryController silentlyRepairPDPStateWithCompletion:].cold.1
- -[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:].cold.4
- GCC_except_table121
- GCC_except_table29
- GCC_except_table36
- GCC_except_table64
- GCC_except_table74
- GCC_except_table79
- _CDP_FOLLOWUP_CDP_PDP_REPAIR
- ___119-[CDPDStateMachine _attemptBackupRecoveryWithLocalSecret:type:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.170
- ___156-[CDPDStateMachine _attemptBackupRecoveryByPromptingForRemoteSecretWithLocalSecret:localSecretType:useSecureBackupCachedSecret:circleJoinResult:completion:]_block_invoke.174
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2162
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2162.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2163
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2163.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2226
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2226.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2226.cold.2
- ___38-[CDPDStateMachine _attemptCDPEnable:]_block_invoke.118
- ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.111
- ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.112
- ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.115
- ___55-[CDPDStateMachine resetAccountCDPStateWithCompletion:]_block_invoke.115.cold.1
- ___56-[CDPDStateMachine _attemptPDPFallbackForProximityFlow:]_block_invoke.198
- ___58-[CDPDStateMachine _handleBeneficiaryTrustWithCompletion:]_block_invoke.93
- ___62-[CDPDPDPRecoveryController _interactiveRepairWithCompletion:]_block_invoke.78
- ___62-[CDPDPDPRecoveryController _interactiveRepairWithCompletion:]_block_invoke.78.cold.1
- ___62-[CDPDPDPRecoveryController _interactiveRepairWithCompletion:]_block_invoke.78.cold.2
- ___65-[CDPDClientHandler attemptToEscrowPreRecord:context:completion:]_block_invoke.81
- ___65-[CDPDPDPRecoveryController _silentPasswordChangeWithCompletion:]_block_invoke.71
- ___65-[CDPDPDPRecoveryController _silentPasswordChangeWithCompletion:]_block_invoke.71.cold.1
- ___65-[CDPDPDPRecoveryController validatePDPIdentitiesWithCompletion:]_block_invoke.81
- ___65-[CDPDPDPRecoveryController validatePDPIdentitiesWithCompletion:]_block_invoke.81.cold.1
- ___65-[CDPDPDPRecoveryController validatePDPIdentitiesWithCompletion:]_block_invoke.81.cold.2
- ___65-[CDPDPDPRecoveryController validatePDPIdentitiesWithCompletion:]_block_invoke.81.cold.3
- ___65-[CDPDPDPRecoveryController validatePDPIdentitiesWithCompletion:]_block_invoke.81.cold.4
- ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.116
- ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.116.cold.1
- ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.104
- ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.104.cold.1
- ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.105
- ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.106
- ___65-[CDPDStateMachine _enrollOrDisableCDPAfterEnabledStateVerified:]_block_invoke.108
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.52
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.55
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.60
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.68
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.75
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.77
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.77.cold.1
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.84
- ___65-[CDPDStateMachine handleCloudDataProtectionStateWithCompletion:]_block_invoke.84.cold.1
- ___65-[CDPDStateMachine repairCloudDataProtectionStateWithCompletion:]_block_invoke.153
- ___65-[CDPDStateMachine repairCloudDataProtectionStateWithCompletion:]_block_invoke.153.cold.1
- ___65-[CDPDStateMachine repairCloudDataProtectionStateWithCompletion:]_block_invoke.153.cold.2
- ___65-[CDPDStateMachine repairCloudDataProtectionStateWithCompletion:]_block_invoke.cold.2
- ___66-[CDPDPDPRecoveryController silentlyRepairPDPStateWithCompletion:]_block_invoke.73
- ___66-[CDPDPDPRecoveryController silentlyRepairPDPStateWithCompletion:]_block_invoke.73.cold.1
- ___66-[CDPDStateMachine _handleCloudDataProtectionStateWithCompletion:]_block_invoke.90
- ___66-[CDPDStateMachine _handleCloudDataProtectionStateWithCompletion:]_block_invoke.91
- ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.182
- ___71-[CDPDStateMachine _enableSecureBackupWithCircleJoinResult:completion:]_block_invoke.183.cold.1
- ___72-[CDPDStateMachine _recoverSecureBackupWithCircleJoinResult:completion:]_block_invoke.159
- ___73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.50
- ___73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.50.cold.1
- ___73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.50.cold.2
- ___73-[CDPDClientHandler shouldPerformRepairForContext:forceFetch:completion:]_block_invoke.78
- ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.179
- ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.179.cold.1
- ___74-[CDPDStateMachine _postRecoveryEnableSecureBackupWithContext:completion:]_block_invoke.179.cold.2
- ___80-[CDPDClientHandler startCircleApplicationApprovalServerWithContext:completion:]_block_invoke.68
- ___80-[CDPDClientHandler startCircleApplicationApprovalServerWithContext:completion:]_block_invoke_2.69
- ___80-[CDPDStateMachine _continueShouldPerformRepairWithOptionForceFetch:completion:]_block_invoke.142
- ___80-[CDPDStateMachine _continueShouldPerformRepairWithOptionForceFetch:completion:]_block_invoke.143
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.2227
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2229
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2229.cold.1
- ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.160
- ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.160.cold.1
- ___82-[CDPDStateMachine _handleInteractiveRecoveryFlowWithCircleJoinResult:completion:]_block_invoke.162
- ___82-[CDPInternalWalrusStateController _updateWalrusState:context:account:completion:]_block_invoke
- ___82-[CDPInternalWalrusStateController _updateWalrusState:context:account:completion:]_block_invoke.cold.1
- ___83-[CDPDClientHandler localSecretChangedTo:secretType:context:uiProvider:completion:]_block_invoke.82
- ___85-[CDPDClientHandler _startObservingConnectionStateForRepairWithStateMachine:context:]_block_invoke.73
- ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.83
- ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.83.cold.1
- ___85-[CDPDClientHandler handleCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.54
- ___85-[CDPDClientHandler repairCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.57
- ___85-[CDPDStateMachine _attemptBeneficiaryTrustWithInheritanceKey:retryCount:completion:]_block_invoke.102
- ___86-[CDPDClientHandler shouldPerformAuthenticatedRepairForContext:forceFetch:completion:]_block_invoke.79
- ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.84
- ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.84.cold.1
- ___block_descriptor_48_e8_32bs40w_e20_v24?0Q8"NSError"16lw40l8s32l8
- ___block_descriptor_49_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs48w_e20_v24?0Q8"NSError"16lw48l8s40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e20_v24?0Q8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_57_e8_32s40bs48r_e31_v16?0"CDPStateHandlerResult"8ls32l8r48l8s40l8
- ___block_descriptor_57_e8_32s40bs_e31_v16?0"CDPStateHandlerResult"8ls32l8s40l8
- ___block_literal_global.1025
- ___block_literal_global.1036
- ___block_literal_global.1140
- ___block_literal_global.1187
- ___block_literal_global.1222
- ___block_literal_global.1299
- ___block_literal_global.1328
- ___block_literal_global.152
- ___block_literal_global.2131
- ___block_literal_global.2143
- ___block_literal_global.2159
- ___block_literal_global.2231
- ___block_literal_global.513
- ___block_literal_global.57
- ___block_literal_global.72
- __os_feature_enabled_impl
- __swift_FORCE_LOAD_$_swiftAccelerate
- __swift_FORCE_LOAD_$_swiftAccelerate_$_CoreCDPInternal
- _handleCloudDataProtectionStateWithCompletion:.once
- _handleCloudDataProtectionStateWithCompletion:.stateMachineSemaphore
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$contextForCDPPDPStateRepair
- _objc_msgSend$pdpPCSGuitarfishRepairIdentities:completion:
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "%@: ADP enablement healing failed: %@"
+ "%@: ADP enablement healing succeeded"
+ "%@: Calling SEAR healing SPI to fix broken ADP enablement"
+ "%@: Failed to create PDP context dictionary. PDP blob generation is not possible."
+ "%@: Generating PDP blob with context dictionary"
+ "%@: Missing password or password metadata on CDPContext. ADP healing is not possible. CDPContext=%@"
+ "%@: Missing required password metadata for PDP blob generation. Missing fields: %@"
+ "%@: Unable to get primary account for ADP healing"
+ "%s: ADP enablement healing failed with error: %@"
+ "%s: ADP enablement healing returned NO without error"
+ "%s: ADP enablement healing succeeded"
+ "%s: Calling healing SPI"
+ "%s: Cannot perform ADP healing without password in context"
+ "%s: Detected PCS error PCSErrCuttlefishFailedToEnableWalrus for PDP user, will prompt for password"
+ "%s: PDP user needs password for ADP enablement, returning error to client"
+ "%s: Starting ADP enablement healing flow"
+ ", "
+ "-[CDPDPDPRecoveryController performADPEnablementHealingWithCompletion:]"
+ "-[CDPDPDPRecoveryController performADPEnablementHealingWithCompletion:]_block_invoke"
+ "-[CDPInternalWalrusStateController _createPDPPasswordRequiredErrorWithUnderlyingError:]"
+ "-[CDPInternalWalrusStateController _shouldPromptForPasswordWithError:context:]"
+ "B28@0:8B16@20"
+ "B32@0:8q16@24"
+ "CDPDPCSController deallocated before ADP enablement healing completion"
+ "CDPDPDPRecoveryController found nil during ADP enablement healing"
+ "DBR_TWO feature flag is disabled"
+ "Denying access to PDP blob generation, missing entitlements."
+ "Experienced error while attempting to post PDP repair CFU: %@"
+ "Finished PDP blob generation with blob length=%lu error=%@"
+ "Generate PDP Blob completed with blob length=%lu error=%@"
+ "Generating PDP blob..."
+ "PDP blob generation requires active PDP state, current state: %lu"
+ "PDP controller is nil, skipping PDP repair and continuing with CDP repair"
+ "PDP repair status: %@"
+ "PDPv2: PDP repair failed with error %@, posting PDP repair CFU."
+ "PDPv2: password change failed with error %@, posting PDP repair CFU."
+ "Posting PDP repair CFU due to healing failure"
+ "_containsPCSError:inError:"
+ "_createPDPPasswordRequiredErrorWithUnderlyingError:"
+ "_isDroppedKeysSuccessForEnablement:error:"
+ "_postPDPRepairFollowUp"
+ "_retryWalrusStateUpdate:context:account:completion:"
+ "_shouldPromptForPasswordWithError:context:"
+ "com.apple.appleaccount.signIn.deleteLocalData"
+ "com.apple.appleaccount.signIn.differentAccount"
+ "com.apple.appleaccount.signIn.mergeLocalData"
+ "com.apple.appleaccount.signIn.sameAccount"
+ "com.apple.appleaccount.signOut.eraseFlowStarted"
+ "com.apple.appleaccount.signOut.signOutWithoutErasing"
+ "com.apple.appleaccount.signOut.unsyncedDataAlertShown"
+ "componentsJoinedByString:"
+ "generatePDPBlob:completion:"
+ "generatePDPBlobWithCompletion:"
+ "generatePDPBlobWithContext:completion:"
+ "healBrokenADPEnablementWithAccountIdentifier:parameters:completion:"
+ "healBrokenADPEnablementWithCompletion:"
+ "isDBRTwoEnabled"
+ "pdpPCSDBRRepairIdentities:completion:"
+ "performADPEnablementHealingWithCompletion:"
+ "srpVerifier"
- "%s: Interactive PDP Repair method invoked unexpectedly in LuckC. Context type: %lu"
- "%s: PDP Repair method invoked unexpectedly in LuckC. Context type: %lu"
- "%s: Silent PDP Repair method invoked unexpectedly in LuckC. Context type: %lu"
- "-[CDPDPDPRecoveryController _interactiveRepairWithCompletion:]"
- "-[CDPDPDPRecoveryController performInteractivePDPRepairWithCompletion:]"
- "-[CDPDPDPRecoveryController repairPDPStateWithCompletion:]"
- "-[CDPDPDPRecoveryController silentlyRepairPDPStateWithCompletion:]"
- "AppleAccount"
- "CDP repair isn't needed"
- "Clearing all PDP CFUs - PDP only and fix all (PDP+CDP)"
- "Clearing the fix all (CDP+PDP) CFU"
- "Creating CDP & PDP Repair followup"
- "Experienced error while attempting to post Fix All (PDP and CDP) CFU: %@"
- "FastSignIn"
- "PDP is good now, but CDP is broken and needs repair"
- "PDP recovery successful"
- "PDP repair failed, continue with CDP state machine repair"
- "PDPv2: PDP repair failed with error %@, not posting any repair CFU."
- "PDPv2: password change failed with error %@, not posting any repair CFU."
- "Posting the Fix All (PDP and CDP) CFU"
- "_clearAllPDPFollowUps"
- "_postRepairPDPCDPFollowUp"
- "contextForCDPPDPStateRepair"
- "pdpPCSGuitarfishRepairIdentities:completion:"

```
