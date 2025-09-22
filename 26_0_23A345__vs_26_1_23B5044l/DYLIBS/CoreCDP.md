## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP`

```diff

-413.0.0.0.0
-  __TEXT.__text: 0x5395c
-  __TEXT.__auth_stubs: 0x10b0
-  __TEXT.__objc_methlist: 0x3a8c
-  __TEXT.__const: 0x12f4
-  __TEXT.__gcc_except_tab: 0x129c
-  __TEXT.__oslogstring: 0x9046
-  __TEXT.__cstring: 0x6082
+416.125.2.0.0
+  __TEXT.__text: 0x4ec70
+  __TEXT.__auth_stubs: 0x1040
+  __TEXT.__objc_methlist: 0x3714
+  __TEXT.__const: 0x1304
+  __TEXT.__gcc_except_tab: 0x1174
+  __TEXT.__oslogstring: 0x856e
+  __TEXT.__cstring: 0x5684
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x1580
-  __TEXT.__objc_classname: 0x71f
-  __TEXT.__objc_methname: 0x9343
-  __TEXT.__objc_methtype: 0x1c8e
-  __TEXT.__objc_stubs: 0x5020
-  __DATA_CONST.__got: 0x4c8
-  __DATA_CONST.__const: 0x2f70
+  __TEXT.__unwind_info: 0x14a0
+  __TEXT.__objc_classname: 0x718
+  __TEXT.__objc_methname: 0x88b1
+  __TEXT.__objc_methtype: 0x1a3d
+  __TEXT.__objc_stubs: 0x4be0
+  __DATA_CONST.__got: 0x490
+  __DATA_CONST.__const: 0x2d48
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2190
+  __DATA_CONST.__objc_selrefs: 0x1fb0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x868
-  __AUTH_CONST.__const: 0x5d0
-  __AUTH_CONST.__cfstring: 0x3f00
-  __AUTH_CONST.__objc_const: 0x8ae0
+  __AUTH_CONST.__auth_got: 0x830
+  __AUTH_CONST.__const: 0x590
+  __AUTH_CONST.__cfstring: 0x36e0
+  __AUTH_CONST.__objc_const: 0x84a8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_ivar: 0x304
-  __DATA.__data: 0x1108
-  __DATA.__bss: 0x101
+  __DATA.__objc_ivar: 0x2c8
+  __DATA.__data: 0x1110
+  __DATA.__bss: 0xf9
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x118
+  __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BFF0C657-2CD8-3089-A400-FE395C0D1C20
-  Functions: 2317
-  Symbols:   7708
-  CStrings:  3851
+  UUID: 639B24A6-9592-3A34-8364-791D3E476B6F
+  Functions: 2203
+  Symbols:   7371
+  CStrings:  3550
 
Symbols:
+ +[CDPStringUtilities isValidKeyLength:expectedLength:withSeparator:]
+ +[CDPStringUtilities keyWithGrouping:groupLength:separator:]
+ +[CDPStringUtilities sanitizedKeyInput:]
+ GCC_except_table100
+ GCC_except_table109
+ GCC_except_table119
+ GCC_except_table122
+ GCC_except_table125
+ GCC_except_table128
+ GCC_except_table131
+ GCC_except_table134
+ GCC_except_table136
+ GCC_except_table31
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table40
+ GCC_except_table51
+ GCC_except_table54
+ GCC_except_table57
+ GCC_except_table60
+ GCC_except_table83
+ GCC_except_table86
+ GCC_except_table93
+ _OBJC_CLASS_$_CDPStringUtilities
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_IVAR_$_CDPContext._isProxSignIn
+ _OBJC_METACLASS_$_CDPStringUtilities
+ __OBJC_$_CLASS_METHODS_CDPStringUtilities
+ __OBJC_CLASS_RO_$_CDPStringUtilities
+ __OBJC_METACLASS_RO_$_CDPStringUtilities
+ ___36-[CDPAccount isOTEnabledForContext:]_block_invoke.29
+ ___48-[CDPStateController generateRandomRecoveryKey:]_block_invoke.59
+ ___49-[CDPStateController deleteRecoveryKeyWithError:]_block_invoke.50
+ ___51+[CDPAccount isICDPEnabledForDSID:checkWithServer:]_block_invoke.17
+ ___54-[CDPStateController isRecoveryKeyAvailableWithError:]_block_invoke.51
+ ___59-[CDPStateController isRecoveryKeyAvailableWithCompletion:]_block_invoke.52
+ ___60-[CDPStateController isWalrusRecoveryKeyAvailableWithError:]_block_invoke.54
+ ___62-[CDPAccountRepresentation isICDPEnabledByCheckingWithServer:]_block_invoke.57
+ ___65-[CDPStateController isWalrusRecoveryKeyAvailableWithCompletion:]_block_invoke.55
+ ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.38
+ ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.38.cold.1
+ ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.39
+ ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.39.cold.1
+ ___66-[CDPStateController startSilentEscrowRecordRepairWithCompletion:]_block_invoke.76
+ ___68-[CDPStateController performSilentEscrowRecordRepairWithCompletion:]_block_invoke.77
+ ___68-[CDPStateController shouldPerformRepairWithOptionForceFetch:error:]_block_invoke.40
+ ___69-[CDPStateController authenticateAndDeleteRecoveryKeyWithCompletion:]_block_invoke.47
+ ___69-[CDPStateController authenticateAndDeleteRecoveryKeyWithCompletion:]_block_invoke.47.cold.1
+ ___70-[CDPStateController generateEscrowRecordReportUsingCache:completion:]_block_invoke.43
+ ___72-[CDPStateController anyRecoveryKeysAreOctagonDistrustedWithCompletion:]_block_invoke.58
+ ___73-[CDPStateUIProviderProxy cdpContext:promptForLocalSecretWithCompletion:]_block_invoke.25
+ ___74-[CDPStateController authenticateAndGenerateNewRecoveryKeyWithCompletion:]_block_invoke.45
+ ___74-[CDPStateController authenticateAndGenerateNewRecoveryKeyWithCompletion:]_block_invoke.45.cold.1
+ ___74-[CDPStateController updateLastSilentEscrowRecordRepairAttemptDate:error:]_block_invoke.78
+ ___76-[CDPStateController shouldPerformSilentEscrowRecordRepairUsingCache:error:]_block_invoke.74
+ ___81-[CDPStateController shouldPerformAuthenticatedRepairWithOptionForceFetch:error:]_block_invoke.41
+ ___81-[CDPStateController shouldPerformSilentEscrowRecordRepairUsingCache:completion:]_block_invoke.75
+ ___82-[CDPStateController performEscrowRecordCheckWithContext:isBackground:completion:]_block_invoke.82
+ ___82-[CDPStateController performEscrowRecordCheckWithContext:isBackground:completion:]_block_invoke.82.cold.1
+ ___82-[CDPStateController verifyRecoveryKeyObservingSystemsHaveMatchingStateWithError:]_block_invoke.56
+ ___block_literal_global.166
+ ___block_literal_global.25
+ ___block_literal_global.28
+ ___block_literal_global.80
+ ___block_literal_global.85
+ ___block_literal_global.89
+ ___block_literal_global.93
+ ___block_literal_global.97
+ ___der_key_ephdm
+ _der_key_ephdm
+ _objc_msgSend$alphanumericCharacterSet
+ _objc_msgSend$characterAtIndex:
+ _objc_msgSend$characterIsMember:
+ _objc_msgSend$stringWithCharacters:length:
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$uppercaseString
- +[CDPEDPConfigProvider sharedInstance]
- +[CDPEDPConfigProvider sharedInstance].cold.1
- +[CDPFollowUpContext contextForCDPEDPStateRepair]
- +[CDPFollowUpContext contextForCDPEDPStateRepair].cold.1
- +[CDPFollowUpContext contextForEDPStateRepair]
- +[CDPFollowUpContext contextForEDPStateRepair].cold.1
- +[CDPUtilities isGuitarfishEnabled]
- +[CDPUtilities isGuitarfishEnabled].cold.1
- -[CDPCircleProxyImpl synchronizeCircleViews].cold.1
- -[CDPCircleProxyImpl synchronizeCircleViews].cold.2
- -[CDPContext _alwaysPromptForEDPRecoveryToken]
- -[CDPContext _forceEDPReset]
- -[CDPContext _parseEDPStateFromRawState:]
- -[CDPContext _parseEDPStateFromRawState:].cold.1
- -[CDPContext _rawEDPHealthForAccount:]
- -[CDPContext _updateEDPAttributesFromAccountCacheWithAccount:]
- -[CDPContext _updateEDPAttributesFromAccountCacheWithAccount:].cold.1
- -[CDPContext _updateEDPAttributesFromAccountCacheWithAccount:].cold.2
- -[CDPContext _updateEDPAttributesFromAccountCacheWithAccount:].cold.3
- -[CDPContext _updateEDPAttributesFromAccountCache]
- -[CDPContext _updateEDPWithAuthenticationResults:]
- -[CDPContext edpHealth]
- -[CDPContext edpRecoveryToken]
- -[CDPContext edpState]
- -[CDPContext forceInteractiveCDPEDPRepair]
- -[CDPContext interactiveAuthDefaultButtonString]
- -[CDPContext passwordVersion]
- -[CDPContext setEdpHealth:]
- -[CDPContext setEdpRecoveryToken:]
- -[CDPContext setEdpState:]
- -[CDPContext setForceInteractiveCDPEDPRepair:]
- -[CDPContext setInteractiveAuthDefaultButtonString:]
- -[CDPContext setPasswordVersion:]
- -[CDPContext setSrpIteration:]
- -[CDPContext setSrpProtocol:]
- -[CDPContext setSrpSalt:]
- -[CDPContext set_alwaysPromptForEDPRecoveryToken:]
- -[CDPContext set_forceEDPReset:]
- -[CDPContext srpIteration]
- -[CDPContext srpProtocol]
- -[CDPContext srpSalt]
- -[CDPEDPConfigProvider .cxx_destruct]
- -[CDPEDPConfigProvider _extractTokenNameFromConfig:finalize:]
- -[CDPEDPConfigProvider _extractTokenNameFromConfig:finalize:].cold.1
- -[CDPEDPConfigProvider _extractTokenNameFromConfig:finalize:].cold.2
- -[CDPEDPConfigProvider fetchCompleted]
- -[CDPEDPConfigProvider fetchConfig]
- -[CDPEDPConfigProvider setFetchCompleted:]
- -[CDPEDPConfigProvider setTokenName:]
- -[CDPEDPConfigProvider setTokenNameMedium:]
- -[CDPEDPConfigProvider setTokenNameTitle:]
- -[CDPEDPConfigProvider tokenNameMedium]
- -[CDPEDPConfigProvider tokenNameTitle]
- -[CDPEDPConfigProvider tokenName]
- -[CDPProtectedCloudStorageProxyImpl edpPCSGuitarfishChangePassword:completion:]
- -[CDPProtectedCloudStorageProxyImpl edpPCSGuitarfishGetRecoveryTokenInfo:completion:]
- -[CDPProtectedCloudStorageProxyImpl edpPCSGuitarfishRepairIdentities:completion:]
- -[CDPProtectedCloudStorageProxyImpl edpPCSGuitarfishSetupIdentities:completion:]
- -[CDPProtectedCloudStorageProxyImpl edpPCSGuitarfishValidateIdentities:completion:]
- -[CDPProtectedCloudStorageProxyImpl edpPCSResetProtectedData:completion:]
- -[CDPRemoteDeviceSecretValidator repairEDPStateWithContext:completion:]
- -[CDPRemoteDeviceSecretValidator validateEDPRecoveryToken:withContext:completion:]
- -[CDPSOSCircleProxyImpl synchronizeCircleViews].cold.2
- -[CDPSOSCircleProxyImpl synchronizeCircleViews].cold.3
- -[CDPStateController createEDPLivenessDictionaryWithContext:error:]
- -[CDPStateController fetchEDPTokenWithCompletion:]
- -[CDPStateController repairEDPStateWithCompletion:]
- -[CDPStateController validateEDPIdentitiesWithContext:completion:]
- -[CDPStateUIProviderProxy cdpContext:promptForEDPRecoveryTokenWithValidator:successfulCDPRecoveryContinuationHandler:]
- -[CDPToolFakeUIProvider cdpContext:promptForEDPRecoveryTokenWithValidator:successfulCDPRecoveryContinuationHandler:]
- -[CDPToolFakeUIProvider recoveryToken]
- -[CDPToolFakeUIProvider setRecoveryToken:]
- -[NSError(CDP) cdp_indicatesEDPRecoveryTokenIsNeeded]
- GCC_except_table101
- GCC_except_table108
- GCC_except_table121
- GCC_except_table123
- GCC_except_table126
- GCC_except_table129
- GCC_except_table132
- GCC_except_table135
- GCC_except_table138
- GCC_except_table140
- GCC_except_table143
- GCC_except_table148
- GCC_except_table151
- GCC_except_table30
- GCC_except_table46
- GCC_except_table47
- GCC_except_table49
- GCC_except_table52
- GCC_except_table55
- GCC_except_table58
- GCC_except_table61
- GCC_except_table84
- GCC_except_table87
- GCC_except_table94
- _AKEDPStateKey
- _AKPasswordVersionKey
- _AKSRPIterationCountKey
- _AKSRPProtocolKey
- _AKSRPSaltKey
- _CDPEDPCofigKey
- _CDPEDPTokenKey
- _CDPEDPTokenMediumKey
- _CDPEDPTokenTitleKey
- _CDPReplaceEDPTokens
- _CDP_FOLLOWUP_CDP_EDP_REPAIR
- _CDP_FOLLOWUP_EDP_ONLY_REPAIR
- _OBJC_CLASS_$_AKGlobalConfig
- _OBJC_CLASS_$_CDPEDPConfigProvider
- _OBJC_IVAR_$_CDPContext.__alwaysPromptForEDPRecoveryToken
- _OBJC_IVAR_$_CDPContext.__forceEDPReset
- _OBJC_IVAR_$_CDPContext._edpHealth
- _OBJC_IVAR_$_CDPContext._edpRecoveryToken
- _OBJC_IVAR_$_CDPContext._edpState
- _OBJC_IVAR_$_CDPContext._forceInteractiveCDPEDPRepair
- _OBJC_IVAR_$_CDPContext._interactiveAuthDefaultButtonString
- _OBJC_IVAR_$_CDPContext._passwordVersion
- _OBJC_IVAR_$_CDPContext._srpIteration
- _OBJC_IVAR_$_CDPContext._srpProtocol
- _OBJC_IVAR_$_CDPContext._srpSalt
- _OBJC_IVAR_$_CDPEDPConfigProvider._fetchCompleted
- _OBJC_IVAR_$_CDPEDPConfigProvider._tokenName
- _OBJC_IVAR_$_CDPEDPConfigProvider._tokenNameMedium
- _OBJC_IVAR_$_CDPEDPConfigProvider._tokenNameTitle
- _OBJC_IVAR_$_CDPToolFakeUIProvider._recoveryToken
- _OBJC_METACLASS_$_CDPEDPConfigProvider
- _PCSGuitarfishChangePassword
- _PCSGuitarfishGetRecoveryTokenInfo
- _PCSGuitarfishRepairIdentities
- _PCSGuitarfishResetProtectedData
- _PCSGuitarfishSetupIdentities
- _PCSGuitarfishValidateIdentities
- _SecureBackupIsGuitarfishEnabled
- __OBJC_$_CLASS_METHODS_CDPEDPConfigProvider
- __OBJC_$_INSTANCE_METHODS_CDPEDPConfigProvider
- __OBJC_$_INSTANCE_VARIABLES_CDPEDPConfigProvider
- __OBJC_$_PROP_LIST_CDPEDPConfigProvider
- __OBJC_CLASS_RO_$_CDPEDPConfigProvider
- __OBJC_METACLASS_RO_$_CDPEDPConfigProvider
- ___116-[CDPToolFakeUIProvider cdpContext:promptForEDPRecoveryTokenWithValidator:successfulCDPRecoveryContinuationHandler:]_block_invoke
- ___116-[CDPToolFakeUIProvider cdpContext:promptForEDPRecoveryTokenWithValidator:successfulCDPRecoveryContinuationHandler:]_block_invoke.cold.1
- ___118-[CDPStateUIProviderProxy cdpContext:promptForEDPRecoveryTokenWithValidator:successfulCDPRecoveryContinuationHandler:]_block_invoke
- ___118-[CDPStateUIProviderProxy cdpContext:promptForEDPRecoveryTokenWithValidator:successfulCDPRecoveryContinuationHandler:]_block_invoke.cold.1
- ___118-[CDPStateUIProviderProxy cdpContext:promptForEDPRecoveryTokenWithValidator:successfulCDPRecoveryContinuationHandler:]_block_invoke.cold.2
- ___35+[CDPUtilities isGuitarfishEnabled]_block_invoke
- ___35+[CDPUtilities isGuitarfishEnabled]_block_invoke.cold.1
- ___35-[CDPEDPConfigProvider fetchConfig]_block_invoke
- ___35-[CDPEDPConfigProvider fetchConfig]_block_invoke.30
- ___35-[CDPEDPConfigProvider fetchConfig]_block_invoke.30.cold.1
- ___35-[CDPEDPConfigProvider fetchConfig]_block_invoke.cold.1
- ___36-[CDPAccount isOTEnabledForContext:]_block_invoke.47
- ___38+[CDPEDPConfigProvider sharedInstance]_block_invoke
- ___48-[CDPStateController generateRandomRecoveryKey:]_block_invoke.61
- ___49-[CDPStateController deleteRecoveryKeyWithError:]_block_invoke.52
- ___50-[CDPStateController fetchEDPTokenWithCompletion:]_block_invoke
- ___50-[CDPStateController fetchEDPTokenWithCompletion:]_block_invoke.85
- ___50-[CDPStateController fetchEDPTokenWithCompletion:]_block_invoke.86
- ___50-[CDPStateController fetchEDPTokenWithCompletion:]_block_invoke.cold.1
- ___50-[CDPStateController fetchEDPTokenWithCompletion:]_block_invoke_2
- ___51+[CDPAccount isICDPEnabledForDSID:checkWithServer:]_block_invoke.35
- ___51-[CDPStateController repairEDPStateWithCompletion:]_block_invoke
- ___51-[CDPStateController repairEDPStateWithCompletion:]_block_invoke.38
- ___51-[CDPStateController repairEDPStateWithCompletion:]_block_invoke.39
- ___51-[CDPStateController repairEDPStateWithCompletion:]_block_invoke.39.cold.1
- ___54-[CDPStateController isRecoveryKeyAvailableWithError:]_block_invoke.53
- ___59-[CDPStateController isRecoveryKeyAvailableWithCompletion:]_block_invoke.54
- ___60-[CDPStateController isWalrusRecoveryKeyAvailableWithError:]_block_invoke.56
- ___61-[CDPEDPConfigProvider _extractTokenNameFromConfig:finalize:]_block_invoke
- ___62-[CDPAccountRepresentation isICDPEnabledByCheckingWithServer:]_block_invoke.63
- ___65-[CDPStateController isWalrusRecoveryKeyAvailableWithCompletion:]_block_invoke.57
- ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.40
- ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.40.cold.1
- ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.41
- ___65-[CDPStateController localSecretChangedTo:secretType:completion:]_block_invoke.41.cold.1
- ___66-[CDPStateController startSilentEscrowRecordRepairWithCompletion:]_block_invoke.78
- ___66-[CDPStateController validateEDPIdentitiesWithContext:completion:]_block_invoke
- ___66-[CDPStateController validateEDPIdentitiesWithContext:completion:]_block_invoke.84
- ___66-[CDPStateController validateEDPIdentitiesWithContext:completion:]_block_invoke.84.cold.1
- ___66-[CDPStateController validateEDPIdentitiesWithContext:completion:]_block_invoke.cold.1
- ___67-[CDPStateController createEDPLivenessDictionaryWithContext:error:]_block_invoke
- ___67-[CDPStateController createEDPLivenessDictionaryWithContext:error:]_block_invoke.88
- ___67-[CDPStateController createEDPLivenessDictionaryWithContext:error:]_block_invoke.cold.1
- ___67-[CDPStateController createEDPLivenessDictionaryWithContext:error:]_block_invoke.cold.2
- ___68-[CDPStateController performSilentEscrowRecordRepairWithCompletion:]_block_invoke.79
- ___68-[CDPStateController shouldPerformRepairWithOptionForceFetch:error:]_block_invoke.42
- ___69-[CDPStateController authenticateAndDeleteRecoveryKeyWithCompletion:]_block_invoke.49
- ___69-[CDPStateController authenticateAndDeleteRecoveryKeyWithCompletion:]_block_invoke.49.cold.1
- ___70-[CDPStateController generateEscrowRecordReportUsingCache:completion:]_block_invoke.45
- ___72-[CDPStateController anyRecoveryKeysAreOctagonDistrustedWithCompletion:]_block_invoke.60
- ___73-[CDPProtectedCloudStorageProxyImpl edpPCSResetProtectedData:completion:]_block_invoke
- ___73-[CDPStateUIProviderProxy cdpContext:promptForLocalSecretWithCompletion:]_block_invoke.43
- ___74-[CDPStateController authenticateAndGenerateNewRecoveryKeyWithCompletion:]_block_invoke.47
- ___74-[CDPStateController authenticateAndGenerateNewRecoveryKeyWithCompletion:]_block_invoke.47.cold.1
- ___74-[CDPStateController updateLastSilentEscrowRecordRepairAttemptDate:error:]_block_invoke.80
- ___76-[CDPStateController shouldPerformSilentEscrowRecordRepairUsingCache:error:]_block_invoke.76
- ___79-[CDPProtectedCloudStorageProxyImpl edpPCSGuitarfishChangePassword:completion:]_block_invoke
- ___80-[CDPProtectedCloudStorageProxyImpl edpPCSGuitarfishSetupIdentities:completion:]_block_invoke
- ___81-[CDPProtectedCloudStorageProxyImpl edpPCSGuitarfishRepairIdentities:completion:]_block_invoke
- ___81-[CDPStateController shouldPerformAuthenticatedRepairWithOptionForceFetch:error:]_block_invoke.43
- ___81-[CDPStateController shouldPerformSilentEscrowRecordRepairUsingCache:completion:]_block_invoke.77
- ___82-[CDPStateController performEscrowRecordCheckWithContext:isBackground:completion:]_block_invoke.90
- ___82-[CDPStateController performEscrowRecordCheckWithContext:isBackground:completion:]_block_invoke.90.cold.1
- ___82-[CDPStateController verifyRecoveryKeyObservingSystemsHaveMatchingStateWithError:]_block_invoke.58
- ___83-[CDPProtectedCloudStorageProxyImpl edpPCSGuitarfishValidateIdentities:completion:]_block_invoke
- ___85-[CDPProtectedCloudStorageProxyImpl edpPCSGuitarfishGetRecoveryTokenInfo:completion:]_block_invoke
- ___block_descriptor_40_e8_32s_e34_v24?0"NSDictionary"8"NSError"16ls32l8
- ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e37_v32?0Q8"NSDictionary"16"NSError"24ls32l8s40l8
- ___block_descriptor_56_e8_32bs_e23_v32?0Q8Q16"NSError"24ls32l8
- ___block_descriptor_56_e8_32bs_e35_v40?0Q8Q16"NSArray"24"NSError"32ls32l8
- ___block_descriptor_56_e8_32bs_e40_v40?0Q8Q16"NSDictionary"24"NSError"32ls32l8
- ___block_descriptor_56_e8_32bs_e48_v48?0Q8Q16"NSArray"24"NSString"32"NSError"40ls32l8
- ___block_descriptor_56_e8_32s40r48r_e34_v24?0"NSDictionary"8"NSError"16ls32l8r40l8r48l8
- ___block_literal_global.189
- ___block_literal_global.43
- ___block_literal_global.46
- ___block_literal_global.79
- ___block_literal_global.82
- ___block_literal_global.87
- ___block_literal_global.91
- ___block_literal_global.95
- ___block_literal_global.99
- _isGuitarfishEnabled.enabled
- _isGuitarfishEnabled.once
- _kCDPAnalyticsEDPChangePasswordEvent
- _kCDPAnalyticsEDPEligibility
- _kCDPAnalyticsEDPHealth
- _kCDPAnalyticsEDPPasswordValidationEvent
- _kCDPAnalyticsEDPRecoveryTokenDontHaveKeyAlertEscapeOptionTappedEvent
- _kCDPAnalyticsEDPRecoveryTokenDontHaveKeyAlertPresentedEvent
- _kCDPAnalyticsEDPRecoveryTokenEntryScreenEscapeOptionTappedEvent
- _kCDPAnalyticsEDPRecoveryTokenEntryScreenLandingEvent
- _kCDPAnalyticsEDPRecoveryTokenFetchEvent
- _kCDPAnalyticsEDPRecoveryTokenInformationalScreenEscapeOptionTappedEvent
- _kCDPAnalyticsEDPRecoveryTokenInformationalScreenLandingEvent
- _kCDPAnalyticsEDPRecoveryTokenValidationEvent
- _kCDPAnalyticsEDPRepairFinishEvent
- _kCDPAnalyticsEDPRepairStartEvent
- _kCDPAnalyticsEDPResetProtectedDataEvent
- _kCDPAnalyticsEDPSendRecoveryTokenEvent
- _kCDPAnalyticsEDPSetupIdentitiesEvent
- _kCDPAnalyticsEDPSpyglassPaneEmailButtonTappedEvent
- _kCDPAnalyticsEDPSpyglassPaneLandingEvent
- _kCDPEventCountry
- _kEDPDataAccessDontHaveDataAccessKey
- _kEDPDataAccessDontHaveKey
- _kEDPDataAccessTryAgainLater
- _kPCSSetupRawPassword
- _objc_msgSend$_extractTokenNameFromConfig:finalize:
- _objc_msgSend$_parseEDPStateFromRawState:
- _objc_msgSend$_rawEDPHealthForAccount:
- _objc_msgSend$_updateEDPAttributesFromAccountCache
- _objc_msgSend$_updateEDPAttributesFromAccountCacheWithAccount:
- _objc_msgSend$_updateEDPWithAuthenticationResults:
- _objc_msgSend$cdpContext:promptForEDPRecoveryTokenWithValidator:successfulCDPRecoveryContinuationHandler:
- _objc_msgSend$cdp_indicatesEDPRecoveryTokenIsNeeded
- _objc_msgSend$componentsSeparatedByString:
- _objc_msgSend$createEDPLivenessDictionaryWithContext:completion:
- _objc_msgSend$edpHealth
- _objc_msgSend$edpRecoveryToken
- _objc_msgSend$edpState
- _objc_msgSend$edpStateForAccount:
- _objc_msgSend$fetchCompleted
- _objc_msgSend$fetchEDPTokenForContext:completion:
- _objc_msgSend$fetchGlobalConfigUsingCachePolicy:completion:
- _objc_msgSend$forceInteractiveCDPEDPRepair
- _objc_msgSend$isBeneficiaryFlow
- _objc_msgSend$isGuitarfishEnabled
- _objc_msgSend$passwordVersion
- _objc_msgSend$passwordVersionForAccount:
- _objc_msgSend$removeThisDeviceFromCircle:
- _objc_msgSend$repairEDPStateWithContext:completion:
- _objc_msgSend$repairEDPStateWithContext:uiProvider:completion:
- _objc_msgSend$replaceToken:withConfigToken:fallbackToken:
- _objc_msgSend$setAccountIsGuitarfish:
- _objc_msgSend$setFetchCompleted:
- _objc_msgSend$setTokenName:
- _objc_msgSend$setTokenNameMedium:
- _objc_msgSend$setTokenNameTitle:
- _objc_msgSend$srpIteration
- _objc_msgSend$srpProtocol
- _objc_msgSend$srpProtocolForAccount:
- _objc_msgSend$srpSalt
- _objc_msgSend$tokenName
- _objc_msgSend$tokenNameMedium
- _objc_msgSend$tokenNameTitle
- _objc_msgSend$validateEDPIdentitiesWithContext:uiProvider:completion:
- _objc_msgSend$validateEDPRecoveryToken:withContext:completion:
- _sharedInstance.instance
CStrings:
+ "@40@0:8@16Q24@32"
+ "B40@0:8@16Q24@32"
+ "CDPStringUtilities"
+ "Finished calling waitForPriorityViewKeychainDataRecovery didSync=%i error=%@"
+ "TB,R,N,V_isProxSignIn"
+ "_isProxSignIn"
+ "alphanumericCharacterSet"
+ "characterAtIndex:"
+ "characterIsMember:"
+ "isValidKeyLength:expectedLength:withSeparator:"
+ "keyWithGrouping:groupLength:separator:"
+ "sanitizedKeyInput:"
+ "stringWithCharacters:length:"
+ "substringWithRange:"
+ "uppercaseString"
- "\tInteractive Auth Button String: %@\n"
- "\tedpState: %ld\n"
- "\tforceInteractiveCDPEDPRepair: %d\n"
- "\toldPassword is %@ missing\n"
- "\tpassword is %@ missing\n"
- "\tpasswordVersion: %@\n"
- "\tsrpIteration is %@ missing\n"
- "\tsrpProtocol is %@ missing\n"
- "\tsrpSalt is %@ missing\n"
- "%s in CDPStateUIProviderProxy: Failed to prompt for EDP recovery token due to incomplete UI provider"
- "%s: Calling into daemon validator to repair EDP state"
- "%s: Calling into daemon validator to validate recovery token"
- "%s: Rejecting out-of-range EDP state (%@)."
- "%s: Unable to obtain the edpStateForAccount because AKAccountManager (%@) doesn't respond to selector."
- "%s: Unable to obtain the passwordVersionForAccount because AKAccountManager (%@) doesn't respond to selector."
- "%s: Unable to obtain the srpProtocolForAccount because AKAccountManager (%@) doesn't respond to selector."
- "-"
- "-[CDPContext _parseEDPStateFromRawState:]"
- "-[CDPContext _updateEDPAttributesFromAccountCacheWithAccount:]"
- "-[CDPRemoteDeviceSecretValidator repairEDPStateWithContext:completion:]"
- "-[CDPRemoteDeviceSecretValidator validateEDPRecoveryToken:withContext:completion:]"
- "-[CDPStateUIProviderProxy cdpContext:promptForEDPRecoveryTokenWithValidator:successfulCDPRecoveryContinuationHandler:]"
- "-[CDPStateUIProviderProxy cdpContext:promptForEDPRecoveryTokenWithValidator:successfulCDPRecoveryContinuationHandler:]_block_invoke"
- "A recovery token is required to repair EDP"
- "Attempted to prompt for EDP recovery token while in beneficiary flow. Doing nothing."
- "BEGIN [%lld]: GuitarfishChangePassword  enableTelemetry=YES "
- "BEGIN [%lld]: GuitarfishGetRecoveryTokenInfo  enableTelemetry=YES "
- "BEGIN [%lld]: GuitarfishRepair  enableTelemetry=YES "
- "BEGIN [%lld]: GuitarfishResetProtectedData  enableTelemetry=YES "
- "BEGIN [%lld]: GuitarfishSetup  enableTelemetry=YES "
- "BEGIN [%lld]: GuitarfishValidate  enableTelemetry=YES "
- "BEGIN [%lld]: RepairEDPState  enableTelemetry=YES "
- "CDPEDPConfigProvider"
- "Checking for EDP health status"
- "Creating EDP liveness health payload..."
- "Creating context for CDP & EDP Repair CFU"
- "Creating context for EDP Only Repair CFU"
- "EDP config is not a dictionary"
- "EDP livness dictionary=%@"
- "EDP repair completed didRepair=%{BOOL}d error=%@"
- "EDP_RECOVERY_KEY"
- "EDP_RECOVERY_KEY_MEDIUM"
- "EDP_RECOVERY_KEY_TITLECASE"
- "END [%lld] %fs: GuitarfishChangePassword  Error=%{public,signpost.telemetry:number1,name=Error}d "
- "END [%lld] %fs: GuitarfishGetRecoveryTokenInfo  Error=%{public,signpost.telemetry:number1,name=Error}d "
- "END [%lld] %fs: GuitarfishRepair  Error=%{public,signpost.telemetry:number1,name=Error}d "
- "END [%lld] %fs: GuitarfishResetProtectedData  Error=%{public,signpost.telemetry:number1,name=Error}d "
- "END [%lld] %fs: GuitarfishSetup  Error=%{public,signpost.telemetry:number1,name=Error}d "
- "END [%lld] %fs: GuitarfishValidate  Error=%{public,signpost.telemetry:number1,name=Error}d "
- "END [%lld] %fs: RepairEDPState  Error=%{public,signpost.telemetry:number1,name=Error}d "
- "Error getting cached EDP config. Error - %@"
- "Error getting fresh EDP config. Error - %@"
- "Failed to validate EDP identities with error: %@"
- "Failed to validate EDP identities: %{public}@, healthState: %ld"
- "Failed to validate token with error: %@"
- "Fetching EDP Token..."
- "Guitarfish Enabled: %{BOOL}d"
- "GuitarfishChangePassword"
- "GuitarfishGetRecoveryTokenInfo"
- "GuitarfishRepair"
- "GuitarfishResetProtectedData"
- "GuitarfishSetup"
- "GuitarfishValidate"
- "Localizable-EDP"
- "NOT"
- "No EDP config found in global config."
- "Recovery token was valid!"
- "RepairEDPState"
- "Requesting repair of EDP state..."
- "T@\"CDPCustodianRecoveryInfo\",&,N"
- "T@\"CUMessageSession\",&,N"
- "T@\"NSData\",&,N"
- "T@\"NSData\",C,N"
- "T@\"NSData\",C,N,V_srpSalt"
- "T@\"NSNumber\",C,N"
- "T@\"NSNumber\",C,N,V_passwordVersion"
- "T@\"NSNumber\",C,N,V_srpIteration"
- "T@\"NSString\",&,N,GtelemetryDeviceSessionID"
- "T@\"NSString\",&,N,V_edpRecoveryToken"
- "T@\"NSString\",C,N"
- "T@\"NSString\",C,N,V_interactiveAuthDefaultButtonString"
- "T@\"NSString\",C,N,V_recoveryToken"
- "T@\"NSString\",C,N,V_srpProtocol"
- "T@\"NSString\",C,V_tokenName"
- "T@\"NSString\",C,V_tokenNameMedium"
- "T@\"NSString\",C,V_tokenNameTitle"
- "TB,N,V__alwaysPromptForEDPRecoveryToken"
- "TB,N,V__forceEDPReset"
- "TB,N,V_forceInteractiveCDPEDPRepair"
- "TB,V_fetchCompleted"
- "TQ,N,V_edpHealth"
- "TQ,N,V_edpState"
- "Tq,N"
- "We failed to sync and now we failed to remove self form circle, nothing good will happen here"
- "We failed to sync but managed to get out of the circle, hopefully the next attempt will work"
- "XPC Error while repairing EDP state: %@"
- "__alwaysPromptForEDPRecoveryToken"
- "__forceEDPReset"
- "_alwaysPromptForEDPRecoveryToken"
- "_edpHealth"
- "_edpRecoveryToken"
- "_edpState"
- "_extractTokenNameFromConfig:finalize:"
- "_fetchCompleted"
- "_forceEDPReset"
- "_forceInteractiveCDPEDPRepair"
- "_interactiveAuthDefaultButtonString"
- "_parseEDPStateFromRawState:"
- "_passwordVersion"
- "_rawEDPHealthForAccount:"
- "_recoveryToken"
- "_srpIteration"
- "_srpProtocol"
- "_srpSalt"
- "_tokenName"
- "_tokenNameMedium"
- "_tokenNameTitle"
- "_updateEDPAttributesFromAccountCache"
- "_updateEDPAttributesFromAccountCacheWithAccount:"
- "_updateEDPWithAuthenticationResults:"
- "cdp/edp-health-liveness-payload"
- "cdp/edp-health-status"
- "cdp/edp-state-repair"
- "cdp/fetch-edp-token"
- "cdpContext:promptForEDPRecoveryTokenWithValidator:successfulCDPRecoveryContinuationHandler:"
- "cdp_indicatesEDPRecoveryTokenIsNeeded"
- "com.apple.corecdp.edpEmailRecoveryTokenButtonTapped"
- "com.apple.corecdp.edpRecoveryTokenInputEscapeOptionTapped"
- "com.apple.corecdp.edpRecoveryTokenInputLanding"
- "com.apple.corecdp.edpRecoveryTokenSpyglassLanding"
- "com.apple.corecdp.edpRepairEntry"
- "com.apple.corecdp.edpRepairFinish"
- "com.apple.corecdp.edpResetProtectedData"
- "com.apple.corecdp.fetchRecoveryToken"
- "com.apple.corecdp.passwordChange"
- "com.apple.corecdp.passwordValidation"
- "com.apple.corecdp.recoveryTokenInformationalAlertEscapeOffersPresented"
- "com.apple.corecdp.recoveryTokenInformationalAlertEscapeOptionTapped"
- "com.apple.corecdp.recoveryTokenInformationalEscapeOptionTapped"
- "com.apple.corecdp.recoveryTokenInformationalLanding"
- "com.apple.corecdp.recoveryTokenValidation"
- "com.apple.corecdp.sendRecoveryToken"
- "com.apple.corecdp.setUpIdentities"
- "com.apple.dataaccess.recoveryToken.accessDataLater"
- "com.apple.dataaccess.recoveryToken.dontHaveKey"
- "com.apple.dataaccess.recoverytoken.dontHave"
- "com.apple.protectedcloudstorage"
- "componentsSeparatedByString:"
- "contextForCDPEDPStateRepair"
- "contextForEDPStateRepair"
- "country"
- "createEDPLivenessDictionaryWithContext:completion:"
- "createEDPLivenessDictionaryWithContext:error:"
- "edp"
- "edpEligible"
- "edpHealth"
- "edpPCSGuitarfishChangePassword:completion:"
- "edpPCSGuitarfishGetRecoveryTokenInfo:completion:"
- "edpPCSGuitarfishRepairIdentities:completion:"
- "edpPCSGuitarfishSetupIdentities:completion:"
- "edpPCSGuitarfishValidateIdentities:completion:"
- "edpPCSResetProtectedData:completion:"
- "edpRecoveryToken"
- "edpState"
- "edpStateForAccount:"
- "fetchCompleted"
- "fetchConfig"
- "fetchEDPTokenForContext:completion:"
- "fetchEDPTokenWithCompletion:"
- "fetchGlobalConfigUsingCachePolicy:completion:"
- "forceInteractiveCDPEDPRepair"
- "interactiveAuthDefaultButtonString"
- "isGuitarfishEnabled"
- "kCDPEDPStateRepair"
- "kEDPOnlyStateRepair"
- "kPCSAuthenticateAppleID"
- "kPCSSetupGuitarfish"
- "kPCSSetupPasswordGeneration"
- "kPCSSetupRecoveryToken"
- "kPCSSetupVerifierIterationCount"
- "kPCSSetupVerifierProtocol"
- "kPCSSetupVerifierSalt"
- "kcdp_PCSGuitarfishRepairIdentities:completion:"
- "kcdp_PCSGuitarfishSetupIdentities:completion:"
- "kcdp_PCSGuitarfishValidateIdentities:completion:"
- "passwordVersion"
- "passwordVersionForAccount:"
- "recoveryToken"
- "repairEDPStateWithCompletion:"
- "repairEDPStateWithContext:completion:"
- "repairEDPStateWithContext:uiProvider:completion:"
- "rtName"
- "setAccountIsGuitarfish:"
- "setEdpHealth:"
- "setEdpRecoveryToken:"
- "setEdpState:"
- "setFetchCompleted:"
- "setForceInteractiveCDPEDPRepair:"
- "setInteractiveAuthDefaultButtonString:"
- "setPasswordVersion:"
- "setRecoveryToken:"
- "setSrpIteration:"
- "setSrpProtocol:"
- "setSrpSalt:"
- "setTokenName:"
- "setTokenNameMedium:"
- "setTokenNameTitle:"
- "set_alwaysPromptForEDPRecoveryToken:"
- "set_forceEDPReset:"
- "shortRTName"
- "srpIteration"
- "srpProtocol"
- "srpProtocolForAccount:"
- "srpSalt"
- "titleRTName"
- "tokenName"
- "tokenNameMedium"
- "tokenNameTitle"
- "v28@0:8@16B24"
- "v32@0:8@\"CDPContext\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"CDPContext\"16@?<v@?BB@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?Q@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?Q@\"NSArray\"@\"NSString\"@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?QB@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?QQ@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?QQ@\"NSError\">24"
- "v32@?0Q8@\"NSDictionary\"16@\"NSError\"24"
- "v32@?0Q8Q16@\"NSError\"24"
- "v40@0:8@\"CDPContext\"16@\"<CDPRemoteDeviceSecretValidatorProtocolInternal>\"24@?<v@?>32"
- "v40@0:8@\"CDPContext\"16@\"<CDPStateUIProviderInternal>\"24@?<v@?Q@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"CDPContext\"16@\"CDPRemoteDeviceSecretValidator\"24@?<v@?>32"
- "v40@?0Q8Q16@\"NSArray\"24@\"NSError\"32"
- "v40@?0Q8Q16@\"NSDictionary\"24@\"NSError\"32"
- "v48@?0Q8Q16@\"NSArray\"24@\"NSString\"32@\"NSError\"40"
- "validateEDPIdentitiesWithContext:completion:"
- "validateEDPIdentitiesWithContext:uiProvider:completion:"
- "validateEDPRecoveryToken:withContext:completion:"
- "{key.long.titlecase}"
- "{key.long}"
- "{key.medium}"

```
