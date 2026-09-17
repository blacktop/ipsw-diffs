## IntlPreferences

> `/System/Library/PrivateFrameworks/IntlPreferences.framework/Versions/A/IntlPreferences`

```diff

-496.0.0.0.0
-  __TEXT.__text: 0x2a9bc
-  __TEXT.__objc_methlist: 0x26ac
+498.0.0.0.0
+  __TEXT.__text: 0x2b188
+  __TEXT.__objc_methlist: 0x26f4
   __TEXT.__const: 0x228
-  __TEXT.__gcc_except_tab: 0x334
+  __TEXT.__gcc_except_tab: 0x348
   __TEXT.__cstring: 0x2a35
-  __TEXT.__oslogstring: 0x114b
+  __TEXT.__oslogstring: 0x126d
   __TEXT.__dlopen_cstrs: 0xea
   __TEXT.__ustring: 0x58
   __TEXT.__swift5_typeref: 0x66
-  __TEXT.__unwind_info: 0xae8
+  __TEXT.__unwind_info: 0xb18
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2240
+  __DATA_CONST.__objc_selrefs: 0x2270
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x890
-  __DATA_CONST.__got: 0x510
-  __AUTH_CONST.__const: 0xa00
+  __DATA_CONST.__got: 0x518
+  __AUTH_CONST.__const: 0xa60
   __AUTH_CONST.__cfstring: 0x3a60
-  __AUTH_CONST.__objc_const: 0x4720
+  __AUTH_CONST.__objc_const: 0x4730
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x168

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 827
-  Symbols:   2457
-  CStrings:  610
+  Functions: 836
+  Symbols:   2472
+  CStrings:  613
 
Symbols:
+ +[IntlUtility _migratePerAppLanguageSelectionOutOfGlobalDomain]
+ +[IntlUtility _perAppLanguageSelectionBundleIdentifiersFromPrivateDomain]
+ +[IntlUtility _updatePerAppLanguageSelectionInPrivateDomainForBundleID:selected:]
+ +[IntlUtility perAppLanguageSelectionBundleIdentifiersWithCompletion:]
+ GCC_except_table115
+ __55+[IntlUtility perAppLanguageSelectionBundleIdentifiers]_block_invoke
+ __70+[IntlUtility perAppLanguageSelectionBundleIdentifiersWithCompletion:]_block_invoke
+ ___49+[IntlUtility _setPreferredLanguage:forBundleID:]_block_invoke
+ ___55+[IntlUtility perAppLanguageSelectionBundleIdentifiers]_block_invoke
+ ___70+[IntlUtility perAppLanguageSelectionBundleIdentifiersWithCompletion:]_block_invoke
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSArray"8l
+ ___block_descriptor_48_e8_32bs_e17_v16?0"NSError"8l
+ _kCFPreferencesCurrentApplication
+ _objc_msgSend$_perAppLanguageSelectionBundleIdentifiersFromPrivateDomain
+ _objc_msgSend$perAppLanguageSelectionBundleIdentifiersWithReply:
+ _objc_msgSend$updatePerAppLanguageSelectionForBundleID:selected:
- _objc_msgSend$perAppLanguageSelectionBundleIdentifiers
CStrings:
+ "[%{public}@]: Error obtaining remote object proxy to update per-app-language selection, %{public}@"
+ "[%{public}@]: Migrated per-app-language index (%lu entries) from global domain into private domain"
+ "[%{public}@]: Private per-app-language index already present; discarding legacy global copy"
```
