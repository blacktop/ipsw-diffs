## GenerationalStorage

> `/System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage`

```diff

-405.0.0.0.1
-  __TEXT.__text: 0x16788
+411.0.0.0.0
+  __TEXT.__text: 0x166a4
   __TEXT.__objc_methlist: 0xd9c
-  __TEXT.__const: 0x148
-  __TEXT.__cstring: 0x12ba
+  __TEXT.__const: 0x140
+  __TEXT.__cstring: 0x129d
   __TEXT.__oslogstring: 0x7f6
   __TEXT.__gcc_except_tab: 0x4b8
-  __TEXT.__unwind_info: 0x7f0
+  __TEXT.__unwind_info: 0x7f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x928
+  __DATA_CONST.__objc_selrefs: 0x930
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__got: 0x190
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x1160
+  __AUTH_CONST.__cfstring: 0x1140
   __AUTH_CONST.__objc_const: 0x1730
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__auth_got: 0x4b0
+  __AUTH_CONST.__auth_got: 0x498
   __DATA.__objc_ivar: 0xe4
   __DATA.__data: 0x300
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 459
-  Symbols:   1129
-  CStrings:  236
+  Functions: 460
+  Symbols:   1128
+  CStrings:  234
 
Symbols:
+ -[_CopyfileCallbackCtx doArchiveWithOwnerUID]
+ -[_CopyfileCallbackCtx setDoArchiveWithOwnerUID:]
+ _GSCloneTree
+ _OBJC_IVAR_$__CopyfileCallbackCtx._doArchiveWithOwnerUID
+ _objc_msgSend$doArchiveWithOwnerUID
+ _objc_msgSend$setDoArchiveWithOwnerUID:
+ _objc_msgSend$unsignedIntValue
- -[_CopyfileCallbackCtx doArchive]
- -[_CopyfileCallbackCtx setDoArchive:]
- _OBJC_IVAR_$__CopyfileCallbackCtx._doArchive
- _objc_msgSend$doArchive
- _objc_msgSend$setDoArchive:
- _objc_release_x3
- _snprintf
- _unlink
CStrings:
+ "\"%s\" is not owned by the caller"
- "%s_XXXXXX"
- "stat(%s) failed"
- "temporary path \"%s_XXXXXX\" too long"
```
