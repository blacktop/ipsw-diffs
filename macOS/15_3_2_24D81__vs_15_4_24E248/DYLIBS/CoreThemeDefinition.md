## CoreThemeDefinition

> `/System/Library/PrivateFrameworks/CoreThemeDefinition.framework/Versions/A/CoreThemeDefinition`

```diff

 611.0.0.0.0
-  __TEXT.__text: 0x53afc
-  __TEXT.__auth_stubs: 0x1290
-  __TEXT.__objc_methlist: 0x486c
+  __TEXT.__text: 0x543c0
+  __TEXT.__auth_stubs: 0x1280
+  __TEXT.__objc_methlist: 0x4958
   __TEXT.__const: 0x230
   __TEXT.__cstring: 0x751d
   __TEXT.__gcc_except_tab: 0x3a4
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0xe78
+  __TEXT.__unwind_info: 0xee0
   __TEXT.__objc_classname: 0xd3b
   __TEXT.__objc_methname: 0xe878
   __TEXT.__objc_methtype: 0x1670

   __DATA_CONST.__objc_selrefs: 0x3d48
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__auth_got: 0x958
+  __AUTH_CONST.__auth_got: 0x950
   __AUTH_CONST.__const: 0xb10
   __AUTH_CONST.__cfstring: 0x6120
-  __AUTH_CONST.__objc_const: 0xa1d8
+  __AUTH_CONST.__objc_const: 0xa028
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 20CA7D18-2C28-32CB-A3B6-F8518218B713
-  Functions: 1594
-  Symbols:   5171
+  UUID: BEB13A47-3C6F-3349-BCA8-D6114522272D
+  Functions: 1660
+  Symbols:   5251
   CStrings:  4491
 
Symbols:
+ +[CoreThemeDocument _sharedDocumentList].cold.1
+ +[CoreThemeDocument dataModelVersion].cold.1
+ +[CoreThemeDocument shouldConvertColorsFromColorSpaceWithIdentifier:toIdentifier:error:].cold.1
+ +[TDAsset _filenameRegex].cold.1
+ +[TDLogger defaultLogger].cold.1
+ +[TDThemeSchema loadThemeConstantsForEntity:inContext:].cold.1
+ +[TDVectorGlyphReader vectorGlyphReaderWithURL:platform:error:].cold.1
+ -[CoreThemeDocument _tidyUpLayerStacks].cold.1
+ -[CoreThemeDocument _updateRenditionPackings:error:].cold.1
+ -[CoreThemeDocument allObjectsForEntity:withSortDescriptors:].cold.1
+ -[CoreThemeDocument appearanceWithIdentifier:].cold.1
+ -[CoreThemeDocument appearanceWithIdentifier:name:createIfNeeded:].cold.1
+ -[CoreThemeDocument catalogGlobals].cold.1
+ -[CoreThemeDocument checksum].cold.1
+ -[CoreThemeDocument createNamedArtworkProductionsForAssets:customInfos:error:].cold.1
+ -[CoreThemeDocument createNamedArtworkProductionsForAssets:customInfos:error:].cold.2
+ -[CoreThemeDocument createNamedColorProductionsForImportInfos:error:].cold.1
+ -[CoreThemeDocument createNamedGlyphVectorForCustomInfos:referenceFiles:bitSource:error:].cold.2
+ -[CoreThemeDocument createNamedGlyphVectorForCustomInfos:referenceFiles:bitSource:error:].cold.3
+ -[CoreThemeDocument createNamedModelsForCustomInfos:referenceFiles:bitSource:error:].cold.1
+ -[CoreThemeDocument createNamedModelsForCustomInfos:referenceFiles:bitSource:error:].cold.2
+ -[CoreThemeDocument createNamedRecognitionObjectsForAssets:customInfos:error:].cold.1
+ -[CoreThemeDocument createNamedRecognitionObjectsForAssets:customInfos:error:].cold.2
+ -[CoreThemeDocument createNamedRenditionGroupProductionsForImportInfos:error:].cold.1
+ -[CoreThemeDocument createNamedRenditionGroupProductionsForImportInfos:error:].cold.2
+ -[CoreThemeDocument createNamedTexturesForCustomInfos:referenceFiles:bitSource:error:].cold.1
+ -[CoreThemeDocument createNamedTexturesForCustomInfos:referenceFiles:bitSource:error:].cold.2
+ -[CoreThemeDocument deleteObject:].cold.1
+ -[CoreThemeDocument deleteObjects:].cold.1
+ -[CoreThemeDocument localizationWithIdentifier:].cold.1
+ -[CoreThemeDocument metadatumForKey:].cold.1
+ -[CoreThemeDocument metadatumForKey:].cold.2
+ -[CoreThemeDocument newObjectForEntity:].cold.1
+ -[CoreThemeDocument newObjectForEntity:].cold.2
+ -[CoreThemeDocument objectsForEntity:withPredicate:sortDescriptors:].cold.1
+ -[CoreThemeDocument persistentStoreTypeForFileType:].cold.1
+ -[CoreThemeDocument setMetadatum:forKey:].cold.1
+ -[CoreThemeDocument setMetadatum:forKey:].cold.2
+ -[TDDeviceTraits _deploymentTargetFromTraitString:].cold.1
+ -[TDDistillRunner _moveScratchToOutputPath].cold.1
+ -[TDDistiller _renditionsWithError:].cold.1
+ -[TDDistiller cancelDistill].cold.1
+ -[TDDistiller distillCatalogGlobals].cold.1
+ -[TDMultisizeImageSetProduction processRendition:withBackstop:].cold.1
+ -[TDMultisizeImageSetRenditionSpec createCSIRepresentationWithCompression:colorSpaceID:document:].cold.1
+ -[TDNamedAssetImportInfo verify].cold.1
+ -[TDNamedAssetImportInfo verify].cold.2
+ -[TDNamedAssetImportInfo verify].cold.3
+ -[TDNamedAssetImportInfo verify].cold.4
+ -[TDNamedAssetImportInfo verify].cold.5
+ -[TDNamedColorRenditionSpec setColorPropertiesFromCGColor:].cold.1
+ -[TDPersistentDocument setFileURL:].cold.1
+ -[TDPhotoshopRenditionSpec _layerIndexInPSDImage:].cold.1
+ -[TDSchemaPartDefinition validStatesWithDocument:].cold.1
+ -[TDSimpleArtworkRenditionSpec _createImageRefWithURL:andDocument:format:vectorBased:].cold.1
+ -[TDSimpleArtworkRenditionSpec _createImageRefWithURL:andDocument:format:vectorBased:].cold.2
+ -[TDSimpleArtworkRenditionSpec _createImageRefWithURL:andDocument:format:vectorBased:].cold.3
+ -[TDSimpleArtworkRenditionSpec _createImageRefWithURL:andDocument:format:vectorBased:].cold.4
+ -[TDTextureRawRenditionSpec textureWithDocument:].cold.1
+ -[TDTextureRawRenditionSpec textureWithDocument:].cold.2
+ -[TDThemeSchema _sanityCheckSchemaAssets].cold.1
+ -[TDThreadMOCOrganizer initWithDocument:mainThread:].cold.1
+ -[TDThreadMOCOrganizer initWithDocument:mainThread:].cold.2
+ -[TDThreadMOCOrganizer setThreadMOC:].cold.1
+ -[TDVectorGlyphReader _readSVGNodesError:].cold.1
+ -[TDVectorGlyphReader _readSVGNodesError:].cold.2
+ -[TDVectorGlyphReader _readSVGNodesError:].cold.3
+ -[TDVectorGlyphReader _readSVGNodesError:].cold.4
+ -[TDVectorGlyphReader _readSVGNodesError:].cold.5
+ TDColorSpaceGetExtendedRangeSRGB.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ __24-[TDDistiller _distill:]_block_invoke.cold.1
+ __31-[TDDistiller _distillChanges:]_block_invoke.cold.1
+ __CUIVectorGlyphGuideIDs_block_invoke.cold.1
- _fmod

```
