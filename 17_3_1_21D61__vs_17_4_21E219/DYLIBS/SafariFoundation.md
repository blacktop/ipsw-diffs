## SafariFoundation

> `/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation`

```diff

-617.2.4.10.8
-  __TEXT.__text: 0x1dc20
+618.1.15.10.11
+  __TEXT.__text: 0x1f3e8
   __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_methlist: 0x15f0
+  __TEXT.__objc_methlist: 0x1698
+  __TEXT.__cstring: 0x20fc
   __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0xe74
-  __TEXT.__cstring: 0x2049
-  __TEXT.__oslogstring: 0xdfb
-  __TEXT.__ustring: 0xb8
+  __TEXT.__gcc_except_tab: 0xe90
+  __TEXT.__oslogstring: 0xdf9
   __TEXT.__dlopen_cstrs: 0x156
-  __TEXT.__unwind_info: 0xb80
-  __TEXT.__objc_classname: 0x44a
-  __TEXT.__objc_methname: 0x5eaf
-  __TEXT.__objc_methtype: 0xa50
-  __TEXT.__objc_stubs: 0x3e20
-  __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0xea0
-  __DATA_CONST.__objc_classlist: 0xe8
+  __TEXT.__ustring: 0xdc
+  __TEXT.__unwind_info: 0xbd4
+  __TEXT.__objc_classname: 0x45f
+  __TEXT.__objc_methname: 0x6267
+  __TEXT.__objc_methtype: 0xa7c
+  __TEXT.__objc_stubs: 0x3f40
+  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__const: 0xee8
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2338
-  __DATA_CONST.__objc_selrefs: 0x12b8
+  __DATA_CONST.__objc_const: 0x2470
+  __DATA_CONST.__objc_selrefs: 0x1338
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x278
+  __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__cfstring: 0x15c0
-  __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__const: 0x180
+  __AUTH_CONST.__cfstring: 0x16c0
+  __AUTH_CONST.__objc_const: 0x48
+  __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x3a8
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x278
-  __DATA.__objc_superrefs: 0xb0
-  __DATA.__objc_ivar: 0x188
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x198
   __DATA.__data: 0x380
-  __DATA.__bss: 0xa4
-  __DATA_DIRTY.__const: 0x2a0
+  __DATA.__bss: 0xb0
+  __DATA_DIRTY.__const: 0x2c0
   __DATA_DIRTY.__objc_const: 0xc58
   __DATA_DIRTY.__objc_data: 0x910
   __DATA_DIRTY.__bss: 0xc0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 738
-  Symbols:   2864
-  CStrings:  1288
+  Functions: 762
+  Symbols:   2936
+  CStrings:  1320
 
Symbols:
+ +[SFPasswordManagerURL passwordManagerURLWithParameters:]
+ +[SFPasswordManagerURL passwordManagerURLWithPrefsURL:]
+ +[SFPasswordManagerURL passwordManagerURL]
+ +[SFSafariCredentialStore _credentialsForAppID:matchingSharedWebCredentialsDatabaseEntries:websiteURL:savedAccounts:]
+ +[SFSafariCredentialStore _fetchKeychainCredentialsIfRequiredForAppID:withSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:completion:]
+ +[SFSafariCredentialStore _getBundleIDForEnabledCredentialProvidersWithCompletionHandler:]
+ +[SFSafariCredentialStore _getCredentialsForAppWithAppID:approvedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completionHandler:]
+ +[SFSafariCredentialStore _getCredentialsForAppWithAppID:approvedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:completionHandler:]
+ +[SFSafariCredentialStore _getExternalCredentialsForAppID:matchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completion:]
+ +[SFSafariCredentialStore _shouldUseQuirks]
+ +[SFSafariCredentialStore _sortCredentials:appID:usingApprovedSharedWebCredentialsDatabaseEntries:]
+ +[SFSafariCredentialStore titleForCredentialIdentity:formURL:]
+ -[SFAutoFillFeatureManager test_overrideShouldAutoFillFromKeychain:]
+ -[SFCredentialProviderExtensionHelperProxy fetchAllCredentialIdentitiesMatchingDomains:forExtension:completion:]
+ -[SFCredentialProviderExtensionHelperProxy fetchCredentialIdentitiesForService:serviceIdentifierType:credentialIdentityTypes:completion:]
+ -[SFCredentialProviderExtensionHelperProxy fetchPasswordCredentialIdentitiesMatchingDomains:forExtension:completion:]
+ -[SFCredentialProviderExtensionManager atLeastOneEnabledExtensionSupportsPasskeys]
+ -[SFCredentialProviderExtensionManager canEnableCredentialProviderExtension]
+ -[SFCredentialProviderExtensionManager enabledExtensionWithContainingAppBundleID:]
+ -[SFCredentialProviderExtensionManager enabledExtensionWithContainingAppBundleID:].cold.1
+ -[SFCredentialProviderExtensionManager enabledExtensions]
+ -[SFCredentialProviderExtensionManager getEnabledExtensionsSynchronously]
+ -[SFCredentialProviderExtensionManager getEnabledExtensionsWithCompletion:]
+ -[SFCredentialProviderExtensionManager getExtensionWithBundleID:completion:]
+ -[SFCredentialProviderExtensionManager test_overrideAtLeastOneExtensionSupportsPasskeys:]
+ -[SFExternalCredentialIdentityStore _fetchCredentialIdentitiesMatchingDomains:credentialIdentityType:]
+ GCC_except_table35
+ GCC_except_table45
+ _OBJC_CLASS_$_SFPasswordManagerURL
+ _OBJC_IVAR_$_SFAutoFillFeatureManager._overrideShouldAutoFillFromKeychainValue
+ _OBJC_IVAR_$_SFAutoFillFeatureManager._shouldOverrideShouldAutoFillFromKeychain
+ _OBJC_IVAR_$_SFCredentialProviderExtensionManager._overrideAtLeastOneExtensionSupportsPasskeysValue
+ _OBJC_IVAR_$_SFCredentialProviderExtensionManager._shouldOverrideAtLeastOneExtensionSupportsPasskeys
+ _OBJC_METACLASS_$_SFPasswordManagerURL
+ _SFStringFromCredentialIdentityType
+ _WBSRemoteAutoFillQuirksLastUpdateTimePreferenceKey
+ __OBJC_$_CLASS_METHODS_SFPasswordManagerURL
+ __OBJC_CLASS_RO_$_SFPasswordManagerURL
+ __OBJC_METACLASS_RO_$_SFPasswordManagerURL
+ ___112-[SFCredentialProviderExtensionHelperProxy fetchAllCredentialIdentitiesMatchingDomains:forExtension:completion:]_block_invoke
+ ___112-[SFCredentialProviderExtensionHelperProxy fetchAllCredentialIdentitiesMatchingDomains:forExtension:completion:]_block_invoke.cold.1
+ ___117-[SFCredentialProviderExtensionHelperProxy fetchPasswordCredentialIdentitiesMatchingDomains:forExtension:completion:]_block_invoke
+ ___117-[SFCredentialProviderExtensionHelperProxy fetchPasswordCredentialIdentitiesMatchingDomains:forExtension:completion:]_block_invoke.cold.1
+ ___137-[SFCredentialProviderExtensionHelperProxy fetchCredentialIdentitiesForService:serviceIdentifierType:credentialIdentityTypes:completion:]_block_invoke
+ ___137-[SFCredentialProviderExtensionHelperProxy fetchCredentialIdentitiesForService:serviceIdentifierType:credentialIdentityTypes:completion:]_block_invoke.cold.1
+ ___158+[SFSafariCredentialStore getCredentialsForAppWithAppID:frameIdentifier:externallyVerifiedAndApprovedSharedWebCredentialDomains:websiteURL:completionHandler:]_block_invoke_2.11
+ ___158+[SFSafariCredentialStore getCredentialsForAppWithAppID:frameIdentifier:externallyVerifiedAndApprovedSharedWebCredentialDomains:websiteURL:completionHandler:]_block_invoke_3
+ ___164+[SFSafariCredentialStore _getExternalCredentialsForAppID:matchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completion:]_block_invoke
+ ___164+[SFSafariCredentialStore _getExternalCredentialsForAppID:matchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completion:]_block_invoke_2
+ ___164+[SFSafariCredentialStore _getExternalCredentialsForAppID:matchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completion:]_block_invoke_3
+ ___164+[SFSafariCredentialStore _getExternalCredentialsForAppID:matchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completion:]_block_invoke_4
+ ___173+[SFSafariCredentialStore _fetchKeychainCredentialsIfRequiredForAppID:withSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:completion:]_block_invoke
+ ___197+[SFSafariCredentialStore _getCredentialsForAppWithAppID:approvedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:completionHandler:]_block_invoke
+ ___197+[SFSafariCredentialStore _getCredentialsForAppWithAppID:approvedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:completionHandler:]_block_invoke_2
+ ___57-[SFCredentialProviderExtensionManager enabledExtensions]_block_invoke
+ ___73-[SFCredentialProviderExtensionManager getEnabledExtensionsSynchronously]_block_invoke
+ ___75-[SFCredentialProviderExtensionManager getEnabledExtensionsWithCompletion:]_block_invoke
+ ___75-[SFCredentialProviderExtensionManager getEnabledExtensionsWithCompletion:]_block_invoke_2
+ ___76-[SFCredentialProviderExtensionManager getExtensionWithBundleID:completion:]_block_invoke
+ ___76-[SFCredentialProviderExtensionManager getExtensionWithBundleID:completion:]_block_invoke.7
+ ___76-[SFCredentialProviderExtensionManager getExtensionWithBundleID:completion:]_block_invoke.7.cold.1
+ ___90+[SFSafariCredentialStore _getBundleIDForEnabledCredentialProvidersWithCompletionHandler:]_block_invoke
+ ___90+[SFSafariCredentialStore _getBundleIDForEnabledCredentialProvidersWithCompletionHandler:]_block_invoke_2
+ ___99+[SFSafariCredentialStore _sortCredentials:appID:usingApprovedSharedWebCredentialsDatabaseEntries:]_block_invoke
+ ___block_descriptor_32_e31_"NSString"16?0"NSExtension"8l
+ ___block_descriptor_40_e8_32s_e50_"SFSafariCredential"16?0"SFCredentialIdentity"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e17_v16?0"NSArray"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e17_v16?0"NSArray"8ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e29_v24?0"NSArray"8"NSError"16lr48l8s40l8s32l8r56l8
+ ___block_descriptor_72_e8_32s40s48s56s_e51_q24?0"SFSafariCredential"8"SFSafariCredential"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8s64l8s56l8
+ ___block_descriptor_81_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
+ ___block_descriptor_89_e8_32s40s48s56s64bs72r_e17_v16?0"NSArray"8ls32l8s40l8s48l8s56l8r72l8s64l8
+ ___block_literal_global.120
+ ___block_literal_global.126
+ ___block_literal_global.128
+ ___block_literal_global.129
+ ___block_literal_global.130
+ ___block_literal_global.14
+ ___block_literal_global.24
+ ___block_literal_global.31
+ ___block_literal_global.74
+ ___block_literal_global.79
+ ___block_literal_global.82
+ ___findEnabledExtensions_block_invoke
+ _objc_msgSend$_credentialsForAppID:matchingSharedWebCredentialsDatabaseEntries:websiteURL:savedAccounts:
+ _objc_msgSend$_fetchCredentialIdentitiesMatchingDomains:credentialIdentityType:
+ _objc_msgSend$_fetchKeychainCredentialsIfRequiredForAppID:withSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:completion:
+ _objc_msgSend$_getBundleIDForEnabledCredentialProvidersWithCompletionHandler:
+ _objc_msgSend$_getCredentialsForAppWithAppID:approvedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:completionHandler:
+ _objc_msgSend$_getExternalCredentialsForAppID:matchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completion:
+ _objc_msgSend$_shouldUseQuirks
+ _objc_msgSend$_sortCredentials:appID:usingApprovedSharedWebCredentialsDatabaseEntries:
+ _objc_msgSend$appToWebsiteAssociationManager
+ _objc_msgSend$associatedDomainsManager
+ _objc_msgSend$domainsWithAssociatedCredentialsForAppID:
+ _objc_msgSend$domainsWithAssociatedCredentialsForDomain:
+ _objc_msgSend$extensionSupportsPasskeys:
+ _objc_msgSend$fetchAllCredentialIdentitiesMatchingDomains:forExtension:completion:
+ _objc_msgSend$fetchCredentialIdentitiesForService:serviceIdentifierType:credentialIdentityTypes:completion:
+ _objc_msgSend$fetchPasswordCredentialIdentitiesMatchingDomains:forExtension:completion:
+ _objc_msgSend$getEnabledExtensionsSynchronously
+ _objc_msgSend$getEnabledExtensionsWithCompletion:
+ _objc_msgSend$isDeveloperModeEnabled
+ _objc_msgSend$passwordManagerURLWithPrefsURL:
+ _objc_msgSend$titleForCredentialIdentity:formURL:
+ _quirksManager
- +[SFSafariCredentialStore _credentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:savedAccounts:]
- +[SFSafariCredentialStore _fetchKeychainCredentialsIfRequiredWithSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:completion:]
- +[SFSafariCredentialStore _getBundleIDForPrimaryCredentialProviderWithCompletionHandler:]
- +[SFSafariCredentialStore _getCredentialsForAppWithApprovedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completionHandler:]
- +[SFSafariCredentialStore _getCredentialsForAppWithApprovedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:completionHandler:]
- +[SFSafariCredentialStore _getExternalCredentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completion:]
- +[SFSafariCredentialStore _sortCredentials:usingApprovedSharedWebCredentialsDatabaseEntries:]
- +[SFSafariCredentialStore titleForPasswordCredentialIdentity:formURL:]
- -[SFCredentialProviderExtensionManager getPrimaryExtensionWithCompletion:]
- -[SFCredentialProviderExtensionManager primaryExtensionSync]
- -[SFCredentialProviderExtensionManager primaryExtension]
- -[SFExternalCredentialIdentityStore _fetchPasswordCredentialIdentitiesMatchingDomains:credentialIdentityType:]
- GCC_except_table18
- GCC_except_table24
- GCC_except_table33
- ___155+[SFSafariCredentialStore _getExternalCredentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completion:]_block_invoke
- ___155+[SFSafariCredentialStore _getExternalCredentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completion:]_block_invoke_2
- ___155+[SFSafariCredentialStore _getExternalCredentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completion:]_block_invoke_3
- ___155+[SFSafariCredentialStore _getExternalCredentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completion:]_block_invoke_4
- ___164+[SFSafariCredentialStore _fetchKeychainCredentialsIfRequiredWithSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:completion:]_block_invoke
- ___191+[SFSafariCredentialStore _getCredentialsForAppWithApprovedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:completionHandler:]_block_invoke
- ___191+[SFSafariCredentialStore _getCredentialsForAppWithApprovedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:completionHandler:]_block_invoke_2
- ___56-[SFCredentialProviderExtensionManager primaryExtension]_block_invoke
- ___60-[SFCredentialProviderExtensionManager primaryExtensionSync]_block_invoke
- ___74-[SFCredentialProviderExtensionManager getPrimaryExtensionWithCompletion:]_block_invoke
- ___74-[SFCredentialProviderExtensionManager getPrimaryExtensionWithCompletion:]_block_invoke.7
- ___89+[SFSafariCredentialStore _getBundleIDForPrimaryCredentialProviderWithCompletionHandler:]_block_invoke
- ___93+[SFSafariCredentialStore _sortCredentials:usingApprovedSharedWebCredentialsDatabaseEntries:]_block_invoke
- ___93+[SFSafariCredentialStore _sortCredentials:usingApprovedSharedWebCredentialsDatabaseEntries:]_block_invoke_2
- ___block_descriptor_40_e8_32bs_e21_v16?0"NSExtension"8ls32l8
- ___block_descriptor_40_e8_32bs_e56_v24?0"SFCredentialProviderExtensionState"8"NSArray"16ls32l8
- ___block_descriptor_40_e8_32s_e51_q24?0"SFSafariCredential"8"SFSafariCredential"16ls32l8
- ___block_descriptor_48_e8_32s40s_e50_"SFSafariCredential"16?0"SFCredentialIdentity"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e18_v16?0"NSString"8ls32l8s40l8r48l8
- ___block_descriptor_72_e8_32s40s48s56bs_e56_v24?0"SFCredentialProviderExtensionState"8"NSArray"16ls32l8s40l8s56l8s48l8
- ___block_descriptor_73_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
- ___block_descriptor_81_e8_32s40s48s56bs64r_e17_v16?0"NSArray"8ls32l8s40l8s48l8r64l8s56l8
- ___block_literal_global.115
- ___block_literal_global.116
- ___block_literal_global.15
- ___block_literal_global.22
- ___block_literal_global.45
- ___block_literal_global.54
- ___block_literal_global.59
- ___block_literal_global.62
- ___block_literal_global.65
- ___block_literal_global.83
- ___findPrimaryExtension_block_invoke
- _findPrimaryExtension
- _findPrimaryExtension.cold.1
- _objc_msgSend$_credentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:savedAccounts:
- _objc_msgSend$_fetchKeychainCredentialsIfRequiredWithSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:completion:
- _objc_msgSend$_fetchPasswordCredentialIdentitiesMatchingDomains:credentialIdentityType:
- _objc_msgSend$_getBundleIDForPrimaryCredentialProviderWithCompletionHandler:
- _objc_msgSend$_getCredentialsForAppWithApprovedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:completionHandler:
- _objc_msgSend$_getExternalCredentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completion:
- _objc_msgSend$_sortCredentials:usingApprovedSharedWebCredentialsDatabaseEntries:
- _objc_msgSend$getPrimaryExtensionWithCompletion:
- _objc_msgSend$primaryExtension
- _objc_msgSend$primaryExtensionSync
- _objc_msgSend$setOwningExtensionState:
- _objc_msgSend$titleForPasswordCredentialIdentity:formURL:
CStrings:
+ ", "
+ "@\"NSString\"16@?0@\"NSExtension\"8"
+ "No enabled extension that would match provided bundleID were found."
+ "Passkey Credential"
+ "Password Credential"
+ "SFPasswordManagerURL"
+ "T@\"NSArray\",R,N"
+ "T@\"NSString\",?,R,C"
+ "Third party passkey header for current website"
+ "Third party passkey header for specific website"
+ "Third party password header for current website"
+ "Third party password header for specific website"
+ "Wasn't able to find extension among enabled ones."
+ "_credentialsForAppID:matchingSharedWebCredentialsDatabaseEntries:websiteURL:savedAccounts:"
+ "_fetchCredentialIdentitiesMatchingDomains:credentialIdentityType:"
+ "_fetchKeychainCredentialsIfRequiredForAppID:withSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:completion:"
+ "_getBundleIDForEnabledCredentialProvidersWithCompletionHandler:"
+ "_getCredentialsForAppWithAppID:approvedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completionHandler:"
+ "_getCredentialsForAppWithAppID:approvedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:completionHandler:"
+ "_getExternalCredentialsForAppID:matchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completion:"
+ "_overrideAtLeastOneExtensionSupportsPasskeysValue"
+ "_overrideShouldAutoFillFromKeychainValue"
+ "_shouldOverrideAtLeastOneExtensionSupportsPasskeys"
+ "_shouldOverrideShouldAutoFillFromKeychain"
+ "_shouldUseQuirks"
+ "_sortCredentials:appID:usingApprovedSharedWebCredentialsDatabaseEntries:"
+ "appToWebsiteAssociationManager"
+ "atLeastOneEnabledExtensionSupportsPasskeys"
+ "canEnableCredentialProviderExtension"
+ "com.apple."
+ "domainsWithAssociatedCredentialsForAppID:"
+ "domainsWithAssociatedCredentialsForDomain:"
+ "enabledExtensionWithContainingAppBundleID:"
+ "enabledExtensions"
+ "fetchAllCredentialIdentitiesMatchingDomains:forExtension:completion:"
+ "fetchCredentialIdentitiesForService:serviceIdentifierType:credentialIdentityTypes:completion:"
+ "fetchPasswordCredentialIdentitiesMatchingDomains:forExtension:completion:"
+ "getEnabledExtensionsSynchronously"
+ "getEnabledExtensionsWithCompletion:"
+ "getExtensionWithBundleID:completion:"
+ "isDeveloperModeEnabled"
+ "passwordManagerURLWithParameters:"
+ "passwordManagerURLWithPrefsURL:"
+ "test_overrideAtLeastOneExtensionSupportsPasskeys:"
+ "test_overrideShouldAutoFillFromKeychain:"
+ "titleForCredentialIdentity:formURL:"
+ "v24@0:8@?<v@?@\"NSArray\">16"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\">24"
+ "v40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?@\"NSArray\">32"
+ "v40@0:8@16@24@32"
+ "v48@0:8@\"NSString\"16q24q32@?<v@?@\"NSArray\">40"
+ "v48@0:8@16q24q32@?40"
+ "v64@0:8@16@24@32@40B48B52@?56"
+ "verification code"
+ "verification code for %@"
- "Error: Multiple credential provider extensions are active. Which one will be used as the primary extension is undefined"
- "T@\"NSExtension\",R,N"
- "Verification code"
- "Verification code for %@"
- "_credentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:savedAccounts:"
- "_fetchKeychainCredentialsIfRequiredWithSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:completion:"
- "_fetchPasswordCredentialIdentitiesMatchingDomains:credentialIdentityType:"
- "_getBundleIDForPrimaryCredentialProviderWithCompletionHandler:"
- "_getCredentialsForAppWithApprovedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completionHandler:"
- "_getCredentialsForAppWithApprovedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:completionHandler:"
- "_getExternalCredentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completion:"
- "_sortCredentials:usingApprovedSharedWebCredentialsDatabaseEntries:"
- "getPrimaryExtensionWithCompletion:"
- "primaryExtension"
- "primaryExtensionSync"
- "titleForPasswordCredentialIdentity:formURL:"
- "v16@?0@\"NSExtension\"8"
- "v16@?0@\"NSString\"8"
- "v24@0:8@?<v@?@\"SFCredentialProviderExtensionState\"@\"NSArray\">16"
- "v24@?0@\"SFCredentialProviderExtensionState\"8@\"NSArray\"16"
- "v32@0:8@\"NSArray\"16@?<v@?@\"SFCredentialProviderExtensionState\"@\"NSArray\">24"
- "v48@0:8@16@24B32B36@?40"
- "v52@0:8@16@24@32B40@?44"

```
