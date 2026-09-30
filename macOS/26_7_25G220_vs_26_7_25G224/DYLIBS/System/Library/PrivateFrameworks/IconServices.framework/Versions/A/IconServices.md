## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices`

```diff

 743.5.2.401.0
-  __TEXT.__text: 0x84430
+  __TEXT.__text: 0x841bc
   __TEXT.__auth_stubs: 0x1640
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_methlist: 0x7744
+  __TEXT.__objc_methlist: 0x7714
   __TEXT.__const: 0x9550
   __TEXT.__gcc_except_tab: 0x6f0
-  __TEXT.__cstring: 0x4f58
+  __TEXT.__cstring: 0x4f27
   __TEXT.__oslogstring: 0x37d6
-  __TEXT.__unwind_info: 0x1c70
+  __TEXT.__unwind_info: 0x1c68
   __TEXT.__eh_frame: 0x88
-  __TEXT.__objc_classname: 0x1508
-  __TEXT.__objc_methname: 0xdacd
+  __TEXT.__objc_classname: 0x14ef
+  __TEXT.__objc_methname: 0xda95
   __TEXT.__objc_methtype: 0x1ed1
-  __TEXT.__objc_stubs: 0xb080
+  __TEXT.__objc_stubs: 0xb060
   __DATA_CONST.__got: 0x7b8
   __DATA_CONST.__const: 0x6c8
-  __DATA_CONST.__objc_classlist: 0x5c8
+  __DATA_CONST.__objc_classlist: 0x5c0
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x36e0
+  __DATA_CONST.__objc_selrefs: 0x36d0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x480
-  __DATA_CONST.__objc_arraydata: 0xc8
+  __DATA_CONST.__objc_arraydata: 0xb0
   __AUTH_CONST.__auth_got: 0xb38
   __AUTH_CONST.__const: 0x1aa8
-  __AUTH_CONST.__cfstring: 0x5900
-  __AUTH_CONST.__objc_const: 0x169c8
-  __AUTH_CONST.__objc_intobj: 0x6c0
-  __AUTH_CONST.__objc_arrayobj: 0x120
+  __AUTH_CONST.__cfstring: 0x58c0
+  __AUTH_CONST.__objc_const: 0x16928
+  __AUTH_CONST.__objc_intobj: 0x690
+  __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0xc80
+  __AUTH.__objc_data: 0xc30
   __AUTH.__data: 0x8
   __DATA.__objc_ivar: 0x778
   __DATA.__data: 0x2118

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2983
-  Symbols:   7225
-  CStrings:  4181
+  Functions: 2980
+  Symbols:   7216
+  CStrings:  4175
 
Symbols:
- -[ISDefaults isForceHomeAccessoryDeviceEnabled]
- -[ISDeviceInfo isHomeAccessoryDevice]
- -[ISHomeAccessoryAppRecipe iconSpecification]
- _OBJC_CLASS_$_ISHomeAccessoryAppRecipe
- _OBJC_METACLASS_$_ISHomeAccessoryAppRecipe
- __OBJC_$_INSTANCE_METHODS_ISHomeAccessoryAppRecipe
- __OBJC_CLASS_RO_$_ISHomeAccessoryAppRecipe
- __OBJC_METACLASS_RO_$_ISHomeAccessoryAppRecipe
- _objc_msgSend$isHomeAccessoryDevice
Functions:
- -[ISHomeAccessoryAppRecipe iconSpecification]
~ +[ISRecipeInfo appRecipeForPlatform:descriptor:preferRichRecipe:] : 572 -> 436
~ ___43+[ISSymbol _generateVariantKeyFromOptions:]_block_invoke : 916 -> 868
- -[ISDefaults simulateTintableAppearance]
~ -[ISCompositingDescriptor CUINamedImageDeviceClass] : 388 -> 336
~ -[ISCompositingDescriptor encapsulationShape] : 440 -> 384
~ -[ISPlatformInfo supportsRequestingMultisizedImagesForPlatform:] : 240 -> 164
~ -[ISPlatformInfo supportsRequestingIconStacksForPlatform:] : 332 -> 264
~ -[ISDeviceInfo homeScreenIconSize] : 500 -> 440
- -[ISDeviceInfo screenClass]
~ -[ISImageDescriptor continuousCornerRadius] : 248 -> 216
~ ___55-[CUICatalog(IconServicesAdditions) idiomsForPlatform:]_block_invoke : 228 -> 168
CStrings:
- "ISHomeAccessoryAppRecipe"
- "force_accessory"
- "homeaccessory"
- "homeaccessory_wall"
- "isForceHomeAccessoryDeviceEnabled"
- "isHomeAccessoryDevice"
```
