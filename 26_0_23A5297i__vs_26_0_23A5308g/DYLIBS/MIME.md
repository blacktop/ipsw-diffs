## MIME

> `/System/Library/PrivateFrameworks/MIME.framework/MIME`

```diff

-3860.100.5.2.1
-  __TEXT.__text: 0x33e4c
+3863.100.1.2.5
+  __TEXT.__text: 0x342e8
   __TEXT.__auth_stubs: 0x10e0
-  __TEXT.__objc_methlist: 0x31e4
-  __TEXT.__gcc_except_tab: 0x41a0
+  __TEXT.__objc_methlist: 0x31fc
+  __TEXT.__gcc_except_tab: 0x4234
   __TEXT.__const: 0x7f1
-  __TEXT.__cstring: 0x29ef
-  __TEXT.__oslogstring: 0x114e
+  __TEXT.__cstring: 0x29fa
+  __TEXT.__oslogstring: 0x1213
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1a58
+  __TEXT.__unwind_info: 0x1a60
   __TEXT.__objc_classname: 0x6a8
-  __TEXT.__objc_methname: 0x64ff
+  __TEXT.__objc_methname: 0x6526
   __TEXT.__objc_methtype: 0xd60
-  __TEXT.__objc_stubs: 0x5980
+  __TEXT.__objc_stubs: 0x59c0
   __DATA_CONST.__got: 0x4b0
   __DATA_CONST.__const: 0xd20
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f28
+  __DATA_CONST.__objc_selrefs: 0x1f38
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0xa8
   __AUTH_CONST.__auth_got: 0x888
-  __AUTH_CONST.__const: 0x588
+  __AUTH_CONST.__const: 0x5a8
   __AUTH_CONST.__cfstring: 0x3780
   __AUTH_CONST.__objc_const: 0x4390
   __AUTH_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_ivar: 0x290
   __DATA.__data: 0x6d0
-  __DATA.__bss: 0x98
+  __DATA.__bss: 0xa8
   __DATA_DIRTY.__objc_data: 0xe10
   __DATA_DIRTY.__data: 0x130
   __DATA_DIRTY.__common: 0x18

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 88E2B993-BE21-39E7-AA41-C978D949E710
-  Functions: 1199
-  Symbols:   4678
-  CStrings:  2577
+  UUID: 24E30192-AF51-3F90-AE87-A2A7129AD8E7
+  Functions: 1206
+  Symbols:   4696
+  CStrings:  2583
 
Symbols:
+ -[MFMimeBody hasEncryptedDescendantPart].cold.1
+ -[MFMimeBody hasEncryptedDescendantPart].cold.2
+ -[MFMimePart isDetatchedSignature]
+ -[MFMimePart isMultipartSigned]
+ ____ef_log_MFMimeBody_block_invoke
+ ___block_literal_global.715
+ ___block_literal_global.740
+ __ef_log_MFMimeBody
+ __ef_log_MFMimeBody.cold.1
+ __ef_log_MFMimeBody.log
+ __ef_log_MFMimeBody.onceToken
+ _objc_msgSend$isDetatchedSignature
+ _objc_msgSend$isMultipartSigned
- ___block_literal_global.713
- ___block_literal_global.738
CStrings:
+ "Error: Multipart Signed had more than one Encrypted part"
+ "Error: Multipart Signed should have exactly 2 direct children, here the count is %lu"
+ "Fetched body data of length %lu for message %{public}@"
+ "isDetatchedSignature"
+ "isMultipartSigned"

```
