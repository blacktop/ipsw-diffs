## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/IconServices`

```diff

 793.1.10.0.0
-  __TEXT.__text: 0x6595c
+  __TEXT.__text: 0x65b88
   __TEXT.__delay_stubs: 0x80
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x6a44
-  __TEXT.__cstring: 0x464d
+  __TEXT.__objc_methlist: 0x6a74
+  __TEXT.__cstring: 0x467e
   __TEXT.__const: 0x8970
   __TEXT.__oslogstring: 0x3f95
   __TEXT.__gcc_except_tab: 0x6b8

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xa80
-  __DATA_CONST.__objc_classlist: 0x538
+  __DATA_CONST.__objc_classlist: 0x540
   __DATA_CONST.__objc_catlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3230
+  __DATA_CONST.__objc_selrefs: 0x3248
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x410
-  __DATA_CONST.__objc_arraydata: 0xb0
+  __DATA_CONST.__objc_arraydata: 0xc8
   __DATA_CONST.__got: 0x6b8
   __AUTH_CONST.__const: 0x11c8
-  __AUTH_CONST.__cfstring: 0x4a40
-  __AUTH_CONST.__objc_const: 0x14110
-  __AUTH_CONST.__objc_intobj: 0x558
-  __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH_CONST.__cfstring: 0x4a80
+  __AUTH_CONST.__objc_const: 0x141b0
+  __AUTH_CONST.__objc_intobj: 0x588
+  __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__auth_got: 0x808
-  __AUTH.__objc_data: 0x50
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x6e0
   __DATA.__data: 0x1cf0
   __DATA_DIRTY.__objc_data: 0x33e0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2637
-  Symbols:   5013
-  CStrings:  1096
+  Functions: 2640
+  Symbols:   5021
+  CStrings:  1099
 
Symbols:
+ -[ISDefaults isForceHomeAccessoryDeviceEnabled]
+ -[ISDeviceInfo isHomeAccessoryDevice]
+ -[ISHomeAccessoryAppRecipe iconSpecification]
+ _OBJC_CLASS_$_ISHomeAccessoryAppRecipe
+ _OBJC_METACLASS_$_ISHomeAccessoryAppRecipe
+ __OBJC_$_INSTANCE_METHODS_ISHomeAccessoryAppRecipe
+ __OBJC_CLASS_RO_$_ISHomeAccessoryAppRecipe
+ __OBJC_METACLASS_RO_$_ISHomeAccessoryAppRecipe
Functions:
~ ___55-[CUICatalog(IconServicesAdditions) idiomsForPlatform:]_block_invoke : 168 -> 220
~ +[ISRecipeInfo appRecipeForPlatform:descriptor:preferRichRecipe:] : 328 -> 448
~ -[ISPlatformInfo supportsRequestingIconStacksForPlatform:] : 240 -> 300
+ ___55-[CUICatalog(IconServicesAdditions) idiomsForPlatform:]_block_invoke.85
~ -[ISPlatformInfo supportsRequestingMultisizedImagesForPlatform:] : 156 -> 224
~ -[ISImageDescriptor continuousCornerRadius] : 260 -> 284
+ -[ISHomeAccessoryAppRecipe iconSpecification]
~ ___38+[ISSymbol _variantOptionsToKeyPieces]_block_invoke : 840 -> 888
+ -[ISDefaults simulateTintableAppearance]
~ -[ISCompositingDescriptor CUINamedImageDeviceClass] : 312 -> 356
~ -[ISCompositingDescriptor encapsulationShape] : 356 -> 404
~ -[ISDeviceInfo homeScreenIconSize] : 432 -> 484
+ -[ISDeviceInfo screenClass]
- ___55-[CUICatalog(IconServicesAdditions) idiomsForPlatform:]_block_invoke.82
CStrings:
+ "force_accessory"
+ "homeaccessory"
+ "homeaccessory_wall"
```
