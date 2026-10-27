## IntlPreferences

> `/System/iOSSupport/System/Library/PrivateFrameworks/IntlPreferences.framework/Versions/A/IntlPreferences`

```diff

-496.0.0.0.0
-  __TEXT.__text: 0x192e4
-  __TEXT.__objc_methlist: 0x10cc
-  __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x1145
-  __TEXT.__oslogstring: 0xc19
-  __TEXT.__gcc_except_tab: 0x120
+500.1.1.0.0
+  __TEXT.__text: 0x1a38c
+  __TEXT.__objc_methlist: 0x112c
+  __TEXT.__const: 0x200
+  __TEXT.__cstring: 0x11e5
+  __TEXT.__oslogstring: 0x1038
+  __TEXT.__gcc_except_tab: 0x134
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x76
-  __TEXT.__unwind_info: 0x518
+  __TEXT.__unwind_info: 0x550
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x528
+  __DATA_CONST.__const: 0x578
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf60
+  __DATA_CONST.__objc_selrefs: 0xfa8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x360
-  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__got: 0x2d0
   __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0x19e0
-  __AUTH_CONST.__objc_const: 0x1508
+  __AUTH_CONST.__cfstring: 0x1a40
+  __AUTH_CONST.__objc_const: 0x1520
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x1b0
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x5d0
+  __AUTH_CONST.__auth_got: 0x5d8
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x54
   __DATA.__data: 0x148
   __DATA.__bss: 0x148
-  __DATA_DIRTY.__objc_data: 0x640
+  __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__data: 0x48
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 411
-  Symbols:   1287
-  CStrings:  303
+  Functions: 424
+  Symbols:   1311
+  CStrings:  316
 
Symbols:
+ +[IntlUtility _migratePerAppLanguageSelectionOutOfGlobalDomain]
+ +[IntlUtility _migratePreferredLanguageFromBundleID:sourceContainerPath:toBundleID:destinationContainerPath:carriedLanguages:error:]
+ +[IntlUtility _perAppLanguageSelectionBundleIdentifiersFromPrivateDomain]
+ +[IntlUtility _updatePerAppLanguageSelectionInPrivateDomainForBundleID:selected:]
+ +[IntlUtility perAppLanguageSelectionBundleIdentifiersWithCompletion:]
+ GCC_except_table105
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_NSError
+ _OUTLINED_FUNCTION_2
+ __55+[IntlUtility perAppLanguageSelectionBundleIdentifiers]_block_invoke
+ __70+[IntlUtility perAppLanguageSelectionBundleIdentifiersWithCompletion:]_block_invoke
+ __CFPreferencesSynchronizeWithContainer
+ ___49+[IntlUtility _setPreferredLanguage:forBundleID:]_block_invoke
+ ___55+[IntlUtility perAppLanguageSelectionBundleIdentifiers]_block_invoke
+ ___70+[IntlUtility perAppLanguageSelectionBundleIdentifiersWithCompletion:]_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSArray"8lr32l8
+ ___block_descriptor_48_e8_32bs_e17_v16?0"NSError"8ls32l8
+ __appleLanguagesInContainer
+ _kCFPreferencesCurrentApplication
+ _objc_msgSend$_perAppLanguageSelectionBundleIdentifiersFromPrivateDomain
+ _objc_msgSend$_updatePerAppLanguageSelectionInPrivateDomainForBundleID:selected:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$perAppLanguageSelectionBundleIdentifiersWithReply:
+ _objc_msgSend$updatePerAppLanguageSelectionForBundleID:selected:
- _objc_msgSend$perAppLanguageSelectionBundleIdentifiers
CStrings:
+ "### [%{public}@]: Per-app language migration failed: could not synchronize AppleLanguages for %{private}@"
+ "Empty bundle identifier or container path"
+ "Failed to synchronize AppleLanguages for the destination app"
+ "[%{public}@]: Error obtaining remote object proxy to update per-app-language selection, %{public}@"
+ "[%{public}@]: Migrated per-app-language index (%lu entries) from global domain into private domain"
+ "[%{public}@]: Per-app language migration complete: %{private}@ -> %{private}@, override language [%{public}@], %lu entries"
+ "[%{public}@]: Per-app language migration complete: [%{public}@] resolves to the default for %{private}@, so nothing was recorded"
+ "[%{public}@]: Per-app language migration complete: source %{private}@ had no override to carry over"
+ "[%{public}@]: Per-app language migration rejected: empty bundle identifier or container path"
+ "[%{public}@]: Per-app language migration skipped: source and destination are the same app"
+ "[%{public}@]: Private per-app-language index already present; discarding legacy global copy"
+ "[IntlUtility]: Per-app language migration could not read the destination bundle for %{private}@; carrying the override over"
+ "com.apple.IntlPreferences.PerAppLanguageMigration"
```
