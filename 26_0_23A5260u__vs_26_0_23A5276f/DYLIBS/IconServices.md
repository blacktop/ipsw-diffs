## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/IconServices`

```diff

-705.100.0.0.0
-  __TEXT.__text: 0x5ce6c
-  __TEXT.__auth_stubs: 0xfd0
+711.100.0.0.0
+  __TEXT.__text: 0x5eb3c
+  __TEXT.__auth_stubs: 0xf00
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x62b4
-  __TEXT.__const: 0x48f2
+  __TEXT.__objc_methlist: 0x63fc
+  __TEXT.__const: 0x4922
   __TEXT.__gcc_except_tab: 0x40c
-  __TEXT.__cstring: 0x526a
-  __TEXT.__oslogstring: 0x2da4
-  __TEXT.__swift5_typeref: 0x8
-  __TEXT.__unwind_info: 0x16d0
-  __TEXT.__objc_classname: 0x11bb
-  __TEXT.__objc_methname: 0xbcd7
+  __TEXT.__cstring: 0x521a
+  __TEXT.__oslogstring: 0x2e35
+  __TEXT.__unwind_info: 0x1700
+  __TEXT.__eh_frame: 0x88
+  __TEXT.__objc_classname: 0x11d1
+  __TEXT.__objc_methname: 0xbe33
   __TEXT.__objc_methtype: 0x1740
-  __TEXT.__objc_stubs: 0x93c0
-  __DATA_CONST.__got: 0x648
-  __DATA_CONST.__const: 0x9e8
+  __TEXT.__objc_stubs: 0x9540
+  __DATA_CONST.__got: 0x630
+  __DATA_CONST.__const: 0x9c8
   __DATA_CONST.__objc_classlist: 0x518
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f78
+  __DATA_CONST.__objc_selrefs: 0x2fc8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x3c8
-  __DATA_CONST.__objc_arraydata: 0xc08
-  __AUTH_CONST.__auth_got: 0x800
-  __AUTH_CONST.__const: 0xea0
-  __AUTH_CONST.__cfstring: 0x6780
-  __AUTH_CONST.__objc_const: 0x12c60
-  __AUTH_CONST.__objc_intobj: 0x510
-  __AUTH_CONST.__objc_arrayobj: 0xf0
+  __DATA_CONST.__objc_superrefs: 0x3e8
+  __DATA_CONST.__objc_arraydata: 0xc50
+  __AUTH_CONST.__auth_got: 0x798
+  __AUTH_CONST.__const: 0xf60
+  __AUTH_CONST.__cfstring: 0x68a0
+  __AUTH_CONST.__objc_const: 0x12ea8
+  __AUTH_CONST.__objc_intobj: 0x528
+  __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0xae0
-  __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x680
-  __DATA.__data: 0x1c40
-  __DATA.__bss: 0x578
+  __AUTH.__objc_data: 0xaa0
+  __DATA.__objc_ivar: 0x698
+  __DATA.__data: 0x1c28
+  __DATA.__bss: 0x5c8
   __DATA_DIRTY.__objc_data: 0x2850
   __DATA_DIRTY.__data: 0xc
   __DATA_DIRTY.__bss: 0x1f0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0FC3B73F-D276-30DC-85A9-68F863211103
-  Functions: 2398
-  Symbols:   9014
-  CStrings:  4727
+  UUID: 495E0526-0DB4-3B07-90C6-468EDBAB6BBE
+  Functions: 2428
+  Symbols:   9157
+  CStrings:  4756
 
Symbols:
+ +[ISIcon placeholderIcon]
+ +[ISIconDecoration decorationsFromDescriptor:]
+ +[ISPlaceholderIcon sharedInstance]
+ +[ISPlaceholderIcon sharedInstance].cold.1
+ +[ISPlaceholderIcon supportsSecureCoding]
+ +[ISResourceProvider(Convenience) placeholderIconResourceProvider]
+ +[_ISImageIcon supportsSecureCoding]
+ -[CUICatalog(IconServicesAdditions) idiomsForPlatform:].cold.1
+ -[ISBundleResourceProvider _shouldTreatLikeApp]
+ -[ISDefaults prepareImageBagIconsOutOfProcess]
+ -[ISImageBagIcon _remoteGenerateImageWithDescriptor:]
+ -[ISImageBagIcon makeResourceProvider]
+ -[ISLeadingStatusBadgeRecipe badgedDocumentIconRect]
+ -[ISLeadingStatusBadgeRecipe badgedDocumentIconRect].cold.1
+ -[ISLeadingStatusBadgeRecipe badgedFolderIconRect]
+ -[ISLeadingStatusBadgeRecipe badgedFolderIconRect].cold.1
+ -[ISLeadingStatusBadgeRecipe defaultBadgeRect]
+ -[ISLeadingStatusBadgeRecipe defaultBadgeRect].cold.1
+ -[ISLeadingStatusBadgeRecipe init]
+ -[ISLeadingStatusBadgeRecipe primaryIconType]
+ -[ISLeadingStatusBadgeRecipe setPrimaryIconType:]
+ -[ISPlaceholderIcon .cxx_destruct]
+ -[ISPlaceholderIcon initWithCoder:]
+ -[ISPlaceholderIcon init]
+ -[ISPlaceholderIcon makeResourceProvider]
+ -[ISPlaceholderIcon resourceProvider]
+ -[ISRecipeFactory recipeForDecoration:]
+ -[ISRecordResourceProvider _isFolder]
+ -[ISRecordResourceProvider _shouldTreatLikeFolder]
+ -[ISRecordResourceProvider shouldUseFolderRecipe]
+ -[ISResourceProvider _shouldTreatLikeApp]
+ -[ISResourceProvider _shouldTreatLikeFolder]
+ -[ISStaticResources placeholderIconResourceForPlatform:]
+ -[ISStaticResources placeholderIconResourceForPlatform:].cold.1
+ -[ISStaticResources placeholderIconResource]
+ -[ISTrailingStatusBadgeRecipe badgedDocumentIconRect]
+ -[ISTrailingStatusBadgeRecipe badgedDocumentIconRect].cold.1
+ -[ISTrailingStatusBadgeRecipe badgedFolderIconRect]
+ -[ISTrailingStatusBadgeRecipe badgedFolderIconRect].cold.1
+ -[ISTrailingStatusBadgeRecipe defaultBadgeRect]
+ -[ISTrailingStatusBadgeRecipe defaultBadgeRect].cold.1
+ -[ISTrailingStatusBadgeRecipe init]
+ -[ISTrailingStatusBadgeRecipe primaryIconType]
+ -[ISTrailingStatusBadgeRecipe setPrimaryIconType:]
+ -[_ISImageIcon .cxx_destruct]
+ -[_ISImageIcon encodeWithCoder:]
+ -[_ISImageIcon imageData]
+ -[_ISImageIcon initImage:]
+ -[_ISImageIcon initWithCoder:]
+ -[_ISImageIcon makeResourceProvider]
+ -[_ISImageIcon setImageData:]
+ _ISAccelerateIconClassifySpecularWithDebug
+ _ISAccelerateIconComputeIconSegmentationFlag
+ _ISAccelerateIconComputeIconSegmentationFlagForShadows
+ _ISAccelerateIconCreateScaledCGImage
+ _ISAccelerateIconSegmentationComputeAdditionalGradientFlag
+ _ISAccelerateIconSegmentationComputeFlagForMoreConfidence
+ _ISAccelerateIconSegmentationSamples_readAlmostOpaqueSample_i
+ _ISAccelerateIconSegmentationSamples_readSample_i
+ _OBJC_CLASS_$_ISPlaceholderIcon
+ _OBJC_CLASS_$__ISImageIcon
+ _OBJC_IVAR_$_ISLeadingStatusBadgeRecipe._primaryIconType
+ _OBJC_IVAR_$_ISPlaceholderIcon._resourceProvider
+ _OBJC_IVAR_$_ISResourceProvider.__shouldTreatLikeApp
+ _OBJC_IVAR_$_ISResourceProvider.__shouldTreatLikeFolder
+ _OBJC_IVAR_$_ISTrailingStatusBadgeRecipe._primaryIconType
+ _OBJC_IVAR_$__ISImageIcon._imageData
+ _OBJC_METACLASS_$_ISPlaceholderIcon
+ _OBJC_METACLASS_$__ISImageIcon
+ __OBJC_$_CLASS_METHODS_IFImage(GenerationReport|ISScalableCompositorResource|ISPlaceholderImage)
+ __OBJC_$_CLASS_METHODS_ISPlaceholderIcon
+ __OBJC_$_CLASS_METHODS__ISImageIcon
+ __OBJC_$_CLASS_PROP_LIST__ISImageIcon
+ __OBJC_$_INSTANCE_METHODS_IFImage(GenerationReport|ISScalableCompositorResource|ISPlaceholderImage)
+ __OBJC_$_INSTANCE_METHODS_ISPlaceholderIcon
+ __OBJC_$_INSTANCE_METHODS__ISImageIcon
+ __OBJC_$_INSTANCE_VARIABLES_ISLeadingStatusBadgeRecipe
+ __OBJC_$_INSTANCE_VARIABLES_ISPlaceholderIcon
+ __OBJC_$_INSTANCE_VARIABLES_ISTrailingStatusBadgeRecipe
+ __OBJC_$_INSTANCE_VARIABLES__ISImageIcon
+ __OBJC_$_PROP_LIST_ISPlaceholderIcon
+ __OBJC_$_PROP_LIST__ISImageIcon
+ __OBJC_CLASS_PROTOCOLS_$_IFImage(GenerationReport|ISScalableCompositorResource|ISPlaceholderImage)
+ __OBJC_CLASS_PROTOCOLS_$__ISImageIcon
+ __OBJC_CLASS_RO_$_ISPlaceholderIcon
+ __OBJC_CLASS_RO_$__ISImageIcon
+ __OBJC_METACLASS_RO_$_ISPlaceholderIcon
+ __OBJC_METACLASS_RO_$__ISImageIcon
+ ___35+[ISPlaceholderIcon sharedInstance]_block_invoke
+ ___46-[ISLeadingStatusBadgeRecipe defaultBadgeRect]_block_invoke
+ ___47-[ISTrailingStatusBadgeRecipe defaultBadgeRect]_block_invoke
+ ___50-[ISLeadingStatusBadgeRecipe badgedFolderIconRect]_block_invoke
+ ___51-[ISTrailingStatusBadgeRecipe badgedFolderIconRect]_block_invoke
+ ___52-[ISLeadingStatusBadgeRecipe badgedDocumentIconRect]_block_invoke
+ ___53-[ISTrailingStatusBadgeRecipe badgedDocumentIconRect]_block_invoke
+ ___55-[CUICatalog(IconServicesAdditions) idiomsForPlatform:]_block_invoke.82
+ ___block_literal_global.123
+ ___block_literal_global.134
+ ___block_literal_global.136
+ ___block_literal_global.164
+ ___block_literal_global.166
+ ___block_literal_global.77
+ ___block_literal_global.84
+ ___block_literal_global.91
+ ___block_literal_global.94
+ _badgedDocumentIconRect.onceToken
+ _badgedDocumentIconRect.onceToken.75
+ _badgedDocumentIconRect.rect
+ _badgedDocumentIconRect.rect.74
+ _badgedFolderIconRect.onceToken
+ _badgedFolderIconRect.onceToken.79
+ _badgedFolderIconRect.rect
+ _badgedFolderIconRect.rect.78
+ _defaultBadgeRect.onceToken
+ _defaultBadgeRect.onceToken.71
+ _defaultBadgeRect.rect
+ _defaultBadgeRect.rect.70
+ _hintedBadgeRect.onceToken.121
+ _hintedBadgeRect.onceToken.132
+ _hintedBadgeRect.rect.120
+ _hintedBadgeRect.rect.131
+ _idiomsForPlatform:.checkMarketingIdiom
+ _idiomsForPlatform:.onceToken
+ _objc_msgSend$_isFolder
+ _objc_msgSend$_remoteGenerateImageWithDescriptor:
+ _objc_msgSend$_shouldTreatLikeFolder
+ _objc_msgSend$badgedDocumentIconRect
+ _objc_msgSend$badgedFolderIconRect
+ _objc_msgSend$decorationsFromDescriptor:
+ _objc_msgSend$defaultBadgeRect
+ _objc_msgSend$initImage:
+ _objc_msgSend$initWithData:uuid:
+ _objc_msgSend$mode
+ _objc_msgSend$placeholderIconResource
+ _objc_msgSend$placeholderIconResourceForPlatform:
+ _objc_msgSend$placeholderIconResourceProvider
+ _objc_msgSend$prepareImageBagIconsOutOfProcess
+ _objc_msgSend$primaryIconType
+ _objc_msgSend$recipeForDecoration:
+ _objc_msgSend$setPrimaryIconType:
+ _objc_msgSend$shouldUseFolderRecipe
+ _sharedInstance.onceToken.75
+ _sharedInstance.sharedInstance.74
+ _vImageBuffer_Init
+ _vImageBuffer_InitWithCGImage
+ _vImageCreateCGImageFromBuffer
+ _vImageScale_ARGB8888
- -[IFImage(Internal) initWithIconStack:size:scale:]
- -[IFImage(Internal) initWithIconStack:size:scale:].cold.1
- -[ISGenerationRequest(Generation) _decorationRecipeKeyFromTypeIdentifier:position:]
- -[ISLeadingStatusBadgeRecipe leadingBottomBadgeRect].cold.1
- -[ISRecordResourceProvider shouldUseFolderRecipe:]
- -[ISStaticResources cacheMissIconResourceForPlatform:]
- -[ISStaticResources cacheMissIconResourceForPlatform:].cold.1
- -[ISStaticResources cacheMissIconResource]
- -[ISTrailingStatusBadgeRecipe trailingBottomBadgeRect].cold.1
- _OBJC_CLASS_$_ICRIconLayer
- _OBJC_CLASS_$_ISICRIconLayerWrapper
- _OBJC_CLASS_$__ISWrapper_CUINamedIconLayerStack
- _OBJC_METACLASS_$_ISICRIconLayerWrapper
- _OBJC_METACLASS_$__ISWrapper_CUINamedIconLayerStack
- __DATA_ISICRIconLayerWrapper
- __DATA__ISWrapper_CUINamedIconLayerStack
- __INSTANCE_METHODS_ISICRIconLayerWrapper
- __INSTANCE_METHODS__ISWrapper_CUINamedIconLayerStack
- __IVARS_ISICRIconLayerWrapper
- __IVARS__ISWrapper_CUINamedIconLayerStack
- __METACLASS_DATA_ISICRIconLayerWrapper
- __METACLASS_DATA__ISWrapper_CUINamedIconLayerStack
- __OBJC_$_CLASS_METHODS_IFImage(GenerationReport|ISScalableCompositorResource|Internal|ISPlaceholderImage)
- __OBJC_$_INSTANCE_METHODS_IFImage(GenerationReport|ISScalableCompositorResource|Internal|ISPlaceholderImage)
- __OBJC_CLASS_PROTOCOLS_$_IFImage(GenerationReport|ISScalableCompositorResource|Internal|ISPlaceholderImage)
- __PROPERTIES__ISWrapper_CUINamedIconLayerStack
- ___52-[ISLeadingStatusBadgeRecipe leadingBottomBadgeRect]_block_invoke
- ___54-[ISTrailingStatusBadgeRecipe trailingBottomBadgeRect]_block_invoke
- ___block_literal_global.107
- ___block_literal_global.109
- ___block_literal_global.137
- ___block_literal_global.139
- ___block_literal_global.54
- ___block_literal_global.64
- ___block_literal_global.69
- ___swift_instantiateConcreteTypeFromMangledName
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_IconServices
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_IconServices
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_IconServices
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_IconServices
- __swift_stdlib_reportUnimplementedInitializer
- _computeIconSegmentationFlagForMoreConfidence
- _hintedBadgeRect.onceToken.105
- _hintedBadgeRect.onceToken.94
- _hintedBadgeRect.rect.104
- _hintedBadgeRect.rect.93
- _leadingBottomBadgeRect.onceToken
- _leadingBottomBadgeRect.rect
- _objc_allocWithZone
- _objc_msgSend$_decorationRecipeKeyFromTypeIdentifier:position:
- _objc_msgSend$cacheMissIconResourceForPlatform:
- _objc_msgSend$finalizeAtSize:scale:
- _objc_msgSend$initWithIconStack:
- _objc_msgSend$renderCGImageAtSize:scale:
- _objc_msgSend$shouldUseFolderRecipe:
- _objc_opt_self
- _swift_errorRelease
- _swift_getObjCClassFromMetadata
- _swift_getObjCClassMetadata
- _swift_getTypeByMangledNameInContext2
- _swift_release
- _symbolic _____Sg 13IconRendering12ICRIconIdiomO
- _trailingBottomBadgeRect.onceToken
- _trailingBottomBadgeRect.rect
CStrings:
+ "21:34:37"
+ "CHECK_MARKETING_IDIOM"
+ "ISPlaceholderIcon"
+ "Incompatible decoration position/mode combo: p:%lu,m:%lu. Perferring mode..."
+ "Invalid decoration position configuration for resource. Defaulting to trailing bottom..."
+ "Invalid position: %lu. Using default positioning instead.."
+ "PrepareImageBagIconsOutOfProcess"
+ "STATIC_PLACHOLDER_ICON"
+ "T@\"NSData\",&,V_imageData"
+ "TB,R,V__shouldTreatLikeApp"
+ "TB,R,V__shouldTreatLikeFolder"
+ "Tq,V_primaryIconType"
+ "_ISImageIcon"
+ "__shouldTreatLikeApp"
+ "__shouldTreatLikeFolder"
+ "_imageData"
+ "_isFolder"
+ "_primaryIconType"
+ "_remoteGenerateImageWithDescriptor:"
+ "_shouldTreatLikeFolder"
+ "badgedDocumentIconRect"
+ "badgedFolderIconRect"
+ "com.apple.PhotoBooth"
+ "com.apple.SOSBuddy"
+ "com.apple.SupportFlow"
+ "com.apple.VisionProApp"
+ "connection.assistant"
+ "decorationsFromDescriptor:"
+ "defaultBadgeRect"
+ "imageData"
+ "initImage:"
+ "initWithData:uuid:"
+ "inject_alternate_assets"
+ "placeholderIcon"
+ "placeholderIconResource"
+ "placeholderIconResourceForPlatform:"
+ "placeholderIconResourceProvider"
+ "prepareImageBagIconsOutOfProcess"
+ "primaryIconType"
+ "recipeForDecoration:"
+ "setImageData:"
+ "setPrimaryIconType:"
+ "shouldUseFolderRecipe"
+ "stepbystepguides"
+ "visionpro.companion"
- "01:31:22"
- "Failed to construct finalized icon stack"
- "Failed to render icon stack to cgimage"
- "ISICRIconLayerWrapper"
- "Internal"
- "SwiftWrappers_Internal._ISWrapper_CUINamedIconLayerStack"
- "T@\"CUINamedIconLayerStack\",N,R,ViconStack"
- "^{CGImage=}40@0:8{CGSize=dd}16d32"
- "_ISWrapper_CUINamedIconLayerStack"
- "_decorationRecipeKeyFromTypeIdentifier:position:"
- "cacheMissIconResource"
- "cacheMissIconResourceForPlatform:"
- "finalizeAtSize:scale:"
- "init()"
- "initWithIconStack:"
- "initWithIconStack:size:scale:"
- "inject_solarium_assets"
- "makeSnapshot"
- "renderAtSize:scale:"
- "renderCGImageAtSize:scale:"
- "shouldUseFolderRecipe:"

```
