## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/IconServices`

```diff

-711.100.0.0.0
-  __TEXT.__text: 0x5eb3c
-  __TEXT.__auth_stubs: 0xf00
+714.101.0.0.0
+  __TEXT.__text: 0x5fa58
+  __TEXT.__auth_stubs: 0xf50
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x63fc
-  __TEXT.__const: 0x4922
+  __TEXT.__objc_methlist: 0x648c
+  __TEXT.__const: 0x493a
   __TEXT.__gcc_except_tab: 0x40c
-  __TEXT.__cstring: 0x521a
-  __TEXT.__oslogstring: 0x2e35
-  __TEXT.__unwind_info: 0x1700
+  __TEXT.__cstring: 0x5202
+  __TEXT.__oslogstring: 0x3037
+  __TEXT.__unwind_info: 0x1788
   __TEXT.__eh_frame: 0x88
-  __TEXT.__objc_classname: 0x11d1
-  __TEXT.__objc_methname: 0xbe33
-  __TEXT.__objc_methtype: 0x1740
-  __TEXT.__objc_stubs: 0x9540
-  __DATA_CONST.__got: 0x630
+  __TEXT.__objc_classname: 0x1224
+  __TEXT.__objc_methname: 0xbea6
+  __TEXT.__objc_methtype: 0x1775
+  __TEXT.__objc_stubs: 0x9560
+  __DATA_CONST.__got: 0x638
   __DATA_CONST.__const: 0x9c8
-  __DATA_CONST.__objc_classlist: 0x518
+  __DATA_CONST.__objc_classlist: 0x520
   __DATA_CONST.__objc_catlist: 0xf0
-  __DATA_CONST.__objc_protolist: 0x100
+  __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2fc8
-  __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x3e8
+  __DATA_CONST.__objc_selrefs: 0x2fe8
+  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_superrefs: 0x3f0
   __DATA_CONST.__objc_arraydata: 0xc50
-  __AUTH_CONST.__auth_got: 0x798
+  __AUTH_CONST.__auth_got: 0x7c0
   __AUTH_CONST.__const: 0xf60
-  __AUTH_CONST.__cfstring: 0x68a0
-  __AUTH_CONST.__objc_const: 0x12ea8
+  __AUTH_CONST.__cfstring: 0x6880
+  __AUTH_CONST.__objc_const: 0x13200
   __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0xaa0
-  __DATA.__objc_ivar: 0x698
-  __DATA.__data: 0x1c28
+  __AUTH.__objc_data: 0xaf0
+  __DATA.__objc_ivar: 0x694
+  __DATA.__data: 0x1c88
   __DATA.__bss: 0x5c8
   __DATA_DIRTY.__objc_data: 0x2850
   __DATA_DIRTY.__data: 0xc

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 495E0526-0DB4-3B07-90C6-468EDBAB6BBE
-  Functions: 2428
-  Symbols:   9157
-  CStrings:  4756
+  UUID: 40C74EE7-CE30-3635-AC35-6A19B2325327
+  Functions: 2440
+  Symbols:   9209
+  CStrings:  4766
 
Symbols:
+ +[ISAssetCatalogResource assetCatalogResourceWithURL:imageName:platform:isAppLike:error:]
+ +[ISAssetCatalogResource assetCatalogResourceWithURL:imageName:platform:isAppLike:error:].cold.1
+ +[ISAssetCatalogResource assetCatalogResourceWithURL:imageName:platform:isAppLike:error:].cold.2
+ -[ISAssetCatalogResource setPlatform:]
+ -[ISAssetInspector(Accessibility) assetExistsForSize:scale:]
+ -[ISCompositingDescriptor cacheFinalizedIconOnGeneratedImage]
+ -[ISCompositingDescriptor setCacheFinalizedIconOnGeneratedImage:]
+ -[ISCompositor graphicsContextPreset]
+ -[ISCompositor setGraphicsContextPreset:]
+ -[ISGenerationRequest(Generation) compositorElementsForDecorations:primaryIconResourceProvider:imageDescriptor:]
+ -[ISIconStackAssetCatalogResource .cxx_destruct]
+ -[ISIconStackAssetCatalogResource _compositingDescriptorWithSize:scale:]
+ -[ISIconStackAssetCatalogResource _finalizedIconForSize:scale:]
+ -[ISIconStackAssetCatalogResource _keyForSize:scale:]
+ -[ISIconStackAssetCatalogResource finalizedIcons]
+ -[ISIconStackAssetCatalogResource initWithCatalog:imageName:platform:]
+ -[ISIconStackAssetCatalogResource layerDataForSize:scale:]
+ -[ISIconStackCompositeResource _finalizedIconForSize:scale:]
+ -[ISIconStackCompositeResource _keyForSize:scale:]
+ -[ISIconStackCompositeResource finalizedIcons]
+ -[ISIconStackCompositeResource initWithResource:platform:]
+ -[ISIconStackCompositeResource layerDataForSize:scale:]
+ -[ISMultisizedAppAssetCatalogResource _compositingDescriptorWithSize:scale:]
+ -[ISMultisizedAppAssetCatalogResource _lookupForSize:scale:]
+ -[ISMultisizedAppAssetCatalogResource iconStackForSize:scale:]
+ -[ISMultisizedAppAssetCatalogResource imageForSize:scale:]
+ -[ISRecordResourceProvider _isAppClip]
+ _Lanczos2
+ _NewLanczos2Filter
+ _OBJC_CLASS_$_ISMultisizedAppAssetCatalogResource
+ _OBJC_IVAR_$_ISCompositingDescriptor._cacheFinalizedIconOnGeneratedImage
+ _OBJC_IVAR_$_ISCompositor._graphicsContextPreset
+ _OBJC_IVAR_$_ISIconStackAssetCatalogResource._finalizedIcons
+ _OBJC_IVAR_$_ISIconStackCompositeResource._finalizedIcons
+ _OBJC_METACLASS_$_ISMultisizedAppAssetCatalogResource
+ _UTTypeData
+ __OBJC_$_INSTANCE_METHODS_ISAssetInspector(AppReview|Accessibility)
+ __OBJC_$_INSTANCE_METHODS_ISMultisizedAppAssetCatalogResource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ISLayerScalableCompositorResource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ISLayerScalableCompositorResource
+ __OBJC_$_PROTOCOL_REFS_ISLayerScalableCompositorResource
+ __OBJC_CLASS_RO_$_ISMultisizedAppAssetCatalogResource
+ __OBJC_LABEL_PROTOCOL_$_ISLayerScalableCompositorResource
+ __OBJC_METACLASS_RO_$_ISMultisizedAppAssetCatalogResource
+ __OBJC_PROTOCOL_$_ISLayerScalableCompositorResource
+ __OBJC_PROTOCOL_REFERENCE_$_ISLayerScalableCompositorResource
+ ___89+[ISAssetCatalogResource assetCatalogResourceWithURL:imageName:platform:isAppLike:error:]_block_invoke
+ ___block_literal_global.233
+ ___block_literal_global.235
+ _objc_msgSend$_compositingDescriptorWithSize:scale:
+ _objc_msgSend$_finalizedIconForSize:scale:
+ _objc_msgSend$_isAppClip
+ _objc_msgSend$_keyForSize:scale:
+ _objc_msgSend$assetCatalogResourceWithURL:imageName:platform:isAppLike:error:
+ _objc_msgSend$cacheFinalizedIconOnGeneratedImage
+ _objc_msgSend$compositorElementsForDecorations:primaryIconResourceProvider:imageDescriptor:
+ _objc_msgSend$finalizedIcons
+ _objc_msgSend$graphicsContextPreset
+ _objc_msgSend$initWithResource:platform:
+ _objc_msgSend$layerDataForSize:scale:
+ _objc_msgSend$renderedFullBleedIconWithConfiguration:excludeChicletSpecularHighlights:
+ _objc_msgSend$resourceProviderWithTypeIdentifier:options:
+ _objc_msgSend$setCacheFinalizedIconOnGeneratedImage:
+ _objc_msgSend$setGraphicsContextPreset:
+ _sinf
+ _vImageDestroyResamplingFilter
+ _vImageGetResamplingFilterSize
+ _vImageHorizontalShear_ARGB8888
+ _vImageNewResamplingFilterForFunctionUsingBuffer
+ _vImageVerticalShear_ARGB8888
- +[ISAssetCatalogResource assetCatalogResourceWithURL:imageName:platform:error:].cold.1
- +[ISAssetCatalogResource assetCatalogResourceWithURL:imageName:platform:error:].cold.2
- -[ICRFinalizedIcon(IconServicesAdditions) _IS_imageWithCompositingDescriptor:].cold.2
- -[ISCompositingDescriptor serializeLayerObjectForCaching]
- -[ISCompositingDescriptor setSerializeLayerObjectForCaching:]
- -[ISIconStackAssetCatalogResource setUsesExternalCompositor:]
- -[ISMultisizedAssetCatalogResource _iconStackComposerForNamedImage:]
- -[ISMultisizedAssetCatalogResource _imageForMultisizeImage:size:scale:]
- -[ISMultisizedAssetCatalogResource extrapolateIconStack]
- -[ISMultisizedAssetCatalogResource iconStackForSize:scale:]
- -[ISMultisizedAssetCatalogResource setExtrapolateIconStack:]
- -[ISMultisizedAssetCatalogResource setUsesExternalCompositor:]
- -[ISMultisizedAssetCatalogResource usesExternalCompositor]
- -[ISRecordResourceProvider externalCompositingResource]
- -[ISRecordResourceProvider layeredIconResource]
- -[ISRecordResourceProvider setLayeredIconResource:]
- -[ISResourceProvider externalCompositingResource]
- _OBJC_IVAR_$_ISCompositingDescriptor._serializeLayerObjectForCaching
- _OBJC_IVAR_$_ISMultisizedAssetCatalogResource._extrapolateIconStack
- _OBJC_IVAR_$_ISMultisizedAssetCatalogResource._usesExternalCompositor
- _OBJC_IVAR_$_ISRecordResourceProvider._layeredIconResource
- _OBJC_IVAR_$_ISResourceProvider._externalCompositingResource
- __OBJC_$_INSTANCE_METHODS_ISAssetInspector(AppReview)
- __OBJC_$_INSTANCE_VARIABLES_ISMultisizedAssetCatalogResource
- __OBJC_$_PROP_LIST_ISMultisizedAssetCatalogResource
- __OBJC_CLASS_PROTOCOLS_$_ISMultisizedAssetCatalogResource
- ___79+[ISAssetCatalogResource assetCatalogResourceWithURL:imageName:platform:error:]_block_invoke
- ___block_literal_global.246
- ___block_literal_global.248
- _objc_msgSend$ICRIconLayer
- _objc_msgSend$_iconStackComposerForNamedImage:
- _objc_msgSend$_imageForMultisizeImage:size:scale:
- _objc_msgSend$externalCompositingResource
- _objc_msgSend$extrapolateIconStack
- _objc_msgSend$imageForCompositingDescriptor:
- _objc_msgSend$initWithEffects:
- _objc_msgSend$layeredIconResource
- _objc_msgSend$renderedFullBleedIconWithConfiguration:
- _objc_msgSend$serializeLayerObjectForCaching
- _objc_msgSend$setExtrapolateIconStack:
- _objc_msgSend$setSerializeLayerObjectForCaching:
- _objc_msgSend$setUsesExternalCompositor:
- _objc_msgSend$usesExternalCompositor
- _vImageScale_ARGB8888
CStrings:
+ "%.1f-%.1f@%d"
+ "21:02:54"
+ "@\"NSData\"40@0:8{CGSize=dd}16d32"
+ "@52@0:8@16@24Q32B40^@44"
+ "Accessibility"
+ "B40@0:8{CGSize=dd}16d32"
+ "Failed to generate flatten representation for composite icon stack size: (%f,%f) scale:(%lf)"
+ "Failed to generate flatten representation for icon stack with named: %@ for size: (%f,%f) scale:(%lf)"
+ "Failed to generate flatten representation for multisized image with named: %@ for size: (%f,%f) scale:(%lf)"
+ "Failed to generate icon stack for composite resource for size: (%f,%f) scale:(%lf)"
+ "Failed to serialize finalized composite icon for size: (%f,%f) scale:(%lf). Error:%@"
+ "Failed to serialize finalized icon for named: %@ for size: (%f,%f) scale:(%lf). Error:%@"
+ "ISLayerScalableCompositorResource"
+ "ISMultisizedAppAssetCatalogResource"
+ "Incompatible decoration position/mode combo: p:%lu,m:%lu. Preferring mode..."
+ "T@\"NSMutableDictionary\",R,V_finalizedIcons"
+ "TB,R,N,V_usesExternalCompositor"
+ "TB,V_cacheFinalizedIconOnGeneratedImage"
+ "TQ,V_graphicsContextPreset"
+ "_cacheFinalizedIconOnGeneratedImage"
+ "_compositingDescriptorWithSize:scale:"
+ "_finalizedIconForSize:scale:"
+ "_finalizedIcons"
+ "_graphicsContextPreset"
+ "_isAppClip"
+ "_keyForSize:scale:"
+ "assetCatalogResourceWithURL:imageName:platform:isAppLike:error:"
+ "assetExistsForSize:scale:"
+ "cacheFinalizedIconOnGeneratedImage"
+ "com.apple.graphic-icon"
+ "compositorElementsForDecorations:primaryIconResourceProvider:imageDescriptor:"
+ "finalizedIcons"
+ "graphicsContextPreset"
+ "initWithResource:platform:"
+ "layerDataForSize:scale:"
+ "renderedFullBleedIconWithConfiguration:excludeChicletSpecularHighlights:"
+ "setCacheFinalizedIconOnGeneratedImage:"
+ "setGraphicsContextPreset:"
- "21:34:37"
- "@48@0:8@16{CGSize=dd}24d40"
- "AppClipCenterMask"
- "Center Image Background"
- "Center Image mask"
- "Failed to serialize finalized icon. Error: %@"
- "ICRIconLayer"
- "Incompatible decoration position/mode combo: p:%lu,m:%lu. Perferring mode..."
- "T@\"<ISScalableCompositorResource>\",&,N,V_layeredIconResource"
- "T@\"<ISScalableCompositorResource>\",R,V_externalCompositingResource"
- "TB,V_extrapolateIconStack"
- "TB,V_serializeLayerObjectForCaching"
- "TB,V_usesExternalCompositor"
- "_externalCompositingResource"
- "_extrapolateIconStack"
- "_iconStackComposerForNamedImage:"
- "_imageForMultisizeImage:size:scale:"
- "_layeredIconResource"
- "_serializeLayerObjectForCaching"
- "externalCompositingResource"
- "extrapolateIconStack"
- "layeredIconResource"
- "renderedFullBleedIconWithConfiguration:"
- "serializeLayerObjectForCaching"
- "setExtrapolateIconStack:"
- "setLayeredIconResource:"
- "setSerializeLayerObjectForCaching:"

```
