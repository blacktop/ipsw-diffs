## IntlPreferences

> `/System/iOSSupport/System/Library/PrivateFrameworks/IntlPreferences.framework/Versions/A/IntlPreferences`

```diff

-496.0.0.0.0
-  __TEXT.__text: 0x18818
-  __TEXT.__objc_methlist: 0x10cc
-  __TEXT.__const: 0x1e0
+498.0.0.0.0
+  __TEXT.__text: 0x18f80
+  __TEXT.__objc_methlist: 0x1114
+  __TEXT.__const: 0x1f0
   __TEXT.__cstring: 0x1145
-  __TEXT.__oslogstring: 0xc19
-  __TEXT.__gcc_except_tab: 0x120
+  __TEXT.__oslogstring: 0xd3b
+  __TEXT.__gcc_except_tab: 0x134
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x76
-  __TEXT.__unwind_info: 0x670
+  __TEXT.__unwind_info: 0x698
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
+  __DATA_CONST.__objc_selrefs: 0xf90
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x360
-  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__got: 0x2c0
   __AUTH_CONST.__const: 0x260
   __AUTH_CONST.__cfstring: 0x19e0
-  __AUTH_CONST.__objc_const: 0x1508
+  __AUTH_CONST.__objc_const: 0x1518
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x1b0

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 411
-  Symbols:   1287
-  CStrings:  303
+  Functions: 420
+  Symbols:   1303
+  CStrings:  306
 
Symbols:
+ +[IntlUtility _migratePerAppLanguageSelectionOutOfGlobalDomain]
+ +[IntlUtility _perAppLanguageSelectionBundleIdentifiersFromPrivateDomain]
+ +[IntlUtility _updatePerAppLanguageSelectionInPrivateDomainForBundleID:selected:]
+ +[IntlUtility perAppLanguageSelectionBundleIdentifiersWithCompletion:]
+ GCC_except_table105
+ __55+[IntlUtility perAppLanguageSelectionBundleIdentifiers]_block_invoke
+ __70+[IntlUtility perAppLanguageSelectionBundleIdentifiersWithCompletion:]_block_invoke
+ ___49+[IntlUtility _setPreferredLanguage:forBundleID:]_block_invoke
+ ___55+[IntlUtility perAppLanguageSelectionBundleIdentifiers]_block_invoke
+ ___70+[IntlUtility perAppLanguageSelectionBundleIdentifiersWithCompletion:]_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSArray"8lr32l8
+ ___block_descriptor_48_e8_32bs_e17_v16?0"NSError"8ls32l8
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
