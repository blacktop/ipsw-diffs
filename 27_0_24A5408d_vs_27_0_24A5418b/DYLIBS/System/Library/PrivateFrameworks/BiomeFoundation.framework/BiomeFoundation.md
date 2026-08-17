## BiomeFoundation

> `/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation`

```diff

-250.0.0.1.0
-  __TEXT.__text: 0x34808
-  __TEXT.__objc_methlist: 0x2a5c
+250.0.0.3.0
+  __TEXT.__text: 0x3485c
+  __TEXT.__objc_methlist: 0x2a64
   __TEXT.__const: 0x23a
   __TEXT.__cstring: 0x50cd
   __TEXT.__oslogstring: 0x33a2

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18b8
+  __DATA_CONST.__objc_selrefs: 0x18c0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x1348

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1228
-  Symbols:   2797
+  Functions: 1229
+  Symbols:   2799
   CStrings:  1060
 
Symbols:
+ +[BMVanillaContainer biomeDirectoryURLForContainerPath:]
+ _objc_msgSend$biomeDirectoryURLForContainerPath:
Functions:
~ -[BMResourceContainerManager _standardDataVaultContainerForResource:] : 140 -> 144
~ +[BMVanillaContainer containerForPersonaIdentifier:error:] : 684 -> 656
+ +[BMVanillaContainer biomeDirectoryURLForContainerPath:]
```
