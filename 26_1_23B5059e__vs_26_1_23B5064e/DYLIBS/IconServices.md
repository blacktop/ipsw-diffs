## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/IconServices`

```diff

-733.100.0.0.0
-  __TEXT.__text: 0x635b0
+737.0.0.0.0
+  __TEXT.__text: 0x637fc
   __TEXT.__auth_stubs: 0xf70
   __TEXT.__delay_helper: 0xc8
   __TEXT.__objc_methlist: 0x66bc
   __TEXT.__const: 0x87b2
   __TEXT.__gcc_except_tab: 0x42c
-  __TEXT.__cstring: 0x3e25
-  __TEXT.__oslogstring: 0x31c6
+  __TEXT.__cstring: 0x3e65
+  __TEXT.__oslogstring: 0x3208
   __TEXT.__unwind_info: 0x1848
   __TEXT.__eh_frame: 0x88
   __TEXT.__objc_classname: 0x1228
-  __TEXT.__objc_methname: 0xbf0f
+  __TEXT.__objc_methname: 0xbf2b
   __TEXT.__objc_methtype: 0x1851
-  __TEXT.__objc_stubs: 0x9600
+  __TEXT.__objc_stubs: 0x9620
   __DATA_CONST.__got: 0x628
-  __DATA_CONST.__const: 0x9c8
+  __DATA_CONST.__const: 0x9f0
   __DATA_CONST.__objc_classlist: 0x528
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2fd0
+  __DATA_CONST.__objc_selrefs: 0x2fd8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0xb0
   __AUTH_CONST.__auth_got: 0x7d0
   __AUTH_CONST.__const: 0x1188
-  __AUTH_CONST.__cfstring: 0x4240
+  __AUTH_CONST.__cfstring: 0x42a0
   __AUTH_CONST.__objc_const: 0x13bb0
   __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_arrayobj: 0x108

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9C4BB6DF-6DA7-38F1-8600-58589A62F76A
-  Functions: 2523
-  Symbols:   9466
-  CStrings:  4163
+  UUID: 1778F50F-7333-32EB-92A1-CCFC59D37763
+  Functions: 2526
+  Symbols:   9474
+  CStrings:  4172
 
Symbols:
+ -[ISCompositingDescriptor encapsulationShape].cold.1
+ ___33-[ISIconLayerElement description]_block_invoke
+ ___block_descriptor_40_e8_32s_e24_v32?0"IFImage"8Q16^B24ls32l8
+ _objc_msgSend$enumerateObjectsUsingBlock:
Functions:
~ -[ISAssetInspector(AppReview) catalogAssetAppearances] : 224 -> 284
~ +[ISResourceProvider(Convenience) resourceWithBundleURL:iconDictionary:options:] : 1900 -> 1928
~ -[ISCompositingDescriptor copyWithZone:] : 164 -> 172
~ -[ISCompositingDescriptor encapsulationShape] : 92 -> 232
+ _OUTLINED_FUNCTION_0
~ -[ISIconLayerElement description] : 240 -> 396
+ ___33-[ISIconLayerElement description]_block_invoke
~ -[ISRecipeFactory preferRichRecipe] : 176 -> 88
~ -[ISCompositingDescriptor CUINamedImageDeviceClass].cold.1 : 140 -> 124
+ -[ISCompositingDescriptor encapsulationShape].cold.1
CStrings:
+ "%@ O:%@, E:%@, C:%@ Images: %@"
+ "%@ O:%@, S:%@, CS:%@ B:%@ T:%@ SS:%@ S:%@ ElementLayers: %@"
+ ", "
+ "23:06:48"
+ "<IFImage 0x%lx> CGImage:%@"
+ "Unable to map platform to encapsulation shape for icon stack: %lu"
+ "enumerateObjectsUsingBlock:"
+ "v32@?0@\"IFImage\"8Q16^B24"
+ "valid"
- "%@ Images: %@ - O:%@, E:%@, C:%@"
- "%@ Images: %@ - O:%@, S:%@, CS:%@ B:%@ T:%@ SS:%@ S:%@"
- "21:27:03"

```
