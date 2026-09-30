## BiomeFoundation

> `/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation`

```diff

-250.0.0.3.0
-  __TEXT.__text: 0x3378c
-  __TEXT.__objc_methlist: 0x2a64
+255.0.2.0.0
+  __TEXT.__text: 0x33ae0
+  __TEXT.__objc_methlist: 0x2a74
   __TEXT.__const: 0x23a
-  __TEXT.__cstring: 0x50cd
-  __TEXT.__oslogstring: 0x33a2
+  __TEXT.__cstring: 0x50dd
+  __TEXT.__oslogstring: 0x33c2
   __TEXT.__gcc_except_tab: 0xdf4
   __TEXT.__dlopen_cstrs: 0x2d4
   __TEXT.__constg_swiftt: 0x64

   __TEXT.__swift5_reflstr: 0x2f
   __TEXT.__swift5_fieldmd: 0x44
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x12b8
+  __TEXT.__unwind_info: 0x12c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18c0
+  __DATA_CONST.__objc_selrefs: 0x18d0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x1348
   __DATA_CONST.__got: 0x388
   __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x58c0
-  __AUTH_CONST.__objc_const: 0x6c88
+  __AUTH_CONST.__cfstring: 0x58e0
+  __AUTH_CONST.__objc_const: 0x6c98
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_arrayobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x230

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1229
-  Symbols:   2799
-  CStrings:  1060
+  Functions: 1232
+  Symbols:   2803
+  CStrings:  1062
 
Symbols:
+ -[BMFileHandle isUnlinked]
+ -[BMFileManager removeFilesAtPaths:error:]
+ GCC_except_table22
+ GCC_except_table27
+ _objc_msgSend$privacyPathname:
- GCC_except_table15
Functions:
~ -[BMFileManager removeFileAtPath:error:] : 880 -> 912
+ -[BMFileHandle isUnlinked]
+ -[BMFileManager removeFilesAtPaths:error:]
+ -[BMFileManager removeFilesAtPaths:error:].cold.1
CStrings:
+ "Unable to remove %{public}@: %@"
+ "paths"
```
