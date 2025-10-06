## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`

```diff

-622.2.5.10.3
-  __TEXT.__text: 0x11b178
+622.2.9.10.3
+  __TEXT.__text: 0x11b464
   __TEXT.__auth_stubs: 0x2ea0
-  __TEXT.__objc_methlist: 0xb62c
-  __TEXT.__const: 0x2a14
-  __TEXT.__gcc_except_tab: 0x66d0
+  __TEXT.__objc_methlist: 0xb63c
+  __TEXT.__const: 0x2a24
+  __TEXT.__gcc_except_tab: 0x66a0
   __TEXT.__cstring: 0x11c35
   __TEXT.__ustring: 0x2810
-  __TEXT.__oslogstring: 0x9edd
+  __TEXT.__oslogstring: 0xa02d
   __TEXT.__dlopen_cstrs: 0x19b
   __TEXT.__swift5_typeref: 0xd42
   __TEXT.__swift5_fieldmd: 0x804

   __TEXT.__unwind_info: 0x6008
   __TEXT.__eh_frame: 0x2d30
   __TEXT.__objc_classname: 0x19d8
-  __TEXT.__objc_methname: 0x23d1d
+  __TEXT.__objc_methname: 0x23def
   __TEXT.__objc_methtype: 0x3db9
   __TEXT.__objc_stubs: 0x11600
   __DATA_CONST.__got: 0xdf8
-  __DATA_CONST.__const: 0x4e40
+  __DATA_CONST.__const: 0x4e70
   __DATA_CONST.__objc_classlist: 0x5d0
   __DATA_CONST.__objc_catlist: 0x168
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6958
+  __DATA_CONST.__objc_selrefs: 0x6968
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x480
   __DATA_CONST.__objc_arraydata: 0x2790
   __AUTH_CONST.__auth_got: 0x1768
   __AUTH_CONST.__const: 0x4c38
   __AUTH_CONST.__cfstring: 0x185a0
-  __AUTH_CONST.__objc_const: 0x12b90
+  __AUTH_CONST.__objc_const: 0x12ba0
   __AUTH_CONST.__objc_intobj: 0x390
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x5a0

   __AUTH.__objc_data: 0x2438
   __AUTH.__data: 0x480
   __DATA.__objc_ivar: 0xbc4
-  __DATA.__data: 0x1678
+  __DATA.__data: 0x1670
   __DATA.__bss: 0x3fb0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1730
-  __DATA_DIRTY.__data: 0x1c8
+  __DATA_DIRTY.__data: 0x1d0
   __DATA_DIRTY.__bss: 0x488
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0E3A8BC5-BAD3-3E63-A6C8-BA45AF0F6651
-  Functions: 6767
-  Symbols:   18562
-  CStrings:  12489
+  UUID: D5E42121-E262-357B-A320-6E8509864154
+  Functions: 6769
+  Symbols:   18567
+  CStrings:  12492
 
Symbols:
+ -[NSURLProtectionSpace(SafariCoreExtras) safari_protectionSpaceBySimplifyingHost]
+ -[WBSSavedAccountStore _setSavedAccountAsDefaultOnInternalQueue:forProtectionSpace:context:associatedDomainsManager:]
+ -[WBSSavedAccountStore _setSavedAccountAsDefaultOnInternalQueue:forProtectionSpace:context:associatedDomainsManager:].cold.1
+ -[WBSSavedAccountStore _setSavedAccountAsDefaultOnInternalQueue:forProtectionSpace:context:associatedDomainsManager:].cold.2
+ -[WBSSavedAccountStore _setSavedAccountAsDefaultOnInternalQueue:forProtectionSpace:context:associatedDomainsManager:].cold.3
+ -[WBSSavedAccountStore _setSavedAccountAsDefaultOnInternalQueue:forProtectionSpace:context:associatedDomainsManager:].cold.4
+ -[WBSSavedAccountStore setSavedAccountAsDefault:forProtectionSpace:context:associatedDomainsManager:]
+ -[WBSSavedAccountStore setSavedAccountAsDefault:forProtectionSpace:context:associatedDomainsManager:completionHandler:]
+ GCC_except_table285
+ GCC_except_table344
+ GCC_except_table346
+ GCC_except_table351
+ GCC_except_table357
+ ___101-[WBSSavedAccountStore setSavedAccountAsDefault:forProtectionSpace:context:associatedDomainsManager:]_block_invoke
+ ___119-[WBSSavedAccountStore setSavedAccountAsDefault:forProtectionSpace:context:associatedDomainsManager:completionHandler:]_block_invoke
+ ___145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke.348
+ ___145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke_2.349
+ ___66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.356
+ ___66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.360
+ ___69-[WBSSavedAccountStore _performRecentlyDeletedMaintenanceIfNecessary]_block_invoke.334
+ ___74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.335
+ ___74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.335.cold.1
+ ___74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.339
+ ___86-[WBSSavedAccountStore _ensureNoRecentlyDeletedSavedAccountsConflictWithSavedAccount:]_block_invoke.368
+ ___86-[WBSSavedAccountStore _moveContributedSavedAccountsBackToPersonalKeychainIfNecessary]_block_invoke.355
+ ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.342
+ ___block_literal_global.344
+ ___block_literal_global.351
+ ___block_literal_global.359
+ ___block_literal_global.367
+ ___block_literal_global.814
+ ___block_literal_global.891
+ ___block_literal_global.897
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_SafariCore
+ _objc_msgSend$_setSavedAccountAsDefaultOnInternalQueue:forProtectionSpace:context:associatedDomainsManager:
+ _objc_msgSend$safari_protectionSpaceBySimplifyingHost
- -[WBSSavedAccountStore setSavedAccountAsDefault:forProtectionSpace:]
- -[WBSSavedAccountStore setSavedAccountAsDefault:forProtectionSpace:context:]
- -[WBSSavedAccountStore setSavedAccountAsDefault:forProtectionSpace:context:].cold.1
- -[WBSSavedAccountStore setSavedAccountAsDefault:forProtectionSpace:context:].cold.2
- -[WBSSavedAccountStore setSavedAccountAsDefault:forProtectionSpace:context:].cold.3
- -[WBSSavedAccountStore setSavedAccountAsDefault:forProtectionSpace:context:].cold.4
- GCC_except_table263
- GCC_except_table284
- GCC_except_table343
- GCC_except_table345
- GCC_except_table350
- ___145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke.349
- ___145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke_2.350
- ___66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.357
- ___66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.361
- ___69-[WBSSavedAccountStore _performRecentlyDeletedMaintenanceIfNecessary]_block_invoke.335
- ___74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.336
- ___74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.336.cold.1
- ___74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.340
- ___86-[WBSSavedAccountStore _ensureNoRecentlyDeletedSavedAccountsConflictWithSavedAccount:]_block_invoke.369
- ___86-[WBSSavedAccountStore _moveContributedSavedAccountsBackToPersonalKeychainIfNecessary]_block_invoke.356
- ___90-[WBSSavedAccountStore _hasSavedAccountWithSameUserNameOfSavedAccount:forProtectionSpace:]_block_invoke_2
- ___94-[WBSSavedAccountStore _shouldUpdateLastUsedDateForSavedAccount:forProtectionSpace:inContext:]_block_invoke
- ___block_descriptor_48_e8_32s40r_e36_v16?0"WBSSavedAccountMatchResult"8lr40l8s32l8
- ___block_literal_global.343
- ___block_literal_global.345
- ___block_literal_global.352
- ___block_literal_global.360
- ___block_literal_global.368
- ___block_literal_global.813
- ___block_literal_global.890
- ___block_literal_global.896
- _objc_msgSend$hasProtectionSpaceForAdditionalSite:
- _objc_msgSend$setSavedAccountAsDefault:forProtectionSpace:context:
CStrings:
+ "Adding generated password for %{sensitive}@"
+ "Attempted to set non-sidecar object of type %{public}@ for %{sensitive}@ (%{sensitive}@)"
+ "Failed to delete recently generated password item for date %@ and host %{sensitive}@: status=%ld"
+ "Failed to migrate keychain item; protectionSpace: %{sensitive}@, username: %{sensitive}@"
+ "Invalid sidecar type (%lu) while setting sidecar for %{sensitive}@ (%{sensitive}@)"
+ "Migrating keychain item; protectionSpace: %{sensitive}@, username: %{sensitive}@"
+ "No generated password item found for date %@ and host %{sensitive}@"
+ "Removing generated password item for %{sensitive}@"
+ "Simplified protection space from %{sensitive}@ to %{sensitive}@ before setting saved account as default"
+ "Unable to fetch generated password item for date %@ and host %{sensitive}@"
+ "Unable to move credential %{sensitive}@ (%{sensitive}@) to access group %@: %@"
+ "Unable to query for passkey credential item for %@ (%{sensitive}@): %ld"
+ "Unable to query for password credential item for %{sensitive}@ (%{sensitive}@): %ld"
+ "Unable to query for sidecar item for %{sensitive}@ (%{sensitive}@): %ld"
+ "Updating generated password for %{sensitive}@"
+ "_setSavedAccountAsDefaultOnInternalQueue:forProtectionSpace:context:associatedDomainsManager:"
+ "safari_protectionSpaceBySimplifyingHost"
+ "setSavedAccountAsDefault:forProtectionSpace:context:associatedDomainsManager:"
+ "setSavedAccountAsDefault:forProtectionSpace:context:associatedDomainsManager:completionHandler:"
- "Adding generated password for %@"
- "Attempted to set non-sidecar object of type %{public}@ for %@ (%@)"
- "Failed to delete recently generated password item for date %@ and host %@: status=%ld"
- "Failed to migrate keychain item; protectionSpace: %@, username: %@"
- "Invalid sidecar type (%lu) while setting sidecar for %@ (%@)"
- "Migrating keychain item; protectionSpace: %@, username: %@"
- "No generated password item found for date %@ and host %@"
- "Removing generated password item for %@"
- "Unable to fetch generated password item for date %@ and host %@"
- "Unable to move credential %@ (%@) to access group %@: %@"
- "Unable to query for passkey credential item for %@ (%@): %ld"
- "Unable to query for password credential item for %@ (%@): %ld"
- "Unable to query for sidecar item for %@ (%@): %ld"
- "Updating generated password for %@"
- "setSavedAccountAsDefault:forProtectionSpace:"
- "setSavedAccountAsDefault:forProtectionSpace:context:"

```
