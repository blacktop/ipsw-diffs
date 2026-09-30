## CoreThemeDefinition

> `/System/Library/PrivateFrameworks/CoreThemeDefinition.framework/CoreThemeDefinition`

```diff

-611.0.0.0.0
-  __TEXT.__text: 0x5016c
-  __TEXT.__auth_stubs: 0x1390
-  __TEXT.__objc_methlist: 0x4768
+640.0.0.0.0
+  __TEXT.__text: 0x53e44
+  __TEXT.__auth_stubs: 0x13c0
+  __TEXT.__objc_methlist: 0x49f8
   __TEXT.__const: 0x230
-  __TEXT.__cstring: 0x74a2
-  __TEXT.__gcc_except_tab: 0x3a4
+  __TEXT.__cstring: 0x777d
+  __TEXT.__gcc_except_tab: 0x3c4
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0xdf0
-  __TEXT.__objc_classname: 0xd09
-  __TEXT.__objc_methname: 0xdf69
-  __TEXT.__objc_methtype: 0x15b2
-  __TEXT.__objc_stubs: 0xcda0
-  __DATA_CONST.__got: 0x798
-  __DATA_CONST.__const: 0xa60
-  __DATA_CONST.__objc_classlist: 0x4b8
+  __TEXT.__unwind_info: 0xe60
+  __TEXT.__objc_classname: 0xd70
+  __TEXT.__objc_methname: 0xe9a2
+  __TEXT.__objc_methtype: 0x16ba
+  __TEXT.__objc_stubs: 0xd7e0
+  __DATA_CONST.__got: 0x800
+  __DATA_CONST.__const: 0xaa8
+  __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a60
-  __DATA_CONST.__objc_superrefs: 0x180
+  __DATA_CONST.__objc_selrefs: 0x3d28
+  __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__auth_got: 0x9d8
-  __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x60a0
-  __AUTH_CONST.__objc_const: 0x9d50
+  __AUTH_CONST.__auth_got: 0x9f0
+  __AUTH_CONST.__const: 0x380
+  __AUTH_CONST.__cfstring: 0x62c0
+  __AUTH_CONST.__objc_const: 0xa2b0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x2f30
-  __DATA.__objc_ivar: 0x4a0
+  __AUTH.__objc_data: 0x3070
+  __DATA.__objc_ivar: 0x4c8
   __DATA.__data: 0x160
   __DATA.__bss: 0xd0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/PrivateFrameworks/CoreSVG.framework/CoreSVG
   - /System/Library/PrivateFrameworks/CoreUI.framework/CoreUI
+  - /System/Library/PrivateFrameworks/IconRendering.framework/IconRendering
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: EAE9AB82-583A-3F33-A35B-F51DFE4F7772
-  Functions: 1578
-  Symbols:   6628
-  CStrings:  4370
+  UUID: 7D2B3283-326A-3780-B3CC-DAB4997684F7
+  Functions: 1630
+  Symbols:   6864
+  CStrings:  4523
 
Symbols:
+ +[TDColorStop(CoreDataProperties) fetchRequest]
+ +[TDLayerGroupRenditionSpec(CoreDataProperties) fetchRequest]
+ +[TDNamedGradientProduction(CoreDataProperties) fetchRequest]
+ +[TDNamedGradientRenditionSpec(CoreDataProperties) fetchRequest]
+ +[TDVectorGlyphReader _anchorInOutlineCoordinateSpaceForAnchorPoint:glyph:]
+ -[CoreThemeDocument _addLayerReference:toMutableIconLayerStack:error:]
+ -[CoreThemeDocument _addLegacyIconAssetsForLayerStack:error:]
+ -[CoreThemeDocument _addLegacyIconAssetsForLayerStackProduction:withName:error:]
+ -[CoreThemeDocument _iconLayerStackFromLayerStackRendition:withName:error:]
+ -[CoreThemeDocument _namedColorFromColorRendition:]
+ -[CoreThemeDocument _namedGradientFromGradientRendition:]
+ -[CoreThemeDocument _testRenditionForP3:]
+ -[CoreThemeDocument createCGColorSpaceWithIdentifier:]
+ -[CoreThemeDocument createNamedGradientProductionsForImportInfos:error:]
+ -[CoreThemeDocument createNamedGradientProductionsForImportInfos:error:].cold.1
+ -[CoreThemeDocument createNamedGradientProductionsForImportInfos:error:].cold.2
+ -[CoreThemeDocument createNamedIconLayerStacksForCustomInfos:referenceFiles:bitSource:error:]
+ -[CoreThemeDocument urlForRasterizedIconImageStackNamed:]
+ -[TDFlattenedImageRenditionSpec copyAttributesInto:]
+ -[TDLayerGroupRenditionSpec createCSIRepresentationWithCompression:colorSpaceID:document:]
+ -[TDNamedAssetImportInfo colorNames]
+ -[TDNamedAssetImportInfo colorStops]
+ -[TDNamedAssetImportInfo generateFallbackIcon]
+ -[TDNamedAssetImportInfo gradientAngle]
+ -[TDNamedAssetImportInfo gradientEndPoint]
+ -[TDNamedAssetImportInfo gradientStartPoint]
+ -[TDNamedAssetImportInfo gradientType]
+ -[TDNamedAssetImportInfo setColorNames:]
+ -[TDNamedAssetImportInfo setColorStops:]
+ -[TDNamedAssetImportInfo setGenerateFallbackIcon:]
+ -[TDNamedAssetImportInfo setGradientAngle:]
+ -[TDNamedAssetImportInfo setGradientEndPoint:]
+ -[TDNamedAssetImportInfo setGradientStartPoint:]
+ -[TDNamedAssetImportInfo setGradientType:]
+ -[TDNamedGradientRenditionSpec createCSIRepresentationWithCompression:colorSpaceID:document:]
+ -[TDNamedGradientRenditionSpec(CoreDataProperties) gradientEndPoint]
+ -[TDNamedGradientRenditionSpec(CoreDataProperties) gradientStartPoint]
+ -[TDNamedGradientRenditionSpec(CoreDataProperties) setGradientEndPoint:]
+ -[TDNamedGradientRenditionSpec(CoreDataProperties) setGradientStartPoint:]
+ -[TDVectorGlyphReader _createAnchorNodeFromPoint:withIdentifier:]
+ -[TDVectorGlyphReader _readSVGNodesError:].cold.6
+ -[TDVectorGlyphReader _writeDrawAttachmentDataToRootNode:forWeight:size:glyphNode:scaleFactor:transform:]
+ -[TDVectorGlyphReader _writeRotateAnchorToRootNode:forWeight:size:glyphNode:scaleFactor:transform:]
+ -[TDVectorGlyphReader createInterpolatedDrawAttachmentDataForWeight:size:scaleFactor:]
+ -[TDVectorGlyphReader resolvedFillStyle]
+ -[TDVectorGlyphReader resolvedVariableMode]
+ -[TDVectorGlyphReader unsafeDrawAttachmentAnchors]
+ -[TDVectorGlyphReader unsafeDrawAttachmentData]
+ GCC_except_table109
+ GCC_except_table190
+ GCC_except_table201
+ GCC_except_table205
+ GCC_except_table249
+ GCC_except_table268
+ GCC_except_table310
+ GCC_except_table322
+ GCC_except_table327
+ GCC_except_table39
+ OBJC_IVAR_$_CoreThemeDocument._appearanceIconFilesForName
+ OBJC_IVAR_$_CoreThemeDocument._tempFilesToCleanup
+ _CGSVGNodeCreateGroupNode
+ _OBJC_CLASS_$_CUIMutableNamedColor
+ _OBJC_CLASS_$_CUIMutableNamedGradient
+ _OBJC_CLASS_$_CUIMutableNamedIconLayerGroup
+ _OBJC_CLASS_$_CUIMutableNamedIconLayerStack
+ _OBJC_CLASS_$_CUIMutableNamedLayerImage
+ _OBJC_CLASS_$_CUIMutableNamedLayerVectorSVGImage
+ _OBJC_CLASS_$_CUIVectorGlyphDrawAttachmentDataStore
+ _OBJC_CLASS_$_CUIVectorGlyphManagedPointArray
+ _OBJC_CLASS_$_ICRGlobalConfiguration
+ _OBJC_CLASS_$_ICRRenderingMode
+ _OBJC_CLASS_$_TDColorStop
+ _OBJC_CLASS_$_TDLayerGroupRenditionSpec
+ _OBJC_CLASS_$_TDNamedGradientProduction
+ _OBJC_CLASS_$_TDNamedGradientRenditionSpec
+ _OBJC_CLASS_$_TDResolvedImageLayerReference
+ _OBJC_IVAR_$_TDNamedAssetImportInfo._colorNames
+ _OBJC_IVAR_$_TDNamedAssetImportInfo._colorStops
+ _OBJC_IVAR_$_TDNamedAssetImportInfo._generateFallbackIcon
+ _OBJC_IVAR_$_TDNamedAssetImportInfo._gradientAngle
+ _OBJC_IVAR_$_TDNamedAssetImportInfo._gradientEndPoint
+ _OBJC_IVAR_$_TDNamedAssetImportInfo._gradientStartPoint
+ _OBJC_IVAR_$_TDNamedAssetImportInfo._gradientType
+ _OBJC_IVAR_$_TDVectorGlyphReader._vectorGlyphDrawAttachmentDataNodes
+ _OBJC_METACLASS_$_TDColorStop
+ _OBJC_METACLASS_$_TDLayerGroupRenditionSpec
+ _OBJC_METACLASS_$_TDNamedGradientProduction
+ _OBJC_METACLASS_$_TDNamedGradientRenditionSpec
+ _OBJC_METACLASS_$_TDResolvedImageLayerReference
+ __CUILog
+ __OBJC_$_CLASS_METHODS_TDColorStop(CoreDataProperties)
+ __OBJC_$_CLASS_METHODS_TDLayerGroupRenditionSpec(CoreDataProperties)
+ __OBJC_$_CLASS_METHODS_TDNamedGradientProduction(CoreDataProperties)
+ __OBJC_$_CLASS_METHODS_TDNamedGradientRenditionSpec(CoreDataProperties)
+ __OBJC_$_INSTANCE_METHODS_TDLayerGroupRenditionSpec
+ __OBJC_$_INSTANCE_METHODS_TDNamedGradientRenditionSpec(CoreDataProperties)
+ __OBJC_$_PROP_LIST_TDResolvedImageLayerReference
+ __OBJC_CLASS_RO_$_TDColorStop
+ __OBJC_CLASS_RO_$_TDLayerGroupRenditionSpec
+ __OBJC_CLASS_RO_$_TDNamedGradientProduction
+ __OBJC_CLASS_RO_$_TDNamedGradientRenditionSpec
+ __OBJC_CLASS_RO_$_TDResolvedImageLayerReference
+ __OBJC_METACLASS_RO_$_TDColorStop
+ __OBJC_METACLASS_RO_$_TDLayerGroupRenditionSpec
+ __OBJC_METACLASS_RO_$_TDNamedGradientProduction
+ __OBJC_METACLASS_RO_$_TDNamedGradientRenditionSpec
+ __OBJC_METACLASS_RO_$_TDResolvedImageLayerReference
+ ___28-[CoreThemeDocument dealloc]_block_invoke
+ ___51-[CoreThemeDocument _automaticP3GenerationFromSRGB]_block_invoke_3
+ ___72-[CoreThemeDocument createNamedGradientProductionsForImportInfos:error:]_block_invoke
+ ___93-[CoreThemeDocument createNamedIconLayerStacksForCustomInfos:referenceFiles:bitSource:error:]_block_invoke
+ ___block_descriptor_144_e8_32o40o48o56o64o72o80o88o96o104o112o120o128o136o_e39_v32?0"TDNamedAssetImportInfo"8Q16^B24ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8s136l8
+ ___block_descriptor_161_e8_32o40o48o56o64o72o80o88o96o104o112o120o128o136o144o152b_e5_v8?0ls32l8s40l8s48l8s56l8s152l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8s136l8s144l8
+ ___block_descriptor_169_e8_32o40o48o56o64o72o80o88o96o104o112o120o128o136o144o152o160b_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s160l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8s136l8s144l8s152l8
+ ___block_descriptor_32_e22_v32?0"NSURL"8Q16^B24l
+ ___block_descriptor_48_e8_32o_e15_v32?0816^B24ls32l8
+ ___block_literal_global.1037
+ ___block_literal_global.1211
+ ___block_literal_global.1235
+ ___block_literal_global.1725
+ ___block_literal_global.207
+ ___block_literal_global.220
+ ___block_literal_global.270
+ ___block_literal_global.416
+ ___block_literal_global.418
+ ___block_literal_global.605
+ ___block_literal_global.613
+ ___block_literal_global.624
+ ___block_literal_global.642
+ ___block_literal_global.644
+ ___block_literal_global.841
+ ___createClassSet
+ _kCGColorSpaceGenericRGB
+ _objc_msgSend$_addLayerReference:toMutableIconLayerStack:error:
+ _objc_msgSend$_addLegacyIconAssetsForLayerStack:error:
+ _objc_msgSend$_addLegacyIconAssetsForLayerStackProduction:withName:error:
+ _objc_msgSend$_anchorInOutlineCoordinateSpaceForAnchorPoint:glyph:
+ _objc_msgSend$_createAnchorNodeFromPoint:withIdentifier:
+ _objc_msgSend$_iconLayerStackFromLayerStackRendition:withName:error:
+ _objc_msgSend$_namedColorFromColorRendition:
+ _objc_msgSend$_namedGradientFromGradientRendition:
+ _objc_msgSend$_testRenditionForP3:
+ _objc_msgSend$_writeDrawAttachmentDataToRootNode:forWeight:size:glyphNode:scaleFactor:transform:
+ _objc_msgSend$_writeRotateAnchorToRootNode:forWeight:size:glyphNode:scaleFactor:transform:
+ _objc_msgSend$addLayer:
+ _objc_msgSend$anchors
+ _objc_msgSend$blurStrength
+ _objc_msgSend$cgColor
+ _objc_msgSend$clearInstanceCache
+ _objc_msgSend$color
+ _objc_msgSend$colorName
+ _objc_msgSend$colorNames
+ _objc_msgSend$colorStops
+ _objc_msgSend$createCGColorSpaceWithIdentifier:
+ _objc_msgSend$createFloatDeltasFrom:to:
+ _objc_msgSend$createInterpolatedDrawAttachmentDataForWeight:size:scaleFactor:
+ _objc_msgSend$createInterpolatedFloatsFromFloats:ultralightDeltas:blackDeltas:withScalars:
+ _objc_msgSend$createManagedPointArrayWrapping:
+ _objc_msgSend$createNamedGradientProductionsForImportInfos:error:
+ _objc_msgSend$createNamedIconLayerStacksForCustomInfos:referenceFiles:bitSource:error:
+ _objc_msgSend$createWithPointCount:
+ _objc_msgSend$data
+ _objc_msgSend$dataAtIndex:
+ _objc_msgSend$encodeToSVGNode:
+ _objc_msgSend$finalizedIconWithSize:scale:deviceClass:appearance:renderingMode:
+ _objc_msgSend$gathersSpecularByElement
+ _objc_msgSend$generateFallbackIcon
+ _objc_msgSend$gradientEndPoint
+ _objc_msgSend$gradientEndX
+ _objc_msgSend$gradientEndY
+ _objc_msgSend$gradientOrColorName
+ _objc_msgSend$gradientStartPoint
+ _objc_msgSend$gradientStartX
+ _objc_msgSend$gradientStartY
+ _objc_msgSend$gradientType
+ _objc_msgSend$hasLightingEffects
+ _objc_msgSend$hasSpecular
+ _objc_msgSend$initAdoptingData:anchors:
+ _objc_msgSend$initWithContext:
+ _objc_msgSend$initWithGradientNamed:type:startPoint:endPoint:colorNames:colorStops:
+ _objc_msgSend$initWithName:withSize:atScale:
+ _objc_msgSend$initWithSVGNode:
+ _objc_msgSend$orderedSet
+ _objc_msgSend$rawArray
+ _objc_msgSend$renderedLegacyCompatibleIconWithConfiguration:forDeviceClass:
+ _objc_msgSend$setBlurStrength:
+ _objc_msgSend$setCGColor:
+ _objc_msgSend$setColor:
+ _objc_msgSend$setColorName:
+ _objc_msgSend$setColorNames:
+ _objc_msgSend$setColorStops:
+ _objc_msgSend$setColors:andStops:
+ _objc_msgSend$setGathersSpecularByElement:
+ _objc_msgSend$setGenerateFallbackIcon:
+ _objc_msgSend$setGradientEndPoint:
+ _objc_msgSend$setGradientEndX:
+ _objc_msgSend$setGradientEndY:
+ _objc_msgSend$setGradientOrColorName:
+ _objc_msgSend$setGradientStartPoint:
+ _objc_msgSend$setGradientStartX:
+ _objc_msgSend$setGradientStartY:
+ _objc_msgSend$setGradientType:
+ _objc_msgSend$setHasLightingEffects:
+ _objc_msgSend$setHasSpecular:
+ _objc_msgSend$setImage:
+ _objc_msgSend$setShadowOpacity:
+ _objc_msgSend$setShadowStyle:
+ _objc_msgSend$setStack:
+ _objc_msgSend$setStop:
+ _objc_msgSend$setSvgDocument:
+ _objc_msgSend$setSvgDocumentURL:
+ _objc_msgSend$setTranslucency:
+ _objc_msgSend$shadowOpacity
+ _objc_msgSend$shadowStyle
+ _objc_msgSend$stop
+ _objc_msgSend$translucency
+ _objc_opt_new
+ _vDSP_vsaddD
- GCC_except_table108
- GCC_except_table178
- GCC_except_table189
- GCC_except_table193
- GCC_except_table237
- GCC_except_table255
- GCC_except_table297
- GCC_except_table309
- GCC_except_table313
- GCC_except_table36
- _OBJC_CLASS_$_TDResolvedLayerReference
- _OBJC_METACLASS_$_TDResolvedLayerReference
- __OBJC_$_PROP_LIST_TDResolvedLayerReference
- __OBJC_CLASS_RO_$_TDResolvedLayerReference
- __OBJC_METACLASS_RO_$_TDResolvedLayerReference
- ___block_descriptor_128_e8_32o40o48o56o64o72o80o88o96o104o112o120o_e39_v32?0"TDNamedAssetImportInfo"8Q16^B24ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8
- ___block_descriptor_145_e8_32o40o48o56o64o72o80o88o96o104o112o120o128o136b_e5_v8?0ls32l8s40l8s48l8s56l8s136l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8
- ___block_descriptor_153_e8_32o40o48o56o64o72o80o88o96o104o112o120o128o136o144b_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s144l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8s136l8
- ___block_literal_global.1120
- ___block_literal_global.1153
- ___block_literal_global.1649
- ___block_literal_global.213
- ___block_literal_global.262
- ___block_literal_global.392
- ___block_literal_global.394
- ___block_literal_global.601
- ___block_literal_global.609
- ___block_literal_global.621
- ___block_literal_global.623
- ___block_literal_global.785
- ___block_literal_global.979
- _objc_msgSend$vectorGlyphReaderWithURL:error:
- _objc_retain_x26
CStrings:
+ "\n\tname: %@ \n\tnameIdentifier: %d \n\tappearance: %@ \n\tappearanceIdentifier: %d \n\tlocalization: %@ \n\tlocalizationIdentifier: %d \n\tfileURL: %@ \n\tmodificationDate: %@   \n\tidiom: %d \n\tsubtype: %d \n\tscaleFactor: %d \n\tsliceInsets: %@ \n\trenditionType: %d  \n\tresizingMode: %d \n\tresizableSliceSize: %@    \n\tisTemplate: %d \n\tpreservesVectorRepresentation: %d\n\ttemplateRenderingMode: %d \n\toptOutOfThinning: %d \n\talignmentRect: %@ \n\tsizeClassHorizontal: %d \n\tsizeClassVertical: %d  \n\tdisplayGamut: %@ \n\tlayoutDirection: %@   \n\tisFlippable: %d   \n\tmemoryClass: %d \n\tgraphicsFeatureSetClass: %d \n\tcompressionType: %d \n\tlossyCompressionQuality: %f    \n\ttags: %@ \n\tuniversalTypeIdentifier: %@ \n\tcontainedImageNames: %@    \n\tcanvasSize: %@ \n\tlayerReferences: %@ \n\trenditionSubtype: %d \n\tcompressionType: %d\n\tcubeMap: %d\n\ttextureWidth: %d\n\ttextureHeight: %d\n\ttexturePixelFormat: %d textureImportInfos:%@ \n\ticonSize: %@\n\tfontName: %@\n\tfontSize: %d\n\tcolorSpaceId: %d"
+ "-draw-attachment-data"
+ "?"
+ "?0"
+ "@\"CUIVectorGlyphDrawAttachmentDataStore\"16@0:8"
+ "@40@0:8q16q24d32"
+ "ColorStop"
+ "CoreThemeDefinition: TDNamedAssetImportInfo for icon with name '%@' has NO layerReferences it should have at least 1"
+ "CoreThemeDefinition: TDNamedAssetImportInfo group with name '%@' has NO layerReferences it should have at least 1"
+ "Couldn't resolve layer reference pointing to layer '%@' in Layer Stack %@"
+ "IconGroup"
+ "LayerGroupRenditionSpec"
+ "LayerReference %@ contained in '%@' of type '%@' has an empty name for the reference please provide one"
+ "NamedGradientProduction"
+ "NamedGradientRenditionSpec"
+ "ResolvedImageLayerReference"
+ "T@\"NSArray\",C,N,V_colorNames"
+ "T@\"NSArray\",C,N,V_colorStops"
+ "TB,N,V_generateFallbackIcon"
+ "TDColorStop"
+ "TDLayerGroupRenditionSpec"
+ "TDNamedGradientProduction"
+ "TDNamedGradientRenditionSpec"
+ "TDResolvedImageLayerReference"
+ "Td,N,V_gradientAngle"
+ "Tq,N,V_gradientType"
+ "T{CGPoint=dd},N,V_gradientEndPoint"
+ "T{CGPoint=dd},N,V_gradientStartPoint"
+ "Unknown target platform %d"
+ "^{CGColorSpace=}24@0:8Q16"
+ "^{CGSVGNode=}40@0:8{CGPoint=dd}16^{__CFString=}32"
+ "_%@.png"
+ "_addLayerReference:toMutableIconLayerStack:error:"
+ "_addLegacyIconAssetsForLayerStack:error:"
+ "_addLegacyIconAssetsForLayerStackProduction:withName:error:"
+ "_anchorInOutlineCoordinateSpaceForAnchorPoint:glyph:"
+ "_appearanceIconFilesForName"
+ "_colorNames"
+ "_colorStops"
+ "_createAnchorNodeFromPoint:withIdentifier:"
+ "_generateFallbackIcon"
+ "_gradientAngle"
+ "_gradientEndPoint"
+ "_gradientStartPoint"
+ "_gradientType"
+ "_iconLayerStackFromLayerStackRendition:withName:error:"
+ "_namedColorFromColorRendition:"
+ "_namedGradientFromGradientRendition:"
+ "_tempFilesToCleanup"
+ "_testRenditionForP3:"
+ "_vectorGlyphDrawAttachmentDataNodes"
+ "_writeDrawAttachmentDataToRootNode:forWeight:size:glyphNode:scaleFactor:transform:"
+ "_writeRotateAnchorToRootNode:forWeight:size:glyphNode:scaleFactor:transform:"
+ "addLayer:"
+ "anchors"
+ "blurStrength"
+ "cgColor"
+ "color"
+ "colorName"
+ "colorNames"
+ "colorNames count should equal colorStops count'%@'."
+ "colorNames should contain colornames '%@'."
+ "colorStops"
+ "createCGColorSpaceWithIdentifier:"
+ "createFloatDeltasFrom:to:"
+ "createInterpolatedDrawAttachmentDataForWeight:size:scaleFactor:"
+ "createInterpolatedFloatsFromFloats:ultralightDeltas:blackDeltas:withScalars:"
+ "createManagedPointArrayWrapping:"
+ "createNamedGradientProductionsForImportInfos:error:"
+ "createNamedIconLayerStacksForCustomInfos:referenceFiles:bitSource:error:"
+ "createWithPointCount:"
+ "da"
+ "data"
+ "dataAtIndex:"
+ "encodeToSVGNode:"
+ "finalizedIconWithSize:scale:deviceClass:appearance:renderingMode:"
+ "gathersSpecularByElement"
+ "generateFallbackIcon"
+ "gradientAngle"
+ "gradientEndPoint"
+ "gradientEndX"
+ "gradientEndY"
+ "gradientOrColorName"
+ "gradientStartPoint"
+ "gradientStartX"
+ "gradientStartY"
+ "gradientType"
+ "hasLightingEffects"
+ "hasSpecular"
+ "initAdoptingData:anchors:"
+ "initWithContext:"
+ "initWithGradientNamed:type:startPoint:endPoint:colorNames:colorStops:"
+ "initWithName:withSize:atScale:"
+ "initWithSVGNode:"
+ "light"
+ "name.name IN %@"
+ "orderedSet"
+ "rawArray"
+ "renderedLegacyCompatibleIconWithConfiguration:forDeviceClass:"
+ "resolvedFillStyle"
+ "resolvedVariableMode"
+ "setBlurStrength:"
+ "setCGColor:"
+ "setColor:"
+ "setColorName:"
+ "setColorNames:"
+ "setColorStops:"
+ "setColors:andStops:"
+ "setGathersSpecularByElement:"
+ "setGenerateFallbackIcon:"
+ "setGradientAngle:"
+ "setGradientEndPoint:"
+ "setGradientEndX:"
+ "setGradientEndY:"
+ "setGradientOrColorName:"
+ "setGradientStartPoint:"
+ "setGradientStartX:"
+ "setGradientStartY:"
+ "setGradientType:"
+ "setHasLightingEffects:"
+ "setHasSpecular:"
+ "setImage:"
+ "setShadowOpacity:"
+ "setShadowStyle:"
+ "setStack:"
+ "setStop:"
+ "setSvgDocument:"
+ "setSvgDocumentURL:"
+ "setTranslucency:"
+ "shadowOpacity"
+ "shadowStyle"
+ "stop"
+ "svg"
+ "translucency"
+ "unsafeDrawAttachmentAnchors"
+ "unsafeDrawAttachmentData"
+ "urlForRasterizedIconImageStackNamed:"
+ "v104@0:8^{CGSVGNode=}16q24q32^{CGSVGNode=}40d48{CGAffineTransform=dddddd}56"
+ "v32@?0@\"NSURL\"8Q16^B24"
+ "{CGPoint=dd}40@0:8{CGPoint=dd}16^{CGSVGNode=}32"
- "\n\tname: %@ \n\tnameIdentifier: %d \n\tappearance: %@ \n\tappearanceIdentifier: %d \n\tlocalization: %@ \n\tlocalizationIdentifier: %d \n\tfileURL: %@ \n\tmodificationDate: %@   \n\tidiom: %d \n\tsubtype: %d \n\tscaleFactor: %d \n\tsliceInsets: %@ \n\trenditionType: %d  \n\tresizingMode: %d \n\tresizableSliceSize: %@    \n\tisTemplate: %d \n\tpreservesVectorRepresentation: %d\n\ttemplateRenderingMode: %d \n\toptOutOfThinning: %d \n\talignmentRect: %@ \n\tsizeClassHorizontal: %d \n\tsizeClassVertical: %d  \n\tdisplayGamut: %@ \n\tlayoutDirection: %@   \n\tisFlippable: %d   \n\tmemoryClass: %d \n\tgraphicsFeatureSetClass: %d \n\tcompressionType: %d \n\tlossyCompressionQuality: %f    \n\ttags: %@ \n\tuniversalTypeIdentifier: %@ \n\tcontainedImageNames: %@    \n\tcanvasSize: %@ \n\tlayerReferences: %@ \n\trenditionSubtype: %d \n\tcompressionType: %d\n\tcubeMap: %d\n\ttextureWidth: %d\n\ttextureHeight: %d\n\ttexturePixelFormat: %d textureImportInfos:%@ \n\ticonSize: %@\n\tfontName: %@\n\tfontSize: %d"
- "ResolvedLayerReference"
- "TDResolvedLayerReference"
- "Tq,D,N"

```
