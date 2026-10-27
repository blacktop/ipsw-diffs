## IntlPreferences

> `/System/Library/PrivateFrameworks/IntlPreferences.framework/Versions/A/IntlPreferences`

```diff

-496.0.0.0.0
-  __TEXT.__text: 0x2bb24
-  __TEXT.__objc_methlist: 0x26ac
-  __TEXT.__const: 0x228
-  __TEXT.__gcc_except_tab: 0x334
-  __TEXT.__cstring: 0x2a35
-  __TEXT.__oslogstring: 0x114b
+500.1.1.0.0
+  __TEXT.__text: 0x2ccc8
+  __TEXT.__objc_methlist: 0x270c
+  __TEXT.__const: 0x238
+  __TEXT.__gcc_except_tab: 0x348
+  __TEXT.__cstring: 0x2ad5
+  __TEXT.__oslogstring: 0x156a
   __TEXT.__dlopen_cstrs: 0xea
   __TEXT.__ustring: 0x58
   __TEXT.__swift5_typeref: 0x66
-  __TEXT.__unwind_info: 0x8d8
+  __TEXT.__unwind_info: 0x920
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2240
+  __DATA_CONST.__objc_selrefs: 0x2280
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x890
-  __DATA_CONST.__got: 0x510
-  __AUTH_CONST.__const: 0xa00
-  __AUTH_CONST.__cfstring: 0x3a60
-  __AUTH_CONST.__objc_const: 0x4720
+  __DATA_CONST.__got: 0x520
+  __AUTH_CONST.__const: 0xa60
+  __AUTH_CONST.__cfstring: 0x3ac0
+  __AUTH_CONST.__objc_const: 0x4738
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x650
+  __AUTH_CONST.__auth_got: 0x658
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x320
+  __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x1cc
   __DATA.__data: 0x380
   __DATA.__bss: 0x220
-  __DATA_DIRTY.__objc_data: 0x6e0
+  __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__data: 0x48
   __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 827
-  Symbols:   2457
-  CStrings:  610
+  Functions: 840
+  Symbols:   2478
+  CStrings:  623
 
Symbols:
+ +[IntlUtility _migratePerAppLanguageSelectionOutOfGlobalDomain]
+ +[IntlUtility _migratePreferredLanguageFromBundleID:sourceContainerPath:toBundleID:destinationContainerPath:carriedLanguages:error:]
+ +[IntlUtility _perAppLanguageSelectionBundleIdentifiersFromPrivateDomain]
+ +[IntlUtility _updatePerAppLanguageSelectionInPrivateDomainForBundleID:selected:]
+ +[IntlUtility perAppLanguageSelectionBundleIdentifiersWithCompletion:]
+ GCC_except_table115
+ _NSLocalizedDescriptionKey
+ _OUTLINED_FUNCTION_4
+ __55+[IntlUtility perAppLanguageSelectionBundleIdentifiers]_block_invoke
+ __70+[IntlUtility perAppLanguageSelectionBundleIdentifiersWithCompletion:]_block_invoke
+ __CFPreferencesSynchronizeWithContainer
+ ___49+[IntlUtility _setPreferredLanguage:forBundleID:]_block_invoke
+ ___55+[IntlUtility perAppLanguageSelectionBundleIdentifiers]_block_invoke
+ ___70+[IntlUtility perAppLanguageSelectionBundleIdentifiersWithCompletion:]_block_invoke
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSArray"8l
+ ___block_descriptor_48_e8_32bs_e17_v16?0"NSError"8l
+ __appleLanguagesInContainer
+ _kCFPreferencesCurrentApplication
+ _objc_msgSend$_perAppLanguageSelectionBundleIdentifiersFromPrivateDomain
+ _objc_msgSend$_updatePerAppLanguageSelectionInPrivateDomainForBundleID:selected:
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
