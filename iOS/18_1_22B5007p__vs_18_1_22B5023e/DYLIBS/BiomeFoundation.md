## BiomeFoundation

> `/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation`

```diff

-153.2.0.1.0
-  __TEXT.__text: 0x2b554
+153.5.0.2.0
+  __TEXT.__text: 0x2a9e0
   __TEXT.__auth_stubs: 0xba0
-  __TEXT.__objc_methlist: 0x1ca4
-  __TEXT.__const: 0x198
-  __TEXT.__cstring: 0x4283
-  __TEXT.__oslogstring: 0x2a82
-  __TEXT.__gcc_except_tab: 0xba4
+  __TEXT.__objc_methlist: 0x1ccc
+  __TEXT.__const: 0x170
+  __TEXT.__cstring: 0x428a
+  __TEXT.__oslogstring: 0x2946
+  __TEXT.__gcc_except_tab: 0xbc8
   __TEXT.__dlopen_cstrs: 0x1b6
-  __TEXT.__unwind_info: 0xac0
-  __TEXT.__objc_classname: 0x4bd
-  __TEXT.__objc_methname: 0x43e8
-  __TEXT.__objc_methtype: 0xd91
-  __TEXT.__objc_stubs: 0x3ac0
+  __TEXT.__unwind_info: 0xad0
+  __TEXT.__objc_classname: 0x4c7
+  __TEXT.__objc_methname: 0x442c
+  __TEXT.__objc_methtype: 0xdc5
+  __TEXT.__objc_stubs: 0x3b00
   __DATA_CONST.__got: 0x2f8
-  __DATA_CONST.__const: 0x9f0
+  __DATA_CONST.__const: 0xa18
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12e0
+  __DATA_CONST.__objc_selrefs: 0x12f8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x1298
   __AUTH_CONST.__auth_got: 0x5e0
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x4ba0
-  __AUTH_CONST.__objc_const: 0x55d0
+  __AUTH_CONST.__cfstring: 0x4c60
+  __AUTH_CONST.__objc_const: 0x5630
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x208
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x1dc
   __DATA.__data: 0x4f8
-  __DATA.__bss: 0x120
+  __DATA.__bss: 0xf0
   __DATA_DIRTY.__objc_data: 0xbe0
   __DATA_DIRTY.__data: 0x1b0
-  __DATA_DIRTY.__bss: 0xd0
+  __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 920
-  Symbols:   1384
-  CStrings:  1917
+  Functions: 923
+  Symbols:   1393
+  CStrings:  1920
 
CStrings:
+ "BMAccessClient.removeResource:"
+ "Can't remove folder at %!@(MISSING) with error %!@(MISSING), isUnlocked: %!h(MISSING)hd"
+ "Deletions"
+ "Discoverability.Signals"
+ "Evaluating %!{(MISSING)public}@ request for removal of %!{(MISSING)public}@"
+ "Failed entitlement check, will not perform deletion"
+ "Failed to clean up directory"
+ "Failed to determine path, will not perform deletion"
+ "Invalid process type"
+ "Invalid resource type"
+ "Successfully removed folder at %!@(MISSING)"
+ "Successfully removed path: %!@(MISSING) for resource: %!@(MISSING)"
+ "Utilizing temporary exception to allow %!@(MISSING) access to Biome"
+ "Utilizing temporary exception to allow %!{(MISSING)public}@ access to %!{(MISSING)public}@"
+ "_removeDirectoryAtPath:"
+ "com.apple.activitysharingd"
+ "com.apple.camera"
+ "removeResource:error:"
+ "removeResource:reply:"
+ "v20@?0B8@\"NSError\"12"
+ "v32@0:8@\"BMResourceSpecifier\"16@?<v@?B@\"NSError\">24"
- "/Library/Caches/com.apple.xbs/Sources/Biome/BiomeFoundation/BiomeFoundation/Filesystem/BMFilesystem.m"
- "F_GETPATH"
- "F_GETPROTECTIONCLASS"
- "F_SETPROTECTIONCLASS"
- "close(%!d(MISSING)) -> %!d(MISSING), %!{(MISSING)darwin.errno}d (%!s(MISSING):%!d(MISSING))"
- "fclonefileat(%!d(MISSING), %!d(MISSING), \"%!s(MISSING)\", ...) -> %!d(MISSING), %!{(MISSING)darwin.errno}d (%!s(MISSING):%!d(MISSING))\n"
- "fcntl(%!d(MISSING), %!s(MISSING), ...) -> %!d(MISSING), %!{(MISSING)darwin.errno}d (%!s(MISSING):%!d(MISSING))\n"
- "fcopyfile(%!d(MISSING), %!d(MISSING), ...) -> %!d(MISSING), %!{(MISSING)darwin.errno}d (%!s(MISSING):%!d(MISSING))\n"
- "fstat(%!d(MISSING), ...) -> %!d(MISSING), %!{(MISSING)darwin.errno}d (%!s(MISSING):%!d(MISSING))\n"
- "fstatfs(%!d(MISSING), ...) -> %!d(MISSING), %!{(MISSING)darwin.errno}d (%!s(MISSING):%!d(MISSING))\n"
- "lseek(%!d(MISSING), ...) -> %!l(MISSING)ld, %!{(MISSING)darwin.errno}d (%!s(MISSING):%!d(MISSING))\n"
- "mkdirat(%!d(MISSING), \"%!s(MISSING)\", ...) -> %!d(MISSING), %!{(MISSING)darwin.errno}d (%!s(MISSING):%!d(MISSING))\n"
- "mkostempsat_np(%!d(MISSING), \"%!s(MISSING)\", ...) -> %!d(MISSING), %!{(MISSING)darwin.errno}d (%!s(MISSING):%!d(MISSING))\n"
- "mktemp(%!s(MISSING)) -> %!d(MISSING), %!{(MISSING)darwin.errno}d (%!s(MISSING):%!d(MISSING))\n"
- "openat(%!d(MISSING), \"%!s(MISSING)\", 0x%!x(MISSING), ...) -> %!d(MISSING), %!{(MISSING)darwin.errno}d (%!s(MISSING):%!d(MISSING))\n"
- "openat_dprotected_np(%!d(MISSING), \"%!s(MISSING)\", ...) -> %!d(MISSING), %!{(MISSING)darwin.errno}d (%!s(MISSING):%!d(MISSING))\n"
- "renameat(%!d(MISSING), \"%!s(MISSING)\", %!d(MISSING), \"%!s(MISSING)\") -> %!d(MISSING), %!{(MISSING)darwin.errno}d (%!s(MISSING):%!d(MISSING))\n"
- "unlinkat(%!d(MISSING), \"%!s(MISSING)\", ...) -> %!d(MISSING), %!{(MISSING)darwin.errno}d (%!s(MISSING):%!d(MISSING))\n"

```
