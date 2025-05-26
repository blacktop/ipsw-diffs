## CoreRecents

> `/System/Library/PrivateFrameworks/CoreRecents.framework/CoreRecents`

```diff

-1209.0.0.0.0
-  __TEXT.__text: 0x7b08
-  __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__objc_methlist: 0xbe8
-  __TEXT.__cstring: 0x92d
+1210.0.0.0.0
+  __TEXT.__text: 0x7b44
+  __TEXT.__auth_stubs: 0x4d0
+  __TEXT.__objc_methlist: 0xbf0
+  __TEXT.__cstring: 0x922
   __TEXT.__const: 0x90
   __TEXT.__gcc_except_tab: 0x4c
   __TEXT.__oslogstring: 0x2b5
-  __TEXT.__unwind_info: 0x314
+  __TEXT.__unwind_info: 0x318
   __TEXT.__objc_classname: 0x151
-  __TEXT.__objc_methname: 0x2431
+  __TEXT.__objc_methname: 0x2457
   __TEXT.__objc_methtype: 0x69f
-  __TEXT.__objc_stubs: 0x1d60
+  __TEXT.__objc_stubs: 0x1d80
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x650
   __DATA_CONST.__objc_classlist: 0x58

   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xcf0
-  __DATA_CONST.__objc_selrefs: 0xa00
+  __DATA_CONST.__objc_selrefs: 0xa10
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__cfstring: 0xc20
-  __AUTH_CONST.__auth_got: 0x270
+  __AUTH_CONST.__cfstring: 0xca0
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__auth_got: 0x278
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x148
   __DATA.__objc_superrefs: 0x48
   __DATA.__objc_ivar: 0x90
   __DATA.__data: 0x198
-  __DATA_DIRTY.__const: 0x300
+  __DATA_DIRTY.__const: 0x2a0
   __DATA_DIRTY.__objc_const: 0x7a0
   __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__bss: 0xa8

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 287
-  Symbols:   1234
-  CStrings:  676
+  Functions: 288
+  Symbols:   1238
+  CStrings:  681
 
Symbols:
+ -[CRRecentContact appendSanitizedDescriptionTo:]
+ GCC_except_table11
+ _NSStringFromClass
+ ___block_literal_global.305
+ ___block_literal_global.308
+ ___block_literal_global.321
+ _objc_msgSend$appendSanitizedDescriptionTo:
+ _objc_msgSend$string
- GCC_except_table10
- ___block_literal_global.297
- ___block_literal_global.300
- ___block_literal_global.313
- _objc_msgSend$sanitizedDescription
CStrings:
+ " %@ <%@:%@>"
+ " cid=%lld"
+ " cid=<null-contact-id>"
+ " isGroup=%s"
+ " metadata-keys=%lu"
+ " rid=%lld"
+ " rid=<null-recent-id>"
+ "<%@ %p"
+ ">"
+ "appendSanitizedDescriptionTo:"
+ "string"
- "%@, %@ <%@:%@>"
- "%lld"
- "<%@: %p> (rid=%@) (cid=%@) dates={%@}, %lu metadata key%s, isGroup=%s"
- "<null-contact-id>"
- "<null-recent-id>"
- "s"

```
