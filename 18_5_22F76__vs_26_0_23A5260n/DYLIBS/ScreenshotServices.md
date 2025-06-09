## ScreenshotServices

> `/System/Library/PrivateFrameworks/ScreenshotServices.framework/ScreenshotServices`

```diff

-369.401.0.0.0
-  __TEXT.__text: 0x179d4
-  __TEXT.__auth_stubs: 0x800
-  __TEXT.__objc_methlist: 0x20b4
-  __TEXT.__const: 0x148
-  __TEXT.__cstring: 0x15fb
-  __TEXT.__oslogstring: 0xd9b
-  __TEXT.__gcc_except_tab: 0x368
-  __TEXT.__dlopen_cstrs: 0x456
-  __TEXT.__unwind_info: 0x890
-  __TEXT.__objc_classname: 0x7ec
-  __TEXT.__objc_methname: 0x5698
-  __TEXT.__objc_methtype: 0xeef
-  __TEXT.__objc_stubs: 0x4f60
-  __DATA_CONST.__got: 0x568
-  __DATA_CONST.__const: 0x9a8
-  __DATA_CONST.__objc_classlist: 0x1d0
-  __DATA_CONST.__objc_catlist: 0x20
+400.1.100.0.0
+  __TEXT.__text: 0x1ba4c
+  __TEXT.__auth_stubs: 0x910
+  __TEXT.__objc_methlist: 0x23e4
+  __TEXT.__const: 0x158
+  __TEXT.__cstring: 0x1b54
+  __TEXT.__oslogstring: 0xf7f
+  __TEXT.__gcc_except_tab: 0x39c
+  __TEXT.__dlopen_cstrs: 0x4ae
+  __TEXT.__unwind_info: 0xa60
+  __TEXT.__objc_classname: 0x81e
+  __TEXT.__objc_methname: 0x60ad
+  __TEXT.__objc_methtype: 0xf4f
+  __TEXT.__objc_stubs: 0x5600
+  __DATA_CONST.__got: 0x678
+  __DATA_CONST.__const: 0xa58
+  __DATA_CONST.__objc_classlist: 0x1e0
+  __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1738
+  __DATA_CONST.__objc_selrefs: 0x1a40
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x410
-  __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0x1140
-  __AUTH_CONST.__objc_const: 0x46a8
-  __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__objc_intobj: 0xc0
+  __AUTH_CONST.__auth_got: 0x498
+  __AUTH_CONST.__const: 0x6c0
+  __AUTH_CONST.__cfstring: 0x19e0
+  __AUTH_CONST.__objc_const: 0x48c0
+  __AUTH_CONST.__objc_doubleobj: 0x40
+  __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0x228
+  __AUTH.__objc_data: 0x730
+  __DATA.__objc_ivar: 0x238
   __DATA.__data: 0x6e0
-  __DATA.__bss: 0x100
+  __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0xb90
-  __DATA_DIRTY.__bss: 0xb0
+  __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/Photos.framework/Photos
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
+  - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3427696E-92CF-3F59-B9DD-089A38038977
-  Functions: 777
-  Symbols:   3266
-  CStrings:  1615
+  UUID: 9E00B085-08B9-3EC9-83A7-082DD359F3F3
+  Functions: 901
+  Symbols:   3666
+  CStrings:  1879
 
Symbols:
+ +[SSChromeFactory closeBarButtonItem]
+ +[SSChromeHelper cropsCornerLengthLong]
+ +[SSChromeHelper roundedCropsLength]
+ +[SSScreenshotAssetManagerPhotoLibraryBackend jpegImageDataFromImage:withProperties:]
+ +[SSScreenshotAssetManagerPhotoLibraryBackend jpegImageDataFromImage:withProperties:].cold.1
+ +[SSScreenshotAssetManagerPhotoLibraryBackend jpegImageDataFromImage:withProperties:].cold.2
+ +[SSScreenshotAssetManagerPhotoLibraryBackend jpegImageDataFromImage:withProperties:].cold.3
+ +[SSStatisticsManager sharedStatisticsManager]
+ +[SSStatisticsManager sharedStatisticsManager].cold.1
+ +[UIImage(SSImageSurface) ss_imageProperties]
+ +[UIImage(SSImageSurface) ss_isHEICImageData:]
+ -[SSEnvironmentDescription earlyVIAnalysis]
+ -[SSEnvironmentDescription setEarlyVIAnalysis:]
+ -[SSImageSurface hdrBackingSurface]
+ -[SSImageSurface setHdrBackingSurface:]
+ -[SSScreenshotAssetManager saveImageDataToTemporaryLocation:persistable:completionHandler:]
+ -[SSScreenshotAssetManagerPhotoLibraryBackend saveImageDataToTemporaryLocation:withName:imageDescription:completionHandler:]
+ -[SSScreenshotAssetManagerPhotoLibraryBackend saveImageDataToTemporaryLocation:withName:imageDescription:completionHandler:].cold.1
+ -[SSScreenshotAssetManagerPhotoLibraryBackend saveImageDataToTemporaryLocation:withName:imageDescription:completionHandler:].cold.2
+ -[SSScreenshotAssetManagerPhotoLibraryBackend saveImageDataToTemporaryLocation:withName:imageDescription:completionHandler:].cold.3
+ -[SSScreenshotAssetManagerPhotoLibraryBackend saveImageDataToTemporaryLocation:withName:imageDescription:completionHandler:].cold.4
+ -[SSScreenshotsWindow hasRemoteViewController]
+ -[SSStatisticsManager _appendSettingsAndSendEvent:block:]
+ -[SSStatisticsManager _sendEvent:block:]
+ -[SSStatisticsManager _statisticsEnabled]
+ -[SSStatisticsManager _triggerTypeForPresentationMode:]
+ -[SSStatisticsManager carPlaySettingsChanged]
+ -[SSStatisticsManager didAccidentallyDraw]
+ -[SSStatisticsManager didChangeOpacityOnFullPage]
+ -[SSStatisticsManager didChangeOpacityOnNormalScreenshot]
+ -[SSStatisticsManager didCopyDeleteScreenshots]
+ -[SSStatisticsManager didCropInFullPageMode]
+ -[SSStatisticsManager didCropInNormalMode]
+ -[SSStatisticsManager didDeleteScreenshots]
+ -[SSStatisticsManager didRenameScreenshot]
+ -[SSStatisticsManager didSaveFullPagePDFToFiles]
+ -[SSStatisticsManager didSaveImageToFiles]
+ -[SSStatisticsManager didSaveImageToPhotos]
+ -[SSStatisticsManager didSaveImageToQuickNote]
+ -[SSStatisticsManager didSaveMixedAllToFiles]
+ -[SSStatisticsManager didSaveMixedToPhotosAndFiles]
+ -[SSStatisticsManager didSaveMixedToQuickNoteAndFiles]
+ -[SSStatisticsManager didSavePDFImageToPhotos]
+ -[SSStatisticsManager didShareFullPageMixedScreenshots]
+ -[SSStatisticsManager didShareFullPageScreenshotAsAutomaticImage]
+ -[SSStatisticsManager didShareFullPageScreenshotAsAutomaticPDF]
+ -[SSStatisticsManager didShareFullPageScreenshotAsImage]
+ -[SSStatisticsManager didShareFullPageScreenshotAsPDF]
+ -[SSStatisticsManager didShareScreenMultipleScreenshots]
+ -[SSStatisticsManager didShareScreenSingleScreenshots]
+ -[SSStatisticsManager didSubmitFeedbackWithAnnotationCount:]
+ -[SSStatisticsManager didTapBetaFeedbackButton]
+ -[SSStatisticsManager didTapFullPageSegment]
+ -[SSStatisticsManager drewStrokes:]
+ -[SSStatisticsManager fileFormatIsHDRSettingsChanged]
+ -[SSStatisticsManager fullScreenPreviewsSettingsChanged]
+ -[SSStatisticsManager fullscreenExperienceHadCropEvent]
+ -[SSStatisticsManager logTotalAnnotations:]
+ -[SSStatisticsManager pipDragEndedSuccessfully]
+ -[SSStatisticsManager pipExpanded]
+ -[SSStatisticsManager pipSlidOffscreenDueToTimeout]
+ -[SSStatisticsManager screenshotGestureTriggered:]
+ -[SSStatisticsManager screenshotGestureTriggeredWhileAnotherScreenshotWasShowing:]
+ -[UIImage(SSImageSurface) ss_dataWithFileFormat:addProperties:]
+ -[UIImage(SSImageSurface) ss_hdrSurfaceCGImage]
+ -[UIImage(SSImageSurface) ss_heicData]
+ -[UIImage(SSImageSurface) ss_ioSurfaceImageData]
+ -[UIImage(SSImageSurface) ss_isHDRImage]
+ -[UIImage(SSImageSurface) ss_jpegData]
+ -[UIImage(SSImageSurface) ss_pngData]
+ -[UIImage(SSImageSurface) ss_sdrSurfaceCGImage]
+ -[UIView(SSPreferences) _ss_vi2Enabled]
+ GCC_except_table18
+ GCC_except_table32
+ GCC_except_table38
+ _AnalyticsSendEventLazy
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterPostNotification
+ _CGColorSpaceIsHDR
+ _CGColorSpaceUsesExtendedRange
+ _CGImageCreateFromIOSurface
+ _CGImageGetColorSpace
+ _CGImageGetContentHeadroom
+ _CGImageSourceCreateWithData
+ _CGImageSourceGetType
+ _MKBGetDeviceLockState
+ _NSGlobalDomain
+ _OBJC_CLASS_$_NSLayoutConstraint
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_PHContentEditingOutputRequestOptions
+ _OBJC_CLASS_$_SSChromeFactory
+ _OBJC_CLASS_$_SSStatisticsManager
+ _OBJC_CLASS_$_UIDevice
+ _OBJC_CLASS_$_UIStackView
+ _OBJC_IVAR_$_SSChromePlaceholderView._closeItem
+ _OBJC_IVAR_$_SSEnvironmentDescription._earlyVIAnalysis
+ _OBJC_IVAR_$_SSImageSurface._hdrBackingSurface
+ _OBJC_IVAR_$_SSVellumOpacityControl._containerStackView
+ _OBJC_METACLASS_$_SSChromeFactory
+ _OBJC_METACLASS_$_SSStatisticsManager
+ _SSDecodingCreateIOSurface
+ _SSDecodingCreateIOSurface.cold.1
+ _SSEncodeIOSurface
+ _UIImageHEICRepresentation
+ _UTTypeHEIC
+ _UTTypeJPEG
+ _UTTypePNG
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UIView_$_SSPreferences
+ __OBJC_$_CATEGORY_UIView_$_SSPreferences
+ __OBJC_$_CLASS_METHODS_SSChromeFactory
+ __OBJC_$_CLASS_METHODS_SSStatisticsManager
+ __OBJC_$_INSTANCE_METHODS_SSStatisticsManager
+ __OBJC_CLASS_RO_$_SSChromeFactory
+ __OBJC_CLASS_RO_$_SSStatisticsManager
+ __OBJC_METACLASS_RO_$_SSChromeFactory
+ __OBJC_METACLASS_RO_$_SSStatisticsManager
+ __SSCarPlayEnabled
+ __SSCarPlayScreenshotsEnabled
+ __SSEnableCarPlayScreenshots
+ __SSEnableHDRCapture
+ __SSEnablePIPExperience
+ __SSEnableVisualLookUpInScreenshots
+ __SSGetLastUsedScreenshotShareFormatOption
+ __SSHDRCaptureEnabled
+ __SSIsDeviceLocked
+ __SSNotifyPreferencesDidChange
+ __SSPIPExperienceEnabled
+ __SSPIPExperienceEnabled.cold.1
+ __SSPreferencesDidChangeRemoteNotification
+ __SSScreenshotsRedesign2025Enabled
+ __SSScreenshotsRedesign2025Enabled.__SSScreenshotsRedesign2025Enabled
+ __SSScreenshotsRedesign2025Enabled.cold.1
+ __SSScreenshotsRedesign2025Enabled.onceToken
+ __SSSetLastUsedScreenshotShareFormatOption
+ __SSVisualIntelligenceV2Enabled
+ __SSVisualLookUpInScreenshotsEnabled
+ __UIRenderingBufferCreateUIImage
+ __UIRenderingMultiBufferCreate
+ __UISolariumEnabled
+ ___103-[SSScreenshotAssetManagerPhotoLibraryBackend _registerEntryWithImage:options:retry:identifierHandler:]_block_invoke.51
+ ___103-[SSScreenshotAssetManagerPhotoLibraryBackend _registerEntryWithImage:options:retry:identifierHandler:]_block_invoke.51.cold.1
+ ___162-[SSScreenshotAssetManagerPhotoLibraryBackend updateImageData:withModificationData:forEntryWithIdentifier:registrationOptions:imageDescription:completionHandler:]_block_invoke.67
+ ___34-[SSStatisticsManager pipExpanded]_block_invoke
+ ___35-[SSStatisticsManager drewStrokes:]_block_invoke
+ ___42-[SSStatisticsManager didAccidentallyDraw]_block_invoke
+ ___42-[SSStatisticsManager didCropInNormalMode]_block_invoke
+ ___42-[SSStatisticsManager didRenameScreenshot]_block_invoke
+ ___42-[SSStatisticsManager didSaveImageToFiles]_block_invoke
+ ___43-[SSStatisticsManager didDeleteScreenshots]_block_invoke
+ ___43-[SSStatisticsManager didSaveImageToPhotos]_block_invoke
+ ___43-[SSStatisticsManager logTotalAnnotations:]_block_invoke
+ ___44-[SSStatisticsManager didCropInFullPageMode]_block_invoke
+ ___44-[SSStatisticsManager didTapFullPageSegment]_block_invoke
+ ___45-[SSStatisticsManager carPlaySettingsChanged]_block_invoke
+ ___45-[SSStatisticsManager didSaveMixedAllToFiles]_block_invoke
+ ___46+[SSStatisticsManager sharedStatisticsManager]_block_invoke
+ ___46-[SSStatisticsManager didSaveImageToQuickNote]_block_invoke
+ ___46-[SSStatisticsManager didSavePDFImageToPhotos]_block_invoke
+ ___47-[SSStatisticsManager didCopyDeleteScreenshots]_block_invoke
+ ___47-[SSStatisticsManager didTapBetaFeedbackButton]_block_invoke
+ ___47-[SSStatisticsManager pipDragEndedSuccessfully]_block_invoke
+ ___48-[SSStatisticsManager didSaveFullPagePDFToFiles]_block_invoke
+ ___49-[SSStatisticsManager didChangeOpacityOnFullPage]_block_invoke
+ ___50-[SSStatisticsManager screenshotGestureTriggered:]_block_invoke
+ ___51-[SSStatisticsManager didSaveMixedToPhotosAndFiles]_block_invoke
+ ___51-[SSStatisticsManager pipSlidOffscreenDueToTimeout]_block_invoke
+ ___53-[SSStatisticsManager fileFormatIsHDRSettingsChanged]_block_invoke
+ ___54-[SSStatisticsManager didSaveMixedToQuickNoteAndFiles]_block_invoke
+ ___54-[SSStatisticsManager didShareFullPageScreenshotAsPDF]_block_invoke
+ ___54-[SSStatisticsManager didShareScreenSingleScreenshots]_block_invoke
+ ___55-[SSStatisticsManager didShareFullPageMixedScreenshots]_block_invoke
+ ___55-[SSStatisticsManager fullscreenExperienceHadCropEvent]_block_invoke
+ ___56-[SSStatisticsManager didShareFullPageScreenshotAsImage]_block_invoke
+ ___56-[SSStatisticsManager didShareScreenMultipleScreenshots]_block_invoke
+ ___56-[SSStatisticsManager fullScreenPreviewsSettingsChanged]_block_invoke
+ ___57-[SSStatisticsManager _appendSettingsAndSendEvent:block:]_block_invoke
+ ___57-[SSStatisticsManager didChangeOpacityOnNormalScreenshot]_block_invoke
+ ___60-[SSStatisticsManager didSubmitFeedbackWithAnnotationCount:]_block_invoke
+ ___63-[SSStatisticsManager didShareFullPageScreenshotAsAutomaticPDF]_block_invoke
+ ___65-[SSStatisticsManager didShareFullPageScreenshotAsAutomaticImage]_block_invoke
+ ___77+[SSScreenshotMetadataHarvester harvestScreenshotMetadataAndRespondToAction:]_block_invoke.30
+ ___77+[SSScreenshotMetadataHarvester harvestScreenshotMetadataAndRespondToAction:]_block_invoke.31
+ ___82-[SSStatisticsManager screenshotGestureTriggeredWhileAnotherScreenshotWasShowing:]_block_invoke
+ ___86-[SSScreenshotAssetManager recordEditsToPersistable:inTransition:withCompletionBlock:]_block_invoke.15
+ ___91-[SSScreenshotAssetManager saveImageDataToTemporaryLocation:persistable:completionHandler:]_block_invoke
+ ____SSNotifyPreferencesDidChange_block_invoke
+ ____SSScreenshotsRedesign2025Enabled_block_invoke
+ ___block_descriptor_32_e19_"NSDictionary"8?0l
+ ___block_descriptor_40_e19_"NSDictionary"8?0l
+ ___block_descriptor_40_e8_32bs_e19_"NSDictionary"8?0ls32l8
+ ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e19_v20?0"NSData"8B16ls32l8s40l8s48l8
+ ___block_descriptor_81_e8_32s40s48s56s64s72bs_e48_v24?0"PHContentEditingInput"8"NSDictionary"16ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.161
+ ___block_literal_global.163
+ ___block_literal_global.165
+ ___block_literal_global.167
+ ___block_literal_global.169
+ ___block_literal_global.171
+ ___block_literal_global.173
+ ___block_literal_global.175
+ ___block_literal_global.177
+ ___block_literal_global.179
+ ___block_literal_global.183
+ ___block_literal_global.185
+ ___block_literal_global.187
+ ___block_literal_global.189
+ ___block_literal_global.191
+ ___block_literal_global.193
+ ___block_literal_global.195
+ ___block_literal_global.197
+ ___block_literal_global.199
+ ___block_literal_global.201
+ ___block_literal_global.203
+ ___block_literal_global.205
+ ___block_literal_global.207
+ ___block_literal_global.209
+ ___block_literal_global.211
+ ___block_literal_global.213
+ ___block_literal_global.215
+ ___block_literal_global.217
+ ___block_literal_global.219
+ ___block_literal_global.221
+ ___block_literal_global.223
+ ___block_literal_global.225
+ ___block_literal_global.41
+ ___block_literal_global.45
+ ___block_literal_global.48
+ ___block_literal_global.61
+ ___block_literal_global.64
+ ___block_literal_global.68
+ ___block_literal_global.71
+ ___block_literal_global.92
+ ___kCFBooleanFalse
+ ___sharedStatisticsManager
+ _kCGColorSpaceDisplayP3
+ _kCGColorSpaceDisplayP3_PQ
+ _kCGGenerateAdaptiveSoftClipCurve
+ _kCGImageDestinationEncodeAlternateColorSpace
+ _kCGImageDestinationEncodeBaseColorSpace
+ _kCGImageDestinationEncodeBasePixelFormatRequest
+ _kCGImageDestinationEncodeGainMapPixelFormatRequest
+ _kCGImageDestinationEncodeGainMapSubsampleFactor
+ _kCGImageDestinationEncodeGenerateGainMapWithBaseImage
+ _kCGImageDestinationEncodeIsBaseImage
+ _kCGImageDestinationEncodeRequest
+ _kCGImageDestinationEncodeRequestOptions
+ _kCGImageDestinationEncodeToISOGainmap
+ _kCGImageDestinationEncodeToISOHDR
+ _kCGImageDestinationLossyCompressionQuality
+ _kCGImagePropertyDPIHeight
+ _kCGImagePropertyDPIWidth
+ _kCGImagePropertyExifDictionary
+ _kCGImagePropertyExifUserComment
+ _kCGImagePropertyOrientation
+ _kCGImageSurfaceFormatRequest
+ _kUIRenderingDestinationHDR
+ _objc_getProperty
+ _objc_msgSend$_appendSettingsAndSendEvent:block:
+ _objc_msgSend$_initWithSDRIOSurface:HDRIOSurface:scale:orientation:
+ _objc_msgSend$_sendEvent:block:
+ _objc_msgSend$_statisticsEnabled
+ _objc_msgSend$_triggerTypeForPresentationMode:
+ _objc_msgSend$activateConstraints:
+ _objc_msgSend$carPlaySettingsChanged
+ _objc_msgSend$centerYAnchor
+ _objc_msgSend$closeBarButtonItem
+ _objc_msgSend$constraintEqualToAnchor:
+ _objc_msgSend$constraintEqualToAnchor:constant:
+ _objc_msgSend$constraintEqualToConstant:
+ _objc_msgSend$currentDevice
+ _objc_msgSend$fileFormatIsHDRSettingsChanged
+ _objc_msgSend$fullScreenPreviewsSettingsChanged
+ _objc_msgSend$hasRemoteViewController
+ _objc_msgSend$hdrBackingSurface
+ _objc_msgSend$hdrSurface
+ _objc_msgSend$heightAnchor
+ _objc_msgSend$initWithArrangedSubviews:
+ _objc_msgSend$initWithContentEditingInput:withOptions:
+ _objc_msgSend$initWithImage:menu:
+ _objc_msgSend$interfaceOrientation
+ _objc_msgSend$isHighDynamicRange
+ _objc_msgSend$jpegImageDataFromImage:withProperties:
+ _objc_msgSend$leadingAnchor
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$objectForKey:inDomain:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$saveImageDataToTemporaryLocation:withName:imageDescription:completionHandler:
+ _objc_msgSend$sdrSurface
+ _objc_msgSend$setAlignment:
+ _objc_msgSend$setAxis:
+ _objc_msgSend$setHdrBackingSurface:
+ _objc_msgSend$setObject:forKey:inDomain:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setOverrideUserInterfaceStyle:
+ _objc_msgSend$setPreferHEICForRenderedImages:
+ _objc_msgSend$setSpacing:
+ _objc_msgSend$setTitle:
+ _objc_msgSend$setTranslatesAutoresizingMaskIntoConstraints:
+ _objc_msgSend$sharedStatisticsManager
+ _objc_msgSend$ss_dataWithFileFormat:addProperties:
+ _objc_msgSend$ss_heicData
+ _objc_msgSend$ss_imageProperties
+ _objc_msgSend$ss_ioSurfaceImageData
+ _objc_msgSend$ss_isHDRImage
+ _objc_msgSend$ss_isHEICImageData:
+ _objc_msgSend$ss_pngData
+ _objc_msgSend$ss_ppkHeicDataWithProperties:
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$trailingAnchor
+ _objc_msgSend$widthAnchor
+ _objc_retain_x5
+ _objc_setProperty_atomic
+ _os_variant_has_internal_diagnostics
+ _sharedStatisticsManager.onceToken
- +[SSScreenshotAssetManagerPhotoLibraryBackend imageDataFromImage:withProperties:]
- +[SSScreenshotAssetManagerPhotoLibraryBackend imageDataFromImage:withProperties:].cold.1
- +[SSScreenshotAssetManagerPhotoLibraryBackend imageDataFromImage:withProperties:].cold.2
- +[SSScreenshotAssetManagerPhotoLibraryBackend imageDataFromImage:withProperties:].cold.3
- -[SSImageSurface initWithBSXPCCoder:].cold.1
- -[SSScreenshotAssetManagerPhotoLibraryBackend saveImageToTemporaryLocation:withName:imageDescription:completionHandler:].cold.1
- -[SSScreenshotAssetManagerPhotoLibraryBackend saveImageToTemporaryLocation:withName:imageDescription:completionHandler:].cold.2
- -[SSScreenshotAssetManagerPhotoLibraryBackend saveImageToTemporaryLocation:withName:imageDescription:completionHandler:].cold.3
- -[SSScreenshotAssetManagerPhotoLibraryBackend saveImageToTemporaryLocation:withName:imageDescription:completionHandler:].cold.4
- GCC_except_table17
- _PHImageDataFromImageAsScreenshot
- _UIImagePNGRepresentation
- ___103-[SSScreenshotAssetManagerPhotoLibraryBackend _registerEntryWithImage:options:retry:identifierHandler:]_block_invoke.48
- ___103-[SSScreenshotAssetManagerPhotoLibraryBackend _registerEntryWithImage:options:retry:identifierHandler:]_block_invoke.48.cold.1
- ___162-[SSScreenshotAssetManagerPhotoLibraryBackend updateImageData:withModificationData:forEntryWithIdentifier:registrationOptions:imageDescription:completionHandler:]_block_invoke.63
- ___77+[SSScreenshotMetadataHarvester harvestScreenshotMetadataAndRespondToAction:]_block_invoke.27
- ___77+[SSScreenshotMetadataHarvester harvestScreenshotMetadataAndRespondToAction:]_block_invoke.28
- ___86-[SSScreenshotAssetManager recordEditsToPersistable:inTransition:withCompletionBlock:]_block_invoke.12
- ___block_descriptor_56_e8_32s40s48bs_e16_v16?0"NSData"8ls32l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e48_v24?0"PHContentEditingInput"8"NSDictionary"16ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.18
- ___block_literal_global.26
- ___block_literal_global.31
- ___block_literal_global.38
- ___block_literal_global.43
- ___block_literal_global.50
- ___getVKSelectableBarButtonItemClass_block_invoke
- ___getVKSelectableBarButtonItemClass_block_invoke.cold.1
- _getVKSelectableBarButtonItemClass.softClass
- _objc_msgSend$imageDataFromImage:withProperties:
- _objc_msgSend$initWithContentEditingInput:
- _objc_msgSend$ioSurface
- _objc_msgSend$saveImageToTemporaryLocation:withName:imageDescription:completionHandler:
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "@\"UIStackView\""
+ "@\"VKCImageAnalysis\""
+ "BEGIN \"EncodeScreenshotImageData\""
+ "CLOSE"
+ "Close"
+ "DeviceSupportsCarIntegration"
+ "END \"EncodeScreenshotImageData\""
+ "EncodeScreenshotImageData"
+ "Failed to assign surface ownership (surface=%p, key=%@) to task %d"
+ "Preferences"
+ "SSChromeFactory"
+ "SSImageSurfaceHDRBackingSurfaceKey"
+ "SSLastUsedScreenshotShareFormatOption"
+ "SSPreferences"
+ "SSPreferencesCarPlayScreenshotsEnabled"
+ "SSPreferencesHDRCaptureEnabled"
+ "SSPreferencesPIPExperienceEnabled"
+ "SSPreferencesVisualLookUpInSSSEnabled"
+ "SSStatisticsManager"
+ "Screenshot"
+ "ScreenshotsRedesign2025"
+ "ScreenshotsVI2025"
+ "Solarium"
+ "SwiftUI"
+ "T@\"VKCImageAnalysis\",&,V_earlyVIAnalysis"
+ "T^{__IOSurface=},N,V_hdrBackingSurface"
+ "^{CGImage=}16@0:8"
+ "_SSPreferencesDidChangeRemoteNotification"
+ "_appendSettingsAndSendEvent:block:"
+ "_closeItem"
+ "_containerStackView"
+ "_earlyVIAnalysis"
+ "_hdrBackingSurface"
+ "_initWithSDRIOSurface:HDRIOSurface:scale:orientation:"
+ "_sendEvent:block:"
+ "_ss_vi2Enabled"
+ "_statisticsEnabled"
+ "_triggerTypeForPresentationMode:"
+ "accidental_draw"
+ "activateConstraints:"
+ "annotation_count"
+ "arrow.uturn.backward"
+ "arrow.uturn.forward"
+ "beta_feedback_submitted"
+ "beta_feedback_tapped"
+ "carPlayScreenshots"
+ "carPlaySettingsChanged"
+ "centerYAnchor"
+ "change_type"
+ "checkmark"
+ "closeBarButtonItem"
+ "com.apple.screenshotservices.%@"
+ "constraintEqualToAnchor:"
+ "constraintEqualToAnchor:constant:"
+ "constraintEqualToConstant:"
+ "copy_and_delete"
+ "cropped"
+ "cropsCornerLengthLong"
+ "currentDevice"
+ "delete"
+ "didAccidentallyDraw"
+ "didChangeOpacityOnFullPage"
+ "didChangeOpacityOnNormalScreenshot"
+ "didCopyDeleteScreenshots"
+ "didCropInFullPageMode"
+ "didCropInNormalMode"
+ "didDeleteScreenshots"
+ "didRenameScreenshot"
+ "didSaveFullPagePDFToFiles"
+ "didSaveImageToFiles"
+ "didSaveImageToPhotos"
+ "didSaveImageToQuickNote"
+ "didSaveMixedAllToFiles"
+ "didSaveMixedToPhotosAndFiles"
+ "didSaveMixedToQuickNoteAndFiles"
+ "didSavePDFImageToPhotos"
+ "didShareFullPageMixedScreenshots"
+ "didShareFullPageScreenshotAsAutomaticImage"
+ "didShareFullPageScreenshotAsAutomaticPDF"
+ "didShareFullPageScreenshotAsImage"
+ "didShareFullPageScreenshotAsPDF"
+ "didShareScreenMultipleScreenshots"
+ "didShareScreenSingleScreenshots"
+ "didSubmitFeedbackWithAnnotationCount:"
+ "didTapBetaFeedbackButton"
+ "didTapFullPageSegment"
+ "done_action"
+ "dragendedsuccessfully"
+ "drewStrokes:"
+ "earlyVIAnalysis"
+ "edit"
+ "enable CarPlayScreenshots preference: %{BOOL}d"
+ "enable HDR preference: %{BOOL}d"
+ "enable PIP experience preference: %{BOOL}d"
+ "enable Visual Look Up in SSS preference: %{BOOL}d"
+ "fileFormatIsHDR"
+ "fileFormatIsHDRSettingsChanged"
+ "fullScreenPreview"
+ "fullScreenPreviewsSettingsChanged"
+ "full_page"
+ "full_page_segmented_control"
+ "fullscreen"
+ "fullscreenExperienceHadCropEvent"
+ "hasRemoteViewController"
+ "hdrBackingSurface"
+ "hdrSurface"
+ "heic"
+ "heightAnchor"
+ "image_to_files"
+ "image_to_photos"
+ "image_to_quick_note"
+ "initWithArrangedSubviews:"
+ "initWithContentEditingInput:withOptions:"
+ "initWithImage:menu:"
+ "interfaceOrientation"
+ "isHighDynamicRange"
+ "jpegImageDataFromImage:withProperties:"
+ "keyboard"
+ "keychord"
+ "leadingAnchor"
+ "localizedStringForKey:value:table:"
+ "logTotalAnnotations:"
+ "mixed_all_to_files"
+ "mixed_photos_and_files"
+ "mixed_quick_note_and_files"
+ "mutableCopy"
+ "normal"
+ "notify preferences did change"
+ "numberWithBool:"
+ "numberWithInt:"
+ "numberWithUnsignedInt:"
+ "objectForKey:inDomain:"
+ "objectForKeyedSubscript:"
+ "opacity"
+ "pdf_image_to_photos"
+ "pdf_to_files"
+ "pencil"
+ "pip"
+ "pipDragEndedSuccessfully"
+ "pipExpanded"
+ "pipSlidOffscreenDueToTimeout"
+ "public.heic"
+ "public.png"
+ "reason"
+ "rename_screenshot"
+ "roundedCropsLength"
+ "saveImageDataToTemporaryLocation:persistable:completionHandler:"
+ "saveImageDataToTemporaryLocation:withName:imageDescription:completionHandler:"
+ "screenshotGestureTriggered:"
+ "screenshotGestureTriggeredWhileAnotherScreenshotWasShowing:"
+ "screenshot_showing"
+ "sdrSurface"
+ "setAlignment:"
+ "setAxis:"
+ "setEarlyVIAnalysis:"
+ "setHdrBackingSurface:"
+ "setObject:forKey:inDomain:"
+ "setObject:forKeyedSubscript:"
+ "setOverrideUserInterfaceStyle:"
+ "setPreferHEICForRenderedImages:"
+ "setSpacing:"
+ "setTitle:"
+ "setTranslatesAutoresizingMaskIntoConstraints:"
+ "settingsChanged"
+ "settingsName"
+ "share_action"
+ "share_full_page_mixed_screenshots"
+ "share_full_page_screenshot_as_automatic_image"
+ "share_full_page_screenshot_as_automatic_pdf"
+ "share_full_page_screenshot_as_image"
+ "share_full_page_screenshot_as_pdf"
+ "share_screen_multiple_screenshots"
+ "share_screen_single_screenshot"
+ "sharedStatisticsManager"
+ "skip enable CarPlayScreenshots preference: %{BOOL}d"
+ "skip enable HDR preference: %{BOOL}d"
+ "skip enable PIP preference: %{BOOL}d"
+ "skip enable Visual Look Up in SSS preference: %{BOOL}d"
+ "slidoffscreenduetotimer"
+ "ss_dataWithFileFormat:addProperties:"
+ "ss_hdrSurfaceCGImage"
+ "ss_heicData"
+ "ss_imageProperties"
+ "ss_ioSurfaceImageData"
+ "ss_isHDRImage"
+ "ss_isHEICImageData:"
+ "ss_jpegData"
+ "ss_pngData"
+ "ss_ppkHeicDataWithProperties:"
+ "ss_sdrSurfaceCGImage"
+ "standardUserDefaults"
+ "stroke_count"
+ "tapped"
+ "trailingAnchor"
+ "triggerType"
+ "triggered"
+ "type"
+ "unexpected NULL backing surface for image %@"
+ "v20@?0@\"NSData\"8B16"
+ "v48@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSURL\"@\"NSError\">40"
+ "widthAnchor"
+ "xmark"
- "@\"VKSelectableBarButtonItem\""
- "Failed to assign surface ownership to task %d"
- "VKSelectableBarButtonItem"
- "imageDataFromImage:withProperties:"
- "initWithContentEditingInput:"
- "ioSurface"
- "unexpected NULL backing surface for image %@ (copied:%d)"
- "v16@?0@\"NSData\"8"

```
