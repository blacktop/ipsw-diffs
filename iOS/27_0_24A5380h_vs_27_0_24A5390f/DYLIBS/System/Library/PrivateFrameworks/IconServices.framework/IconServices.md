## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/IconServices`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-785.0.100.0.0
-  __TEXT.__text: 0x670e4
+788.0.0.0.0
+  __TEXT.__text: 0x66840
   __TEXT.__delay_stubs: 0x80
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x6964
+  __TEXT.__objc_methlist: 0x6934
   __TEXT.__const: 0x8840
-  __TEXT.__cstring: 0x44f1
-  __TEXT.__oslogstring: 0x406a
-  __TEXT.__gcc_except_tab: 0x610
-  __TEXT.__unwind_info: 0x19c8
+  __TEXT.__cstring: 0x45c3
+  __TEXT.__oslogstring: 0x3cb3
+  __TEXT.__gcc_except_tab: 0x650
+  __TEXT.__unwind_info: 0x19d8
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa38
+  __DATA_CONST.__const: 0xa50
   __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_catlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3180
+  __DATA_CONST.__objc_selrefs: 0x3178
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x400
-  __DATA_CONST.__objc_arraydata: 0xc8
+  __DATA_CONST.__objc_superrefs: 0x408
+  __DATA_CONST.__objc_arraydata: 0xb0
   __DATA_CONST.__got: 0x6a8
   __AUTH_CONST.__const: 0x11a8
-  __AUTH_CONST.__cfstring: 0x48a0
+  __AUTH_CONST.__cfstring: 0x49c0
   __AUTH_CONST.__objc_const: 0x13f98
-  __AUTH_CONST.__objc_intobj: 0x570
-  __AUTH_CONST.__objc_arrayobj: 0x120
+  __AUTH_CONST.__objc_intobj: 0x528
+  __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__auth_got: 0x7f0
   __AUTH.__objc_data: 0x870

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2606
-  Symbols:   6202
-  CStrings:  1079
+  Functions: 2599
+  Symbols:   6198
+  CStrings:  1076
 
Symbols:
+ -[ICRFinalizedIcon(IconServicesAdditions) _IS_imageWithCompositingDescriptor:debugResourceVariant:]
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
+ GCC_except_table54
+ _OBJC_IVAR_$_ISICRCompositor._assetDescription
+ _OBJC_IVAR_$_ISIconStackAssetCatalogResource._icrCompositor
+ _OBJC_IVAR_$_ISIconStackCompositeResource._icrCompositor
+ ___58-[ISIconStackCompositeResource initWithResource:platform:]_block_invoke
+ ___70-[ISIconStackAssetCatalogResource initWithCatalog:imageName:platform:]_block_invoke
+ ___99-[ICRFinalizedIcon(IconServicesAdditions) _IS_imageWithCompositingDescriptor:debugResourceVariant:]_block_invoke
+ __typeForSiriMode
+ _objc_msgSend$_IS_imageWithCompositingDescriptor:debugResourceVariant:
+ _objc_msgSend$_assetDescription
+ _objc_msgSend$_fallbackImageForSize:scale:debugResourceVariant:
+ _objc_msgSend$_finalizedIconForCompositingDescriptor:producedStack:
+ _objc_msgSend$assetDescription
+ _objc_msgSend$desiredOrchestrationModeIfEnabled
+ _objc_msgSend$initWithIconStackBlock:assetDescription:
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
- GCC_except_table53
- _OBJC_IVAR_$_ISICRCompositor._compositingDescriptor
- _OBJC_IVAR_$_ISIconStackAssetCatalogResource._finalizedIcons
- _OBJC_IVAR_$_ISIconStackCompositeResource._finalizedIcons
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- ___78-[ICRFinalizedIcon(IconServicesAdditions) _IS_imageWithCompositingDescriptor:]_block_invoke
- _objc_msgSend$_IS_imageWithCompositingDescriptor:
- _objc_msgSend$_fallbackImageForSize:scale:
- _objc_msgSend$_finalizedIconForCompositingDescriptor:
- _objc_msgSend$_finalizedIconForSize:scale:
- _objc_msgSend$_keyForSize:scale:
- _objc_msgSend$desiredOrchestrationMode
- _objc_msgSend$initWithIconStackBlock:
- _objc_msgSend$missingDesiredCapabilitiesFor:
CStrings:
+ "20:59:25"
+ "CompositeStack"
+ "DynamicStack"
+ "Failed to generate flatten representation for icon stack %@ with descriptor: %@ for asset type: %@"
+ "GenericAppIcon_iOS_Debug_IR_Finalization_Failure"
+ "GenericAppIcon_iOS_Debug_IR_Render_Failure"
+ "GenericAppIcon_iOS_Debug_Transparent"
+ "IR_FinalizationFailed"
+ "IR_RenderFailed"
+ "IR_TransparentRender"
+ "MultisizeImageCompositeStack"
+ "NaturalStack"
+ "Siri availability reported desiredOrchestrationModeIfEnabled: %@ (%lu)"
- "%.1f-%.1f@%d"
- "12:43:35"
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
