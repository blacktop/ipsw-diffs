## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`

```diff

-623.1.12.10.4
-  __TEXT.__text: 0x138348
-  __TEXT.__auth_stubs: 0x3140
-  __TEXT.__objc_methlist: 0xbcdc
-  __TEXT.__const: 0x3390
-  __TEXT.__gcc_except_tab: 0x6ef8
-  __TEXT.__cstring: 0x135f5
+623.1.13.10.3
+  __TEXT.__text: 0x13ab44
+  __TEXT.__auth_stubs: 0x3180
+  __TEXT.__objc_methlist: 0xbcfc
+  __TEXT.__const: 0x33b0
+  __TEXT.__gcc_except_tab: 0x6f04
+  __TEXT.__cstring: 0x136b5
   __TEXT.__ustring: 0x2810
-  __TEXT.__oslogstring: 0xa7fd
+  __TEXT.__oslogstring: 0xaa1d
   __TEXT.__dlopen_cstrs: 0x157
-  __TEXT.__swift5_typeref: 0xfdf
+  __TEXT.__swift5_typeref: 0x100f
   __TEXT.__swift5_fieldmd: 0x964
   __TEXT.__constg_swiftt: 0xaf0
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_reflstr: 0x710
   __TEXT.__swift5_assocty: 0x238
-  __TEXT.__swift5_capture: 0x630
+  __TEXT.__swift5_capture: 0x684
   __TEXT.__swift5_proto: 0x214
   __TEXT.__swift5_types: 0xdc
-  __TEXT.__swift_as_entry: 0xf0
-  __TEXT.__swift_as_ret: 0xcc
+  __TEXT.__swift_as_entry: 0xf8
+  __TEXT.__swift_as_ret: 0xe0
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x66c8
-  __TEXT.__eh_frame: 0x33a8
+  __TEXT.__unwind_info: 0x6768
+  __TEXT.__eh_frame: 0x35c0
   __TEXT.__objc_classname: 0x1a78
-  __TEXT.__objc_methname: 0x252eb
-  __TEXT.__objc_methtype: 0x4016
-  __TEXT.__objc_stubs: 0x12040
+  __TEXT.__objc_methname: 0x253c3
+  __TEXT.__objc_methtype: 0x4020
+  __TEXT.__objc_stubs: 0x12080
   __DATA_CONST.__got: 0xe68
-  __DATA_CONST.__const: 0x4fa8
+  __DATA_CONST.__const: 0x4fb0
   __DATA_CONST.__objc_classlist: 0x608
   __DATA_CONST.__objc_catlist: 0x170
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6ce0
+  __DATA_CONST.__objc_selrefs: 0x6d00
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x498
-  __DATA_CONST.__objc_arraydata: 0x2a70
-  __AUTH_CONST.__auth_got: 0x18b8
-  __AUTH_CONST.__const: 0x6998
-  __AUTH_CONST.__cfstring: 0x193a0
+  __DATA_CONST.__objc_arraydata: 0x2a10
+  __AUTH_CONST.__auth_got: 0x18d8
+  __AUTH_CONST.__const: 0x6aa0
+  __AUTH_CONST.__cfstring: 0x193c0
   __AUTH_CONST.__objc_const: 0x137b0
   __AUTH_CONST.__objc_intobj: 0x840
-  __AUTH_CONST.__objc_dictobj: 0x1b8
-  __AUTH_CONST.__objc_arrayobj: 0x5b8
+  __AUTH_CONST.__objc_dictobj: 0x190
+  __AUTH_CONST.__objc_arrayobj: 0x570
   __AUTH.__objc_data: 0x2710
-  __AUTH.__data: 0x628
+  __AUTH.__data: 0x618
   __DATA.__objc_ivar: 0xc40
-  __DATA.__data: 0x19a0
-  __DATA.__bss: 0x51e0
+  __DATA.__data: 0x19d0
+  __DATA.__bss: 0x5200
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1730
-  __DATA_DIRTY.__data: 0x180
+  __DATA_DIRTY.__data: 0x178
   __DATA_DIRTY.__bss: 0x3e0
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9E5430A4-6425-3843-8B26-6CCED37DDEEB
-  Functions: 7768
-  Symbols:   20783
-  CStrings:  13101
+  UUID: 574F156C-174A-3A25-8714-2C79A9343052
+  Functions: 7813
+  Symbols:   20834
+  CStrings:  13120
 
Symbols:
+ -[WBSAuthenticationServicesAgentProxy getPasskeysForRunningAssertionWithApplicationIdentifier:webPageURL:withCompletionHandler:]
+ -[WBSDevice objectForKey:].cold.1
+ -[WBSDevice objectForKey:].cold.2
+ -[WBSDevice setObject:forKey:].cold.1
+ -[WBSDevice setObject:forKey:].cold.2
+ -[WBSPasswordManagerWebsiteMetadataStore deleteMetadataForDomain:]
+ -[WBSSavedAccountKeychainCoordinator passwordCredentialExistsInKeychainForFullyQualifiedDomain:]
+ GCC_except_table161
+ GCC_except_table163
+ GCC_except_table165
+ GCC_except_table265
+ GCC_except_table272
+ GCC_except_table307
+ GCC_except_table380
+ _SecCopyErrorMessageString
+ _WBSOSLogDeviceIdentifier
+ _WBSOSLogDeviceIdentifier.cold.1
+ _WBSOSLogDeviceIdentifier.log
+ _WBSOSLogDeviceIdentifier.onceToken
+ _WBSOSLogDeviceProperties
+ _WBSOSLogDeviceProperties.cold.1
+ _WBSOSLogDeviceProperties.log
+ _WBSOSLogDeviceProperties.onceToken
+ _WBSPasswordsAppFuzzySearchSubstringShouldMatchLexiconKey
+ ___112-[WBSSavedAccountStore canSaveUser:password:forProtectionSpace:highLevelDomain:notes:customTitle:groupID:error:]_block_invoke.305
+ ___126-[WBSSavedAccountStore _cleanUpSharedSavedAccountsWithUnknownOriginalContributorParticipantIDsIfNecessaryFromRecentlyDeleted:]_block_invoke.329
+ ___128-[WBSAuthenticationServicesAgentProxy getPasskeysForRunningAssertionWithApplicationIdentifier:webPageURL:withCompletionHandler:]_block_invoke
+ ___128-[WBSAuthenticationServicesAgentProxy getPasskeysForRunningAssertionWithApplicationIdentifier:webPageURL:withCompletionHandler:]_block_invoke.77
+ ___128-[WBSAuthenticationServicesAgentProxy getPasskeysForRunningAssertionWithApplicationIdentifier:webPageURL:withCompletionHandler:]_block_invoke.cold.1
+ ___145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke.358
+ ___145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke_2.359
+ ___147-[WBSSavedAccountStore _getSavedAccountMatchesFromSavedAccountTreeMatchesOnInternalQueue:withCriteria:mergingAutoFillPasskeys:nearbyDeviceOptions:]_block_invoke.408
+ ___63-[WBSSavedAccountStore _removeCredentialTypes:forSavedAccount:]_block_invoke
+ ___66-[WBSPasswordManagerWebsiteMetadataStore deleteMetadataForDomain:]_block_invoke
+ ___66-[WBSPasswordManagerWebsiteMetadataStore deleteMetadataForDomain:]_block_invoke.cold.1
+ ___66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.366
+ ___66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.370
+ ___69-[WBSSavedAccountStore _performRecentlyDeletedMaintenanceIfNecessary]_block_invoke.339
+ ___74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.340
+ ___74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.340.cold.1
+ ___74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.344
+ ___74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke_2.346
+ ___86-[WBSSavedAccountStore _ensureNoRecentlyDeletedSavedAccountsConflictWithSavedAccount:]_block_invoke.379
+ ___86-[WBSSavedAccountStore _moveContributedSavedAccountsBackToPersonalKeychainIfNecessary]_block_invoke.365
+ ___95-[WBSSavedAccountStore _changeSavedAccountWithRequestOnInternalQueue:performPostUpdateActions:]_block_invoke.275
+ ___WBSOSLogDeviceIdentifier_block_invoke
+ ___WBSOSLogDeviceProperties_block_invoke
+ ___block_literal_global.137
+ ___block_literal_global.151
+ ___block_literal_global.158
+ ___block_literal_global.163
+ ___block_literal_global.176
+ ___block_literal_global.200
+ ___block_literal_global.202
+ ___block_literal_global.217
+ ___block_literal_global.260
+ ___block_literal_global.262
+ ___block_literal_global.314
+ ___block_literal_global.320
+ ___block_literal_global.328
+ ___block_literal_global.353
+ ___block_literal_global.361
+ ___block_literal_global.406
+ ___block_literal_global.592
+ ___block_literal_global.604
+ ___block_literal_global.633
+ ___block_literal_global.636
+ ___block_literal_global.862
+ ___block_literal_global.939
+ ___block_literal_global.945
+ _block_copy_helper.80
+ _block_descriptor.82
+ _block_destroy_helper.81
+ _objc_msgSend$getPasskeysForRunningAssertionWithApplicationIdentifier:webPageURL:withCompletionHandler:
+ _objc_msgSend$precomposedStringWithCompatibilityMapping
+ _objc_msgSend$removeWebsiteMetadataIfNecessaryForSavedAccount:coordinator:completionHandler:
+ _objectdestroy.27Tm
+ _symbolic So34WBSSavedAccountKeychainCoordinatorC
+ _symbolic _____Sg 10Foundation6LocaleV
- -[WBSAuthenticationServicesAgentProxy getPasskeysForRunningAssertionWithApplicationIdentifier:withCompletionHandler:]
- GCC_except_table160
- GCC_except_table167
- GCC_except_table169
- GCC_except_table264
- GCC_except_table271
- GCC_except_table306
- GCC_except_table366
- GCC_except_table368
- GCC_except_table373
- GCC_except_table379
- GCC_except_table86
- ___112-[WBSSavedAccountStore canSaveUser:password:forProtectionSpace:highLevelDomain:notes:customTitle:groupID:error:]_block_invoke.304
- ___117-[WBSAuthenticationServicesAgentProxy getPasskeysForRunningAssertionWithApplicationIdentifier:withCompletionHandler:]_block_invoke
- ___117-[WBSAuthenticationServicesAgentProxy getPasskeysForRunningAssertionWithApplicationIdentifier:withCompletionHandler:]_block_invoke.77
- ___117-[WBSAuthenticationServicesAgentProxy getPasskeysForRunningAssertionWithApplicationIdentifier:withCompletionHandler:]_block_invoke.cold.1
- ___126-[WBSSavedAccountStore _cleanUpSharedSavedAccountsWithUnknownOriginalContributorParticipantIDsIfNecessaryFromRecentlyDeleted:]_block_invoke.328
- ___145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke.357
- ___145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke_2.358
- ___147-[WBSSavedAccountStore _getSavedAccountMatchesFromSavedAccountTreeMatchesOnInternalQueue:withCriteria:mergingAutoFillPasskeys:nearbyDeviceOptions:]_block_invoke.407
- ___66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.365
- ___66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.369
- ___69-[WBSSavedAccountStore _performRecentlyDeletedMaintenanceIfNecessary]_block_invoke.338
- ___74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.339
- ___74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.339.cold.1
- ___74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.343
- ___74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke_2.345
- ___86-[WBSSavedAccountStore _ensureNoRecentlyDeletedSavedAccountsConflictWithSavedAccount:]_block_invoke.378
- ___86-[WBSSavedAccountStore _moveContributedSavedAccountsBackToPersonalKeychainIfNecessary]_block_invoke.364
- ___95-[WBSSavedAccountStore _changeSavedAccountWithRequestOnInternalQueue:performPostUpdateActions:]_block_invoke.274
- ___block_literal_global.128
- ___block_literal_global.148
- ___block_literal_global.155
- ___block_literal_global.160
- ___block_literal_global.164
- ___block_literal_global.182
- ___block_literal_global.199
- ___block_literal_global.211
- ___block_literal_global.218
- ___block_literal_global.259
- ___block_literal_global.263
- ___block_literal_global.266
- ___block_literal_global.313
- ___block_literal_global.319
- ___block_literal_global.347
- ___block_literal_global.350
- ___block_literal_global.352
- ___block_literal_global.368
- ___block_literal_global.377
- ___block_literal_global.416
- ___block_literal_global.861
- ___block_literal_global.938
- ___block_literal_global.944
- _block_copy_helper.61
- _block_descriptor.63
- _block_destroy_helper.62
- _objc_msgSend$getPasskeysForRunningAssertionWithApplicationIdentifier:withCompletionHandler:
- _objectdestroy.25Tm
CStrings:
+ "DeviceIdentifier"
+ "DeviceProperties"
+ "Did delete device property for key %{public}@"
+ "Did fail to copy device property for key %{public}@, error: %d, message: %{public}@"
+ "Did fail to encode device property value for key %{public}@, error: %{public}@"
+ "Did fail to save device property for key %{public}@, error: %d, message: %{public}@"
+ "Did save device property value for key %{public}@"
+ "EnablePasswordsFuzzySearchSubstringShouldMatchLexicon"
+ "Failed to decode device property data for key %{public}@, error: %{public}@"
+ "Failed to delete website metadata for %{sensitive}@: %d"
+ "No existing device property for key %@"
+ "Removed website metadata for %{sensitive}@"
+ "deleteMetadataForDomain:"
+ "getPasskeysForRunningAssertionWithApplicationIdentifier:webPageURL:withCompletionHandler:"
+ "passwordCredentialExistsInKeychainForFullyQualifiedDomain:"
+ "precomposedStringWithCompatibilityMapping"
+ "removeWebsiteMetadataIfNecessaryForSavedAccount:coordinator:completionHandler:"
+ "v24@?0r^{_LXEntry=}8*16"
+ "v40@0:8@\"NSString\"16@\"NSURL\"24@?<v@?@\"NSArray\"@\"WBSPasskeyAutoFillFromNearbyDeviceOptions\">32"
+ "v40@0:8@\"WBSSavedAccount\"16@\"WBSSavedAccountKeychainCoordinator\"24@?<v@?B>32"
- "getPasskeysForRunningAssertionWithApplicationIdentifier:withCompletionHandler:"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"WBSPasskeyAutoFillFromNearbyDeviceOptions\">24"

```
