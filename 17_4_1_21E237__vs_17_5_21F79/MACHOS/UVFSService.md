## UVFSService

> `/System/Library/PrivateFrameworks/UVFSXPCService.framework/XPCServices/UVFSService.xpc/UVFSService`

```diff

-663.100.13.0.0
-  __TEXT.__text: 0x287e8
+663.122.1.0.0
+  __TEXT.__text: 0x28d60
   __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_stubs: 0x32c0
+  __TEXT.__objc_stubs: 0x32e0
   __TEXT.__objc_methlist: 0x1334
-  __TEXT.__cstring: 0x11e7
+  __TEXT.__cstring: 0x1283
   __TEXT.__objc_classname: 0x1fe
-  __TEXT.__objc_methname: 0x4443
+  __TEXT.__objc_methname: 0x446b
   __TEXT.__objc_methtype: 0x15c1
-  __TEXT.__oslogstring: 0x48c7
+  __TEXT.__oslogstring: 0x4952
   __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0x93c
-  __TEXT.__unwind_info: 0x610
+  __TEXT.__unwind_info: 0x60c
   __DATA_CONST.__auth_got: 0x4c8
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x760

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x2bb0
-  __DATA.__objc_selrefs: 0x1030
+  __DATA.__objc_selrefs: 0x1038
   __DATA.__objc_ivar: 0x1b0
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x278

   - /System/Library/PrivateFrameworks/LiveFS.framework/LiveFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 864
+  Functions: 871
   Symbols:   296
-  CStrings:  1553
+  CStrings:  1560
 
CStrings:
+ "%s: called with invalid name:%@"
+ "%s: called with invalid name:%@:node:%@"
+ "-[userFSVolume insertIntoNameCache:withParent:withName:]"
+ "-[userFSVolume lookupWithParent:andName:]"
+ "-[userFSVolume removeFromNameCache:withParent:withName:]"
+ "getFileSystemRepresentation:maxLength:"
+ "pathToStringNode:node:%@name:%@, failed to get UTF8 representation"

```
