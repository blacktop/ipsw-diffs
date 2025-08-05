## BiomeFoundation

> `/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation`

```diff

-198.0.0.0.0
-  __TEXT.__text: 0x3566c
+200.0.0.0.0
+  __TEXT.__text: 0x355d4
   __TEXT.__auth_stubs: 0xdc0
   __TEXT.__objc_methlist: 0x29a4
   __TEXT.__const: 0x22a
-  __TEXT.__cstring: 0x4f26
-  __TEXT.__oslogstring: 0x324e
-  __TEXT.__gcc_except_tab: 0xdc4
+  __TEXT.__cstring: 0x4f36
+  __TEXT.__oslogstring: 0x3209
+  __TEXT.__gcc_except_tab: 0xdb8
   __TEXT.__dlopen_cstrs: 0x2d4
   __TEXT.__constg_swiftt: 0x64
   __TEXT.__swift5_typeref: 0x21

   __TEXT.__swift5_types: 0x8
   __TEXT.__unwind_info: 0xe18
   __TEXT.__objc_classname: 0x669
-  __TEXT.__objc_methname: 0x59e6
+  __TEXT.__objc_methname: 0x59ad
   __TEXT.__objc_methtype: 0x10d9
-  __TEXT.__objc_stubs: 0x4880
+  __TEXT.__objc_stubs: 0x4860
   __DATA_CONST.__got: 0x380
   __DATA_CONST.__const: 0xc80
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1810
+  __DATA_CONST.__objc_selrefs: 0x1808
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x1328
   __AUTH_CONST.__auth_got: 0x6f0
   __AUTH_CONST.__const: 0x480
-  __AUTH_CONST.__cfstring: 0x56e0
-  __AUTH_CONST.__objc_const: 0x6890
+  __AUTH_CONST.__cfstring: 0x5700
+  __AUTH_CONST.__objc_const: 0x68a0
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x230
-  __AUTH.__objc_data: 0x3e0
+  __AUTH.__objc_data: 0x480
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x290
   __DATA.__data: 0x5b8
-  __DATA.__bss: 0x138
+  __DATA.__bss: 0x128
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0xe60
+  __DATA_DIRTY.__objc_data: 0xdc0
   __DATA_DIRTY.__data: 0x198
-  __DATA_DIRTY.__bss: 0x168
+  __DATA_DIRTY.__bss: 0x178
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 75067E67-B173-3281-B184-8982D9B7FAD2
+  UUID: 40E4404B-8E96-3A0A-AD19-B3CDF9B8D2B4
   Functions: 1201
-  Symbols:   4472
-  CStrings:  3014
+  Symbols:   4471
+  CStrings:  3013
 
Symbols:
+ -[BMAccessDescriptor personaIdentifier]
+ GCC_except_table31
+ _OBJC_IVAR_$_BMAccessDescriptor._personaIdentifier
- -[BMAccessAssertionCache _invalidateCacheIfPersonaSwitched]
- GCC_except_table29
- _OBJC_IVAR_$_BMAccessAssertionCache._lastPersonaIdentifier
- _objc_msgSend$_invalidateCacheIfPersonaSwitched
CStrings:
+ " as persona %@"
+ "<BMAccessDescriptor: %@ access to %@ in domain %lu%@>"
- "<BMAccessDescriptor: %@ access to %@ in domain %lu>"
- "Invalidating access assertion cache - persona switched from %@ to %@"
- "_invalidateCacheIfPersonaSwitched"
- "_lastPersonaIdentifier"

```
