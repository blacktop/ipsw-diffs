## SafariFoundation

> `/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation`

```diff

-616.1.27.10.16
-  __TEXT.__text: 0x1b154
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x1570
+616.2.9.10.10
+  __TEXT.__text: 0x1b8d4
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__objc_methlist: 0x15a8
   __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0xb0c
-  __TEXT.__cstring: 0x1ef7
-  __TEXT.__oslogstring: 0xc7a
+  __TEXT.__gcc_except_tab: 0xb3c
+  __TEXT.__cstring: 0x1f00
+  __TEXT.__oslogstring: 0xd66
   __TEXT.__ustring: 0xb8
   __TEXT.__dlopen_cstrs: 0x156
-  __TEXT.__unwind_info: 0xa34
-  __TEXT.__objc_classname: 0x449
-  __TEXT.__objc_methname: 0x5b01
-  __TEXT.__objc_methtype: 0x9f6
-  __TEXT.__objc_stubs: 0x3c60
-  __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0xd60
+  __TEXT.__unwind_info: 0xa44
+  __TEXT.__objc_classname: 0x44a
+  __TEXT.__objc_methname: 0x5cdd
+  __TEXT.__objc_methtype: 0xa14
+  __TEXT.__objc_stubs: 0x3ce0
+  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__const: 0xde0
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x22b8
-  __DATA_CONST.__objc_selrefs: 0x1230
+  __DATA_CONST.__objc_const: 0x2338
+  __DATA_CONST.__objc_selrefs: 0x1258
   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__cfstring: 0x15c0
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x398
+  __AUTH_CONST.__auth_got: 0x3b0
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x278
   __DATA.__objc_superrefs: 0xb0
-  __DATA.__objc_ivar: 0x180
+  __DATA.__objc_ivar: 0x188
   __DATA.__data: 0x380
   __DATA.__bss: 0xa4
-  __DATA_DIRTY.__const: 0x420
+  __DATA_DIRTY.__const: 0x2c0
   __DATA_DIRTY.__objc_const: 0xc58
   __DATA_DIRTY.__objc_data: 0x910
   __DATA_DIRTY.__bss: 0xc0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 702
-  Symbols:   2743
-  CStrings:  1252
+  Functions: 699
+  Symbols:   2750
+  CStrings:  1267
 
Symbols:
+ +[SFSafariCredentialStore _getCredentialsForAppWithApprovedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completionHandler:]
+ +[SFSafariCredentialStore _getCredentialsForAppWithApprovedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:completionHandler:]
+ +[SFSafariCredentialStore _getExternalCredentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completion:]
+ +[SFSafariCredentialStore getCredentialsForAppWithAppID:frameIdentifier:externallyVerifiedAndApprovedSharedWebCredentialDomains:websiteURL:completionHandler:].cold.1
+ -[SFAppAutoFillOneTimeCodeProvider _sortedOneTimeCodesFromSavedAccounts:context:]
+ -[SFAutoFillOneTimeCode initWithTOTPGenerator:user:highLevelDomain:lastUsedDateOfAssociatedSavedAccount:]
+ -[SFAutoFillOneTimeCode lastUseDateOfAssociatedSavedAccount]
+ -[SFCredentialProviderExtensionHelperProxy fetchAllCredentialIdentitiesMatchingDomains:completion:]
+ -[SFCredentialProviderExtensionHelperProxy fetchPasswordCredentialIdentitiesMatchingDomains:completion:]
+ -[SFExternalCredentialIdentityStore _fetchPasswordCredentialIdentitiesMatchingDomains:credentialIdentityType:]
+ -[SFExternalCredentialIdentityStore fetchPasswordCredentialIdentitiesMatchingDomains:completion:]
+ -[SFSafariCredential lastUsedDate]
+ -[SFSafariCredential setLastUsedDate:]
+ GCC_except_table33
+ GCC_except_table48
+ _OBJC_IVAR_$_SFAutoFillOneTimeCode._lastUseDateOfAssociatedSavedAccount
+ _OBJC_IVAR_$_SFSafariCredential._lastUsedDate
+ __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi1ERlJU8__strongP8NSString33SFCredentialServiceIdentifierTypeS4_S4_lEEEvP18WBSSQLiteStatementOT0_DpOT1_
+ __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi1ERlJU8__strongP8NSString33SFCredentialServiceIdentifierTypeS4_S4_lS4_S4_EEEvP18WBSSQLiteStatementOT0_DpOT1_
+ __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi1ERlJU8__strongP8NSString33SFCredentialServiceIdentifierTypeS4_S4_llEEEvP18WBSSQLiteStatementOT0_DpOT1_
+ __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi1EU8__strongP8NSStringJ33SFCredentialServiceIdentifierTypeS3_S3_lEEEvP18WBSSQLiteStatementOT0_DpOT1_
+ __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi2E33SFCredentialServiceIdentifierTypeJU8__strongP8NSStringS4_lEEEvP18WBSSQLiteStatementOT0_DpOT1_
+ __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi3EU8__strongP8NSStringJS3_lEEEvP18WBSSQLiteStatementOT0_DpOT1_
+ __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi4EU8__strongP8NSStringJlEEEvP18WBSSQLiteStatementOT0_DpOT1_
+ ___104-[SFCredentialProviderExtensionHelperProxy fetchPasswordCredentialIdentitiesMatchingDomains:completion:]_block_invoke
+ ___104-[SFCredentialProviderExtensionHelperProxy fetchPasswordCredentialIdentitiesMatchingDomains:completion:]_block_invoke.cold.1
+ ___114-[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:]_block_invoke.48
+ ___114-[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:]_block_invoke.56
+ ___114-[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:]_block_invoke.cold.1
+ ___119-[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesForWebBrowserWithWebsiteFrameURLs:fieldClassification:inContext:]_block_invoke
+ ___155+[SFSafariCredentialStore _getExternalCredentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completion:]_block_invoke
+ ___155+[SFSafariCredentialStore _getExternalCredentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completion:]_block_invoke_2
+ ___155+[SFSafariCredentialStore _getExternalCredentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completion:]_block_invoke_3
+ ___155+[SFSafariCredentialStore _getExternalCredentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completion:]_block_invoke_4
+ ___158+[SFSafariCredentialStore getCredentialsForAppWithAppID:frameIdentifier:externallyVerifiedAndApprovedSharedWebCredentialDomains:websiteURL:completionHandler:]_block_invoke.6
+ ___191+[SFSafariCredentialStore _getCredentialsForAppWithApprovedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:completionHandler:]_block_invoke
+ ___191+[SFSafariCredentialStore _getCredentialsForAppWithApprovedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:completionHandler:]_block_invoke_2
+ ___81-[SFAppAutoFillOneTimeCodeProvider _sortedOneTimeCodesFromSavedAccounts:context:]_block_invoke
+ ___81-[SFAppAutoFillOneTimeCodeProvider _sortedOneTimeCodesFromSavedAccounts:context:]_block_invoke_2
+ ___81-[SFAppAutoFillOneTimeCodeProvider _sortedOneTimeCodesFromSavedAccounts:context:]_block_invoke_3
+ ___97-[SFExternalCredentialIdentityStore fetchPasswordCredentialIdentitiesMatchingDomains:completion:]_block_invoke
+ ___99-[SFCredentialProviderExtensionHelperProxy fetchAllCredentialIdentitiesMatchingDomains:completion:]_block_invoke
+ ___99-[SFCredentialProviderExtensionHelperProxy fetchAllCredentialIdentitiesMatchingDomains:completion:]_block_invoke.cold.1
+ ___block_descriptor_40_e8_32s_e56_"NSMutableSet"24?0"WBSSavedAccount"8"NSMutableSet"16ls32l8
+ ___block_descriptor_48_e8_32s40r_e8_v12?0B8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e49_"SFAutoFillOneTimeCode"16?0"WBSTOTPGenerator"8ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_81_e8_32s40s48s56bs64r_e17_v16?0"NSArray"8ls32l8s40l8s48l8r64l8s56l8
+ ___block_literal_global.15
+ ___block_literal_global.22
+ ___block_literal_global.45
+ ___block_literal_global.54
+ ___block_literal_global.59
+ ___block_literal_global.62
+ ___block_literal_global.65
+ ___block_literal_global.83
+ ___block_literal_global.85
+ ___block_literal_global.91
+ __os_activity_create
+ __os_activity_current
+ _objc_msgSend$_fetchPasswordCredentialIdentitiesMatchingDomains:credentialIdentityType:
+ _objc_msgSend$_getCredentialsForAppWithApprovedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:completionHandler:
+ _objc_msgSend$_getExternalCredentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completion:
+ _objc_msgSend$_sortedOneTimeCodesFromSavedAccounts:context:
+ _objc_msgSend$fetchAllCredentialIdentitiesMatchingDomains:completion:
+ _objc_msgSend$fetchPasswordCredentialIdentitiesMatchingDomains:completion:
+ _objc_msgSend$getIsPasskeyAssertionRequestRunningForWebFrameIdentifier:orApplicationIdentifier:completionHandler:
+ _objc_msgSend$initWithTOTPGenerator:user:highLevelDomain:lastUsedDateOfAssociatedSavedAccount:
+ _objc_msgSend$lastUseDateOfAssociatedSavedAccount
+ _objc_msgSend$lastUsedDate
+ _objc_msgSend$lastUsedDateForContext:
+ _objc_msgSend$setLastUsedDate:
+ _objc_retain_x27
+ _os_activity_apply
- +[SFSafariCredentialStore _getCredentialsForAppWithApprovedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:completionHandler:]
- +[SFSafariCredentialStore _getCredentialsForAppWithApprovedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:completionHandler:]
- +[SFSafariCredentialStore _getExternalCredentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:completion:]
- -[SFAppAutoFillOneTimeCodeProvider _processOneTimeCodeFromMail:withTimestamp:andMessageID:].cold.1
- -[SFAppAutoFillOneTimeCodeProvider _processOneTimeCodeFromMessages:].cold.1
- -[SFAppAutoFillOneTimeCodeProvider _sortedOneTimeCodesFromSavedAccounts:]
- -[SFAppAutoFillOneTimeCodeProvider _stopGeneratorTimer].cold.1
- -[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:].cold.1
- -[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:].cold.2
- -[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:].cold.3
- -[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:].cold.4
- -[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:].cold.5
- -[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:].cold.6
- -[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:].cold.7
- -[SFAutoFillOneTimeCode initWithTOTPGenerator:user:highLevelDomain:]
- -[SFCredentialProviderExtensionHelperProxy fetchCredentialIdentitiesMatchingDomains:completion:]
- -[SFExternalCredentialIdentityStore _fetchCredentialIdentitiesMatchingDomains:credentialIdentityType:]
- -[SFExternalCredentialIdentityStore fetchCredentialIdentitiesMatchingDomains:completion:]
- GCC_except_table14
- GCC_except_table23
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi1ER24SFCredentialIdentityTypeJU8__strongP8NSString33SFCredentialServiceIdentifierTypeS5_S5_lEEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi1ER24SFCredentialIdentityTypeJU8__strongP8NSString33SFCredentialServiceIdentifierTypeS5_S5_lS5_S5_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi1ER24SFCredentialIdentityTypeJU8__strongP8NSString33SFCredentialServiceIdentifierTypeS5_S5_llEEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi1EU8__strongP8NSStringJ33SFCredentialServiceIdentifierTypeS3_S3_24SFCredentialIdentityTypeEEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi2E33SFCredentialServiceIdentifierTypeJU8__strongP8NSStringS4_24SFCredentialIdentityTypeEEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi3EU8__strongP8NSStringJS3_24SFCredentialIdentityTypeEEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi4EU8__strongP8NSStringJ24SFCredentialIdentityTypeEEEvP18WBSSQLiteStatementOT0_DpOT1_
- ___114-[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:]_block_invoke.55
- ___137+[SFSafariCredentialStore _getExternalCredentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:completion:]_block_invoke
- ___137+[SFSafariCredentialStore _getExternalCredentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:completion:]_block_invoke_2
- ___137+[SFSafariCredentialStore _getExternalCredentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:completion:]_block_invoke_3
- ___137+[SFSafariCredentialStore _getExternalCredentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:completion:]_block_invoke_4
- ___173+[SFSafariCredentialStore _getCredentialsForAppWithApprovedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:completionHandler:]_block_invoke
- ___173+[SFSafariCredentialStore _getCredentialsForAppWithApprovedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:completionHandler:]_block_invoke_2
- ___73-[SFAppAutoFillOneTimeCodeProvider _sortedOneTimeCodesFromSavedAccounts:]_block_invoke
- ___73-[SFAppAutoFillOneTimeCodeProvider _sortedOneTimeCodesFromSavedAccounts:]_block_invoke_2
- ___73-[SFAppAutoFillOneTimeCodeProvider _sortedOneTimeCodesFromSavedAccounts:]_block_invoke_3
- ___89-[SFExternalCredentialIdentityStore fetchCredentialIdentitiesMatchingDomains:completion:]_block_invoke
- ___96-[SFCredentialProviderExtensionHelperProxy fetchCredentialIdentitiesMatchingDomains:completion:]_block_invoke
- ___96-[SFCredentialProviderExtensionHelperProxy fetchCredentialIdentitiesMatchingDomains:completion:]_block_invoke.cold.1
- ___block_descriptor_32_e49_"NSSet"24?0"WBSSavedAccount"8"NSMutableSet"16l
- ___block_descriptor_40_e8_32s_e49_"SFAutoFillOneTimeCode"16?0"WBSTOTPGenerator"8ls32l8
- ___block_descriptor_73_e8_32s40s48s56bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8s56l8
- ___block_literal_global.12
- ___block_literal_global.41
- ___block_literal_global.50
- ___block_literal_global.55
- ___block_literal_global.58
- ___block_literal_global.61
- ___block_literal_global.79
- ___block_literal_global.81
- ___block_literal_global.84
- ___block_literal_global.89
- _objc_msgSend$_fetchCredentialIdentitiesMatchingDomains:credentialIdentityType:
- _objc_msgSend$_getCredentialsForAppWithApprovedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:completionHandler:
- _objc_msgSend$_getExternalCredentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:completion:
- _objc_msgSend$_sortedOneTimeCodesFromSavedAccounts:
- _objc_msgSend$allTypes
- _objc_msgSend$fetchCredentialIdentitiesMatchingDomains:completion:
- _objc_msgSend$initWithTOTPGenerator:user:highLevelDomain:
- _objc_msgSend$orderedMatches
CStrings:
+ "\x03(\x11"
+ "\x18"
+ "@\"NSMutableSet\"24@?0@\"WBSSavedAccount\"8@\"NSMutableSet\"16"
+ "App %{sensitive, mask.hash}@ has web browser entitlement. Getting passwords for website URL %{sensitive, mask.hash}@."
+ "Fetching passwords for associated domains for app %{sensitive, mask.hash}@."
+ "Notifying observer %@ of new one-time code"
+ "Retrieving Current One-Time Codes for App"
+ "Retrieving Current One-Time Codes for Web Browser App"
+ "Returning %ld available one-time code%s"
+ "T@\"NSDate\",&,N,V_lastUsedDate"
+ "T@\"NSDate\",R,N,V_lastUseDateOfAssociatedSavedAccount"
+ "Timed out while querying for passkey request"
+ "_fetchPasswordCredentialIdentitiesMatchingDomains:credentialIdentityType:"
+ "_getCredentialsForAppWithApprovedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completionHandler:"
+ "_getCredentialsForAppWithApprovedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:hasPasskeyRequest:completionHandler:"
+ "_getExternalCredentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:hasPasskeyRequest:completion:"
+ "_lastUseDateOfAssociatedSavedAccount"
+ "_lastUsedDate"
+ "_sortedOneTimeCodesFromSavedAccounts:context:"
+ "fetchAllCredentialIdentitiesMatchingDomains:completion:"
+ "fetchPasswordCredentialIdentitiesMatchingDomains:completion:"
+ "getIsPasskeyAssertionRequestRunningForWebFrameIdentifier:orApplicationIdentifier:completionHandler:"
+ "initWithTOTPGenerator:user:highLevelDomain:lastUsedDateOfAssociatedSavedAccount:"
+ "lastUseDateOfAssociatedSavedAccount"
+ "lastUsedDate"
+ "lastUsedDateForContext:"
+ "s"
+ "setLastUsedDate:"
+ "v48@0:8@16@24B32B36@?40"
+ "v56@0:8@16@24@32B40B44@?48"
- "\x03("
- "\x17"
- "@\"NSSet\"24@?0@\"WBSSavedAccount\"8@\"NSMutableSet\"16"
- "App %{private}@ has web browser entitlement. Getting passwords for website URL %{private}@."
- "Codes for app: %{private}@"
- "Fetching passwords for associated domains for app %{private}@."
- "_fetchCredentialIdentitiesMatchingDomains:credentialIdentityType:"
- "_getCredentialsForAppWithApprovedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:completionHandler:"
- "_getCredentialsForAppWithApprovedAndValidSharedWebCredentialsDatabaseEntries:websiteURL:webFrameIdentifier:isEntitledWebBrowser:completionHandler:"
- "_getExternalCredentialsMatchingSharedWebCredentialsDatabaseEntries:websiteURL:isEntitledWebBrowser:completion:"
- "_sortedOneTimeCodesFromSavedAccounts:"
- "fetchCredentialIdentitiesMatchingDomains:completion:"
- "initWithTOTPGenerator:user:highLevelDomain:"
- "orderedMatches"
- "v44@0:8@16@24B32@?36"

```
