## MediaControls

> `/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls`

```diff

-4023.510.2.0.0
-  __TEXT.__text: 0xd73a0
+4023.610.3.0.0
+  __TEXT.__text: 0xd82ac
   __TEXT.__auth_stubs: 0x1230
-  __TEXT.__objc_methlist: 0x10af0
-  __TEXT.__cstring: 0x44d9
+  __TEXT.__objc_methlist: 0x10c00
+  __TEXT.__cstring: 0x44ea
   __TEXT.__ustring: 0x30
-  __TEXT.__const: 0xc80
-  __TEXT.__gcc_except_tab: 0x1298
-  __TEXT.__oslogstring: 0x578d
+  __TEXT.__const: 0xca0
+  __TEXT.__gcc_except_tab: 0x12a0
+  __TEXT.__oslogstring: 0x5873
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__unwind_info: 0x377c
+  __TEXT.__unwind_info: 0x3828
   __TEXT.__objc_classname: 0x247a
-  __TEXT.__objc_methname: 0x2c259
+  __TEXT.__objc_methname: 0x2c60c
   __TEXT.__objc_methtype: 0x7ac4
-  __TEXT.__objc_stubs: 0x1a540
-  __DATA_CONST.__got: 0x530
-  __DATA_CONST.__const: 0x2d20
+  __TEXT.__objc_stubs: 0x1a740
+  __DATA_CONST.__got: 0x538
+  __DATA_CONST.__const: 0x2d48
   __DATA_CONST.__objc_classlist: 0x640
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x370
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x38918
-  __DATA_CONST.__objc_selrefs: 0x8b20
+  __DATA_CONST.__objc_const: 0x38a50
+  __DATA_CONST.__objc_selrefs: 0x8bd8
   __DATA_CONST.__objc_classrefs: 0xcb8
   __DATA_CONST.__objc_superrefs: 0x5b0
   __DATA_CONST.__objc_arraydata: 0x168
-  __AUTH_CONST.__cfstring: 0x4a00
+  __AUTH_CONST.__cfstring: 0x4a20
   __AUTH_CONST.__const: 0xb80
   __AUTH_CONST.__objc_const: 0x44e0
   __AUTH_CONST.__objc_intobj: 0x1e0

   __AUTH_CONST.__auth_got: 0x928
   __AUTH.__objc_data: 0x11f8
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x1774
-  __DATA.__data: 0x2968
-  __DATA.__bss: 0x79
+  __DATA.__objc_ivar: 0x1794
+  __DATA.__data: 0x2970
+  __DATA.__bss: 0x71
   __DATA_DIRTY.__objc_data: 0x2c88
   __DATA_DIRTY.__data: 0x38
   __DATA_DIRTY.__bss: 0x218

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 25832662-C439-3B8A-9B8D-BC5AB6165F6A
-  Functions: 6305
-  Symbols:   21881
-  CStrings:  9808
+  UUID: 00E5C448-CBE3-3436-A6AB-82322437C255
+  Functions: 6330
+  Symbols:   21955
+  CStrings:  9852
 
Symbols:
+ -[MRUActivityNowPlayingViewController artworkTransitionDirection]
+ -[MRUActivityNowPlayingViewController didTapTransportButton:]
+ -[MRUActivityNowPlayingViewController lastLeftButtonTapDate]
+ -[MRUActivityNowPlayingViewController setLastLeftButtonTapDate:]
+ -[MRUFlippingArtworkLayer artworkStyle]
+ -[MRUFlippingArtworkLayer backLegibilityLayer]
+ -[MRUFlippingArtworkLayer frontLegibilityLayer]
+ -[MRUFlippingArtworkLayer makeDynamicIslandLegibilityFilter]
+ -[MRUFlippingArtworkLayer makeLegibilityLayer]
+ -[MRUFlippingArtworkLayer setArtworkStyle:]
+ -[MRUFlippingArtworkLayer setBackLegibilityLayer:]
+ -[MRUFlippingArtworkLayer setFrontLegibilityLayer:]
+ -[MRUFlippingArtworkLayer updateArtworkStyle]
+ -[MRUImageLoader deferredFittingSize]
+ -[MRUImageLoader deferredScale]
+ -[MRUImageLoader deferredUpdateFittingSize]
+ -[MRUImageLoader fittingSizeUpdateScheduled]
+ -[MRUImageLoader lastVendedArtworkIdentifier]
+ -[MRUImageLoader runningSynchronously]
+ -[MRUImageLoader setDeferredFittingSize:]
+ -[MRUImageLoader setDeferredScale:]
+ -[MRUImageLoader setFittingSizeUpdateScheduled:]
+ -[MRUImageLoader setLastVendedArtworkIdentifier:]
+ -[MRUImageLoader setRunningSynchronously:]
+ -[MRUImageLoader setTargetFittingSizeForCurrentCatalogConfiguration:]
+ -[MRUImageLoader targetFittingSizeForCurrentCatalogConfiguration]
+ -[MRUImageLoader withNoEscapeCheck:]
+ GCC_except_table34
+ _OBJC_IVAR_$_MRUActivityNowPlayingViewController._lastLeftButtonTapDate
+ _OBJC_IVAR_$_MRUFlippingArtworkLayer._artworkStyle
+ _OBJC_IVAR_$_MRUFlippingArtworkLayer._backLegibilityLayer
+ _OBJC_IVAR_$_MRUFlippingArtworkLayer._frontLegibilityLayer
+ _OBJC_IVAR_$_MRUImageLoader._deferredFittingSize
+ _OBJC_IVAR_$_MRUImageLoader._deferredScale
+ _OBJC_IVAR_$_MRUImageLoader._fittingSizeUpdateScheduled
+ _OBJC_IVAR_$_MRUImageLoader._lastVendedArtworkIdentifier
+ _OBJC_IVAR_$_MRUImageLoader._runningSynchronously
+ _OBJC_IVAR_$_MRUImageLoader._targetFittingSizeForCurrentCatalogConfiguration
+ ___34-[MRUImageLoader configureCatalog]_block_invoke_2
+ ___42-[MRUImageLoader updateFittingSize:scale:]_block_invoke
+ ___43-[MRUImageLoader deferredUpdateFittingSize]_block_invoke
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0ls32l8s40l8w48l8
+ _kCAFilterVibrantColorMatrix
+ _objc_msgSend$deferredFittingSize
+ _objc_msgSend$deferredScale
+ _objc_msgSend$deferredUpdateFittingSize
+ _objc_msgSend$fittingSizeUpdateScheduled
+ _objc_msgSend$lastVendedArtworkIdentifier
+ _objc_msgSend$makeDynamicIslandLegibilityFilter
+ _objc_msgSend$makeLegibilityLayer
+ _objc_msgSend$redColor
+ _objc_msgSend$runningSynchronously
+ _objc_msgSend$setArtworkStyle:
+ _objc_msgSend$setDeferredFittingSize:
+ _objc_msgSend$setDeferredScale:
+ _objc_msgSend$setDoubleSided:
+ _objc_msgSend$setFittingSizeUpdateScheduled:
+ _objc_msgSend$setLastLeftButtonTapDate:
+ _objc_msgSend$setLastVendedArtworkIdentifier:
+ _objc_msgSend$setRunningSynchronously:
+ _objc_msgSend$setTargetFittingSizeForCurrentCatalogConfiguration:
+ _objc_msgSend$targetFittingSizeForCurrentCatalogConfiguration
+ _objc_msgSend$valueWithCAColorMatrix:
+ _objc_msgSend$verboseImageLoadingLogging
+ _objc_msgSend$withNoEscapeCheck:
- -[MRUActivityNowPlayingViewController artworkView:didChangeArtworkImage:]
- -[MRUImageLoader effectiveScaledFittingSizeForConfiguration]
- -[MRUImageLoader lastLoadedArtworkIdentifier]
- -[MRUImageLoader setEffectiveScaledFittingSizeForConfiguration:]
- -[MRUImageLoader setLastLoadedArtworkIdentifier:]
- GCC_except_table33
- _OBJC_IVAR_$_MRUImageLoader._effectiveScaledFittingSizeForConfiguration
- _OBJC_IVAR_$_MRUImageLoader._lastLoadedArtworkIdentifier
- _objc_msgSend$effectiveScaledFittingSizeForConfiguration
- _objc_msgSend$initWithToken:dataSource:
- _objc_msgSend$lastLoadedArtworkIdentifier
- _objc_msgSend$setEffectiveScaledFittingSizeForConfiguration:
- _objc_msgSend$setLastLoadedArtworkIdentifier:
- _objc_msgSend$token
CStrings:
+ "!("
+ "$\x13"
+ "T@\"<MPArtworkDataSourceVisualIdenticality>\",&,N,V_lastVendedArtworkIdentifier"
+ "T@\"CALayer\",&,N,V_backLegibilityLayer"
+ "T@\"CALayer\",&,N,V_frontLegibilityLayer"
+ "T@\"NSDate\",&,N,V_lastLeftButtonTapDate"
+ "TB,N,V_fittingSizeUpdateScheduled"
+ "TB,N,V_runningSynchronously"
+ "Td,N,V_deferredScale"
+ "Tq,N,V_artworkStyle"
+ "T{CGSize=dd},N,V_deferredFittingSize"
+ "T{CGSize=dd},N,V_targetFittingSizeForCurrentCatalogConfiguration"
+ "[MRUImageLoader] %@<%p> skip caching for image that is already cached in catalog: %@."
+ "[MRUImageLoader] %@<%p> update deferred fitting size: %@, scale: %lf."
+ "[MRUImageLoader] %@<%p> update fitting size: %@ on associated catalog: %p"
+ "\\"
+ "_artworkStyle"
+ "_backLegibilityLayer"
+ "_deferredFittingSize"
+ "_deferredScale"
+ "_fittingSizeUpdateScheduled"
+ "_frontLegibilityLayer"
+ "_lastLeftButtonTapDate"
+ "_lastVendedArtworkIdentifier"
+ "_runningSynchronously"
+ "_targetFittingSizeForCurrentCatalogConfiguration"
+ "artworkStyle"
+ "backLegibilityLayer"
+ "deferredFittingSize"
+ "deferredScale"
+ "deferredUpdateFittingSize"
+ "didTapTransportButton:"
+ "fittingSizeUpdateScheduled"
+ "frontLegibilityLayer"
+ "inputColorMatrix"
+ "lastLeftButtonTapDate"
+ "lastVendedArtworkIdentifier"
+ "makeDynamicIslandLegibilityFilter"
+ "makeLegibilityLayer"
+ "redColor"
+ "runningSynchronously"
+ "setArtworkStyle:"
+ "setBackLegibilityLayer:"
+ "setDeferredFittingSize:"
+ "setDeferredScale:"
+ "setDoubleSided:"
+ "setFittingSizeUpdateScheduled:"
+ "setFrontLegibilityLayer:"
+ "setLastLeftButtonTapDate:"
+ "setLastVendedArtworkIdentifier:"
+ "setRunningSynchronously:"
+ "setTargetFittingSizeForCurrentCatalogConfiguration:"
+ "targetFittingSizeForCurrentCatalogConfiguration"
+ "valueWithCAColorMatrix:"
+ "verboseImageLoadingLogging"
+ "withNoEscapeCheck:"
- "!'"
- "#\x14"
- "J"
- "T@\"<MPArtworkDataSourceVisualIdenticality>\",&,N,V_lastLoadedArtworkIdentifier"
- "T{CGSize=dd},N,V_effectiveScaledFittingSizeForConfiguration"
- "_effectiveScaledFittingSizeForConfiguration"
- "_lastLoadedArtworkIdentifier"
- "effectiveScaledFittingSizeForConfiguration"
- "initWithToken:dataSource:"
- "lastLoadedArtworkIdentifier"
- "setEffectiveScaledFittingSizeForConfiguration:"
- "setLastLoadedArtworkIdentifier:"
- "token"

```
