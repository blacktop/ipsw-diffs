## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`

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
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-625.1.22.10.3
-  __TEXT.__text: 0x1e93b0
-  __TEXT.__objc_methlist: 0xd03c
+625.1.24.10.1
+  __TEXT.__text: 0x1eb4f8
+  __TEXT.__objc_methlist: 0xd0fc
   __TEXT.__const: 0x7aa4
-  __TEXT.__gcc_except_tab: 0x772c
-  __TEXT.__cstring: 0x16bc7
+  __TEXT.__gcc_except_tab: 0x7758
+  __TEXT.__cstring: 0x16d47
   __TEXT.__ustring: 0x2784
-  __TEXT.__oslogstring: 0xe161
+  __TEXT.__oslogstring: 0xe261
   __TEXT.__dlopen_cstrs: 0x157
   __TEXT.__constg_swiftt: 0x21c4
-  __TEXT.__swift5_typeref: 0x25b4
+  __TEXT.__swift5_typeref: 0x25c2
   __TEXT.__swift5_reflstr: 0x14db
   __TEXT.__swift5_fieldmd: 0x1978
   __TEXT.__swift5_builtin: 0x140

   __TEXT.__swift5_capture: 0x1490
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x9a88
-  __TEXT.__eh_frame: 0xa3c0
+  __TEXT.__unwind_info: 0x9ae0
+  __TEXT.__eh_frame: 0xa3f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x58a0
+  __DATA_CONST.__const: 0x5910
   __DATA_CONST.__objc_classlist: 0x6f8
   __DATA_CONST.__objc_catlist: 0x160
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7570
+  __DATA_CONST.__objc_selrefs: 0x75d8
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x4c0
   __DATA_CONST.__objc_arraydata: 0x2aa0
-  __DATA_CONST.__got: 0x13a0
-  __AUTH_CONST.__const: 0xaff8
-  __AUTH_CONST.__cfstring: 0x1ac40
-  __AUTH_CONST.__objc_const: 0x16200
+  __DATA_CONST.__got: 0x13a8
+  __AUTH_CONST.__const: 0xb018
+  __AUTH_CONST.__cfstring: 0x1ad60
+  __AUTH_CONST.__objc_const: 0x162c0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x5a0
-  __AUTH_CONST.__auth_got: 0x21a8
+  __AUTH_CONST.__auth_got: 0x21b0
   __AUTH.__objc_data: 0x2220
   __AUTH.__data: 0xfd0
-  __DATA.__objc_ivar: 0xd1c
-  __DATA.__data: 0x34f0
-  __DATA.__bss: 0xa410
+  __DATA.__objc_ivar: 0xd2c
+  __DATA.__data: 0x3540
+  __DATA.__bss: 0xa420
   __DATA.__common: 0x78
   __DATA_DIRTY.__objc_data: 0x2980
   __DATA_DIRTY.__data: 0xdc8

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11180
-  Symbols:   14516
-  CStrings:  5226
+  Functions: 11211
+  Symbols:   14564
+  CStrings:  5241
 
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
+ GCC_except_table206
+ GCC_except_table240
+ GCC_except_table304
+ GCC_except_table311
+ GCC_except_table413
+ GCC_except_table418
+ GCC_except_table424
+ GCC_except_table443
+ _OBJC_IVAR_$_WBSGeneratedPassword._displayName
+ _OBJC_IVAR_$_WBSGeneratedPassword._serviceIdentifierType
+ _OBJC_IVAR_$_WBSManagedExtensionsConfigurationStore._cachedConfiguration
+ _OBJC_IVAR_$_WBSManagedExtensionsConfigurationStore._hasBegunObserving
+ _OBJC_IVAR_$_WBSManagedExtensionsConfigurationStore._internalQueue
+ _WBSAutomaticPasswordChangeDebugSiteShouldEnableObstacleKey
+ _WBSAutomaticPasswordChangeDisableIsOnAllowedDomainCheckKey
+ _WBSOSLogMagicExtensionsSync
+ _WBSOSLogMagicExtensionsSync.log
+ _WBSOSLogMagicExtensionsSync.onceToken
+ _WBSWebExtensionPointIdentifier
+ __ZZ50+[WBSSQLiteDatabase setUpSQLiteTemporaryDirectory]E9onceToken
+ ___146-[WBSGeneratedPasswordStore addGeneratedPassword:forProtectionSpace:displayName:serviceIdentifierType:inPrivateBrowsingSession:completionHandler:]_block_invoke
+ ___50+[WBSSQLiteDatabase setUpSQLiteTemporaryDirectory]_block_invoke
+ ___63-[WBSManagedExtensionsConfigurationStore beginObservingStorage]_block_invoke
+ ___76-[WBSManagedExtensionsConfigurationStore _underlyingConfigurationDidChange:]_block_invoke_2
+ ___95-[WBSSavedAccountStore _changeSavedAccountWithRequestOnInternalQueue:performPostUpdateActions:]_block_invoke_3
+ ___WBSOSLogMagicExtensionsSync_block_invoke
+ ___block_descriptor_40_e8_32s_e49_"NSString"16?0"WBSSavedAccountAdditionalSite"8ls32l8
+ ___block_descriptor_40_e8_32s_e49_"WBSSavedAccountAdditionalSite"16?0"NSString"8ls32l8
+ ___block_descriptor_45_e8_32s_e45_v24?0q8"<WBSSavedAccountSidecarInternal>"16ls32l8
+ ___block_descriptor_49_e8_32s40bs_e45_v24?0q8"<WBSSavedAccountSidecarInternal>"16ls40l8s32l8
+ ___block_descriptor_81_e8_32s40s48s56bs64w_e5_v8?0lw64l8s56l8s32l8s40l8s48l8
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
- GCC_except_table114
- GCC_except_table204
- GCC_except_table302
- GCC_except_table309
- GCC_except_table341
- GCC_except_table409
- GCC_except_table416
- _OBJC_IVAR_$_WBSManagedExtensionsConfigurationStore._managedExtensionsConfiguration
- ___112-[WBSGeneratedPasswordStore addGeneratedPassword:forProtectionSpace:inPrivateBrowsingSession:completionHandler:]_block_invoke
- ___block_descriptor_32_e49_"NSString"16?0"WBSSavedAccountAdditionalSite"8l
- ___block_descriptor_46_e8_32s_e45_v24?0q8"<WBSSavedAccountSidecarInternal>"16ls32l8
- ___block_descriptor_65_e8_32s40s48bs56w_e5_v8?0lw56l8s48l8s32l8s40l8
- _objc_msgSend$_initWithPassword:protectionSpace:generationDate:wasGeneratedInPrivateBrowsingSession:keychainPersistentReference:originalDictionary:
- _objc_msgSend$addGeneratedPassword:forProtectionSpace:wasGeneratedInPrivateBrowsingSession:
CStrings:
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
```
