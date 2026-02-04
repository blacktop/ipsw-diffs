## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP`

```diff

 416.325.4.0.0
-  __TEXT.__text: 0x4eea0
-  __TEXT.__auth_stubs: 0x1040
-  __TEXT.__objc_methlist: 0x372c
+  __TEXT.__text: 0x52334
+  __TEXT.__auth_stubs: 0x10a0
+  __TEXT.__objc_methlist: 0x3954
   __TEXT.__const: 0x1324
-  __TEXT.__gcc_except_tab: 0x1174
-  __TEXT.__oslogstring: 0x8626
-  __TEXT.__cstring: 0x56e4
+  __TEXT.__gcc_except_tab: 0x125c
+  __TEXT.__oslogstring: 0x8da1
+  __TEXT.__cstring: 0x5b99
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x14b0
-  __TEXT.__objc_classname: 0x718
-  __TEXT.__objc_methname: 0x8923
-  __TEXT.__objc_methtype: 0x1a3d
-  __TEXT.__objc_stubs: 0x4c00
-  __DATA_CONST.__got: 0x490
-  __DATA_CONST.__const: 0x2d58
+  __TEXT.__unwind_info: 0x1550
+  __TEXT.__objc_classname: 0x719
+  __TEXT.__objc_methname: 0x8f7b
+  __TEXT.__objc_methtype: 0x1b9a
+  __TEXT.__objc_stubs: 0x4ee0
+  __DATA_CONST.__got: 0x4e0
+  __DATA_CONST.__const: 0x2ec8
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fc8
+  __DATA_CONST.__objc_selrefs: 0x2128
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x830
-  __AUTH_CONST.__const: 0x590
-  __AUTH_CONST.__cfstring: 0x3740
-  __AUTH_CONST.__objc_const: 0x84d8
+  __AUTH_CONST.__auth_got: 0x860
+  __AUTH_CONST.__const: 0x5b0
+  __AUTH_CONST.__cfstring: 0x3b80
+  __AUTH_CONST.__objc_const: 0x86f0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_ivar: 0x2cc
+  __DATA.__objc_ivar: 0x2ec
   __DATA.__data: 0x1110
-  __DATA.__bss: 0xf9
+  __DATA.__bss: 0x109
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AA3B713E-1383-3C52-8645-0DEC9ADC3367
-  Functions: 2208
-  Symbols:   7381
-  CStrings:  3563
+  UUID: 334538B9-90A3-3D4B-BC4D-519206C584AA
+  Functions: 2276
+  Symbols:   7596
+  CStrings:  3743
 
Symbols:
+ +[CDPFollowUpContext contextForCDPPDPStateRepair]
+ +[CDPFollowUpContext contextForCDPPDPStateRepair].cold.1
+ +[CDPFollowUpContext contextForPDPStateRepair]
+ +[CDPFollowUpContext contextForPDPStateRepair].cold.1
+ +[CDPUtilities isPDPEnabled]
+ +[CDPUtilities isPDPEnabled].cold.1
+ -[CDPContext _forcePDPReset]
+ -[CDPContext _parsePDPStateFromRawState:]
+ -[CDPContext _parsePDPStateFromRawState:].cold.1
+ -[CDPContext _rawPDPHealthForAccount:]
+ -[CDPContext _shouldAttemptPasswordBasedPDPSetup]
+ -[CDPContext _updatePDPAttributesFromAccountCacheWithAccount:]
+ -[CDPContext _updatePDPAttributesFromAccountCacheWithAccount:].cold.1
+ -[CDPContext _updatePDPAttributesFromAccountCacheWithAccount:].cold.2
+ -[CDPContext _updatePDPAttributesFromAccountCacheWithAccount:].cold.3
+ -[CDPContext _updatePDPAttributesFromAccountCache]
+ -[CDPContext _updatePDPWithAuthenticationResults:]
+ -[CDPContext forceInteractiveCDPPDPRepair]
+ -[CDPContext interactiveAuthDefaultButtonString]
+ -[CDPContext isPDPStateEligible]
+ -[CDPContext isPDPStateEligible].cold.1
+ -[CDPContext passwordVersion]
+ -[CDPContext pdpHealth]
+ -[CDPContext pdpState]
+ -[CDPContext setForceInteractiveCDPPDPRepair:]
+ -[CDPContext setInteractiveAuthDefaultButtonString:]
+ -[CDPContext setPasswordVersion:]
+ -[CDPContext setPdpHealth:]
+ -[CDPContext setPdpState:]
+ -[CDPContext setSrpIteration:]
+ -[CDPContext setSrpProtocol:]
+ -[CDPContext setSrpSalt:]
+ -[CDPContext set_forcePDPReset:]
+ -[CDPContext srpIteration]
+ -[CDPContext srpProtocol]
+ -[CDPContext srpSalt]
+ -[CDPProtectedCloudStorageProxyImpl pdpPCSDBRSetupIdentities:completion:]
+ -[CDPProtectedCloudStorageProxyImpl pdpPCSDBRValidateIdentities:completion:]
+ -[CDPProtectedCloudStorageProxyImpl pdpPCSGuitarfishChangePassword:completion:]
+ -[CDPProtectedCloudStorageProxyImpl pdpPCSGuitarfishRepairIdentities:completion:]
+ -[CDPProtectedCloudStorageProxyImpl pdpPCSResetProtectedData:completion:]
+ -[CDPRemoteDeviceSecretValidator repairPDPStateWithContext:completion:]
+ -[CDPStateController createPDPLivenessDictionaryWithContext:error:]
+ -[CDPStateController repairPDPStateWithCompletion:]
+ -[CDPStateController validatePDPIdentitiesWithContext:completion:]
+ GCC_except_table101
+ GCC_except_table108
+ GCC_except_table121
+ GCC_except_table123
+ GCC_except_table126
+ GCC_except_table129
+ GCC_except_table132
+ GCC_except_table135
+ GCC_except_table138
+ GCC_except_table140
+ GCC_except_table143
+ GCC_except_table146
+ GCC_except_table30
+ GCC_except_table47
+ GCC_except_table49
+ GCC_except_table50
+ GCC_except_table52
+ GCC_except_table55
+ GCC_except_table58
+ GCC_except_table61
+ GCC_except_table84
+ GCC_except_table87
+ GCC_except_table94
+ _AKPDPStateKey
+ _AKPasswordVersionKey
+ _AKSRPIterationCountKey
+ _AKSRPProtocolKey
+ _AKSRPSaltKey
+ _CDP_FOLLOWUP_CDP_PDP_REPAIR
+ _CDP_FOLLOWUP_PDP_ONLY_REPAIR
+ _OBJC_IVAR_$_CDPContext.__forcePDPReset
+ _OBJC_IVAR_$_CDPContext._forceInteractiveCDPPDPRepair
+ _OBJC_IVAR_$_CDPContext._interactiveAuthDefaultButtonString
+ _OBJC_IVAR_$_CDPContext._passwordVersion
+ _OBJC_IVAR_$_CDPContext._pdpHealth
+ _OBJC_IVAR_$_CDPContext._pdpState
+ _OBJC_IVAR_$_CDPContext._srpIteration
+ _OBJC_IVAR_$_CDPContext._srpProtocol
+ _OBJC_IVAR_$_CDPContext._srpSalt
+ _PCSDBRSetupIdentities
+ _PCSDBRValidateIdentities
+ _PCSGuitarfishChangePassword
+ _PCSGuitarfishRepairIdentities
+ _PCSGuitarfishResetProtectedData
+ _SecureBackupIsDBREnabled
+ ___28+[CDPUtilities isPDPEnabled]_block_invoke
+ ___28+[CDPUtilities isPDPEnabled]_block_invoke.cold.1
+ ___48-[CDPStateController generateRandomRecoveryKey:]_block_invoke.61
+ ___49-[CDPStateController deleteRecoveryKeyWithError:]_block_invoke.52
+ ___51-[CDPStateController repairPDPStateWithCompletion:]_block_invoke
+ ___51-[CDPStateController repairPDPStateWithCompletion:]_block_invoke.38
+ ___51-[CDPStateController repairPDPStateWithCompletion:]_block_invoke.39
+ ___51-[CDPStateController repairPDPStateWithCompletion:]_block_invoke.39.cold.1
+ ___54-[CDPStateController isRecoveryKeyAvailableWithError:]_block_invoke.53
+ ___59-[CDPStateController isRecoveryKeyAvailableWithCompletion:]_block_invoke.54
+ ___60-[CDPStateController isWalrusRecoveryKeyAvailableWithError:]_block_invoke.56
+ ___65-[CDPStateController isWalrusRecoveryKeyAvailableWithCompletion:]_block_invoke.57
+ ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.40
+ ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.40.cold.1
+ ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.41
+ ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.41.cold.1
+ ___66-[CDPStateController startSilentEscrowRecordRepairWithCompletion:]_block_invoke.78
+ ___66-[CDPStateController validatePDPIdentitiesWithContext:completion:]_block_invoke
+ ___66-[CDPStateController validatePDPIdentitiesWithContext:completion:]_block_invoke.84
+ ___66-[CDPStateController validatePDPIdentitiesWithContext:completion:]_block_invoke.84.cold.1
+ ___66-[CDPStateController validatePDPIdentitiesWithContext:completion:]_block_invoke.cold.1
+ ___67-[CDPStateController createPDPLivenessDictionaryWithContext:error:]_block_invoke
+ ___67-[CDPStateController createPDPLivenessDictionaryWithContext:error:]_block_invoke.86
+ ___67-[CDPStateController createPDPLivenessDictionaryWithContext:error:]_block_invoke.cold.1
+ ___67-[CDPStateController createPDPLivenessDictionaryWithContext:error:]_block_invoke.cold.2
+ ___68-[CDPStateController performSilentEscrowRecordRepairWithCompletion:]_block_invoke.79
+ ___68-[CDPStateController shouldPerformRepairWithOptionForceFetch:error:]_block_invoke.42
+ ___69-[CDPStateController authenticateAndDeleteRecoveryKeyWithCompletion:]_block_invoke.49
+ ___69-[CDPStateController authenticateAndDeleteRecoveryKeyWithCompletion:]_block_invoke.49.cold.1
+ ___70-[CDPStateController generateEscrowRecordReportUsingCache:completion:]_block_invoke.45
+ ___72-[CDPStateController anyRecoveryKeysAreOctagonDistrustedWithCompletion:]_block_invoke.60
+ ___73-[CDPProtectedCloudStorageProxyImpl pdpPCSDBRSetupIdentities:completion:]_block_invoke
+ ___73-[CDPProtectedCloudStorageProxyImpl pdpPCSResetProtectedData:completion:]_block_invoke
+ ___74-[CDPStateController authenticateAndGenerateNewRecoveryKeyWithCompletion:]_block_invoke.47
+ ___74-[CDPStateController authenticateAndGenerateNewRecoveryKeyWithCompletion:]_block_invoke.47.cold.1
+ ___74-[CDPStateController updateLastSilentEscrowRecordRepairAttemptDate:error:]_block_invoke.80
+ ___76-[CDPProtectedCloudStorageProxyImpl pdpPCSDBRValidateIdentities:completion:]_block_invoke
+ ___76-[CDPStateController shouldPerformSilentEscrowRecordRepairUsingCache:error:]_block_invoke.76
+ ___79-[CDPProtectedCloudStorageProxyImpl pdpPCSGuitarfishChangePassword:completion:]_block_invoke
+ ___81-[CDPProtectedCloudStorageProxyImpl pdpPCSGuitarfishRepairIdentities:completion:]_block_invoke
+ ___81-[CDPStateController shouldPerformAuthenticatedRepairWithOptionForceFetch:error:]_block_invoke.43
+ ___81-[CDPStateController shouldPerformSilentEscrowRecordRepairUsingCache:completion:]_block_invoke.77
+ ___82-[CDPStateController performEscrowRecordCheckWithContext:isBackground:completion:]_block_invoke.88
+ ___82-[CDPStateController performEscrowRecordCheckWithContext:isBackground:completion:]_block_invoke.88.cold.1
+ ___82-[CDPStateController verifyRecoveryKeyObservingSystemsHaveMatchingStateWithError:]_block_invoke.58
+ ___block_descriptor_48_e8_32s40bs_e37_v32?0Q8"NSDictionary"16"NSError"24ls32l8s40l8
+ ___block_descriptor_56_e8_32bs_e23_v32?0Q8Q16"NSError"24ls32l8
+ ___block_descriptor_56_e8_32bs_e23_v32?0q8q16"NSError"24ls32l8
+ ___block_descriptor_56_e8_32bs_e40_v40?0Q8Q16"NSDictionary"24"NSError"32ls32l8
+ ___block_descriptor_56_e8_32bs_e40_v40?0q8q16"NSDictionary"24"NSError"32ls32l8
+ ___block_descriptor_56_e8_32s40r48r_e34_v24?0"NSDictionary"8"NSError"16ls32l8r40l8r48l8
+ ___block_literal_global.170
+ ___block_literal_global.79
+ ___block_literal_global.82
+ ___block_literal_global.87
+ ___block_literal_global.91
+ ___block_literal_global.95
+ ___block_literal_global.99
+ _isPDPEnabled.enabled
+ _isPDPEnabled.once
+ _kCDPAnalyticsNativeIntermissionAPIEvent
+ _kCDPAnalyticsNativeIntermissionAuthRequiredEvent
+ _kCDPAnalyticsNativeIntermissionFinishEvent
+ _kCDPAnalyticsNativeIntermissionStartEvent
+ _kCDPAnalyticsNativeIntermissionUnavailableEvent
+ _kCDPAnalyticsPDPChangePasswordEvent
+ _kCDPAnalyticsPDPEligibility
+ _kCDPAnalyticsPDPHealth
+ _kCDPAnalyticsPDPPasswordValidationEvent
+ _kCDPAnalyticsPDPRepairFinishEvent
+ _kCDPAnalyticsPDPRepairStartEvent
+ _kCDPAnalyticsPDPSetupIdentitiesEvent
+ _kCDPEventCountry
+ _kPCSAuthenticateAppleID
+ _kPCSSetupPasswordGeneration
+ _kPCSSetupRawPassword
+ _kPCSSetupVerifierIterationCount
+ _kPCSSetupVerifierProtocol
+ _kPCSSetupVerifierSalt
+ _objc_msgSend$_parsePDPStateFromRawState:
+ _objc_msgSend$_rawPDPHealthForAccount:
+ _objc_msgSend$_recoveryMethodAvailable
+ _objc_msgSend$_updatePDPAttributesFromAccountCache
+ _objc_msgSend$_updatePDPAttributesFromAccountCacheWithAccount:
+ _objc_msgSend$_updatePDPWithAuthenticationResults:
+ _objc_msgSend$createPDPLivenessDictionaryWithContext:completion:
+ _objc_msgSend$forceInteractiveCDPPDPRepair
+ _objc_msgSend$isPDPEnabled
+ _objc_msgSend$isPDPStateEligible
+ _objc_msgSend$passwordVersion
+ _objc_msgSend$passwordVersionForAccount:
+ _objc_msgSend$pdpHealth
+ _objc_msgSend$pdpState
+ _objc_msgSend$pdpStateValueForAccount:
+ _objc_msgSend$repairPDPStateWithContext:completion:
+ _objc_msgSend$repairPDPStateWithContext:uiProvider:completion:
+ _objc_msgSend$setAccountIsDBR:
+ _objc_msgSend$srpIteration
+ _objc_msgSend$srpProtocol
+ _objc_msgSend$srpProtocolForAccount:
+ _objc_msgSend$srpSalt
+ _objc_msgSend$validatePDPIdentitiesWithContext:uiProvider:completion:
- GCC_except_table100
- GCC_except_table109
- GCC_except_table119
- GCC_except_table122
- GCC_except_table125
- GCC_except_table128
- GCC_except_table131
- GCC_except_table134
- GCC_except_table136
- GCC_except_table31
- GCC_except_table37
- GCC_except_table38
- GCC_except_table40
- GCC_except_table51
- GCC_except_table54
- GCC_except_table57
- GCC_except_table60
- GCC_except_table83
- GCC_except_table86
- GCC_except_table93
- _OBJC_IVAR_$_CDPContext._isProxSignIn
- ___48-[CDPStateController generateRandomRecoveryKey:]_block_invoke.59
- ___49-[CDPStateController deleteRecoveryKeyWithError:]_block_invoke.50
- ___54-[CDPStateController isRecoveryKeyAvailableWithError:]_block_invoke.51
- ___59-[CDPStateController isRecoveryKeyAvailableWithCompletion:]_block_invoke.52
- ___60-[CDPStateController isWalrusRecoveryKeyAvailableWithError:]_block_invoke.54
- ___65-[CDPStateController isWalrusRecoveryKeyAvailableWithCompletion:]_block_invoke.55
- ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.38
- ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.38.cold.1
- ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.39
- ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.39.cold.1
- ___66-[CDPStateController startSilentEscrowRecordRepairWithCompletion:]_block_invoke.76
- ___68-[CDPStateController performSilentEscrowRecordRepairWithCompletion:]_block_invoke.77
- ___68-[CDPStateController shouldPerformRepairWithOptionForceFetch:error:]_block_invoke.40
- ___69-[CDPStateController authenticateAndDeleteRecoveryKeyWithCompletion:]_block_invoke.47
- ___69-[CDPStateController authenticateAndDeleteRecoveryKeyWithCompletion:]_block_invoke.47.cold.1
- ___70-[CDPStateController generateEscrowRecordReportUsingCache:completion:]_block_invoke.43
- ___72-[CDPStateController anyRecoveryKeysAreOctagonDistrustedWithCompletion:]_block_invoke.58
- ___74-[CDPStateController authenticateAndGenerateNewRecoveryKeyWithCompletion:]_block_invoke.45
- ___74-[CDPStateController authenticateAndGenerateNewRecoveryKeyWithCompletion:]_block_invoke.45.cold.1
- ___74-[CDPStateController updateLastSilentEscrowRecordRepairAttemptDate:error:]_block_invoke.78
- ___76-[CDPStateController shouldPerformSilentEscrowRecordRepairUsingCache:error:]_block_invoke.74
- ___81-[CDPStateController shouldPerformAuthenticatedRepairWithOptionForceFetch:error:]_block_invoke.41
- ___81-[CDPStateController shouldPerformSilentEscrowRecordRepairUsingCache:completion:]_block_invoke.75
- ___82-[CDPStateController performEscrowRecordCheckWithContext:isBackground:completion:]_block_invoke.82
- ___82-[CDPStateController performEscrowRecordCheckWithContext:isBackground:completion:]_block_invoke.82.cold.1
- ___82-[CDPStateController verifyRecoveryKeyObservingSystemsHaveMatchingStateWithError:]_block_invoke.56
- ___block_literal_global.166
- ___block_literal_global.80
- ___block_literal_global.85
- ___block_literal_global.89
- ___block_literal_global.93
- ___block_literal_global.97
CStrings:
+ "\tInteractive Auth Button String: %@\n"
+ "\tforceInteractiveCDPPDPRepair: %d\n"
+ "\toldPassword is %@ missing\n"
+ "\tpassword is %@ missing\n"
+ "\tpasswordVersion: %@\n"
+ "\tpdpState: %ld\n"
+ "\tsrpIteration is %@ missing\n"
+ "\tsrpProtocol is %@ missing\n"
+ "\tsrpSalt is %@ missing\n"
+ "%s: Calling into daemon validator to repair PDP state"
+ "%s: Rejecting out-of-range PDP state (%@)."
+ "%s: Unable to obtain the passwordVersionForAccount because AKAccountManager (%@) doesn't respond to selector."
+ "%s: Unable to obtain the pdpStateValueForAccount because AKAccountManager (%@) doesn't respond to selector."
+ "%s: Unable to obtain the srpProtocolForAccount because AKAccountManager (%@) doesn't respond to selector."
+ "-[CDPContext _parsePDPStateFromRawState:]"
+ "-[CDPContext _updatePDPAttributesFromAccountCacheWithAccount:]"
+ "-[CDPRemoteDeviceSecretValidator repairPDPStateWithContext:completion:]"
+ "BEGIN [%lld]: DBRChangePassword  enableTelemetry=YES "
+ "BEGIN [%lld]: DBRRepair  enableTelemetry=YES "
+ "BEGIN [%lld]: DBRResetProtectedData  enableTelemetry=YES "
+ "BEGIN [%lld]: DBRSetup  enableTelemetry=YES "
+ "BEGIN [%lld]: DBRValidate  enableTelemetry=YES "
+ "BEGIN [%lld]: RepairPDPState  enableTelemetry=YES "
+ "CDPContext: PDP eligibility check: pdpState=%ld, isEligible=%{BOOL}d"
+ "Checking for PDP health status"
+ "Creating PDP liveness health payload..."
+ "Creating context for CDP & PDP Repair CFU"
+ "Creating context for PDP Only Repair CFU"
+ "DBR Enabled: %{BOOL}d"
+ "DBRChangePassword"
+ "DBRRepair"
+ "DBRResetProtectedData"
+ "DBRSetup"
+ "DBRValidate"
+ "END [%lld] %fs: DBRChangePassword  Error=%{public,signpost.telemetry:number1,name=Error}d "
+ "END [%lld] %fs: DBRRepair  Error=%{public,signpost.telemetry:number1,name=Error}d "
+ "END [%lld] %fs: DBRResetProtectedData  Error=%{public,signpost.telemetry:number1,name=Error}d "
+ "END [%lld] %fs: DBRSetup  Error=%{public,signpost.telemetry:number1,name=Error}d "
+ "END [%lld] %fs: DBRValidate  Error=%{public,signpost.telemetry:number1,name=Error}d "
+ "END [%lld] %fs: RepairPDPState  Error=%{public,signpost.telemetry:number1,name=Error}d "
+ "Failed to validate PDP identities with error: %@"
+ "Failed to validate PDP identities: %{public}@, healthState: %ld"
+ "NOT"
+ "PDP livness dictionary=%@"
+ "PDP repair completed didRepair=%{BOOL}d error=%@"
+ "RepairPDPState"
+ "Requesting repair of PDP state..."
+ "T@\"NSData\",C,N,V_srpSalt"
+ "T@\"NSNumber\",C,N,V_passwordVersion"
+ "T@\"NSNumber\",C,N,V_srpIteration"
+ "T@\"NSString\",C,N,V_interactiveAuthDefaultButtonString"
+ "T@\"NSString\",C,N,V_srpProtocol"
+ "TB,N,V__forcePDPReset"
+ "TB,N,V_forceInteractiveCDPPDPRepair"
+ "TQ,N,V_pdpHealth"
+ "TQ,N,V_pdpState"
+ "XPC Error while repairing PDP state: %@"
+ "__forcePDPReset"
+ "_forceInteractiveCDPPDPRepair"
+ "_forcePDPReset"
+ "_interactiveAuthDefaultButtonString"
+ "_parsePDPStateFromRawState:"
+ "_passwordVersion"
+ "_pdpHealth"
+ "_pdpState"
+ "_rawPDPHealthForAccount:"
+ "_shouldAttemptPasswordBasedPDPSetup"
+ "_srpIteration"
+ "_srpProtocol"
+ "_srpSalt"
+ "_updatePDPAttributesFromAccountCache"
+ "_updatePDPAttributesFromAccountCacheWithAccount:"
+ "_updatePDPWithAuthenticationResults:"
+ "cdp/pdp-health-liveness-payload"
+ "cdp/pdp-health-status"
+ "cdp/pdp-state-repair"
+ "com.apple.corecdp.nativeIntermissionAPI"
+ "com.apple.corecdp.nativeIntermissionAuthRequired"
+ "com.apple.corecdp.nativeIntermissionFinish"
+ "com.apple.corecdp.nativeIntermissionStart"
+ "com.apple.corecdp.nativeIntermissionUnavailable"
+ "com.apple.corecdp.passwordChange"
+ "com.apple.corecdp.passwordValidation"
+ "com.apple.corecdp.pdpRepairEntry"
+ "com.apple.corecdp.pdpRepairFinish"
+ "com.apple.corecdp.setUpIdentities"
+ "contextForCDPPDPStateRepair"
+ "contextForPDPStateRepair"
+ "country"
+ "createPDPLivenessDictionaryWithContext:completion:"
+ "createPDPLivenessDictionaryWithContext:error:"
+ "forceInteractiveCDPPDPRepair"
+ "interactiveAuthDefaultButtonString"
+ "isPDPEnabled"
+ "isPDPStateEligible"
+ "kCDPPDPStateRepair"
+ "kPDPOnlyStateRepair"
+ "passwordVersion"
+ "passwordVersionForAccount:"
+ "pdpEligible"
+ "pdpHealth"
+ "pdpPCSDBRSetupIdentities:completion:"
+ "pdpPCSDBRValidateIdentities:completion:"
+ "pdpPCSGuitarfishChangePassword:completion:"
+ "pdpPCSGuitarfishRepairIdentities:completion:"
+ "pdpPCSResetProtectedData:completion:"
+ "pdpState"
+ "pdpStateValueForAccount:"
+ "pdps"
+ "repairPDPStateWithCompletion:"
+ "repairPDPStateWithContext:completion:"
+ "repairPDPStateWithContext:uiProvider:completion:"
+ "setAccountIsDBR:"
+ "setForceInteractiveCDPPDPRepair:"
+ "setInteractiveAuthDefaultButtonString:"
+ "setPasswordVersion:"
+ "setPdpHealth:"
+ "setPdpState:"
+ "setSrpIteration:"
+ "setSrpProtocol:"
+ "setSrpSalt:"
+ "set_forcePDPReset:"
+ "srpIteration"
+ "srpProtocol"
+ "srpProtocolForAccount:"
+ "srpSalt"
+ "v32@0:8@\"NSDictionary\"16@?<v@?Q@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?QQ@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?QQ@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?q@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?qq@\"NSDictionary\"@\"NSError\">24"
+ "v32@?0Q8@\"NSDictionary\"16@\"NSError\"24"
+ "v32@?0Q8Q16@\"NSError\"24"
+ "v32@?0q8q16@\"NSError\"24"
+ "v40@0:8@\"CDPContext\"16@\"<CDPStateUIProviderInternal>\"24@?<v@?Q@\"NSDictionary\"@\"NSError\">32"
+ "v40@?0Q8Q16@\"NSDictionary\"24@\"NSError\"32"
+ "v40@?0q8q16@\"NSDictionary\"24@\"NSError\"32"
+ "validatePDPIdentitiesWithContext:completion:"
+ "validatePDPIdentitiesWithContext:uiProvider:completion:"
- "TB,R,N,V_isProxSignIn"
- "_isProxSignIn"

```
