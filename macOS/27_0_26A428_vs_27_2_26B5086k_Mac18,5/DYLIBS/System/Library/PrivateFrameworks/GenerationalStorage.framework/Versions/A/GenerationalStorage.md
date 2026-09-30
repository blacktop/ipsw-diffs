## GenerationalStorage

> `/System/Library/PrivateFrameworks/GenerationalStorage.framework/Versions/A/GenerationalStorage`

```diff

-405.0.0.0.1
-  __TEXT.__text: 0x1a598
+411.0.0.0.0
+  __TEXT.__text: 0x1a4fc
   __TEXT.__objc_methlist: 0xe14
-  __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x15e4
+  __TEXT.__const: 0x148
+  __TEXT.__cstring: 0x15c7
   __TEXT.__gcc_except_tab: 0x4f4
   __TEXT.__oslogstring: 0x864
-  __TEXT.__unwind_info: 0x888
+  __TEXT.__unwind_info: 0x880
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x938
+  __DATA_CONST.__objc_selrefs: 0x940
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__got: 0x188
   __AUTH_CONST.__const: 0x7c0
-  __AUTH_CONST.__cfstring: 0x1480
+  __AUTH_CONST.__cfstring: 0x1460
   __AUTH_CONST.__objc_const: 0x18f8
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__auth_got: 0x4d8
+  __AUTH_CONST.__auth_got: 0x4d0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0xec
   __DATA.__data: 0x300

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 504
-  Symbols:   1244
-  CStrings:  264
+  Functions: 505
+  Symbols:   1245
+  CStrings:  262
 
Symbols:
+ -[_CopyfileCallbackCtx doArchiveWithOwnerUID]
+ -[_CopyfileCallbackCtx setDoArchiveWithOwnerUID:]
+ OBJC_IVAR_$__CopyfileCallbackCtx._doArchiveWithOwnerUID
+ _GSCloneTree
+ _objc_msgSend$doArchiveWithOwnerUID
+ _objc_msgSend$setDoArchiveWithOwnerUID:
+ _objc_msgSend$unsignedIntValue
- -[_CopyfileCallbackCtx doArchive]
- -[_CopyfileCallbackCtx setDoArchive:]
- OBJC_IVAR_$__CopyfileCallbackCtx._doArchive
- _objc_msgSend$doArchive
- _objc_msgSend$setDoArchive:
- _unlink
CStrings:
+ "\"%s\" is not owned by the caller"
- "%s_XXXXXX"
- "stat(%s) failed"
- "temporary path \"%s_XXXXXX\" too long"
```
