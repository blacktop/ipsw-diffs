## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/Versions/A/SafariCore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_types2`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-625.1.22.11.4
-  __TEXT.__text: 0x1fe9b4
-  __TEXT.__objc_methlist: 0xd37c
+625.1.24.11.2
+  __TEXT.__text: 0x200d24
+  __TEXT.__objc_methlist: 0xd434
   __TEXT.__const: 0x7a94
-  __TEXT.__gcc_except_tab: 0x7d30
-  __TEXT.__cstring: 0x172b7
+  __TEXT.__gcc_except_tab: 0x7d5c
+  __TEXT.__cstring: 0x17427
   __TEXT.__ustring: 0x2784
-  __TEXT.__oslogstring: 0xe531
+  __TEXT.__oslogstring: 0xe631
   __TEXT.__dlopen_cstrs: 0x157
   __TEXT.__constg_swiftt: 0x21c4
-  __TEXT.__swift5_typeref: 0x25b4
+  __TEXT.__swift5_typeref: 0x25c2
   __TEXT.__swift5_reflstr: 0x14db
   __TEXT.__swift5_fieldmd: 0x196c
   __TEXT.__swift5_builtin: 0x140

   __TEXT.__swift5_capture: 0x142c
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x9b20
-  __TEXT.__eh_frame: 0xa270
+  __TEXT.__unwind_info: 0x9b48
+  __TEXT.__eh_frame: 0xa2a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2810
+  __DATA_CONST.__const: 0x2808
   __DATA_CONST.__objc_classlist: 0x708
   __DATA_CONST.__objc_catlist: 0x160
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7708
+  __DATA_CONST.__objc_selrefs: 0x7770
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x4c8
   __DATA_CONST.__objc_arraydata: 0x2a98
-  __DATA_CONST.__got: 0x13b8
-  __AUTH_CONST.__const: 0xe698
-  __AUTH_CONST.__cfstring: 0x1b300
-  __AUTH_CONST.__objc_const: 0x164b0
+  __DATA_CONST.__got: 0x13c0
+  __AUTH_CONST.__const: 0xe748
+  __AUTH_CONST.__cfstring: 0x1b420
+  __AUTH_CONST.__objc_const: 0x16570
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x588
-  __AUTH_CONST.__auth_got: 0x20b0
+  __AUTH_CONST.__auth_got: 0x20b8
   __AUTH.__objc_data: 0x21a0
   __AUTH.__data: 0xfd8
-  __DATA.__objc_ivar: 0xd1c
-  __DATA.__data: 0x3440
-  __DATA.__bss: 0x9c90
+  __DATA.__objc_ivar: 0xd2c
+  __DATA.__data: 0x3480
+  __DATA.__bss: 0x9ca0
   __DATA.__common: 0x78
   __DATA_DIRTY.__objc_data: 0x2ac0
   __DATA_DIRTY.__data: 0xed8

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11355
-  Symbols:   15036
-  CStrings:  5302
+  Functions: 11388
+  Symbols:   15085
+  CStrings:  5317
 
Symbols:
+ +[WBSFeatureAvailability shouldSkipAutomaticPasswordChangeAllowedDomainCheck]
+ +[WBSGeneratedPassword keychainDictionaryRepresentationWithPassword:displayName:serviceIdentifierType:serviceIdentifier:]
+ +[WBSSQLiteDatabase setUpSQLiteTemporaryDirectory]
+ +[WBSSavedAccountAppURL protectionSpaceForAppID:]
+ +[WBSSavedAccountStore splitAdditionalSites:forSavedAccount:additionalSitesToWriteToSidecar:additionalSitesToSaveToNewKeychainItems:]
+ -[WBSGeneratedPassword _initWithPassword:protectionSpace:displayName:serviceIdentifierType:generationDate:wasGeneratedInPrivateBrowsingSession:keychainPersistentReference:originalDictionary:]
+ -[WBSGeneratedPassword displayName]
+ -[WBSGeneratedPassword initWithPassword:protectionSpace:displayName:serviceIdentifierType:generationDate:wasGeneratedInPrivateBrowsingSession:]
+ -[WBSGeneratedPassword serviceIdentifierType]
+ -[WBSGeneratedPasswordStore addGeneratedPassword:forProtectionSpace:displayName:serviceIdentifierType:inPrivateBrowsingSession:completionHandler:]
+ -[WBSManagedExtensionsConfigurationStore cachedConfiguration]
+ -[WBSManagedExtensionsConfigurationStore init]
+ -[WBSManagedExtensionsConfigurationStore setCachedConfiguration:]
+ -[WBSSavedAccount _firstSidecarForAnySiteOfType:allowPasskeySidecars:]
+ -[WBSSavedAccount automaticPasswordChangeAccountLevelEligibility]
+ -[WBSSavedAccountKeychainCoordinator addGeneratedPassword:forProtectionSpace:displayName:serviceIdentifierType:wasGeneratedInPrivateBrowsingSession:]
+ GCC_except_table127
+ GCC_except_table253
+ GCC_except_table384
+ GCC_except_table454
+ GCC_except_table459
+ GCC_except_table465
+ GCC_except_table490
+ OBJC_IVAR_$_WBSGeneratedPassword._displayName
+ OBJC_IVAR_$_WBSGeneratedPassword._serviceIdentifierType
+ OBJC_IVAR_$_WBSManagedExtensionsConfigurationStore._cachedConfiguration
+ OBJC_IVAR_$_WBSManagedExtensionsConfigurationStore._hasBegunObserving
+ OBJC_IVAR_$_WBSManagedExtensionsConfigurationStore._internalQueue
+ WBSOSLogMagicExtensionsSync
+ WBSOSLogMagicExtensionsSync.log
+ WBSOSLogMagicExtensionsSync.onceToken
+ _WBSAutomaticPasswordChangeDebugSiteShouldEnableObstacleKey
+ _WBSAutomaticPasswordChangeDisableIsOnAllowedDomainCheckKey
+ _WBSOSLogMagicExtensionsSync
+ _WBSWebExtensionPointIdentifier
+ __50+[WBSSQLiteDatabase setUpSQLiteTemporaryDirectory]_block_invoke
+ __ZZ50+[WBSSQLiteDatabase setUpSQLiteTemporaryDirectory]E9onceToken
+ ___146-[WBSGeneratedPasswordStore addGeneratedPassword:forProtectionSpace:displayName:serviceIdentifierType:inPrivateBrowsingSession:completionHandler:]_block_invoke
+ ___50+[WBSSQLiteDatabase setUpSQLiteTemporaryDirectory]_block_invoke
+ ___63-[WBSManagedExtensionsConfigurationStore beginObservingStorage]_block_invoke
+ ___76-[WBSManagedExtensionsConfigurationStore _underlyingConfigurationDidChange:]_block_invoke_2
+ ___WBSOSLogMagicExtensionsSync_block_invoke
+ ___block_descriptor_40_e8_32s_e49_"NSString"16?0"WBSSavedAccountAdditionalSite"8l
+ ___block_descriptor_40_e8_32s_e49_"WBSSavedAccountAdditionalSite"16?0"NSString"8l
+ ___block_descriptor_45_e8_32s_e45_v24?0q8"<WBSSavedAccountSidecarInternal>"16l
+ ___block_descriptor_49_e8_32s40bs_e45_v24?0q8"<WBSSavedAccountSidecarInternal>"16l
+ ___block_descriptor_81_e8_32s40s48s56bs64w_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56b64w
+ ___destroy_helper_block_e8_32s40s48s56s64w
+ _objc_msgSend$_firstSidecarForAnySiteOfType:allowPasskeySidecars:
+ _objc_msgSend$_initWithPassword:protectionSpace:displayName:serviceIdentifierType:generationDate:wasGeneratedInPrivateBrowsingSession:keychainPersistentReference:originalDictionary:
+ _objc_msgSend$addGeneratedPassword:forProtectionSpace:displayName:serviceIdentifierType:inPrivateBrowsingSession:completionHandler:
+ _objc_msgSend$addGeneratedPassword:forProtectionSpace:displayName:serviceIdentifierType:wasGeneratedInPrivateBrowsingSession:
+ _objc_msgSend$automaticPasswordChangeAccountLevelEligibility
+ _objc_msgSend$cachedConfiguration
+ _objc_msgSend$initWithPassword:protectionSpace:displayName:serviceIdentifierType:generationDate:wasGeneratedInPrivateBrowsingSession:
+ _objc_msgSend$keychainDictionaryRepresentationWithPassword:displayName:serviceIdentifierType:serviceIdentifier:
+ _objc_msgSend$protectionSpaceForAppID:
+ _objc_msgSend$safari_createTemporaryDirectoryWithError:
+ _objc_msgSend$setCachedConfiguration:
+ _objc_msgSend$shouldSkipAutomaticPasswordChangeAllowedDomainCheck
+ _objc_msgSend$splitAdditionalSites:forSavedAccount:additionalSitesToWriteToSidecar:additionalSitesToSaveToNewKeychainItems:
+ _sqlite3_mprintf
+ _sqlite3_temp_directory
+ _symbolic _____y_____G s11_SetStorageC 16GenerativeModels0cD12AvailabilityV0E0O14RestrictedInfoV0F6ReasonO
- -[WBSGeneratedPassword _initWithPassword:protectionSpace:generationDate:wasGeneratedInPrivateBrowsingSession:keychainPersistentReference:originalDictionary:]
- GCC_except_table218
- GCC_except_table223
- GCC_except_table260
- GCC_except_table274
- GCC_except_table338
- GCC_except_table382
- GCC_except_table450
- GCC_except_table457
- OBJC_IVAR_$_WBSManagedExtensionsConfigurationStore._managedExtensionsConfiguration
- ___112-[WBSGeneratedPasswordStore addGeneratedPassword:forProtectionSpace:inPrivateBrowsingSession:completionHandler:]_block_invoke
- ___block_descriptor_32_e49_"NSString"16?0"WBSSavedAccountAdditionalSite"8l
- ___block_descriptor_46_e8_32s_e45_v24?0q8"<WBSSavedAccountSidecarInternal>"16l
- ___block_descriptor_65_e8_32s40s48bs56w_e5_v8?0l
- _objc_msgSend$_initWithPassword:protectionSpace:generationDate:wasGeneratedInPrivateBrowsingSession:keychainPersistentReference:originalDictionary:
- _objc_msgSend$addGeneratedPassword:forProtectionSpace:wasGeneratedInPrivateBrowsingSession:
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hx5mXZ/Sources/SafariShared/SafariShared/SafariCore/FoundationExtras/WBSCoreNSBundleExtras.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hx5mXZ/Sources/SafariShared/SafariShared/SafariCore/Preferences/WBSSearchEnginePreferenceObserver.m"
+ "<nil>"
+ "<none>"
+ "@\"WBSSavedAccountAdditionalSite\"16@?0@\"NSString\"8"
+ "Could not create a private SQLite temporary directory; SQLite will fall back to its default. error: %{public}@"
+ "PMAutomaticPasswordChangeDebugSiteShouldEnableObstacle"
+ "Skipping isAllowedDomain check (running for %{public}@; attempted URL %{sensitive}@)"
+ "Skipping migration of accounts with invalid authentication types"
+ "TabOverviewDragAndDrop"
+ "UsageRetentionDonation"
+ "WBSAutomaticPasswordChangeDisableIsOnAllowedDomainCheck"
+ "app!"
+ "com.apple.Safari.web-extension"
+ "com.apple.SafariCore.WBSManagedExtensionsConfigurationStore"
+ "serviceIdentifier"
+ "serviceIdentifierType"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nymWhR/Sources/SafariShared/SafariShared/SafariCore/FoundationExtras/WBSCoreNSBundleExtras.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nymWhR/Sources/SafariShared/SafariShared/SafariCore/Preferences/WBSSearchEnginePreferenceObserver.m"
```
