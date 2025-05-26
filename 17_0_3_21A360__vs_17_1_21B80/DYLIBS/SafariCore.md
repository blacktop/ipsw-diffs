## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`

```diff

-616.1.27.10.16
-  __TEXT.__text: 0x96bd0
-  __TEXT.__auth_stubs: 0x1270
-  __TEXT.__objc_methlist: 0x77ec
-  __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0xa1ff
-  __TEXT.__gcc_except_tab: 0x38d8
-  __TEXT.__oslogstring: 0x760a
+616.2.9.10.10
+  __TEXT.__text: 0x987e4
+  __TEXT.__auth_stubs: 0x12b0
+  __TEXT.__objc_methlist: 0x78b4
+  __TEXT.__const: 0x1e8
+  __TEXT.__cstring: 0xa4bc
+  __TEXT.__gcc_except_tab: 0x3938
+  __TEXT.__oslogstring: 0x77c8
   __TEXT.__ustring: 0x16c4
-  __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x35d0
+  __TEXT.__dlopen_cstrs: 0xf3
+  __TEXT.__unwind_info: 0x3664
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x1289
-  __TEXT.__objc_methname: 0x19e95
-  __TEXT.__objc_methtype: 0x2c39
-  __TEXT.__objc_stubs: 0xd720
+  __TEXT.__objc_classname: 0x12ab
+  __TEXT.__objc_methname: 0x1a153
+  __TEXT.__objc_methtype: 0x2c96
+  __TEXT.__objc_stubs: 0xd8a0
   __DATA_CONST.__got: 0x318
-  __DATA_CONST.__const: 0x3b48
-  __DATA_CONST.__objc_classlist: 0x428
+  __DATA_CONST.__const: 0x3bf8
+  __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_catlist: 0x130
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa190
-  __DATA_CONST.__objc_selrefs: 0x4d60
+  __DATA_CONST.__objc_const: 0xa298
+  __DATA_CONST.__objc_selrefs: 0x4dd8
   __DATA_CONST.__objc_arraydata: 0x6e0
-  __AUTH_CONST.__cfstring: 0xbd60
-  __AUTH_CONST.__objc_const: 0x3998
-  __AUTH_CONST.__const: 0x15e0
+  __AUTH_CONST.__cfstring: 0xbe00
+  __AUTH_CONST.__objc_const: 0x3a28
+  __AUTH_CONST.__const: 0x1640
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x468
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x950
-  __AUTH.__objc_data: 0x1720
+  __AUTH_CONST.__auth_got: 0x970
+  __AUTH.__objc_data: 0x1770
   __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x568
-  __DATA.__objc_superrefs: 0x340
-  __DATA.__objc_ivar: 0x7c4
+  __DATA.__objc_classrefs: 0x570
+  __DATA.__objc_superrefs: 0x348
+  __DATA.__objc_ivar: 0x7d4
   __DATA.__data: 0x978
-  __DATA.__bss: 0x3a8
+  __DATA.__bss: 0x3f8
   __DATA_DIRTY.__objc_data: 0x1270
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x398

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/URLFormatting.framework/URLFormatting
+  - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3769
-  Symbols:   12672
-  CStrings:  5994
+  Functions: 3816
+  Symbols:   12818
+  CStrings:  6043
 
Symbols:
+ +[WBSFeatureAvailability shouldShowInternalUI]
+ +[WBSPrimaryAppleAccountObserver sharedObserver]
+ -[NSFileManager(SafariNSFileManagerExtras) safari_canonicalSettingsDirectoryURL]
+ -[NSURLCredentialStorage(SafariCoreExtras) _safari_copyPersonalSidecar:fromGroupWithID:toGroupWithID:fromRecentlyDeleted:]
+ -[NSURLCredentialStorage(SafariCoreExtras) _safari_copyPersonalSidecar:fromGroupWithID:toGroupWithID:fromRecentlyDeleted:].cold.1
+ -[NSURLCredentialStorage(SafariCoreExtras) _safari_copyPersonalSidecarFromPersonalKeychainToSharedPersonalAccessGroup:forGroupWithID:fromRecentlyDeleted:]
+ -[NSURLCredentialStorage(SafariCoreExtras) _safari_copyPersonalSidecarFromPersonalKeychainToSharedPersonalAccessGroup:forGroupWithID:fromRecentlyDeleted:].cold.1
+ -[NSURLCredentialStorage(SafariCoreExtras) _safari_copyPersonalSidecarFromSharedPersonalAccessGroupToPersonalKeychain:fromRecentlyDeleted:]
+ -[NSURLCredentialStorage(SafariCoreExtras) _safari_copyPersonalSidecarFromSharedPersonalAccessGroupToPersonalKeychain:withNewUsername:fromRecentlyDeleted:]
+ -[NSURLCredentialStorage(SafariCoreExtras) _safari_copyPersonalSidecarFromSharedPersonalAccessGroupToPersonalKeychain:withNewUsername:fromRecentlyDeleted:].cold.1
+ -[NSURLCredentialStorage(SafariCoreExtras) _safari_copySharedSidecar:fromGroupWithID:toGroupWithID:fromRecentlyDeleted:]
+ -[NSURLCredentialStorage(SafariCoreExtras) _safari_copySharedSidecar:fromGroupWithID:toGroupWithID:fromRecentlyDeleted:].cold.1
+ -[NSURLCredentialStorage(SafariCoreExtras) _safari_copySharedSidecar:fromGroupWithID:toGroupWithID:fromRecentlyDeleted:].cold.2
+ -[WBSAuthenticationServicesAgentProxy getIsPasskeyAssertionRequestRunningForWebFrameIdentifier:orApplicationIdentifier:completionHandler:]
+ -[WBSKeychainSyncingMonitor _primaryAppleAccountDidChange]
+ -[WBSKeychainSyncingMonitor canKeychainSyncBeEnabled]
+ -[WBSKeychainSyncingMonitor isKeychainSyncEnabled]
+ -[WBSKeychainSyncingMonitor performTaskOnceKeychainSyncValueHasBeenFetchedOnQueue:task:]
+ -[WBSOngoingSharingGroupProvider hasLoadedGroups]
+ -[WBSPrimaryAppleAccountObserver .cxx_destruct]
+ -[WBSPrimaryAppleAccountObserver _registerForUpdates]
+ -[WBSPrimaryAppleAccountObserver _registerForUpdates].cold.1
+ -[WBSPrimaryAppleAccountObserver _registerForUpdates].cold.2
+ -[WBSPrimaryAppleAccountObserver _registerForUpdates].cold.3
+ -[WBSPrimaryAppleAccountObserver _registerForUpdates].cold.4
+ -[WBSPrimaryAppleAccountObserver _setAccountIfPrimary:]
+ -[WBSPrimaryAppleAccountObserver _setAccountOnInternalQueue:]
+ -[WBSPrimaryAppleAccountObserver accountWasAdded:]
+ -[WBSPrimaryAppleAccountObserver accountWasModified:]
+ -[WBSPrimaryAppleAccountObserver accountWasRemoved:]
+ -[WBSPrimaryAppleAccountObserver getPrimaryAppleAccountAltDSIDWithCompletionHandler:]
+ -[WBSPrimaryAppleAccountObserver getPrimaryAppleAccountHasSafariSyncEnabledWithCompletionHandler:]
+ -[WBSPrimaryAppleAccountObserver getPrimaryAppleAccountWithCompletionHandler:]
+ -[WBSPrimaryAppleAccountObserver init]
+ -[WBSPrimaryAppleAccountObserver isCurrentAppleIDManaged]
+ -[WBSPrimaryAppleAccountObserver isUsingICloud]
+ GCC_except_table276
+ GCC_except_table281
+ GCC_except_table33
+ _AccountsLibrary
+ _AccountsLibrary.cold.1
+ _AccountsLibraryCore
+ _AccountsLibraryCore.frameworkLibrary
+ _AppleAccountLibraryCore
+ _AppleAccountLibraryCore.frameworkLibrary
+ _MCFeatureCloudKeychainSyncAllowed
+ _OBJC_CLASS_$_UMUserManager
+ _OBJC_CLASS_$_WBSPrimaryAppleAccountObserver
+ _OBJC_IVAR_$_WBSKeychainSyncingMonitor._keychainStatusFetchingQueue
+ _OBJC_IVAR_$_WBSKeychainSyncingMonitor._primaryAppleAccount
+ _OBJC_IVAR_$_WBSKeychainSyncingMonitor._synchronousGetterQueue
+ _OBJC_IVAR_$_WBSPrimaryAppleAccountObserver._accountStore
+ _OBJC_IVAR_$_WBSPrimaryAppleAccountObserver._primaryAppleAccount
+ _OBJC_IVAR_$_WBSPrimaryAppleAccountObserver._primaryAppleAccountAltDSID
+ _OBJC_IVAR_$_WBSPrimaryAppleAccountObserver._queue
+ _OBJC_METACLASS_$_WBSPrimaryAppleAccountObserver
+ _WBSPrimaryAppleAccountDidChangeNotification
+ _WBS_LOG_CHANNEL_PREFIXAppleAccount
+ _WBS_LOG_CHANNEL_PREFIXAppleAccount.log
+ _WBS_LOG_CHANNEL_PREFIXAppleAccount.onceToken
+ __OBJC_$_CLASS_METHODS_WBSPrimaryAppleAccountObserver
+ __OBJC_$_CLASS_PROP_LIST_WBSPrimaryAppleAccountObserver
+ __OBJC_$_INSTANCE_METHODS_WBSPrimaryAppleAccountObserver
+ __OBJC_$_INSTANCE_VARIABLES_WBSPrimaryAppleAccountObserver
+ __OBJC_$_PROP_LIST_WBSPrimaryAppleAccountObserver
+ __OBJC_CLASS_PROTOCOLS_$_WBSPrimaryAppleAccountObserver
+ __OBJC_CLASS_RO_$_WBSPrimaryAppleAccountObserver
+ __OBJC_METACLASS_RO_$_WBSPrimaryAppleAccountObserver
+ ___100-[WBSSavedAccountStore canSaveUser:password:forProtectionSpace:highLevelDomain:notes:groupID:error:]_block_invoke.199
+ ___110-[WBSAuthenticationServicesAgentProxy getPasskeysForRunningAssertionWithWebFrameIdentifier:completionHandler:]_block_invoke.47
+ ___117-[WBSAuthenticationServicesAgentProxy getPasskeysForRunningAssertionWithApplicationIdentifier:withCompletionHandler:]_block_invoke.45
+ ___126-[WBSSavedAccountStore _cleanUpSharedSavedAccountsWithUnknownOriginalContributorParticipantIDsIfNecessaryFromRecentlyDeleted:]_block_invoke.222
+ ___128-[WBSAuthenticationServicesAgentProxy userSelectedAutoFillPasskey:authenticatedLAContext:savedAccountContext:completionHandler:]_block_invoke.48
+ ___138-[WBSAuthenticationServicesAgentProxy getIsPasskeyAssertionRequestRunningForWebFrameIdentifier:orApplicationIdentifier:completionHandler:]_block_invoke
+ ___138-[WBSAuthenticationServicesAgentProxy getIsPasskeyAssertionRequestRunningForWebFrameIdentifier:orApplicationIdentifier:completionHandler:]_block_invoke.cold.1
+ ___145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke.244
+ ___145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke_2.245
+ ___147-[WBSSavedAccountStore _getSavedAccountMatchesFromSavedAccountTreeMatchesOnInternalQueue:withCriteria:mergingAutoFillPasskeys:nearbyDeviceOptions:]_block_invoke.288
+ ___38-[WBSOngoingSharingGroupProvider init]_block_invoke.19
+ ___38-[WBSPrimaryAppleAccountObserver init]_block_invoke
+ ___47-[WBSPrimaryAppleAccountObserver isUsingICloud]_block_invoke
+ ___48+[WBSPrimaryAppleAccountObserver sharedObserver]_block_invoke
+ ___49-[WBSOngoingSharingGroupProvider hasLoadedGroups]_block_invoke
+ ___50-[WBSKeychainSyncingMonitor isKeychainSyncEnabled]_block_invoke
+ ___52-[WBSPrimaryAppleAccountObserver accountWasRemoved:]_block_invoke
+ ___54-[WBSSavedAccountStore changeSavedAccountWithRequest:]_block_invoke.188
+ ___55-[WBSPrimaryAppleAccountObserver _setAccountIfPrimary:]_block_invoke
+ ___56-[WBSKeychainSyncingMonitor _fetchKeychainSyncingStatus]_block_invoke.8
+ ___56-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:]_block_invoke.230
+ ___56-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:]_block_invoke.230.cold.1
+ ___57-[WBSPrimaryAppleAccountObserver isCurrentAppleIDManaged]_block_invoke
+ ___58-[WBSKeychainSyncingMonitor _primaryAppleAccountDidChange]_block_invoke
+ ___58-[WBSKeychainSyncingMonitor _primaryAppleAccountDidChange]_block_invoke_2
+ ___61-[WBSOngoingSharingGroupProvider _fetchGroupsWithCompletion:]_block_invoke.33
+ ___61-[WBSOngoingSharingGroupProvider _fetchGroupsWithCompletion:]_block_invoke.34
+ ___61-[WBSOngoingSharingGroupProvider _fetchGroupsWithCompletion:]_block_invoke_2.38
+ ___61-[WBSOngoingSharingGroupProvider _fetchGroupsWithCompletion:]_block_invoke_3.41
+ ___66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.252
+ ___78-[WBSPrimaryAppleAccountObserver getPrimaryAppleAccountWithCompletionHandler:]_block_invoke
+ ___79-[WBSOngoingSharingGroupProvider _fetchCurrentUserParticipantIDWithCompletion:]_block_invoke.26
+ ___79-[WBSOngoingSharingGroupProvider _fetchCurrentUserParticipantIDWithCompletion:]_block_invoke.26.cold.1
+ ___79-[WBSOngoingSharingGroupProvider _fetchCurrentUserParticipantIDWithCompletion:]_block_invoke.27
+ ___85-[WBSPrimaryAppleAccountObserver getPrimaryAppleAccountAltDSIDWithCompletionHandler:]_block_invoke
+ ___86-[WBSSavedAccountStore _ensureNoRecentlyDeletedSavedAccountsConflictWithSavedAccount:]_block_invoke.265
+ ___86-[WBSSavedAccountStore _moveContributedSavedAccountsBackToPersonalKeychainIfNecessary]_block_invoke.251
+ ___88-[WBSKeychainSyncingMonitor performTaskOnceKeychainSyncValueHasBeenFetchedOnQueue:task:]_block_invoke
+ ___98-[WBSPrimaryAppleAccountObserver getPrimaryAppleAccountHasSafariSyncEnabledWithCompletionHandler:]_block_invoke
+ ___98-[WBSPrimaryAppleAccountObserver getPrimaryAppleAccountHasSafariSyncEnabledWithCompletionHandler:]_block_invoke.cold.1
+ ___AccountsLibraryCore_block_invoke
+ ___AppleAccountLibraryCore_block_invoke
+ ___WBS_LOG_CHANNEL_PREFIXAppleAccount_block_invoke
+ ___block_descriptor_40_e8_32s_e19_v16?0"ACAccount"8ls32l8
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e49_v32?0q8"<WBSSavedAccountSidecarInternal>"16^B24lr56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e49_v32?0q8"<WBSSavedAccountSidecarInternal>"16^B24ls32l8r64l8s40l8s48l8s56l8
+ ___block_literal_global.170
+ ___block_literal_global.177
+ ___block_literal_global.183
+ ___block_literal_global.208
+ ___block_literal_global.213
+ ___block_literal_global.237
+ ___block_literal_global.239
+ ___block_literal_global.247
+ ___block_literal_global.255
+ ___block_literal_global.263
+ ___block_literal_global.283
+ ___block_literal_global.298
+ ___block_literal_global.45
+ ___block_literal_global.47
+ ___block_literal_global.49
+ ___block_literal_global.616
+ ___block_literal_global.64
+ ___block_literal_global.66
+ ___block_literal_global.687
+ ___getAAAccountClassPrimarySymbolLoc_block_invoke
+ ___getAAAccountClassPrimarySymbolLoc_block_invoke.cold.1
+ ___getACAccountDataclassBookmarksSymbolLoc_block_invoke
+ ___getACAccountTypeIdentifierAppleAccountSymbolLoc_block_invoke
+ ___getACMonitoredAccountStoreClass_block_invoke
+ ___getACMonitoredAccountStoreClass_block_invoke.cold.1
+ _audit_stringAccounts
+ _audit_stringAppleAccount
+ _dispatch_activate
+ _dispatch_assert_queue$V2
+ _dispatch_queue_attr_make_initially_inactive
+ _getAAAccountClassPrimary
+ _getAAAccountClassPrimary.cold.1
+ _getAAAccountClassPrimarySymbolLoc.ptr
+ _getACAccountDataclassBookmarksSymbolLoc.ptr
+ _getACAccountTypeIdentifierAppleAccountSymbolLoc.ptr
+ _getACMonitoredAccountStoreClass.softClass
+ _objc_getClass
+ _objc_msgSend$_primaryAppleAccountDidChange
+ _objc_msgSend$_registerForUpdates
+ _objc_msgSend$_safari_copyPersonalSidecar:fromGroupWithID:toGroupWithID:fromRecentlyDeleted:
+ _objc_msgSend$_safari_copyPersonalSidecarFromPersonalKeychainToSharedPersonalAccessGroup:forGroupWithID:fromRecentlyDeleted:
+ _objc_msgSend$_safari_copyPersonalSidecarFromSharedPersonalAccessGroupToPersonalKeychain:fromRecentlyDeleted:
+ _objc_msgSend$_safari_copyPersonalSidecarFromSharedPersonalAccessGroupToPersonalKeychain:withNewUsername:fromRecentlyDeleted:
+ _objc_msgSend$_safari_copySharedSidecar:fromGroupWithID:toGroupWithID:fromRecentlyDeleted:
+ _objc_msgSend$_setAccountIfPrimary:
+ _objc_msgSend$_setAccountOnInternalQueue:
+ _objc_msgSend$aa_isAccountClass:
+ _objc_msgSend$applicationIdentifier
+ _objc_msgSend$boolRestrictionForFeature:
+ _objc_msgSend$getIsPasskeyAssertionRequestRunningForWebFrameIdentifier:orApplicationIdentifier:completionHandler:
+ _objc_msgSend$getPrimaryAppleAccountWithCompletionHandler:
+ _objc_msgSend$isEnabledForDataclass:
+ _objc_msgSend$isSharedIPad
+ _objc_msgSend$isUsingICloud
+ _objc_msgSend$performTaskOnceKeychainSyncValueHasBeenFetchedOnQueue:task:
+ _objc_msgSend$safari_isEarlierThanDate:
+ _objc_msgSend$setSharedGroupName:
+ _objc_msgSend$sharedObserver
+ _sharedObserver.onceToken
+ _sharedObserver.sharedObserver
- -[NSURLCredentialStorage(SafariCoreExtras) _safari_copyPersonalSidecar:fromGroupWithID:toGroupWithID:]
- -[NSURLCredentialStorage(SafariCoreExtras) _safari_copyPersonalSidecar:fromGroupWithID:toGroupWithID:].cold.1
- -[NSURLCredentialStorage(SafariCoreExtras) _safari_copyPersonalSidecarFromPersonalKeychainToSharedPersonalAccessGroup:forGroupWithID:]
- -[NSURLCredentialStorage(SafariCoreExtras) _safari_copyPersonalSidecarFromPersonalKeychainToSharedPersonalAccessGroup:forGroupWithID:].cold.1
- -[NSURLCredentialStorage(SafariCoreExtras) _safari_copyPersonalSidecarFromSharedPersonalAccessGroupToPersonalKeychain:]
- -[NSURLCredentialStorage(SafariCoreExtras) _safari_copyPersonalSidecarFromSharedPersonalAccessGroupToPersonalKeychain:withNewUsername:]
- -[NSURLCredentialStorage(SafariCoreExtras) _safari_copyPersonalSidecarFromSharedPersonalAccessGroupToPersonalKeychain:withNewUsername:].cold.1
- -[NSURLCredentialStorage(SafariCoreExtras) _safari_copySharedSidecar:fromGroupWithID:toGroupWithID:]
- -[NSURLCredentialStorage(SafariCoreExtras) _safari_copySharedSidecar:fromGroupWithID:toGroupWithID:].cold.1
- -[NSURLCredentialStorage(SafariCoreExtras) _safari_copySharedSidecar:fromGroupWithID:toGroupWithID:].cold.2
- -[WBSKeychainSyncingMonitor accountCredentialChanged:]
- -[WBSKeychainSyncingMonitor accountWasAdded:]
- -[WBSKeychainSyncingMonitor accountWasModified:]
- -[WBSKeychainSyncingMonitor accountWasRemoved:]
- -[WBSKeychainSyncingMonitor isCurrentAppleIDManaged]
- -[WBSKeychainSyncingMonitor isUsingiCloud]
- -[WBSSavedAccountStore _performOneTimeMigrationForRadar105843594IfNeeded]
- GCC_except_table214
- GCC_except_table273
- GCC_except_table277
- _ACAccountTypeIdentifierAppleAccount
- _OBJC_CLASS_$_ACMonitoredAccountStore
- _OBJC_IVAR_$_WBSKeychainSyncingMonitor._accountStore
- _OBJC_IVAR_$_WBSKeychainSyncingMonitor._syncStatusFetchingQueue
- _OBJC_IVAR_$_WBSSavedAccountStore._didReportKeychainItemsWithInvalidAuthenticationTypes
- __OBJC_CLASS_PROTOCOLS_$_WBSKeychainSyncingMonitor
- ___100-[WBSSavedAccountStore canSaveUser:password:forProtectionSpace:highLevelDomain:notes:groupID:error:]_block_invoke.197
- ___110-[WBSAuthenticationServicesAgentProxy getPasskeysForRunningAssertionWithWebFrameIdentifier:completionHandler:]_block_invoke.44
- ___117-[WBSAuthenticationServicesAgentProxy getPasskeysForRunningAssertionWithApplicationIdentifier:withCompletionHandler:]_block_invoke.42
- ___126-[WBSSavedAccountStore _cleanUpSharedSavedAccountsWithUnknownOriginalContributorParticipantIDsIfNecessaryFromRecentlyDeleted:]_block_invoke.220
- ___128-[WBSAuthenticationServicesAgentProxy userSelectedAutoFillPasskey:authenticatedLAContext:savedAccountContext:completionHandler:]_block_invoke.45
- ___145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke.248
- ___145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke_2.249
- ___147-[WBSSavedAccountStore _getSavedAccountMatchesFromSavedAccountTreeMatchesOnInternalQueue:withCriteria:mergingAutoFillPasskeys:nearbyDeviceOptions:]_block_invoke.292
- ___33-[WBSKeychainSyncingMonitor init]_block_invoke
- ___38-[WBSOngoingSharingGroupProvider init]_block_invoke.16
- ___45-[WBSKeychainSyncingMonitor accountWasAdded:]_block_invoke
- ___47-[WBSKeychainSyncingMonitor accountWasRemoved:]_block_invoke
- ___48-[WBSKeychainSyncingMonitor accountWasModified:]_block_invoke
- ___54-[WBSKeychainSyncingMonitor accountCredentialChanged:]_block_invoke
- ___54-[WBSSavedAccountStore changeSavedAccountWithRequest:]_block_invoke.186
- ___56-[WBSKeychainSyncingMonitor _fetchKeychainSyncingStatus]_block_invoke.6
- ___56-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:]_block_invoke.234.cold.1
- ___56-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:]_block_invoke.238
- ___61-[WBSOngoingSharingGroupProvider _fetchGroupsWithCompletion:]_block_invoke.29
- ___61-[WBSOngoingSharingGroupProvider _fetchGroupsWithCompletion:]_block_invoke.30
- ___61-[WBSOngoingSharingGroupProvider _fetchGroupsWithCompletion:]_block_invoke_2.34
- ___61-[WBSOngoingSharingGroupProvider _fetchGroupsWithCompletion:]_block_invoke_3.37
- ___66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.260
- ___79-[WBSOngoingSharingGroupProvider _fetchCurrentUserParticipantIDWithCompletion:]_block_invoke.23
- ___79-[WBSOngoingSharingGroupProvider _fetchCurrentUserParticipantIDWithCompletion:]_block_invoke.23.cold.1
- ___79-[WBSOngoingSharingGroupProvider _fetchCurrentUserParticipantIDWithCompletion:]_block_invoke.24
- ___86-[WBSSavedAccountStore _ensureNoRecentlyDeletedSavedAccountsConflictWithSavedAccount:]_block_invoke.269
- ___86-[WBSSavedAccountStore _moveContributedSavedAccountsBackToPersonalKeychainIfNecessary]_block_invoke.255
- ___block_descriptor_48_e8_32s40r_e49_v32?0q8"<WBSSavedAccountSidecarInternal>"16^B24lr40l8s32l8
- ___block_descriptor_64_e8_32s40s48s56r_e49_v32?0q8"<WBSSavedAccountSidecarInternal>"16^B24ls32l8r56l8s40l8s48l8
- ___block_literal_global.167
- ___block_literal_global.171
- ___block_literal_global.180
- ___block_literal_global.206
- ___block_literal_global.209
- ___block_literal_global.219
- ___block_literal_global.241
- ___block_literal_global.243
- ___block_literal_global.251
- ___block_literal_global.259
- ___block_literal_global.267
- ___block_literal_global.287
- ___block_literal_global.302
- ___block_literal_global.33
- ___block_literal_global.42
- ___block_literal_global.54
- ___block_literal_global.621
- ___block_literal_global.692
- _objc_msgSend$_performOneTimeMigrationForRadar105843594IfNeeded
- _objc_msgSend$_safari_copyPersonalSidecar:fromGroupWithID:toGroupWithID:
- _objc_msgSend$_safari_copyPersonalSidecarFromPersonalKeychainToSharedPersonalAccessGroup:forGroupWithID:
- _objc_msgSend$_safari_copyPersonalSidecarFromSharedPersonalAccessGroupToPersonalKeychain:
- _objc_msgSend$_safari_copyPersonalSidecarFromSharedPersonalAccessGroupToPersonalKeychain:withNewUsername:
- _objc_msgSend$_safari_copySharedSidecar:fromGroupWithID:toGroupWithID:
- _objc_msgSend$aa_isUsingiCloud
- _objc_msgSend$isUsingiCloud
- _objc_msgSend$teamIdentifier
CStrings:
+ "\x04\x12"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__tree"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__utility/exception_guard.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/vector"
+ "@\"ACAccount\""
+ "AAAccountClassPrimary"
+ "ACAccountDataclassBookmarks"
+ "ACAccountTypeIdentifierAppleAccount"
+ "ACMonitoredAccountStore"
+ "AppleAccount"
+ "B44@0:8@16@24@32B40"
+ "Class getACMonitoredAccountStoreClass(void)_block_invoke"
+ "Failed to register for account updates: %{public}@"
+ "LastInvalidAuthTypeMigrationDate"
+ "NSString *getAAAccountClassPrimary(void)"
+ "NSString *getACAccountDataclassBookmarks(void)"
+ "NSString *getACAccountTypeIdentifierAppleAccount(void)"
+ "Ongoing credential sharing is disabled because iCloud Keychain state is unknown"
+ "Running in an environment where Accounts.framework is not available. Refusing to connect to account store."
+ "Running in an environment where AppleAccount.framework is not available. Refusing to connect to account store."
+ "Skipping invalid auth type migration because the migration has already run in the past %lu days."
+ "T@\"WBSPrimaryAppleAccountObserver\",R,N"
+ "Unable to find class %s"
+ "WBSKeychainSyncStatusMayHaveChangedNotification"
+ "WBSOngoingSharingGroupProviderErrorDomain"
+ "WBSPrimaryAppleAccountDidChangeNotification"
+ "WBSPrimaryAppleAccountObserver"
+ "WBSPrimaryAppleAccountObserver.m"
+ "_keychainStatusFetchingQueue"
+ "_primaryAppleAccount"
+ "_primaryAppleAccountDidChange"
+ "_registerForUpdates"
+ "_safari_copyPersonalSidecar:fromGroupWithID:toGroupWithID:fromRecentlyDeleted:"
+ "_safari_copyPersonalSidecarFromPersonalKeychainToSharedPersonalAccessGroup:forGroupWithID:fromRecentlyDeleted:"
+ "_safari_copyPersonalSidecarFromSharedPersonalAccessGroupToPersonalKeychain:fromRecentlyDeleted:"
+ "_safari_copyPersonalSidecarFromSharedPersonalAccessGroupToPersonalKeychain:withNewUsername:fromRecentlyDeleted:"
+ "_safari_copySharedSidecar:fromGroupWithID:toGroupWithID:fromRecentlyDeleted:"
+ "_setAccountIfPrimary:"
+ "_setAccountOnInternalQueue:"
+ "_synchronousGetterQueue"
+ "aa_isAccountClass:"
+ "applicationIdentifier"
+ "boolRestrictionForFeature:"
+ "canKeychainSyncBeEnabled"
+ "com.apple.SafariCore.WBSKeychainSyncingMonitor.keychainStatusFetchingQueue"
+ "com.apple.SafariCore.WBSKeychainSyncingMonitor.synchronousGetterQueue"
+ "com.apple.SafariCore.WBSPrimaryAppleAccountObserver"
+ "getIsPasskeyAssertionRequestRunningForWebFrameIdentifier:orApplicationIdentifier:completionHandler:"
+ "getPrimaryAppleAccountAltDSIDWithCompletionHandler:"
+ "getPrimaryAppleAccountHasSafariSyncEnabledWithCompletionHandler:"
+ "getPrimaryAppleAccountWithCompletionHandler:"
+ "hasLoadedGroups"
+ "hideInternalUI"
+ "isEnabledForDataclass:"
+ "isKeychainSyncEnabled"
+ "isSharedIPad"
+ "isUsingICloud"
+ "performTaskOnceKeychainSyncValueHasBeenFetchedOnQueue:task:"
+ "safari_canonicalSettingsDirectoryURL"
+ "shouldShowInternalUI"
+ "softlink:o:path:/System/Library/Frameworks/Accounts.framework/Accounts"
+ "softlink:o:path:/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount"
+ "v16@?0@\"ACAccount\"8"
+ "v40@0:8@\"WBSGlobalFrameIdentifier\"16@\"NSString\"24@?<v@?B>32"
+ "void *AccountsLibrary(void)"
+ "void *AppleAccountLibrary(void)"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__tree"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__utility/exception_guard.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/vector"
- "_didReportKeychainItemsWithInvalidAuthenticationTypes"
- "_performOneTimeMigrationForRadar105843594IfNeeded"
- "_safari_copyPersonalSidecar:fromGroupWithID:toGroupWithID:"
- "_safari_copyPersonalSidecarFromPersonalKeychainToSharedPersonalAccessGroup:forGroupWithID:"
- "_safari_copyPersonalSidecarFromSharedPersonalAccessGroupToPersonalKeychain:"
- "_safari_copyPersonalSidecarFromSharedPersonalAccessGroupToPersonalKeychain:withNewUsername:"
- "_safari_copySharedSidecar:fromGroupWithID:toGroupWithID:"
- "_syncStatusFetchingQueue"
- "aa_isUsingiCloud"
- "com.apple.SafariCore.WBSKeychainSyncingMonitor.fetchingQueue"
- "didPerformOneTimeMigrationForRadar105843594"
- "isUsingiCloud"
- "keychainSyncStatusMayHaveChanged"
- "teamIdentifier"

```
