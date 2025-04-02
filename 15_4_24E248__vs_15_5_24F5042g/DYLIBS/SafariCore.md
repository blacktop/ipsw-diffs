## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/Versions/A/SafariCore`

```diff

-621.1.15.11.10
-  __TEXT.__text: 0x1128d4
+621.2.1.11.5
+  __TEXT.__text: 0x112b1c
   __TEXT.__auth_stubs: 0x2670
-  __TEXT.__objc_methlist: 0xabb4
+  __TEXT.__objc_methlist: 0xabcc
   __TEXT.__const: 0x1688
-  __TEXT.__gcc_except_tab: 0x6894
-  __TEXT.__cstring: 0x10ff5
+  __TEXT.__gcc_except_tab: 0x6858
+  __TEXT.__cstring: 0x11015
   __TEXT.__ustring: 0x2690
-  __TEXT.__oslogstring: 0x9d4a
+  __TEXT.__oslogstring: 0x9d1a
   __TEXT.__dlopen_cstrs: 0x19b
   __TEXT.__swift5_typeref: 0x90b
   __TEXT.__swift5_fieldmd: 0x4a4

   __TEXT.__swift_as_entry: 0x8c
   __TEXT.__swift_as_ret: 0x6c
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x5768
+  __TEXT.__unwind_info: 0x5758
   __TEXT.__eh_frame: 0x1da8
   __TEXT.__objc_classname: 0x1870
-  __TEXT.__objc_methname: 0x21fda
+  __TEXT.__objc_methname: 0x22039
   __TEXT.__objc_methtype: 0x3ba5
-  __TEXT.__objc_stubs: 0x10b00
+  __TEXT.__objc_stubs: 0x10b60
   __DATA_CONST.__got: 0xce8
   __DATA_CONST.__const: 0x2068
   __DATA_CONST.__objc_classlist: 0x568
   __DATA_CONST.__objc_catlist: 0x150
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6498
+  __DATA_CONST.__objc_selrefs: 0x64a8
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x440
   __DATA_CONST.__objc_arraydata: 0x2738
   __AUTH_CONST.__auth_got: 0x1350
-  __AUTH_CONST.__auth_ptr: 0x318
-  __AUTH_CONST.__const: 0x7060
+  __AUTH_CONST.__auth_ptr: 0x310
+  __AUTH_CONST.__const: 0x7090
   __AUTH_CONST.__cfstring: 0x180e0
   __AUTH_CONST.__objc_const: 0x11320
   __AUTH_CONST.__objc_intobj: 0x390

   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 6151
   Symbols:   12574
-  CStrings:  9056
+  CStrings:  9058
 
Symbols:
+ -[WBSGeneratedPasswordStore removeGeneratedPasswordMatchingSavedAccount:]
+ __112-[WBSSavedAccountStore canSaveUser:password:forProtectionSpace:highLevelDomain:notes:customTitle:groupID:error:]_block_invoke.319
+ __126-[WBSSavedAccountStore _cleanUpSharedSavedAccountsWithUnknownOriginalContributorParticipantIDsIfNecessaryFromRecentlyDeleted:]_block_invoke.350
+ __126-[WBSSavedAccountStore _relyingPartyURLForPasskeyCredentialIdentifierOnInternalQueue:credentialIdentifiersToAutoFillPasskeys:]_block_invoke.418
+ __145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke.383
+ __145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke_2.384
+ __147-[WBSSavedAccountStore _getSavedAccountMatchesFromSavedAccountTreeMatchesOnInternalQueue:withCriteria:mergingAutoFillPasskeys:nearbyDeviceOptions:]_block_invoke.447
+ __66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.391
+ __66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.395
+ __69-[WBSSavedAccountStore _performRecentlyDeletedMaintenanceIfNecessary]_block_invoke.366
+ __72-[WBSSavedAccountStore changeSavedAccountWithRequest:completionHandler:]_block_invoke.282
+ __74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.367
+ __74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.367.cold.1
+ __74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.371
+ __86-[WBSSavedAccountStore _ensureNoRecentlyDeletedSavedAccountsConflictWithSavedAccount:]_block_invoke.409
+ __86-[WBSSavedAccountStore _ensureNoRecentlyDeletedSavedAccountsConflictWithSavedAccount:]_block_invoke.413
+ __86-[WBSSavedAccountStore _moveContributedSavedAccountsBackToPersonalKeychainIfNecessary]_block_invoke.390
+ __90-[WBSSavedAccountStore _performLegacySidecarModificationWithChangeRequest:toSavedAccount:]_block_invoke.286
+ ___73-[WBSGeneratedPasswordStore removeGeneratedPasswordMatchingSavedAccount:]_block_invoke
+ ___block_descriptor_40_e8_32s_e30_B16?0"WBSGeneratedPassword"8l
+ __block_literal_global.313
+ __block_literal_global.330
+ __block_literal_global.337
+ __block_literal_global.339
+ __block_literal_global.375
+ __block_literal_global.379
+ __block_literal_global.386
+ __block_literal_global.394
+ __block_literal_global.406
+ __block_literal_global.442
+ __block_literal_global.462
+ __block_literal_global.858
+ __block_literal_global.935
+ __block_literal_global.941
+ _objc_msgSend$generatedPasswordsForProtectionSpace:options:
+ _objc_msgSend$removeGeneratedPassword:completionHandler:
+ _objc_msgSend$removeGeneratedPasswordMatchingSavedAccount:
- __112-[WBSSavedAccountStore canSaveUser:password:forProtectionSpace:highLevelDomain:notes:customTitle:groupID:error:]_block_invoke.318
- __126-[WBSSavedAccountStore _cleanUpSharedSavedAccountsWithUnknownOriginalContributorParticipantIDsIfNecessaryFromRecentlyDeleted:]_block_invoke.349
- __126-[WBSSavedAccountStore _relyingPartyURLForPasskeyCredentialIdentifierOnInternalQueue:credentialIdentifiersToAutoFillPasskeys:]_block_invoke.417
- __145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke.382
- __145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke_2.383
- __147-[WBSSavedAccountStore _getSavedAccountMatchesFromSavedAccountTreeMatchesOnInternalQueue:withCriteria:mergingAutoFillPasskeys:nearbyDeviceOptions:]_block_invoke.446
- __66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.390
- __66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.394
- __69-[WBSSavedAccountStore _performRecentlyDeletedMaintenanceIfNecessary]_block_invoke.365
- __72-[WBSSavedAccountStore changeSavedAccountWithRequest:completionHandler:]_block_invoke.281
- __74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.366
- __74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.366.cold.1
- __74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.370
- __86-[WBSSavedAccountStore _ensureNoRecentlyDeletedSavedAccountsConflictWithSavedAccount:]_block_invoke.408
- __86-[WBSSavedAccountStore _ensureNoRecentlyDeletedSavedAccountsConflictWithSavedAccount:]_block_invoke.412
- __86-[WBSSavedAccountStore _moveContributedSavedAccountsBackToPersonalKeychainIfNecessary]_block_invoke.389
- __90-[WBSSavedAccountStore _performLegacySidecarModificationWithChangeRequest:toSavedAccount:]_block_invoke.285
- __ZN12SafariShared25SuddenTerminationDisablerC1EP8NSStringU13block_pointerFvvE
- __ZN12SafariShared25SuddenTerminationDisablerC2EP8NSStringU13block_pointerFvvE
- ___ZL35temporarilyDisableSuddenTerminationP17WBSSQLiteDatabase_block_invoke.60
- ___ZL35temporarilyDisableSuddenTerminationP17WBSSQLiteDatabase_block_invoke.cold.1
- __block_literal_global.312
- __block_literal_global.329
- __block_literal_global.336
- __block_literal_global.338
- __block_literal_global.348
- __block_literal_global.374
- __block_literal_global.378
- __block_literal_global.385
- __block_literal_global.393
- __block_literal_global.441
- __block_literal_global.461
- __block_literal_global.62
- __block_literal_global.857
- __block_literal_global.934
- __block_literal_global.940
CStrings:
+ "/AppleInternal/Library/BuildRoots/4931fbb8-0af0-11f0-9779-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SafariShared/SafariShared/SafariCore/FoundationExtras/WBSCoreNSBundleExtras.m"
+ "/AppleInternal/Library/BuildRoots/4931fbb8-0af0-11f0-9779-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SafariShared/SafariShared/SafariCore/Preferences/WBSSearchEnginePreferenceObserver.m"
+ "ReadingListItemEntity"
+ "correlateReadingListEntityForItem:withUUIDString:"
+ "removeGeneratedPasswordMatchingSavedAccount:"
- "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SafariShared/SafariShared/SafariCore/FoundationExtras/WBSCoreNSBundleExtras.m"
- "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SafariShared/SafariShared/SafariCore/Preferences/WBSSearchEnginePreferenceObserver.m"
- "Background Task Expired. %@, database URL: %@"

```
