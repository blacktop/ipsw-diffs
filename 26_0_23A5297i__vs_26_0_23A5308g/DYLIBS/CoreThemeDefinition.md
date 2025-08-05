## CoreThemeDefinition

> `/System/Library/PrivateFrameworks/CoreThemeDefinition.framework/CoreThemeDefinition`

```diff

-648.0.0.0.0
-  __TEXT.__text: 0x54e1c
+651.0.0.0.0
+  __TEXT.__text: 0x5504c
   __TEXT.__auth_stubs: 0x13f0
   __TEXT.__objc_methlist: 0x4a08
   __TEXT.__const: 0x230
-  __TEXT.__cstring: 0x78df
+  __TEXT.__cstring: 0x79ab
   __TEXT.__gcc_except_tab: 0x3d4
   __TEXT.__ustring: 0x20
   __TEXT.__unwind_info: 0xe78
   __TEXT.__objc_classname: 0xd70
-  __TEXT.__objc_methname: 0xead2
-  __TEXT.__objc_methtype: 0x16e7
+  __TEXT.__objc_methname: 0xeaed
+  __TEXT.__objc_methtype: 0x16ff
   __TEXT.__objc_stubs: 0xd8e0
   __DATA_CONST.__got: 0x808
   __DATA_CONST.__const: 0xad0

   __DATA_CONST.__objc_arraydata: 0xc8
   __AUTH_CONST.__auth_got: 0xa08
   __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x6480
+  __AUTH_CONST.__cfstring: 0x64c0
   __AUTH_CONST.__objc_const: 0xa2d0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: BF75A3FE-5544-3BC0-92CF-03D266A255DF
+  UUID: D580AF7B-9233-3A4B-9416-430E09F1E3CB
   Functions: 1635
   Symbols:   6888
-  CStrings:  4561
+  CStrings:  4567
 
Symbols:
+ -[CoreThemeDocument _addLegacyIconAssetsForLayerStack:forAppearance:renderedAppearance:renderingMode:error:]
+ -[CoreThemeDocument _addLegacyIconAssetsForLayerStack:forAppearance:renderedAppearance:renderingMode:error:].cold.1
+ -[CoreThemeDocument createNamedArtworkProductionsForAssets:customInfos:skipLastStep:error:]
+ -[CoreThemeDocument createNamedArtworkProductionsForAssets:customInfos:skipLastStep:error:].cold.1
+ -[CoreThemeDocument createNamedArtworkProductionsForAssets:customInfos:skipLastStep:error:].cold.2
+ ___91-[CoreThemeDocument createNamedArtworkProductionsForAssets:customInfos:skipLastStep:error:]_block_invoke
+ ___91-[CoreThemeDocument createNamedArtworkProductionsForAssets:customInfos:skipLastStep:error:]_block_invoke_2
+ ___block_literal_global.1078
+ ___block_literal_global.1219
+ ___block_literal_global.1251
+ ___block_literal_global.1275
+ ___block_literal_global.1773
+ ___block_literal_global.879
+ _objc_msgSend$_addLegacyIconAssetsForLayerStack:forAppearance:renderedAppearance:renderingMode:error:
+ _objc_msgSend$createNamedArtworkProductionsForAssets:customInfos:skipLastStep:error:
- -[CoreThemeDocument _addLegacyIconAssetsForLayerStack:forAppearance:renderedAppearance:error:]
- -[CoreThemeDocument _addLegacyIconAssetsForLayerStack:forAppearance:renderedAppearance:error:].cold.1
- -[CoreThemeDocument createNamedArtworkProductionsForAssets:customInfos:error:]
- -[CoreThemeDocument createNamedArtworkProductionsForAssets:customInfos:error:].cold.1
- -[CoreThemeDocument createNamedArtworkProductionsForAssets:customInfos:error:].cold.2
- ___78-[CoreThemeDocument createNamedArtworkProductionsForAssets:customInfos:error:]_block_invoke
- ___78-[CoreThemeDocument createNamedArtworkProductionsForAssets:customInfos:error:]_block_invoke_2
- ___block_literal_global.1071
- ___block_literal_global.1212
- ___block_literal_global.1244
- ___block_literal_global.1268
- ___block_literal_global.1765
- ___block_literal_global.872
- _objc_msgSend$_addLegacyIconAssetsForLayerStack:forAppearance:renderedAppearance:error:
- _objc_msgSend$createNamedArtworkProductionsForAssets:customInfos:error:
Functions:
~ -[CoreThemeDocument createNamedArtworkProductionsForAssets:customInfos:error:] -> -[CoreThemeDocument createNamedArtworkProductionsForAssets:customInfos:skipLastStep:error:] : 10316 -> 10452
~ -[CoreThemeDocument _addLegacyIconAssetsForLayerStackProduction:withName:error:] : 796 -> 872
~ -[CoreThemeDocument _iconLayerStackFromLayerStackRendition:withName:matchingAppearance:fallbackAppearance:error:] : 368 -> 396
~ -[CoreThemeDocument _namedColorFromColorRendition:] : 236 -> 264
~ -[CoreThemeDocument _namedGradientFromGradientRendition:matchingAppearance:fallbackAppearance:] : 660 -> 720
~ -[CoreThemeDocument _addLayerReference:toMutableIconLayerStack:matchingAppearance:fallbackAppearance:error:] : 2520 -> 2748
~ -[CoreThemeDocument _addLegacyIconAssetsForLayerStack:forAppearance:renderedAppearance:error:] -> -[CoreThemeDocument _addLegacyIconAssetsForLayerStack:forAppearance:renderedAppearance:renderingMode:error:] : 2064 -> 2060
~ ___84-[CoreThemeDocument importNamedAssetsFromFileURLs:referenceFiles:completionHandler:]_block_invoke_2 : 400 -> 404
~ ___87-[CoreThemeDocument importNamedAssetsWithImportInfos:referenceFiles:completionHandler:]_block_invoke_15 : 940 -> 944
CStrings:
+ "@44@0:8@16@24B32^@36"
+ "CoreThemeDefinition: key '%@' is defined as contained in a packing but we don't have any assets that match it skipping"
+ "_addLegacyIconAssetsForLayerStack:forAppearance:renderedAppearance:renderingMode:error:"
+ "createNamedArtworkProductionsForAssets:customInfos:skipLastStep:error:"
+ "infinite recusion for layer group %@"
+ "infinite recusion for layer group %@ in icon %@"
+ "v56@0:8@16@24Q32@40^@48"
- "_addLegacyIconAssetsForLayerStack:forAppearance:renderedAppearance:error:"
- "createNamedArtworkProductionsForAssets:customInfos:error:"
- "v48@0:8@16@24Q32^@40"

```
