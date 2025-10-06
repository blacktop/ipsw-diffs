## StorageKit

> `/System/Library/PrivateFrameworks/StorageKit.framework/StorageKit`

```diff

-854.100.13.0.0
-  __TEXT.__text: 0x28610
-  __TEXT.__auth_stubs: 0xba0
-  __TEXT.__objc_methlist: 0x2870
+854.120.9.0.0
+  __TEXT.__text: 0x28650
+  __TEXT.__auth_stubs: 0xb90
+  __TEXT.__objc_methlist: 0x2890
   __TEXT.__oslogstring: 0x1093
   __TEXT.__cstring: 0x299c
   __TEXT.__const: 0xaa

   __TEXT.__swift5_types: 0x8
   __TEXT.__unwind_info: 0xac8
   __TEXT.__objc_classname: 0x505
-  __TEXT.__objc_methname: 0x5c02
-  __TEXT.__objc_methtype: 0xded
-  __TEXT.__objc_stubs: 0x55a0
+  __TEXT.__objc_methname: 0x5c32
+  __TEXT.__objc_methtype: 0xd72
+  __TEXT.__objc_stubs: 0x55c0
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__const: 0x7f8
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x58d8
-  __DATA_CONST.__objc_selrefs: 0x1938
+  __DATA_CONST.__objc_const: 0x5918
+  __DATA_CONST.__objc_selrefs: 0x1950
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_classrefs: 0x288
   __DATA_CONST.__objc_superrefs: 0xf8

   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x5e0
+  __AUTH_CONST.__auth_got: 0x5d8
   __AUTH.__objc_data: 0xce8
-  __DATA.__objc_ivar: 0x2f8
+  __DATA.__objc_ivar: 0x2fc
   __DATA.__objc_data: 0x20
   __DATA.__data: 0xa88
   __DATA.__bss: 0x78

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
-  UUID: F9DB96DE-5875-3F9A-BCB1-9CE851DE3DE7
-  Functions: 1033
-  Symbols:   3959
-  CStrings:  2383
+  UUID: 43135DA0-B3B0-3A30-BE30-311D8D0C5C9E
+  Functions: 1036
+  Symbols:   3966
+  CStrings:  2385
 
Symbols:
+ -[SKDisk isRemovable]
+ -[SKDisk isTrusted]
+ -[SKDisk setIsRemovable:]
+ -[SKHelperClient mountDisk:options:blocking:completionBlock:]
+ -[SKHelperClient mountDisk:options:completionBlock:]
+ _OBJC_IVAR_$_SKDisk._isRemovable
+ ___61-[SKHelperClient mountDisk:options:blocking:completionBlock:]_block_invoke
+ ___61-[SKHelperClient mountDisk:options:blocking:completionBlock:]_block_invoke_2
+ _objc_msgSend$isRemovable
+ _objc_msgSend$mountDisk:options:blocking:completionBlock:
+ _objc_msgSend$mountDisk:options:completionBlock:
- -[SKHelperClient mountDisk:options:connection:blocking:completionBlock:]
- -[SKHelperClient mountDisk:options:connection:completionBlock:]
- GCC_except_table21
- ___72-[SKHelperClient mountDisk:options:connection:blocking:completionBlock:]_block_invoke
- ___72-[SKHelperClient mountDisk:options:connection:blocking:completionBlock:]_block_invoke_2
- _objc_msgSend$mountDisk:options:connection:blocking:completionBlock:
- _objc_msgSend$mountDisk:options:connection:completionBlock:
- _objc_retain_x6
CStrings:
+ "-[SKHelperClient mountDisk:options:blocking:completionBlock:]"
+ "TB,V_isRemovable"
+ "_isRemovable"
+ "isRemovable"
+ "isTrusted"
+ "mountDisk:options:blocking:completionBlock:"
+ "mountDisk:options:completionBlock:"
+ "setIsRemovable:"
- "-[SKHelperClient mountDisk:options:connection:blocking:completionBlock:]"
- "mountDisk:options:connection:blocking:completionBlock:"
- "mountDisk:options:connection:completionBlock:"
- "v48@0:8@\"SKDisk\"16@\"NSDictionary\"24@\"SKDaemonConnection\"32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v52@0:8@16@24@32B40@?44"

```
