## CoreThemeDefinition

> `/System/Library/PrivateFrameworks/CoreThemeDefinition.framework/CoreThemeDefinition`

```diff

-643.0.0.0.0
-  __TEXT.__text: 0x54274
-  __TEXT.__auth_stubs: 0x13c0
+645.1.0.0.0
+  __TEXT.__text: 0x54b28
+  __TEXT.__auth_stubs: 0x13f0
   __TEXT.__objc_methlist: 0x4a08
   __TEXT.__const: 0x230
-  __TEXT.__cstring: 0x7832
-  __TEXT.__gcc_except_tab: 0x3b0
+  __TEXT.__cstring: 0x78d9
+  __TEXT.__gcc_except_tab: 0x3d4
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0xe70
+  __TEXT.__unwind_info: 0xe78
   __TEXT.__objc_classname: 0xd70
-  __TEXT.__objc_methname: 0xe9ec
-  __TEXT.__objc_methtype: 0x16ba
-  __TEXT.__objc_stubs: 0xd800
-  __DATA_CONST.__got: 0x7f8
+  __TEXT.__objc_methname: 0xead2
+  __TEXT.__objc_methtype: 0x16e7
+  __TEXT.__objc_stubs: 0xd8e0
+  __DATA_CONST.__got: 0x808
   __DATA_CONST.__const: 0xad0
   __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d30
+  __DATA_CONST.__objc_selrefs: 0x3d68
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__auth_got: 0x9f0
+  __AUTH_CONST.__auth_got: 0xa08
   __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x6380
-  __AUTH_CONST.__objc_const: 0xa2b0
+  __AUTH_CONST.__cfstring: 0x6460
+  __AUTH_CONST.__objc_const: 0xa2d0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: C42E98E2-BD08-3F50-B27F-96981A0EEAD2
-  Functions: 1633
-  Symbols:   6873
-  CStrings:  4536
+  UUID: F72F461C-B385-3727-9ABD-CED437AA1689
+  Functions: 1635
+  Symbols:   6888
+  CStrings:  4559
 
Symbols:
+ -[CoreThemeDocument _addLayerReference:toMutableIconLayerStack:matchingAppearance:fallbackAppearance:error:]
+ -[CoreThemeDocument _addLegacyIconAssetsForLayerStack:forAppearance:renderedAppearance:error:]
+ -[CoreThemeDocument _addLegacyIconAssetsForLayerStack:forAppearance:renderedAppearance:error:].cold.1
+ -[CoreThemeDocument _iconLayerStackFromLayerStackRendition:withName:matchingAppearance:fallbackAppearance:error:]
+ _CGImageGetBitsPerPixel
+ _OBJC_CLASS_$_NSProcessInfo
+ ___51-[CoreThemeDocument _automaticP3GenerationFromSRGB]_block_invoke_3
+ ___block_literal_global.1068
+ ___block_literal_global.1209
+ ___block_literal_global.1241
+ ___block_literal_global.1265
+ ___block_literal_global.1762
+ ___block_literal_global.869
+ _objc_msgSend$_addLayerReference:toMutableIconLayerStack:matchingAppearance:fallbackAppearance:error:
+ _objc_msgSend$_addLegacyIconAssetsForLayerStack:forAppearance:renderedAppearance:error:
+ _objc_msgSend$_iconLayerStackFromLayerStackRendition:withName:matchingAppearance:fallbackAppearance:error:
+ _objc_msgSend$globallyUniqueString
+ _objc_msgSend$processInfo
+ _objc_msgSend$scaledHeight
+ _objc_msgSend$scaledWidth
+ _objc_msgSend$setScaledHeight:
+ _objc_msgSend$setScaledWidth:
+ _objc_msgSend$tintWithRed:green:blue:alpha:
+ _vImageBuffer_Init
+ _vImageBuffer_InitWithCGImage
- -[CoreThemeDocument _addLayerReference:toMutableIconLayerStack:error:]
- -[CoreThemeDocument _addLegacyIconAssetsForLayerStack:error:]
- -[CoreThemeDocument _iconLayerStackFromLayerStackRendition:withName:error:]
- ___block_literal_global.1056
- ___block_literal_global.1197
- ___block_literal_global.1229
- ___block_literal_global.1253
- ___block_literal_global.1743
- ___block_literal_global.854
- _objc_msgSend$_addLayerReference:toMutableIconLayerStack:error:
- _objc_msgSend$_addLegacyIconAssetsForLayerStack:error:
- _objc_msgSend$_iconLayerStackFromLayerStackRendition:withName:error:
CStrings:
+ "Any"
+ "Error creating CGImage from buffer: %ld\n"
+ "Error during scaling: %ld\n"
+ "Error initializing destination buffer: %ld\n"
+ "Error initializing source buffer: %ld\n"
+ "Failed to find a light mode icon rendition for layered icon production"
+ "ISAppearanceTintable"
+ "NSAppearanceNameDarkAqua"
+ "UIAppearanceDark"
+ "_%@_%@.png"
+ "_addLayerReference:toMutableIconLayerStack:matchingAppearance:fallbackAppearance:error:"
+ "_addLegacyIconAssetsForLayerStack:forAppearance:renderedAppearance:error:"
+ "_iconLayerStackFromLayerStackRendition:withName:matchingAppearance:fallbackAppearance:error:"
+ "globallyUniqueString"
+ "processInfo"
+ "scaledHeight"
+ "scaledWidth"
+ "setScaledHeight:"
+ "setScaledWidth:"
+ "tintWithRed:green:blue:alpha:"
+ "v48@0:8@16@24Q32^@40"
+ "v56@0:8@16@24@32@40^@48"
- "CoreThemeDefinition: key '%@' is defined as contained in a packing but we don't have any assets that match it skipping"
- "_%@.png"
- "_addLayerReference:toMutableIconLayerStack:error:"
- "_addLegacyIconAssetsForLayerStack:error:"
- "_iconLayerStackFromLayerStackRendition:withName:error:"
- "light"

```
