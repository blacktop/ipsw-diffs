## DocumentManagerCore

> `/System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore`

```diff

-367.1.2.1.0
-  __TEXT.__text: 0x47b24
+367.1.5.0.0
+  __TEXT.__text: 0x480f4
   __TEXT.__auth_stubs: 0x10e0
-  __TEXT.__objc_methlist: 0x3ad8
+  __TEXT.__objc_methlist: 0x3b50
   __TEXT.__const: 0x6e8
-  __TEXT.__gcc_except_tab: 0x74c
-  __TEXT.__cstring: 0x4e8a
-  __TEXT.__oslogstring: 0x3922
+  __TEXT.__gcc_except_tab: 0x754
+  __TEXT.__cstring: 0x4e9a
+  __TEXT.__oslogstring: 0x3982
   __TEXT.__ustring: 0x10c
   __TEXT.__swift5_typeref: 0x438
   __TEXT.__constg_swiftt: 0xbc

   __TEXT.__swift5_proto: 0x5c
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_capture: 0x84
-  __TEXT.__unwind_info: 0x12d8
+  __TEXT.__unwind_info: 0x12d0
   __TEXT.__eh_frame: 0x2c0
   __TEXT.__objc_classname: 0x5bd
-  __TEXT.__objc_methname: 0x98e1
-  __TEXT.__objc_methtype: 0xe48
-  __TEXT.__objc_stubs: 0x65e0
+  __TEXT.__objc_methname: 0x9934
+  __TEXT.__objc_methtype: 0xe66
+  __TEXT.__objc_stubs: 0x6620
   __DATA_CONST.__got: 0x600
-  __DATA_CONST.__const: 0x15d8
+  __DATA_CONST.__const: 0x15b8
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26a0
+  __DATA_CONST.__objc_selrefs: 0x26b8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x880
-  __AUTH_CONST.__const: 0xba0
-  __AUTH_CONST.__cfstring: 0x2fa0
-  __AUTH_CONST.__objc_const: 0x6188
+  __AUTH_CONST.__const: 0xb80
+  __AUTH_CONST.__cfstring: 0x2fc0
+  __AUTH_CONST.__objc_const: 0x6210
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x448

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F5F107C3-9A03-39D3-A921-D629A344BABA
-  Functions: 1835
-  Symbols:   5273
-  CStrings:  3102
+  UUID: AAD8AD4C-3362-32E2-8EC6-4F6D87996251
+  Functions: 1841
+  Symbols:   5285
+  CStrings:  3111
 
Symbols:
+ +[DOCAXIdentifier tagDotButtonIdentifier]
+ -[FINode(DOCNode) cachedDomain:]
+ -[FINode(DOCNode) isInTrash]
+ -[FINode(DOCNode) simplifiedFolderIcon]
+ -[FPItem(DOCNode) cachedDomain:]
+ -[FPItem(DOCNode) cachedDomain:].cold.1
+ -[FPItem(DOCNode) isInTrash]
+ -[FPItem(DOCNode) simplifiedFolderIcon]
+ GCC_except_table150
+ ___88+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:]_block_invoke.7
+ ___88+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:]_block_invoke.7.cold.1
+ ___block_literal_global.384
+ _objc_msgSend$cachedDomain:
+ _objc_msgSend$isAnyParentTrashed
+ _objc_msgSend$simplifiedFolderIcon
- -[FINode(DOCNode) cachedDomain].cold.1
- GCC_except_table140
- ___29-[FPItem(DOCNode) folderIcon]_block_invoke
- ___88+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:]_block_invoke.5
- ___88+[DOCRenameSupport _spi_renameDocumentAtURL:proposedName:synchronous:completionHandler:]_block_invoke.5.cold.1
- ___block_descriptor_32_e27_v24?0"NSURL"8"NSError"16l
- ___block_literal_global.379
- ___block_literal_global.98
- _objc_msgSend$nodeIsAll:
CStrings:
+ "@\"FPProviderDomain\"24@0:8^@16"
+ "Error getting domain for node %{public}@ from domainID: %{public}@, domain error: %{public}@"
+ "Error getting domain from FPItem: %{public}@ error: %{public}@"
+ "TB,R,N,GisInTrash"
+ "cachedDomain:"
+ "inTrash"
+ "isInTrash"
+ "simplifiedFolderIcon"
+ "tag-dot-button"
+ "tagDotButtonIdentifier"
- "Error getting domain from domainID: %@, domain error: %@"
- "nodeIsAll:"

```
