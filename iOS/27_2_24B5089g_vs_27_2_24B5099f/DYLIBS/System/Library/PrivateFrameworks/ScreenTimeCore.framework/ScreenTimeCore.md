## ScreenTimeCore

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore`

```diff

-655.1.9.1.0
-  __TEXT.__text: 0xf78d8
-  __TEXT.__objc_methlist: 0xa420
-  __TEXT.__const: 0x3538
-  __TEXT.__cstring: 0xa91c
-  __TEXT.__oslogstring: 0xc32a
-  __TEXT.__gcc_except_tab: 0x1b80
+655.1.12.0.0
+  __TEXT.__text: 0x1004f8
+  __TEXT.__objc_methlist: 0xa4c0
+  __TEXT.__const: 0x35a8
+  __TEXT.__cstring: 0xa9cc
+  __TEXT.__oslogstring: 0xc85a
+  __TEXT.__gcc_except_tab: 0x1bb0
   __TEXT.__constg_swiftt: 0xe14
-  __TEXT.__swift5_typeref: 0x15d2
+  __TEXT.__swift5_typeref: 0x1704
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_reflstr: 0x7fe
   __TEXT.__swift5_fieldmd: 0xa34
   __TEXT.__swift5_assocty: 0x138
   __TEXT.__swift5_proto: 0x214
   __TEXT.__swift5_types: 0xf8
-  __TEXT.__swift5_capture: 0xb8c
+  __TEXT.__swift5_capture: 0xbe4
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__swift_as_entry: 0x180
-  __TEXT.__swift_as_ret: 0x1bc
-  __TEXT.__swift_as_cont: 0x258
+  __TEXT.__swift_as_entry: 0x18c
+  __TEXT.__swift_as_ret: 0x1c8
+  __TEXT.__swift_as_cont: 0x278
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x5440
-  __TEXT.__eh_frame: 0x4490
+  __TEXT.__unwind_info: 0x5620
+  __TEXT.__eh_frame: 0x4960
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1f40
-  __DATA_CONST.__objc_classlist: 0x6f0
+  __DATA_CONST.__objc_classlist: 0x6f8
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x240
+  __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x54f0
-  __DATA_CONST.__objc_protorefs: 0x138
+  __DATA_CONST.__objc_selrefs: 0x5548
+  __DATA_CONST.__objc_protorefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x4d0
   __DATA_CONST.__objc_arraydata: 0x260
-  __DATA_CONST.__got: 0xef0
-  __AUTH_CONST.__const: 0x37c8
-  __AUTH_CONST.__cfstring: 0x9a60
-  __AUTH_CONST.__objc_const: 0x135b0
+  __DATA_CONST.__got: 0xef8
+  __AUTH_CONST.__const: 0x38b8
+  __AUTH_CONST.__cfstring: 0x9a80
+  __AUTH_CONST.__objc_const: 0x13660
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x13a0
-  __AUTH.__objc_data: 0x3248
-  __AUTH.__data: 0x4e0
-  __DATA.__objc_ivar: 0x7e0
-  __DATA.__data: 0x2210
-  __DATA.__common: 0xd0
+  __AUTH_CONST.__auth_got: 0x1410
+  __AUTH.__objc_data: 0x32b8
+  __AUTH.__data: 0x508
+  __DATA.__objc_ivar: 0x7e4
+  __DATA.__data: 0x2350
+  __DATA.__common: 0xe8
   __DATA_DIRTY.__objc_data: 0x1f40
-  __DATA_DIRTY.__data: 0x2a8
+  __DATA_DIRTY.__data: 0x2b8
   __DATA_DIRTY.__bss: 0x1c0
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6048
-  Symbols:   6865
-  CStrings:  2294
+  Functions: 6144
+  Symbols:   6905
+  CStrings:  2309
 
Symbols:
+ -[STAppInfoCache isMigratedToNewScreenTime]
+ -[STConversation _allHandlesAreManagingParents:]
+ -[STConversation _isManagingParentHandle:]
+ -[STConversation allowableByContactsHandles:allowingManagingParentsWhenBlocked:]
+ -[STConversationContext allowsManagingParentsWhenBlocked]
+ -[STConversationContext setAllowsManagingParentsWhenBlocked:]
+ -[STConversationContext updateShouldBeAllowedDuringGeneralScreenTime:shouldBeAllowedByScreenTimeWhenLimited:shouldBeAllowedWhenBlocked:currentApplicationState:emergencyModeEnabled:]
+ -[STManagementState migrateAppDataFromBundleIdentifier:toBundleIdentifier:completionHandler:]
+ GCC_except_table34
+ GCC_except_table37
+ GCC_except_table40
+ GCC_except_table50
+ GCC_except_table55
+ GCC_except_table66
+ GCC_except_table68
+ _OBJC_CLASS_$_STAppDataMigrator
+ _OBJC_IVAR_$_STConversationContext._allowsManagingParentsWhenBlocked
+ _OBJC_METACLASS_$_STAppDataMigrator
+ _STDisplayableBundleIdentifiers
+ __CLASS_METHODS_STAppDataMigrator
+ __DATA_STAppDataMigrator
+ __INSTANCE_METHODS_STAppDataMigrator
+ __METACLASS_DATA_STAppDataMigrator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_STAppDataMigratorCategoryProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_STAppDataMigratorCategoryProviding
+ __OBJC_$_PROTOCOL_REFS_STAppDataMigratorCategoryProviding
+ __OBJC_LABEL_PROTOCOL_$_STAppDataMigratorCategoryProviding
+ __OBJC_PROTOCOL_$_STAppDataMigratorCategoryProviding
+ ___93-[STManagementState migrateAppDataFromBundleIdentifier:toBundleIdentifier:completionHandler:]_block_invoke
+ ___93-[STManagementState migrateAppDataFromBundleIdentifier:toBundleIdentifier:completionHandler:]_block_invoke_2
+ __swift_implicitisolationactor_to_executor_cast
+ _flat unique So34STAppDataMigratorCategoryProviding_p
+ _swift_release_n
+ _swift_retain_x28
+ _symbolic SDySSSo10CTCategoryCG
+ _symbolic ScCySDySSSo10CTCategoryCG______pG s5ErrorP
+ _symbolic So17STAppDataMigratorCXMT
+ _symbolic ______p So34STAppDataMigratorCategoryProvidingP
+ _symbolic _____ySSSo10CTCategoryCG s18_DictionaryStorageC
+ _symbolic _____ySnySiGG s23_ContiguousArrayStorageC
+ _symbolic _____ySo11STBlueprintCG s11_SetStorageC
+ _symbolic _____ySo21STBlueprintUsageLimitCG s11_SetStorageC
+ _symbolic _____ySo24STBlueprintConfigurationCG s11_SetStorageC
+ _symbolic _____ySo8NSNumberCACG s18_DictionaryStorageC
+ _symbolic _____y______pG s23_ContiguousArrayStorageC s5ErrorP
- -[STConversationContext updateShouldBeAllowedDuringGeneralScreenTime:shouldBeAllowedByScreenTimeWhenLimited:currentApplicationState:emergencyModeEnabled:]
- GCC_except_table44
- GCC_except_table54
- GCC_except_table63
- GCC_except_table64
CStrings:
+ "Added %{public}s to %ld of %ld app limit(s) for app data migration"
+ "Failed to fetch always-allowed bundle identifiers, proceeding as if empty: %{public}s"
+ "Failed to save app limit while adding %{public}s for app data migration: %{public}s"
+ "Not adding destination to app limit matched by source bundle identifier: already covered by the limit's own category"
+ "Not making any changes for app data migration from %{public}s to %{public}s due to a missing managing organization"
+ "Not updating app limits for source category: %{public}s and %{public}s share the same category"
+ "Not updating app limits for source category: no category found for source bundle identifier %{public}s"
+ "Not updating app limits for source category: source bundle identifier's category is not covered by any app limit"
+ "Requested %{public}@ context allowing managing parents when blocked for handles:%{private}@. currentApplicationState:%lu allowedByScreenTime:%d managingParentAppleIDs:%{private}@"
+ "Skipping app data migration as source and destination resolve to the same canonical app: %{public}s"
+ "Skipping app data migration to %{public}s as it already has an existing app limits configured"
+ "Skipping app data migration to %{public}s as it is already in always allowed"
+ "appDataMigration"
+ "com.apple.SiriApp"
+ "migrateAppData(fromBundleIdentifier:toBundleIdentifier:persistenceController:categoryProvider:completionHandler:)"
```
