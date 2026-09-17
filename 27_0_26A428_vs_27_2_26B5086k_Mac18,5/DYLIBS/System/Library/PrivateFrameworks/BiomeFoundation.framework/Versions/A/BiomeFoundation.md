## BiomeFoundation

> `/System/Library/PrivateFrameworks/BiomeFoundation.framework/Versions/A/BiomeFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-250.0.0.3.0
-  __TEXT.__text: 0x37c2c
-  __TEXT.__objc_methlist: 0x2aec
+255.0.2.0.0
+  __TEXT.__text: 0x37fb8
+  __TEXT.__objc_methlist: 0x2afc
   __TEXT.__const: 0x23a
   __TEXT.__cstring: 0x511d
-  __TEXT.__oslogstring: 0x350d
+  __TEXT.__oslogstring: 0x352d
   __TEXT.__gcc_except_tab: 0xe6c
   __TEXT.__dlopen_cstrs: 0x2d4
   __TEXT.__constg_swiftt: 0x64

   __TEXT.__swift5_reflstr: 0x2f
   __TEXT.__swift5_fieldmd: 0x44
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1310
+  __TEXT.__unwind_info: 0x1318
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1900
+  __DATA_CONST.__objc_selrefs: 0x1910
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x1408
   __DATA_CONST.__got: 0x388
   __AUTH_CONST.__const: 0xa80
-  __AUTH_CONST.__cfstring: 0x5a00
-  __AUTH_CONST.__objc_const: 0x6d50
+  __AUTH_CONST.__cfstring: 0x5a20
+  __AUTH_CONST.__objc_const: 0x6d60
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_arrayobj: 0x630
   __AUTH_CONST.__objc_dictobj: 0x1b8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1276
+  Functions: 1279
   Symbols:   2890
-  CStrings:  1084
+  CStrings:  1086
 
Symbols:
+ -[BMFileHandle isUnlinked]
+ -[BMFileManager removeFilesAtPaths:error:]
- GCC_except_table28
- GCC_except_table34
CStrings:
+ "Unable to remove %{public}@: %@"
+ "paths"
```
