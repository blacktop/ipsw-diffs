## AOSUI

> `/System/Library/PrivateFrameworks/AOSUI.framework/Versions/A/AOSUI`

```diff

-876.226.0.0.0
-  __TEXT.__text: 0x127124
+876.453.0.0.0
+  __TEXT.__text: 0x126698
   __TEXT.__auth_stubs: 0x1310
-  __TEXT.__objc_methlist: 0xe38c
+  __TEXT.__objc_methlist: 0x10bd4
   __TEXT.__const: 0x2d8
-  __TEXT.__cstring: 0x132e4
-  __TEXT.__oslogstring: 0xbde9
-  __TEXT.__gcc_except_tab: 0x18cc
+  __TEXT.__cstring: 0x133d8
+  __TEXT.__oslogstring: 0xbe13
+  __TEXT.__gcc_except_tab: 0x18c8
   __TEXT.__ustring: 0x132
   __TEXT.__dlopen_cstrs: 0x1f4
-  __TEXT.__unwind_info: 0x44e8
+  __TEXT.__unwind_info: 0x46a0
   __TEXT.__objc_classname: 0x2192
-  __TEXT.__objc_methname: 0x2a672
+  __TEXT.__objc_methname: 0x2a6c7
   __TEXT.__objc_methtype: 0x74e8
   __TEXT.__objc_stubs: 0x1a760
-  __DATA_CONST.__got: 0x1870
+  __DATA_CONST.__got: 0x1888
   __DATA_CONST.__const: 0xe58
   __DATA_CONST.__objc_classlist: 0x6a0
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8be0
+  __DATA_CONST.__objc_selrefs: 0x9630
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x478
   __DATA_CONST.__objc_arraydata: 0x108
   __AUTH_CONST.__auth_got: 0x998
-  __AUTH_CONST.__const: 0x4260
-  __AUTH_CONST.__cfstring: 0xce00
-  __AUTH_CONST.__objc_const: 0x337d0
+  __AUTH_CONST.__const: 0x4290
+  __AUTH_CONST.__cfstring: 0xcdc0
+  __AUTH_CONST.__objc_const: 0x2ed18
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH.__objc_data: 0x1950
-  __DATA.__objc_ivar: 0x1494
+  __DATA.__objc_ivar: 0x14a0
   __DATA.__data: 0x2298
   __DATA.__bss: 0x348
   __DATA.__common: 0x28

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4F14F32B-BCBA-3247-9B50-293DCF5AFF99
-  Functions: 7023
-  Symbols:   16805
-  CStrings:  12562
+  UUID: 21B0ED75-6D84-3ECC-A61B-8C6CA43411A5
+  Functions: 7147
+  Symbols:   16945
+  CStrings:  12559
 
Symbols:
+ +[AOSUIFeatureManager isLCInviteAcceptanceEnabled].cold.1
+ +[AOSUIImageFetcher sharedImageFetcher].cold.1
+ +[AOSUIProfilePictureStore sharedProfilePictureStoreForAccount:].cold.1
+ +[AOSUIProfileViewCacheController _cacheQueue].cold.1
+ +[AOSUIProfileViewUtility sharedProfileViewUtility].cold.1
+ +[AOSUISignInDataclassManager sharedManager].cold.1
+ +[AOSUISignOutController sharedInstance].cold.1
+ +[CastlePlugin sharedCastlePlugin].cold.1
+ +[MMAccountInterface scriptInterface].cold.1
+ +[MMAccountMgr sharedMgr].cold.1
+ +[MMAppDisplayUtilities _displayNameCache].cold.1
+ +[MMAppDisplayUtilities _imageCache].cold.1
+ +[MMBaseInterface scriptInterface].cold.1
+ +[MMCloudAccountInterface scriptInterface].cold.1
+ +[MMDiskManagement systemHasTRB].cold.1
+ +[MMFindMyMacService _updateQueue].cold.1
+ +[MMMessagesInterface scriptInterface].cold.1
+ +[MMPhoneNumberFormatter availableCountryCodes].cold.1
+ +[MMQuotaInterface scriptInterface].cold.1
+ +[MMServiceFactory defaultOrderedServiceIDs].cold.1
+ +[MMTermsOfServiceController _setTermsInProgress:].cold.1
+ +[MMUtilities upgradeLegacyPaneIDIfNecessary:].cold.1
+ +[MMWebProcessPlugInDelegateInterface remoteObjectInterface].cold.1
+ +[NSImage(Additions) imageNameForBundleID:].cold.1
+ +[_MMScriptResolver _resolverWithBlock:].cold.1
+ +[iCloudAccountDetailsControllerNew _requestQueue].cold.1
+ +[iCloudLocHelper localizationIdentifierForService:].cold.1
+ +[iCloudUtilities dataclassesToEnable].cold.1
+ +[iCloudUtilities sharedFollowUpController].cold.1
+ -[AOSUIAccountConversionSignOutFlowControllerDelegate initWithAccountManager:shouldRemoveAppleAccount:presentingWindow:].cold.2
+ -[AOSUIAccountConversionSignOutFlowControllerDelegate initWithAccountManager:shouldRemoveAppleAccount:presentingWindow:].cold.3
+ -[AOSUIBeneficiaryRadioListView addOptionsWithShareOptions:].cold.1
+ -[AOSUIMyBenefactorActionHandler _setupWindowWithContentViewController:]
+ -[AOSUIMyBenefactorActionHandler modalWindow]
+ -[AOSUIMyBenefactorActionHandler setModalWindow:]
+ -[AOSUIMyBeneficiaryActionHandler _setupWindowWithContentViewController:]
+ -[AOSUIMyBeneficiaryActionHandler modalWindow]
+ -[AOSUIMyBeneficiaryActionHandler setModalWindow:]
+ -[AOSUIMyCustodianActionHandler _setupWindowWithContentViewController:]
+ -[AOSUIMyCustodianActionHandler modalWindow]
+ -[AOSUIMyCustodianActionHandler setModalWindow:]
+ -[AOSUIPrivateConnectService icon].cold.1
+ -[AOSUIPrivateEmailService icon].cold.1
+ -[AOSUIProfilePictureStore _contactKeysToFetch].cold.1
+ -[AOSUIProfileViewCacheViewController initWithCacheData:].cold.1
+ -[AOSUISignOutFlowControllerDelegate initWithAccountManager:presentingWindow:].cold.1
+ -[AOSUISignOutFlowControllerDelegate initWithAccountManager:presentingWindow:].cold.2
+ -[AOSUISpyglassBaseViewController initWithAccountManager:].cold.1
+ -[CastlePlugin signInFailedMainThread:].cold.1
+ -[ImagePlaygroundService icon].cold.1
+ -[MMAccountMgr(MMAccountMgr_SetupAssistant) authenticateAccount:withPassword:delegatePlist:].cold.1
+ -[MMAccountMgr(MMAccountMgr_SetupAssistant) authenticateAccount:withPassword:withAuthResults:delegatePlist:].cold.1
+ -[MMBookmarksService icon].cold.1
+ -[MMCalendarsService icon].cold.1
+ -[MMContactsService icon].cold.1
+ -[MMFindMyMacService _fmmIcon].cold.1
+ -[MMFindMyMacService _fmmWarningIcon].cold.1
+ -[MMFindMyMacService _serviceEnableChanged:].cold.1
+ -[MMFindMyMacService _servicePropertiesChanged:].cold.1
+ -[MMICAWebKitViewController fidoRegister:userHandle:rpId:credentialName:excludedCredentials:promptTitle:promptHeader:promptBody:callback:].cold.2
+ -[MMICAWebKitViewController fidoRegister:userHandle:rpId:credentialName:excludedCredentials:promptTitle:promptHeader:promptBody:callback:].cold.3
+ -[MMICAWebKitViewController fidoVerify:allowedCredentials:rpId:promptTitle:promptHeader:promptBody:callback:].cold.2
+ -[MMICAWebKitViewController fidoVerify:allowedCredentials:rpId:promptTitle:promptHeader:promptBody:callback:].cold.3
+ -[MMKeychainService _enabledStateChanged:].cold.1
+ -[MMKeychainService _servicePropertiesChanged:].cold.1
+ -[MMKeychainService _stateChanged:].cold.1
+ -[MMMBWebKitViewController mmWebKitControllerConfigureForFrame:].cold.1
+ -[MMMBWebKitViewController mmWebKitControllerConfigureForFrame:].cold.2
+ -[MMMBWebKitViewController mmWebKitControllerConfigureForFrame:].cold.3
+ -[MMMailService icon].cold.1
+ -[MMMediaStreamService _serviceEnableChanged:].cold.1
+ -[MMMediaStreamService _servicePropertiesChanged:].cold.1
+ -[MMMediaStreamService icon].cold.1
+ -[MMMobileDocumentsService _serviceEnableChanged:].cold.1
+ -[MMMobileDocumentsService icon].cold.1
+ -[MMNotesService icon].cold.1
+ -[MMPromptForLocalSecret userFullName].cold.1
+ -[MMRemindersService icon].cold.1
+ -[MMURLRequestFactory _premiumFeaturesURLRequest:queryParams:].cold.2
+ -[MMURLRequestFactory accountContinuationURLRequest:andError:].cold.1
+ -[MMURLRequestFactory accountContinuationURLRequest:andError:].cold.2
+ -[MMURLRequestFactory accountContinuationURLRequest:andError:].cold.3
+ -[MMURLRequestFactory accountCreationURLRequest:].cold.1
+ -[MMURLRequestFactory accountCreationURLRequest:].cold.2
+ -[MMURLRequestFactory accountCreationURLRequest:].cold.3
+ -[MMURLRequestFactory accountMailCreationURLRequest:andError:].cold.1
+ -[MMURLRequestFactory accountMailCreationURLRequest:andError:].cold.2
+ -[MMURLRequestFactory accountMailCreationURLRequest:andError:].cold.3
+ -[MMURLRequestFactory accountNotesCreationURLRequest:andError:].cold.1
+ -[MMURLRequestFactory accountNotesCreationURLRequest:andError:].cold.2
+ -[MMURLRequestFactory accountNotesCreationURLRequest:andError:].cold.3
+ -[MMURLRequestFactory accountNotesCreationURLRequest:andError:].cold.4
+ -[MMURLRequestFactory accountQuotaURLRequest:].cold.2
+ -[MMURLRequestFactory accountStorageURLRequest:dsid:authTokent:storageInfo:withQueryParam:].cold.4
+ -[MMURLRequestFactory accountStorageURLRequestForAccount:withQueryParam:].cold.3
+ -[MMURLRequestFactory(MBAdditions) urlRequestForMBAccoutContinuation:continutationHeaderValue:error:].cold.1
+ -[MMURLRequestFactory(MBAdditions) urlRequestForMBAccoutContinuation:continutationHeaderValue:error:].cold.2
+ -[MMURLRequestFactory(MBAdditions) urlRequestForMBAccoutContinuation:continutationHeaderValue:error:].cold.3
+ -[MMWebKitViewController initForInternetPrivacyWithAccountID:].cold.1
+ -[MMWebKitViewController initForMailAccountCreationWithAccountID:].cold.1
+ -[MMWebKitViewController initForMatterhornUpsell:].cold.1
+ -[MMWebKitViewController initForNotesAccountCreationWithAccountID:].cold.1
+ -[MMWebKitViewController initForStorageManagementWithAccountID:].cold.1
+ -[MMWebKitViewController initForStorageUpgradeWithAccountID:].cold.1
+ -[MMWebKitViewController initForSubscriptionFeaturesWithAccountID:].cold.1
+ -[MMWebKitViewController initForTermsOfServiceWithAccountID:password:authenticationResults:].cold.1
+ -[MMWebKitViewController mmWebKitControllerConfigureForFrame:].cold.1
+ -[MMWebKitViewController mmWebKitControllerConfigureForFrame:].cold.2
+ -[MMWebKitViewController mmWebKitControllerConfigureForFrame:].cold.3
+ -[MM_Account _handleBeginMigrationNotification:].cold.1
+ -[MM_Account _handleBeginMigrationNotification:].cold.2
+ -[MM_Account _handleEndMigrationNotification:].cold.1
+ -[MM_Account _handleEndMigrationNotification:].cold.2
+ -[MM_Account(Preflight) preflightDelete:withWindow:].cold.1
+ -[_MMScriptResolver _resolveWithToken:arguments:].cold.1
+ -[_MMScriptResolver _resolveWithToken:arguments:].cold.2
+ -[iCloudFreeformService icon].cold.1
+ -[iCloudHomeService icon].cold.1
+ -[iCloudMessagesService icon].cold.1
+ -[iCloudNewsService icon].cold.1
+ -[iCloudPhoneFaceTimeService icon].cold.1
+ -[iCloudSettingsSyncService icon].cold.1
+ -[iCloudSiriService icon].cold.1
+ -[iCloudStocksService icon].cold.1
+ -[iCloudWalletService icon].cold.1
+ JS_GetDataclassState.cold.3
+ JS_RegisterWithAppleId.cold.2
+ JS_RegisterWithAppleId.cold.3
+ JS_SetDataclassState.cold.3
+ JS_SetTermsContext.cold.3
+ JS_TransferCookie.cold.3
+ JS_TransferCookie.cold.4
+ OBJC_IVAR_$_AOSUIMyBenefactorActionHandler._modalWindow
+ OBJC_IVAR_$_AOSUIMyBeneficiaryActionHandler._modalWindow
+ OBJC_IVAR_$_AOSUIMyCustodianActionHandler._modalWindow
+ Shared_JS_GetAuthToken.cold.2
+ _AOSUILogSystem.cold.1
+ _AOSUISignpostGetNanoseconds.cold.1
+ _AOSUISignpostLogSystem.cold.1
+ __100-[MMPasswordChangeWebKitViewController runPasswordChangeSheetForWindow:accountID:completionHandler:]_block_invoke.62
+ __100-[MMPasswordChangeWebKitViewController runPasswordChangeSheetForWindow:accountID:completionHandler:]_block_invoke.66
+ __100-[MMPasswordChangeWebKitViewController runPasswordChangeSheetForWindow:accountID:completionHandler:]_block_invoke.77
+ __105-[MMKeychainService _handleDidForgetSheet:window:shouldRegister:password:pet:firstDevice:alreadyPending:]_block_invoke.280
+ __105-[MMKeychainService _handleDidForgetSheet:window:shouldRegister:password:pet:firstDevice:alreadyPending:]_block_invoke.293
+ __105-[MMKeychainService _handleDidForgetSheet:window:shouldRegister:password:pet:firstDevice:alreadyPending:]_block_invoke.302
+ __105-[MMKeychainService _handleDidForgetSheet:window:shouldRegister:password:pet:firstDevice:alreadyPending:]_block_invoke_2.283
+ __105-[MMKeychainService _handleDidForgetSheet:window:shouldRegister:password:pet:firstDevice:alreadyPending:]_block_invoke_2.294
+ __105-[MMKeychainService _handleDidForgetSheet:window:shouldRegister:password:pet:firstDevice:alreadyPending:]_block_invoke_3.295
+ __105-[MMKeychainService _handleDidForgetSheet:window:shouldRegister:password:pet:firstDevice:alreadyPending:]_block_invoke_4.296
+ __105-[MMKeychainService _handleDidForgetSheet:window:shouldRegister:password:pet:firstDevice:alreadyPending:]_block_invoke_5.297
+ __105-[MMKeychainService _handleDidForgetSheet:window:shouldRegister:password:pet:firstDevice:alreadyPending:]_block_invoke_6.298
+ __105-[MMKeychainService _handleDidForgetSheet:window:shouldRegister:password:pet:firstDevice:alreadyPending:]_block_invoke_6.298.cold.1
+ __105-[MMKeychainService _handleDidForgetSheet:window:shouldRegister:password:pet:firstDevice:alreadyPending:]_block_invoke_7.299
+ __107-[MMKeychainService _handleHardLimitReset:shouldRegister:password:pet:didReset:modifiesCircle:firstDevice:]_block_invoke.268
+ __107-[MMKeychainService _handleHardLimitReset:shouldRegister:password:pet:didReset:modifiesCircle:firstDevice:]_block_invoke.268.cold.1
+ __107-[MMKeychainService _handleHardLimitReset:shouldRegister:password:pet:didReset:modifiesCircle:firstDevice:]_block_invoke.270
+ __107-[MMKeychainService _handleHardLimitReset:shouldRegister:password:pet:didReset:modifiesCircle:firstDevice:]_block_invoke_2.269
+ __112-[MMKeychainService _finishRequestApproval:secureBackupEnabled:alreadyPending:registerCredentials:password:pet:]_block_invoke.192
+ __112-[MMKeychainService _finishRequestApproval:secureBackupEnabled:alreadyPending:registerCredentials:password:pet:]_block_invoke.193
+ __112-[MMKeychainService _finishRequestApproval:secureBackupEnabled:alreadyPending:registerCredentials:password:pet:]_block_invoke_2.194
+ __132-[MMKeychainService _handleCredentialVerificationIfNeeded:shouldNest:title:message:authenticatedHandler:cancelHandler:errorHandler:]_block_invoke.611
+ __132-[MMKeychainService _handleCredentialVerificationIfNeeded:shouldNest:title:message:authenticatedHandler:cancelHandler:errorHandler:]_block_invoke.614
+ __31-[CastlePlugin reauthenticate:]_block_invoke.287
+ __34-[MMKeychainService showMoreInfo:]_block_invoke.104
+ __34-[MMKeychainService showMoreInfo:]_block_invoke.107
+ __34-[MMKeychainService showMoreInfo:]_block_invoke.109
+ __34-[MMKeychainService showMoreInfo:]_block_invoke.116
+ __34-[MMKeychainService showMoreInfo:]_block_invoke_2.117
+ __36-[MMKeychainService handleAEEvents:]_block_invoke.118
+ __36-[MMKeychainService handleAEEvents:]_block_invoke_2.119
+ __36-[MMKeychainService handleAEEvents:]_block_invoke_3.120
+ __36-[MMKeychainService handleAEEvents:]_block_invoke_4.121
+ __42-[MMKeychainService _enabledStateChanged:]_block_invoke.511
+ __43-[MMKeychainService handleEnable:creating:]_block_invoke.88
+ __45-[MMICAWebKitViewController getWalrusStatus:]_block_invoke.702
+ __46-[MMKeychainOptionsController detailsPressed:]_block_invoke.157
+ __46-[MMKeychainService _handleManaullyResetSheet]_block_invoke.362
+ __46-[MMKeychainService _handleManaullyResetSheet]_block_invoke_2.363
+ __48-[MMICAWebKitViewController getWebAccessStatus:]_block_invoke.720
+ __48-[MMKeychainService _updateStatusWithICDPState:]_block_invoke.125
+ __50-[MMOutOfNetworkSheetController showFailureAlert:]_block_invoke.cold.1
+ __50-[MMOutOfNetworkSheetController showFailureAlert:]_block_invoke.cold.2
+ __51-[MMICAWebKitViewController validateLocalPassword:]_block_invoke.587
+ __51-[MMICAWebKitViewController validateLocalPassword:]_block_invoke.591
+ __51-[MMKeychainService _handleHardLimitRecoveryError:]_block_invoke.255
+ __52-[MM_Account(Preflight) preflightDelete:withWindow:]_block_invoke.247
+ __55-[MMKeychainService showCDPEnableSheet:withCompletion:]_block_invoke.578
+ __57-[MMKeychainService mmCSCRecoveryControllerDidEnd:error:]_block_invoke.632
+ __57-[MMKeychainService showCDPDeletionSheet:withCompletion:]_block_invoke.596
+ __57-[MMKeychainService showCDPDeletionSheet:withCompletion:]_block_invoke.596.cold.1
+ __57-[MMKeychainService showCDPDeletionSheet:withCompletion:]_block_invoke.597
+ __58-[MMKeychainOptionsController _finishSavingAccountDetails]_block_invoke.141
+ __59-[iCloudAccountDetailsControllerNew _handleInvalidGSToken:]_block_invoke.168
+ __60-[MMKeychainService _handleSecurityCodeResetAuthentication:]_block_invoke.429
+ __60-[MMKeychainService _handleSecurityCodeResetAuthentication:]_block_invoke_2.435
+ __63-[MMKeychainService _handleAlreadyPending:secureBackupEnabled:]_block_invoke.183
+ __63-[MMKeychainService _handleAlreadyPending:secureBackupEnabled:]_block_invoke_2.186
+ __63-[MMKeychainService _handleAlreadyPending:secureBackupEnabled:]_block_invoke_3.187
+ __64-[MMICAWebKitViewController reAuthenticateWithAuthKit:callback:]_block_invoke.818
+ __64-[MMICAWebKitViewController reAuthenticateWithAuthKit:callback:]_block_invoke.819
+ __64-[MMKeychainService handleCDPDeletionResponse:successful:error:]_block_invoke.601
+ __67-[AOSUISignOutController signOutAccount:window:options:completion:]_block_invoke.80
+ __67-[AOSUISignOutController signOutAccount:window:options:completion:]_block_invoke.81
+ __68-[MMFindMyMacService showiCloudPasswordSheet:withCompletionHandler:]_block_invoke.279
+ __68-[MMFindMyMacService showiCloudPasswordSheet:withCompletionHandler:]_block_invoke.282
+ __68-[MMFindMyMacService showiCloudPasswordSheet:withCompletionHandler:]_block_invoke.285
+ __68-[MMFindMyMacService showiCloudPasswordSheet:withCompletionHandler:]_block_invoke_2.286
+ __71-[iCloudAccountDetailsWebTabView icaWebKitViewControllerDidFail:error:]_block_invoke.247
+ __75-[MMICAWebKitViewController openAccountRecoveryContactsListViewController:]_block_invoke.787
+ __76-[MMICAWebKitViewController setWalrusStatus:successCallback:acceptCallback:]_block_invoke.693
+ __76-[MMICAWebKitViewController setWalrusStatus:successCallback:acceptCallback:]_block_invoke.693.cold.1
+ __77-[MMICAWebKitViewController retriveFromServer:callback:fallBackToLocal:dsid:]_block_invoke.753
+ __78-[MMKeychainService _completeEnable:registerCredentials:usingPassword:andPET:]_block_invoke.97
+ __78-[MMKeychainService _completeEnable:registerCredentials:usingPassword:andPET:]_block_invoke_2.98
+ __79-[MMICAWebKitViewController setWebAccessStatus:successCallback:acceptCallback:]_block_invoke.709
+ __79-[MMICAWebKitViewController setWebAccessStatus:successCallback:acceptCallback:]_block_invoke.709.cold.1
+ __81-[MMKeychainService _finishManuallyResetSheet:shouldRestore:withPassword:andPet:]_block_invoke.375
+ __87-[AOSUISignOutController _finishDeletingAccount:window:withActions:options:completion:]_block_invoke.90
+ __87-[AOSUISignOutController _finishDeletingAccount:window:withActions:options:completion:]_block_invoke.91
+ __JS_DisableAndDeleteCloudSyncWithCompletion_block_invoke.447
+ __JS_GetAbsintheToken_block_invoke.376
+ __JS_TransferCookie_block_invoke.465
+ ___50-[AOSUIMyBeneficiaryActionHandler _showAccessKey:]_block_invoke
+ ___block_descriptor_64_e8_32s40r48r56w_e5_v8?0l
+ ___copy_helper_block_e8_32s40r48r56w
+ ___destroy_helper_block_e8_32s40r48r56w
+ __block_literal_global.171
+ __block_literal_global.185
+ __block_literal_global.196
+ __block_literal_global.215
+ __block_literal_global.282
+ __block_literal_global.295
+ __block_literal_global.304
+ __block_literal_global.346
+ __block_literal_global.417
+ __block_literal_global.421
+ __block_literal_global.431
+ __block_literal_global.568
+ __block_literal_global.680
+ __block_literal_global.70
+ __block_literal_global.72
+ __block_literal_global.73
+ __block_literal_global.748
+ _objc_msgSend$setPreventsApplicationTerminationWhenModal:
+ addFamilyDispatchQueue.cold.1
+ appListDispatchQueue.cold.1
+ fmmDispatchQueue.cold.1
- -[MMAOSKeychainWrapper getAttributesForKeys:].cold.1
- _OUTLINED_FUNCTION_22
- _OUTLINED_FUNCTION_23
- __100-[MMPasswordChangeWebKitViewController runPasswordChangeSheetForWindow:accountID:completionHandler:]_block_invoke.70
- __100-[MMPasswordChangeWebKitViewController runPasswordChangeSheetForWindow:accountID:completionHandler:]_block_invoke.74
- __100-[MMPasswordChangeWebKitViewController runPasswordChangeSheetForWindow:accountID:completionHandler:]_block_invoke.85
- __105-[MMKeychainService _handleDidForgetSheet:window:shouldRegister:password:pet:firstDevice:alreadyPending:]_block_invoke.288
- __105-[MMKeychainService _handleDidForgetSheet:window:shouldRegister:password:pet:firstDevice:alreadyPending:]_block_invoke.301
- __105-[MMKeychainService _handleDidForgetSheet:window:shouldRegister:password:pet:firstDevice:alreadyPending:]_block_invoke.310
- __105-[MMKeychainService _handleDidForgetSheet:window:shouldRegister:password:pet:firstDevice:alreadyPending:]_block_invoke_2.291
- __105-[MMKeychainService _handleDidForgetSheet:window:shouldRegister:password:pet:firstDevice:alreadyPending:]_block_invoke_2.302
- __105-[MMKeychainService _handleDidForgetSheet:window:shouldRegister:password:pet:firstDevice:alreadyPending:]_block_invoke_3.303
- __105-[MMKeychainService _handleDidForgetSheet:window:shouldRegister:password:pet:firstDevice:alreadyPending:]_block_invoke_4.304
- __105-[MMKeychainService _handleDidForgetSheet:window:shouldRegister:password:pet:firstDevice:alreadyPending:]_block_invoke_5.305
- __105-[MMKeychainService _handleDidForgetSheet:window:shouldRegister:password:pet:firstDevice:alreadyPending:]_block_invoke_6.306
- __105-[MMKeychainService _handleDidForgetSheet:window:shouldRegister:password:pet:firstDevice:alreadyPending:]_block_invoke_6.306.cold.1
- __105-[MMKeychainService _handleDidForgetSheet:window:shouldRegister:password:pet:firstDevice:alreadyPending:]_block_invoke_7.307
- __107-[MMKeychainService _handleHardLimitReset:shouldRegister:password:pet:didReset:modifiesCircle:firstDevice:]_block_invoke.276
- __107-[MMKeychainService _handleHardLimitReset:shouldRegister:password:pet:didReset:modifiesCircle:firstDevice:]_block_invoke.276.cold.1
- __107-[MMKeychainService _handleHardLimitReset:shouldRegister:password:pet:didReset:modifiesCircle:firstDevice:]_block_invoke.278
- __107-[MMKeychainService _handleHardLimitReset:shouldRegister:password:pet:didReset:modifiesCircle:firstDevice:]_block_invoke_2.277
- __112-[MMKeychainService _finishRequestApproval:secureBackupEnabled:alreadyPending:registerCredentials:password:pet:]_block_invoke.200
- __112-[MMKeychainService _finishRequestApproval:secureBackupEnabled:alreadyPending:registerCredentials:password:pet:]_block_invoke.201
- __112-[MMKeychainService _finishRequestApproval:secureBackupEnabled:alreadyPending:registerCredentials:password:pet:]_block_invoke_2.202
- __132-[MMKeychainService _handleCredentialVerificationIfNeeded:shouldNest:title:message:authenticatedHandler:cancelHandler:errorHandler:]_block_invoke.619
- __132-[MMKeychainService _handleCredentialVerificationIfNeeded:shouldNest:title:message:authenticatedHandler:cancelHandler:errorHandler:]_block_invoke.622
- __31-[CastlePlugin reauthenticate:]_block_invoke.295
- __34-[MMKeychainService showMoreInfo:]_block_invoke.112
- __34-[MMKeychainService showMoreInfo:]_block_invoke.115
- __34-[MMKeychainService showMoreInfo:]_block_invoke.117
- __34-[MMKeychainService showMoreInfo:]_block_invoke.124
- __34-[MMKeychainService showMoreInfo:]_block_invoke_2.125
- __36-[MMKeychainService handleAEEvents:]_block_invoke.126
- __36-[MMKeychainService handleAEEvents:]_block_invoke_2.127
- __36-[MMKeychainService handleAEEvents:]_block_invoke_3.128
- __36-[MMKeychainService handleAEEvents:]_block_invoke_4.129
- __42-[MMKeychainService _enabledStateChanged:]_block_invoke.519
- __43-[MMKeychainService handleEnable:creating:]_block_invoke.96
- __45-[MMICAWebKitViewController getWalrusStatus:]_block_invoke.710
- __46-[MMKeychainOptionsController detailsPressed:]_block_invoke.165
- __46-[MMKeychainService _handleManaullyResetSheet]_block_invoke.370
- __46-[MMKeychainService _handleManaullyResetSheet]_block_invoke_2.371
- __48-[MMICAWebKitViewController getWebAccessStatus:]_block_invoke.728
- __48-[MMKeychainService _updateStatusWithICDPState:]_block_invoke.133
- __51-[MMICAWebKitViewController validateLocalPassword:]_block_invoke.595
- __51-[MMICAWebKitViewController validateLocalPassword:]_block_invoke.599
- __51-[MMKeychainService _handleHardLimitRecoveryError:]_block_invoke.263
- __52-[MM_Account(Preflight) preflightDelete:withWindow:]_block_invoke.241
- __55-[MMKeychainService showCDPEnableSheet:withCompletion:]_block_invoke.586
- __57-[MMKeychainService mmCSCRecoveryControllerDidEnd:error:]_block_invoke.640
- __57-[MMKeychainService showCDPDeletionSheet:withCompletion:]_block_invoke.604
- __57-[MMKeychainService showCDPDeletionSheet:withCompletion:]_block_invoke.604.cold.1
- __57-[MMKeychainService showCDPDeletionSheet:withCompletion:]_block_invoke.605
- __58-[MMKeychainOptionsController _finishSavingAccountDetails]_block_invoke.149
- __59-[iCloudAccountDetailsControllerNew _handleInvalidGSToken:]_block_invoke.176
- __60-[MMKeychainService _handleSecurityCodeResetAuthentication:]_block_invoke.437
- __60-[MMKeychainService _handleSecurityCodeResetAuthentication:]_block_invoke_2.443
- __63-[MMKeychainService _handleAlreadyPending:secureBackupEnabled:]_block_invoke.191
- __63-[MMKeychainService _handleAlreadyPending:secureBackupEnabled:]_block_invoke_2.194
- __63-[MMKeychainService _handleAlreadyPending:secureBackupEnabled:]_block_invoke_3.195
- __64-[MMICAWebKitViewController reAuthenticateWithAuthKit:callback:]_block_invoke.826
- __64-[MMICAWebKitViewController reAuthenticateWithAuthKit:callback:]_block_invoke.827
- __64-[MMKeychainService handleCDPDeletionResponse:successful:error:]_block_invoke.609
- __67-[AOSUISignOutController signOutAccount:window:options:completion:]_block_invoke.74
- __67-[AOSUISignOutController signOutAccount:window:options:completion:]_block_invoke.75
- __68-[MMFindMyMacService showiCloudPasswordSheet:withCompletionHandler:]_block_invoke.287
- __68-[MMFindMyMacService showiCloudPasswordSheet:withCompletionHandler:]_block_invoke.290
- __68-[MMFindMyMacService showiCloudPasswordSheet:withCompletionHandler:]_block_invoke.293
- __68-[MMFindMyMacService showiCloudPasswordSheet:withCompletionHandler:]_block_invoke_2.294
- __71-[iCloudAccountDetailsWebTabView icaWebKitViewControllerDidFail:error:]_block_invoke.255
- __75-[MMICAWebKitViewController openAccountRecoveryContactsListViewController:]_block_invoke.795
- __76-[MMICAWebKitViewController setWalrusStatus:successCallback:acceptCallback:]_block_invoke.701
- __76-[MMICAWebKitViewController setWalrusStatus:successCallback:acceptCallback:]_block_invoke.701.cold.1
- __77-[MMICAWebKitViewController retriveFromServer:callback:fallBackToLocal:dsid:]_block_invoke.761
- __78-[MMKeychainService _completeEnable:registerCredentials:usingPassword:andPET:]_block_invoke.105
- __78-[MMKeychainService _completeEnable:registerCredentials:usingPassword:andPET:]_block_invoke_2.106
- __79-[MMICAWebKitViewController setWebAccessStatus:successCallback:acceptCallback:]_block_invoke.717
- __79-[MMICAWebKitViewController setWebAccessStatus:successCallback:acceptCallback:]_block_invoke.717.cold.1
- __81-[MMKeychainService _finishManuallyResetSheet:shouldRestore:withPassword:andPet:]_block_invoke.383
- __87-[AOSUISignOutController _finishDeletingAccount:window:withActions:options:completion:]_block_invoke.84
- __87-[AOSUISignOutController _finishDeletingAccount:window:withActions:options:completion:]_block_invoke.85
- __JS_DisableAndDeleteCloudSyncWithCompletion_block_invoke.455
- __JS_GetAbsintheToken_block_invoke.384
- __JS_TransferCookie_block_invoke.473
- __block_literal_global.179
- __block_literal_global.201
- __block_literal_global.204
- __block_literal_global.209
- __block_literal_global.290
- __block_literal_global.303
- __block_literal_global.312
- __block_literal_global.354
- __block_literal_global.425
- __block_literal_global.429
- __block_literal_global.439
- __block_literal_global.576
- __block_literal_global.64
- __block_literal_global.66
- __block_literal_global.688
- __block_literal_global.756
- __block_literal_global.81
- _objc_msgSend$containsString:
CStrings:
+ "ACCOUNT_DETAILS_MESSAGE_REBRAND"
+ "ACCOUNT_SYNC_ACCEPT_APPLICANTS_MESSAGE-%@-%@_REBRAND"
+ "ACCOUNT_SYNC_AUTHENTICATION_CREATE_KEYCHAIN_TITLE_REBRAND"
+ "ACCOUNT_SYNC_AUTHENTICATION_FIRST_DEVICE_TITLE_REBRAND"
+ "ACCOUNT_SYNC_AUTHENTICATION_MESSAGE-%@_REBRAND"
+ "ACCOUNT_SYNC_AUTHENTICATION_PENDING_RESET_TITLE_REBRAND"
+ "ACCOUNT_SYNC_AUTHENTICATION_REQUEST_APPROVAL_TITLE_REBRAND"
+ "ACCOUNT_SYNC_AUTHENTICATION_RESET_TITLE_REBRAND"
+ "ACCOUNT_SYNC_AUTHENTICATION_UPDATE_KEYCHAIN_TITLE_REBRAND"
+ "ACCOUNT_SYNC_AUTHENTICATION_UPDATE_TITLE_REBRAND"
+ "ALREADY_SIGNED_IN_TOPLEVEL_INFO_REBRAND"
+ "APPLEID_LABEL_REBRAND"
+ "AVC_NO_NETWORK_ACCOUNT_SETUP_REBRAND"
+ "AVC_SERVER_ERROR_ACCOUNT_SETUP_REBRAND"
+ "FMM_DISABLE_MESSAGE_REBRAND"
+ "FMM_DISABLE_TITLE_REBRAND"
+ "GSF_BAD_LOGIN_TITLE_REBRAND"
+ "LCInvite: isEnabled in Defaults: %{BOOL}d"
+ "PASSWORD_CHANGE_MESSAGE_REBRAND"
+ "REAUTHVIEW_TEXT_REBRAND"
+ "REAUTH_FORMAT_REBRAND"
+ "RENEW_CREDENTIALS_TITLE_REBRAND"
+ "TERMS_RENEW_CREDENTIALS_TITLE_REBRAND"
+ "TURN_OFF_KEYCHAIN_AUTHENTICATION_TITLE_REBRAND"
+ "USER_NAME_LABEL_REBRAND"
+ "VERIFICATION_CODE_DESCRIPTION_REBRAND"
+ "VERIFICATION_CODE_FAILED_REBRAND"
+ "VETTING_FAILURE_ALERT_BODY_INITIATE_TOO_MANY_VETS_EMAIL_REBRAND"
+ "VETTING_FAILURE_ALERT_BODY_INITIATE_TOO_MANY_VETS_NUMBER_REBRAND"
+ "VETTING_FAILURE_ALERT_BODY_INITIATE_VETTED_TO_CALLER_ERROR_EMAIL_NO_APPLE_ID_REBRAND"
+ "VETTING_FAILURE_ALERT_BODY_INITIATE_VETTED_TO_CALLER_ERROR_EMAIL_REBRAND"
+ "VETTING_FAILURE_ALERT_BODY_INITIATE_VETTED_TO_CALLER_ERROR_PHONE_NO_APPLE_ID_REBRAND"
+ "VETTING_FAILURE_ALERT_BODY_INITIATE_VETTED_TO_CALLER_ERROR_PHONE_REBRAND"
+ "VETTING_FAILURE_ALERT_BODY_INITIATE_VETTED_TO_OTHER_EMAIL_REBRAND"
+ "VETTING_FAILURE_ALERT_BODY_INITIATE_VETTED_TO_OTHER_NUMBER_REBRAND"
+ "setPreventsApplicationTerminationWhenModal:"
+ "signOutFlowController:startSignOutForAccount:completion:"
- "AABranding"
- "ACCOUNT_DETAILS_MESSAGE"
- "ACCOUNT_SYNC_ACCEPT_APPLICANTS_MESSAGE-%@-%@"
- "ACCOUNT_SYNC_AUTHENTICATION_CREATE_KEYCHAIN_TITLE"
- "ACCOUNT_SYNC_AUTHENTICATION_FIRST_DEVICE_TITLE"
- "ACCOUNT_SYNC_AUTHENTICATION_MESSAGE-%@"
- "ACCOUNT_SYNC_AUTHENTICATION_PENDING_RESET_TITLE"
- "ACCOUNT_SYNC_AUTHENTICATION_REQUEST_APPROVAL_TITLE"
- "ACCOUNT_SYNC_AUTHENTICATION_RESET_TITLE"
- "ACCOUNT_SYNC_AUTHENTICATION_UPDATE_KEYCHAIN_TITLE"
- "ACCOUNT_SYNC_AUTHENTICATION_UPDATE_TITLE"
- "ALREADY_SIGNED_IN_TOPLEVEL_INFO"
- "APPLEID_LABEL"
- "AVC_NO_NETWORK_ACCOUNT_SETUP"
- "AVC_SERVER_ERROR_ACCOUNT_SETUP"
- "FMM_DISABLE_MESSAGE"
- "FMM_DISABLE_TITLE"
- "GSF_BAD_LOGIN_TITLE"
- "PASSWORD_CHANGE_MESSAGE"
- "REAUTHVIEW_TEXT"
- "REAUTH_FORMAT"
- "REBRAND"
- "RENEW_CREDENTIALS_TITLE"
- "TERMS_RENEW_CREDENTIALS_TITLE"
- "TURN_OFF_KEYCHAIN_AUTHENTICATION_TITLE"
- "USER_NAME_LABEL"
- "VERIFICATION_CODE_DESCRIPTION"
- "VERIFICATION_CODE_FAILED"
- "VETTING_FAILURE_ALERT_BODY_INITIATE_TOO_MANY_VETS_EMAIL"
- "VETTING_FAILURE_ALERT_BODY_INITIATE_TOO_MANY_VETS_NUMBER"
- "VETTING_FAILURE_ALERT_BODY_INITIATE_VETTED_TO_CALLER_ERROR_EMAIL"
- "VETTING_FAILURE_ALERT_BODY_INITIATE_VETTED_TO_CALLER_ERROR_EMAIL_NO_APPLE_ID"
- "VETTING_FAILURE_ALERT_BODY_INITIATE_VETTED_TO_CALLER_ERROR_PHONE"
- "VETTING_FAILURE_ALERT_BODY_INITIATE_VETTED_TO_CALLER_ERROR_PHONE_NO_APPLE_ID"
- "VETTING_FAILURE_ALERT_BODY_INITIATE_VETTED_TO_OTHER_EMAIL"
- "VETTING_FAILURE_ALERT_BODY_INITIATE_VETTED_TO_OTHER_NUMBER"
- "_REBRAND"
- "containsString:"

```
