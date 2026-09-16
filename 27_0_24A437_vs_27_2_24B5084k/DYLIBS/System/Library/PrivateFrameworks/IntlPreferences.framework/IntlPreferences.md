## IntlPreferences

> `/System/Library/PrivateFrameworks/IntlPreferences.framework/IntlPreferences`

```diff

-496.0.0.0.0
-  __TEXT.__text: 0x1ae50
-  __TEXT.__objc_methlist: 0x11bc
-  __TEXT.__const: 0x1f0
+498.0.0.0.0
+  __TEXT.__text: 0x1b5b8
+  __TEXT.__objc_methlist: 0x1204
+  __TEXT.__const: 0x200
   __TEXT.__cstring: 0x12e5
-  __TEXT.__oslogstring: 0xeca
-  __TEXT.__gcc_except_tab: 0x220
+  __TEXT.__oslogstring: 0xfec
+  __TEXT.__gcc_except_tab: 0x234
   __TEXT.__dlopen_cstrs: 0x20a
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x76
-  __TEXT.__unwind_info: 0x778
+  __TEXT.__unwind_info: 0x7a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x678
+  __DATA_CONST.__const: 0x6c8
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1098
+  __DATA_CONST.__objc_selrefs: 0x10c8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x300
-  __DATA_CONST.__got: 0x310
+  __DATA_CONST.__got: 0x320
   __AUTH_CONST.__const: 0x280
   __AUTH_CONST.__cfstring: 0x1a80
-  __AUTH_CONST.__objc_const: 0x1638
+  __AUTH_CONST.__objc_const: 0x1648
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x180

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 465
-  Symbols:   1410
-  CStrings:  335
+  Functions: 474
+  Symbols:   1423
+  CStrings:  338
 
Symbols:
+ +[IntlUtility _migratePerAppLanguageSelectionOutOfGlobalDomain]
+ +[IntlUtility _perAppLanguageSelectionBundleIdentifiersFromPrivateDomain]
+ +[IntlUtility _updatePerAppLanguageSelectionInPrivateDomainForBundleID:selected:]
+ +[IntlUtility perAppLanguageSelectionBundleIdentifiersWithCompletion:]
+ GCC_except_table107
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
