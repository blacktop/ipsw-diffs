## VideosUICore

> `/System/Library/PrivateFrameworks/VideosUICore.framework/VideosUICore`

```diff

-973.50.8.0.0
-  __TEXT.__text: 0x2cfa0
-  __TEXT.__auth_stubs: 0xc00
-  __TEXT.__objc_methlist: 0x4ccc
+1046.0.0.0.7
+  __TEXT.__text: 0x2dc08
+  __TEXT.__auth_stubs: 0xbe0
+  __TEXT.__objc_methlist: 0x4d34
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x2b0b
-  __TEXT.__oslogstring: 0xac2
-  __TEXT.__gcc_except_tab: 0x81c
+  __TEXT.__cstring: 0x2c0a
+  __TEXT.__oslogstring: 0xd7a
+  __TEXT.__gcc_except_tab: 0x83c
   __TEXT.__ustring: 0x6a
-  __TEXT.__unwind_info: 0xf30
-  __TEXT.__objc_classname: 0x888
-  __TEXT.__objc_methname: 0xd5a4
-  __TEXT.__objc_methtype: 0x22e4
-  __TEXT.__objc_stubs: 0x8b60
+  __TEXT.__unwind_info: 0xf88
+  __TEXT.__objc_classname: 0x8c5
+  __TEXT.__objc_methname: 0xd608
+  __TEXT.__objc_methtype: 0x2272
+  __TEXT.__objc_stubs: 0x88c0
   __DATA_CONST.__got: 0x5d0
-  __DATA_CONST.__const: 0x1b78
-  __DATA_CONST.__objc_classlist: 0x220
+  __DATA_CONST.__const: 0x1b50
+  __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0xb0
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3450
+  __DATA_CONST.__objc_selrefs: 0x33f8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x188
-  __AUTH_CONST.__auth_got: 0x610
-  __AUTH_CONST.__const: 0x560
-  __AUTH_CONST.__cfstring: 0x53e0
-  __AUTH_CONST.__objc_const: 0x7c78
+  __DATA_CONST.__objc_superrefs: 0x190
+  __AUTH_CONST.__auth_got: 0x600
+  __AUTH_CONST.__const: 0x580
+  __AUTH_CONST.__cfstring: 0x56c0
+  __AUTH_CONST.__objc_const: 0x7d68
   __AUTH_CONST.__objc_intobj: 0x300
-  __AUTH_CONST.__objc_doubleobj: 0xe0
+  __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH.__objc_data: 0x780
-  __DATA.__objc_ivar: 0x520
-  __DATA.__data: 0x7f0
+  __DATA.__objc_ivar: 0x51c
+  __DATA.__data: 0x7f8
   __DATA.__bss: 0x88
-  __DATA_DIRTY.__objc_data: 0xdc0
+  __DATA_DIRTY.__objc_data: 0xe60
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x201
+  __DATA_DIRTY.__bss: 0x210
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
+  - /System/Library/Frameworks/Symbols.framework/Symbols
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/CoreSVG.framework/CoreSVG
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D32F5771-F34A-3F4C-BB60-E0F89CC5907F
-  Functions: 1629
-  Symbols:   6063
-  CStrings:  4140
+  UUID: 3B037E7C-F239-38A0-8DD0-01ED3B21A67F
+  Functions: 1649
+  Symbols:   6101
+  CStrings:  4180
 
Symbols:
+ +[UITabBarController(radar147256381) vuiSetShouldCollapseTabBarOnScroll:on:]
+ +[VUIAssetLibrary cacheHasBeenPurgedForHeic:]
+ +[VUIAssetLibrary markCachePurgedForHeic:]
+ +[VUICoreConfiguration sharedInstance]
+ +[VUICoreConfiguration sharedInstance].cold.1
+ +[VUICoreUtilities defaultPlaceholderImageName]
+ +[VUICoreUtilities formatForOpaqueImage]
+ +[VUICoreUtilities formatForTransparentImage]
+ +[VUICoreUtilities isHeicFormatAllowed]
+ +[VUICoreUtilities isTVApp]
+ +[VUICoreUtilities vuiNormalizedPath:evenOddFillRule:]
+ +[VUIImage cgImageHasAlpha:]
+ +[VUISymbolContentTransition symbolAutomaticContentTransition]
+ +[VUISymbolContentTransition symbolReplaceContentDownUpTransition]
+ +[VUISymbolContentTransition symbolReplaceContentOffUpTransition]
+ +[VUISymbolContentTransition symbolReplaceContentTransition]
+ +[VUISymbolContentTransition symbolReplaceContentUpUpTransition]
+ +[_TVURLSessionDownloadTaskWrapper writeRequestToTempDir:resultError:]
+ +[_TVURLSessionDownloadTaskWrapper writeRequestToTempDir:resultError:].cold.1
+ +[_TVURLSessionDownloadTaskWrapper writeRequestToTempDir:resultError:].cold.2
+ -[UIImage(VideosUICore) vuiAccessibilityLabel]
+ -[UIViewController(VideosUICore) vui_findPresentationSource:]
+ -[VUIAppIconImageLoader loadImageForObject:scaleToSize:cropToFit:imageDirection:completionHandler:]
+ -[VUICoreConfiguration minimalSessionImageLoading]
+ -[VUICoreConfiguration setMinimalSessionImageLoading:]
+ -[VUIDebugDefaults setVStackInForEachEnabled:]
+ -[VUIDebugDefaults vStackInForEachEnabled]
+ -[VUIImageProxy _completeImageLoadWithImage:imagePath:error:assetKey:expiryDate:tags:]
+ -[VUIImageProxy _decorateAndWriteImage:imagePath:scaleToSize:cropToFit:scalingResult:assetKey:expiryDate:tags:]
+ -[VUIImageView _setImage:shouldUpdateImageView:]
+ -[VUIImageView _updateFlatImageWithImage:shouldUpdateImageView:]
+ -[VUIImageView adjustsLocalImageForContentSizeCategory]
+ -[VUIImageView clearsBackgroundColorOnImageLoad]
+ -[VUIImageView localImageViewSize]
+ -[VUIImageView overrideLocalImageViewSizingMode]
+ -[VUIImageView setAdjustsLocalImageForContentSizeCategory:]
+ -[VUIImageView setClearsBackgroundColorOnImageLoad:]
+ -[VUIImageView setLocalImageViewSize:]
+ -[VUIImageView setOverrideLocalImageViewSizingMode:]
+ -[VUILayeredImageContainerView _setSelectionStyle:]
+ -[VUILayeredImageContainerView prepareForReuse]
+ -[VUILayeredImageContainerView selectionStyle]
+ -[VUILayeredImageContainerView setControlState:animated:focusAnimationCoordinator:]
+ -[VUILayeredImageContainerView setSelectionStyle:]
+ -[VUIStackedImageView cornerRadii]
+ -[VUIStackedImageView setCornerRadii:]
+ -[VUIStackedImageView setImageOverlayView:]
+ -[VUIStackedImageView setZDepth:]
+ -[VUIStackedImageView zDepth]
+ -[VUISymbolContentTransition .cxx_destruct]
+ -[VUISymbolContentTransition initWithTransition:]
+ -[VUISymbolContentTransition setSymbolTransition:]
+ -[VUISymbolContentTransition symbolTransition]
+ -[VUIURLImageLoader loadImageForObject:scaleToSize:cropToFit:imageDirection:completionHandler:]
+ -[VUIURLImageLoader sharedAMSUrlSession]
+ -[_TVURLSessionDownloadTaskWrapper resumeWithCompletionHandler:session:]
+ -[_TVURLSessionDownloadTaskWrapper resumeWithCompletionHandler:session:].cold.1
+ GCC_except_table10
+ GCC_except_table29
+ GCC_except_table69
+ GCC_except_table70
+ GCC_except_table9
+ _CGPathCreateCopyByNormalizing
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_NSSymbolAutomaticContentTransition
+ _OBJC_CLASS_$_NSSymbolReplaceContentTransition
+ _OBJC_CLASS_$_VUICoreConfiguration
+ _OBJC_CLASS_$_VUISymbolContentTransition
+ _OBJC_IVAR_$_VUICoreConfiguration._minimalSessionImageLoading
+ _OBJC_IVAR_$_VUIDebugDefaults._vStackInForEachEnabled
+ _OBJC_IVAR_$_VUIImageView._adjustsLocalImageForContentSizeCategory
+ _OBJC_IVAR_$_VUIImageView._clearsBackgroundColorOnImageLoad
+ _OBJC_IVAR_$_VUIImageView._localImageViewSize
+ _OBJC_IVAR_$_VUIImageView._overrideLocalImageViewSizingMode
+ _OBJC_IVAR_$_VUILayeredImageContainerView._selectionStyle
+ _OBJC_IVAR_$_VUISymbolContentTransition._symbolTransition
+ _OBJC_IVAR_$__TVURLSessionDownloadTaskWrapper._dataTask
+ _OBJC_IVAR_$__TVURLSessionDownloadTaskWrapper._taskID
+ _OBJC_METACLASS_$_VUICoreConfiguration
+ _OBJC_METACLASS_$_VUISymbolContentTransition
+ _UTTypeHEIC
+ _VUIImageViewSizingModeFitToProvidedSize
+ _VUIImageViewSizingModeFitToViewBounds
+ _VUISolariumEnabled
+ __OBJC_$_CLASS_METHODS_UITabBarController(VideosUICore|radar147256381)
+ __OBJC_$_CLASS_METHODS_VUICoreConfiguration
+ __OBJC_$_CLASS_METHODS_VUISymbolContentTransition
+ __OBJC_$_CLASS_METHODS__TVURLSessionDownloadTaskWrapper
+ __OBJC_$_INSTANCE_METHODS_VUICoreConfiguration
+ __OBJC_$_INSTANCE_METHODS_VUISymbolContentTransition
+ __OBJC_$_INSTANCE_VARIABLES_VUICoreConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_VUISymbolContentTransition
+ __OBJC_$_PROP_LIST_VUICoreConfiguration
+ __OBJC_$_PROP_LIST_VUISymbolContentTransition
+ __OBJC_CLASS_RO_$_VUICoreConfiguration
+ __OBJC_CLASS_RO_$_VUISymbolContentTransition
+ __OBJC_METACLASS_RO_$_VUICoreConfiguration
+ __OBJC_METACLASS_RO_$_VUISymbolContentTransition
+ __UISolariumEnabled
+ ___111-[VUIImageProxy _decorateAndWriteImage:imagePath:scaleToSize:cropToFit:scalingResult:assetKey:expiryDate:tags:]_block_invoke
+ ___111-[VUIImageProxy _decorateAndWriteImage:imagePath:scaleToSize:cropToFit:scalingResult:assetKey:expiryDate:tags:]_block_invoke_2
+ ___111-[VUIImageProxy _decorateAndWriteImage:imagePath:scaleToSize:cropToFit:scalingResult:assetKey:expiryDate:tags:]_block_invoke_3
+ ___21-[VUIImageProxy load]_block_invoke.33
+ ___21-[VUIImageProxy load]_block_invoke_2.36
+ ___26-[VUIImageView _loadImage]_block_invoke.28
+ ___38+[VUICoreConfiguration sharedInstance]_block_invoke
+ ___72-[_TVURLSessionDownloadTaskWrapper resumeWithCompletionHandler:session:]_block_invoke
+ ___72-[_TVURLSessionDownloadTaskWrapper resumeWithCompletionHandler:session:]_block_invoke.11
+ ___72-[_TVURLSessionDownloadTaskWrapper resumeWithCompletionHandler:session:]_block_invoke.6
+ ___72-[_TVURLSessionDownloadTaskWrapper resumeWithCompletionHandler:session:]_block_invoke_2
+ ___72-[_TVURLSessionDownloadTaskWrapper resumeWithCompletionHandler:session:]_block_invoke_2.8
+ ___72-[_TVURLSessionDownloadTaskWrapper resumeWithCompletionHandler:session:]_block_invoke_3
+ ___72-[_TVURLSessionDownloadTaskWrapper resumeWithCompletionHandler:session:]_block_invoke_3.9
+ ___72-[_TVURLSessionDownloadTaskWrapper resumeWithCompletionHandler:session:]_block_invoke_3.9.cold.1
+ ___72-[_TVURLSessionDownloadTaskWrapper resumeWithCompletionHandler:session:]_block_invoke_3.cold.1
+ ___81-[VUIAssetLibrary _setImageAsset:forKey:inGroupOfType:expiryDate:overWrite:tags:]_block_invoke.47
+ ___86-[VUIImageProxy _completeImageLoadWithImage:imagePath:error:assetKey:expiryDate:tags:]_block_invoke
+ ___86-[VUIImageProxy _completeImageLoadWithImage:imagePath:error:assetKey:expiryDate:tags:]_block_invoke_2
+ ___95-[VUIURLImageLoader loadImageForObject:scaleToSize:cropToFit:imageDirection:completionHandler:]_block_invoke
+ ___99-[VUIAppIconImageLoader loadImageForObject:scaleToSize:cropToFit:imageDirection:completionHandler:]_block_invoke
+ ___block_descriptor_130_e8_32s40s48s56s64s72s80s88s96w_e5_v8?0lw96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_41_e8_32w_e24_v16?0"NSNotification"8lw32l8
+ ___block_descriptor_48_e8_32s40bs_e27_v16?0"VUIURLImageLoader"8ls32l8s40l8
+ ___block_descriptor_56_e8_32bs40w_e30_v16?0"NSURLSessionDataTask"8lw40l8s32l8
+ ___block_descriptor_56_e8_32bs40w_e34_v24?0"AMSURLResult"8"NSError"16lw40l8s32l8
+ ___block_descriptor_72_e8_32s40s48bs56w_e5_v8?0ls32l8s40l8w56l8s48l8
+ ___block_descriptor_72_e8_32s40s48bs56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80r_e27_v16?0"VUIURLImageLoader"8ls32l8s40l8s48l8s56l8s64l8r80l8s72l8
+ ___block_literal_global.27
+ ___block_literal_global.32
+ ___block_literal_global.37
+ ___block_literal_global.43
+ ___block_literal_global.44
+ ___block_literal_global.479
+ ___block_literal_global.71
+ ___block_literal_global.74
+ ___block_literal_global.99
+ _defaultPlaceholderImageForUserInterfaceStyle:.__once.39
+ _kDefaultPlaceholderImageName
+ _objc_msgSend$_completeImageLoadWithImage:imagePath:error:assetKey:expiryDate:tags:
+ _objc_msgSend$_decorateAndWriteImage:imagePath:scaleToSize:cropToFit:scalingResult:assetKey:expiryDate:tags:
+ _objc_msgSend$_setImage:shouldUpdateImageView:
+ _objc_msgSend$_setShouldCollapseTabBarOnScroll:
+ _objc_msgSend$_updateFlatImageWithImage:shouldUpdateImageView:
+ _objc_msgSend$adjustsLocalImageForContentSizeCategory
+ _objc_msgSend$cacheHasBeenPurgedForHeic:
+ _objc_msgSend$cgImageHasAlpha:
+ _objc_msgSend$clearsBackgroundColorOnImageLoad
+ _objc_msgSend$createDataTaskWithRequest:activity:dataTaskCreationCompletionHandler:requestCompletionHandler:
+ _objc_msgSend$createFileAtPath:contents:attributes:
+ _objc_msgSend$imageOverlayView
+ _objc_msgSend$initWithTransition:
+ _objc_msgSend$isHeicFormatAllowed
+ _objc_msgSend$isTVApp
+ _objc_msgSend$localImageViewSize
+ _objc_msgSend$markCachePurgedForHeic:
+ _objc_msgSend$minimalSessionImageLoading
+ _objc_msgSend$overrideLocalImageViewSizingMode
+ _objc_msgSend$replaceDownUpTransition
+ _objc_msgSend$replaceOffUpTransition
+ _objc_msgSend$replaceUpUpTransition
+ _objc_msgSend$resumeWithCompletionHandler:session:
+ _objc_msgSend$setConfig:
+ _objc_msgSend$setLayeredImageProxy:
+ _objc_msgSend$setLocalImageViewSize:
+ _objc_msgSend$setSelected:animated:withAnimationCoordinator:
+ _objc_msgSend$setSelectionStyle:
+ _objc_msgSend$setZDepth:
+ _objc_msgSend$sharedAMSUrlSession
+ _objc_msgSend$symbolTransition
+ _objc_msgSend$transition
+ _objc_msgSend$writeRequestToTempDir:resultError:
+ _objc_msgSend$zDepth
- +[VUICoreUtilities image:didCompleteLoadingForCache:requestRecord:]
- +[VUIStackedImageView layerClass]
- -[UIImage(VideosUICore) vuiJPEGRepresentation]
- -[UIImage(VideosUICore) vuiPNGRepresentation]
- -[VUIAppIconImageLoader loadImageForObject:scaleToSize:cropToFit:imageDirection:requestLoader:completionHandler:]
- -[VUIDebugDefaults capellaMockedDataEnabled]
- -[VUIDebugDefaults setCapellaMockedDataEnabled:]
- -[VUIImageProxy _completeImageLoadWithImage:imagePath:error:assetKey:expiryDate:tags:requestRecord:]
- -[VUIImageProxy _decorateAndWriteImage:imagePath:scaleToSize:cropToFit:scalingResult:assetKey:expiryDate:tags:requestRecord:]
- -[VUIImageProxy requestLoader]
- -[VUIImageProxy setRequestLoader:]
- -[VUIImageView resourceOrSymbolSize]
- -[VUIImageView setResourceOrSymbolSize:]
- -[VUIImageView setShouldScaleToSize:]
- -[VUIImageView shouldScaleToSize]
- -[VUILayeredImageContainerView layeredImageContainerLayer]
- -[VUILayeredImageContainerView overlayView]
- -[VUILayeredImageContainerView setOverlayView:]
- -[VUILayeredImageContainerView setOverlayView:masked:]
- -[VUILayeredImageContainerView setPressed:animated:]
- -[VUILayeredImageContainerView setPressed:animated:completion:]
- -[VUILayeredImageContainerView setSelected:]
- -[VUILayeredImageContainerView setSelected:animated:focusAnimationCoordinator:]
- -[VUIStackedImageView _attachMotionEffects]
- -[VUIStackedImageView _detachMotionEffects]
- -[VUIStackedImageView _idleModeFocusSizeOffset]
- -[VUIStackedImageView _imageConfiguration]
- -[VUIStackedImageView _layerBelowTitles]
- -[VUIStackedImageView _layeredImageContainerLayer]
- -[VUIStackedImageView _setFocusDirection:duration:]
- -[VUIStackedImageView controlState]
- -[VUIStackedImageView isPressed]
- -[VUIStackedImageView isSelected]
- -[VUIStackedImageView overlayView]
- -[VUIStackedImageView primaryControlState]
- -[VUIStackedImageView setControlState:]
- -[VUIStackedImageView setControlState:animated:]
- -[VUIStackedImageView setFocusDirection:animated:]
- -[VUIStackedImageView setFocused:]
- -[VUIStackedImageView setOverlayView:]
- -[VUIStackedImageView setPressed:animated:]
- -[VUIStackedImageView setPressed:animated:completion:]
- -[VUIStackedImageView setPressed:duration:completion:]
- -[VUIStackedImageView setSelected:]
- -[VUIStackedImageView setSelected:animated:focusAnimationCoordinator:]
- -[VUIStackedImageView setUnmaskedOverlayView:]
- -[VUIStackedImageView unmaskedOverlayView]
- -[VUIURLImageLoader loadImageForObject:scaleToSize:cropToFit:imageDirection:requestLoader:completionHandler:]
- GCC_except_table17
- GCC_except_table18
- GCC_except_table8
- GCC_except_table86
- GCC_except_table87
- _OBJC_CLASS_$_UIInterpolatingMotionEffect
- _OBJC_CLASS_$_UIMotionEffectGroup
- _OBJC_CLASS_$__UIStackedImageContainerLayer
- _OBJC_IVAR_$_VUIDebugDefaults._capellaMockedDataEnabled
- _OBJC_IVAR_$_VUIImageProxy._requestLoader
- _OBJC_IVAR_$_VUIImageView._resourceOrSymbolSize
- _OBJC_IVAR_$_VUIImageView._shouldScaleToSize
- _OBJC_IVAR_$_VUILayeredImageContainerView._overlayView
- _OBJC_IVAR_$_VUIStackedImageView._imageStackConfig
- _OBJC_IVAR_$_VUIStackedImageView._imageStackLayer
- _OBJC_IVAR_$_VUIStackedImageView._motionEffectGroup
- _OBJC_IVAR_$_VUIStackedImageView._overlayView
- _OBJC_IVAR_$_VUIStackedImageView._unmaskedOverlayView
- _OBJC_IVAR_$__TVURLSessionDownloadTaskWrapper._downloadTaskID
- _UIImageJPEGRepresentation
- _UIImagePNGRepresentation
- _UTTypeCopyPreferredTagWithClass
- _VUIStackedImageControlStateFocusedIdle
- ___100-[VUIImageProxy _completeImageLoadWithImage:imagePath:error:assetKey:expiryDate:tags:requestRecord:]_block_invoke
- ___100-[VUIImageProxy _completeImageLoadWithImage:imagePath:error:assetKey:expiryDate:tags:requestRecord:]_block_invoke_2
- ___109-[VUIURLImageLoader loadImageForObject:scaleToSize:cropToFit:imageDirection:requestLoader:completionHandler:]_block_invoke
- ___113-[VUIAppIconImageLoader loadImageForObject:scaleToSize:cropToFit:imageDirection:requestLoader:completionHandler:]_block_invoke
- ___125-[VUIImageProxy _decorateAndWriteImage:imagePath:scaleToSize:cropToFit:scalingResult:assetKey:expiryDate:tags:requestRecord:]_block_invoke
- ___125-[VUIImageProxy _decorateAndWriteImage:imagePath:scaleToSize:cropToFit:scalingResult:assetKey:expiryDate:tags:requestRecord:]_block_invoke_2
- ___125-[VUIImageProxy _decorateAndWriteImage:imagePath:scaleToSize:cropToFit:scalingResult:assetKey:expiryDate:tags:requestRecord:]_block_invoke_3
- ___21-[VUIImageProxy load]_block_invoke.35
- ___21-[VUIImageProxy load]_block_invoke_2.38
- ___26-[VUIImageView _loadImage]_block_invoke.22
- ___67+[VUICoreUtilities image:didCompleteLoadingForCache:requestRecord:]_block_invoke
- ___67+[VUICoreUtilities image:didCompleteLoadingForCache:requestRecord:]_block_invoke_2
- ___81-[VUIAssetLibrary _setImageAsset:forKey:inGroupOfType:expiryDate:overWrite:tags:]_block_invoke.40
- ___block_descriptor_138_e8_32s40s48s56s64s72s80s88s96s104w_e5_v8?0lw104l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
- ___block_descriptor_49_e8_32s40w_e24_v16?0"NSNotification"8lw40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e27_v16?0"VUIURLImageLoader"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e44_v16?0?<v?"NSData""NSString""NSError">8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88r_e27_v16?0"VUIURLImageLoader"8ls32l8s40l8s48l8s56l8s64l8r88l8s72l8s80l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_literal_global.25
- ___block_literal_global.30
- ___block_literal_global.35
- ___block_literal_global.39
- ___block_literal_global.46
- ___block_literal_global.475
- ___block_literal_global.69
- ___block_literal_global.72
- ___block_literal_global.97
- _defaultPlaceholderImageForUserInterfaceStyle:.__once.37
- _kUTTagClassMIMEType
- _kUTTypeJPEG2000
- _objc_autoreleasePoolPop
- _objc_autoreleasePoolPush
- _objc_msgSend$_attachMotionEffects
- _objc_msgSend$_completeImageLoadWithImage:imagePath:error:assetKey:expiryDate:tags:requestRecord:
- _objc_msgSend$_decorateAndWriteImage:imagePath:scaleToSize:cropToFit:scalingResult:assetKey:expiryDate:tags:requestRecord:
- _objc_msgSend$_detachMotionEffects
- _objc_msgSend$_idleModeFocusSizeOffset
- _objc_msgSend$_layerBelowTitles
- _objc_msgSend$_primaryControlStateForState:
- _objc_msgSend$_selectionStyle
- _objc_msgSend$_setFocusDirection:duration:
- _objc_msgSend$_setOverlayLayer:
- _objc_msgSend$_setSelectionStyle:
- _objc_msgSend$_setUnmaskedOverlayLayer:
- _objc_msgSend$_timingData
- _objc_msgSend$addMotionEffect:
- _objc_msgSend$didCompleteLoadingFromCache:withResponseBodyBlock:
- _objc_msgSend$didCompleteLoadingWithResponseBody:
- _objc_msgSend$didFailWithError:
- _objc_msgSend$didReceiveData:
- _objc_msgSend$didReceiveResponse:timingData:
- _objc_msgSend$focusDirection
- _objc_msgSend$image:didCompleteLoadingForCache:requestRecord:
- _objc_msgSend$initWithKeyPath:type:
- _objc_msgSend$isPressed
- _objc_msgSend$isSelected
- _objc_msgSend$layeredImageContainerLayer
- _objc_msgSend$loadImageForObject:scaleToSize:cropToFit:imageDirection:requestLoader:completionHandler:
- _objc_msgSend$pressedDuration
- _objc_msgSend$recordForResource:withInitiator:
- _objc_msgSend$removeMotionEffect:
- _objc_msgSend$requestLoader
- _objc_msgSend$resourceOrSymbolSize
- _objc_msgSend$setControlState:
- _objc_msgSend$setControlState:animated:
- _objc_msgSend$setFocusDirection:animated:
- _objc_msgSend$setFocused:
- _objc_msgSend$setMaximumRelativeValue:
- _objc_msgSend$setMinimumRelativeValue:
- _objc_msgSend$setMotionEffects:
- _objc_msgSend$setOverlayView:masked:
- _objc_msgSend$setPressed:
- _objc_msgSend$setPressed:animated:
- _objc_msgSend$setPressed:animated:completion:
- _objc_msgSend$setPressedDuration:
- _objc_msgSend$setResourceOrSymbolSize:
- _objc_msgSend$setSelected:
- _objc_msgSend$setSelected:animated:
- _objc_msgSend$setSelected:animated:focusAnimationCoordinator:
- _objc_msgSend$setStackFocused:
- _objc_msgSend$setStackFocused:withFocusAnimationCoordinator:
- _objc_msgSend$setUnpressedDuration:
- _objc_msgSend$shouldScaleToSize
- _objc_msgSend$unpressedDuration
- _objc_msgSend$vuiJPEGRepresentation
- _objc_msgSend$vuiPNGRepresentation
- _objc_msgSend$willSendRequest:
CStrings:
+ "10-12pg"
+ "13"
+ "7-9pg"
+ "@\"AMSURLSession\"16@0:8"
+ "@\"NSSymbolContentTransition\""
+ "B24@0:8^{CGImage=}16"
+ "DebugDefault:: vStackInForEachEnabled: %d"
+ "DefaultPlaceholderImage"
+ "FitToProvidedSize"
+ "FitToViewBounds"
+ "Purging asset library caches since menkaure is enabled AND cache not purged before"
+ "T@\"NSString\",&,N,V_overrideLocalImageViewSizingMode"
+ "T@\"NSSymbolContentTransition\",&,N,V_symbolTransition"
+ "TB,N,V_adjustsLocalImageForContentSizeCategory"
+ "TB,N,V_clearsBackgroundColorOnImageLoad"
+ "TB,N,V_vStackInForEachEnabled"
+ "TB,V_minimalSessionImageLoading"
+ "Tq,N,V_selectionStyle"
+ "T{CACornerRadii={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGSize=dd}},N"
+ "T{CGSize=dd},N,V_localImageViewSize"
+ "UITabBar:: vuiSetShouldCollapseTabBarOnScroll: %d"
+ "VUICoreConfiguration"
+ "VUILayeredImageProxy - Called resumeWithCompletionHandler with AMSSession called but the seession is nil. This is a bug. Falling back to a using a new URL Session which is inefficient."
+ "VUILayeredImageProxy - Error occurred writing an image to disk."
+ "VUILayeredImageProxy - Skipping writing image to disk since network request has an error or no data."
+ "VUILayeredImageProxy - weakSelf is unexpectedely nil in dataTaskCreationCompletionHandler"
+ "VUILayeredImageProxy - weakSelf is unexpectedely nil in requestCompletionHandler"
+ "VUISymbolContentTransition"
+ "^{CGPath=}28@0:8^{CGPath=}16B24"
+ "_adjustsLocalImageForContentSizeCategory"
+ "_clearsBackgroundColorOnImageLoad"
+ "_completeImageLoadWithImage:imagePath:error:assetKey:expiryDate:tags:"
+ "_dataTask"
+ "_decorateAndWriteImage:imagePath:scaleToSize:cropToFit:scalingResult:assetKey:expiryDate:tags:"
+ "_localImageViewSize"
+ "_minimalSessionImageLoading"
+ "_overrideLocalImageViewSizingMode"
+ "_setImage:shouldUpdateImageView:"
+ "_setShouldCollapseTabBarOnScroll:"
+ "_symbolTransition"
+ "_taskID"
+ "_updateFlatImageWithImage:shouldUpdateImageView:"
+ "_vStackInForEachEnabled"
+ "adjustsLocalImageForContentSizeCategory"
+ "cacheHasBeenPurgedForHeic:"
+ "cgImageHasAlpha:"
+ "clearsBackgroundColorOnImageLoad"
+ "com.apple.TV"
+ "com.apple.TVWatchList"
+ "createDataTaskWithRequest:activity:dataTaskCreationCompletionHandler:requestCompletionHandler:"
+ "createFileAtPath:contents:attributes:"
+ "cuscuz"
+ "defaultPlaceholderImageName"
+ "emerald"
+ "formatForOpaqueImage"
+ "formatForTransparentImage"
+ "heic"
+ "imageOverlayView"
+ "initWithTransition:"
+ "isHeicFormatAllowed"
+ "isTVApp"
+ "localImageViewSize"
+ "markCachePurgedForHeic:"
+ "mars"
+ "menkaure"
+ "menkaure.enabled"
+ "menkaureMac"
+ "minimalSessionImageLoading"
+ "opal"
+ "overrideLocalImageViewSizingMode"
+ "plato"
+ "prepareForReuse"
+ "puget"
+ "radar147256381"
+ "replaceDownUpTransition"
+ "replaceOffUpTransition"
+ "replaceUpUpTransition"
+ "resumeWithCompletionHandler:session:"
+ "setAdjustsLocalImageForContentSizeCategory:"
+ "setClearsBackgroundColorOnImageLoad:"
+ "setConfig:"
+ "setImageOverlayView:"
+ "setLocalImageViewSize:"
+ "setMinimalSessionImageLoading:"
+ "setOverrideLocalImageViewSizingMode:"
+ "setSymbolTransition:"
+ "setVStackInForEachEnabled:"
+ "setZDepth:"
+ "sharedAMSUrlSession"
+ "solarium"
+ "symbolAutomaticContentTransition"
+ "symbolReplaceContentDownUpTransition"
+ "symbolReplaceContentOffUpTransition"
+ "symbolReplaceContentTransition"
+ "symbolReplaceContentUpUpTransition"
+ "symbolTransition"
+ "timbuktu"
+ "transition"
+ "v16@?0@\"NSURLSessionDataTask\"8"
+ "v24@?0@\"AMSURLResult\"8@\"NSError\"16"
+ "v32@0:8@?16@24"
+ "v64@0:8@16@24@32@40@48@56"
+ "v80@0:8{CACornerRadii={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGSize=dd}}16"
+ "v84@0:8@16@24{CGSize=dd}32B48Q52@60@68@76"
+ "vStackInForEachEnabled"
+ "vuiAccessibilityLabel"
+ "vuiNormalizedPath:evenOddFillRule:"
+ "vuiSetShouldCollapseTabBarOnScroll:on:"
+ "vui_findPresentationSource:"
+ "writeRequestToTempDir:resultError:"
+ "zDepth"
+ "za_movies-10"
+ "za_movies-1012pg"
+ "za_movies-13"
+ "za_movies-16"
+ "za_movies-18"
+ "za_movies-79pg"
+ "za_movies-a"
+ "za_movies-pg"
+ "za_tv-10"
+ "za_tv-1012pg"
+ "za_tv-13"
+ "za_tv-16"
+ "za_tv-79pg"
+ "za_tv-a"
+ "za_tv-pg"
+ "{CACornerRadii={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGSize=dd}}16@0:8"
- "@\"<VUINetworkRequestLoader>\""
- "@\"UIMotionEffectGroup\""
- "@\"_UIStackedImageConfiguration\""
- "@\"_UIStackedImageContainerLayer\""
- "@68@0:8@16{CGSize=dd}24B40q44@\"<VUINetworkRequestLoader>\"52@?<v@?@\"VUIImage\"@\"NSString\"@\"NSDate\"Q@\"NSError\">60"
- "@68@0:8@16{CGSize=dd}24B40q44@52@?60"
- "EnableCapellaMockedData"
- "T@\"<VUINetworkRequestLoader>\",W,N,V_requestLoader"
- "T@\"UIView\",&,N,V_overlayView"
- "T@\"UIView\",&,N,V_unmaskedOverlayView"
- "T@\"_UIStackedImageContainerLayer\",R,N"
- "TB,N,GisPressed"
- "TB,N,GisSelected"
- "TB,N,V_capellaMockedDataEnabled"
- "TB,N,V_shouldScaleToSize"
- "T{CGSize=dd},N,V_resourceOrSymbolSize"
- "VUIURLImageLoaderOptionsRequestRecordKey"
- "_attachMotionEffects"
- "_capellaMockedDataEnabled"
- "_completeImageLoadWithImage:imagePath:error:assetKey:expiryDate:tags:requestRecord:"
- "_decorateAndWriteImage:imagePath:scaleToSize:cropToFit:scalingResult:assetKey:expiryDate:tags:requestRecord:"
- "_detachMotionEffects"
- "_downloadTaskID"
- "_idleModeFocusSizeOffset"
- "_imageConfiguration"
- "_imageStackConfig"
- "_imageStackLayer"
- "_layerBelowTitles"
- "_layeredImageContainerLayer"
- "_motionEffectGroup"
- "_overlayView"
- "_primaryControlStateForState:"
- "_requestLoader"
- "_resourceOrSymbolSize"
- "_setFocusDirection:duration:"
- "_setOverlayLayer:"
- "_setUnmaskedOverlayLayer:"
- "_shouldScaleToSize"
- "_timingData"
- "_unmaskedOverlayView"
- "addMotionEffect:"
- "bannock"
- "barrette_menu"
- "capellaMockedDataEnabled"
- "coral"
- "didCompleteLoadingFromCache:withResponseBodyBlock:"
- "didCompleteLoadingWithResponseBody:"
- "didFailWithError:"
- "didReceiveData:"
- "didReceiveResponse:timingData:"
- "fromm"
- "garnet"
- "image:didCompleteLoadingForCache:requestRecord:"
- "initWithKeyPath:type:"
- "isPressed"
- "isSelected"
- "jintasaur"
- "layerClass"
- "layeredImageContainerLayer"
- "ludicolo"
- "metate"
- "overlayView"
- "pressed"
- "pressedDuration"
- "primaryControlState"
- "recordForResource:withInitiator:"
- "removeMotionEffect:"
- "requestLoader"
- "resourceOrSymbolSize"
- "sctie"
- "selected"
- "setCapellaMockedDataEnabled:"
- "setControlState:"
- "setControlState:animated:"
- "setFocusDirection:animated:"
- "setFocused:"
- "setMaximumRelativeValue:"
- "setMinimumRelativeValue:"
- "setMotionEffects:"
- "setOverlayView:"
- "setOverlayView:masked:"
- "setPressed:animated:"
- "setPressed:animated:completion:"
- "setPressed:duration:completion:"
- "setPressedDuration:"
- "setRequestLoader:"
- "setResourceOrSymbolSize:"
- "setSelected:"
- "setSelected:animated:focusAnimationCoordinator:"
- "setShouldScaleToSize:"
- "setStackFocused:"
- "setStackFocused:withFocusAnimationCoordinator:"
- "setUnmaskedOverlayView:"
- "setUnpressedDuration:"
- "shouldScaleToSize"
- "sports_register_init2"
- "tractor"
- "unmaskedOverlayView"
- "unpressedDuration"
- "v16@?0@?<v@?@\"NSData\"@\"NSString\"@\"NSError\">8"
- "v28@0:8Q16B24"
- "v32@0:8B16B20@?24"
- "v36@0:8B16d20@?28"
- "v36@0:8{CGPoint=dd}16B32"
- "v40@0:8{CGPoint=dd}16d32"
- "v72@0:8@16@24@32@40@48@56@64"
- "v92@0:8@16@24{CGSize=dd}32B48Q52@60@68@76@84"
- "vampire"
- "vuiJPEGRepresentation"
- "vuiPNGRepresentation"
- "willSendRequest:"

```
