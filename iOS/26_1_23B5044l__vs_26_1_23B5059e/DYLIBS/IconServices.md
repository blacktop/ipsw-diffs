## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/IconServices`

```diff

-732.0.0.0.0
-  __TEXT.__text: 0x61acc
+733.100.0.0.0
+  __TEXT.__text: 0x635b0
   __TEXT.__auth_stubs: 0xf70
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x6504
-  __TEXT.__const: 0x87c2
-  __TEXT.__gcc_except_tab: 0x40c
-  __TEXT.__cstring: 0x3c9a
-  __TEXT.__oslogstring: 0x307b
-  __TEXT.__unwind_info: 0x17b8
+  __TEXT.__objc_methlist: 0x66bc
+  __TEXT.__const: 0x87b2
+  __TEXT.__gcc_except_tab: 0x42c
+  __TEXT.__cstring: 0x3e25
+  __TEXT.__oslogstring: 0x31c6
+  __TEXT.__unwind_info: 0x1848
   __TEXT.__eh_frame: 0x88
-  __TEXT.__objc_classname: 0x11fc
-  __TEXT.__objc_methname: 0xbeb7
-  __TEXT.__objc_methtype: 0x17e9
-  __TEXT.__objc_stubs: 0x9580
+  __TEXT.__objc_classname: 0x1228
+  __TEXT.__objc_methname: 0xbf0f
+  __TEXT.__objc_methtype: 0x1851
+  __TEXT.__objc_stubs: 0x9600
   __DATA_CONST.__got: 0x628
-  __DATA_CONST.__const: 0x9a0
-  __DATA_CONST.__objc_classlist: 0x518
+  __DATA_CONST.__const: 0x9c8
+  __DATA_CONST.__objc_classlist: 0x528
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2fc0
+  __DATA_CONST.__objc_selrefs: 0x2fd0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x3f0
+  __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0xb0
   __AUTH_CONST.__auth_got: 0x7d0
   __AUTH_CONST.__const: 0x1188
-  __AUTH_CONST.__cfstring: 0x3fa0
-  __AUTH_CONST.__objc_const: 0x133d8
+  __AUTH_CONST.__cfstring: 0x4240
+  __AUTH_CONST.__objc_const: 0x13bb0
   __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x910
-  __DATA.__objc_ivar: 0x6a0
+  __DATA.__objc_ivar: 0x6ac
   __DATA.__data: 0x1c88
-  __DATA.__bss: 0x650
-  __DATA_DIRTY.__objc_data: 0x29e0
+  __DATA.__bss: 0x640
+  __DATA_DIRTY.__objc_data: 0x2a80
   __DATA_DIRTY.__data: 0xc
-  __DATA_DIRTY.__bss: 0x1f8
+  __DATA_DIRTY.__bss: 0x208
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 623302F7-47EC-3455-AECD-687E9685242C
-  Functions: 2489
-  Symbols:   9342
-  CStrings:  4107
+  UUID: 9C4BB6DF-6DA7-38F1-8600-58589A62F76A
+  Functions: 2523
+  Symbols:   9466
+  CStrings:  4163
 
Symbols:
+ +[ISIconLayerElement supportsSecureCoding]
+ +[ISIconLayerGroup supportsSecureCoding]
+ +[ISLayeredIcon supportsSecureCoding]
+ -[ISCompositingDescriptor digest:size:]
+ -[ISCompositingDescriptor digest]
+ -[ISDynamicIconStackResource .cxx_destruct]
+ -[ISDynamicIconStackResource _compositingDescriptorWithSize:scale:]
+ -[ISDynamicIconStackResource _compositingDescriptorWithSize:scale:].cold.1
+ -[ISDynamicIconStackResource baseIconStackForSize:scale:]
+ -[ISDynamicIconStackResource compositingDescriptor]
+ -[ISDynamicIconStackResource generationReport]
+ -[ISDynamicIconStackResource iconStackForSize:scale:]
+ -[ISDynamicIconStackResource iconStackForSize:scale:].cold.1
+ -[ISDynamicIconStackResource icrCompositor]
+ -[ISDynamicIconStackResource imageForSize:scale:]
+ -[ISDynamicIconStackResource initWithTypeIdentifier:layerGroups:]
+ -[ISDynamicIconStackResource layerDataForSize:scale:]
+ -[ISDynamicIconStackResource layerGroups]
+ -[ISDynamicIconStackResource platform]
+ -[ISDynamicIconStackResource setCompositingDescriptor:]
+ -[ISDynamicIconStackResource setGenerationReport:]
+ -[ISDynamicIconStackResource setIcrCompositor:]
+ -[ISDynamicIconStackResource typeIdentifier]
+ -[ISICRCompositor .cxx_destruct]
+ -[ISICRCompositor _fallbackImageForSize:scale:]
+ -[ISICRCompositor _finalizedIconForCompositingDescriptor:]
+ -[ISICRCompositor _keyForCompositingDescriptor:]
+ -[ISICRCompositor compositingDescriptor]
+ -[ISICRCompositor finalizedIcons]
+ -[ISICRCompositor iconStack]
+ -[ISICRCompositor imageForCompositingDescriptor:]
+ -[ISICRCompositor initWithIconStackBlock:]
+ -[ISICRCompositor layerDataForCompositingDescriptor:]
+ -[ISICRCompositor layerDataForCompositingDescriptor:].cold.1
+ -[ISICRCompositor setCompositingDescriptor:]
+ -[ISICRCompositor setIconStack:]
+ -[ISIconLayerElement cuiLayerImageForAppearance:size:scale:frame:]
+ -[ISIconLayerElement description]
+ -[ISIconLayerElement digest]
+ -[ISIconLayerElement encodeWithCoder:]
+ -[ISIconLayerElement hash]
+ -[ISIconLayerElement initWithCoder:]
+ -[ISIconLayerElement isEqual:]
+ -[ISIconLayerGroup _IS_cuiShadowStyleFromStyle:]
+ -[ISIconLayerGroup _IS_cuiShadowStyleFromStyle:].cold.1
+ -[ISIconLayerGroup cuiGroupForAppearance:]
+ -[ISIconLayerGroup description]
+ -[ISIconLayerGroup digest]
+ -[ISIconLayerGroup encodeWithCoder:]
+ -[ISIconLayerGroup hash]
+ -[ISIconLayerGroup initWithCoder:]
+ -[ISIconLayerGroup isEqual:]
+ -[ISLayeredIcon description]
+ -[ISLayeredIcon encodeWithCoder:]
+ -[ISLayeredIcon hash]
+ -[ISLayeredIcon initWithCoder:]
+ -[ISLayeredIcon isEqual:]
+ -[ISLayeredIcon makeResourceProvider]
+ GCC_except_table0
+ _OBJC_CLASS_$_ISDynamicIconStackResource
+ _OBJC_CLASS_$_ISICRCompositor
+ _OBJC_IVAR_$_ISDynamicIconStackResource._compositingDescriptor
+ _OBJC_IVAR_$_ISDynamicIconStackResource._icrCompositor
+ _OBJC_IVAR_$_ISDynamicIconStackResource._layerGroups
+ _OBJC_IVAR_$_ISDynamicIconStackResource._typeIdentifier
+ _OBJC_IVAR_$_ISDynamicIconStackResource.generationReport
+ _OBJC_IVAR_$_ISDynamicIconStackResource.platform
+ _OBJC_IVAR_$_ISICRCompositor._compositingDescriptor
+ _OBJC_IVAR_$_ISICRCompositor._finalizedIcons
+ _OBJC_IVAR_$_ISICRCompositor._iconStack
+ _OBJC_METACLASS_$_ISDynamicIconStackResource
+ _OBJC_METACLASS_$_ISICRCompositor
+ __OBJC_$_CLASS_METHODS_ISIconLayerElement
+ __OBJC_$_CLASS_METHODS_ISIconLayerGroup
+ __OBJC_$_CLASS_METHODS_ISLayeredIcon
+ __OBJC_$_CLASS_PROP_LIST_ISIconLayerElement
+ __OBJC_$_CLASS_PROP_LIST_ISIconLayerGroup
+ __OBJC_$_INSTANCE_METHODS_ISDynamicIconStackResource
+ __OBJC_$_INSTANCE_METHODS_ISICRCompositor
+ __OBJC_$_INSTANCE_VARIABLES_ISDynamicIconStackResource
+ __OBJC_$_INSTANCE_VARIABLES_ISICRCompositor
+ __OBJC_$_PROP_LIST_ISDynamicIconStackResource
+ __OBJC_$_PROP_LIST_ISICRCompositor
+ __OBJC_CLASS_PROTOCOLS_$_ISDynamicIconStackResource
+ __OBJC_CLASS_PROTOCOLS_$_ISIconLayerElement
+ __OBJC_CLASS_PROTOCOLS_$_ISIconLayerGroup
+ __OBJC_CLASS_RO_$_ISDynamicIconStackResource
+ __OBJC_CLASS_RO_$_ISICRCompositor
+ __OBJC_METACLASS_RO_$_ISDynamicIconStackResource
+ __OBJC_METACLASS_RO_$_ISICRCompositor
+ ___57-[ISConcreteIcon generateImageWithDescriptor:completion:]_block_invoke.25
+ ___65-[ISDynamicIconStackResource initWithTypeIdentifier:layerGroups:]_block_invoke
+ ___block_descriptor_40_e8_32w_e45_"CUINamedIconLayerStack"32?0{CGSize=dd}8d24lw32l8
+ _objc_msgSend$_finalizedIconForCompositingDescriptor:
+ _objc_msgSend$_keyForCompositingDescriptor:
+ _objc_msgSend$baseIconStackForSize:scale:
+ _objc_msgSend$blurs
+ _objc_msgSend$combineSpeculars
+ _objc_msgSend$cuiGroupForAppearance:
+ _objc_msgSend$cuiLayerImageForAppearance:size:scale:frame:
+ _objc_msgSend$fillColors
+ _objc_msgSend$iconStack
+ _objc_msgSend$icrCompositor
+ _objc_msgSend$imageForCompositingDescriptor:
+ _objc_msgSend$initWithIconStackBlock:
+ _objc_msgSend$initWithLayers:
+ _objc_msgSend$layerDataForCompositingDescriptor:
+ _objc_msgSend$opacities
+ _objc_msgSend$shadowStyles
+ _objc_msgSend$shadows
+ _objc_msgSend$speculars
+ _objc_msgSend$translucencies
- -[ISIconFactory initWithBundleIdentifier:imageLayers:]
- -[ISIconFactory initWithTypeIdentifier:iconLayers:]
- -[ISIconLayerElement fills]
- -[ISIconLayerElement setFills:]
- -[ISLayeredIcon _IS_cuiShadowStyleFromStyle:]
- -[ISLayeredIcon _IS_cuiShadowStyleFromStyle:].cold.1
- -[ISLayeredIcon _generateImageWithDescriptor:]
- -[ISLayeredIcon _generateImageWithDescriptor:].cold.1
- -[ISLayeredIcon _init]
- -[ISLayeredIcon _prepareImagesForImageDescriptors:]
- -[ISLayeredIcon _tweakCopiedImageDescriptorsIfNecessary:]
- -[ISLayeredIcon baseStackForDescriptor:]
- -[ISLayeredIcon baseStackForDescriptor:].cold.1
- -[ISLayeredIcon bundleIdentifier]
- -[ISLayeredIcon bundlePlatform]
- -[ISLayeredIcon getImageForImageDescriptor:completion:]
- -[ISLayeredIcon iconLayers]
- -[ISLayeredIcon iconStackForDescriptor:]
- -[ISLayeredIcon imageCache]
- -[ISLayeredIcon imageForImageDescriptor:]
- -[ISLayeredIcon imageLayers]
- -[ISLayeredIcon initWithBundleIdentifier:imageLayers:]
- -[ISLayeredIcon initWithTypeIdentifier:iconLayers:]
- -[ISLayeredIcon setBundlePlatform:]
- -[ISLayeredIcon setImageCache:]
- _OBJC_IVAR_$_ISIconLayerElement._fills
- _OBJC_IVAR_$_ISLayeredIcon._bundleIdentifier
- _OBJC_IVAR_$_ISLayeredIcon._bundlePlatform
- _OBJC_IVAR_$_ISLayeredIcon._iconLayers
- _OBJC_IVAR_$_ISLayeredIcon._imageCache
- _OBJC_IVAR_$_ISLayeredIcon._imageLayers
- ___57-[ISConcreteIcon generateImageWithDescriptor:completion:]_block_invoke.24
- _objc_msgSend$baseStackForDescriptor:
- _objc_msgSend$bundlePlatform
- _objc_msgSend$hasLightEffects
- _objc_msgSend$iconLayers
- _objc_msgSend$iconStackForDescriptor:
- _objc_msgSend$imageLayers
- _objc_msgSend$initWithBundleIdentifier:imageLayers:
- _objc_msgSend$initWithTypeIdentifier:iconLayers:
- _objc_msgSend$setBundlePlatform:
- _objc_msgSend$setCacheFinalizedIconOnGeneratedImage:
- _objc_msgSend$setHasEffects:
- _objc_msgSend$setHasOverlappingChildSpecularsCombined:
- _objc_msgSend$setLayerGroups:
- _objc_msgSend$setLayers:
- _objc_msgSend$setShadow:
CStrings:
+ "%@ Images: %@ - O:%@, E:%@, C:%@"
+ "%@ Images: %@ - O:%@, S:%@, CS:%@ B:%@ T:%@ SS:%@ S:%@"
+ "%@ Type: %@ LayerGroups: %@"
+ "%@-%.1f-%.1f@%d"
+ "%@_%@"
+ "%@_%d"
+ "'%@' cannot provide icon resources"
+ "21:27:03"
+ "@\"CUINamedIconLayerStack\"32@?0{CGSize=dd}8d24"
+ "@\"ISICRCompositor\""
+ "@24@0:8@?16"
+ "@80@0:8q16{CGSize=dd}24d40{CGRect={CGPoint=dd}{CGSize=dd}}48"
+ "@?"
+ "@?16@0:8"
+ "Failed to find base icon stack resource for '%@'"
+ "Failed to find icon stack"
+ "Failed to generate flatten representation for icon stack %@ with descriptor: %@"
+ "Failed to retrieve base icon stack resource for '%@'"
+ "Failed to serialize finalized icon for icon stack %@ with descriptor: %@"
+ "ISDynamicIconStackResource"
+ "ISICRCompositor"
+ "No base icon stack for '%@'"
+ "No record exists for type: '%@'"
+ "O:%@, S:%@, CS:%@ B:%@ T:%@ SS:%@ S:%@"
+ "Preparing to composite but with no compositing configuration"
+ "T@\"ISICRCompositor\",C,V_icrCompositor"
+ "T@\"NSArray\",R,V_layerGroups"
+ "T@?,C,N,V_iconStack"
+ "TQ,R,Vplatform"
+ "_finalizedIconForCompositingDescriptor:"
+ "_iconStack"
+ "_icrCompositor"
+ "_keyForCompositingDescriptor:"
+ "baseIconStackForSize:scale:"
+ "cuiGroupForAppearance:"
+ "cuiLayerImageForAppearance:size:scale:frame:"
+ "iconStack"
+ "icrCompositor"
+ "imageForCompositingDescriptor:"
+ "initWithIconStackBlock:"
+ "layerDataForCompositingDescriptor:"
+ "opacities: %@, effects: %@"
+ "setIconStack:"
+ "setIcrCompositor:"
- "23:08:24"
- "Failed to finalized ISLayeredIcon icon"
- "No images provided!"
- "T@\"NSArray\",R,V_iconLayers"
- "T@\"NSArray\",R,V_imageLayers"
- "T@\"NSMutableDictionary\",&,V_fills"
- "TQ,V_bundlePlatform"
- "Unknown icon. Failing back to application icon"
- "_bundlePlatform"
- "_fills"
- "_iconLayers"
- "_imageLayers"
- "baseStackForDescriptor:"
- "bundlePlatform"
- "fills"
- "iconLayers"
- "iconStackForDescriptor:"
- "imageLayers"
- "initWithBundleIdentifier:imageLayers:"
- "initWithTypeIdentifier:iconLayers:"
- "setBundlePlatform:"
- "setFills:"

```
