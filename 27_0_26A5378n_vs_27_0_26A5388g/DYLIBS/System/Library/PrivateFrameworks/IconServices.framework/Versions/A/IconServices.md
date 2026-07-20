## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-785.0.0.0.0
-  __TEXT.__text: 0x82950
+788.0.0.0.0
+  __TEXT.__text: 0x823c0
   __TEXT.__delay_stubs: 0x80
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x78dc
+  __TEXT.__objc_methlist: 0x78c4
   __TEXT.__const: 0x9570
-  __TEXT.__cstring: 0x5478
-  __TEXT.__oslogstring: 0x4000
-  __TEXT.__gcc_except_tab: 0x8c4
-  __TEXT.__unwind_info: 0x1dc8
+  __TEXT.__cstring: 0x5575
+  __TEXT.__oslogstring: 0x3cc1
+  __TEXT.__gcc_except_tab: 0x904
+  __TEXT.__unwind_info: 0x1de0
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6d0
+  __DATA_CONST.__const: 0x6e8
   __DATA_CONST.__objc_classlist: 0x5c8
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37c0
+  __DATA_CONST.__objc_selrefs: 0x37c8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x480
-  __DATA_CONST.__objc_arraydata: 0xc8
+  __DATA_CONST.__objc_superrefs: 0x488
+  __DATA_CONST.__objc_arraydata: 0xb0
   __DATA_CONST.__got: 0x840
-  __AUTH_CONST.__const: 0x1ae8
-  __AUTH_CONST.__cfstring: 0x5dc0
-  __AUTH_CONST.__objc_const: 0x16b18
+  __AUTH_CONST.__const: 0x1b18
+  __AUTH_CONST.__cfstring: 0x5f20
+  __AUTH_CONST.__objc_const: 0x16b48
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_intobj: 0x6d8
-  __AUTH_CONST.__objc_arrayobj: 0x120
+  __AUTH_CONST.__objc_intobj: 0x690
+  __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__auth_got: 0xb48
   __AUTH.__objc_data: 0xcd0
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x794
+  __DATA.__objc_ivar: 0x798
   __DATA.__data: 0x211c
   __DATA.__bss: 0x770
   __DATA_DIRTY.__objc_data: 0x2d00

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3035
-  Symbols:   7310
-  CStrings:  1278
+  Functions: 3034
+  Symbols:   7313
+  CStrings:  1280
 
Symbols:
+ -[ICRFinalizedIcon(IconServicesAdditions) _IS_imageWithCompositingDescriptor:debugResourceVariant:]
+ -[ISGenericRecipe isDebugModeEnabled]
+ -[ISGenericRecipe setDebugModeEnabled:]
+ -[ISICRCompositor _fallbackImageForSize:scale:debugResourceVariant:]
+ -[ISICRCompositor _finalizedIconForCompositingDescriptor:producedStack:]
+ -[ISICRCompositor assetDescription]
+ -[ISICRCompositor initWithIconStackBlock:assetDescription:]
+ -[ISIconStackAssetCatalogResource _assetDescription]
+ -[ISIconStackAssetCatalogResource icrCompositor]
+ -[ISIconStackAssetCatalogResource setIcrCompositor:]
+ -[ISIconStackCompositeResource icrCompositor]
+ -[ISIconStackCompositeResource setIcrCompositor:]
+ -[ISMultisizedAppAssetCatalogResource _assetDescription]
+ GCC_except_table63
+ OBJC_IVAR_$_ISGenericRecipe._debugModeEnabled
+ OBJC_IVAR_$_ISICRCompositor._assetDescription
+ OBJC_IVAR_$_ISIconStackAssetCatalogResource._icrCompositor
+ OBJC_IVAR_$_ISIconStackCompositeResource._icrCompositor
+ _ISIsTransparent
+ ___58-[ISIconStackCompositeResource initWithResource:platform:]_block_invoke
+ ___70-[ISIconStackAssetCatalogResource initWithCatalog:imageName:platform:]_block_invoke
+ ___99-[ICRFinalizedIcon(IconServicesAdditions) _IS_imageWithCompositingDescriptor:debugResourceVariant:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48s_e15_^{CGImage=}8?0l
+ __typeForSiriMode
+ _objc_msgSend$_IS_imageWithCompositingDescriptor:debugResourceVariant:
+ _objc_msgSend$_assetDescription
+ _objc_msgSend$_fallbackImageForSize:scale:debugResourceVariant:
+ _objc_msgSend$_finalizedIconForCompositingDescriptor:producedStack:
+ _objc_msgSend$assetDescription
+ _objc_msgSend$desiredOrchestrationModeIfEnabled
+ _objc_msgSend$initWithIconStackBlock:assetDescription:
+ _objc_msgSend$isDebugModeEnabled
+ _objc_msgSend$setDebugModeEnabled:
- -[CUINamedIconLayerStack(IconServicesAdditions) _IS_imageWithCompositingDescriptor:]
- -[ICRFinalizedIcon(IconServicesAdditions) _IS_imageWithCompositingDescriptor:]
- -[ISICRCompositor _fallbackImageForSize:scale:]
- -[ISICRCompositor _finalizedIconForCompositingDescriptor:]
- -[ISICRCompositor compositingDescriptor]
- -[ISICRCompositor initWithIconStackBlock:]
- -[ISICRCompositor setCompositingDescriptor:]
- -[ISIconStackAssetCatalogResource _fallbackImageForSize:scale:]
- -[ISIconStackAssetCatalogResource _finalizedIconForSize:scale:]
- -[ISIconStackAssetCatalogResource _keyForSize:scale:]
- -[ISIconStackAssetCatalogResource finalizedIcons]
- -[ISIconStackCompositeResource _fallbackImageForSize:scale:]
- -[ISIconStackCompositeResource _finalizedIconForSize:scale:]
- -[ISIconStackCompositeResource _keyForSize:scale:]
- -[ISIconStackCompositeResource finalizedIcons]
- GCC_except_table62
- OBJC_IVAR_$_ISICRCompositor._compositingDescriptor
- OBJC_IVAR_$_ISIconStackAssetCatalogResource._finalizedIcons
- OBJC_IVAR_$_ISIconStackCompositeResource._finalizedIcons
- _OUTLINED_FUNCTION_7
- _objc_msgSend$_IS_imageWithCompositingDescriptor:
- _objc_msgSend$_fallbackImageForSize:scale:
- _objc_msgSend$_finalizedIconForCompositingDescriptor:
- _objc_msgSend$_finalizedIconForSize:scale:
- _objc_msgSend$_keyForSize:scale:
- _objc_msgSend$borderWidth
- _objc_msgSend$desiredOrchestrationMode
- _objc_msgSend$initWithIconStackBlock:
- _objc_msgSend$initWithLineWidth:color:
- _objc_msgSend$missingDesiredCapabilitiesFor:
CStrings:
+ "Central pixel is still transparent even with retry."
+ "CompositeStack"
+ "DynamicStack"
+ "Failed to generate flatten representation for icon stack %@ with descriptor: %@ for asset type: %@"
+ "Flattened representation is seemingly a fully transparent image: %@"
+ "GenericAppIcon_iOS_Debug_IR_Finalization_Failure"
+ "GenericAppIcon_iOS_Debug_IR_Render_Failure"
+ "GenericAppIcon_iOS_Debug_Transparent"
+ "IR_FinalizationFailed"
+ "IR_RenderFailed"
+ "IR_TransparentRender"
+ "MultisizeImageCompositeStack"
+ "NaturalStack"
+ "Siri availability reported desiredOrchestrationModeIfEnabled: %@ (%lu)"
+ "^{CGImage=}8@?0"
+ "debug layer"
+ "figure.skating"
- "%.1f-%.1f@%d"
- "After interpretation, final Siri mode is %@ (%lu), creating icon from that"
- "Default case, requesting ISAliasedTypeIcon with type com.apple.application-icon.siri-gen1"
- "EnhancedGlass"
- "Failed to find icon stack for with named: %@ for size: (%f,%f) scale:(%lf)"
- "Failed to generate flatten representation for composite icon stack size: (%f,%f) scale:(%lf)"
- "Failed to generate flatten representation for icon stack %@ with descriptor: %@"
- "Failed to generate flatten representation for icon stack with named: %@ for size: (%f,%f) scale:(%lf)"
- "Failed to generate flatten representation for multisized image with named: %@ for size: (%f,%f) scale:(%lf)"
- "Failed to generate icon stack for composite resource for size: (%f,%f) scale:(%lf)"
- "SOSiriOrchestrationModeLinwood, requesting ISAliasedTypeIcon with type com.apple.application-icon.siri-gen2"
- "SOSiriOrchestrationModeSiriClassic, requesting ISAliasedTypeIcon with type com.apple.application-icon.siri-gen1"
- "SOSiriOrchestrationModeSystemAssistantExperience, requesting ISAliasedTypeIcon with type com.apple.application-icon.siri-intelligence"
- "Siri availability reported desiredOrchestrationMode %@ (%lu)"
- "SolariumCornerRadius"
```
