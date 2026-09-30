## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`

```diff

-623.1.13.10.3
-  __TEXT.__text: 0x13ab44
+623.1.14.10.6
+  __TEXT.__text: 0x13ae10
   __TEXT.__auth_stubs: 0x3180
-  __TEXT.__objc_methlist: 0xbcfc
+  __TEXT.__objc_methlist: 0xbd0c
   __TEXT.__const: 0x33b0
-  __TEXT.__gcc_except_tab: 0x6f04
+  __TEXT.__gcc_except_tab: 0x6ef8
   __TEXT.__cstring: 0x136b5
   __TEXT.__ustring: 0x2810
-  __TEXT.__oslogstring: 0xaa1d
+  __TEXT.__oslogstring: 0xaaad
   __TEXT.__dlopen_cstrs: 0x157
   __TEXT.__swift5_typeref: 0x100f
   __TEXT.__swift5_fieldmd: 0x964

   __TEXT.__swift_as_entry: 0xf8
   __TEXT.__swift_as_ret: 0xe0
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x6768
+  __TEXT.__unwind_info: 0x6780
   __TEXT.__eh_frame: 0x35c0
   __TEXT.__objc_classname: 0x1a78
-  __TEXT.__objc_methname: 0x253c3
+  __TEXT.__objc_methname: 0x253cc
   __TEXT.__objc_methtype: 0x4020
-  __TEXT.__objc_stubs: 0x12080
+  __TEXT.__objc_stubs: 0x12060
   __DATA_CONST.__got: 0xe68
   __DATA_CONST.__const: 0x4fb0
   __DATA_CONST.__objc_classlist: 0x608

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 574F156C-174A-3A25-8714-2C79A9343052
-  Functions: 7813
-  Symbols:   20834
-  CStrings:  13120
+  UUID: 6755CF2A-9912-3EF9-982D-688E5BAA28E3
+  Functions: 7818
+  Symbols:   20843
+  CStrings:  13121
 
Symbols:
+ -[WBSSavedAccountStore _loadSavedAccountsWithPasskeysFromPasskeyData:forGroupID:fromRecentlyDeleted:withDictionaryForSavedAccountsWithPasskeys:].cold.3
+ -[WBSSavedAccountStore test_loadSavedAccountsWithPasskeysFromPasskeyData:]
+ GCC_except_table308
+ GCC_except_table368
+ GCC_except_table370
+ GCC_except_table375
+ GCC_except_table381
+ ___144-[WBSSavedAccountStore _loadSavedAccountsWithPasskeysFromPasskeyData:forGroupID:fromRecentlyDeleted:withDictionaryForSavedAccountsWithPasskeys:]_block_invoke
+ ___74-[WBSSavedAccountStore test_loadSavedAccountsWithPasskeysFromPasskeyData:]_block_invoke
+ ___block_literal_global.863
+ ___block_literal_global.940
+ ___block_literal_global.946
- GCC_except_table161
- GCC_except_table265
- GCC_except_table272
- GCC_except_table307
- GCC_except_table380
- ___block_literal_global.862
- ___block_literal_global.939
- ___block_literal_global.945
- _objc_msgSend$precomposedStringWithCompatibilityMapping
CStrings:
+ "Found passkey with same RPID, user handle and credential ID as another passkey that has already been loaded in the account store. Dropping it."
+ "test_loadSavedAccountsWithPasskeysFromPasskeyData:"
- "precomposedStringWithCompatibilityMapping"

```
