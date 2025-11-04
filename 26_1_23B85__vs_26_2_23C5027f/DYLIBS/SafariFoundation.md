## SafariFoundation

> `/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation`

```diff

-622.2.11.10.8
-  __TEXT.__text: 0x285c4
-  __TEXT.__auth_stubs: 0xa40
-  __TEXT.__objc_methlist: 0x1e14
-  __TEXT.__cstring: 0x29dc
-  __TEXT.__const: 0x278
-  __TEXT.__gcc_except_tab: 0x11e0
-  __TEXT.__oslogstring: 0x1100
+623.1.12.10.4
+  __TEXT.__text: 0x2aa1c
+  __TEXT.__auth_stubs: 0xa90
+  __TEXT.__objc_methlist: 0x1fec
+  __TEXT.__cstring: 0x2c3c
+  __TEXT.__const: 0x21c
+  __TEXT.__gcc_except_tab: 0x1358
+  __TEXT.__oslogstring: 0x115a
   __TEXT.__dlopen_cstrs: 0x203
-  __TEXT.__ustring: 0x1ee
-  __TEXT.__swift5_typeref: 0x163
+  __TEXT.__ustring: 0x224
+  __TEXT.__swift5_typeref: 0x15a
   __TEXT.__swift5_capture: 0x128
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x2c
-  __TEXT.__constg_swiftt: 0x60
-  __TEXT.__swift5_reflstr: 0x1c
-  __TEXT.__swift5_fieldmd: 0x1c
-  __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xf60
+  __TEXT.__unwind_info: 0x1078
   __TEXT.__eh_frame: 0x518
   __TEXT.__objc_classname: 0x4b1
-  __TEXT.__objc_methname: 0x73e5
-  __TEXT.__objc_methtype: 0xb59
-  __TEXT.__objc_stubs: 0x47e0
-  __DATA_CONST.__got: 0x4d0
-  __DATA_CONST.__const: 0x12b0
-  __DATA_CONST.__objc_classlist: 0x120
+  __TEXT.__objc_methname: 0x7e95
+  __TEXT.__objc_methtype: 0xbf9
+  __TEXT.__objc_stubs: 0x4c60
+  __DATA_CONST.__got: 0x4d8
+  __DATA_CONST.__const: 0x1400
+  __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1740
+  __DATA_CONST.__objc_selrefs: 0x18a0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xb0
-  __DATA_CONST.__objc_arraydata: 0x108
-  __AUTH_CONST.__auth_got: 0x538
-  __AUTH_CONST.__const: 0x750
-  __AUTH_CONST.__cfstring: 0x1c00
-  __AUTH_CONST.__objc_const: 0x3330
+  __DATA_CONST.__objc_arraydata: 0x110
+  __AUTH_CONST.__auth_got: 0x560
+  __AUTH_CONST.__const: 0x730
+  __AUTH_CONST.__cfstring: 0x1de0
+  __AUTH_CONST.__objc_const: 0x33f0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1f0
-  __AUTH.__data: 0x130
-  __DATA.__objc_ivar: 0x1b4
+  __AUTH.__data: 0x78
+  __DATA.__objc_ivar: 0x1c8
   __DATA.__data: 0x480
-  __DATA.__bss: 0x98
+  __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0x960
-  __DATA_DIRTY.__bss: 0xe8
+  __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A4A075E3-E48B-3207-87A8-C79C2D2C1AAA
-  Functions: 1021
-  Symbols:   3458
-  CStrings:  1756
+  UUID: E672A337-B9BC-30DF-8559-ADC1BB5F5479
+  Functions: 1067
+  Symbols:   3610
+  CStrings:  1841
 
Symbols:
+ +[SFSafariCredentialStore _addBestDomainToAppCredentialWithAppID:userName:]
+ +[SFSafariCredentialStore _applicationIDsForAppsToNotOfferToSavePasswords]
+ +[SFSafariCredentialStore _applicationIDsForAppsToOfferToSaveEvenIfEnabledAsCredentialProvider]
+ +[SFSafariCredentialStore _approvedAndValidSharedWebCredentialsDatabaseEntriesForAppWithAppID:appIsEntitledWebBrowser:domain:completionHandler:]
+ +[SFSafariCredentialStore _credentialsForAppID:matchingSharedWebCredentialsDatabaseEntries:domainsAssociatedToApprovedDomainsByQuirks:websiteURL:savedAccounts:]
+ +[SFSafariCredentialStore _credentialsForAppWithAppID:completionHandler:]
+ +[SFSafariCredentialStore _ensureQuirksManagerIsInitialized]
+ +[SFSafariCredentialStore _ensureQuirksManagerIsInitialized].cold.1
+ +[SFSafariCredentialStore _fetchKeychainCredentialsIfRequiredForAppID:withSharedWebCredentialsDatabaseEntries:domainsAssociatedToApprovedDomainsByQuirks:websiteURL:webFrameIdentifier:isEntitledWebBrowser:testOptions:completion:]
+ +[SFSafariCredentialStore _getAllowedActionForAppCredentialsWithAppID:websiteURL:user:password:shouldAnalyzePasswordsAppState:completionHandler:]
+ +[SFSafariCredentialStore _getAllowedActionForAppCredentialsWithAppID:websiteURL:user:password:shouldAnalyzePasswordsAppState:completionHandler:].cold.1
+ +[SFSafariCredentialStore _getCredentialsForAppWithAppID:approvedAndValidSharedWebCredentialsDatabaseEntries:domainsAssociatedToApprovedDomainsByQuirks:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:testOptions:completionHandler:]
+ +[SFSafariCredentialStore _isEnabledCredentialProviderApp:enabledExtensions:]
+ +[SFSafariCredentialStore _sortCredentials:appID:usingApprovedSharedWebCredentialsDatabaseEntries:domainsAssociatedToApprovedDomainsByQuirks:]
+ +[SFSafariCredentialStore _titleForCredentialIdentityType:matchingSite:providerName:showCredentialProviderName:isForAppID:]
+ +[SFSafariCredentialStore appIsEntitledWebBrowser:]
+ +[SFSafariCredentialStore bundleRecordIsEntitledWebBrowser:]
+ +[SFSafariCredentialStore canOfferToSavePasswordsForApplication:]
+ +[SFSafariCredentialStore canOfferToSavePasswordsForApplicationFromAuditToken:]
+ +[SFSafariCredentialStore canOfferToSuggestStrongPasswordsForApplicationFromAuditToken:]
+ +[SFSafariCredentialStore didUsePasswordForUserName:appID:]
+ +[SFSafariCredentialStore isAppEligibleForSavingPasswords:isEnabledAsCredentialProvider:]
+ +[SFSafariCredentialStore isAppIDEligibleForSavingPasswords:isEnabledAsCredentialProvider:]
+ +[SFSafariCredentialStore isPasswordSavingAvailable]
+ +[SFSafariCredentialStore isSuggestingStrongPasswordsAvailable]
+ +[SFSafariCredentialStore textSuggestionHeaderForCredential:]
+ -[SFAppAutoFillOneTimeCodeProvider test_setOverrideForAppIdentifier:associatedDomainEntriess:]
+ -[SFAppAutoFillOneTimeCodeProvider test_setOverrideForAppIdentifier:isWebBrowser:]
+ -[SFAppAutoFillPasskeyProvider didFillCredentialForUsername:password:serviceIdentifierType:serviceIdentifier:providerApplicationBundleIdentifier:providerExtensionBundleIdentifier:hostApplicationBundleIdentifier:]
+ -[SFAutoFillFeatureManager _preferredCredentialProviderForSaving]
+ -[SFAutoFillFeatureManager preferredCredentialProviderForSaving]
+ -[SFAutoFillFeatureManager setPreferredCredentialProviderForSaving:]
+ -[SFCredentialIdentity externalProviderBundleID]
+ -[SFCredentialIdentity externalProviderExtensionBundleID]
+ -[SFCredentialIdentity initWithRowIdentifier:serviceIdentifier:serviceIdentifierType:serviceDisplayName:externalRecordIdentifier:user:rank:]
+ -[SFCredentialIdentity initWithRowIdentifier:serviceIdentifier:serviceIdentifierType:serviceDisplayName:externalRecordIdentifier:user:rank:owningExtensionState:]
+ -[SFCredentialIdentity initWithServiceIdentifier:serviceIdentifierType:serviceDisplayName:externalRecordIdentifier:user:rank:]
+ -[SFCredentialIdentity serviceDisplayName]
+ -[SFCredentialIdentity wbsServiceIdentifierType]
+ -[SFCredentialProviderExtensionManager extensionSupportsGeneratingPasswordCredentials:]
+ -[SFCredentialProviderExtensionManager extensionSupportsGeneratingPasswordCredentialsWithUI:]
+ -[SFCredentialProviderExtensionManager extensionSupportsSavingPasswordCredentials:]
+ -[SFCredentialProviderExtensionState initWithEnabledState:supportsIncrementalUpdates:localizedDisplayName:credentialIdentityStoreIdentifier:providerBundleID:providerExtensionBundleID:]
+ -[SFCredentialProviderExtensionState initWithEnabledState:supportsIncrementalUpdates:localizedDisplayName:providerBundleID:providerExtensionBundleID:]
+ -[SFCredentialProviderExtensionState providerExtensionBundleID]
+ -[SFExternalCredentialIdentityStore _migrateToSchemaVersion_4]
+ -[SFSafariCredential externalProviderBundleID]
+ -[SFSafariCredential externalProviderExtensionBundleID]
+ -[SFSafariCredential isForAppID]
+ -[SFSafariCredential setIsForAppID:]
+ -[SFSharablePassword initWithSavedAccount:passkeyCredentialID:exportedPasskeyData:]
+ GCC_except_table102
+ GCC_except_table103
+ GCC_except_table104
+ GCC_except_table105
+ GCC_except_table106
+ GCC_except_table107
+ GCC_except_table108
+ GCC_except_table109
+ GCC_except_table110
+ GCC_except_table111
+ GCC_except_table112
+ GCC_except_table113
+ GCC_except_table114
+ GCC_except_table115
+ GCC_except_table125
+ GCC_except_table21
+ GCC_except_table33
+ GCC_except_table37
+ GCC_except_table39
+ GCC_except_table41
+ GCC_except_table48
+ GCC_except_table51
+ _CFGetTypeID
+ _CFPreferencesCopyAppValue
+ _CFStringGetTypeID
+ _OBJC_CLASS_$_WBSSavedAccountAppURL
+ _OBJC_IVAR_$_SFAppAutoFillOneTimeCodeProvider._test_overrideAppIdentifierToAssociatedDomainEntries
+ _OBJC_IVAR_$_SFAppAutoFillOneTimeCodeProvider._test_overrideAppIdentifierToIsWebBrowser
+ _OBJC_IVAR_$_SFCredentialIdentity._serviceDisplayName
+ _OBJC_IVAR_$_SFCredentialProviderExtensionState._providerExtensionBundleID
+ _OBJC_IVAR_$_SFSafariCredential._isForAppID
+ _SFCredentialProviderCapabilitiesSupportsGeneratePasswordCredentials
+ _SFCredentialProviderCapabilitiesSupportsGeneratePasswordCredentialsWithUI
+ _SFCredentialProviderCapabilitiesSupportsSavePasswordCredentials
+ _WBSOSLogAutoFill
+ _WBSOSLogCredentialProviderExtension
+ _WBSOSLogCredentials
+ _WBSOSLogPasswordSharing
+ __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi1ERlJU8__strongP8NSString33SFCredentialServiceIdentifierTypeS4_S4_S4_lEEEvP18WBSSQLiteStatementOT0_DpOT1_
+ __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi1ERlJU8__strongP8NSString33SFCredentialServiceIdentifierTypeS4_S4_S4_llEEEvP18WBSSQLiteStatementOT0_DpOT1_
+ __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi2EU8__strongP8NSStringJ33SFCredentialServiceIdentifierTypeS3_S3_S3_lEEEvP18WBSSQLiteStatementOT0_DpOT1_
+ __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi2EU8__strongP8NSStringJ33SFCredentialServiceIdentifierTypeS3_S3_S3_llEEEvP18WBSSQLiteStatementOT0_DpOT1_
+ __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi3E33SFCredentialServiceIdentifierTypeJU8__strongP8NSStringS4_S4_lEEEvP18WBSSQLiteStatementOT0_DpOT1_
+ __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi3E33SFCredentialServiceIdentifierTypeJU8__strongP8NSStringS4_S4_llEEEvP18WBSSQLiteStatementOT0_DpOT1_
+ __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi4EU8__strongP8NSStringJS3_S3_lEEEvP18WBSSQLiteStatementOT0_DpOT1_
+ __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi4EU8__strongP8NSStringJS3_S3_llEEEvP18WBSSQLiteStatementOT0_DpOT1_
+ __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi5EU8__strongP8NSStringJS3_lEEEvP18WBSSQLiteStatementOT0_DpOT1_
+ __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi5EU8__strongP8NSStringJS3_llEEEvP18WBSSQLiteStatementOT0_DpOT1_
+ __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi6EU8__strongP8NSStringJlEEEvP18WBSSQLiteStatementOT0_DpOT1_
+ __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi6EU8__strongP8NSStringJllEEEvP18WBSSQLiteStatementOT0_DpOT1_
+ __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi7ElJlEEEvP18WBSSQLiteStatementOT0_DpOT1_
+ ___142+[SFSafariCredentialStore _sortCredentials:appID:usingApprovedSharedWebCredentialsDatabaseEntries:domainsAssociatedToApprovedDomainsByQuirks:]_block_invoke
+ ___144+[SFSafariCredentialStore _approvedAndValidSharedWebCredentialsDatabaseEntriesForAppWithAppID:appIsEntitledWebBrowser:domain:completionHandler:]_block_invoke
+ ___145+[SFSafariCredentialStore _getAllowedActionForAppCredentialsWithAppID:websiteURL:user:password:shouldAnalyzePasswordsAppState:completionHandler:]_block_invoke
+ ___145+[SFSafariCredentialStore _getAllowedActionForAppCredentialsWithAppID:websiteURL:user:password:shouldAnalyzePasswordsAppState:completionHandler:]_block_invoke_2
+ ___145+[SFSafariCredentialStore _getAllowedActionForAppCredentialsWithAppID:websiteURL:user:password:shouldAnalyzePasswordsAppState:completionHandler:]_block_invoke_3
+ ___228+[SFSafariCredentialStore _fetchKeychainCredentialsIfRequiredForAppID:withSharedWebCredentialsDatabaseEntries:domainsAssociatedToApprovedDomainsByQuirks:websiteURL:webFrameIdentifier:isEntitledWebBrowser:testOptions:completion:]_block_invoke
+ ___228+[SFSafariCredentialStore _fetchKeychainCredentialsIfRequiredForAppID:withSharedWebCredentialsDatabaseEntries:domainsAssociatedToApprovedDomainsByQuirks:websiteURL:webFrameIdentifier:isEntitledWebBrowser:testOptions:completion:]_block_invoke_2
+ ___252+[SFSafariCredentialStore _getCredentialsForAppWithAppID:approvedAndValidSharedWebCredentialsDatabaseEntries:domainsAssociatedToApprovedDomainsByQuirks:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:testOptions:completionHandler:]_block_invoke
+ ___252+[SFSafariCredentialStore _getCredentialsForAppWithAppID:approvedAndValidSharedWebCredentialsDatabaseEntries:domainsAssociatedToApprovedDomainsByQuirks:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:testOptions:completionHandler:]_block_invoke_2
+ ___252+[SFSafariCredentialStore _getCredentialsForAppWithAppID:approvedAndValidSharedWebCredentialsDatabaseEntries:domainsAssociatedToApprovedDomainsByQuirks:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:testOptions:completionHandler:]_block_invoke_3
+ ___60+[SFSafariCredentialStore _ensureQuirksManagerIsInitialized]_block_invoke
+ ___64-[SFAutoFillFeatureManager preferredCredentialProviderForSaving]_block_invoke
+ ___65+[SFSafariCredentialStore canOfferToSavePasswordsForApplication:]_block_invoke
+ ___73+[SFSafariCredentialStore _credentialsForAppWithAppID:completionHandler:]_block_invoke
+ ___73+[SFSafariCredentialStore _credentialsForAppWithAppID:completionHandler:]_block_invoke_2
+ ___75+[SFSafariCredentialStore _addBestDomainToAppCredentialWithAppID:userName:]_block_invoke
+ ___75+[SFSafariCredentialStore _addBestDomainToAppCredentialWithAppID:userName:]_block_invoke_2
+ ___75+[SFSafariCredentialStore _addBestDomainToAppCredentialWithAppID:userName:]_block_invoke_3
+ ___77+[SFSafariCredentialStore _isEnabledCredentialProviderApp:enabledExtensions:]_block_invoke
+ ___99+[SFSafariCredentialStore getApprovedSharedWebCredentialsEntriesForAppWithAppID:completionHandler:]_block_invoke
+ ___block_descriptor_32_e28_B16?0"SFSafariCredential"8l
+ ___block_descriptor_32_e50_"SFSafariCredential"16?0"WBSSavedAccountMatch"8l
+ ___block_descriptor_40_e8_32bs_e29_v24?0"NSArray"8"NSArray"16ls32l8
+ ___block_descriptor_40_e8_32bs_e36_v16?0"WBSSavedAccountMatchResult"8ls32l8
+ ___block_descriptor_40_e8_32s_e18_v16?0"NSString"8ls32l8
+ ___block_descriptor_48_e8_32s40r_e29_v24?0"NSArray"8"NSArray"16lr40l8s32l8
+ ___block_descriptor_48_e8_32s_e36_v16?0"WBSSavedAccountMatchResult"8ls32l8
+ ___block_descriptor_56_e8_32s40bs_e29_v24?0"NSArray"8"NSArray"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r_e17_v16?0"NSArray"8ls32l8r48l8s40l8
+ ___block_descriptor_65_e8_32s40s48bs_e29_v24?0"NSArray"8"NSArray"16ls32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_97_e8_32s40s48s56s64s72bs80r_e29_v24?0"NSArray"8"NSArray"16ls32l8s40l8s48l8s56l8r80l8s64l8s72l8
+ ___block_descriptor_97_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s80l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.166
+ ___block_literal_global.168
+ ___block_literal_global.170
+ ___block_literal_global.171
+ ___block_literal_global.173
+ ___block_literal_global.175
+ ___block_literal_global.177
+ ___block_literal_global.182
+ ___block_literal_global.26
+ ___block_literal_global.29
+ ___block_literal_global.35
+ ___block_literal_global.39
+ ___block_literal_global.40
+ ___block_literal_global.71
+ __ensureQuirksManagerIsInitialized.onceToken
+ _objc_msgSend$_addBestDomainToAppCredentialWithAppID:userName:
+ _objc_msgSend$_applicationIDsForAppsToNotOfferToSavePasswords
+ _objc_msgSend$_applicationIDsForAppsToOfferToSaveEvenIfEnabledAsCredentialProvider
+ _objc_msgSend$_approvedAndValidSharedWebCredentialsDatabaseEntriesForAppWithAppID:appIsEntitledWebBrowser:domain:completionHandler:
+ _objc_msgSend$_credentialsForAppID:matchingSharedWebCredentialsDatabaseEntries:domainsAssociatedToApprovedDomainsByQuirks:websiteURL:savedAccounts:
+ _objc_msgSend$_credentialsForAppWithAppID:completionHandler:
+ _objc_msgSend$_ensureQuirksManagerIsInitialized
+ _objc_msgSend$_fetchKeychainCredentialsIfRequiredForAppID:withSharedWebCredentialsDatabaseEntries:domainsAssociatedToApprovedDomainsByQuirks:websiteURL:webFrameIdentifier:isEntitledWebBrowser:testOptions:completion:
+ _objc_msgSend$_getAllowedActionForAppCredentialsWithAppID:websiteURL:user:password:shouldAnalyzePasswordsAppState:completionHandler:
+ _objc_msgSend$_getCredentialsForAppWithAppID:approvedAndValidSharedWebCredentialsDatabaseEntries:domainsAssociatedToApprovedDomainsByQuirks:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:testOptions:completionHandler:
+ _objc_msgSend$_isEnabledCredentialProviderApp:enabledExtensions:
+ _objc_msgSend$_migrateToSchemaVersion_4
+ _objc_msgSend$_preferredCredentialProviderForSaving
+ _objc_msgSend$_sortCredentials:appID:usingApprovedSharedWebCredentialsDatabaseEntries:domainsAssociatedToApprovedDomainsByQuirks:
+ _objc_msgSend$_titleForCredentialIdentityType:matchingSite:providerName:showCredentialProviderName:isForAppID:
+ _objc_msgSend$addAdditionalSite:toSavedAccount:completionHandler:
+ _objc_msgSend$appIDFromAppURL:
+ _objc_msgSend$appIdentifiersFromAdditionalSites
+ _objc_msgSend$appIsEntitledWebBrowser:
+ _objc_msgSend$bestDomainForAppID:completionHandler:
+ _objc_msgSend$bundleRecordForAuditToken:error:
+ _objc_msgSend$bundleRecordIsEntitledWebBrowser:
+ _objc_msgSend$canOfferToSavePasswordsForApplication:
+ _objc_msgSend$canOfferToSavePasswordsForApplicationFromAuditToken:
+ _objc_msgSend$didFillCredentialForUsername:password:serviceIdentifierType:serviceIdentifier:providerApplicationBundleIdentifier:providerExtensionBundleIdentifier:hostApplicationBundleIdentifier:externalProviderConditionalRegistrationRequester:
+ _objc_msgSend$extensionSupportsGeneratingPasswordCredentials:
+ _objc_msgSend$extensionSupportsSavingPasswordCredentials:
+ _objc_msgSend$externalProviderBundleID
+ _objc_msgSend$externalProviderExtensionBundleID
+ _objc_msgSend$initWithAppID:options:userNameQuery:
+ _objc_msgSend$initWithEnabledState:supportsIncrementalUpdates:localizedDisplayName:credentialIdentityStoreIdentifier:providerBundleID:providerExtensionBundleID:
+ _objc_msgSend$initWithRowIdentifier:serviceIdentifier:serviceIdentifierType:serviceDisplayName:externalRecordIdentifier:user:rank:
+ _objc_msgSend$initWithRowIdentifier:serviceIdentifier:serviceIdentifierType:serviceDisplayName:externalRecordIdentifier:user:rank:owningExtensionState:
+ _objc_msgSend$isAppEligibleForSavingPasswords:isEnabledAsCredentialProvider:
+ _objc_msgSend$isAppIDEligibleForSavingPasswords:isEnabledAsCredentialProvider:
+ _objc_msgSend$isAutomaticStrongPasswordsEnabled
+ _objc_msgSend$isCredentialProviderPasswordSavingEnabled
+ _objc_msgSend$isForAppID
+ _objc_msgSend$isPasswordSavingAvailable
+ _objc_msgSend$providerBundleID
+ _objc_msgSend$providerExtensionBundleID
+ _objc_msgSend$safari_firstObjectPassingTest:
+ _objc_msgSend$safari_isPasswordEligibleForAutoFill
+ _objc_msgSend$savedAccountsMatchingCriteria:withCompletionHandler:
+ _objc_msgSend$serviceDisplayName
+ _objc_msgSend$setByAddingObjectsFromArray:
+ _objc_msgSend$setIsForAppID:
+ _objc_msgSend$textSuggestionHeaderForExternalCredential:
- +[SFSafariCredentialStore _appIsEntitledWebBrowser:]
- +[SFSafariCredentialStore _approvedAndValidSharedWebCredentialsDatabaseEntriesForAppWithAppID:completionHandler:]
- +[SFSafariCredentialStore _credentialsForAppID:matchingSharedWebCredentialsDatabaseEntries:websiteURL:savedAccounts:]
- +[SFSafariCredentialStore _fetchKeychainCredentialsIfRequiredForAppID:withSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:testOptions:completion:]
- +[SFSafariCredentialStore _getAllowedActionForAppCredentialsWithAppID:websiteURL:user:password:shouldAnalyzeExistingCredentials:completionHandler:]
- +[SFSafariCredentialStore _getAllowedActionForAppCredentialsWithAppID:websiteURL:user:password:shouldAnalyzeExistingCredentials:completionHandler:].cold.1
- +[SFSafariCredentialStore _getBundleIDForEnabledCredentialProvidersWithCompletionHandler:]
- +[SFSafariCredentialStore _getCredentialsForAppWithAppID:approvedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:testOptions:completionHandler:]
- +[SFSafariCredentialStore _sortCredentials:appID:usingApprovedSharedWebCredentialsDatabaseEntries:]
- -[SFCredentialIdentity initWithRowIdentifier:serviceIdentifier:serviceIdentifierType:externalRecordIdentifier:user:rank:]
- -[SFCredentialIdentity initWithRowIdentifier:serviceIdentifier:serviceIdentifierType:externalRecordIdentifier:user:rank:owningExtensionState:]
- -[SFCredentialIdentity initWithServiceIdentifier:serviceIdentifierType:externalRecordIdentifier:user:rank:]
- -[SFCredentialProviderExtensionState initWithEnabledState:supportsIncrementalUpdates:localizedDisplayName:credentialIdentityStoreIdentifier:providerBundleID:]
- -[SFCredentialProviderExtensionState initWithEnabledState:supportsIncrementalUpdates:localizedDisplayName:providerBundleID:]
- -[SFSharablePassword initWithSavedPassword:]
- GCC_except_table20
- GCC_except_table26
- GCC_except_table38
- GCC_except_table40
- GCC_except_table42
- GCC_except_table50
- GCC_except_table56
- _OBJC_CLASS_$__TtCs12_SwiftObject
- _OBJC_METACLASS_$__TtCs12_SwiftObject
- _WBS_LOG_CHANNEL_PREFIXAutoFill
- _WBS_LOG_CHANNEL_PREFIXAutoFill.cold.1
- _WBS_LOG_CHANNEL_PREFIXAutoFill.log
- _WBS_LOG_CHANNEL_PREFIXAutoFill.onceToken
- _WBS_LOG_CHANNEL_PREFIXCredentialProviderExtension
- _WBS_LOG_CHANNEL_PREFIXCredentialProviderExtension.cold.1
- _WBS_LOG_CHANNEL_PREFIXCredentialProviderExtension.log
- _WBS_LOG_CHANNEL_PREFIXCredentialProviderExtension.onceToken
- _WBS_LOG_CHANNEL_PREFIXCredentials
- _WBS_LOG_CHANNEL_PREFIXCredentials.cold.1
- _WBS_LOG_CHANNEL_PREFIXCredentials.log
- _WBS_LOG_CHANNEL_PREFIXCredentials.onceToken
- _WBS_LOG_CHANNEL_PREFIXPasswordSharing
- _WBS_LOG_CHANNEL_PREFIXPasswordSharing.cold.1
- _WBS_LOG_CHANNEL_PREFIXPasswordSharing.log
- _WBS_LOG_CHANNEL_PREFIXPasswordSharing.onceToken
- __DATA__TtC16SafariFoundation39SymbolOfNewBeginningsInSafariFoundation
- __IVARS__TtC16SafariFoundation39SymbolOfNewBeginningsInSafariFoundation
- __METACLASS_DATA__TtC16SafariFoundation39SymbolOfNewBeginningsInSafariFoundation
- ___147+[SFSafariCredentialStore _getAllowedActionForAppCredentialsWithAppID:websiteURL:user:password:shouldAnalyzeExistingCredentials:completionHandler:]_block_invoke
- ___147+[SFSafariCredentialStore _getAllowedActionForAppCredentialsWithAppID:websiteURL:user:password:shouldAnalyzeExistingCredentials:completionHandler:]_block_invoke_2
- ___147+[SFSafariCredentialStore _getAllowedActionForAppCredentialsWithAppID:websiteURL:user:password:shouldAnalyzeExistingCredentials:completionHandler:]_block_invoke_3
- ___185+[SFSafariCredentialStore _fetchKeychainCredentialsIfRequiredForAppID:withSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:testOptions:completion:]_block_invoke
- ___209+[SFSafariCredentialStore _getCredentialsForAppWithAppID:approvedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:testOptions:completionHandler:]_block_invoke
- ___209+[SFSafariCredentialStore _getCredentialsForAppWithAppID:approvedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:testOptions:completionHandler:]_block_invoke_2
- ___90+[SFSafariCredentialStore _getBundleIDForEnabledCredentialProvidersWithCompletionHandler:]_block_invoke
- ___90+[SFSafariCredentialStore _getBundleIDForEnabledCredentialProvidersWithCompletionHandler:]_block_invoke_2
- ___99+[SFSafariCredentialStore _sortCredentials:appID:usingApprovedSharedWebCredentialsDatabaseEntries:]_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXAutoFill_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXCredentialProviderExtension_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXCredentials_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXPasswordSharing_block_invoke
- ___block_descriptor_32_e31_"NSString"16?0"NSExtension"8l
- ___block_descriptor_56_e8_32s40s48r_e17_v16?0"NSArray"8ls32l8s40l8r48l8
- ___block_descriptor_65_e8_32s40s48bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8
- ___block_descriptor_89_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s72l8s40l8s48l8s56l8s64l8
- ___block_descriptor_97_e8_32s40s48s56s64s72bs80r_e17_v16?0"NSArray"8ls32l8s40l8s48l8s56l8r80l8s64l8s72l8
- ___block_literal_global.152
- ___block_literal_global.154
- ___block_literal_global.156
- ___block_literal_global.158
- ___block_literal_global.16
- ___block_literal_global.161
- ___block_literal_global.163
- ___block_literal_global.179
- ___block_literal_global.22
- ___block_literal_global.23
- ___block_literal_global.32
- ___block_literal_global.56
- _objc_msgSend$_appIsEntitledWebBrowser:
- _objc_msgSend$_approvedAndValidSharedWebCredentialsDatabaseEntriesForAppWithAppID:completionHandler:
- _objc_msgSend$_credentialsForAppID:matchingSharedWebCredentialsDatabaseEntries:websiteURL:savedAccounts:
- _objc_msgSend$_exportPasskeyCredential
- _objc_msgSend$_fetchKeychainCredentialsIfRequiredForAppID:withSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:testOptions:completion:
- _objc_msgSend$_getAllowedActionForAppCredentialsWithAppID:websiteURL:user:password:shouldAnalyzeExistingCredentials:completionHandler:
- _objc_msgSend$_getBundleIDForEnabledCredentialProvidersWithCompletionHandler:
- _objc_msgSend$_getCredentialsForAppWithAppID:approvedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:testOptions:completionHandler:
- _objc_msgSend$_sortCredentials:appID:usingApprovedSharedWebCredentialsDatabaseEntries:
- _objc_msgSend$initWithEnabledState:supportsIncrementalUpdates:localizedDisplayName:credentialIdentityStoreIdentifier:providerBundleID:
- _objc_msgSend$initWithRowIdentifier:serviceIdentifier:serviceIdentifierType:externalRecordIdentifier:user:rank:
- _objc_msgSend$initWithRowIdentifier:serviceIdentifier:serviceIdentifierType:externalRecordIdentifier:user:rank:owningExtensionState:
- _os_log_create
- _swift_deallocClassInstance
- _swift_deletedMethodError
- _symbolic SS
- _symbolic _____ 16SafariFoundation023SymbolOfNewBeginningsInaB0C
CStrings:
+ ".onecubic.com"
+ "@48@0:8q16@24@32B40B44"
+ "@56@0:8B16B20@24@32@40@48"
+ "@64@0:8@16q24@32@40@48q56"
+ "@72@0:8q16@24q32@40@48@56q64"
+ "@80@0:8q16@24q32@40@48@56q64@72"
+ "ALTER TABLE credential_identities ADD COLUMN service_display_name TEXT DEFAULT NULL"
+ "B16@?0@\"SFSafariCredential\"8"
+ "B28@0:8@16B24"
+ "B32@0:8@16@24"
+ "B48@0:8{?=[8I]}16"
+ "Failed to add service_display_name column to credential_identities table: %{public}@ (%d)"
+ "INSERT INTO credential_identities (identity_type, service_id, service_id_type, service_display_name, external_record_id, user, rank) VALUES (?, ?, ?, ?, ?, ?, ?)"
+ "Passwords (app name)"
+ "PreferredCredentialProviderForSaving"
+ "QuickType one time code header for specific website"
+ "QuickType passkey header for specific website"
+ "SupportsGeneratePasswordCredentials"
+ "SupportsGeneratePasswordCredentialsWithUI"
+ "SupportsSavePasswordCredentials"
+ "T@\"NSString\",&,N"
+ "T@\"NSString\",R,C,N,V_providerExtensionBundleID"
+ "T@\"NSString\",R,C,N,V_serviceDisplayName"
+ "TB,N,V_isForAppID"
+ "Third party password header for specific app"
+ "UPDATE credential_identities SET identity_type = ?, service_id = ?, service_id_type = ?, service_display_name = ?, external_record_id = ?, user = ?, rank = ? WHERE id = ?"
+ "_addBestDomainToAppCredentialWithAppID:userName:"
+ "_applicationIDsForAppsToNotOfferToSavePasswords"
+ "_applicationIDsForAppsToOfferToSaveEvenIfEnabledAsCredentialProvider"
+ "_approvedAndValidSharedWebCredentialsDatabaseEntriesForAppWithAppID:appIsEntitledWebBrowser:domain:completionHandler:"
+ "_credentialsForAppID:matchingSharedWebCredentialsDatabaseEntries:domainsAssociatedToApprovedDomainsByQuirks:websiteURL:savedAccounts:"
+ "_credentialsForAppWithAppID:completionHandler:"
+ "_ensureQuirksManagerIsInitialized"
+ "_fetchKeychainCredentialsIfRequiredForAppID:withSharedWebCredentialsDatabaseEntries:domainsAssociatedToApprovedDomainsByQuirks:websiteURL:webFrameIdentifier:isEntitledWebBrowser:testOptions:completion:"
+ "_getAllowedActionForAppCredentialsWithAppID:websiteURL:user:password:shouldAnalyzePasswordsAppState:completionHandler:"
+ "_getCredentialsForAppWithAppID:approvedAndValidSharedWebCredentialsDatabaseEntries:domainsAssociatedToApprovedDomainsByQuirks:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:testOptions:completionHandler:"
+ "_isEnabledCredentialProviderApp:enabledExtensions:"
+ "_isForAppID"
+ "_migrateToSchemaVersion_4"
+ "_preferredCredentialProviderForSaving"
+ "_providerExtensionBundleID"
+ "_serviceDisplayName"
+ "_sortCredentials:appID:usingApprovedSharedWebCredentialsDatabaseEntries:domainsAssociatedToApprovedDomainsByQuirks:"
+ "_test_overrideAppIdentifierToAssociatedDomainEntries"
+ "_test_overrideAppIdentifierToIsWebBrowser"
+ "_titleForCredentialIdentityType:matchingSite:providerName:showCredentialProviderName:isForAppID:"
+ "addAdditionalSite:toSavedAccount:completionHandler:"
+ "appIDFromAppURL:"
+ "appIdentifiersFromAdditionalSites"
+ "appIsEntitledWebBrowser:"
+ "bundleRecordForAuditToken:error:"
+ "bundleRecordIsEntitledWebBrowser:"
+ "canOfferToSavePasswordsForApplication:"
+ "canOfferToSavePasswordsForApplicationFromAuditToken:"
+ "canOfferToSuggestStrongPasswordsForApplicationFromAuditToken:"
+ "com.apple.LaunchServices.applicationStateChanged"
+ "com.apple.sfapp"
+ "didFillCredentialForUsername:password:serviceIdentifierType:serviceIdentifier:providerApplicationBundleIdentifier:providerExtensionBundleIdentifier:hostApplicationBundleIdentifier:"
+ "didFillCredentialForUsername:password:serviceIdentifierType:serviceIdentifier:providerApplicationBundleIdentifier:providerExtensionBundleIdentifier:hostApplicationBundleIdentifier:externalProviderConditionalRegistrationRequester:"
+ "didUsePasswordForUserName:appID:"
+ "extensionSupportsGeneratingPasswordCredentials:"
+ "extensionSupportsGeneratingPasswordCredentialsWithUI:"
+ "extensionSupportsSavingPasswordCredentials:"
+ "externalProviderBundleID"
+ "externalProviderExtensionBundleID"
+ "initWithAppID:options:userNameQuery:"
+ "initWithEnabledState:supportsIncrementalUpdates:localizedDisplayName:credentialIdentityStoreIdentifier:providerBundleID:providerExtensionBundleID:"
+ "initWithEnabledState:supportsIncrementalUpdates:localizedDisplayName:providerBundleID:providerExtensionBundleID:"
+ "initWithRowIdentifier:serviceIdentifier:serviceIdentifierType:serviceDisplayName:externalRecordIdentifier:user:rank:"
+ "initWithRowIdentifier:serviceIdentifier:serviceIdentifierType:serviceDisplayName:externalRecordIdentifier:user:rank:owningExtensionState:"
+ "initWithSavedAccount:passkeyCredentialID:exportedPasskeyData:"
+ "initWithServiceIdentifier:serviceIdentifierType:serviceDisplayName:externalRecordIdentifier:user:rank:"
+ "isAppEligibleForSavingPasswords:isEnabledAsCredentialProvider:"
+ "isAppIDEligibleForSavingPasswords:isEnabledAsCredentialProvider:"
+ "isAutomaticStrongPasswordsEnabled"
+ "isCredentialProviderPasswordSavingEnabled"
+ "isForAppID"
+ "isPasswordSavingAvailable"
+ "isSuggestingStrongPasswordsAvailable"
+ "preferredCredentialProviderForSaving"
+ "providerExtensionBundleID"
+ "safari_firstObjectPassingTest:"
+ "safari_isPasswordEligibleForAutoFill"
+ "savedAccountsMatchingCriteria:withCompletionHandler:"
+ "serviceDisplayName"
+ "setByAddingObjectsFromArray:"
+ "setIsForAppID:"
+ "setPreferredCredentialProviderForSaving:"
+ "test_setOverrideForAppIdentifier:associatedDomainEntriess:"
+ "test_setOverrideForAppIdentifier:isWebBrowser:"
+ "textSuggestionHeaderForCredential:"
+ "v16@?0@\"NSString\"8"
+ "v24@?0@\"NSArray\"8@\"NSArray\"16"
+ "v44@0:8@16B24@28@?36"
+ "v48@0:8@16@24@32@40"
+ "v72@0:8@16@24q32@40@48@56@64"
+ "v76@0:8@16@24@32@40@48B56@60@?68"
+ "v80@0:8@16@24@32@40@48B56B60@64@?72"
+ "wbsServiceIdentifierType"
- "@\"NSString\"16@?0@\"NSExtension\"8"
- "@40@0:8B16B20@24@32"
- "@56@0:8@16q24@32@40q48"
- "@64@0:8q16@24q32@40@48q56"
- "@72@0:8q16@24q32@40@48q56@64"
- "AutoFill"
- "CredentialProviderExtension"
- "Credentials"
- "PasswordSharing"
- "Third party one time code header for specific website"
- "Third party passkey header for specific website"
- "_TtC16SafariFoundation39SymbolOfNewBeginningsInSafariFoundation"
- "_appIsEntitledWebBrowser:"
- "_approvedAndValidSharedWebCredentialsDatabaseEntriesForAppWithAppID:completionHandler:"
- "_credentialsForAppID:matchingSharedWebCredentialsDatabaseEntries:websiteURL:savedAccounts:"
- "_exportPasskeyCredential"
- "_fetchKeychainCredentialsIfRequiredForAppID:withSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:testOptions:completion:"
- "_getAllowedActionForAppCredentialsWithAppID:websiteURL:user:password:shouldAnalyzeExistingCredentials:completionHandler:"
- "_getBundleIDForEnabledCredentialProvidersWithCompletionHandler:"
- "_getCredentialsForAppWithAppID:approvedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:testOptions:completionHandler:"
- "_sortCredentials:appID:usingApprovedSharedWebCredentialsDatabaseEntries:"
- "com.apple.SafariShared"
- "initWithEnabledState:supportsIncrementalUpdates:localizedDisplayName:credentialIdentityStoreIdentifier:providerBundleID:"
- "initWithEnabledState:supportsIncrementalUpdates:localizedDisplayName:providerBundleID:"
- "initWithRowIdentifier:serviceIdentifier:serviceIdentifierType:externalRecordIdentifier:user:rank:"
- "initWithRowIdentifier:serviceIdentifier:serviceIdentifierType:externalRecordIdentifier:user:rank:owningExtensionState:"
- "initWithSavedPassword:"
- "initWithServiceIdentifier:serviceIdentifierType:externalRecordIdentifier:user:rank:"
- "v68@0:8@16@24@32@40B48@52@?60"
- "v72@0:8@16@24@32@40B48B52@56@?64"
- "welcomeToTheWorldOfTomorrow"

```
