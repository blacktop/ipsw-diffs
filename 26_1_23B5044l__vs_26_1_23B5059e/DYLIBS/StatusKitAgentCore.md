## StatusKitAgentCore

> `/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore`

```diff

-116.200.31.0.0
-  __TEXT.__text: 0xfff2c
+116.200.41.0.0
+  __TEXT.__text: 0x1004e0
   __TEXT.__auth_stubs: 0x1ce0
-  __TEXT.__objc_methlist: 0x7ffc
+  __TEXT.__objc_methlist: 0x8034
   __TEXT.__const: 0x1d60
-  __TEXT.__cstring: 0x4e91
-  __TEXT.__oslogstring: 0x12e6f
-  __TEXT.__gcc_except_tab: 0x1294
+  __TEXT.__cstring: 0x4ea1
+  __TEXT.__oslogstring: 0x12fcf
+  __TEXT.__gcc_except_tab: 0x12e8
   __TEXT.__swift5_typeref: 0x163e
   __TEXT.__constg_swiftt: 0x6d0
   __TEXT.__swift5_reflstr: 0x617

   __TEXT.__swift5_types: 0x88
   __TEXT.__swift_as_entry: 0x224
   __TEXT.__swift_as_ret: 0x204
-  __TEXT.__unwind_info: 0x3738
+  __TEXT.__unwind_info: 0x3748
   __TEXT.__eh_frame: 0x54f8
   __TEXT.__objc_classname: 0xed1
-  __TEXT.__objc_methname: 0x11c27
+  __TEXT.__objc_methname: 0x11c69
   __TEXT.__objc_methtype: 0x4a95
-  __TEXT.__objc_stubs: 0x9be0
+  __TEXT.__objc_stubs: 0x9c40
   __DATA_CONST.__got: 0x910
   __DATA_CONST.__const: 0x1ce0
   __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3510
+  __DATA_CONST.__objc_selrefs: 0x3528
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0xe80
   __AUTH_CONST.__const: 0x30d0
-  __AUTH_CONST.__cfstring: 0x24a0
-  __AUTH_CONST.__objc_const: 0xbcb8
+  __AUTH_CONST.__cfstring: 0x24c0
+  __AUTH_CONST.__objc_const: 0xbcc8
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x938
-  __AUTH.__data: 0xe8
+  __AUTH.__objc_data: 0x8a0
+  __AUTH.__data: 0xb8
   __DATA.__objc_ivar: 0x620
-  __DATA.__data: 0x1470
-  __DATA.__bss: 0x11c0
+  __DATA.__data: 0x1450
+  __DATA.__bss: 0x1140
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x1ed8
-  __DATA_DIRTY.__data: 0xb90
-  __DATA_DIRTY.__bss: 0xad0
+  __DATA_DIRTY.__objc_data: 0x1f70
+  __DATA_DIRTY.__data: 0xbd0
+  __DATA_DIRTY.__bss: 0xb50
   __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C384D5E0-5295-3583-8578-BE84D52B4915
-  Functions: 4851
-  Symbols:   15623
-  CStrings:  4893
+  UUID: 28BA6EF2-F2AF-39BD-B96C-E4C8AAEE50D5
+  Functions: 4855
+  Symbols:   15635
+  CStrings:  4903
 
Symbols:
+ -[SKADatabaseManager clearPersistentHistoryIfNeeded]
+ -[SKADatabaseProvider clearPersistentHistoryIfNeeded]
+ GCC_except_table46
+ ___48-[SKADatabaseProvider createPersistentContainer]_block_invoke.27
+ ___48-[SKADatabaseProvider createPersistentContainer]_block_invoke.27.cold.1
+ ___53-[SKADatabaseProvider clearPersistentHistoryIfNeeded]_block_invoke
+ ___53-[SKADatabaseProvider clearPersistentHistoryIfNeeded]_block_invoke.cold.1
+ ___76-[SKADatabaseProvider deviceToDeviceEncryptedDatabaseCapableWithCompletion:]_block_invoke.78
+ ___76-[SKADatabaseProvider deviceToDeviceEncryptedDatabaseCapableWithCompletion:]_block_invoke.78.cold.1
+ ___block_literal_global.96
+ _objc_msgSend$clearPersistentHistoryIfNeeded
+ _objc_msgSend$deleteHistoryBeforeDate:
+ _objc_msgSend$succeeded
- ___48-[SKADatabaseProvider createPersistentContainer]_block_invoke.24
- ___48-[SKADatabaseProvider createPersistentContainer]_block_invoke.24.cold.1
- ___76-[SKADatabaseProvider deviceToDeviceEncryptedDatabaseCapableWithCompletion:]_block_invoke.75
- ___76-[SKADatabaseProvider deviceToDeviceEncryptedDatabaseCapableWithCompletion:]_block_invoke.75.cold.1
- ___block_literal_global.92
CStrings:
+ "Attempting to clear persistent history before %@ (export date: %@)"
+ "Clearing persistent history before %@ failed with error: %@"
+ "Clearing persistent history before %@ succeeded with result: %@"
+ "Export completed, will clear persistent history before %@ in maintenance activity"
+ "No date found for last database export, will not clear persistent history"
+ "clearPersistentHistoryIfNeeded"
+ "deleteHistoryBeforeDate:"
+ "lastDatabaseExportDate"
+ "succeeded"

```
