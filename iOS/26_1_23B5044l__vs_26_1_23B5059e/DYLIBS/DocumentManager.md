## DocumentManager

> `/System/Library/PrivateFrameworks/DocumentManager.framework/DocumentManager`

```diff

-367.1.2.1.0
-  __TEXT.__text: 0x351f4
+367.1.5.0.0
+  __TEXT.__text: 0x35500
   __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x2dd4
+  __TEXT.__objc_methlist: 0x2e04
   __TEXT.__const: 0x180
-  __TEXT.__cstring: 0x4c31
+  __TEXT.__cstring: 0x4c45
   __TEXT.__ustring: 0x6a2
-  __TEXT.__oslogstring: 0x313f
+  __TEXT.__oslogstring: 0x3175
   __TEXT.__gcc_except_tab: 0xa74
-  __TEXT.__unwind_info: 0xdc0
-  __TEXT.__objc_classname: 0x789
-  __TEXT.__objc_methname: 0xac2f
-  __TEXT.__objc_methtype: 0x16ab
-  __TEXT.__objc_stubs: 0x7c20
+  __TEXT.__unwind_info: 0xdc8
+  __TEXT.__objc_classname: 0x787
+  __TEXT.__objc_methname: 0xace0
+  __TEXT.__objc_methtype: 0x16b6
+  __TEXT.__objc_stubs: 0x7cc0
   __DATA_CONST.__got: 0x638
   __DATA_CONST.__const: 0x1718
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a10
+  __DATA_CONST.__objc_selrefs: 0x2a38
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x468
   __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0x4120
-  __AUTH_CONST.__objc_const: 0x4578
+  __AUTH_CONST.__cfstring: 0x4140
+  __AUTH_CONST.__objc_const: 0x45a8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x28c
+  __DATA.__objc_ivar: 0x290
   __DATA.__data: 0x950
   __DATA.__bss: 0xd0
   __DATA_DIRTY.__objc_data: 0x320

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: ED46F970-872F-3355-ADCD-696A0D0A6F44
-  Functions: 1239
-  Symbols:   4778
-  CStrings:  3284
+  UUID: EAA2C728-E98C-3167-87C2-7490AABE84A6
+  Functions: 1244
+  Symbols:   4794
+  CStrings:  3295
 
Symbols:
+ -[DOCSmartFolderDatabase _acquireBackgroundAssertionWithReason:]
+ -[DOCSmartFolderDatabase _acquireBackgroundAssertionWithReason:].cold.1
+ -[DOCSmartFolderDatabase _relinquishBackgroundAssertionWithReason:]
+ -[DOCSmartFolderDatabase batchingAssertion]
+ -[DOCSmartFolderDatabase openAssertion]
+ -[DOCSmartFolderDatabase setBatchingAssertion:]
+ -[DOCSmartFolderDatabase setOpenAssertion:]
+ GCC_except_table60
+ GCC_except_table76
+ _OBJC_IVAR_$_DOCSmartFolderDatabase._batchingAssertion
+ _OBJC_IVAR_$_DOCSmartFolderDatabase._openAssertion
+ ___48-[DOCSmartFolderDatabase _setUpDatabaseWatcher:]_block_invoke.184
+ ___48-[DOCSmartFolderDatabase _setUpDatabaseWatcher:]_block_invoke.184.cold.1
+ ___48-[DOCSmartFolderDatabase _setUpDatabaseWatcher:]_block_invoke.185
+ ___48-[DOCSmartFolderDatabase _setUpDatabaseWatcher:]_block_invoke.185.cold.1
+ ___48-[DOCSmartFolderDatabase _setUpDatabaseWatcher:]_block_invoke.186
+ ___57-[DOCSmartFolderDatabase _openConnectionToDatabaseAtURL:]_block_invoke.171
+ ___57-[DOCSmartFolderDatabase _openConnectionToDatabaseAtURL:]_block_invoke.171.cold.1
+ ___61-[DOCSmartFolderDatabase _createDatabaseIfNeededAtURL:error:]_block_invoke.179
+ _objc_msgSend$_acquireBackgroundAssertionWithReason:
+ _objc_msgSend$_relinquishBackgroundAssertionWithReason:
+ _objc_msgSend$batchingAssertion
+ _objc_msgSend$isValid
+ _objc_msgSend$openAssertion
+ _objc_msgSend$setBatchingAssertion:
+ _objc_msgSend$setOpenAssertion:
- -[DOCSmartFolderDatabase processAssertion]
- -[DOCSmartFolderDatabase setProcessAssertion:]
- GCC_except_table57
- GCC_except_table73
- _OBJC_IVAR_$_DOCSmartFolderDatabase._processAssertion
- ___48-[DOCSmartFolderDatabase _setUpDatabaseWatcher:]_block_invoke.180
- ___48-[DOCSmartFolderDatabase _setUpDatabaseWatcher:]_block_invoke.180.cold.1
- ___48-[DOCSmartFolderDatabase _setUpDatabaseWatcher:]_block_invoke.181
- ___48-[DOCSmartFolderDatabase _setUpDatabaseWatcher:]_block_invoke.181.cold.1
- ___48-[DOCSmartFolderDatabase _setUpDatabaseWatcher:]_block_invoke.182
- ___48-[DOCSmartFolderDatabase _setUpDatabaseWatcher:]_block_invoke.cold.3
- ___57-[DOCSmartFolderDatabase _openConnectionToDatabaseAtURL:]_block_invoke.cold.1
- ___61-[DOCSmartFolderDatabase _createDatabaseIfNeededAtURL:error:]_block_invoke.162
- _objc_msgSend$processAssertion
- _objc_msgSend$setProcessAssertion:
CStrings:
+ "B24@0:8Q16"
+ "Failed to acquire background assertion with name %@: %@"
+ "Open SQL Connection"
+ "T@\"RBSAssertion\",&,N,V_batchingAssertion"
+ "T@\"RBSAssertion\",&,N,V_openAssertion"
+ "_acquireBackgroundAssertionWithReason:"
+ "_batchingAssertion"
+ "_openAssertion"
+ "_relinquishBackgroundAssertionWithReason:"
+ "already acquired background %@ assertion"
+ "batchingAssertion"
+ "isValid"
+ "openAssertion"
+ "setBatchingAssertion:"
+ "setOpenAssertion:"
- "Failed to acquire background assertion: %@"
- "T@\"RBSAssertion\",&,N,V_processAssertion"
- "_processAssertion"
- "processAssertion"
- "setProcessAssertion:"

```
