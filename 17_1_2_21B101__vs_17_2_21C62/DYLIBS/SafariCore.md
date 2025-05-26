## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`

```diff

-616.2.9.10.13
-  __TEXT.__text: 0x987e4
-  __TEXT.__auth_stubs: 0x12b0
-  __TEXT.__objc_methlist: 0x78b4
-  __TEXT.__const: 0x1e8
-  __TEXT.__cstring: 0xa4bc
-  __TEXT.__gcc_except_tab: 0x3938
-  __TEXT.__oslogstring: 0x77c8
+617.1.17.10.9
+  __TEXT.__text: 0x9bc6c
+  __TEXT.__auth_stubs: 0x13c0
+  __TEXT.__objc_methlist: 0x7b40
+  __TEXT.__const: 0x232
+  __TEXT.__cstring: 0xba73
+  __TEXT.__oslogstring: 0x7aa3
+  __TEXT.__gcc_except_tab: 0x3b34
   __TEXT.__ustring: 0x16c4
   __TEXT.__dlopen_cstrs: 0xf3
-  __TEXT.__unwind_info: 0x3664
+  __TEXT.__constg_swiftt: 0x48
+  __TEXT.__swift5_typeref: 0x1f
+  __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0x37b4
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x12ab
-  __TEXT.__objc_methname: 0x1a153
-  __TEXT.__objc_methtype: 0x2c96
-  __TEXT.__objc_stubs: 0xd8a0
-  __DATA_CONST.__got: 0x318
-  __DATA_CONST.__const: 0x3bf8
-  __DATA_CONST.__objc_classlist: 0x430
-  __DATA_CONST.__objc_catlist: 0x130
+  __TEXT.__objc_classname: 0x1302
+  __TEXT.__objc_methname: 0x1aa2b
+  __TEXT.__objc_methtype: 0x2d91
+  __TEXT.__objc_stubs: 0xdba0
+  __DATA_CONST.__got: 0x348
+  __DATA_CONST.__const: 0x3d80
+  __DATA_CONST.__objc_classlist: 0x448
+  __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa298
-  __DATA_CONST.__objc_selrefs: 0x4dd8
-  __DATA_CONST.__objc_arraydata: 0x6e0
-  __AUTH_CONST.__cfstring: 0xbe00
-  __AUTH_CONST.__objc_const: 0x3a28
-  __AUTH_CONST.__const: 0x1640
-  __AUTH_CONST.__objc_intobj: 0x258
+  __DATA_CONST.__objc_const: 0xa718
+  __DATA_CONST.__objc_selrefs: 0x4f50
+  __DATA_CONST.__objc_arraydata: 0x2630
+  __AUTH_CONST.__cfstring: 0x13f80
+  __AUTH_CONST.__objc_const: 0x3af8
+  __AUTH_CONST.__const: 0x16c8
+  __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0x168
-  __AUTH_CONST.__objc_arrayobj: 0x468
+  __AUTH_CONST.__objc_arrayobj: 0x480
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x970
-  __AUTH.__objc_data: 0x1770
+  __AUTH_CONST.__auth_got: 0x9f8
+  __AUTH.__objc_data: 0x18c8
+  __AUTH.__data: 0x28
   __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x570
-  __DATA.__objc_superrefs: 0x348
-  __DATA.__objc_ivar: 0x7d4
-  __DATA.__data: 0x978
-  __DATA.__bss: 0x3f8
+  __DATA.__objc_classrefs: 0x588
+  __DATA.__objc_superrefs: 0x358
+  __DATA.__objc_ivar: 0x818
+  __DATA.__data: 0x980
+  __DATA.__bss: 0x428
   __DATA_DIRTY.__objc_data: 0x1270
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x398

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3816
-  Symbols:   12818
-  CStrings:  6043
+  - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  Functions: 3899
+  Symbols:   13100
+  CStrings:  7178
 
Symbols:
+ +[NSUserDefaults(SafariCoreExtras) safari_canonicalApplicationDefaults]
+ +[WBSFeatureAvailability isSearchEvaluationLoggingEnabled]
+ +[WBSSavedAccountContext _nameForDefaultSafariProfile]
+ -[LSApplicationWorkspace(SafariCoreExtras) safari_setDefaultOTPAuthMigrationURLHandlerToApplicationWithBundleIdentifier:completionHandler:]
+ -[LSApplicationWorkspace(SafariCoreExtras) safari_setDefaultOTPAuthMigrationURLHandlerToApplicationWithBundleIdentifier:shouldFallBackToSystemHandlerIfNeeded:completionHandler:]
+ -[LSApplicationWorkspace(SafariCoreExtras) safari_setDefaultOTPAuthURLHandlerToApplicationWithBundleIdentifier:completionHandler:]
+ -[LSApplicationWorkspace(SafariCoreExtras) safari_setDefaultOTPAuthURLHandlerToApplicationWithBundleIdentifier:shouldFallBackToSystemHandlerIfNeeded:completionHandler:]
+ -[LSApplicationWorkspace(SafariCoreExtras) safari_setDefaultURLHandlerForScheme:toApplicationWithBundleIdentifier:completionHandler:]
+ -[LSApplicationWorkspace(SafariCoreExtras) safari_setDefaultURLHandlerForScheme:toApplicationWithBundleIdentifier:completionHandler:].cold.1
+ -[NSDate(WBSNSDateExtras) safari_filenameFormattedString]
+ -[NSError(SafariCoreExtras) safari_matchesErrorDomain:]
+ -[NSString(SafariCoreExtras) safari_caseAndDiacriticInsensitiveStandardRangeOfString:additionalOptions:]
+ -[NSString(SafariCoreExtras) safari_isPathExtensionAllowedForAnalytics]
+ -[NSString(SafariCoreExtras) safari_stringByRemovingTopLevelDomainFromHost]
+ -[NSString(WBSURLHostComponentEnumeratorExtras) safari_hostComponentsEnumerator]
+ -[NSString(WBSURLHostComponentEnumeratorExtras) safari_hostDomainsEnumerator]
+ -[NSURL(SafariCoreExtras) safari_URLWithUniqueFilename]
+ -[NSURL(SafariCoreExtras) safari_absoluteStringWithoutFragment]
+ -[NSURL(SafariCoreExtras) safari_accessingSecurityScopedResource:]
+ -[NSURL(SafariCoreExtras) safari_hasScheme:]
+ -[NSURL(SafariCoreExtras) safari_highLevelDomainFromHostFallingBackToHostOrAbsoluteString]
+ -[NSURL(SafariCoreExtras) safari_hostCompare:]
+ -[NSURL(SafariCoreExtras) safari_isAppleNewsURL]
+ -[NSURL(SafariCoreExtras) safari_isAppleOneURL]
+ -[NSURL(SafariCoreExtras) safari_isXWebSearchURL]
+ -[NSURL(SafariCoreExtras) safari_topLevelDomain]
+ -[NSURL(WBSURLHostComponentEnumeratorExtras) safari_hostComponentsEnumerator]
+ -[NSURL(WBSURLHostComponentEnumeratorExtras) safari_hostDomainsEnumerator]
+ -[WBSAnalyticsLogger didActivateVoiceSearchAccidentally:]
+ -[WBSAnalyticsLogger didSelectFavoritesRow:]
+ -[WBSAnalyticsLogger reportAdvancedPrivacyProtectionPreference]
+ -[WBSAnalyticsLogger reportNewTabBehavior:]
+ -[WBSAnalyticsLogger reportNewWindowBehavior:]
+ -[WBSAnalyticsLogger reportTabGroupSyncFinishedWithInfo:]
+ -[WBSAnalyticsLogger reportTabGroupSyncSuccessesWithCount:]
+ -[WBSAnalyticsLogger reportTabUpdatedWithUpdateType:]
+ -[WBSBuildingLegacy .cxx_destruct]
+ -[WBSBuildingLegacy bridgingInspiration]
+ -[WBSBuildingLegacy init]
+ -[WBSSavedAccountStore numberOfSavedAccountsInPersonalKeychainForHighLevelDomain:]
+ -[WBSSavedAccountStore savedAccountsForGroupID:].cold.1
+ -[WBSSavedAccountStore updateAllSavedAccountsWithPasswordsWithUser:protectionSpace:withNewPassword:]
+ -[WBSURLHostComponentEnumerator .cxx_destruct]
+ -[WBSURLHostComponentEnumerator _checkIsIPAddress]
+ -[WBSURLHostComponentEnumerator _nextPointRangeInRange:didFindPeriod:]
+ -[WBSURLHostComponentEnumerator clearAccumulatedDomains]
+ -[WBSURLHostComponentEnumerator containsEmptyComponents]
+ -[WBSURLHostComponentEnumerator host]
+ -[WBSURLHostComponentEnumerator initWithHost:options:]
+ -[WBSURLHostComponentEnumerator init]
+ -[WBSURLHostComponentEnumerator ipv4Address]
+ -[WBSURLHostComponentEnumerator ipv6Address]
+ -[WBSURLHostComponentEnumerator isSpeculative]
+ -[WBSURLHostComponentEnumerator kind]
+ -[WBSURLHostComponentEnumerator nextObject]
+ -[WBSURLHostComponentEnumerator options]
+ GCC_except_table185
+ GCC_except_table197
+ GCC_except_table199
+ GCC_except_table204
+ GCC_except_table212
+ GCC_except_table217
+ GCC_except_table218
+ GCC_except_table222
+ GCC_except_table226
+ GCC_except_table229
+ GCC_except_table230
+ GCC_except_table231
+ GCC_except_table239
+ GCC_except_table244
+ GCC_except_table246
+ GCC_except_table248
+ GCC_except_table251
+ GCC_except_table253
+ GCC_except_table261
+ GCC_except_table270
+ GCC_except_table274
+ GCC_except_table277
+ GCC_except_table278
+ GCC_except_table293
+ GCC_except_table294
+ GCC_except_table295
+ GCC_except_table296
+ GCC_except_table298
+ GCC_except_table299
+ GCC_except_table313
+ GCC_except_table317
+ GCC_except_table319
+ GCC_except_table323
+ GCC_except_table326
+ GCC_except_table328
+ GCC_except_table333
+ GCC_except_table335
+ GCC_except_table337
+ GCC_except_table338
+ GCC_except_table48
+ GCC_except_table50
+ GCC_except_table58
+ GCC_except_table59
+ GCC_except_table61
+ GCC_except_table78
+ GCC_except_table79
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$_WBSBuildingLegacy
+ _OBJC_CLASS_$_WBSURLHostComponentEnumerator
+ _OBJC_CLASS_$__TtC10SafariCore24WBSSymbolOfNewBeginnings
+ _OBJC_IVAR_$_WBSBuildingLegacy._symbolOfNewBeginnings
+ _OBJC_IVAR_$_WBSURLHostComponentEnumerator._accumulatorString
+ _OBJC_IVAR_$_WBSURLHostComponentEnumerator._containsEmptyComponents
+ _OBJC_IVAR_$_WBSURLHostComponentEnumerator._didBeginConsumingCharacters
+ _OBJC_IVAR_$_WBSURLHostComponentEnumerator._didCheckTopLevelDomain
+ _OBJC_IVAR_$_WBSURLHostComponentEnumerator._didFindTopLevelDomain
+ _OBJC_IVAR_$_WBSURLHostComponentEnumerator._didGenerateFullHighLevelDomain
+ _OBJC_IVAR_$_WBSURLHostComponentEnumerator._host
+ _OBJC_IVAR_$_WBSURLHostComponentEnumerator._ipv4Address
+ _OBJC_IVAR_$_WBSURLHostComponentEnumerator._ipv6Address
+ _OBJC_IVAR_$_WBSURLHostComponentEnumerator._isSpeculative
+ _OBJC_IVAR_$_WBSURLHostComponentEnumerator._kind
+ _OBJC_IVAR_$_WBSURLHostComponentEnumerator._length
+ _OBJC_IVAR_$_WBSURLHostComponentEnumerator._nextSearchRange
+ _OBJC_IVAR_$_WBSURLHostComponentEnumerator._numberOfAccummulatedComponents
+ _OBJC_IVAR_$_WBSURLHostComponentEnumerator._options
+ _OBJC_IVAR_$_WBSURLHostComponentEnumerator._topLevelDomainSubstring
+ _OBJC_METACLASS_$_WBSBuildingLegacy
+ _OBJC_METACLASS_$_WBSURLHostComponentEnumerator
+ _OBJC_METACLASS_$__TtC10SafariCore24WBSSymbolOfNewBeginnings
+ _WBSAuthenticationPolicyForCreditCards
+ _WBSAuthenticationPolicyForPasswordManager
+ _WBSUseSTPPasskeyDaemonDefault
+ __DATA__TtC10SafariCore24WBSSymbolOfNewBeginnings
+ __DefaultRuneLocale
+ __METACLASS_DATA__TtC10SafariCore24WBSSymbolOfNewBeginnings
+ __OBJC_$_CATEGORY_LSApplicationWorkspace_$_SafariCoreExtras
+ __OBJC_$_CATEGORY_NSURL_$_WBSURLHostComponentEnumeratorExtras
+ __OBJC_$_CLASS_METHODS_NSString(WBSCloudBookmarksRecordNamingExtras|SafariCoreExtras|WBSURLHostComponentEnumeratorExtras)
+ __OBJC_$_CLASS_METHODS_NSURL(WBSURLHostComponentEnumeratorExtras|SafariCoreExtras)
+ __OBJC_$_INSTANCE_METHODS_LSApplicationWorkspace(SafariCoreExtras)
+ __OBJC_$_INSTANCE_METHODS_NSString(WBSCloudBookmarksRecordNamingExtras|SafariCoreExtras|WBSURLHostComponentEnumeratorExtras)
+ __OBJC_$_INSTANCE_METHODS_NSURL(WBSURLHostComponentEnumeratorExtras|SafariCoreExtras)
+ __OBJC_$_INSTANCE_METHODS_WBSBuildingLegacy
+ __OBJC_$_INSTANCE_METHODS_WBSURLHostComponentEnumerator
+ __OBJC_$_INSTANCE_METHODS__TtC10SafariCore24WBSSymbolOfNewBeginnings
+ __OBJC_$_INSTANCE_VARIABLES_WBSBuildingLegacy
+ __OBJC_$_INSTANCE_VARIABLES_WBSURLHostComponentEnumerator
+ __OBJC_$_PROP_LIST_WBSURLHostComponentEnumerator
+ __OBJC_CLASS_RO_$_WBSBuildingLegacy
+ __OBJC_CLASS_RO_$_WBSURLHostComponentEnumerator
+ __OBJC_METACLASS_RO_$_WBSBuildingLegacy
+ __OBJC_METACLASS_RO_$_WBSURLHostComponentEnumerator
+ __ZGVZ71-[NSString(SafariCoreExtras) safari_isPathExtensionAllowedForAnalytics]E16allowedMIMETypes
+ __ZL10fileExistsP5NSURL
+ __ZZ71-[NSString(SafariCoreExtras) safari_isPathExtensionAllowedForAnalytics]E16allowedMIMETypes
+ ___100-[WBSSavedAccountStore canSaveUser:password:forProtectionSpace:highLevelDomain:notes:groupID:error:]_block_invoke.203
+ ___100-[WBSSavedAccountStore updateAllSavedAccountsWithPasswordsWithUser:protectionSpace:withNewPassword:]_block_invoke
+ ___107-[NSString(SafariCoreExtras) _safari_looksLikeWillRedirectToURLStringAfterAuthentication:orHostAfterLogin:]_block_invoke_3
+ ___110-[WBSAuthenticationServicesAgentProxy getPasskeysForRunningAssertionWithWebFrameIdentifier:completionHandler:]_block_invoke.50
+ ___117-[WBSAuthenticationServicesAgentProxy getPasskeysForRunningAssertionWithApplicationIdentifier:withCompletionHandler:]_block_invoke.48
+ ___126-[WBSSavedAccountStore _cleanUpSharedSavedAccountsWithUnknownOriginalContributorParticipantIDsIfNecessaryFromRecentlyDeleted:]_block_invoke.226
+ ___128-[WBSAuthenticationServicesAgentProxy userSelectedAutoFillPasskey:authenticatedLAContext:savedAccountContext:completionHandler:]_block_invoke.51
+ ___133-[LSApplicationWorkspace(SafariCoreExtras) safari_setDefaultURLHandlerForScheme:toApplicationWithBundleIdentifier:completionHandler:]_block_invoke
+ ___133-[LSApplicationWorkspace(SafariCoreExtras) safari_setDefaultURLHandlerForScheme:toApplicationWithBundleIdentifier:completionHandler:]_block_invoke.cold.1
+ ___145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke.248
+ ___145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke_2.249
+ ___147-[WBSSavedAccountStore _getSavedAccountMatchesFromSavedAccountTreeMatchesOnInternalQueue:withCriteria:mergingAutoFillPasskeys:nearbyDeviceOptions:]_block_invoke.292
+ ___168-[LSApplicationWorkspace(SafariCoreExtras) safari_setDefaultOTPAuthURLHandlerToApplicationWithBundleIdentifier:shouldFallBackToSystemHandlerIfNeeded:completionHandler:]_block_invoke
+ ___177-[LSApplicationWorkspace(SafariCoreExtras) safari_setDefaultOTPAuthMigrationURLHandlerToApplicationWithBundleIdentifier:shouldFallBackToSystemHandlerIfNeeded:completionHandler:]_block_invoke
+ ___43-[WBSAnalyticsLogger reportNewTabBehavior:]_block_invoke
+ ___44-[WBSAnalyticsLogger didSelectFavoritesRow:]_block_invoke
+ ___46-[WBSAnalyticsLogger reportNewWindowBehavior:]_block_invoke
+ ___51-[WBSSavedAccountStore _fetchAndFilterPasskeysData]_block_invoke
+ ___53-[WBSAnalyticsLogger reportTabUpdatedWithUpdateType:]_block_invoke
+ ___54-[WBSSavedAccountStore changeSavedAccountWithRequest:]_block_invoke.192
+ ___56-[WBSKeychainSyncingMonitor _fetchKeychainSyncingStatus]_block_invoke.11
+ ___56-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:]_block_invoke.234.cold.1
+ ___56-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:]_block_invoke.238
+ ___57-[NSDate(WBSNSDateExtras) safari_filenameFormattedString]_block_invoke
+ ___57-[WBSAnalyticsLogger didActivateVoiceSearchAccidentally:]_block_invoke
+ ___57-[WBSAnalyticsLogger reportTabGroupSyncFinishedWithInfo:]_block_invoke
+ ___58+[WBSFeatureAvailability isSearchEvaluationLoggingEnabled]_block_invoke
+ ___58+[WBSFeatureAvailability isSearchEvaluationLoggingEnabled]_block_invoke_2
+ ___59-[WBSAnalyticsLogger reportTabGroupSyncSuccessesWithCount:]_block_invoke
+ ___63-[WBSAnalyticsLogger reportAdvancedPrivacyProtectionPreference]_block_invoke
+ ___66-[WBSSavedAccountStore _fetchAndFilterRecentlyDeletedPasskeysData]_block_invoke
+ ___66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.260
+ ___69-[WBSSavedAccountStore _performRecentlyDeletedMaintenanceIfNecessary]_block_invoke.233
+ ___82-[WBSSavedAccountStore numberOfSavedAccountsInPersonalKeychainForHighLevelDomain:]_block_invoke
+ ___86-[WBSSavedAccountStore _ensureNoRecentlyDeletedSavedAccountsConflictWithSavedAccount:]_block_invoke.269
+ ___86-[WBSSavedAccountStore _moveContributedSavedAccountsBackToPersonalKeychainIfNecessary]_block_invoke.255
+ ___block_descriptor_32_e41_v32?0"NSString"8"NSMutableArray"16^B24l
+ ___block_descriptor_48_ea8_32s40r_e37_v32?0"NSTextCheckingResult"8Q16^B24ls32l8r40l8
+ ___block_descriptor_49_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e36_v16?0"WBSSavedAccountMatchResult"8ls32l8s40l8s48l8
+ ___block_literal_global.1027
+ ___block_literal_global.1034
+ ___block_literal_global.1036
+ ___block_literal_global.1044
+ ___block_literal_global.1065
+ ___block_literal_global.1067
+ ___block_literal_global.1069
+ ___block_literal_global.1071
+ ___block_literal_global.1073
+ ___block_literal_global.1075
+ ___block_literal_global.122
+ ___block_literal_global.179
+ ___block_literal_global.181
+ ___block_literal_global.187
+ ___block_literal_global.212
+ ___block_literal_global.215
+ ___block_literal_global.217
+ ___block_literal_global.225
+ ___block_literal_global.241
+ ___block_literal_global.243
+ ___block_literal_global.251
+ ___block_literal_global.259
+ ___block_literal_global.267
+ ___block_literal_global.287
+ ___block_literal_global.302
+ ___block_literal_global.446
+ ___block_literal_global.48
+ ___block_literal_global.54
+ ___block_literal_global.578
+ ___block_literal_global.601
+ ___block_literal_global.61
+ ___block_literal_global.610
+ ___block_literal_global.619
+ ___block_literal_global.627
+ ___block_literal_global.63
+ ___block_literal_global.638
+ ___block_literal_global.65
+ ___block_literal_global.67
+ ___block_literal_global.69
+ ___block_literal_global.698
+ ___block_literal_global.707
+ ___block_literal_global.71
+ ___block_literal_global.73
+ ___block_literal_global.802
+ ___block_literal_global.804
+ ___block_literal_global.838
+ ___block_literal_global.904
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_reflection_version
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAVFoundation_$_SafariCore
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_SafariCore
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_SafariCore
+ __swift_FORCE_LOAD_$_swiftCoreGraphics
+ __swift_FORCE_LOAD_$_swiftCoreGraphics_$_SafariCore
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_SafariCore
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_SafariCore
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftCoreMedia_$_SafariCore
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_SafariCore
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_SafariCore
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_SafariCore
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_SafariCore
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_SafariCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_SafariCore
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_SafariCore
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_SafariCore
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_SafariCore
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_SafariCore
+ __unnamed_array_storage.3128
+ __unnamed_array_storage.451
+ __unnamed_array_storage.597
+ __unnamed_array_storage.598
+ __unnamed_array_storage.606
+ __unnamed_array_storage.607
+ __unnamed_array_storage.615
+ __unnamed_array_storage.616
+ __unnamed_array_storage.624
+ __unnamed_array_storage.625
+ __unnamed_array_storage.697
+ __unnamed_array_storage.698
+ __unnamed_array_storage.712
+ __unnamed_array_storage.713
+ __unnamed_array_storage.75
+ __unnamed_array_storage.84
+ __unnamed_array_storage.843
+ __unnamed_array_storage.844
+ __unnamed_array_storage.93
+ _inet_pton
+ _isSearchEvaluationLoggingEnabled.isSearchEvaluationLoggingEnabled
+ _isSearchEvaluationLoggingEnabled.onceToken
+ _lstat
+ _objc_allocWithZone
+ _objc_msgSend$URLByAppendingPathExtension:
+ _objc_msgSend$URLByDeletingPathExtension
+ _objc_msgSend$_checkIsIPAddress
+ _objc_msgSend$_nameForDefaultSafariProfile
+ _objc_msgSend$_nextPointRangeInRange:didFindPeriod:
+ _objc_msgSend$cStringUsingEncoding:
+ _objc_msgSend$clearAccumulatedDomains
+ _objc_msgSend$enumerateMatchesInString:options:range:usingBlock:
+ _objc_msgSend$findInspiration
+ _objc_msgSend$fragment
+ _objc_msgSend$initWithHost:options:
+ _objc_msgSend$ipv4Address
+ _objc_msgSend$ipv6Address
+ _objc_msgSend$isSpeculative
+ _objc_msgSend$kind
+ _objc_msgSend$pathComponents
+ _objc_msgSend$pathExtension
+ _objc_msgSend$safari_effectiveTopLevelDomainForHost
+ _objc_msgSend$safari_hasScheme:
+ _objc_msgSend$safari_hostComponentsEnumerator
+ _objc_msgSend$safari_hostDomainsEnumerator
+ _objc_msgSend$safari_matchesErrorDomain:
+ _objc_msgSend$safari_setDefaultOTPAuthMigrationURLHandlerToApplicationWithBundleIdentifier:shouldFallBackToSystemHandlerIfNeeded:completionHandler:
+ _objc_msgSend$safari_setDefaultOTPAuthURLHandlerToApplicationWithBundleIdentifier:shouldFallBackToSystemHandlerIfNeeded:completionHandler:
+ _objc_msgSend$safari_setDefaultURLHandlerForScheme:toApplicationWithBundleIdentifier:completionHandler:
+ _objc_msgSend$savedAccountsInPersonalKeychainExcludingNeverSaveMarkerPasswords
+ _objc_msgSend$setDefaultURLHandlerForScheme:to:completion:
+ _objc_msgSend$startAccessingSecurityScopedResource
+ _objc_msgSend$stopAccessingSecurityScopedResource
+ _objc_opt_self
+ _safari_filenameFormattedString.dateFormatter
+ _safari_filenameFormattedString.onceToken
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_getTypeByMangledNameInContext2
+ _swift_isaMask
+ _swift_lookUpClassMethod
+ _swift_release
+ _swift_retain
+ _symbolic So8NSObjectC
+ _symbolic _____ 10SafariCore24WBSSymbolOfNewBeginningsC
+ _symbolic _____yS2SG s18_DictionaryStorageC
- +[NSString(SafariCoreExtras) safari_reverseEnumerateComponents:usingBlock:]
- +[WBSTOTPGenerator countdownStringForMultipleCodesWithSecondsRemaining:]
- -[NSString(SafariCoreExtras) safari_highLevelDomainFromHostComponents:]
- -[NSString(SafariCoreExtras) safari_topLevelDomainUsingCFFromComponents:]
- -[NSURL(SafariCoreExtras) _labelsOfDomainWithoutWWWOrMSubdomains:]
- -[WBSSavedAccountStore numberOfSavedAccountsForHighLevelDomain:]
- GCC_except_table116
- GCC_except_table182
- GCC_except_table187
- GCC_except_table192
- GCC_except_table198
- GCC_except_table200
- GCC_except_table211
- GCC_except_table213
- GCC_except_table216
- GCC_except_table220
- GCC_except_table223
- GCC_except_table224
- GCC_except_table227
- GCC_except_table234
- GCC_except_table236
- GCC_except_table238
- GCC_except_table241
- GCC_except_table245
- GCC_except_table249
- GCC_except_table252
- GCC_except_table268
- GCC_except_table272
- GCC_except_table276
- GCC_except_table279
- GCC_except_table283
- GCC_except_table285
- GCC_except_table288
- GCC_except_table305
- GCC_except_table307
- GCC_except_table309
- GCC_except_table311
- GCC_except_table318
- GCC_except_table320
- GCC_except_table40
- GCC_except_table43
- GCC_except_table53
- GCC_except_table54
- GCC_except_table69
- GCC_except_table81
- __OBJC_$_CATEGORY_NSURL_$_SafariCoreExtras
- __OBJC_$_CLASS_METHODS_NSString(WBSCloudBookmarksRecordNamingExtras|SafariCoreExtras)
- __OBJC_$_CLASS_METHODS_NSURL(SafariCoreExtras)
- __OBJC_$_INSTANCE_METHODS_NSString(WBSCloudBookmarksRecordNamingExtras|SafariCoreExtras)
- __OBJC_$_INSTANCE_METHODS_NSURL(SafariCoreExtras)
- ___100-[WBSSavedAccountStore canSaveUser:password:forProtectionSpace:highLevelDomain:notes:groupID:error:]_block_invoke.199
- ___105-[NSString(SafariCoreExtras) safari_highLevelDomainForUserTypedStringWhenAddingPasswordInPasswordManager]_block_invoke
- ___110-[WBSAuthenticationServicesAgentProxy getPasskeysForRunningAssertionWithWebFrameIdentifier:completionHandler:]_block_invoke.47
- ___117-[WBSAuthenticationServicesAgentProxy getPasskeysForRunningAssertionWithApplicationIdentifier:withCompletionHandler:]_block_invoke.45
- ___126-[WBSSavedAccountStore _cleanUpSharedSavedAccountsWithUnknownOriginalContributorParticipantIDsIfNecessaryFromRecentlyDeleted:]_block_invoke.222
- ___128-[WBSAuthenticationServicesAgentProxy userSelectedAutoFillPasskey:authenticatedLAContext:savedAccountContext:completionHandler:]_block_invoke.48
- ___145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke.244
- ___145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke_2.245
- ___147-[WBSSavedAccountStore _getSavedAccountMatchesFromSavedAccountTreeMatchesOnInternalQueue:withCriteria:mergingAutoFillPasskeys:nearbyDeviceOptions:]_block_invoke.288
- ___54-[WBSSavedAccountStore changeSavedAccountWithRequest:]_block_invoke.188
- ___56-[WBSKeychainSyncingMonitor _fetchKeychainSyncingStatus]_block_invoke.8
- ___56-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:]_block_invoke.230
- ___56-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:]_block_invoke.230.cold.1
- ___66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.252
- ___67-[NSString(SafariCoreExtras) safari_effectiveTopLevelDomainForHost]_block_invoke
- ___69-[WBSSavedAccountStore _performRecentlyDeletedMaintenanceIfNecessary]_block_invoke.229
- ___73-[NSString(SafariCoreExtras) safari_topLevelDomainUsingCFFromComponents:]_block_invoke
- ___86-[WBSSavedAccountStore _ensureNoRecentlyDeletedSavedAccountsConflictWithSavedAccount:]_block_invoke.265
- ___86-[WBSSavedAccountStore _moveContributedSavedAccountsBackToPersonalKeychainIfNecessary]_block_invoke.251
- ___block_descriptor_32_e18_B16?0"NSString"8l
- ___block_descriptor_48_ea8_32r40r_e25_v32?0"NSString"8Q16^B24lr32l8r40l8
- ___block_literal_global.1001
- ___block_literal_global.1003
- ___block_literal_global.1008
- ___block_literal_global.1031
- ___block_literal_global.1033
- ___block_literal_global.1035
- ___block_literal_global.1037
- ___block_literal_global.1039
- ___block_literal_global.143
- ___block_literal_global.183
- ___block_literal_global.208
- ___block_literal_global.211
- ___block_literal_global.213
- ___block_literal_global.237
- ___block_literal_global.239
- ___block_literal_global.247
- ___block_literal_global.255
- ___block_literal_global.263
- ___block_literal_global.283
- ___block_literal_global.298
- ___block_literal_global.36
- ___block_literal_global.425
- ___block_literal_global.45
- ___block_literal_global.49
- ___block_literal_global.557
- ___block_literal_global.56
- ___block_literal_global.568
- ___block_literal_global.580
- ___block_literal_global.598
- ___block_literal_global.60
- ___block_literal_global.616
- ___block_literal_global.617
- ___block_literal_global.62
- ___block_literal_global.64
- ___block_literal_global.686
- ___block_literal_global.687
- ___block_literal_global.781
- ___block_literal_global.783
- ___block_literal_global.817
- ___block_literal_global.880
- ___block_literal_global.994
- ___block_literal_global.996
- __unnamed_array_storage.430
- __unnamed_array_storage.576
- __unnamed_array_storage.577
- __unnamed_array_storage.585
- __unnamed_array_storage.586
- __unnamed_array_storage.594
- __unnamed_array_storage.595
- __unnamed_array_storage.603
- __unnamed_array_storage.604
- __unnamed_array_storage.676
- __unnamed_array_storage.677
- __unnamed_array_storage.691
- __unnamed_array_storage.692
- __unnamed_array_storage.822
- __unnamed_array_storage.823
- __unnamed_array_storage.85
- _objc_msgSend$_labelsOfDomainWithoutWWWOrMSubdomains:
- _objc_msgSend$safari_highLevelDomainFromHostComponents:
- _objc_msgSend$safari_reverseEnumerateComponents:usingBlock:
- _objc_msgSend$safari_topLevelDomainUsingCFFromComponents:
- _objc_msgSend$stringWithCapacity:
CStrings:
+ "\x02a"
+ "%@-%u"
+ "%s: Loaded %zu passkey keychain records from group %{public}@"
+ "%s: Loaded %zu passkey keychain records from personal keychain"
+ "%s: Loaded %zu password keychain records from group: %{public}@ from Recently Deleted: %@"
+ "%s: Loaded %zu recently deleted passkey keychain records from group %{public}@"
+ "%s: Loaded %zu recently deleted passkey keychain records from personal keychain"
+ "(log.{0,2}(in|on|out))|(sign.{0,2}(in|on|up|out))|account|auth|authentication|federate|setsid"
+ "-[WBSSavedAccountStore _fetchAndFilterPasskeysData]"
+ "-[WBSSavedAccountStore _fetchAndFilterPasskeysData]_block_invoke"
+ "-[WBSSavedAccountStore _fetchAndFilterRecentlyDeletedPasskeysData]"
+ "-[WBSSavedAccountStore _fetchAndFilterRecentlyDeletedPasskeysData]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/__tree"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/__utility/exception_guard.h"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/vector"
+ "3dml"
+ "3ds"
+ "3g2"
+ "3gp"
+ "7z"
+ "@\"NSMutableString\""
+ "@\"_TtC10SafariCore24WBSSymbolOfNewBeginnings\""
+ "Attempting to set default URL handler for scheme %@ to bundle ID %@"
+ "Empty Page"
+ "Extensions"
+ "Failed to load application record for bundle ID %@; error=%{public}@"
+ "Failed to set default URL handler for scheme %@ to bundle ID %@; error=%{public}@"
+ "Fatal error"
+ "Homepage"
+ "I16@0:8"
+ "Inspiration yet to be found."
+ "Overriding iCloud Keychain check due to iCloudKeychainEnabledOverrideDefault"
+ "Queried account store for saved accounts from group but no dictionary exists for groupID: %@"
+ "SafariCore/WBSSymbolOfNewBeginnings.swift"
+ "Same Page"
+ "Start Page"
+ "T@\"NSString\",R,C,N,V_host"
+ "T@\"WBSURLHostComponentEnumerator\",R,N"
+ "TB,R,N,V_containsEmptyComponents"
+ "TB,R,N,V_isSpeculative"
+ "TI,R,N,V_ipv4Address"
+ "TQ,R,N,V_options"
+ "Tabs"
+ "Tq,R,N,V_kind"
+ "T{in6_addr=(?=[16C][8S][4I])},R,N,V_ipv6Address"
+ "URLByAppendingPathExtension:"
+ "URLByDeletingPathExtension"
+ "WBSBuildingLegacy"
+ "WBSDebugSearchEvaluationLogging"
+ "WBSURLHostComponentEnumerator"
+ "WBSURLHostComponentEnumeratorExtras"
+ "_TtC10SafariCore24WBSSymbolOfNewBeginnings"
+ "_accumulatorString"
+ "_checkIsIPAddress"
+ "_containsEmptyComponents"
+ "_didBeginConsumingCharacters"
+ "_didCheckTopLevelDomain"
+ "_didFindTopLevelDomain"
+ "_didGenerateFullHighLevelDomain"
+ "_ipv4Address"
+ "_ipv6Address"
+ "_isSpeculative"
+ "_kind"
+ "_length"
+ "_nameForDefaultSafariProfile"
+ "_nextPointRangeInRange:didFindPeriod:"
+ "_nextSearchRange"
+ "_numberOfAccummulatedComponents"
+ "_symbolOfNewBeginnings"
+ "_topLevelDomainSubstring"
+ "aab"
+ "aac"
+ "aam"
+ "aas"
+ "abw"
+ "ac"
+ "acc"
+ "ace"
+ "activatedAccidentally"
+ "acu"
+ "acutc"
+ "adp"
+ "aep"
+ "afm"
+ "afp"
+ "ahead"
+ "ai"
+ "aif"
+ "aifc"
+ "aiff"
+ "air"
+ "ait"
+ "all browsing"
+ "ami"
+ "ams-ui"
+ "apk"
+ "appcache"
+ "apple.news"
+ "application"
+ "apr"
+ "arc"
+ "asc"
+ "asf"
+ "asm"
+ "aso"
+ "asx"
+ "atc"
+ "atom"
+ "atomcat"
+ "atomsvc"
+ "atx"
+ "au"
+ "avi"
+ "aw"
+ "azf"
+ "azs"
+ "azw"
+ "backgrounded"
+ "bat"
+ "bcpio"
+ "bdf"
+ "bdm"
+ "bed"
+ "bh2"
+ "bin"
+ "blb"
+ "blorb"
+ "bmi"
+ "bmp"
+ "book"
+ "box"
+ "boz"
+ "bpk"
+ "bridgingInspiration"
+ "btif"
+ "bz"
+ "bz2"
+ "c11amc"
+ "c11amz"
+ "c4d"
+ "c4f"
+ "c4g"
+ "c4p"
+ "c4u"
+ "cStringUsingEncoding:"
+ "cab"
+ "caf"
+ "cap"
+ "car"
+ "cat"
+ "cb7"
+ "cba"
+ "cbr"
+ "cbt"
+ "cbz"
+ "cc"
+ "cct"
+ "ccxml"
+ "cdbcmsg"
+ "cdf"
+ "cdkey"
+ "cdmia"
+ "cdmic"
+ "cdmid"
+ "cdmio"
+ "cdmiq"
+ "cdx"
+ "cdxml"
+ "cdy"
+ "cer"
+ "cfs"
+ "cgm"
+ "chat"
+ "chm"
+ "chrt"
+ "cif"
+ "cii"
+ "cil"
+ "cla"
+ "clearAccumulatedDomains"
+ "clkk"
+ "clkp"
+ "clkt"
+ "clkw"
+ "clkx"
+ "closed"
+ "clp"
+ "cmc"
+ "cmdf"
+ "cml"
+ "cmp"
+ "cmx"
+ "cod"
+ "com"
+ "com.apple.Safari.DidModifyTab"
+ "com.apple.Safari.Favorites"
+ "com.apple.Safari.NewTabBehavior"
+ "com.apple.Safari.NewWindowBehavior"
+ "com.apple.Safari.Preferences.ReportAdvancedPrivacyProtectionStatus"
+ "com.apple.Safari.TabGroups.Sync.SyncFinished"
+ "com.apple.Safari.VoiceSearchActivatedAccidentally"
+ "conf"
+ "containsEmptyComponents"
+ "cpio"
+ "cpp"
+ "cpt"
+ "crd"
+ "crl"
+ "crt"
+ "cryptonote"
+ "csh"
+ "csml"
+ "csp"
+ "css"
+ "cst"
+ "csv"
+ "cu"
+ "curl"
+ "cww"
+ "cxt"
+ "cxx"
+ "dae"
+ "daf"
+ "dart"
+ "dataless"
+ "davmount"
+ "dbk"
+ "dcr"
+ "dcurl"
+ "dd2"
+ "ddd"
+ "deb"
+ "def"
+ "deploy"
+ "der"
+ "dfac"
+ "dgc"
+ "dic"
+ "didActivateVoiceSearchAccidentally:"
+ "didSelectFavoritesRow:"
+ "dif"
+ "dir"
+ "dis"
+ "disabled"
+ "dist"
+ "distz"
+ "djv"
+ "djvu"
+ "dll"
+ "dmg"
+ "dmp"
+ "dms"
+ "dna"
+ "doc"
+ "docm"
+ "docx"
+ "dot"
+ "dotm"
+ "dotx"
+ "dp"
+ "dpg"
+ "dra"
+ "dsc"
+ "dssc"
+ "dtb"
+ "dtd"
+ "dts"
+ "dtshd"
+ "dump"
+ "dv"
+ "dvb"
+ "dvi"
+ "dwf"
+ "dwg"
+ "dxf"
+ "dxp"
+ "dxr"
+ "ecelp4800"
+ "ecelp7470"
+ "ecelp9600"
+ "ecma"
+ "edm"
+ "edx"
+ "efif"
+ "ei6"
+ "elc"
+ "emf"
+ "eml"
+ "emma"
+ "emz"
+ "enumerateMatchesInString:options:range:usingBlock:"
+ "eol"
+ "eot"
+ "eps"
+ "epub"
+ "es3"
+ "esa"
+ "esf"
+ "et3"
+ "etx"
+ "eva"
+ "evy"
+ "exe"
+ "exi"
+ "ext"
+ "ez"
+ "ez2"
+ "ez3"
+ "f"
+ "f4v"
+ "f77"
+ "f90"
+ "favoritesRow"
+ "fbs"
+ "fcdt"
+ "fcs"
+ "fdf"
+ "fe_launch"
+ "fg5"
+ "fgd"
+ "fh"
+ "fh4"
+ "fh5"
+ "fh7"
+ "fhc"
+ "fig"
+ "findInspiration"
+ "flac"
+ "fli"
+ "flo"
+ "flv"
+ "flw"
+ "flx"
+ "fly"
+ "fm"
+ "fnc"
+ "for"
+ "foregrounded"
+ "fpx"
+ "fragment"
+ "frame"
+ "fsc"
+ "fst"
+ "ftc"
+ "fti"
+ "fvt"
+ "fxp"
+ "fxpl"
+ "fzs"
+ "g2w"
+ "g3"
+ "g3w"
+ "gac"
+ "gam"
+ "gbr"
+ "gca"
+ "gdl"
+ "geo"
+ "gex"
+ "ggb"
+ "ggt"
+ "ghf"
+ "gif"
+ "gim"
+ "gml"
+ "gmx"
+ "gnumeric"
+ "gph"
+ "gpx"
+ "gqf"
+ "gqs"
+ "gram"
+ "gramps"
+ "gre"
+ "grv"
+ "grxml"
+ "gsf"
+ "gtar"
+ "gtm"
+ "gtw"
+ "gv"
+ "gxf"
+ "gxt"
+ "h"
+ "h261"
+ "h263"
+ "h264"
+ "hal"
+ "hbci"
+ "hdf"
+ "hh"
+ "hlp"
+ "hpgl"
+ "hpid"
+ "hps"
+ "hqx"
+ "htke"
+ "htm"
+ "html"
+ "hvd"
+ "hvp"
+ "hvs"
+ "i2g"
+ "iCloudKeychainEnabledOverride"
+ "icc"
+ "ice"
+ "icm"
+ "ico"
+ "ics"
+ "ief"
+ "ifb"
+ "ifm"
+ "iges"
+ "igl"
+ "igm"
+ "igs"
+ "igx"
+ "iif"
+ "imp"
+ "ims"
+ "in"
+ "initWithHost:options:"
+ "ink"
+ "inkml"
+ "inserted"
+ "install"
+ "iota"
+ "ipfix"
+ "ipk"
+ "ipv4Address"
+ "ipv6Address"
+ "irm"
+ "irp"
+ "isSearchEvaluationLoggingEnabled"
+ "isSpeculative"
+ "iso"
+ "itp"
+ "ivp"
+ "ivu"
+ "jad"
+ "jam"
+ "jar"
+ "java"
+ "jisp"
+ "jlt"
+ "jnlp"
+ "joda"
+ "jp2"
+ "jpe"
+ "jpeg"
+ "jpg"
+ "jpgm"
+ "jpgv"
+ "jpm"
+ "js"
+ "json"
+ "jsonml"
+ "kar"
+ "karbon"
+ "kfo"
+ "kia"
+ "kind"
+ "kml"
+ "kmz"
+ "kne"
+ "knp"
+ "kon"
+ "kpr"
+ "kpt"
+ "kpxx"
+ "ksp"
+ "ktr"
+ "ktx"
+ "ktz"
+ "kwd"
+ "kwt"
+ "lasxml"
+ "latex"
+ "lbd"
+ "lbe"
+ "les"
+ "lha"
+ "link66"
+ "list"
+ "list3820"
+ "listafp"
+ "lnk"
+ "log"
+ "lostxml"
+ "lrf"
+ "lrm"
+ "ltf"
+ "lvp"
+ "lwp"
+ "lzh"
+ "m13"
+ "m14"
+ "m1v"
+ "m21"
+ "m2a"
+ "m2v"
+ "m3a"
+ "m3u"
+ "m3u8"
+ "m4a"
+ "m4p"
+ "m4u"
+ "m4v"
+ "ma"
+ "mac"
+ "mads"
+ "mag"
+ "maker"
+ "man"
+ "manifest"
+ "mar"
+ "mathml"
+ "mb"
+ "mbk"
+ "mbox"
+ "mc1"
+ "mcd"
+ "mcurl"
+ "mdb"
+ "mdi"
+ "me"
+ "mesh"
+ "meta4"
+ "metalink"
+ "mets"
+ "mfm"
+ "mft"
+ "mgp"
+ "mgz"
+ "mid"
+ "midi"
+ "mie"
+ "mif"
+ "mime"
+ "mj2"
+ "mjp2"
+ "mk3d"
+ "mka"
+ "mks"
+ "mkv"
+ "mlp"
+ "mmd"
+ "mmf"
+ "mmr"
+ "mng"
+ "mny"
+ "mobi"
+ "mobipocket-ebook"
+ "mods"
+ "mov"
+ "move"
+ "movie"
+ "mp2"
+ "mp21"
+ "mp2a"
+ "mp3"
+ "mp4"
+ "mp4a"
+ "mp4s"
+ "mp4v"
+ "mpc"
+ "mpe"
+ "mpeg"
+ "mpg"
+ "mpg4"
+ "mpga"
+ "mpkg"
+ "mpm"
+ "mpn"
+ "mpp"
+ "mpt"
+ "mpy"
+ "mqy"
+ "mrc"
+ "mrcx"
+ "mscml"
+ "mseed"
+ "mseq"
+ "msf"
+ "msh"
+ "msi"
+ "msl"
+ "msty"
+ "mts"
+ "mus"
+ "musicxml"
+ "mvb"
+ "mwf"
+ "mxf"
+ "mxl"
+ "mxml"
+ "mxs"
+ "mxu"
+ "n-gage"
+ "n3"
+ "navigation"
+ "nb"
+ "nbp"
+ "nc"
+ "ncx"
+ "newTabBehavior"
+ "newWindowBehavior"
+ "nfo"
+ "ngdat"
+ "nitf"
+ "nlu"
+ "nml"
+ "nnd"
+ "nns"
+ "nnw"
+ "npx"
+ "nsc"
+ "nsf"
+ "ntf"
+ "numberOfSavedAccountsInPersonalKeychainForHighLevelDomain:"
+ "nzb"
+ "oa2"
+ "oa3"
+ "oas"
+ "obd"
+ "obj"
+ "oda"
+ "odb"
+ "odc"
+ "odf"
+ "odft"
+ "odg"
+ "odi"
+ "odm"
+ "odp"
+ "ods"
+ "odt"
+ "oga"
+ "ogg"
+ "ogv"
+ "ogx"
+ "omdoc"
+ "one.apple.com"
+ "onepkg"
+ "onetmp"
+ "onetoc"
+ "onetoc2"
+ "opf"
+ "opml"
+ "oprc"
+ "org"
+ "osf"
+ "osfpvg"
+ "otc"
+ "otf"
+ "otg"
+ "oth"
+ "other change"
+ "oti"
+ "otp"
+ "otpauth-migration"
+ "ots"
+ "ott"
+ "oxps"
+ "oxt"
+ "p"
+ "p10"
+ "p12"
+ "p7b"
+ "p7c"
+ "p7m"
+ "p7r"
+ "p7s"
+ "p8"
+ "pas"
+ "pathComponents"
+ "pathExtension"
+ "paw"
+ "pbd"
+ "pbm"
+ "pcap"
+ "pcf"
+ "pcl"
+ "pclxl"
+ "pct"
+ "pcurl"
+ "pcx"
+ "pdb"
+ "pdf"
+ "periodicCount"
+ "pfa"
+ "pfb"
+ "pfm"
+ "pfr"
+ "pfx"
+ "pgm"
+ "pgn"
+ "pgp"
+ "pic"
+ "pict"
+ "pipEvent"
+ "pkg"
+ "pki"
+ "pkipath"
+ "plb"
+ "plc"
+ "plf"
+ "pls"
+ "pml"
+ "png"
+ "pnm"
+ "pnt"
+ "pntg"
+ "portpkg"
+ "pot"
+ "potm"
+ "potx"
+ "ppam"
+ "ppd"
+ "ppm"
+ "pps"
+ "ppsm"
+ "ppsx"
+ "ppt"
+ "pptm"
+ "pptx"
+ "pqa"
+ "prc"
+ "pre"
+ "preference"
+ "prf"
+ "private browsing only"
+ "ps"
+ "psb"
+ "psd"
+ "psf"
+ "pskcxml"
+ "ptid"
+ "pub"
+ "pvb"
+ "pwn"
+ "pya"
+ "pyv"
+ "qam"
+ "qbo"
+ "qfx"
+ "qps"
+ "qt"
+ "qti"
+ "qtif"
+ "qwd"
+ "qwt"
+ "qxb"
+ "qxd"
+ "qxl"
+ "qxt"
+ "ra"
+ "ram"
+ "rar"
+ "ras"
+ "rcprofile"
+ "rdf"
+ "rdz"
+ "reader activated"
+ "reader deactivated"
+ "reader scrolled"
+ "rep"
+ "reportAdvancedPrivacyProtectionPreference"
+ "reportNewTabBehavior:"
+ "reportNewWindowBehavior:"
+ "reportTabGroupSyncFinishedWithInfo:"
+ "reportTabGroupSyncSuccessesWithCount:"
+ "reportTabUpdatedWithUpdateType:"
+ "res"
+ "rgb"
+ "rif"
+ "rip"
+ "ris"
+ "rl"
+ "rlc"
+ "rld"
+ "rm"
+ "rmi"
+ "rmp"
+ "rms"
+ "rmvb"
+ "rnc"
+ "roa"
+ "roff"
+ "rp9"
+ "rpss"
+ "rpst"
+ "rq"
+ "rs"
+ "rsd"
+ "rss"
+ "rtf"
+ "rtx"
+ "s3m"
+ "saf"
+ "safari_absoluteStringWithoutFragment"
+ "safari_accessingSecurityScopedResource:"
+ "safari_canonicalApplicationDefaults"
+ "safari_caseAndDiacriticInsensitiveStandardRangeOfString:additionalOptions:"
+ "safari_filenameFormattedString"
+ "safari_hasScheme:"
+ "safari_highLevelDomainFromHostFallingBackToHostOrAbsoluteString"
+ "safari_hostCompare:"
+ "safari_hostComponentsEnumerator"
+ "safari_hostDomainsEnumerator"
+ "safari_isAppleNewsURL"
+ "safari_isAppleOneURL"
+ "safari_isXWebSearchURL"
+ "safari_matchesErrorDomain:"
+ "safari_setDefaultOTPAuthMigrationURLHandlerToApplicationWithBundleIdentifier:completionHandler:"
+ "safari_setDefaultOTPAuthMigrationURLHandlerToApplicationWithBundleIdentifier:shouldFallBackToSystemHandlerIfNeeded:completionHandler:"
+ "safari_setDefaultOTPAuthURLHandlerToApplicationWithBundleIdentifier:completionHandler:"
+ "safari_setDefaultOTPAuthURLHandlerToApplicationWithBundleIdentifier:shouldFallBackToSystemHandlerIfNeeded:completionHandler:"
+ "safari_setDefaultURLHandlerForScheme:toApplicationWithBundleIdentifier:completionHandler:"
+ "safari_stringByRemovingTopLevelDomainFromHost"
+ "safari_topLevelDomain"
+ "sbml"
+ "sc"
+ "scd"
+ "scm"
+ "scq"
+ "scs"
+ "scurl"
+ "sda"
+ "sdc"
+ "sdd"
+ "sdkd"
+ "sdkm"
+ "sdp"
+ "sdw"
+ "see"
+ "seed"
+ "selected"
+ "sema"
+ "semd"
+ "semf"
+ "ser"
+ "setDefaultURLHandlerForScheme:to:completion:"
+ "setpay"
+ "setreg"
+ "sfd-hdstx"
+ "sfs"
+ "sfv"
+ "sgi"
+ "sgl"
+ "sgm"
+ "sgml"
+ "sh"
+ "shar"
+ "shf"
+ "sid"
+ "sig"
+ "sil"
+ "silo"
+ "sis"
+ "sisx"
+ "sit"
+ "sitx"
+ "skd"
+ "skm"
+ "skp"
+ "skt"
+ "sldm"
+ "sldx"
+ "slt"
+ "sm"
+ "smf"
+ "smi"
+ "smil"
+ "smv"
+ "smzip"
+ "snd"
+ "snf"
+ "so"
+ "spc"
+ "spf"
+ "spl"
+ "spot"
+ "spp"
+ "spq"
+ "spx"
+ "sql"
+ "src"
+ "srt"
+ "sru"
+ "srx"
+ "ssdl"
+ "sse"
+ "ssf"
+ "ssml"
+ "st"
+ "startAccessingSecurityScopedResource"
+ "stc"
+ "std"
+ "stf"
+ "sti"
+ "stk"
+ "stl"
+ "stopAccessingSecurityScopedResource"
+ "str"
+ "stw"
+ "sub"
+ "sus"
+ "susp"
+ "sv4cpio"
+ "sv4crc"
+ "svc"
+ "svd"
+ "svg"
+ "svgz"
+ "swa"
+ "swf"
+ "swi"
+ "sxc"
+ "sxd"
+ "sxg"
+ "sxi"
+ "sxm"
+ "sxw"
+ "t3"
+ "tabUpdateChangeType"
+ "taglet"
+ "tao"
+ "tar"
+ "tcap"
+ "tcl"
+ "teacher"
+ "tei"
+ "teicorpus"
+ "tex"
+ "texi"
+ "texinfo"
+ "text"
+ "tfi"
+ "tfm"
+ "tga"
+ "thmx"
+ "tif"
+ "tiff"
+ "title changed"
+ "tmo"
+ "torrent"
+ "tpl"
+ "tpt"
+ "tr"
+ "tra"
+ "trm"
+ "ts"
+ "tsd"
+ "tsv"
+ "ttc"
+ "ttf"
+ "ttl"
+ "twd"
+ "twds"
+ "txd"
+ "txf"
+ "txt"
+ "u32"
+ "udeb"
+ "ufd"
+ "ufdl"
+ "ulx"
+ "umj"
+ "unityweb"
+ "uoml"
+ "updateAllSavedAccountsWithPasswordsWithUser:protectionSpace:withNewPassword:"
+ "uri"
+ "uris"
+ "url changed"
+ "urls"
+ "useSTPPasskeyDaemon"
+ "ustar"
+ "utz"
+ "uu"
+ "uva"
+ "uvd"
+ "uvf"
+ "uvg"
+ "uvh"
+ "uvi"
+ "uvm"
+ "uvp"
+ "uvs"
+ "uvt"
+ "uvu"
+ "uvv"
+ "uvva"
+ "uvvd"
+ "uvvf"
+ "uvvg"
+ "uvvh"
+ "uvvi"
+ "uvvm"
+ "uvvp"
+ "uvvs"
+ "uvvt"
+ "uvvu"
+ "uvvv"
+ "uvvx"
+ "uvvz"
+ "uvx"
+ "uvz"
+ "v32@?0@\"NSTextCheckingResult\"8Q16^B24"
+ "vcard"
+ "vcd"
+ "vcf"
+ "vcg"
+ "vcs"
+ "vcx"
+ "vis"
+ "viv"
+ "vob"
+ "vor"
+ "vox"
+ "vrml"
+ "vsd"
+ "vsf"
+ "vss"
+ "vst"
+ "vsw"
+ "vtu"
+ "vxml"
+ "w3d"
+ "wad"
+ "wav"
+ "wax"
+ "wbmp"
+ "wbs"
+ "wbxml"
+ "wcm"
+ "wdb"
+ "wdp"
+ "weba"
+ "webm"
+ "webp"
+ "wg"
+ "wgt"
+ "wks"
+ "wm"
+ "wma"
+ "wmd"
+ "wmf"
+ "wml"
+ "wmlc"
+ "wmls"
+ "wmlsc"
+ "wmv"
+ "wmx"
+ "wmz"
+ "woff"
+ "wpd"
+ "wpl"
+ "wps"
+ "wqd"
+ "wri"
+ "wrl"
+ "wsdl"
+ "wspolicy"
+ "wtb"
+ "wvx"
+ "x-web-search"
+ "x32"
+ "x3d"
+ "x3db"
+ "x3dbz"
+ "x3dv"
+ "x3dvz"
+ "x3dz"
+ "xaml"
+ "xap"
+ "xar"
+ "xbap"
+ "xbd"
+ "xbm"
+ "xdf"
+ "xdm"
+ "xdp"
+ "xdssc"
+ "xdw"
+ "xenc"
+ "xer"
+ "xfdf"
+ "xfdl"
+ "xht"
+ "xhtml"
+ "xhvml"
+ "xif"
+ "xla"
+ "xlam"
+ "xlc"
+ "xlf"
+ "xlm"
+ "xls"
+ "xlsb"
+ "xlsm"
+ "xlsx"
+ "xlt"
+ "xltm"
+ "xltx"
+ "xlw"
+ "xm"
+ "xml"
+ "xo"
+ "xop"
+ "xpi"
+ "xpl"
+ "xpm"
+ "xpr"
+ "xps"
+ "xpw"
+ "xpx"
+ "xsl"
+ "xslt"
+ "xsm"
+ "xspf"
+ "xul"
+ "xvm"
+ "xvml"
+ "xwd"
+ "xyz"
+ "xz"
+ "yang"
+ "yin"
+ "yyyy.MM.dd_HH-mm-ssZZZ"
+ "z1"
+ "z2"
+ "z3"
+ "z4"
+ "z5"
+ "z6"
+ "z7"
+ "z8"
+ "zaz"
+ "zip"
+ "zir"
+ "zirz"
+ "zmm"
+ "{_NSRange=QQ}32@0:8@16Q24"
+ "{_NSRange=QQ}40@0:8{_NSRange=QQ}16^B32"
+ "{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}"
+ "{in6_addr=(?=[16C][8S][4I])}16@0:8"
- "%s: Loaded %lu keychain records"
- "(log.{0,2}(in|on|out))|(sign.{0,2}(in|on|up|out))|auth|account|federate"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__tree"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__utility/exception_guard.h"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/vector"
- "New codes will be generated when they expire."
- "These codes will be valid for the next %zu second."
- "These codes will be valid for the next %zu seconds."
- "_labelsOfDomainWithoutWWWOrMSubdomains:"
- "countdownStringForMultipleCodesWithSecondsRemaining:"
- "numberOfSavedAccountsForHighLevelDomain:"
- "safari_highLevelDomainFromHostComponents:"
- "safari_reverseEnumerateComponents:usingBlock:"
- "safari_topLevelDomainUsingCFFromComponents:"
- "stringWithCapacity:"

```
