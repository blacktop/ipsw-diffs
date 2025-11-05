## SafariFoundation

> `/System/Library/PrivateFrameworks/SafariFoundation.framework/Versions/A/SafariFoundation`

```diff

-620.2.4.11.6
-  __TEXT.__text: 0x24a30
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_methlist: 0x1760
-  __TEXT.__cstring: 0x21eb
-  __TEXT.__const: 0x120
-  __TEXT.__gcc_except_tab: 0x10e8
-  __TEXT.__oslogstring: 0xf24
+621.1.15.11.10
+  __TEXT.__text: 0x25630
+  __TEXT.__auth_stubs: 0x570
+  __TEXT.__objc_methlist: 0x1a84
+  __TEXT.__cstring: 0x22bd
+  __TEXT.__const: 0x16a
+  __TEXT.__gcc_except_tab: 0x1134
+  __TEXT.__oslogstring: 0xfcf
   __TEXT.__dlopen_cstrs: 0xf2
   __TEXT.__ustring: 0x1ee
-  __TEXT.__unwind_info: 0xcb0
+  __TEXT.__constg_swiftt: 0x60
+  __TEXT.__swift5_typeref: 0x9
+  __TEXT.__swift5_reflstr: 0x1c
+  __TEXT.__swift5_fieldmd: 0x1c
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0xce0
   __TEXT.__objc_classname: 0x46e
-  __TEXT.__objc_methname: 0x6447
-  __TEXT.__objc_methtype: 0xa02
-  __TEXT.__objc_stubs: 0x4220
-  __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0x3b8
-  __DATA_CONST.__objc_classlist: 0xf8
+  __TEXT.__objc_methname: 0x6722
+  __TEXT.__objc_methtype: 0xa1c
+  __TEXT.__objc_stubs: 0x4340
+  __DATA_CONST.__got: 0x420
+  __DATA_CONST.__const: 0x418
+  __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1410
+  __DATA_CONST.__objc_selrefs: 0x1518
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xa8
-  __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__auth_got: 0x2c0
-  __AUTH_CONST.__const: 0x11e0
-  __AUTH_CONST.__cfstring: 0x1920
-  __AUTH_CONST.__objc_const: 0x3028
+  __DATA_CONST.__objc_arraydata: 0x130
+  __AUTH_CONST.__auth_got: 0x2d0
+  __AUTH_CONST.__const: 0x12b0
+  __AUTH_CONST.__cfstring: 0x19e0
+  __AUTH_CONST.__objc_const: 0x2c58
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x3c0
+  __AUTH.__data: 0xb8
   __DATA.__objc_ivar: 0x194
   __DATA.__data: 0x318
   __DATA.__bss: 0x140

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: C2669668-E48D-3B37-B73E-7B87FD90E5B9
-  Functions: 823
-  Symbols:   2238
-  CStrings:  1555
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  UUID: 1DADFFFF-2E48-3282-BCFA-A509369C76FB
+  Functions: 851
+  Symbols:   2326
+  CStrings:  1588
 
Symbols:
+ +[SFAutoFillFeatureManager sharedFeatureManager].cold.1
+ +[SFDomainAssociationUtilities domainIsProhibitedForSavingCredentials:].cold.1
+ +[SFDomainAssociationUtilities highLevelDomainHasSuiteOfAssociatedApps:].cold.1
+ +[SFExternalCredentialIdentityStoreManager sharedManager].cold.1
+ +[SFSuggestedUserProvider sharedProvider].cold.1
+ -[NSExtension(SafariFoundationExtras) sf_applicationRecordForContainingApp]
+ -[SFAppAutoFillOneTimeCodeProvider _ignoredTimestamps]
+ -[SFAppAutoFillOneTimeCodeProvider _shouldIgnoreOneTimeCode:]
+ -[SFAppAutoFillOneTimeCodeProvider silenceOneTimeCode:]
+ -[SFAutoFillFeatureManager isUserAllowedToTogglePasswordAutoFillEnabledState]
+ -[SFAutoFillOneTimeCode requiresAuthentication]
+ -[SFAutoFillOneTimeCode type]
+ -[SFCredentialProviderExtensionManager _getExtensionsIncludingDisabled:completionHandler:]
+ -[SFCredentialProviderExtensionManager _numberOfAutoFillProvidersEnabledWithExtensions:]
+ -[SFCredentialProviderExtensionManager extensionSupportedCredentialExchangeFormatVersions:]
+ -[SFCredentialProviderExtensionManager getAllExtensionsForContainingApp:completion:]
+ -[SFCredentialProviderExtensionManager getAllExtensionsWithCompletion:]
+ -[SFCredentialProviderExtensionManager numberOfAutoFillProvidersEnabledWithCompletion:]
+ -[SFSharablePassword(AccountSavingExtras) _saveAdditionalSitesForSavedAccount:completionHandler:]
+ -[SFSharablePassword(AccountSavingExtras) _saveCustomTitleForSavedAccount:completionHandler:]
+ -[SFSharablePassword(AccountSavingExtras) _saveNotesEntryForSavedAccount:completionHandler:]
+ -[SFSharablePassword(AccountSavingExtras) _saveOneTimeCodeForSavedAccount:completionHandler:]
+ -[SFSharablePassword(AccountSavingExtras) saveToKeychainWithCompletionHandler:]
+ GCC_except_table22
+ GCC_except_table27
+ GCC_except_table49
+ WBS_LOG_CHANNEL_PREFIXAutoFill.cold.1
+ WBS_LOG_CHANNEL_PREFIXCredentialProviderExtension.cold.1
+ WBS_LOG_CHANNEL_PREFIXCredentials.cold.1
+ WBS_LOG_CHANNEL_PREFIXPasswordSharing.cold.1
+ WBS_LOG_CHANNEL_PREFIXPasswords.cold.1
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _OUTLINED_FUNCTION_3
+ _SFCredentialProviderCapabilitiesSupportedCredentialExchangeFormatVersions
+ _WBSOngoingSharingGroupIDNone
+ __114-[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:]_block_invoke.63
+ __114-[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:]_block_invoke_2.65
+ __52-[SFAppAutoFillOneTimeCodeProvider initWithOptions:]_block_invoke.50
+ __52-[SFAppAutoFillOneTimeCodeProvider initWithOptions:]_block_invoke_2.51
+ __79-[SFSharablePassword(AccountSavingExtras) saveToKeychainWithCompletionHandler:]_block_invoke.1
+ __80-[SFAppAutoFillOneTimeCodeProvider _savedAccountsWithPasswordsForURL:inContext:]_block_invoke.120
+ __81-[SFAppAutoFillOneTimeCodeProvider _sortedOneTimeCodesFromSavedAccounts:context:]_block_invoke.132
+ __DATA__TtC16SafariFoundation39SymbolOfNewBeginningsInSafariFoundation
+ __IVARS__TtC16SafariFoundation39SymbolOfNewBeginningsInSafariFoundation
+ __METACLASS_DATA__TtC16SafariFoundation39SymbolOfNewBeginningsInSafariFoundation
+ ___54-[SFAppAutoFillOneTimeCodeProvider _ignoredTimestamps]_block_invoke
+ ___79-[SFSharablePassword(AccountSavingExtras) saveToKeychainWithCompletionHandler:]_block_invoke
+ ___79-[SFSharablePassword(AccountSavingExtras) saveToKeychainWithCompletionHandler:]_block_invoke_2
+ ___79-[SFSharablePassword(AccountSavingExtras) saveToKeychainWithCompletionHandler:]_block_invoke_3
+ ___79-[SFSharablePassword(AccountSavingExtras) saveToKeychainWithCompletionHandler:]_block_invoke_4
+ ___84-[SFCredentialProviderExtensionManager getAllExtensionsForContainingApp:completion:]_block_invoke
+ ___84-[SFCredentialProviderExtensionManager getAllExtensionsForContainingApp:completion:]_block_invoke_2
+ ___87-[SFCredentialProviderExtensionManager numberOfAutoFillProvidersEnabledWithCompletion:]_block_invoke
+ ___90-[SFCredentialProviderExtensionManager _getExtensionsIncludingDisabled:completionHandler:]_block_invoke
+ ___90-[SFCredentialProviderExtensionManager _getExtensionsIncludingDisabled:completionHandler:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e16_B16?0"NSDate"8l
+ ___block_descriptor_40_e8_32s_e17_B16?0"WBSPair"8l
+ ___block_descriptor_40_e8_32s_e21_B16?0"NSExtension"8l
+ ___block_descriptor_40_e8_32s_e39_"WBSPair"16?0"WBSSavedAccountMatch"8l
+ ___block_descriptor_40_e8_32s_e48_"NSMutableSet"24?0"WBSPair"8"NSMutableSet"16l
+ ___block_descriptor_41_e8_32bs_e5_v8?0l
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSArray"8l
+ ___block_descriptor_48_e8_32s40s_e71_"SFAutoFillOneTimeCode"32?0"NSNumber"8"SFAutoFillOneTimeCode"16^B24l
+ ___block_descriptor_57_e8_32bs40r48r_e29_v24?0"NSArray"8"NSError"16l
+ ___swift_reflection_version
+ __block_literal_global.135
+ __block_literal_global.197
+ __block_literal_global.23
+ __block_literal_global.78
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_SafariFoundation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_SafariFoundation
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_SafariFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_SafariFoundation
+ __swift_FORCE_LOAD_$_swiftIOKit
+ __swift_FORCE_LOAD_$_swiftIOKit_$_SafariFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_SafariFoundation
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_SafariFoundation
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_SafariFoundation
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_errno_$_SafariFoundation
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_math_$_SafariFoundation
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_signal_$_SafariFoundation
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_stdio_$_SafariFoundation
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swift_time_$_SafariFoundation
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftsys_time_$_SafariFoundation
+ __swift_FORCE_LOAD_$_swiftunistd
+ __swift_FORCE_LOAD_$_swiftunistd_$_SafariFoundation
+ _objc_msgSend$_getExtensionsIncludingDisabled:completionHandler:
+ _objc_msgSend$_ignoredTimestamps
+ _objc_msgSend$_numberOfAutoFillProvidersEnabledWithExtensions:
+ _objc_msgSend$_saveAdditionalSitesForSavedAccount:completionHandler:
+ _objc_msgSend$_saveCustomTitleForSavedAccount:completionHandler:
+ _objc_msgSend$_saveNotesEntryForSavedAccount:completionHandler:
+ _objc_msgSend$_saveOneTimeCodeForSavedAccount:completionHandler:
+ _objc_msgSend$_shouldIgnoreOneTimeCode:
+ _objc_msgSend$arrayForKey:
+ _objc_msgSend$didFillCredentialForUsername:forHost:fromProviderWithBundleIdentifier:inAppWithBundleIdentifier:externalProviderConditionalRegistrationRequester:
+ _objc_msgSend$getAllExtensionsWithCompletion:
+ _objc_msgSend$lastUsedDateForSite:inContext:
+ _objc_msgSend$objectIsForcedForKey:
+ _objc_msgSend$requiresAuthentication
+ _objc_msgSend$safari_arrayContainingObjectsOfClass:forKey:
+ _objc_msgSend$saveAdditionalSites:forSavedAccount:completionHandler:
+ _objc_msgSend$saveCustomTitle:forSavedAccount:completionHandler:
+ _objc_msgSend$saveNotesEntry:forSavedAccount:completionHandler:
+ _objc_msgSend$saveTOTPGenerator:forSavedAccount:completionHandler:
+ _objc_msgSend$sf_applicationRecordForContainingApp
+ _swift_bridgeObjectRelease
+ _swift_deallocClassInstance
+ _swift_deletedMethodError
+ _symbolic SS
+ _symbolic _____ 16SafariFoundation023SymbolOfNewBeginningsInaB0C
- -[SFAppAutoFillPasskeyProvider didFillExternalCredential:inAppWithBundleIdentifier:]
- -[SFSharablePassword(AccountSavingExtras) _saveAdditionalSitesForSavedAccount:]
- -[SFSharablePassword(AccountSavingExtras) _saveCustomTitleForSavedAccount:]
- -[SFSharablePassword(AccountSavingExtras) _saveNotesEntryForSavedAccount:]
- -[SFSharablePassword(AccountSavingExtras) _saveOneTimeCodeForSavedAccount:]
- -[SFSharablePassword(AccountSavingExtras) saveToKeychain]
- GCC_except_table32
- GCC_except_table43
- GCC_except_table63
- __114-[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:]_block_invoke.60
- __114-[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:]_block_invoke_2.61
- __52-[SFAppAutoFillOneTimeCodeProvider initWithOptions:]_block_invoke.47
- __52-[SFAppAutoFillOneTimeCodeProvider initWithOptions:]_block_invoke_2.48
- __80-[SFAppAutoFillOneTimeCodeProvider _savedAccountsWithPasswordsForURL:inContext:]_block_invoke.117
- __81-[SFAppAutoFillOneTimeCodeProvider _sortedOneTimeCodesFromSavedAccounts:context:]_block_invoke.129
- ___75-[SFCredentialProviderExtensionManager getEnabledExtensionsWithCompletion:]_block_invoke
- ___75-[SFCredentialProviderExtensionManager getEnabledExtensionsWithCompletion:]_block_invoke_2
- ___block_descriptor_32_e47_"WBSSavedAccount"16?0"WBSSavedAccountMatch"8l
- ___block_descriptor_40_e8_32s_e25_B16?0"WBSSavedAccount"8l
- ___block_descriptor_40_e8_32s_e56_"NSMutableSet"24?0"WBSSavedAccount"8"NSMutableSet"16l
- ___block_descriptor_40_e8_32s_e71_"SFAutoFillOneTimeCode"32?0"NSNumber"8"SFAutoFillOneTimeCode"16^B24l
- ___block_descriptor_56_e8_32bs40r48r_e29_v24?0"NSArray"8"NSError"16l
- __block_literal_global.120
- __block_literal_global.132
- __block_literal_global.184
- __block_literal_global.24
- __block_literal_global.75
- _objc_msgSend$_saveAdditionalSitesForSavedAccount:
- _objc_msgSend$_saveCustomTitleForSavedAccount:
- _objc_msgSend$_saveNotesEntryForSavedAccount:
- _objc_msgSend$_saveOneTimeCodeForSavedAccount:
- _objc_msgSend$didFillCredentialForUsername:forHost:fromProviderWithBundleIdentifier:inAppWithBundleIdentifier:
- _objc_msgSend$lastUsedDateForContext:
- _objc_msgSend$providerBundleID
- _objc_msgSend$saveAdditionalSites:forSavedAccount:
- _objc_msgSend$saveCustomTitle:forSavedAccount:
- _objc_msgSend$saveNotesEntry:forSavedAccount:
- _objc_msgSend$saveTOTPGenerator:forSavedAccount:
CStrings:
+ "%{sensitive, mask.hash}@ is expired; removing from cache"
+ "%{sensitive, mask.hash}@ is ignored; removing from cache"
+ ".sng.link"
+ "@\"NSMutableSet\"24@?0@\"WBSPair\"8@\"NSMutableSet\"16"
+ "@\"WBSPair\"16@?0@\"WBSSavedAccountMatch\"8"
+ "App %{sensitive, mask.hash}@ has web browser entitlement. Checking domain against website URL %{sensitive, mask.hash}@."
+ "B16@?0@\"NSDate\"8"
+ "B16@?0@\"WBSPair\"8"
+ "Checking domain against associated domains for app %{sensitive, mask.hash}@."
+ "Could not fetch application record for application identifier: %{sensitive, mask.hash}@."
+ "Domain-bound verification code is %@valid for app %{sensitive, mask.hash}@."
+ "Domain-bound verification code is %@valid for frame URLs from web browser: %{sensitive, mask.hash}@"
+ "IgnoredOneTimeCodeTimestamps"
+ "Q24@0:8@16"
+ "SupportedCredentialExchangeVersions"
+ "T@\"LSApplicationRecord\",R,C,N"
+ "Verification Code"
+ "_TtC16SafariFoundation39SymbolOfNewBeginningsInSafariFoundation"
+ "_getExtensionsIncludingDisabled:completionHandler:"
+ "_ignoredTimestamps"
+ "_numberOfAutoFillProvidersEnabledWithExtensions:"
+ "_saveAdditionalSitesForSavedAccount:completionHandler:"
+ "_saveCustomTitleForSavedAccount:completionHandler:"
+ "_saveNotesEntryForSavedAccount:completionHandler:"
+ "_saveOneTimeCodeForSavedAccount:completionHandler:"
+ "_shouldIgnoreOneTimeCode:"
+ "arrayForKey:"
+ "didFillCredentialForUsername:forHost:fromProviderWithBundleIdentifier:inAppWithBundleIdentifier:externalProviderConditionalRegistrationRequester:"
+ "extensionSupportedCredentialExchangeFormatVersions:"
+ "getAllExtensionsForContainingApp:completion:"
+ "getAllExtensionsWithCompletion:"
+ "isUserAllowedToTogglePasswordAutoFillEnabledState"
+ "lastUsedDateForSite:inContext:"
+ "numberOfAutoFillProvidersEnabledWithCompletion:"
+ "objectIsForcedForKey:"
+ "requiresAuthentication"
+ "safari_arrayContainingObjectsOfClass:forKey:"
+ "saveAdditionalSites:forSavedAccount:completionHandler:"
+ "saveCustomTitle:forSavedAccount:completionHandler:"
+ "saveNotesEntry:forSavedAccount:completionHandler:"
+ "saveTOTPGenerator:forSavedAccount:completionHandler:"
+ "saveToKeychainWithCompletionHandler:"
+ "sf_applicationRecordForContainingApp"
+ "silenceOneTimeCode:"
+ "v28@0:8B16@?20"
+ "welcomeToTheWorldOfTomorrow"
- "%@ is expired; removing from cache"
- "@\"NSMutableSet\"24@?0@\"WBSSavedAccount\"8@\"NSMutableSet\"16"
- "@\"WBSSavedAccount\"16@?0@\"WBSSavedAccountMatch\"8"
- "App %@ has web browser entitlement. Checking domain against website URL %{sensitive, mask.hash}@."
- "B16@?0@\"WBSSavedAccount\"8"
- "Checking domain against associated domains for app %@."
- "Could not fetch application record for application identifier: %{private}@."
- "Domain-bound verification code is %@valid for app %@."
- "Domain-bound verification code is %@valid for frame URLs from web browser: %{private}@"
- "_saveAdditionalSitesForSavedAccount:"
- "_saveCustomTitleForSavedAccount:"
- "_saveNotesEntryForSavedAccount:"
- "_saveOneTimeCodeForSavedAccount:"
- "didFillCredentialForUsername:forHost:fromProviderWithBundleIdentifier:inAppWithBundleIdentifier:"
- "didFillExternalCredential:inAppWithBundleIdentifier:"
- "lastUsedDateForContext:"
- "saveAdditionalSites:forSavedAccount:"
- "saveCustomTitle:forSavedAccount:"
- "saveNotesEntry:forSavedAccount:"
- "saveTOTPGenerator:forSavedAccount:"
- "saveToKeychain"

```
