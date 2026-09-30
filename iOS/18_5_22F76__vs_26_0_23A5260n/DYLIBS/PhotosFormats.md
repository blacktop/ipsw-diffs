## PhotosFormats

> `/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats`

```diff

-760.6.150.0.0
-  __TEXT.__text: 0xc312c
-  __TEXT.__auth_stubs: 0x1cb0
-  __TEXT.__objc_methlist: 0xaf58
-  __TEXT.__const: 0x2ce0
+800.14.111.0.0
+  __TEXT.__text: 0xceff8
+  __TEXT.__auth_stubs: 0x1ce0
+  __TEXT.__objc_methlist: 0xbf68
+  __TEXT.__const: 0x2d20
   __TEXT.__dlopen_cstrs: 0x1a4
-  __TEXT.__gcc_except_tab: 0x3030
-  __TEXT.__cstring: 0xc52a
-  __TEXT.__oslogstring: 0x68e5
-  __TEXT.__unwind_info: 0x2eb0
-  __TEXT.__objc_classname: 0x1272
-  __TEXT.__objc_methname: 0x1a2b7
-  __TEXT.__objc_methtype: 0x4de0
-  __TEXT.__objc_stubs: 0xfc60
-  __DATA_CONST.__got: 0x1448
-  __DATA_CONST.__const: 0x27f0
-  __DATA_CONST.__objc_classlist: 0x488
-  __DATA_CONST.__objc_protolist: 0x110
+  __TEXT.__gcc_except_tab: 0x30c4
+  __TEXT.__cstring: 0xcccd
+  __TEXT.__oslogstring: 0x6a9d
+  __TEXT.__unwind_info: 0x3128
+  __TEXT.__objc_classname: 0x14dd
+  __TEXT.__objc_methname: 0x1ca04
+  __TEXT.__objc_methtype: 0x5277
+  __TEXT.__objc_stubs: 0x10c80
+  __DATA_CONST.__got: 0x1538
+  __DATA_CONST.__const: 0x29a0
+  __DATA_CONST.__objc_classlist: 0x510
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5830
+  __DATA_CONST.__objc_selrefs: 0x5dc8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x308
+  __DATA_CONST.__objc_superrefs: 0x358
   __DATA_CONST.__objc_arraydata: 0x7e0
-  __AUTH_CONST.__auth_got: 0xe70
-  __AUTH_CONST.__const: 0x1990
-  __AUTH_CONST.__cfstring: 0xbaa0
-  __AUTH_CONST.__objc_const: 0x11a20
+  __AUTH_CONST.__auth_got: 0xe88
+  __AUTH_CONST.__const: 0x1af0
+  __AUTH_CONST.__cfstring: 0xc1c0
+  __AUTH_CONST.__objc_const: 0x136c8
   __AUTH_CONST.__objc_intobj: 0x8a0
   __AUTH_CONST.__objc_arrayobj: 0x330
-  __AUTH_CONST.__objc_doubleobj: 0x1a0
+  __AUTH_CONST.__objc_doubleobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0x1e0
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xb00
-  __DATA.__data: 0xe18
-  __DATA.__bss: 0x7e8
-  __DATA_DIRTY.__objc_data: 0x2cb0
-  __DATA_DIRTY.__bss: 0xb20
+  __AUTH.__objc_data: 0x488
+  __DATA.__objc_ivar: 0xc64
+  __DATA.__data: 0xdb8
+  __DATA.__bss: 0x878
+  __DATA_DIRTY.__objc_data: 0x2e18
+  __DATA_DIRTY.__bss: 0x990
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto
   - /System/Library/PrivateFrameworks/MMCS.framework/MMCS

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 7835744E-3A0F-3326-B30B-7FAE6512B37E
-  Functions: 4233
-  Symbols:   14574
-  CStrings:  8614
+  UUID: 324966D8-D292-3A0A-A548-8487C997A88B
+  Functions: 4593
+  Symbols:   15699
+  CStrings:  9094
 
Symbols:
+ +[PFClientSideEncryptionManager applyOptions:toArchive:]
+ +[PFCropUtilities bestAdaptiveCropRectForPosterClassification:layoutConfiguration:sourcePixelWidth:sourcePixelHeight:sourcePreferredCropRectNormalized:sourceAcceptableCropRectNormalized:sourceFaceAreaRectNormalized:]
+ +[PFCropUtilities bestAdaptiveCropRectForPosterClassification:layoutConfiguration:sourcePixelWidth:sourcePixelHeight:sourcePreferredCropRectNormalized:sourceAcceptableCropRectNormalized:sourceFaceAreaRectNormalized:headroomFeasible:]
+ +[PFImageMetadataChangePolicy standardPolicy]
+ +[PFImageMetadataChangePolicy supportsSecureCoding]
+ +[PFImageMetadataChangePolicyAddPFMetadata policyWithKey:value:]
+ +[PFImageMetadataChangePolicyAddPFMetadata supportsSecureCoding]
+ +[PFImageMetadataChangePolicyComposite policyWithPolicies:]
+ +[PFImageMetadataChangePolicyComposite supportsSecureCoding]
+ +[PFImageMetadataChangePolicyDefault policyWithLossyCompressionQuality:]
+ +[PFImageMetadataChangePolicyDefault standardPolicy]
+ +[PFImageMetadataChangePolicyDefault supportsSecureCoding]
+ +[PFImageMetadataChangePolicySetAccessibilityDescription policyWithAccessibilityDescription:]
+ +[PFImageMetadataChangePolicySetAccessibilityDescription supportsSecureCoding]
+ +[PFImageMetadataChangePolicySetCaption policyWithCaption:]
+ +[PFImageMetadataChangePolicySetCaption supportsSecureCoding]
+ +[PFImageMetadataChangePolicySetCreationDate policyWithCreationDate:inTimeZone:]
+ +[PFImageMetadataChangePolicySetCreationDate supportsSecureCoding]
+ +[PFImageMetadataChangePolicySetLocation policyWithLocation:]
+ +[PFImageMetadataChangePolicySetLocation supportsSecureCoding]
+ +[PFImageMetadataChangePolicySharedPhotoStream _filterImageProperties:metadataWithKey:preserveProperties:]
+ +[PFImageMetadataChangePolicySharedPhotoStream policyWithAllowLocation:]
+ +[PFImageMetadataChangePolicySharedPhotoStream supportsSecureCoding]
+ +[PFImageMetadataChangePolicyiCloudPhotoLibrary standardPolicy]
+ +[PFMediaUtilities typeRequiresRasterization:]
+ +[PFMetadataIdentifier quickTimeUserDataMultitrackMemoryMovieType]
+ +[PFMetadataIdentifier quicktimeMetadataCinematicVideoIntent]
+ +[PFParallaxDataLayer(Archiver) fileExtension]
+ +[PFParallaxLayoutConfiguration _fallbackTimeRectCollectionForSBSFetchingFailureWithOrientation:]
+ +[PFParallaxLayoutConfiguration _loadDeviceTimeRectCollectionIfNeeded]
+ +[PFParallaxLayoutConfiguration timeRectCollectionLandscape]
+ +[PFParallaxLayoutConfiguration timeRectCollectionPortrait]
+ +[PFParallaxLayoutHelper closeupZoomPercentWithLayoutType:]
+ +[PFParallaxLayoutHelper scoreBonusAdaptiveWithLayoutType:]
+ +[PFParallaxLayoutHelper scoreBonusOverlapStretchWithLayoutType:]
+ +[PFParallaxLayoutHelper targetCenterZoomFactorWithLayoutType:]
+ +[PFParallaxLayoutUtilities adaptiveFrameForTopEdgeVisibleFrame:layoutConfiguration:outVisibleFrame:maxClockStretchOverride:]
+ +[PFParallaxLayoutUtilities adaptiveFrameForVisibleFrame:essentialRect:originalImageSize:layoutConfiguration:classification:maxClockStretchOverride:]
+ +[PFParallaxLayoutUtilities adaptiveLayoutVerticalPriorityThreshold]
+ +[PFParallaxLayoutUtilities centerLayoutHorizontalLowerBound]
+ +[PFParallaxLayoutUtilities centerLayoutHorizontalUpperBound]
+ +[PFParallaxLayoutUtilities computeSpatialFrameForVisibleRect:adaptiveVisibleRect:spatialPaddingPercentage:effectiveImageRect:]
+ +[PFParallaxLayoutUtilities topFrameForVisibleRect:adaptiveRect:]
+ +[PFParallaxLayoutUtilities topFrameFromVisibleRectAspectRatio:adaptiveRect:]
+ +[PFParallaxLayoutUtilities widgetZoneAdjustmentForVisibleFrame:essentialRect:]
+ +[PFParallaxSpatialPhotoLayer(Archiver) fileExtension]
+ +[PFParallaxSpatialPhotoOcclusionLayer(Archiver) fileExtension]
+ +[PFPosterMediaURLImage supportsSecureCoding]
+ +[PFWallpaperCompoundDeviceConfiguration deviceBackdropRoleConfiguration]
+ +[PFWallpaperCompoundDeviceConfiguration forceDisableLandscapeConfiguration:]
+ +[PFWallpaperCompoundDeviceConfiguration genericBackdropConfigurationWithTitleBounds:]
+ +[PFWallpaperCompoundDeviceConfiguration specificConfigurationWithPortraitTitleBounds:portraitScreenSize:landscapeScreenSize:]
+ -[NSValue(NSValuePFWallpaperExtensions) rectValue]
+ -[PFClientSideEncryptionManager archiveFileAtURL:outputFileURL:options:error:]
+ -[PFCropUtilitiesPosterOutputData adaptiveHeadroom]
+ -[PFCropUtilitiesPosterOutputData adaptiveVisibleRect]
+ -[PFCropUtilitiesPosterOutputData clockOverlapAcceptable]
+ -[PFCropUtilitiesPosterOutputData cropScore]
+ -[PFCropUtilitiesPosterOutputData headroomEngaged]
+ -[PFCropUtilitiesPosterOutputData initWithVisibleRect:adaptiveVisibleRect:cropScore:layoutScore:clockOverlapAcceptable:headroomEngaged:adaptiveHeadroom:maxClockShift:layoutVariant:notificationRoom:]
+ -[PFCropUtilitiesPosterOutputData layoutScore]
+ -[PFCropUtilitiesPosterOutputData layoutVariant]
+ -[PFCropUtilitiesPosterOutputData maxClockShift]
+ -[PFCropUtilitiesPosterOutputData notificationRoom]
+ -[PFCropUtilitiesPosterOutputData visibleRect]
+ -[PFDeviceTimeRectCollection .cxx_destruct]
+ -[PFDeviceTimeRectCollection _timeRectInImageSpaceFromPointSpaceRect:screenScale:]
+ -[PFDeviceTimeRectCollection imageSpaceTimeRectForPointSpaceTimeRect:]
+ -[PFDeviceTimeRectCollection initWithPointSpaceSortedTimeRectss:screenScale:]
+ -[PFDeviceTimeRectCollection maxTimeRectInImageSpace]
+ -[PFDeviceTimeRectCollection maxTimeRect]
+ -[PFDeviceTimeRectCollection minTimeRectInImageSpace]
+ -[PFDeviceTimeRectCollection minTimeRect]
+ -[PFDeviceTimeRectCollection nearestRectForPointSpaceHeight:]
+ -[PFDeviceTimeRectCollection sortedTimeRects]
+ -[PFImageIOOptionsBuilder .cxx_destruct]
+ -[PFImageIOOptionsBuilder applyTransform]
+ -[PFImageIOOptionsBuilder colorBehavior]
+ -[PFImageIOOptionsBuilder includeDerivativeDefaults]
+ -[PFImageIOOptionsBuilder includeHDRGainMaps]
+ -[PFImageIOOptionsBuilder initWithOptions:]
+ -[PFImageIOOptionsBuilder init]
+ -[PFImageIOOptionsBuilder maximumLongSideLength]
+ -[PFImageIOOptionsBuilder objectForKeyedSubscript:]
+ -[PFImageIOOptionsBuilder options]
+ -[PFImageIOOptionsBuilder orientation]
+ -[PFImageIOOptionsBuilder setApplyTransform:]
+ -[PFImageIOOptionsBuilder setColorBehavior:]
+ -[PFImageIOOptionsBuilder setIncludeDerivativeDefaults:]
+ -[PFImageIOOptionsBuilder setIncludeHDRGainMaps:]
+ -[PFImageIOOptionsBuilder setMaximumLongSideLength:]
+ -[PFImageIOOptionsBuilder setObject:forKeyedSubscript:]
+ -[PFImageIOOptionsBuilder setOrientation:]
+ -[PFImageIOOptionsBuilder setSkipMetadata:]
+ -[PFImageIOOptionsBuilder skipMetadata]
+ -[PFImageMetadataChangePolicy encodeWithCoder:]
+ -[PFImageMetadataChangePolicy initWithCoder:]
+ -[PFImageMetadataChangePolicy metadataNeedsProcessing:]
+ -[PFImageMetadataChangePolicy processMetadata:]
+ -[PFImageMetadataChangePolicyAddPFMetadata .cxx_destruct]
+ -[PFImageMetadataChangePolicyAddPFMetadata encodeWithCoder:]
+ -[PFImageMetadataChangePolicyAddPFMetadata initWithCoder:]
+ -[PFImageMetadataChangePolicyAddPFMetadata key]
+ -[PFImageMetadataChangePolicyAddPFMetadata metadataNeedsProcessing:]
+ -[PFImageMetadataChangePolicyAddPFMetadata processMetadata:]
+ -[PFImageMetadataChangePolicyAddPFMetadata setKey:]
+ -[PFImageMetadataChangePolicyAddPFMetadata setValue:]
+ -[PFImageMetadataChangePolicyAddPFMetadata value]
+ -[PFImageMetadataChangePolicyComposite .cxx_destruct]
+ -[PFImageMetadataChangePolicyComposite encodeWithCoder:]
+ -[PFImageMetadataChangePolicyComposite initWithCoder:]
+ -[PFImageMetadataChangePolicyComposite metadataNeedsProcessing:]
+ -[PFImageMetadataChangePolicyComposite policies]
+ -[PFImageMetadataChangePolicyComposite processMetadata:]
+ -[PFImageMetadataChangePolicyComposite setPolicies:]
+ -[PFImageMetadataChangePolicyDefault encodeWithCoder:]
+ -[PFImageMetadataChangePolicyDefault initWithCoder:]
+ -[PFImageMetadataChangePolicyDefault initWithLossyCompressionQuality:]
+ -[PFImageMetadataChangePolicyDefault init]
+ -[PFImageMetadataChangePolicyDefault lossyCompressionQuality]
+ -[PFImageMetadataChangePolicyDefault metadataNeedsProcessing:]
+ -[PFImageMetadataChangePolicyDefault processMetadata:]
+ -[PFImageMetadataChangePolicyDefault setLossyCompressionQuality:]
+ -[PFImageMetadataChangePolicySetAccessibilityDescription .cxx_destruct]
+ -[PFImageMetadataChangePolicySetAccessibilityDescription accessibilityDescription]
+ -[PFImageMetadataChangePolicySetAccessibilityDescription encodeWithCoder:]
+ -[PFImageMetadataChangePolicySetAccessibilityDescription initWithCoder:]
+ -[PFImageMetadataChangePolicySetAccessibilityDescription metadataNeedsProcessing:]
+ -[PFImageMetadataChangePolicySetAccessibilityDescription processMetadata:]
+ -[PFImageMetadataChangePolicySetAccessibilityDescription setAccessibilityDescription:]
+ -[PFImageMetadataChangePolicySetCaption .cxx_destruct]
+ -[PFImageMetadataChangePolicySetCaption caption]
+ -[PFImageMetadataChangePolicySetCaption encodeWithCoder:]
+ -[PFImageMetadataChangePolicySetCaption initWithCoder:]
+ -[PFImageMetadataChangePolicySetCaption metadataNeedsProcessing:]
+ -[PFImageMetadataChangePolicySetCaption processMetadata:]
+ -[PFImageMetadataChangePolicySetCaption setCaption:]
+ -[PFImageMetadataChangePolicySetCreationDate .cxx_destruct]
+ -[PFImageMetadataChangePolicySetCreationDate creationDate]
+ -[PFImageMetadataChangePolicySetCreationDate encodeWithCoder:]
+ -[PFImageMetadataChangePolicySetCreationDate initWithCoder:]
+ -[PFImageMetadataChangePolicySetCreationDate metadataNeedsProcessing:]
+ -[PFImageMetadataChangePolicySetCreationDate processMetadata:]
+ -[PFImageMetadataChangePolicySetCreationDate setCreationDate:]
+ -[PFImageMetadataChangePolicySetCreationDate setTimeZone:]
+ -[PFImageMetadataChangePolicySetCreationDate timeZone]
+ -[PFImageMetadataChangePolicySetLocation .cxx_destruct]
+ -[PFImageMetadataChangePolicySetLocation encodeWithCoder:]
+ -[PFImageMetadataChangePolicySetLocation initWithCoder:]
+ -[PFImageMetadataChangePolicySetLocation location]
+ -[PFImageMetadataChangePolicySetLocation metadataNeedsProcessing:]
+ -[PFImageMetadataChangePolicySetLocation processMetadata:]
+ -[PFImageMetadataChangePolicySetLocation setLocation:]
+ -[PFImageMetadataChangePolicySharedPhotoStream metadataNeedsProcessing:]
+ -[PFImageMetadataChangePolicySharedPhotoStream processMetadata:]
+ -[PFImageMetadataChangePolicyiCloudPhotoLibrary processMetadata:]
+ -[PFMetadata cinematicVideoIntent]
+ -[PFMetadata hasAlphaChannel]
+ -[PFMetadataImage hasAlphaChannel]
+ -[PFMetadataMovie cinematicVideoIntent]
+ -[PFParallaxDataLayer .cxx_destruct]
+ -[PFParallaxDataLayer data]
+ -[PFParallaxDataLayer initWithData:frame:zPosition:identifier:]
+ -[PFParallaxDataLayer layerByUpdatingFrame:]
+ -[PFParallaxDataLayer pixelSize]
+ -[PFParallaxDataLayer(Archiver) fileExtension]
+ -[PFParallaxDataLayer(Archiver) saveToURL:error:]
+ -[PFParallaxIntermediateLayout adaptiveHeadroom]
+ -[PFParallaxIntermediateLayout adaptiveInactiveTopRect]
+ -[PFParallaxIntermediateLayout adaptiveStrategy]
+ -[PFParallaxIntermediateLayout adaptiveVisibleRect]
+ -[PFParallaxIntermediateLayout copyWithZone:]
+ -[PFParallaxIntermediateLayout headroomUsage:]
+ -[PFParallaxIntermediateLayout initWithConfiguration:]
+ -[PFParallaxIntermediateLayout isAdaptiveLayout]
+ -[PFParallaxIntermediateLayout layoutVariant]
+ -[PFParallaxIntermediateLayout maxClockShift]
+ -[PFParallaxIntermediateLayout mutableCopyWithZone:]
+ -[PFParallaxIntermediateLayout salientContentRect]
+ -[PFParallaxIntermediateLayout spatialAdaptiveVisibleRect]
+ -[PFParallaxIntermediateLayout spatialStrategy]
+ -[PFParallaxIntermediateLayout spatialVisibleRect]
+ -[PFParallaxIntermediateLayout updateWithConfiguration:]
+ -[PFParallaxIntermediateLayout zoomFactor]
+ -[PFParallaxLayer isSpatialPhoto]
+ -[PFParallaxLayerStack inactiveSpatialPhotoDataLayer]
+ -[PFParallaxLayerStack initWithLayers:layout:depthEnabled:parallaxDisabled:clockAreaLuminance:settlingEffectEnabled:spatialPhotoEnabled:]
+ -[PFParallaxLayerStack spatialPhotoBackgroundLayer]
+ -[PFParallaxLayerStack spatialPhotoEnabled]
+ -[PFParallaxLayerStack spatialPhotoForegroundLayer]
+ -[PFParallaxLayerStack(Updating) layerStackByUpdatingSpatialPhotoEnabled:]
+ -[PFParallaxLayoutConfiguration isPortrait]
+ -[PFParallaxLayoutConfiguration maxStrechAmountNormalized]
+ -[PFParallaxLayoutConfiguration stretchedTimeOverlapCheckBottom:visibleFrame:]
+ -[PFParallaxLayoutConfiguration stretchedTimeOverlapCheckTop:visibleFrame:]
+ -[PFParallaxLayoutConfiguration timeOverlapCheckBottomForTimeRect:]
+ -[PFParallaxLayoutConfiguration timeOverlapCheckTopForTimeRect:]
+ -[PFParallaxLayoutConfiguration timeRectForNormalizedHeight:]
+ -[PFParallaxLayoutHelper allowedClockStretch]
+ -[PFParallaxLayoutHelper allowedLayoutStrategies]
+ -[PFParallaxLayoutHelper computeSpatial]
+ -[PFParallaxLayoutHelper initWithPosterClassification:initialRect:imageSize:effectiveAcceptableRect:effectivePreferredRect:validBoundsNormalized:headroomFeasible:hasTopEdgeContact:computeSpatial:spatialPadding:layoutType:allowedLayoutStrategies:layoutConfiguration:]
+ -[PFParallaxLayoutHelper intermediateWithAdaptiveStrategy:intermediate:]
+ -[PFParallaxLayoutHelper intermediateWithSpatialStrategy:intermediate:]
+ -[PFParallaxLayoutHelper setAllowedClockStretch:]
+ -[PFParallaxLayoutHelper spatialPadding]
+ -[PFParallaxMutableIntermediateLayout adaptiveInactiveTopRect]
+ -[PFParallaxMutableIntermediateLayout adaptiveStrategy]
+ -[PFParallaxMutableIntermediateLayout adaptiveVisibleRect]
+ -[PFParallaxMutableIntermediateLayout cropScore]
+ -[PFParallaxMutableIntermediateLayout hasTopEdgeContact]
+ -[PFParallaxMutableIntermediateLayout headroomStrategy]
+ -[PFParallaxMutableIntermediateLayout inactiveRect]
+ -[PFParallaxMutableIntermediateLayout inactiveStrategy]
+ -[PFParallaxMutableIntermediateLayout layoutScore]
+ -[PFParallaxMutableIntermediateLayout layoutVariant]
+ -[PFParallaxMutableIntermediateLayout maxClockShift]
+ -[PFParallaxMutableIntermediateLayout overlapStrategy]
+ -[PFParallaxMutableIntermediateLayout parallaxStrategy]
+ -[PFParallaxMutableIntermediateLayout salientContentRect]
+ -[PFParallaxMutableIntermediateLayout setAdaptiveInactiveTopRect:]
+ -[PFParallaxMutableIntermediateLayout setAdaptiveStrategy:]
+ -[PFParallaxMutableIntermediateLayout setAdaptiveVisibleRect:]
+ -[PFParallaxMutableIntermediateLayout setCropScore:]
+ -[PFParallaxMutableIntermediateLayout setHasTopEdgeContact:]
+ -[PFParallaxMutableIntermediateLayout setHeadroomStrategy:]
+ -[PFParallaxMutableIntermediateLayout setInactiveRect:]
+ -[PFParallaxMutableIntermediateLayout setInactiveStrategy:]
+ -[PFParallaxMutableIntermediateLayout setLayoutScore:]
+ -[PFParallaxMutableIntermediateLayout setLayoutVariant:]
+ -[PFParallaxMutableIntermediateLayout setMaxClockShift:]
+ -[PFParallaxMutableIntermediateLayout setOverlapStrategy:]
+ -[PFParallaxMutableIntermediateLayout setParallaxStrategy:]
+ -[PFParallaxMutableIntermediateLayout setSalientContentRect:]
+ -[PFParallaxMutableIntermediateLayout setSpatialAdaptiveVisibleRect:]
+ -[PFParallaxMutableIntermediateLayout setSpatialStrategy:]
+ -[PFParallaxMutableIntermediateLayout setSpatialVisibleRect:]
+ -[PFParallaxMutableIntermediateLayout setTimeBottomOverlap:]
+ -[PFParallaxMutableIntermediateLayout setTimeTopOverlap:]
+ -[PFParallaxMutableIntermediateLayout setUninflatedUnsafeAreaOverlap:]
+ -[PFParallaxMutableIntermediateLayout setUnsafeAreaOverlap:]
+ -[PFParallaxMutableIntermediateLayout setVisibleRect:]
+ -[PFParallaxMutableIntermediateLayout setZoomFactor:]
+ -[PFParallaxMutableIntermediateLayout setZoomStrategy:]
+ -[PFParallaxMutableIntermediateLayout spatialAdaptiveVisibleRect]
+ -[PFParallaxMutableIntermediateLayout spatialStrategy]
+ -[PFParallaxMutableIntermediateLayout spatialVisibleRect]
+ -[PFParallaxMutableIntermediateLayout timeBottomOverlap]
+ -[PFParallaxMutableIntermediateLayout timeTopOverlap]
+ -[PFParallaxMutableIntermediateLayout uninflatedUnsafeAreaOverlap]
+ -[PFParallaxMutableIntermediateLayout unsafeAreaOverlap]
+ -[PFParallaxMutableIntermediateLayout visibleRect]
+ -[PFParallaxMutableIntermediateLayout zoomFactor]
+ -[PFParallaxMutableIntermediateLayout zoomStrategy]
+ -[PFParallaxSpatialPhotoLayer .cxx_destruct]
+ -[PFParallaxSpatialPhotoLayer dataRepresentation]
+ -[PFParallaxSpatialPhotoLayer initWithSceneData:scene:frame:zPosition:identifier:]
+ -[PFParallaxSpatialPhotoLayer layerByUpdatingFrame:]
+ -[PFParallaxSpatialPhotoLayer pixelSize]
+ -[PFParallaxSpatialPhotoLayer sceneData]
+ -[PFParallaxSpatialPhotoLayer scene]
+ -[PFParallaxSpatialPhotoLayer(Archiver) fileExtension]
+ -[PFParallaxSpatialPhotoLayer(Archiver) saveToURL:error:]
+ -[PFParallaxSpatialPhotoOcclusionLayer initWithFrame:zPosition:identifier:]
+ -[PFParallaxSpatialPhotoOcclusionLayer layerByUpdatingFrame:]
+ -[PFParallaxSpatialPhotoOcclusionLayer pixelSize]
+ -[PFParallaxSpatialPhotoOcclusionLayer(Archiver) fileExtension]
+ -[PFParallaxSpatialPhotoOcclusionLayer(Archiver) saveToURL:error:]
+ -[PFPosterConfiguration allowedLayoutStrategies]
+ -[PFPosterConfiguration initWithConfigurationType:photoLibraryIdentifier:]
+ -[PFPosterConfiguration photoLibraryIdentifier]
+ -[PFPosterConfiguration setAllowedLayoutStrategies:]
+ -[PFPosterDescriptor initWithDescriptorType:media:photoLibraryIdentifier:]
+ -[PFPosterDescriptor photoLibraryIdentifier]
+ -[PFPosterEditConfiguration additionalTitleLabelHeight]
+ -[PFPosterEditConfiguration isSpatialPhotoAvailable]
+ -[PFPosterEditConfiguration isSpatialPhotoEnabled]
+ -[PFPosterEditConfiguration normalizedAdaptiveTimeFrame]
+ -[PFPosterEditConfiguration normalizedAdaptiveVisibleFrame]
+ -[PFPosterEditConfiguration normalizedLandscapeAdaptiveTimeFrame]
+ -[PFPosterEditConfiguration normalizedLandscapeAdaptiveVisibleFrame]
+ -[PFPosterEditConfiguration setAdditionalTitleLabelHeight:]
+ -[PFPosterEditConfiguration setIsSpatialPhotoAvailable:]
+ -[PFPosterEditConfiguration setIsSpatialPhotoEnabled:]
+ -[PFPosterEditConfiguration setNormalizedAdaptiveTimeFrame:]
+ -[PFPosterEditConfiguration setNormalizedAdaptiveVisibleFrame:]
+ -[PFPosterEditConfiguration setNormalizedLandscapeAdaptiveTimeFrame:]
+ -[PFPosterEditConfiguration setNormalizedLandscapeAdaptiveVisibleFrame:]
+ -[PFPosterEditConfiguration setUserAdjustedTitleLabelHeightOffset:]
+ -[PFPosterEditConfiguration userAdjustedTitleLabelHeightOffset]
+ -[PFPosterLayout layoutByUpdatingNormalizedPortraitAdaptiveTimeFrame:landscapeAdaptiveTimeFrame:]
+ -[PFPosterLayout layoutByUpdatingNormalizedPortraitAdaptiveVisibleFrame:landscapeAdaptiveVisibleFrame:]
+ -[PFPosterMediaURLImage .cxx_destruct]
+ -[PFPosterMediaURLImage copyWithZone:]
+ -[PFPosterMediaURLImage encodeWithCoder:]
+ -[PFPosterMediaURLImage hash]
+ -[PFPosterMediaURLImage imageURL]
+ -[PFPosterMediaURLImage initWithCoder:]
+ -[PFPosterMediaURLImage initWithImageAtURL:]
+ -[PFPosterMediaURLImage isEqual:]
+ -[PFPosterMediaURLImage setImageURL:]
+ -[PFPosterOrientedLayout adaptiveInactiveTopFrame]
+ -[PFPosterOrientedLayout adaptiveTimeFrame]
+ -[PFPosterOrientedLayout adaptiveVisibleFrame]
+ -[PFPosterOrientedLayout initWithImageSize:deviceResolution:parallaxPadding:visibleFrame:adaptiveVisibleFrame:inactiveFrame:adaptiveInactiveTopFrame:spatialVisibleFrame:spatialAdaptiveFrame:timeFrame:adaptiveTimeFrame:salientContentFrame:clockLayerOrder:clockIntersection:layoutVariant:hasTopEdgeContact:maxClockShift:debugLayouts:]
+ -[PFPosterOrientedLayout initWithImageSize:deviceResolution:parallaxPadding:visibleFrame:adaptiveVisibleFrame:inactiveFrame:adaptiveInactiveTopFrame:timeFrame:clockLayerOrder:clockIntersection:layoutVariant:hasTopEdgeContact:maxClockShift:debugLayouts:]
+ -[PFPosterOrientedLayout layoutByUpdatingAdaptiveInactiveFrame:]
+ -[PFPosterOrientedLayout layoutByUpdatingAdaptiveTimeFrame:]
+ -[PFPosterOrientedLayout layoutByUpdatingAdaptiveVisibleFrame:]
+ -[PFPosterOrientedLayout layoutByUpdatingLayoutVariant:]
+ -[PFPosterOrientedLayout layoutByUpdatingMaxClockShift:]
+ -[PFPosterOrientedLayout layoutByUpdatingNormalizedAdaptiveTimeFrame:]
+ -[PFPosterOrientedLayout layoutByUpdatingNormalizedAdaptiveVisibleFrame:]
+ -[PFPosterOrientedLayout layoutByUpdatingNormalizedVisibleFrame:remapAdaptiveVisibleFrame:]
+ -[PFPosterOrientedLayout layoutVariant]
+ -[PFPosterOrientedLayout maxClockShift]
+ -[PFPosterOrientedLayout normalizedAdaptiveTimeFrameInVisibleFrame]
+ -[PFPosterOrientedLayout normalizedAdaptiveTimeFrame]
+ -[PFPosterOrientedLayout normalizedAdaptiveVisibleFrame]
+ -[PFPosterOrientedLayout originalImageExtent]
+ -[PFPosterOrientedLayout salientContentFrame]
+ -[PFPosterOrientedLayout spatialAdaptiveFrame]
+ -[PFPosterOrientedLayout spatialVisibleFrame]
+ -[PFWallpaperCompoundLayerStack compoundLayerStackByUpdatingSpatialPhotoEnabled:]
+ GCC_except_table1091
+ GCC_except_table1445
+ GCC_except_table1452
+ GCC_except_table1455
+ GCC_except_table1490
+ GCC_except_table1504
+ GCC_except_table1598
+ GCC_except_table1613
+ GCC_except_table1666
+ GCC_except_table1687
+ GCC_except_table1689
+ GCC_except_table1765
+ GCC_except_table1769
+ GCC_except_table1780
+ GCC_except_table1816
+ GCC_except_table1818
+ GCC_except_table1843
+ GCC_except_table1854
+ GCC_except_table1880
+ GCC_except_table1888
+ GCC_except_table1891
+ GCC_except_table1905
+ GCC_except_table1926
+ GCC_except_table1931
+ GCC_except_table1940
+ GCC_except_table2044
+ GCC_except_table2075
+ GCC_except_table2081
+ GCC_except_table2083
+ GCC_except_table2088
+ GCC_except_table2104
+ GCC_except_table2160
+ GCC_except_table2169
+ GCC_except_table2189
+ GCC_except_table2253
+ GCC_except_table2256
+ GCC_except_table2389
+ GCC_except_table2390
+ GCC_except_table2397
+ GCC_except_table2399
+ GCC_except_table2400
+ GCC_except_table2402
+ GCC_except_table2405
+ GCC_except_table2449
+ GCC_except_table2472
+ GCC_except_table2474
+ GCC_except_table2588
+ GCC_except_table267
+ GCC_except_table2865
+ GCC_except_table2932
+ GCC_except_table2933
+ GCC_except_table2936
+ GCC_except_table2938
+ GCC_except_table2939
+ GCC_except_table2943
+ GCC_except_table2945
+ GCC_except_table2947
+ GCC_except_table2948
+ GCC_except_table2949
+ GCC_except_table2951
+ GCC_except_table2952
+ GCC_except_table2961
+ GCC_except_table2968
+ GCC_except_table2978
+ GCC_except_table2980
+ GCC_except_table2987
+ GCC_except_table2990
+ GCC_except_table3010
+ GCC_except_table3013
+ GCC_except_table3014
+ GCC_except_table3019
+ GCC_except_table3020
+ GCC_except_table3021
+ GCC_except_table3022
+ GCC_except_table3023
+ GCC_except_table3029
+ GCC_except_table3032
+ GCC_except_table3089
+ GCC_except_table3218
+ GCC_except_table3220
+ GCC_except_table3222
+ GCC_except_table3223
+ GCC_except_table3225
+ GCC_except_table3226
+ GCC_except_table3228
+ GCC_except_table3229
+ GCC_except_table3230
+ GCC_except_table3234
+ GCC_except_table3240
+ GCC_except_table3247
+ GCC_except_table3250
+ GCC_except_table3251
+ GCC_except_table3253
+ GCC_except_table3258
+ GCC_except_table3259
+ GCC_except_table3260
+ GCC_except_table3266
+ GCC_except_table3273
+ GCC_except_table3274
+ GCC_except_table3291
+ GCC_except_table3337
+ GCC_except_table3341
+ GCC_except_table3344
+ GCC_except_table3345
+ GCC_except_table3395
+ GCC_except_table3404
+ GCC_except_table3479
+ GCC_except_table3547
+ GCC_except_table3549
+ GCC_except_table3576
+ GCC_except_table3591
+ GCC_except_table3593
+ GCC_except_table3673
+ GCC_except_table3891
+ GCC_except_table3893
+ GCC_except_table3895
+ GCC_except_table3902
+ GCC_except_table3907
+ GCC_except_table3917
+ GCC_except_table3924
+ GCC_except_table3927
+ GCC_except_table3928
+ GCC_except_table3929
+ GCC_except_table3933
+ GCC_except_table3935
+ GCC_except_table3942
+ GCC_except_table3946
+ GCC_except_table3955
+ GCC_except_table3958
+ GCC_except_table3959
+ GCC_except_table3960
+ GCC_except_table3961
+ GCC_except_table3962
+ GCC_except_table3969
+ GCC_except_table3970
+ GCC_except_table3973
+ GCC_except_table3977
+ GCC_except_table3978
+ GCC_except_table3980
+ GCC_except_table3981
+ GCC_except_table3984
+ GCC_except_table3997
+ GCC_except_table4004
+ GCC_except_table4009
+ GCC_except_table4010
+ GCC_except_table4014
+ GCC_except_table4018
+ GCC_except_table4039
+ GCC_except_table4043
+ GCC_except_table4044
+ GCC_except_table4045
+ GCC_except_table4046
+ GCC_except_table4047
+ GCC_except_table4048
+ GCC_except_table4050
+ GCC_except_table4055
+ GCC_except_table4056
+ GCC_except_table4058
+ GCC_except_table4059
+ GCC_except_table4061
+ GCC_except_table4062
+ GCC_except_table4063
+ GCC_except_table4064
+ GCC_except_table4065
+ GCC_except_table4066
+ GCC_except_table4068
+ GCC_except_table4070
+ GCC_except_table4071
+ GCC_except_table4072
+ GCC_except_table4073
+ GCC_except_table4076
+ GCC_except_table4145
+ GCC_except_table4212
+ GCC_except_table4218
+ GCC_except_table4287
+ GCC_except_table4291
+ GCC_except_table4293
+ GCC_except_table4296
+ GCC_except_table4297
+ GCC_except_table4315
+ GCC_except_table4330
+ GCC_except_table4331
+ GCC_except_table4332
+ GCC_except_table4334
+ GCC_except_table4336
+ GCC_except_table4581
+ GCC_except_table4588
+ GCC_except_table4590
+ GCC_except_table664
+ GCC_except_table671
+ GCC_except_table708
+ GCC_except_table712
+ GCC_except_table713
+ GCC_except_table714
+ GCC_except_table723
+ GCC_except_table726
+ GCC_except_table727
+ GCC_except_table729
+ GCC_except_table730
+ GCC_except_table731
+ GCC_except_table734
+ GCC_except_table738
+ GCC_except_table739
+ GCC_except_table740
+ GCC_except_table741
+ GCC_except_table742
+ GCC_except_table743
+ GCC_except_table748
+ GCC_except_table749
+ GCC_except_table754
+ GCC_except_table755
+ GCC_except_table759
+ GCC_except_table765
+ GCC_except_table766
+ GCC_except_table767
+ GCC_except_table768
+ GCC_except_table769
+ GCC_except_table771
+ GCC_except_table772
+ GCC_except_table773
+ GCC_except_table774
+ GCC_except_table775
+ GCC_except_table778
+ GCC_except_table780
+ GCC_except_table781
+ GCC_except_table782
+ GCC_except_table783
+ GCC_except_table787
+ GCC_except_table792
+ GCC_except_table806
+ GCC_except_table808
+ GCC_except_table809
+ GCC_except_table810
+ _AVAppleMakerNote_MeteorHeadroom
+ _AVMetadataIdentifierQuickTimeMetadataCinematicVideoIntent
+ _AVMetadataQuickTimeMetadataKeyCinematicVideoIntent
+ _MGGetSInt64Answer
+ _MGIsQuestionValid
+ _OBJC_CLASS_$_PFCropUtilitiesPosterOutputData
+ _OBJC_CLASS_$_PFDeviceTimeRectCollection
+ _OBJC_CLASS_$_PFImageIOOptionsBuilder
+ _OBJC_CLASS_$_PFImageMetadataChangePolicy
+ _OBJC_CLASS_$_PFImageMetadataChangePolicyAddPFMetadata
+ _OBJC_CLASS_$_PFImageMetadataChangePolicyComposite
+ _OBJC_CLASS_$_PFImageMetadataChangePolicyDefault
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySetAccessibilityDescription
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySetCaption
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySetCreationDate
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySetLocation
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySharedPhotoStream
+ _OBJC_CLASS_$_PFImageMetadataChangePolicyiCloudPhotoLibrary
+ _OBJC_CLASS_$_PFParallaxDataLayer
+ _OBJC_CLASS_$_PFParallaxMutableIntermediateLayout
+ _OBJC_CLASS_$_PFParallaxSpatialPhotoLayer
+ _OBJC_CLASS_$_PFParallaxSpatialPhotoOcclusionLayer
+ _OBJC_CLASS_$_PFPosterMediaURLImage
+ _OBJC_IVAR_$_PFCropUtilitiesPosterOutputData._adaptiveHeadroom
+ _OBJC_IVAR_$_PFCropUtilitiesPosterOutputData._adaptiveVisibleRect
+ _OBJC_IVAR_$_PFCropUtilitiesPosterOutputData._clockOverlapAcceptable
+ _OBJC_IVAR_$_PFCropUtilitiesPosterOutputData._cropScore
+ _OBJC_IVAR_$_PFCropUtilitiesPosterOutputData._headroomEngaged
+ _OBJC_IVAR_$_PFCropUtilitiesPosterOutputData._layoutScore
+ _OBJC_IVAR_$_PFCropUtilitiesPosterOutputData._layoutVariant
+ _OBJC_IVAR_$_PFCropUtilitiesPosterOutputData._maxClockShift
+ _OBJC_IVAR_$_PFCropUtilitiesPosterOutputData._notificationRoom
+ _OBJC_IVAR_$_PFCropUtilitiesPosterOutputData._visibleRect
+ _OBJC_IVAR_$_PFDeviceTimeRectCollection._screenScale
+ _OBJC_IVAR_$_PFDeviceTimeRectCollection._sortedTimeRects
+ _OBJC_IVAR_$_PFImageIOOptionsBuilder._applyTransform
+ _OBJC_IVAR_$_PFImageIOOptionsBuilder._colorBehavior
+ _OBJC_IVAR_$_PFImageIOOptionsBuilder._customOptions
+ _OBJC_IVAR_$_PFImageIOOptionsBuilder._includeDerivativeDefaults
+ _OBJC_IVAR_$_PFImageIOOptionsBuilder._includeHDRGainMaps
+ _OBJC_IVAR_$_PFImageIOOptionsBuilder._maximumLongSideLength
+ _OBJC_IVAR_$_PFImageIOOptionsBuilder._orientation
+ _OBJC_IVAR_$_PFImageIOOptionsBuilder._skipMetadata
+ _OBJC_IVAR_$_PFImageMetadataChangePolicyAddPFMetadata._key
+ _OBJC_IVAR_$_PFImageMetadataChangePolicyAddPFMetadata._value
+ _OBJC_IVAR_$_PFImageMetadataChangePolicyComposite._policies
+ _OBJC_IVAR_$_PFImageMetadataChangePolicyDefault._lossyCompressionQuality
+ _OBJC_IVAR_$_PFImageMetadataChangePolicySetAccessibilityDescription._accessibilityDescription
+ _OBJC_IVAR_$_PFImageMetadataChangePolicySetCaption._caption
+ _OBJC_IVAR_$_PFImageMetadataChangePolicySetCreationDate._creationDate
+ _OBJC_IVAR_$_PFImageMetadataChangePolicySetCreationDate._timeZone
+ _OBJC_IVAR_$_PFImageMetadataChangePolicySetLocation._location
+ _OBJC_IVAR_$_PFParallaxDataLayer._data
+ _OBJC_IVAR_$_PFParallaxIntermediateLayout._adaptiveInactiveTopRect
+ _OBJC_IVAR_$_PFParallaxIntermediateLayout._adaptiveStrategy
+ _OBJC_IVAR_$_PFParallaxIntermediateLayout._adaptiveVisibleRect
+ _OBJC_IVAR_$_PFParallaxIntermediateLayout._layoutVariant
+ _OBJC_IVAR_$_PFParallaxIntermediateLayout._maxClockShift
+ _OBJC_IVAR_$_PFParallaxIntermediateLayout._salientContentRect
+ _OBJC_IVAR_$_PFParallaxIntermediateLayout._spatialAdaptiveVisibleRect
+ _OBJC_IVAR_$_PFParallaxIntermediateLayout._spatialStrategy
+ _OBJC_IVAR_$_PFParallaxIntermediateLayout._spatialVisibleRect
+ _OBJC_IVAR_$_PFParallaxIntermediateLayout._zoomFactor
+ _OBJC_IVAR_$_PFParallaxLayerStack._spatialPhotoEnabled
+ _OBJC_IVAR_$_PFParallaxLayoutHelper._allowedClockStretch
+ _OBJC_IVAR_$_PFParallaxLayoutHelper._allowedLayoutStrategies
+ _OBJC_IVAR_$_PFParallaxLayoutHelper._computeSpatial
+ _OBJC_IVAR_$_PFParallaxLayoutHelper._spatialPadding
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.adaptiveInactiveTopRect
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.adaptiveStrategy
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.adaptiveVisibleRect
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.cropScore
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.hasTopEdgeContact
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.headroomStrategy
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.inactiveRect
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.inactiveStrategy
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.layoutScore
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.layoutVariant
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.maxClockShift
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.overlapStrategy
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.parallaxStrategy
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.salientContentRect
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.spatialAdaptiveVisibleRect
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.spatialStrategy
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.spatialVisibleRect
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.timeBottomOverlap
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.timeTopOverlap
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.uninflatedUnsafeAreaOverlap
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.unsafeAreaOverlap
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.visibleRect
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.zoomFactor
+ _OBJC_IVAR_$_PFParallaxMutableIntermediateLayout.zoomStrategy
+ _OBJC_IVAR_$_PFParallaxSpatialPhotoLayer._scene
+ _OBJC_IVAR_$_PFParallaxSpatialPhotoLayer._sceneData
+ _OBJC_IVAR_$_PFPosterConfiguration._allowedLayoutStrategies
+ _OBJC_IVAR_$_PFPosterConfiguration._photoLibraryIdentifier
+ _OBJC_IVAR_$_PFPosterDescriptor._photoLibraryIdentifier
+ _OBJC_IVAR_$_PFPosterEditConfiguration._additionalTitleLabelHeight
+ _OBJC_IVAR_$_PFPosterEditConfiguration._isSpatialPhotoAvailable
+ _OBJC_IVAR_$_PFPosterEditConfiguration._isSpatialPhotoEnabled
+ _OBJC_IVAR_$_PFPosterEditConfiguration._normalizedAdaptiveTimeFrame
+ _OBJC_IVAR_$_PFPosterEditConfiguration._normalizedAdaptiveVisibleFrame
+ _OBJC_IVAR_$_PFPosterEditConfiguration._normalizedLandscapeAdaptiveTimeFrame
+ _OBJC_IVAR_$_PFPosterEditConfiguration._normalizedLandscapeAdaptiveVisibleFrame
+ _OBJC_IVAR_$_PFPosterEditConfiguration._userAdjustedTitleLabelHeightOffset
+ _OBJC_IVAR_$_PFPosterMediaURLImage._imageURL
+ _OBJC_IVAR_$_PFPosterOrientedLayout._adaptiveInactiveTopFrame
+ _OBJC_IVAR_$_PFPosterOrientedLayout._adaptiveTimeFrame
+ _OBJC_IVAR_$_PFPosterOrientedLayout._adaptiveVisibleFrame
+ _OBJC_IVAR_$_PFPosterOrientedLayout._layoutVariant
+ _OBJC_IVAR_$_PFPosterOrientedLayout._maxClockShift
+ _OBJC_IVAR_$_PFPosterOrientedLayout._salientContentFrame
+ _OBJC_IVAR_$_PFPosterOrientedLayout._spatialAdaptiveFrame
+ _OBJC_IVAR_$_PFPosterOrientedLayout._spatialVisibleFrame
+ _OBJC_METACLASS_$_PFCropUtilitiesPosterOutputData
+ _OBJC_METACLASS_$_PFDeviceTimeRectCollection
+ _OBJC_METACLASS_$_PFImageIOOptionsBuilder
+ _OBJC_METACLASS_$_PFImageMetadataChangePolicy
+ _OBJC_METACLASS_$_PFImageMetadataChangePolicyAddPFMetadata
+ _OBJC_METACLASS_$_PFImageMetadataChangePolicyComposite
+ _OBJC_METACLASS_$_PFImageMetadataChangePolicyDefault
+ _OBJC_METACLASS_$_PFImageMetadataChangePolicySetAccessibilityDescription
+ _OBJC_METACLASS_$_PFImageMetadataChangePolicySetCaption
+ _OBJC_METACLASS_$_PFImageMetadataChangePolicySetCreationDate
+ _OBJC_METACLASS_$_PFImageMetadataChangePolicySetLocation
+ _OBJC_METACLASS_$_PFImageMetadataChangePolicySharedPhotoStream
+ _OBJC_METACLASS_$_PFImageMetadataChangePolicyiCloudPhotoLibrary
+ _OBJC_METACLASS_$_PFParallaxDataLayer
+ _OBJC_METACLASS_$_PFParallaxMutableIntermediateLayout
+ _OBJC_METACLASS_$_PFParallaxSpatialPhotoLayer
+ _OBJC_METACLASS_$_PFParallaxSpatialPhotoOcclusionLayer
+ _OBJC_METACLASS_$_PFPosterMediaURLImage
+ _PFClientSideEncryptionManagerOptionCompressionKey
+ _PFDeviceLockScreenTimeRectCollectionNormalized_SBS
+ _PFParallaxLayerIDIsAnySpatialPhoto
+ _PFParallaxLayerIDIsSpatialPhotoBackground
+ _PFParallaxLayerIDIsSpatialPhotoForeground
+ _PFParallaxLayerIDIsSpatialPhotoInactiveData
+ _PFParallaxLayerID_SpatialPhotoBackground
+ _PFParallaxLayerID_SpatialPhotoForeground
+ _PFParallaxLayerID_SpatialPhotoInactiveData
+ _PFParallaxStyleCategoryOriginal
+ _PFPosterDeviceSpatialPhotoSupportLevel
+ _PFPosterDeviceSpatialPhotoSupportLevel.onceToken
+ _PFPosterDeviceSpatialPhotoSupportLevel.supportLevel
+ _PFPosterDeviceSupportsSpatialPhoto
+ _PFPosterDeviceSupportsSpatialPhotoWidgetOptimizations
+ _PFPosterDeviceSupportsSpatialPhotoWidgetOptimizations.onceToken
+ _PFPosterDeviceSupportsSpatialPhotoWidgetOptimizations.supported
+ _PFPosterIsAdaptiveLayoutEnabled
+ _PFPosterIsLayoutVariantAdaptive
+ _PFPosterIsPortraitHeadroomEnabled
+ _PFPosterIsRunningInVirtualMachine.isVirtualDevice
+ _PFPosterIsRunningInVirtualMachine.onceToken
+ _PFPosterIsSpatialPhotoEnabled
+ _PFPosterIsSpatialPhotoEnabled.forceDisable
+ _PFPosterIsSpatialPhotoEnabled.onceToken
+ _PFPosterIsSpatialPhotoOcclusionEnabled
+ _PFPosterIsSpatialPhotoOcclusionEnabled.forceDisable
+ _PFPosterIsSpatialPhotoOcclusionEnabled.onceToken
+ _PFPosterScoreKeySpatialPhotoGatingFailures
+ _PFPosterScoreKeySpatialPhotoLayout
+ _PFPosterSpatialPhotoGatingLevelDescription
+ _PFUIGetLog
+ _SpringBoardServicesLibrary
+ _UTTypeDNG
+ _Vertices.11665
+ __AuxiliaryImageCVPixelBufferReleaseBytesCallback.3570
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSValue_$_NSValuePFWallpaperExtensions
+ __OBJC_$_CATEGORY_NSValue_$_NSValuePFWallpaperExtensions
+ __OBJC_$_CLASS_METHODS_PFClientSideEncryptionManager
+ __OBJC_$_CLASS_METHODS_PFImageMetadataChangePolicy
+ __OBJC_$_CLASS_METHODS_PFImageMetadataChangePolicyAddPFMetadata
+ __OBJC_$_CLASS_METHODS_PFImageMetadataChangePolicyComposite
+ __OBJC_$_CLASS_METHODS_PFImageMetadataChangePolicyDefault
+ __OBJC_$_CLASS_METHODS_PFImageMetadataChangePolicySetAccessibilityDescription
+ __OBJC_$_CLASS_METHODS_PFImageMetadataChangePolicySetCaption
+ __OBJC_$_CLASS_METHODS_PFImageMetadataChangePolicySetCreationDate
+ __OBJC_$_CLASS_METHODS_PFImageMetadataChangePolicySetLocation
+ __OBJC_$_CLASS_METHODS_PFImageMetadataChangePolicySharedPhotoStream
+ __OBJC_$_CLASS_METHODS_PFImageMetadataChangePolicyiCloudPhotoLibrary
+ __OBJC_$_CLASS_METHODS_PFParallaxDataLayer(Archiver)
+ __OBJC_$_CLASS_METHODS_PFParallaxSpatialPhotoLayer(Archiver)
+ __OBJC_$_CLASS_METHODS_PFParallaxSpatialPhotoOcclusionLayer(Archiver)
+ __OBJC_$_CLASS_METHODS_PFPosterMediaURLImage
+ __OBJC_$_CLASS_PROP_LIST_PFImageMetadataChangePolicy
+ __OBJC_$_CLASS_PROP_LIST_PFParallaxLayoutUtilities
+ __OBJC_$_INSTANCE_METHODS_PFCropUtilitiesPosterOutputData
+ __OBJC_$_INSTANCE_METHODS_PFDeviceTimeRectCollection
+ __OBJC_$_INSTANCE_METHODS_PFImageIOOptionsBuilder
+ __OBJC_$_INSTANCE_METHODS_PFImageMetadataChangePolicy
+ __OBJC_$_INSTANCE_METHODS_PFImageMetadataChangePolicyAddPFMetadata
+ __OBJC_$_INSTANCE_METHODS_PFImageMetadataChangePolicyComposite
+ __OBJC_$_INSTANCE_METHODS_PFImageMetadataChangePolicyDefault
+ __OBJC_$_INSTANCE_METHODS_PFImageMetadataChangePolicySetAccessibilityDescription
+ __OBJC_$_INSTANCE_METHODS_PFImageMetadataChangePolicySetCaption
+ __OBJC_$_INSTANCE_METHODS_PFImageMetadataChangePolicySetCreationDate
+ __OBJC_$_INSTANCE_METHODS_PFImageMetadataChangePolicySetLocation
+ __OBJC_$_INSTANCE_METHODS_PFImageMetadataChangePolicySharedPhotoStream
+ __OBJC_$_INSTANCE_METHODS_PFImageMetadataChangePolicyiCloudPhotoLibrary
+ __OBJC_$_INSTANCE_METHODS_PFParallaxDataLayer(Archiver)
+ __OBJC_$_INSTANCE_METHODS_PFParallaxMutableIntermediateLayout
+ __OBJC_$_INSTANCE_METHODS_PFParallaxSpatialPhotoLayer(Archiver)
+ __OBJC_$_INSTANCE_METHODS_PFParallaxSpatialPhotoOcclusionLayer(Archiver)
+ __OBJC_$_INSTANCE_METHODS_PFPosterMediaURLImage
+ __OBJC_$_INSTANCE_VARIABLES_PFCropUtilitiesPosterOutputData
+ __OBJC_$_INSTANCE_VARIABLES_PFDeviceTimeRectCollection
+ __OBJC_$_INSTANCE_VARIABLES_PFImageIOOptionsBuilder
+ __OBJC_$_INSTANCE_VARIABLES_PFImageMetadataChangePolicyAddPFMetadata
+ __OBJC_$_INSTANCE_VARIABLES_PFImageMetadataChangePolicyComposite
+ __OBJC_$_INSTANCE_VARIABLES_PFImageMetadataChangePolicyDefault
+ __OBJC_$_INSTANCE_VARIABLES_PFImageMetadataChangePolicySetAccessibilityDescription
+ __OBJC_$_INSTANCE_VARIABLES_PFImageMetadataChangePolicySetCaption
+ __OBJC_$_INSTANCE_VARIABLES_PFImageMetadataChangePolicySetCreationDate
+ __OBJC_$_INSTANCE_VARIABLES_PFImageMetadataChangePolicySetLocation
+ __OBJC_$_INSTANCE_VARIABLES_PFParallaxDataLayer
+ __OBJC_$_INSTANCE_VARIABLES_PFParallaxMutableIntermediateLayout
+ __OBJC_$_INSTANCE_VARIABLES_PFParallaxSpatialPhotoLayer
+ __OBJC_$_INSTANCE_VARIABLES_PFPosterMediaURLImage
+ __OBJC_$_PROP_LIST_PFCropUtilitiesPosterOutputData
+ __OBJC_$_PROP_LIST_PFDeviceTimeRectCollection
+ __OBJC_$_PROP_LIST_PFImageIOOptionsBuilder
+ __OBJC_$_PROP_LIST_PFImageMetadataChangePolicyAddPFMetadata
+ __OBJC_$_PROP_LIST_PFImageMetadataChangePolicyComposite
+ __OBJC_$_PROP_LIST_PFImageMetadataChangePolicyDefault
+ __OBJC_$_PROP_LIST_PFImageMetadataChangePolicySetAccessibilityDescription
+ __OBJC_$_PROP_LIST_PFImageMetadataChangePolicySetCaption
+ __OBJC_$_PROP_LIST_PFImageMetadataChangePolicySetCreationDate
+ __OBJC_$_PROP_LIST_PFImageMetadataChangePolicySetLocation
+ __OBJC_$_PROP_LIST_PFMetadataImage.6298
+ __OBJC_$_PROP_LIST_PFParallaxDataLayer
+ __OBJC_$_PROP_LIST_PFParallaxMutableIntermediateLayout
+ __OBJC_$_PROP_LIST_PFParallaxSpatialPhotoLayer
+ __OBJC_$_PROP_LIST_PFPosterMediaURLImage
+ __OBJC_CLASS_PROTOCOLS_$_PFImageMetadataChangePolicy
+ __OBJC_CLASS_PROTOCOLS_$_PFParallaxIntermediateLayout
+ __OBJC_CLASS_RO_$_PFCropUtilitiesPosterOutputData
+ __OBJC_CLASS_RO_$_PFDeviceTimeRectCollection
+ __OBJC_CLASS_RO_$_PFImageIOOptionsBuilder
+ __OBJC_CLASS_RO_$_PFImageMetadataChangePolicy
+ __OBJC_CLASS_RO_$_PFImageMetadataChangePolicyAddPFMetadata
+ __OBJC_CLASS_RO_$_PFImageMetadataChangePolicyComposite
+ __OBJC_CLASS_RO_$_PFImageMetadataChangePolicyDefault
+ __OBJC_CLASS_RO_$_PFImageMetadataChangePolicySetAccessibilityDescription
+ __OBJC_CLASS_RO_$_PFImageMetadataChangePolicySetCaption
+ __OBJC_CLASS_RO_$_PFImageMetadataChangePolicySetCreationDate
+ __OBJC_CLASS_RO_$_PFImageMetadataChangePolicySetLocation
+ __OBJC_CLASS_RO_$_PFImageMetadataChangePolicySharedPhotoStream
+ __OBJC_CLASS_RO_$_PFImageMetadataChangePolicyiCloudPhotoLibrary
+ __OBJC_CLASS_RO_$_PFParallaxDataLayer
+ __OBJC_CLASS_RO_$_PFParallaxMutableIntermediateLayout
+ __OBJC_CLASS_RO_$_PFParallaxSpatialPhotoLayer
+ __OBJC_CLASS_RO_$_PFParallaxSpatialPhotoOcclusionLayer
+ __OBJC_CLASS_RO_$_PFPosterMediaURLImage
+ __OBJC_METACLASS_RO_$_PFCropUtilitiesPosterOutputData
+ __OBJC_METACLASS_RO_$_PFDeviceTimeRectCollection
+ __OBJC_METACLASS_RO_$_PFImageIOOptionsBuilder
+ __OBJC_METACLASS_RO_$_PFImageMetadataChangePolicy
+ __OBJC_METACLASS_RO_$_PFImageMetadataChangePolicyAddPFMetadata
+ __OBJC_METACLASS_RO_$_PFImageMetadataChangePolicyComposite
+ __OBJC_METACLASS_RO_$_PFImageMetadataChangePolicyDefault
+ __OBJC_METACLASS_RO_$_PFImageMetadataChangePolicySetAccessibilityDescription
+ __OBJC_METACLASS_RO_$_PFImageMetadataChangePolicySetCaption
+ __OBJC_METACLASS_RO_$_PFImageMetadataChangePolicySetCreationDate
+ __OBJC_METACLASS_RO_$_PFImageMetadataChangePolicySetLocation
+ __OBJC_METACLASS_RO_$_PFImageMetadataChangePolicySharedPhotoStream
+ __OBJC_METACLASS_RO_$_PFImageMetadataChangePolicyiCloudPhotoLibrary
+ __OBJC_METACLASS_RO_$_PFParallaxDataLayer
+ __OBJC_METACLASS_RO_$_PFParallaxMutableIntermediateLayout
+ __OBJC_METACLASS_RO_$_PFParallaxSpatialPhotoLayer
+ __OBJC_METACLASS_RO_$_PFParallaxSpatialPhotoOcclusionLayer
+ __OBJC_METACLASS_RO_$_PFPosterMediaURLImage
+ __ZN2pf18SceneGeographyNodeD2Ev
+ __ZN5boost12interprocess10iset_indexINS0_9ipcdetail12index_configIcNS0_15rbtree_best_fitINS0_17null_mutex_familyENS0_10offset_ptrIvlmLm0EEELm0EEEEEEC1EPNS0_20segment_manager_baseIS8_EE
+ __ZN5boost12interprocess25basic_managed_mapped_fileIcNS0_15rbtree_best_fitINS0_17null_mutex_familyENS0_10offset_ptrIvlmLm0EEELm0EEENS0_10iset_indexEED1Ev
+ __ZN5boost12interprocessL8ec_tableE.8210
+ __ZN5boost8geometry5index6detail5rtree8visitors14distance_queryINS1_5rtreeINSt3__14pairINS0_5model5pointIfLm2ENS0_2cs9cartesianEEEtEENS1_9quadraticILm32ELm8EEENS1_9indexableISE_EENS1_8equal_toISE_EENS_12interprocess9allocatorISE_NSL_15segment_managerIcNSL_15rbtree_best_fitINSL_17null_mutex_familyENSL_10offset_ptrIvlmLm0EEELm0EEENSL_10iset_indexEEEEEE14members_holderENS2_10predicates7nearestISD_EEED2Ev
+ __ZN5boost9container12basic_stringIcNSt3__111char_traitsIcEENS_12interprocess9allocatorIcNS5_15segment_managerIcNS5_15rbtree_best_fitINS5_17null_mutex_familyENS5_10offset_ptrIvlmLm0EEELm0EEENS5_10iset_indexEEEEEED1Ev
+ __ZN5boost9container6vectorIjNS_12interprocess9allocatorIjNS2_15segment_managerIcNS2_15rbtree_best_fitINS2_17null_mutex_familyENS2_10offset_ptrIvlmLm0EEELm0EEENS2_10iset_indexEEEEEvED1Ev
+ __ZN5boost9intrusiveeqERKNS0_13tree_iteratorINS0_8bhtraitsINS_12interprocess15rbtree_best_fitINS3_17null_mutex_familyENS3_10offset_ptrIvlmLm0EEELm0EE10block_ctrlENS0_18rbtree_node_traitsIS7_Lb1EEELNS0_14link_mode_typeE0ENS0_7dft_tagELj3EEELb0EEESH_
+ __ZN5boost9unordered13unordered_mapINS_9container12basic_stringIcNSt3__111char_traitsIcEENS_12interprocess9allocatorIcNS7_15segment_managerIcNS7_15rbtree_best_fitINS7_17null_mutex_familyENS7_10offset_ptrIvlmLm0EEELm0EEENS7_10iset_indexEEEEEEEN2pf17SceneTaxonomyNodeENS_4hashISI_EENS4_8equal_toISI_EENS8_INS4_4pairIKSI_SK_EESG_EEE4findERSQ_
+ __ZNK5boost9unordered6detail5tableINS1_3mapINS_12interprocess9allocatorIN2pf18SceneGeographyNodeENS4_15segment_managerIcNS4_15rbtree_best_fitINS4_17null_mutex_familyENS4_10offset_ptrIvlmLm0EEELm0EEENS4_10iset_indexEEEEENS_9container12basic_stringIcNSt3__111char_traitsIcEENS5_IcSF_EEEES7_NS_4hashISN_EENSJ_8equal_toISN_EEEEE4hashERKSN_
+ __ZNK5boost9unordered6detail5tableINS1_3mapINS_12interprocess9allocatorINSt3__14pairIKNS_9container12basic_stringIcNS6_11char_traitsIcEENS5_IcNS4_15segment_managerIcNS4_15rbtree_best_fitINS4_17null_mutex_familyENS4_10offset_ptrIvlmLm0EEELm0EEENS4_10iset_indexEEEEEEEN2pf17SceneTaxonomyNodeEEESJ_EESL_SO_NS_4hashISL_EENS6_8equal_toISL_EEEEE4hashERSM_
+ __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ne200100ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne200100ERKS6_S9_
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__110unique_ptrIN5boost12interprocess25basic_managed_mapped_fileIcNS2_15rbtree_best_fitINS2_17null_mutex_familyENS2_10offset_ptrIvlmLm0EEELm0EEENS2_10iset_indexEEENS_14default_deleteISA_EEED1B8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc
+ __ZNSt3__114__split_bufferIPPKvNS_9allocatorIS3_EEE12emplace_backIJRS3_EEEvDpOT_
+ __ZNSt3__116allocator_traitsIN5boost12interprocess9allocatorINS1_9unordered6detail4nodeINS3_IN2pf18SceneGeographyNodeENS2_15segment_managerIcNS2_15rbtree_best_fitINS2_17null_mutex_familyENS2_10offset_ptrIvlmLm0EEELm0EEENS2_10iset_indexEEEEENS_4pairIKNS1_9container12basic_stringIcNS_11char_traitsIcEENS3_IcSG_EEEES8_EEEESG_EEE10deallocateB8ne200100ERSS_NSC_ISR_lmLm0EEEm
+ __ZNSt3__116allocator_traitsIN5boost12interprocess9allocatorINS1_9unordered6detail4nodeINS3_INS2_10offset_ptrIN2pf17SceneTaxonomyNodeElmLm0EEENS2_15segment_managerIcNS2_15rbtree_best_fitINS2_17null_mutex_familyENS7_IvlmLm0EEELm0EEENS2_10iset_indexEEEEESA_EESH_EEE10deallocateB8ne200100ERSK_NS7_ISJ_lmLm0EEEm
+ __ZNSt3__116allocator_traitsIN5boost12interprocess9allocatorINS1_9unordered6detail4nodeINS3_INS_4pairIKNS1_9container12basic_stringIcNS_11char_traitsIcEENS3_IcNS2_15segment_managerIcNS2_15rbtree_best_fitINS2_17null_mutex_familyENS2_10offset_ptrIvlmLm0EEELm0EEENS2_10iset_indexEEEEEEEN2pf17SceneTaxonomyNodeEEESJ_EESP_EESJ_EEE10deallocateB8ne200100ERSS_NSF_ISR_lmLm0EEEm
+ __ZNSt3__116allocator_traitsIN5boost12interprocess9allocatorINS1_9unordered6detail4nodeINS3_INS_4pairIKyNS2_10offset_ptrIN2pf17SceneTaxonomyNodeElmLm0EEEEENS2_15segment_managerIcNS2_15rbtree_best_fitINS2_17null_mutex_familyENS9_IvlmLm0EEELm0EEENS2_10iset_indexEEEEESD_EESK_EEE10deallocateB8ne200100ERSN_NS9_ISM_lmLm0EEEm
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorINS_4pairIN5boost8geometry5model5pointIfLm2ENS4_2cs9cartesianEEEtEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorINS_4pairIdPKNS2_IN5boost8geometry5model5pointIfLm2ENS4_2cs9cartesianEEEtEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSH_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPKN2pf17SceneTaxonomyNodeEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEtEEPvEEEEEclB8ne200100EPSB_
+ __ZNSt3__15dequeIPKvNS_9allocatorIS2_EEED2B8ne200100Ev
+ __ZNSt3__16vectorIN5boost8geometry5index6detail5rtree8visitors14distance_queryINS3_5rtreeINS_4pairINS2_5model5pointIfLm2ENS2_2cs9cartesianEEEtEENS3_9quadraticILm32ELm8EEENS3_9indexableISF_EENS3_8equal_toISF_EENS1_12interprocess9allocatorISF_NSM_15segment_managerIcNSM_15rbtree_best_fitINSM_17null_mutex_familyENSM_10offset_ptrIvlmLm0EEELm0EEENSM_10iset_indexEEEEEE14members_holderENS4_10predicates7nearestISE_EEE11branch_dataENS_9allocatorIS13_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIN5boost8geometry5model5pointIfLm2ENS3_2cs9cartesianEEEtEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIPKN5boost8geometry5index6detail5rtree8ptr_pairINS3_5model3boxINS8_5pointIfLm2ENS3_2cs9cartesianEEEEENS2_12interprocess10offset_ptrINS2_7variantINS6_12variant_leafINS1_ISD_tEENS4_9quadraticILm32ELm8EEESE_NS6_10allocatorsINSF_9allocatorISJ_NSF_15segment_managerIcNSF_15rbtree_best_fitINSF_17null_mutex_familyENSG_IvlmLm0EEELm0EEENSF_10iset_indexEEEEESJ_SL_SE_NS6_23node_variant_static_tagEEESW_EEJNS6_21variant_internal_nodeISJ_SL_SE_SX_SW_EEEEElmLm0EEEEES15_EENS_9allocatorIS16_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIdPKNS1_IN5boost8geometry5model5pointIfLm2ENS3_2cs9cartesianEEEtEEEENS_9allocatorISC_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPKN2pf17SceneTaxonomyNodeENS_9allocatorIS4_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPKN2pf17SceneTaxonomyNodeENS_9allocatorIS4_EEE7reserveEm
+ __ZNSt3__16vectorIPKN2pf17SceneTaxonomyNodeENS_9allocatorIS4_EEE9push_backB8ne200100EOS4_
+ __ZNSt3__17__sort3B8ne200100INS_17_ClassicAlgPolicyERN5boost8geometry5index6detail5rtree10pack_utils22point_entries_comparerILm0EEENS2_9container12vec_iteratorIPNS_4pairINS3_5model5pointIfLm2ENS3_2cs9cartesianEEENS_11__wrap_iterIPNSD_ISI_tEEEEEELb0EEELi0EEEbT1_SQ_SQ_T0_
+ __ZNSt3__17__sort3B8ne200100INS_17_ClassicAlgPolicyERN5boost8geometry5index6detail5rtree10pack_utils22point_entries_comparerILm1EEENS2_9container12vec_iteratorIPNS_4pairINS3_5model5pointIfLm2ENS3_2cs9cartesianEEENS_11__wrap_iterIPNSD_ISI_tEEEEEELb0EEELi0EEEbT1_SQ_SQ_T0_
+ __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB8ne200100IRN5boost9container12vec_iteratorIPNS_4pairINS4_8geometry5model5pointIfLm2ENS8_2cs9cartesianEEENS_11__wrap_iterIPNS7_ISD_tEEEEEELb0EEESL_EEvOT_OT0_
+ __ZNSt3__19__sift_upB8ne200100INS_17_ClassicAlgPolicyERN5boost8geometry5index6detail5rtree8visitors15pair_first_lessENS_11__wrap_iterIPNS_4pairIdPKNSB_INS3_5model5pointIfLm2ENS3_2cs9cartesianEEEtEEEEEEEEvT1_SN_OT0_NS_15iterator_traitsISN_E15difference_typeE
+ __ZNSt3__19__sift_upB8ne200100INS_17_ClassicAlgPolicyERN5boost8geometry5index6detail5rtree8visitors16branch_data_compENS_11__wrap_iterIPNS7_14distance_queryINS4_5rtreeINS_4pairINS3_5model5pointIfLm2ENS3_2cs9cartesianEEEtEENS4_9quadraticILm32ELm8EEENS4_9indexableISJ_EENS4_8equal_toISJ_EENS2_12interprocess9allocatorISJ_NSQ_15segment_managerIcNSQ_15rbtree_best_fitINSQ_17null_mutex_familyENSQ_10offset_ptrIvlmLm0EEELm0EEENSQ_10iset_indexEEEEEE14members_holderENS5_10predicates7nearestISI_EEE11branch_dataEEEEEvT1_S1A_OT0_NS_15iterator_traitsIS1A_E15difference_typeE
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ ___264-[PFParallaxIntermediateLayout initWithVisibleRect:inactiveRect:zoomStrategy:overlapStrategy:parallaxStrategy:inactiveStrategy:headroomStrategy:cropScore:layoutScore:timeBottomOverlap:timeTopOverlap:unsafeAreaOverlap:uninflatedUnsafeAreaOverlap:hasTopEdgeContact:]_block_invoke
+ ___37-[PFParallaxLayoutHelper bestLayout:]_block_invoke
+ ___39-[PFMetadataMovie cinematicVideoIntent]_block_invoke
+ ___44-[PFParallaxLayoutHelper scoreIntermediate:]_block_invoke
+ ___45+[PFImageMetadataChangePolicy standardPolicy]_block_invoke
+ ___52+[PFImageMetadataChangePolicyDefault standardPolicy]_block_invoke
+ ___54+[PFParallaxLayoutUtilities computeLayoutsWithHelper:]_block_invoke.409
+ ___61-[PFDeviceTimeRectCollection nearestRectForPointSpaceHeight:]_block_invoke
+ ___61-[PFParallaxLayoutConfiguration timeRectForNormalizedHeight:]_block_invoke
+ ___62-[PFImageMetadataChangePolicySetCreationDate processMetadata:]_block_invoke
+ ___63+[PFImageMetadataChangePolicyiCloudPhotoLibrary standardPolicy]_block_invoke
+ ___68-[PFParallaxLayoutHelper intermediateWithZoomStrategy:intermediate:]_block_invoke
+ ___70+[PFParallaxLayoutConfiguration _loadDeviceTimeRectCollectionIfNeeded]_block_invoke
+ ___70-[PFImageMetadataChangePolicySetCreationDate metadataNeedsProcessing:]_block_invoke
+ ___71-[PFParallaxLayoutHelper intermediateWithOverlapStrategy:intermediate:]_block_invoke
+ ___71-[PFParallaxLayoutHelper intermediateWithSpatialStrategy:intermediate:]_block_invoke
+ ___71-[PFParallaxLayoutHelper intermediateWithSpatialStrategy:intermediate:]_block_invoke_2
+ ___72-[PFParallaxLayoutHelper intermediateWithAdaptiveStrategy:intermediate:]_block_invoke
+ ___72-[PFParallaxLayoutHelper intermediateWithAdaptiveStrategy:intermediate:]_block_invoke_2
+ ___72-[PFParallaxLayoutHelper intermediateWithHeadroomStrategy:intermediate:]_block_invoke
+ ___72-[PFParallaxLayoutHelper intermediateWithInactiveStrategy:intermediate:]_block_invoke
+ ___72-[PFParallaxLayoutHelper intermediateWithParallaxStrategy:intermediate:]_block_invoke
+ ___Block_byref_object_copy_.11380
+ ___Block_byref_object_copy_.12078
+ ___Block_byref_object_copy_.13395
+ ___Block_byref_object_copy_.4127
+ ___Block_byref_object_copy_.4593
+ ___Block_byref_object_copy_.4954
+ ___Block_byref_object_copy_.5106
+ ___Block_byref_object_copy_.5214
+ ___Block_byref_object_copy_.5856
+ ___Block_byref_object_copy_.6562
+ ___Block_byref_object_copy_.7604
+ ___Block_byref_object_copy_.8632
+ ___Block_byref_object_copy_.9144
+ ___Block_byref_object_copy_.9474
+ ___Block_byref_object_copy_.9888
+ ___Block_byref_object_dispose_.11381
+ ___Block_byref_object_dispose_.12079
+ ___Block_byref_object_dispose_.13396
+ ___Block_byref_object_dispose_.4128
+ ___Block_byref_object_dispose_.4594
+ ___Block_byref_object_dispose_.4955
+ ___Block_byref_object_dispose_.5107
+ ___Block_byref_object_dispose_.5215
+ ___Block_byref_object_dispose_.5857
+ ___Block_byref_object_dispose_.6563
+ ___Block_byref_object_dispose_.7605
+ ___Block_byref_object_dispose_.8633
+ ___Block_byref_object_dispose_.9145
+ ___Block_byref_object_dispose_.9475
+ ___Block_byref_object_dispose_.9889
+ ___PFDeviceLockScreenTimeRectCollectionNormalized_SBS_block_invoke
+ ___PFDeviceLockScreenTimeRectCollectionNormalized_SBS_block_invoke.9
+ ___PFDeviceLockScreenTimeRectCollectionNormalized_SBS_block_invoke_2
+ ___PFPosterDeviceSpatialPhotoSupportLevel_block_invoke
+ ___PFPosterDeviceSupportsSpatialPhotoWidgetOptimizations_block_invoke
+ ___PFPosterIsRunningInVirtualMachine_block_invoke
+ ___PFPosterIsSpatialPhotoEnabled_block_invoke
+ ___PFPosterIsSpatialPhotoOcclusionEnabled_block_invoke
+ ___block_descriptor_168_e45_v16?0"PFParallaxMutableIntermediateLayout"8l
+ ___block_descriptor_185_e45_v16?0"PFParallaxMutableIntermediateLayout"8l
+ ___block_descriptor_192_e8_32s_e45_v16?0"PFParallaxMutableIntermediateLayout"8ls32l8
+ ___block_descriptor_32_e29_q24?0"NSValue"8"NSValue"16l
+ ___block_descriptor_40_e45_v16?0"PFParallaxMutableIntermediateLayout"8l
+ ___block_descriptor_40_e8_32s_e45_v16?0"PFParallaxMutableIntermediateLayout"8ls32l8
+ ___block_descriptor_64_e8_32s40s48s56r_e11_v24?0d8d16ls32l8s40l8s48l8r56l8
+ ___block_descriptor_72_e45_v16?0"PFParallaxMutableIntermediateLayout"8l
+ ___block_descriptor_80_e45_v16?0"PFParallaxMutableIntermediateLayout"8l
+ ___block_descriptor_80_e8_32s_e45_v16?0"PFParallaxMutableIntermediateLayout"8ls32l8
+ ___block_descriptor_96_e8_32s40s_e45_v16?0"PFParallaxMutableIntermediateLayout"8ls32l8s40l8
+ ___block_literal_global.10003
+ ___block_literal_global.11
+ ___block_literal_global.111
+ ___block_literal_global.11374
+ ___block_literal_global.1144
+ ___block_literal_global.11607
+ ___block_literal_global.11711
+ ___block_literal_global.12.4957
+ ___block_literal_global.12.5866
+ ___block_literal_global.12075
+ ___block_literal_global.123.9134
+ ___block_literal_global.12333
+ ___block_literal_global.12494
+ ___block_literal_global.128.9577
+ ___block_literal_global.12909
+ ___block_literal_global.13
+ ___block_literal_global.13079
+ ___block_literal_global.13211
+ ___block_literal_global.1326
+ ___block_literal_global.147.5598
+ ___block_literal_global.1503
+ ___block_literal_global.152.5595
+ ___block_literal_global.154
+ ___block_literal_global.162.10851
+ ___block_literal_global.182
+ ___block_literal_global.1915
+ ___block_literal_global.195.2075
+ ___block_literal_global.2.4935
+ ___block_literal_global.20
+ ___block_literal_global.2172
+ ___block_literal_global.22.4310
+ ___block_literal_global.2397
+ ___block_literal_global.245
+ ___block_literal_global.263
+ ___block_literal_global.287
+ ___block_literal_global.2881
+ ___block_literal_global.30
+ ___block_literal_global.3267
+ ___block_literal_global.3421
+ ___block_literal_global.3725
+ ___block_literal_global.3990
+ ___block_literal_global.41
+ ___block_literal_global.4219
+ ___block_literal_global.4279
+ ___block_literal_global.4296
+ ___block_literal_global.44
+ ___block_literal_global.46
+ ___block_literal_global.4777
+ ___block_literal_global.4933
+ ___block_literal_global.5158
+ ___block_literal_global.5239
+ ___block_literal_global.5788
+ ___block_literal_global.5848
+ ___block_literal_global.6615
+ ___block_literal_global.6675
+ ___block_literal_global.68
+ ___block_literal_global.69.10662
+ ___block_literal_global.7311
+ ___block_literal_global.7458
+ ___block_literal_global.82.3712
+ ___block_literal_global.8343
+ ___block_literal_global.9
+ ___block_literal_global.9195
+ ___block_literal_global.9633
+ ___block_literal_global.97.9151
+ ___getSBSAdaptiveTimeLayoutContextClass_block_invoke
+ __exifDateTimeFormatter.dateTimeFormatter.5789
+ __exifDateTimeFormatter.onceToken.5787
+ __exifSubsecTimeFormatter.onceToken.5774
+ __exifSubsecTimeFormatter.subsecTimeFormatter.5775
+ __gpsDateFormatter.dateFormatter.5814
+ __gpsDateFormatter.onceToken.5813
+ __gpsTimeFormatter.onceToken.5818
+ __gpsTimeFormatter.timeFormatter.5819
+ __loadDeviceTimeRectCollectionIfNeeded.onceToken
+ _getSBSAdaptiveTimeLayoutContextClass.softClass
+ _kCGImageDestinationCreateHDRGainMap
+ _kCGImageDestinationImageMaxPixelSize
+ _kCGImageDestinationLossyCompressionQuality
+ _kCGImageDestinationPreserveGainMap
+ _kCGImagePropertyHasAlpha
+ _kCGImagePropertyIPTCImageOrientation
+ _kCGImagePropertyMakerFujiDictionary
+ _kCGImagePropertyMakerMinoltaDictionary
+ _kCGImagePropertyMakerOlympusDictionary
+ _kCGImagePropertyMakerPentaxDictionary
+ _kCGImagePropertyTIFFCopyright
+ _kCGImageSourceCreateThumbnailWithTransform
+ _kCGImageSourceDecodeRequest
+ _kCGImageSourceDecodeToSDR
+ _kCGImageSourceSkipMetadata
+ _objc_msgSend$_fallbackTimeRectCollectionForSBSFetchingFailureWithOrientation:
+ _objc_msgSend$_filterImageProperties:metadataWithKey:preserveProperties:
+ _objc_msgSend$_loadDeviceTimeRectCollectionIfNeeded
+ _objc_msgSend$_timeRectInImageSpaceFromPointSpaceRect:screenScale:
+ _objc_msgSend$adaptiveFrameForVisibleFrame:essentialRect:originalImageSize:layoutConfiguration:classification:maxClockStretchOverride:
+ _objc_msgSend$adaptiveHeadroom
+ _objc_msgSend$adaptiveInactiveTopFrame
+ _objc_msgSend$adaptiveInactiveTopRect
+ _objc_msgSend$adaptiveLayoutVerticalPriorityThreshold
+ _objc_msgSend$adaptiveStrategy
+ _objc_msgSend$adaptiveTimeFrame
+ _objc_msgSend$adaptiveVisibleFrame
+ _objc_msgSend$adaptiveVisibleRect
+ _objc_msgSend$addMakerApplePropertyWithKey:value:toProperties:
+ _objc_msgSend$additionalTitleLabelHeight
+ _objc_msgSend$allowedClockStretch
+ _objc_msgSend$allowedLayoutStrategies
+ _objc_msgSend$applyOptions:toArchive:
+ _objc_msgSend$archiveFileAtURL:outputFileURL:options:error:
+ _objc_msgSend$arrayWithObjects:
+ _objc_msgSend$bestAdaptiveCropRectForPosterClassification:layoutConfiguration:sourcePixelWidth:sourcePixelHeight:sourcePreferredCropRectNormalized:sourceAcceptableCropRectNormalized:sourceFaceAreaRectNormalized:
+ _objc_msgSend$bestAdaptiveCropRectForPosterClassification:layoutConfiguration:sourcePixelWidth:sourcePixelHeight:sourcePreferredCropRectNormalized:sourceAcceptableCropRectNormalized:sourceFaceAreaRectNormalized:headroomFeasible:
+ _objc_msgSend$cinematicVideoIntent
+ _objc_msgSend$clockOverlapAcceptable
+ _objc_msgSend$closeupZoomPercentWithLayoutType:
+ _objc_msgSend$computeSpatial
+ _objc_msgSend$computeSpatialFrameForVisibleRect:adaptiveVisibleRect:spatialPaddingPercentage:effectiveImageRect:
+ _objc_msgSend$dataRepresentation
+ _objc_msgSend$decodeFloatForKey:
+ _objc_msgSend$encodeFloat:forKey:
+ _objc_msgSend$exifDictionary
+ _objc_msgSend$fetchAdaptiveTimeBoundsForContext:timeHeight:completionHandler:
+ _objc_msgSend$fetchAdaptiveTimeHeightLimitsForContext:completionHandler:
+ _objc_msgSend$genericPadConfiguration
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithConfiguration:
+ _objc_msgSend$initWithConfigurationType:photoLibraryIdentifier:
+ _objc_msgSend$initWithData:frame:zPosition:identifier:
+ _objc_msgSend$initWithDescriptorType:media:photoLibraryIdentifier:
+ _objc_msgSend$initWithFrame:zPosition:identifier:
+ _objc_msgSend$initWithImageAtURL:
+ _objc_msgSend$initWithImageSize:deviceResolution:parallaxPadding:visibleFrame:adaptiveVisibleFrame:inactiveFrame:adaptiveInactiveTopFrame:spatialVisibleFrame:spatialAdaptiveFrame:timeFrame:adaptiveTimeFrame:salientContentFrame:clockLayerOrder:clockIntersection:layoutVariant:hasTopEdgeContact:maxClockShift:debugLayouts:
+ _objc_msgSend$initWithLayers:layout:depthEnabled:parallaxDisabled:clockAreaLuminance:settlingEffectEnabled:spatialPhotoEnabled:
+ _objc_msgSend$initWithLossyCompressionQuality:
+ _objc_msgSend$initWithPointSpaceSortedTimeRectss:screenScale:
+ _objc_msgSend$initWithPosterClassification:initialRect:imageSize:effectiveAcceptableRect:effectivePreferredRect:validBoundsNormalized:headroomFeasible:hasTopEdgeContact:computeSpatial:spatialPadding:layoutType:allowedLayoutStrategies:layoutConfiguration:
+ _objc_msgSend$initWithSceneData:scene:frame:zPosition:identifier:
+ _objc_msgSend$initWithVisibleRect:adaptiveVisibleRect:cropScore:layoutScore:clockOverlapAcceptable:headroomEngaged:adaptiveHeadroom:maxClockShift:layoutVariant:notificationRoom:
+ _objc_msgSend$intermediateWithAdaptiveStrategy:intermediate:
+ _objc_msgSend$intermediateWithSpatialStrategy:intermediate:
+ _objc_msgSend$iptcDictionary
+ _objc_msgSend$isPortrait
+ _objc_msgSend$isSpatialPhoto
+ _objc_msgSend$isSpatialPhotoAvailable
+ _objc_msgSend$isSpatialPhotoEnabled
+ _objc_msgSend$layerStackByUpdatingSpatialPhotoEnabled:
+ _objc_msgSend$layoutByUpdatingAdaptiveTimeFrame:
+ _objc_msgSend$layoutByUpdatingAdaptiveVisibleFrame:
+ _objc_msgSend$layoutByUpdatingNormalizedAdaptiveTimeFrame:
+ _objc_msgSend$layoutByUpdatingNormalizedAdaptiveVisibleFrame:
+ _objc_msgSend$layoutByUpdatingNormalizedVisibleFrame:remapAdaptiveVisibleFrame:
+ _objc_msgSend$layoutVariant
+ _objc_msgSend$lossyCompressionQuality
+ _objc_msgSend$maxClockShift
+ _objc_msgSend$maxStrechAmountNormalized
+ _objc_msgSend$maxTimeRect
+ _objc_msgSend$maxTimeRectInImageSpace
+ _objc_msgSend$metadataNeedsProcessing:
+ _objc_msgSend$minTimeRect
+ _objc_msgSend$minTimeRectInImageSpace
+ _objc_msgSend$normalizedAdaptiveTimeFrame
+ _objc_msgSend$normalizedAdaptiveVisibleFrame
+ _objc_msgSend$normalizedLandscapeAdaptiveTimeFrame
+ _objc_msgSend$normalizedLandscapeAdaptiveVisibleFrame
+ _objc_msgSend$photoLibraryIdentifier
+ _objc_msgSend$policies
+ _objc_msgSend$policyWithLocation:
+ _objc_msgSend$policyWithPolicies:
+ _objc_msgSend$processMetadata:
+ _objc_msgSend$quickTimeUserDataMultitrackMemoryMovieType
+ _objc_msgSend$quicktimeMetadataCinematicVideoIntent
+ _objc_msgSend$salientContentFrame
+ _objc_msgSend$salientContentRect
+ _objc_msgSend$scene
+ _objc_msgSend$sceneData
+ _objc_msgSend$scoreBonusAdaptiveWithLayoutType:
+ _objc_msgSend$scoreBonusOverlapStretchWithLayoutType:
+ _objc_msgSend$setAccessibilityDescription:
+ _objc_msgSend$setAdaptiveInactiveTopRect:
+ _objc_msgSend$setAdaptiveStrategy:
+ _objc_msgSend$setAdaptiveVisibleRect:
+ _objc_msgSend$setCaption:
+ _objc_msgSend$setCompression:
+ _objc_msgSend$setCreationDate:timeZone:
+ _objc_msgSend$setCropScore:
+ _objc_msgSend$setHasSidebarContents:
+ _objc_msgSend$setHasTopEdgeContact:
+ _objc_msgSend$setHeadroomStrategy:
+ _objc_msgSend$setImageURL:
+ _objc_msgSend$setInactiveRect:
+ _objc_msgSend$setInactiveStrategy:
+ _objc_msgSend$setLayoutScore:
+ _objc_msgSend$setLayoutVariant:
+ _objc_msgSend$setLocation:
+ _objc_msgSend$setLossyCompressionQuality:
+ _objc_msgSend$setMaxClockShift:
+ _objc_msgSend$setOverlapStrategy:
+ _objc_msgSend$setParallaxStrategy:
+ _objc_msgSend$setPolicies:
+ _objc_msgSend$setSalientContentRect:
+ _objc_msgSend$setSpatialAdaptiveVisibleRect:
+ _objc_msgSend$setSpatialStrategy:
+ _objc_msgSend$setSpatialVisibleRect:
+ _objc_msgSend$setTimeBottomOverlap:
+ _objc_msgSend$setTimeTopOverlap:
+ _objc_msgSend$setUninflatedUnsafeAreaOverlap:
+ _objc_msgSend$setUnsafeAreaOverlap:
+ _objc_msgSend$setVisibleRect:
+ _objc_msgSend$setZoomFactor:
+ _objc_msgSend$setZoomStrategy:
+ _objc_msgSend$sortedTimeRects
+ _objc_msgSend$spatialAdaptiveFrame
+ _objc_msgSend$spatialAdaptiveVisibleRect
+ _objc_msgSend$spatialPadding
+ _objc_msgSend$spatialPhotoEnabled
+ _objc_msgSend$spatialStrategy
+ _objc_msgSend$spatialVisibleFrame
+ _objc_msgSend$spatialVisibleRect
+ _objc_msgSend$tiffDictionary
+ _objc_msgSend$timeRectCollectionLandscape
+ _objc_msgSend$timeRectCollectionPortrait
+ _objc_msgSend$timeRectForNormalizedHeight:
+ _objc_msgSend$topFrameForVisibleRect:adaptiveRect:
+ _objc_msgSend$topFrameFromVisibleRectAspectRatio:adaptiveRect:
+ _objc_msgSend$updateWithConfiguration:
+ _objc_msgSend$userAdjustedTitleLabelHeightOffset
+ _objc_msgSend$valueWithRect:
+ _objc_msgSend$widgetZoneAdjustmentForVisibleFrame:essentialRect:
+ _objc_msgSend$zoomFactor
+ _sForceDisableLandscape
+ _s_timeRectCollectionLandscape
+ _s_timeRectCollectionPortrait
+ _standardPolicy.onceToken
+ _standardPolicy.onceToken.42
+ _standardPolicy.onceToken.78
+ _standardPolicy.standardPolicy
+ _standardPolicy.standardPolicy.41
+ _standardPolicy.standardPolicy.77
- +[PFMediaUtilities defaultRasterizationDPI]
- +[PFMediaUtilities typeRequiresRasterizationDPI:]
- -[PFColorConverter .cxx_destruct]
- -[PFColorConverter adjustPixelBuffer:toOutputBuffer:]
- -[PFColorConverter convertWithVideoURL:outURL:progress:completion:]
- -[PFParallaxLayerStack initWithLayers:layout:depthEnabled:parallaxDisabled:clockAreaLuminance:settlingEffectEnabled:]
- -[PFParallaxLayoutHelper initWithPosterClassification:initialRect:imageSize:effectiveAcceptableRect:effectivePreferredRect:validBoundsNormalized:headroomFeasible:hasTopEdgeContact:layoutType:layoutConfiguration:]
- -[PFPosterOrientedLayout initWithImageSize:deviceResolution:parallaxPadding:visibleFrame:inactiveFrame:timeFrame:clockLayerOrder:clockIntersection:debugLayouts:]
- -[PFPosterOrientedLayout initWithImageSize:deviceResolution:parallaxPadding:visibleFrame:inactiveFrame:timeFrame:clockLayerOrder:clockIntersection:hasTopEdgeContact:debugLayouts:]
- GCC_except_table1312
- GCC_except_table1319
- GCC_except_table1322
- GCC_except_table1357
- GCC_except_table1371
- GCC_except_table1465
- GCC_except_table1480
- GCC_except_table1534
- GCC_except_table1555
- GCC_except_table1557
- GCC_except_table1643
- GCC_except_table1647
- GCC_except_table1658
- GCC_except_table1694
- GCC_except_table1696
- GCC_except_table1711
- GCC_except_table1722
- GCC_except_table1748
- GCC_except_table1756
- GCC_except_table1759
- GCC_except_table1773
- GCC_except_table1794
- GCC_except_table1797
- GCC_except_table180
- GCC_except_table1806
- GCC_except_table1910
- GCC_except_table1941
- GCC_except_table1946
- GCC_except_table1948
- GCC_except_table1962
- GCC_except_table2018
- GCC_except_table2027
- GCC_except_table2047
- GCC_except_table2111
- GCC_except_table2114
- GCC_except_table2121
- GCC_except_table2247
- GCC_except_table2248
- GCC_except_table2255
- GCC_except_table2257
- GCC_except_table2258
- GCC_except_table2260
- GCC_except_table2307
- GCC_except_table2330
- GCC_except_table2332
- GCC_except_table2445
- GCC_except_table2623
- GCC_except_table2690
- GCC_except_table2691
- GCC_except_table2694
- GCC_except_table2696
- GCC_except_table2697
- GCC_except_table2701
- GCC_except_table2703
- GCC_except_table2705
- GCC_except_table2707
- GCC_except_table2708
- GCC_except_table2710
- GCC_except_table2711
- GCC_except_table2718
- GCC_except_table2719
- GCC_except_table2720
- GCC_except_table2721
- GCC_except_table2723
- GCC_except_table2724
- GCC_except_table2725
- GCC_except_table2727
- GCC_except_table2736
- GCC_except_table2738
- GCC_except_table2740
- GCC_except_table2746
- GCC_except_table2747
- GCC_except_table2748
- GCC_except_table2750
- GCC_except_table2754
- GCC_except_table2770
- GCC_except_table2772
- GCC_except_table2773
- GCC_except_table2778
- GCC_except_table2779
- GCC_except_table2780
- GCC_except_table2781
- GCC_except_table2782
- GCC_except_table2788
- GCC_except_table2791
- GCC_except_table2846
- GCC_except_table2955
- GCC_except_table2957
- GCC_except_table2970
- GCC_except_table2982
- GCC_except_table2985
- GCC_except_table2993
- GCC_except_table2995
- GCC_except_table3000
- GCC_except_table3007
- GCC_except_table3008
- GCC_except_table3025
- GCC_except_table3061
- GCC_except_table3071
- GCC_except_table3075
- GCC_except_table3078
- GCC_except_table3079
- GCC_except_table3129
- GCC_except_table3138
- GCC_except_table3213
- GCC_except_table3281
- GCC_except_table3283
- GCC_except_table3300
- GCC_except_table3310
- GCC_except_table3325
- GCC_except_table3327
- GCC_except_table3564
- GCC_except_table3568
- GCC_except_table3575
- GCC_except_table3580
- GCC_except_table3590
- GCC_except_table3597
- GCC_except_table3600
- GCC_except_table3601
- GCC_except_table3602
- GCC_except_table3606
- GCC_except_table3608
- GCC_except_table3615
- GCC_except_table3616
- GCC_except_table3619
- GCC_except_table3626
- GCC_except_table3628
- GCC_except_table3631
- GCC_except_table3632
- GCC_except_table3633
- GCC_except_table3634
- GCC_except_table3635
- GCC_except_table3642
- GCC_except_table3643
- GCC_except_table3644
- GCC_except_table3646
- GCC_except_table3650
- GCC_except_table3651
- GCC_except_table3653
- GCC_except_table3654
- GCC_except_table3657
- GCC_except_table3670
- GCC_except_table3677
- GCC_except_table3682
- GCC_except_table3683
- GCC_except_table3687
- GCC_except_table3691
- GCC_except_table3700
- GCC_except_table3704
- GCC_except_table3705
- GCC_except_table3706
- GCC_except_table3708
- GCC_except_table3709
- GCC_except_table3710
- GCC_except_table3714
- GCC_except_table3717
- GCC_except_table3718
- GCC_except_table3720
- GCC_except_table3721
- GCC_except_table3722
- GCC_except_table3723
- GCC_except_table3724
- GCC_except_table3726
- GCC_except_table3728
- GCC_except_table3729
- GCC_except_table3730
- GCC_except_table3731
- GCC_except_table3734
- GCC_except_table3801
- GCC_except_table3868
- GCC_except_table3874
- GCC_except_table3947
- GCC_except_table3949
- GCC_except_table3952
- GCC_except_table3986
- GCC_except_table3987
- GCC_except_table3988
- GCC_except_table3990
- GCC_except_table3992
- GCC_except_table4231
- GCC_except_table4238
- GCC_except_table4240
- GCC_except_table467
- GCC_except_table478
- GCC_except_table481
- GCC_except_table528
- GCC_except_table535
- GCC_except_table573
- GCC_except_table577
- GCC_except_table578
- GCC_except_table579
- GCC_except_table588
- GCC_except_table591
- GCC_except_table592
- GCC_except_table596
- GCC_except_table599
- GCC_except_table603
- GCC_except_table604
- GCC_except_table606
- GCC_except_table607
- GCC_except_table613
- GCC_except_table614
- GCC_except_table615
- GCC_except_table620
- GCC_except_table622
- GCC_except_table626
- GCC_except_table632
- GCC_except_table633
- GCC_except_table634
- GCC_except_table635
- GCC_except_table636
- GCC_except_table638
- GCC_except_table639
- GCC_except_table640
- GCC_except_table641
- GCC_except_table642
- GCC_except_table645
- GCC_except_table647
- GCC_except_table648
- GCC_except_table649
- GCC_except_table650
- GCC_except_table656
- GCC_except_table661
- GCC_except_table675
- GCC_except_table677
- GCC_except_table678
- GCC_except_table679
- GCC_except_table960
- _AVFileTypeDNG
- _OBJC_CLASS_$_PFColorConverter
- _OBJC_IVAR_$_PFColorConverter._conversionContext
- _OBJC_IVAR_$_PFColorConverter._readerWriter
- _OBJC_METACLASS_$_PFColorConverter
- _PFPosterEnableCropVariant
- _PFPosterEnableHeadroom
- _Vertices.11102
- __AuxiliaryImageCVPixelBufferReleaseBytesCallback.3463
- __OBJC_$_INSTANCE_METHODS_PFColorConverter
- __OBJC_$_INSTANCE_VARIABLES_PFColorConverter
- __OBJC_$_PROP_LIST_PFColorConverter
- __OBJC_$_PROP_LIST_PFMetadataImage.6112
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PFAVReaderWriterAdjustDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_PFAVReaderWriterAdjustDelegate
- __OBJC_$_PROTOCOL_REFS_PFAVReaderWriterAdjustDelegate
- __OBJC_CLASS_PROTOCOLS_$_PFColorConverter
- __OBJC_CLASS_RO_$_PFColorConverter
- __OBJC_LABEL_PROTOCOL_$_PFAVReaderWriterAdjustDelegate
- __OBJC_METACLASS_RO_$_PFColorConverter
- __OBJC_PROTOCOL_$_PFAVReaderWriterAdjustDelegate
- __ZN2pf20back_insert_node_setERKN5boost9unordered13unordered_setINS0_12interprocess10offset_ptrINS_17SceneTaxonomyNodeElmLm0EEENS_24SceneTaxonomyNodeFunctorES7_NS3_9allocatorIS6_NS3_15segment_managerIcNS3_15rbtree_best_fitINS3_17null_mutex_familyENS4_IvlmLm0EEELm0EEENS3_10iset_indexEEEEEEERNSt3__16vectorIPKS5_NSK_9allocatorISN_EEEE
- __ZN5boost12interprocess9ipcdetail27managed_open_or_create_implINS1_12file_wrapperELm8ELb1ELb0EED2Ev
- __ZN5boost12interprocessL8ec_tableE.7851
- __ZN5boost8geometry5index6detail5rtree8visitors14distance_queryINS1_5rtreeINSt3__14pairINS0_5model5pointIfLm2ENS0_2cs9cartesianEEEtEENS1_9quadraticILm32ELm8EEENS1_9indexableISE_EENS1_8equal_toISE_EENS_12interprocess9allocatorISE_NSL_15segment_managerIcNSL_15rbtree_best_fitINSL_17null_mutex_familyENSL_10offset_ptrIvlmLm0EEELm0EEENSL_10iset_indexEEEEEE14members_holderENS2_10predicates7nearestISD_EEED1Ev
- __ZN5boost9container12basic_stringIcNSt3__111char_traitsIcEENS_12interprocess9allocatorIcNS5_15segment_managerIcNS5_15rbtree_best_fitINS5_17null_mutex_familyENS5_10offset_ptrIvlmLm0EEELm0EEENS5_10iset_indexEEEEEED2Ev
- __ZN5boost9container6vectorINSt3__14pairIhhEENS_12interprocess9allocatorIS4_NS5_15segment_managerIcNS5_15rbtree_best_fitINS5_17null_mutex_familyENS5_10offset_ptrIvlmLm0EEELm0EEENS5_10iset_indexEEEEEvED2Ev
- __ZN5boost9container6vectorIjNS_12interprocess9allocatorIjNS2_15segment_managerIcNS2_15rbtree_best_fitINS2_17null_mutex_familyENS2_10offset_ptrIvlmLm0EEELm0EEENS2_10iset_indexEEEEEvED2Ev
- __ZN5boost9intrusive8bstbase2INS0_8bhtraitsINS_12interprocess9ipcdetail25intrusive_value_type_implINS0_12generic_hookILNS0_10algo_typesE5ENS0_18rbtree_node_traitsINS3_10offset_ptrIvlmLm0EEELb1EEENS0_7dft_tagELNS0_14link_mode_typeE1ELNS0_14base_hook_typeE3EEEcmEESB_LSD_1ESC_Lj3EEEvvLS7_5EvEC2ERKNSt3__14lessISG_EERKSH_
- __ZN5boost9intrusiveneERKNS0_13tree_iteratorINS0_8bhtraitsINS_12interprocess15rbtree_best_fitINS3_17null_mutex_familyENS3_10offset_ptrIvlmLm0EEELm0EE10block_ctrlENS0_18rbtree_node_traitsIS7_Lb1EEELNS0_14link_mode_typeE0ENS0_7dft_tagELj3EEELb0EEESH_
- __ZNK5boost4hashINS_9container12basic_stringIcNSt3__111char_traitsIcEENS_12interprocess9allocatorIcNS6_15segment_managerIcNS6_15rbtree_best_fitINS6_17null_mutex_familyENS6_10offset_ptrIvlmLm0EEELm0EEENS6_10iset_indexEEEEEEEEclERKSH_
- __ZNK5boost9unordered6detail5tableINS1_3mapINS_12interprocess9allocatorINSt3__14pairIKNS_9container12basic_stringIcNS6_11char_traitsIcEENS5_IcNS4_15segment_managerIcNS4_15rbtree_best_fitINS4_17null_mutex_familyENS4_10offset_ptrIvlmLm0EEELm0EEENS4_10iset_indexEEEEEEEN2pf17SceneTaxonomyNodeEEESJ_EESL_SO_NS_4hashISL_EENS6_8equal_toISL_EEEEE9find_nodeERSM_
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ne190102ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
- __ZNKSt3__16vectorIN5boost8geometry5index6detail5rtree8visitors14distance_queryINS3_5rtreeINS_4pairINS2_5model5pointIfLm2ENS2_2cs9cartesianEEEtEENS3_9quadraticILm32ELm8EEENS3_9indexableISF_EENS3_8equal_toISF_EENS1_12interprocess9allocatorISF_NSM_15segment_managerIcNSM_15rbtree_best_fitINSM_17null_mutex_familyENSM_10offset_ptrIvlmLm0EEELm0EEENSM_10iset_indexEEEEEE14members_holderENS4_10predicates7nearestISE_EEE11branch_dataENS_9allocatorIS13_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4pairIN5boost8geometry5model5pointIfLm2ENS3_2cs9cartesianEEEtEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4pairIPKN5boost8geometry5index6detail5rtree8ptr_pairINS3_5model3boxINS8_5pointIfLm2ENS3_2cs9cartesianEEEEENS2_12interprocess10offset_ptrINS2_7variantINS6_12variant_leafINS1_ISD_tEENS4_9quadraticILm32ELm8EEESE_NS6_10allocatorsINSF_9allocatorISJ_NSF_15segment_managerIcNSF_15rbtree_best_fitINSF_17null_mutex_familyENSG_IvlmLm0EEELm0EEENSF_10iset_indexEEEEESJ_SL_SE_NS6_23node_variant_static_tagEEESW_EEJNS6_21variant_internal_nodeISJ_SL_SE_SX_SW_EEEEElmLm0EEEEES15_EENS_9allocatorIS16_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4pairIdPKNS1_IN5boost8geometry5model5pointIfLm2ENS3_2cs9cartesianEEEtEEEENS_9allocatorISC_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPKN2pf17SceneTaxonomyNodeENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__18equal_toIN5boost9container12basic_stringIcNS_11char_traitsIcEENS1_12interprocess9allocatorIcNS6_15segment_managerIcNS6_15rbtree_best_fitINS6_17null_mutex_familyENS6_10offset_ptrIvlmLm0EEELm0EEENS6_10iset_indexEEEEEEEEclB8ne190102ERKSH_SK_
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne190102ERKS6_S9_
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__110unique_ptrIN5boost12interprocess25basic_managed_mapped_fileIcNS2_15rbtree_best_fitINS2_17null_mutex_familyENS2_10offset_ptrIvlmLm0EEELm0EEENS2_10iset_indexEEENS_14default_deleteISA_EEE5resetB8ne190102EPSA_
- __ZNSt3__112__destroy_atB8ne190102INS_4pairIKN5boost9container12basic_stringIcNS_11char_traitsIcEENS2_12interprocess9allocatorIcNS7_15segment_managerIcNS7_15rbtree_best_fitINS7_17null_mutex_familyENS7_10offset_ptrIvlmLm0EEELm0EEENS7_10iset_indexEEEEEEEN2pf17SceneTaxonomyNodeEEELi0EEEvPT_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__116allocator_traitsIN5boost12interprocess9allocatorINS1_9unordered6detail4nodeINS3_IN2pf18SceneGeographyNodeENS2_15segment_managerIcNS2_15rbtree_best_fitINS2_17null_mutex_familyENS2_10offset_ptrIvlmLm0EEELm0EEENS2_10iset_indexEEEEENS_4pairIKNS1_9container12basic_stringIcNS_11char_traitsIcEENS3_IcSG_EEEES8_EEEESG_EEE10deallocateB8ne190102ERSS_NSC_ISR_lmLm0EEEm
- __ZNSt3__116allocator_traitsIN5boost12interprocess9allocatorINS1_9unordered6detail4nodeINS3_INS2_10offset_ptrIN2pf17SceneTaxonomyNodeElmLm0EEENS2_15segment_managerIcNS2_15rbtree_best_fitINS2_17null_mutex_familyENS7_IvlmLm0EEELm0EEENS2_10iset_indexEEEEESA_EESH_EEE10deallocateB8ne190102ERSK_NS7_ISJ_lmLm0EEEm
- __ZNSt3__116allocator_traitsIN5boost12interprocess9allocatorINS1_9unordered6detail4nodeINS3_INS_4pairIKNS1_9container12basic_stringIcNS_11char_traitsIcEENS3_IcNS2_15segment_managerIcNS2_15rbtree_best_fitINS2_17null_mutex_familyENS2_10offset_ptrIvlmLm0EEELm0EEENS2_10iset_indexEEEEEEEN2pf17SceneTaxonomyNodeEEESJ_EESP_EESJ_EEE10deallocateB8ne190102ERSS_NSF_ISR_lmLm0EEEm
- __ZNSt3__116allocator_traitsIN5boost12interprocess9allocatorINS1_9unordered6detail4nodeINS3_INS_4pairIKyNS2_10offset_ptrIN2pf17SceneTaxonomyNodeElmLm0EEEEENS2_15segment_managerIcNS2_15rbtree_best_fitINS2_17null_mutex_familyENS9_IvlmLm0EEELm0EEENS2_10iset_indexEEEEESD_EESK_EEE10deallocateB8ne190102ERSN_NS9_ISM_lmLm0EEEm
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4pairIN5boost8geometry5model5pointIfLm2ENS4_2cs9cartesianEEEtEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4pairIdPKNS2_IN5boost8geometry5model5pointIfLm2ENS4_2cs9cartesianEEEtEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSH_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPKN2pf17SceneTaxonomyNodeEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEtEEPvEEEEEclB8ne190102EPSB_
- __ZNSt3__15dequeIPKvNS_9allocatorIS2_EEED2B8ne190102Ev
- __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERN5boost8geometry5index6detail5rtree10pack_utils22point_entries_comparerILm0EEENS2_9container12vec_iteratorIPNS_4pairINS3_5model5pointIfLm2ENS3_2cs9cartesianEEENS_11__wrap_iterIPNSD_ISI_tEEEEEELb0EEEEEjT1_SQ_SQ_T0_
- __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERN5boost8geometry5index6detail5rtree10pack_utils22point_entries_comparerILm1EEENS2_9container12vec_iteratorIPNS_4pairINS3_5model5pointIfLm2ENS3_2cs9cartesianEEENS_11__wrap_iterIPNSD_ISI_tEEEEEELb0EEEEEjT1_SQ_SQ_T0_
- __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB8ne190102IRN5boost9container12vec_iteratorIPNS_4pairINS4_8geometry5model5pointIfLm2ENS8_2cs9cartesianEEENS_11__wrap_iterIPNS7_ISD_tEEEEEELb0EEESL_EEvOT_OT0_
- __ZNSt3__19__sift_upB8ne190102INS_17_ClassicAlgPolicyERN5boost8geometry5index6detail5rtree8visitors15pair_first_lessENS_11__wrap_iterIPNS_4pairIdPKNSB_INS3_5model5pointIfLm2ENS3_2cs9cartesianEEEtEEEEEEEEvT1_SN_OT0_NS_15iterator_traitsISN_E15difference_typeE
- __ZNSt3__19__sift_upB8ne190102INS_17_ClassicAlgPolicyERN5boost8geometry5index6detail5rtree8visitors16branch_data_compENS_11__wrap_iterIPNS7_14distance_queryINS4_5rtreeINS_4pairINS3_5model5pointIfLm2ENS3_2cs9cartesianEEEtEENS4_9quadraticILm32ELm8EEENS4_9indexableISJ_EENS4_8equal_toISJ_EENS2_12interprocess9allocatorISJ_NSQ_15segment_managerIcNSQ_15rbtree_best_fitINSQ_17null_mutex_familyENSQ_10offset_ptrIvlmLm0EEELm0EEENSQ_10iset_indexEEEEEE14members_holderENS5_10predicates7nearestISI_EEE11branch_dataEEEEEvT1_S1A_OT0_NS_15iterator_traitsIS1A_E15difference_typeE
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- ___Block_byref_object_copy_.10862
- ___Block_byref_object_copy_.11497
- ___Block_byref_object_copy_.12781
- ___Block_byref_object_copy_.4048
- ___Block_byref_object_copy_.4463
- ___Block_byref_object_copy_.4944
- ___Block_byref_object_copy_.5057
- ___Block_byref_object_copy_.5686
- ___Block_byref_object_copy_.6357
- ___Block_byref_object_copy_.7327
- ___Block_byref_object_copy_.8282
- ___Block_byref_object_copy_.8783
- ___Block_byref_object_copy_.9112
- ___Block_byref_object_copy_.9524
- ___Block_byref_object_dispose_.10863
- ___Block_byref_object_dispose_.11498
- ___Block_byref_object_dispose_.12782
- ___Block_byref_object_dispose_.4049
- ___Block_byref_object_dispose_.4464
- ___Block_byref_object_dispose_.4945
- ___Block_byref_object_dispose_.5058
- ___Block_byref_object_dispose_.5687
- ___Block_byref_object_dispose_.6358
- ___Block_byref_object_dispose_.7328
- ___Block_byref_object_dispose_.8283
- ___Block_byref_object_dispose_.8784
- ___Block_byref_object_dispose_.9113
- ___Block_byref_object_dispose_.9525
- ___PFBitmaskDescription_block_invoke
- ___block_descriptor_64_e8_32s40s48r_e25_v32?0"NSNumber"8Q16^B24ls32l8s40l8r48l8
- ___block_literal_global.1082
- ___block_literal_global.10856
- ___block_literal_global.11148
- ___block_literal_global.11494
- ___block_literal_global.11744
- ___block_literal_global.11905
- ___block_literal_global.12.5696
- ___block_literal_global.123.8773
- ___block_literal_global.1231
- ___block_literal_global.12313
- ___block_literal_global.12470
- ___block_literal_global.12597
- ___block_literal_global.128.9211
- ___block_literal_global.1411
- ___block_literal_global.142.10413
- ___block_literal_global.147.5432
- ___block_literal_global.152.5429
- ___block_literal_global.162.10302
- ___block_literal_global.1817
- ___block_literal_global.195.1979
- ___block_literal_global.2.4785
- ___block_literal_global.2085
- ___block_literal_global.2303
- ___block_literal_global.246
- ___block_literal_global.264
- ___block_literal_global.2783
- ___block_literal_global.288
- ___block_literal_global.3171
- ___block_literal_global.3321
- ___block_literal_global.3603
- ___block_literal_global.3858
- ___block_literal_global.4
- ___block_literal_global.4140
- ___block_literal_global.4197
- ___block_literal_global.4206
- ___block_literal_global.4638
- ___block_literal_global.4783
- ___block_literal_global.5000
- ___block_literal_global.5082
- ___block_literal_global.5455
- ___block_literal_global.5678
- ___block_literal_global.6
- ___block_literal_global.6410
- ___block_literal_global.6471
- ___block_literal_global.7032
- ___block_literal_global.7182
- ___block_literal_global.7981
- ___block_literal_global.8.12467
- ___block_literal_global.86
- ___block_literal_global.8834
- ___block_literal_global.9267
- ___block_literal_global.93
- ___block_literal_global.9641
- ___block_literal_global.97.8790
- __computeIsProRes.proResCodecs
- __exifDateTimeFormatter.dateTimeFormatter.5622
- __exifDateTimeFormatter.onceToken.5620
- __exifSubsecTimeFormatter.onceToken.5607
- __exifSubsecTimeFormatter.subsecTimeFormatter.5608
- __gpsDateFormatter.dateFormatter.5644
- __gpsDateFormatter.onceToken.5643
- __gpsTimeFormatter.onceToken.5648
- __gpsTimeFormatter.timeFormatter.5649
- _kCIContextName
- _kCIImageColorSpace
- _objc_msgSend$headroomPenaltyForIntermediateLayout:originalFullExtent:layoutConfiguration:
- _objc_msgSend$imageWithCVPixelBuffer:options:
- _objc_msgSend$initWithConfigurationType:
- _objc_msgSend$initWithDescriptorType:media:
- _objc_msgSend$initWithImageSize:deviceResolution:parallaxPadding:visibleFrame:inactiveFrame:timeFrame:clockLayerOrder:clockIntersection:hasTopEdgeContact:debugLayouts:
- _objc_msgSend$initWithLayers:layout:depthEnabled:parallaxDisabled:clockAreaLuminance:settlingEffectEnabled:
- _objc_msgSend$initWithPosterClassification:initialRect:imageSize:effectiveAcceptableRect:effectivePreferredRect:validBoundsNormalized:headroomFeasible:hasTopEdgeContact:layoutType:layoutConfiguration:
- _objc_msgSend$intermediateWithParallaxStrategy:intermediate:
- _objc_msgSend$render:toCVPixelBuffer:bounds:colorSpace:
- _objc_msgSend$writeToURL:progress:completion:
- _objc_retain_x6
CStrings:
+ "%@ vis:%.0f,%.0f %.0fx%.0f stub:%@ z:%@ o:%@ p:%@ i:%@ scores, crop:%.2f layout:%.2f bot:%.2f top:%.2f unsafe:%.2f uninfunsafe:%.2f maxClock:%.2f"
+ "(unable to get channel layout)"
+ "+[PFParallaxLayerStackArchiver saveCompoundLayerStack:toURL:options:error:]"
+ "-[PFParallaxDataLayer initWithData:frame:zPosition:identifier:]"
+ "-[PFParallaxLayerStack initWithLayers:layout:depthEnabled:parallaxDisabled:clockAreaLuminance:settlingEffectEnabled:spatialPhotoEnabled:]"
+ "/AppleInternal/Library/BuildRoots/4~B2OaugC4nKd_XCJA6Kp53h_v0kniGmmO6YQi9u4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/geometry/index/detail/exception.hpp"
+ "/Library/Caches/com.apple.xbs/Sources/Photos/Projects/PhotosFormats/PhotosFormats/PFParallaxLayerStack.m"
+ "6"
+ "<%@ %p; identifier: %@; options: %ld; media: %@; edit configuration: %@; shuffle configuration: %@ layout configuration: %@ user info: %@> photoLibraryIdentifier: %ld>"
+ "<%@ %p; style: %@; norm. visible frame: %@; norm. adapt. visible frame: %@; norm. adapt. time frame: %@; land. norm. visible frame: %@; land. norm. adapt. visible frame: %@; land. norm. adapt. time frame: %@; zoom: %@; depth: %@|%@; settle: %@|%@ spatial: %@|%@>"
+ "<%@:%p %0.0fx%0.0f depth:%d parallax:%d settling:%d spatial:%d layers:%@ layout:%@>"
+ "@"
+ "@\"<PFParallaxSpatialPhotoScene>\""
+ "@136@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48d80d88B96B100d104d112Q120d128"
+ "@144@0:8Q16@24Q32Q40{CGRect={CGPoint=dd}{CGSize=dd}}48{CGRect={CGPoint=dd}{CGSize=dd}}80{CGRect={CGPoint=dd}{CGSize=dd}}112"
+ "@148@0:8Q16@24Q32Q40{CGRect={CGPoint=dd}{CGSize=dd}}48{CGRect={CGPoint=dd}{CGSize=dd}}80{CGRect={CGPoint=dd}{CGSize=dd}}112B144"
+ "@20@0:8f16"
+ "@212@0:8Q16{CGRect={CGPoint=dd}{CGSize=dd}}24{CGSize=dd}56{CGRect={CGPoint=dd}{CGSize=dd}}72{CGRect={CGPoint=dd}{CGSize=dd}}104{CGRect={CGPoint=dd}{CGSize=dd}}136B168B172B176d180Q188Q196@204"
+ "@268@0:8{CGSize=dd}16{CGSize=dd}32{CGSize=dd}48{CGRect={CGPoint=dd}{CGSize=dd}}64{CGRect={CGPoint=dd}{CGSize=dd}}96{CGRect={CGPoint=dd}{CGSize=dd}}128{CGRect={CGPoint=dd}{CGSize=dd}}160{CGRect={CGPoint=dd}{CGSize=dd}}192@224Q232Q240B248d252@260"
+ "@32@0:8@16d24"
+ "@32@0:8q16q24"
+ "@396@0:8{CGSize=dd}16{CGSize=dd}32{CGSize=dd}48{CGRect={CGPoint=dd}{CGSize=dd}}64{CGRect={CGPoint=dd}{CGSize=dd}}96{CGRect={CGPoint=dd}{CGSize=dd}}128{CGRect={CGPoint=dd}{CGSize=dd}}160{CGRect={CGPoint=dd}{CGSize=dd}}192{CGRect={CGPoint=dd}{CGSize=dd}}224{CGRect={CGPoint=dd}{CGSize=dd}}256{CGRect={CGPoint=dd}{CGSize=dd}}288{CGRect={CGPoint=dd}{CGSize=dd}}320@352Q360Q368B376d380@388"
+ "@40@0:8q16@24q32"
+ "@52@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16B48"
+ "@56@0:8@16@24B32B36d40B48B52"
+ "@80@0:8@16@24{CGRect={CGPoint=dd}{CGSize=dd}}32d64@72"
+ "@80@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGSize=dd}48{CGSize=dd}64"
+ "A layer stack requires a layout"
+ "B48@0:8@16@24@32^@40"
+ "ChipID"
+ "Compound layer stack is missing a portrait layer stack"
+ "Decoded PFPosterEditConfiguration contains legacy adaptive visible frame, ignored."
+ "Error initializing mapped data for: %@ error:%@"
+ "Exception while serializing layer stack contents: %@, contents: %@"
+ "GyroPoster"
+ "GyroPosterOcclusion"
+ "Incompatible adaptiveVisibleFrame sizes, old: %@ (%.2f) new %@ (%.2f), this will distort adaptiveTimeFrame."
+ "Incompatible visibleFrame sizes, old: %@ (%.2f) new %@ (%.2f), this will distort timeFrame"
+ "Invalid spatialPhotoFlag flag: %@"
+ "IsVirtualDevice"
+ "LZMA"
+ "MMRY"
+ "NSValuePFWallpaperExtensions"
+ "No intermediate layouts available to be scored, falling back to initial layout. Counts: headroom=%tu, zoom=%tu, overlap=%tu, inactive=%tu"
+ "PFAdaptiveLayoutVerticalPriorityThreshold"
+ "PFClientSideEncryptionManagerOptionCompressionKey"
+ "PFCropUtilitiesPosterOutputData"
+ "PFDeviceTimeRectCollection"
+ "PFImageIOOptionsBuilder"
+ "PFImageMetadataChangePolicy"
+ "PFImageMetadataChangePolicyAddPFMetadata"
+ "PFImageMetadataChangePolicyComposite"
+ "PFImageMetadataChangePolicyDefault"
+ "PFImageMetadataChangePolicySetAccessibilityDescription"
+ "PFImageMetadataChangePolicySetCaption"
+ "PFImageMetadataChangePolicySetCreationDate"
+ "PFImageMetadataChangePolicySetLocation"
+ "PFImageMetadataChangePolicySharedPhotoStream"
+ "PFImageMetadataChangePolicyiCloudPhotoLibrary"
+ "PFParallaxDataLayer"
+ "PFParallaxMutableIntermediateLayout"
+ "PFParallaxSpatialPhotoLayer"
+ "PFParallaxSpatialPhotoOcclusionLayer"
+ "PFPosterMediaURLImage"
+ "PICenterLayoutHorizontalLowerBound"
+ "PICenterLayoutHorizontalUpperBound"
+ "PI_DISABLE_ADAPTIVE_LAYOUT"
+ "POSTER_DISABLE_SPATIALPHOTO"
+ "POSTER_DISABLE_SPATIALPHOTO_OCCLUSION"
+ "Portrait layer stack is missing a layout"
+ "PosterAdaptiveLayout"
+ "PosterPortraitHeadroom"
+ "SBSAdaptiveTimeLayoutContext"
+ "Spatial Photo Occlusion Layer"
+ "SpatialPhoto"
+ "T@\"<PFParallaxSpatialPhotoScene>\",R,N,V_scene"
+ "T@\"CLLocation\",&,V_location"
+ "T@\"NSArray\",&,V_policies"
+ "T@\"NSArray\",R,N,V_sortedTimeRects"
+ "T@\"NSData\",R,C,N,V_data"
+ "T@\"NSData\",R,N,V_sceneData"
+ "T@\"NSDate\",&,V_creationDate"
+ "T@\"NSDictionary\",R,C"
+ "T@\"NSString\",&,V_key"
+ "T@\"NSString\",C,V_accessibilityDescription"
+ "T@\"NSString\",C,V_caption"
+ "T@\"NSTimeZone\",&,V_timeZone"
+ "T@\"NSURL\",&,N,V_imageURL"
+ "T@\"PFParallaxDataLayer\",R,N"
+ "T@\"PFParallaxSpatialPhotoLayer\",R,N"
+ "T@\"PFParallaxSpatialPhotoOcclusionLayer\",R,N"
+ "T@,&,V_value"
+ "TB,N,V_isSpatialPhotoAvailable"
+ "TB,N,V_isSpatialPhotoEnabled"
+ "TB,N,VhasTopEdgeContact"
+ "TB,R,N,V_clockOverlapAcceptable"
+ "TB,R,N,V_computeSpatial"
+ "TB,R,N,V_headroomEngaged"
+ "TB,R,N,V_spatialPhotoEnabled"
+ "TB,V_applyTransform"
+ "TB,V_includeDerivativeDefaults"
+ "TB,V_includeHDRGainMaps"
+ "TB,V_skipMetadata"
+ "TI,V_orientation"
+ "TQ,N,V_allowedLayoutStrategies"
+ "TQ,N,VadaptiveStrategy"
+ "TQ,N,VheadroomStrategy"
+ "TQ,N,VinactiveStrategy"
+ "TQ,N,VlayoutVariant"
+ "TQ,N,VoverlapStrategy"
+ "TQ,N,VparallaxStrategy"
+ "TQ,N,VspatialStrategy"
+ "TQ,N,VzoomStrategy"
+ "TQ,R,N,V_adaptiveStrategy"
+ "TQ,R,N,V_allowedLayoutStrategies"
+ "TQ,R,N,V_layoutVariant"
+ "TQ,R,N,V_spatialStrategy"
+ "TQ,V_colorBehavior"
+ "Td,N,V_additionalTitleLabelHeight"
+ "Td,N,V_allowedClockStretch"
+ "Td,N,V_userAdjustedTitleLabelHeightOffset"
+ "Td,N,VcropScore"
+ "Td,N,VlayoutScore"
+ "Td,N,VmaxClockShift"
+ "Td,N,VtimeBottomOverlap"
+ "Td,N,VtimeTopOverlap"
+ "Td,N,VuninflatedUnsafeAreaOverlap"
+ "Td,N,VunsafeAreaOverlap"
+ "Td,N,VzoomFactor"
+ "Td,R,N,V_adaptiveHeadroom"
+ "Td,R,N,V_maxClockShift"
+ "Td,R,N,V_notificationRoom"
+ "Td,R,N,V_spatialPadding"
+ "Td,R,N,V_zoomFactor"
+ "Tf,V_lossyCompressionQuality"
+ "Tq,R,N,V_photoLibraryIdentifier"
+ "Tq,V_maximumLongSideLength"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_normalizedAdaptiveTimeFrame"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_normalizedAdaptiveVisibleFrame"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_normalizedLandscapeAdaptiveTimeFrame"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_normalizedLandscapeAdaptiveVisibleFrame"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,VadaptiveInactiveTopRect"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,VadaptiveVisibleRect"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,VinactiveRect"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,VsalientContentRect"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,VspatialAdaptiveVisibleRect"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,VspatialVisibleRect"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,VvisibleRect"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_adaptiveInactiveTopFrame"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_adaptiveInactiveTopRect"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_adaptiveTimeFrame"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_adaptiveVisibleFrame"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_adaptiveVisibleRect"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_salientContentFrame"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_salientContentRect"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_spatialAdaptiveFrame"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_spatialAdaptiveVisibleRect"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_spatialVisibleFrame"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_spatialVisibleRect"
+ "URL Image"
+ "Unable to add metadata: %@"
+ "UpgradeSuggestionAdaptiveTime"
+ "UpgradeSuggestionGyroPoster"
+ "UpgradeSuggestionGyroPosterAdaptiveTime"
+ "Vertigo"
+ "[PFDeviceLockScreenTimeRectCollectionNormalized_SBS] timeout while requesting time rect collection"
+ "_adaptiveHeadroom"
+ "_adaptiveInactiveTopFrame"
+ "_adaptiveInactiveTopRect"
+ "_adaptiveStrategy"
+ "_adaptiveTimeFrame"
+ "_adaptiveVisibleFrame"
+ "_adaptiveVisibleRect"
+ "_additionalTitleLabelHeight"
+ "_allowedClockStretch"
+ "_allowedLayoutStrategies"
+ "_applyTransform"
+ "_clockOverlapAcceptable"
+ "_colorBehavior"
+ "_computeSpatial"
+ "_customOptions"
+ "_fallbackTimeRectCollectionForSBSFetchingFailureWithOrientation:"
+ "_filterImageProperties:metadataWithKey:preserveProperties:"
+ "_headroomEngaged"
+ "_includeDerivativeDefaults"
+ "_includeHDRGainMaps"
+ "_isSpatialPhotoAvailable"
+ "_isSpatialPhotoEnabled"
+ "_key"
+ "_layoutVariant"
+ "_loadDeviceTimeRectCollectionIfNeeded"
+ "_lossyCompressionQuality"
+ "_maxClockShift"
+ "_maximumLongSideLength"
+ "_normalizedAdaptiveTimeFrame"
+ "_normalizedAdaptiveVisibleFrame"
+ "_normalizedLandscapeAdaptiveTimeFrame"
+ "_normalizedLandscapeAdaptiveVisibleFrame"
+ "_notificationRoom"
+ "_photoLibraryIdentifier"
+ "_policies"
+ "_salientContentFrame"
+ "_salientContentRect"
+ "_scene"
+ "_sceneData"
+ "_skipMetadata"
+ "_sortedTimeRects"
+ "_spatialAdaptiveFrame"
+ "_spatialAdaptiveVisibleRect"
+ "_spatialPadding"
+ "_spatialPhotoEnabled"
+ "_spatialStrategy"
+ "_spatialVisibleFrame"
+ "_spatialVisibleRect"
+ "_timeRectInImageSpaceFromPointSpaceRect:screenScale:"
+ "_userAdjustedTitleLabelHeightOffset"
+ "_value"
+ "_zoomFactor"
+ "adaptiveFrameForTopEdgeVisibleFrame:layoutConfiguration:outVisibleFrame:maxClockStretchOverride:"
+ "adaptiveFrameForVisibleFrame:essentialRect:originalImageSize:layoutConfiguration:classification:maxClockStretchOverride:"
+ "adaptiveHeadroom"
+ "adaptiveInactiveTopFrame"
+ "adaptiveInactiveTopRect"
+ "adaptiveLayoutVerticalPriorityThreshold"
+ "adaptiveStrategy"
+ "adaptiveTimeFrame"
+ "adaptiveVisibleFrame"
+ "adaptiveVisibleRect"
+ "additionalTitleLabelHeight"
+ "allowedClockStretch"
+ "allowedLayoutStrategies"
+ "applyOptions:toArchive:"
+ "applyTransform"
+ "archiveFileAtURL:outputFileURL:options:error:"
+ "arrayWithObjects:"
+ "bestAdaptiveCropRectForPosterClassification:layoutConfiguration:sourcePixelWidth:sourcePixelHeight:sourcePreferredCropRectNormalized:sourceAcceptableCropRectNormalized:sourceFaceAreaRectNormalized:"
+ "bestAdaptiveCropRectForPosterClassification:layoutConfiguration:sourcePixelWidth:sourcePixelHeight:sourcePreferredCropRectNormalized:sourceAcceptableCropRectNormalized:sourceFaceAreaRectNormalized:headroomFeasible:"
+ "c"
+ "center"
+ "centerLayoutHorizontalLowerBound"
+ "centerLayoutHorizontalUpperBound"
+ "cinematicVideoIntent"
+ "clockOverlapAcceptable"
+ "closeup"
+ "closeupZoomPercentWithLayoutType:"
+ "colorBehavior"
+ "compoundLayerStack != nil"
+ "compoundLayerStackByUpdatingSpatialPhotoEnabled:"
+ "computeSpatial"
+ "computeSpatialFrameForVisibleRect:adaptiveVisibleRect:spatialPaddingPercentage:effectiveImageRect:"
+ "creationDateTimeZone"
+ "d80@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48"
+ "dataRepresentation"
+ "decodeFloatForKey:"
+ "deviceBackdropRoleConfiguration"
+ "encodeFloat:forKey:"
+ "fetchAdaptiveTimeBoundsForContext:timeHeight:completionHandler:"
+ "fetchAdaptiveTimeHeightLimitsForContext:completionHandler:"
+ "forceDisableLandscapeConfiguration:"
+ "genericBackdropConfigurationWithTitleBounds:"
+ "hasAlphaChannel"
+ "headroomEngaged"
+ "headroomUsage:"
+ "iPhone"
+ "imageSpaceTimeRectForPointSpaceTimeRect:"
+ "inactiveAdaptive"
+ "inactiveSpatialPhotoDataLayer"
+ "includeDerivativeDefaults"
+ "includeHDRGainMaps"
+ "initWithArray:"
+ "initWithConfiguration:"
+ "initWithConfigurationType:photoLibraryIdentifier:"
+ "initWithData:frame:zPosition:identifier:"
+ "initWithDescriptorType:media:photoLibraryIdentifier:"
+ "initWithImageAtURL:"
+ "initWithImageSize:deviceResolution:parallaxPadding:visibleFrame:adaptiveVisibleFrame:inactiveFrame:adaptiveInactiveTopFrame:spatialVisibleFrame:spatialAdaptiveFrame:timeFrame:adaptiveTimeFrame:salientContentFrame:clockLayerOrder:clockIntersection:layoutVariant:hasTopEdgeContact:maxClockShift:debugLayouts:"
+ "initWithImageSize:deviceResolution:parallaxPadding:visibleFrame:adaptiveVisibleFrame:inactiveFrame:adaptiveInactiveTopFrame:timeFrame:clockLayerOrder:clockIntersection:layoutVariant:hasTopEdgeContact:maxClockShift:debugLayouts:"
+ "initWithLayers:layout:depthEnabled:parallaxDisabled:clockAreaLuminance:settlingEffectEnabled:spatialPhotoEnabled:"
+ "initWithLossyCompressionQuality:"
+ "initWithPointSpaceSortedTimeRectss:screenScale:"
+ "initWithPosterClassification:initialRect:imageSize:effectiveAcceptableRect:effectivePreferredRect:validBoundsNormalized:headroomFeasible:hasTopEdgeContact:computeSpatial:spatialPadding:layoutType:allowedLayoutStrategies:layoutConfiguration:"
+ "initWithSceneData:scene:frame:zPosition:identifier:"
+ "initWithVisibleRect:adaptiveVisibleRect:cropScore:layoutScore:clockOverlapAcceptable:headroomEngaged:adaptiveHeadroom:maxClockShift:layoutVariant:notificationRoom:"
+ "intermediateWithAdaptiveStrategy:intermediate:"
+ "intermediateWithSpatialStrategy:intermediate:"
+ "isAdaptiveLayout"
+ "isSpatialPhoto"
+ "isSpatialPhotoAvailable"
+ "isSpatialPhotoEnabled"
+ "landscapeAdaptiveTimeFrame"
+ "landscapeAdaptiveVisibleFrame"
+ "layerStackByUpdatingSpatialPhotoEnabled:"
+ "layerStackURL != nil"
+ "layers != nil"
+ "layoutByUpdatingAdaptiveInactiveFrame:"
+ "layoutByUpdatingAdaptiveTimeFrame:"
+ "layoutByUpdatingAdaptiveVisibleFrame:"
+ "layoutByUpdatingLayoutVariant:"
+ "layoutByUpdatingMaxClockShift:"
+ "layoutByUpdatingNormalizedAdaptiveTimeFrame:"
+ "layoutByUpdatingNormalizedAdaptiveVisibleFrame:"
+ "layoutByUpdatingNormalizedPortraitAdaptiveTimeFrame:landscapeAdaptiveTimeFrame:"
+ "layoutByUpdatingNormalizedPortraitAdaptiveVisibleFrame:landscapeAdaptiveVisibleFrame:"
+ "layoutByUpdatingNormalizedVisibleFrame:remapAdaptiveVisibleFrame:"
+ "layoutVariant"
+ "lossyCompressionQuality"
+ "maxClockShift"
+ "maxStrechAmountNormalized"
+ "maxTimeRect"
+ "maxTimeRectInImageSpace"
+ "maximumLongSideLength"
+ "mediaMetadataType"
+ "mediaMetadataValue"
+ "metadataNeedsProcessing:"
+ "minTimeRect"
+ "minTimeRectInImageSpace"
+ "mxi"
+ "nearestRectForPointSpaceHeight:"
+ "normalizedAdaptiveTimeFrame"
+ "normalizedAdaptiveTimeFrameInVisibleFrame"
+ "normalizedAdaptiveVisibleFrame"
+ "normalizedLandscapeAdaptiveTimeFrame"
+ "normalizedLandscapeAdaptiveVisibleFrame"
+ "notificationRoom"
+ "originalImageExtent"
+ "photoLibraryIdentifier"
+ "policies"
+ "policyList"
+ "policyWithAccessibilityDescription:"
+ "policyWithAllowLocation:"
+ "policyWithCaption:"
+ "policyWithCreationDate:inTimeZone:"
+ "policyWithKey:value:"
+ "policyWithLocation:"
+ "policyWithLossyCompressionQuality:"
+ "policyWithPolicies:"
+ "processMetadata:"
+ "quickTimeUserDataMultitrackMemoryMovieType"
+ "quicktimeMetadataCinematicVideoIntent"
+ "s"
+ "sRGB"
+ "salientContentFrame"
+ "salientContentRect"
+ "scene"
+ "sceneData"
+ "scoreBonusAdaptiveWithLayoutType:"
+ "scoreBonusOverlapStretchWithLayoutType:"
+ "setAdaptiveInactiveTopRect:"
+ "setAdaptiveStrategy:"
+ "setAdaptiveVisibleRect:"
+ "setAdditionalTitleLabelHeight:"
+ "setAllowedClockStretch:"
+ "setAllowedLayoutStrategies:"
+ "setApplyTransform:"
+ "setColorBehavior:"
+ "setCropScore:"
+ "setHasSidebarContents:"
+ "setHasTopEdgeContact:"
+ "setHeadroomStrategy:"
+ "setImageURL:"
+ "setInactiveRect:"
+ "setInactiveStrategy:"
+ "setIncludeDerivativeDefaults:"
+ "setIncludeHDRGainMaps:"
+ "setIsSpatialPhotoAvailable:"
+ "setIsSpatialPhotoEnabled:"
+ "setLayoutScore:"
+ "setLayoutVariant:"
+ "setLossyCompressionQuality:"
+ "setMaxClockShift:"
+ "setMaximumLongSideLength:"
+ "setNormalizedAdaptiveTimeFrame:"
+ "setNormalizedAdaptiveVisibleFrame:"
+ "setNormalizedLandscapeAdaptiveTimeFrame:"
+ "setNormalizedLandscapeAdaptiveVisibleFrame:"
+ "setOverlapStrategy:"
+ "setParallaxStrategy:"
+ "setPolicies:"
+ "setSalientContentRect:"
+ "setSkipMetadata:"
+ "setSpatialAdaptiveVisibleRect:"
+ "setSpatialStrategy:"
+ "setSpatialVisibleRect:"
+ "setTimeBottomOverlap:"
+ "setTimeTopOverlap:"
+ "setUninflatedUnsafeAreaOverlap:"
+ "setUnsafeAreaOverlap:"
+ "setUserAdjustedTitleLabelHeightOffset:"
+ "setVisibleRect:"
+ "setZoomFactor:"
+ "setZoomStrategy:"
+ "skipMetadata"
+ "sortedTimeRects"
+ "spatial-photo-background"
+ "spatial-photo-foreground"
+ "spatial-photo-inactive-data"
+ "spatialAdaptiveFrame"
+ "spatialAdaptiveVisibleRect"
+ "spatialPadding"
+ "spatialPhotoBackgroundLayer"
+ "spatialPhotoEnabled"
+ "spatialPhotoForegroundLayer"
+ "spatialPhotoGatingFailures"
+ "spatialPhotoLayout"
+ "spatialStrategy"
+ "spatialVisibleFrame"
+ "spatialVisibleRect"
+ "spatial_photo_available"
+ "spatial_photo_enabled"
+ "spatialocclusion"
+ "specificConfigurationWithPortraitTitleBounds:portraitScreenSize:landscapeScreenSize:"
+ "standardPolicy"
+ "stretch"
+ "stretchedTimeOverlapCheckBottom:visibleFrame:"
+ "stretchedTimeOverlapCheckTop:visibleFrame:"
+ "targetCenterZoomFactorWithLayoutType:"
+ "timeOverlapCheckBottomForTimeRect:"
+ "timeOverlapCheckTopForTimeRect:"
+ "timeRectCollectionLandscape"
+ "timeRectCollectionPortrait"
+ "timeRectForNormalizedHeight:"
+ "topFrameForVisibleRect:adaptiveRect:"
+ "topFrameFromVisibleRectAspectRatio:adaptiveRect:"
+ "typeRequiresRasterization:"
+ "u"
+ "updateWithConfiguration:"
+ "userAdjustedTitleLabelHeightOffset"
+ "v16@?0@\"PFParallaxMutableIntermediateLayout\"8"
+ "v24@?0d8d16"
+ "valueWithRect:"
+ "widgetZoneAdjustmentForVisibleFrame:essentialRect:"
+ "zoomFactor"
+ "{%.2f, %.2f}"
+ "{?={CGRect={CGPoint=dd}{CGSize=dd}}{CGRect={CGPoint=dd}{CGSize=dd}}{CGRect={CGPoint=dd}{CGSize=dd}}{CGRect={CGPoint=dd}{CGSize=dd}}}120@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48d80{CGRect={CGPoint=dd}{CGSize=dd}}88"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}120@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48{CGSize=dd}80@96Q104d112"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8d16"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}56@0:8d16{CGRect={CGPoint=dd}{CGSize=dd}}24"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16d48"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}72@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48^{CGRect={CGPoint=dd}{CGSize=dd}}56d64"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}80@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48"
+ "{unique_ptr<boost::interprocess::basic_managed_mapped_file<char, boost::interprocess::rbtree_best_fit<boost::interprocess::null_mutex_family>, boost::interprocess::iset_index>, std::default_delete<boost::interprocess::basic_managed_mapped_file<char, boost::interprocess::rbtree_best_fit<boost::interprocess::null_mutex_family>, boost::interprocess::iset_index>>>=\"__ptr_\"^v}"
+ "{unique_ptr<pf::ArchiveLineParser, std::default_delete<pf::ArchiveLineParser>>=^{ArchiveLineParser}}24@0:8@\"NSString\"16"
+ "{unique_ptr<pf::ArchiveLineParser, std::default_delete<pf::ArchiveLineParser>>=^{ArchiveLineParser}}24@0:8@16"
- "%@ vis:%.0f,%.0f %.0fx%.0f stub:%@ z:%@ o:%@ p:%@ i:%@ scores, crop:%.2f layout:%.2f bot:%.2f top:%.2f unsafe:%.2f uninfunsafe:%.2f"
- "&"
- "/AppleInternal/Library/BuildRoots/24f0c819-1ca3-11f0-bc1f-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/boost/geometry/index/detail/exception.hpp"
- "<%@ %p; identifier: %@; options: %ld; media: %@; edit configuration: %@; shuffle configuration: %@ layout configuration: %@ user info: %@>"
- "<%@ %p; style: %@; norm. visible frame: %@; land. norm. visible frame: %@; zoom: %@; depth: %@|%@; settle: %@|%@>"
- "<%@:%p %0.0fx%0.0f depth:%d parallax:%d settling:%d layers:%@ layout:%@>"
- "@\"PFAVReaderWriter\""
- "@184@0:8{CGSize=dd}16{CGSize=dd}32{CGSize=dd}48{CGRect={CGPoint=dd}{CGSize=dd}}64{CGRect={CGPoint=dd}{CGSize=dd}}96{CGRect={CGPoint=dd}{CGSize=dd}}128@160Q168@176"
- "@188@0:8{CGSize=dd}16{CGSize=dd}32{CGSize=dd}48{CGRect={CGPoint=dd}{CGSize=dd}}64{CGRect={CGPoint=dd}{CGSize=dd}}96{CGRect={CGPoint=dd}{CGSize=dd}}128@160Q168B176@180"
- "@192@0:8Q16{CGRect={CGPoint=dd}{CGSize=dd}}24{CGSize=dd}56{CGRect={CGPoint=dd}{CGSize=dd}}72{CGRect={CGPoint=dd}{CGSize=dd}}104{CGRect={CGPoint=dd}{CGSize=dd}}136B168B172Q176@184"
- "@52@0:8@16@24B32B36d40B48"
- "Exception while serializing layer stack contents: %@"
- "Failed to load video at url: %@"
- "No intermediate layouts available to be scored, falling back to initial layout. Counts: headroom=%tu, zoom=%tu, overlap=%tu, parallax=%tu, inactive=%tu"
- "PFAVReaderWriterAdjustDelegate"
- "PFColorConverter"
- "PFColorConverter-adjustPixelBuffer"
- "PFColorConverterErrorDomain"
- "PI_DISABLE_HEADROOM"
- "PI_POSTER_DISABLE_CROP_VARIANT"
- "UNKNOWN(%lu)"
- "Unable to check for presence of embedded preview: failed to resolved DNG type."
- "Unknown bitmask description (%lu)"
- "_conversionContext"
- "_readerWriter"
- "convertWithVideoURL:outURL:progress:completion:"
- "defaultRasterizationDPI"
- "imageWithCVPixelBuffer:options:"
- "initWithImageSize:deviceResolution:parallaxPadding:visibleFrame:inactiveFrame:timeFrame:clockLayerOrder:clockIntersection:debugLayouts:"
- "initWithImageSize:deviceResolution:parallaxPadding:visibleFrame:inactiveFrame:timeFrame:clockLayerOrder:clockIntersection:hasTopEdgeContact:debugLayouts:"
- "initWithLayers:layout:depthEnabled:parallaxDisabled:clockAreaLuminance:settlingEffectEnabled:"
- "initWithPosterClassification:initialRect:imageSize:effectiveAcceptableRect:effectivePreferredRect:validBoundsNormalized:headroomFeasible:hasTopEdgeContact:layoutType:layoutConfiguration:"
- "render:toCVPixelBuffer:bounds:colorSpace:"
- "typeRequiresRasterizationDPI:"
- "v24@0:8^{__CVBuffer=}16"
- "v32@0:8^{__CVBuffer=}16^{__CVBuffer=}24"
- "{unique_ptr<boost::interprocess::basic_managed_mapped_file<char, boost::interprocess::rbtree_best_fit<boost::interprocess::null_mutex_family>, boost::interprocess::iset_index>, std::default_delete<boost::interprocess::basic_managed_mapped_file<char, boost::interprocess::rbtree_best_fit<boost::interprocess::null_mutex_family>, boost::interprocess::iset_index>>>=\"__ptr_\"{__compressed_pair<boost::interprocess::basic_managed_mapped_file<char, boost::interprocess::rbtree_best_fit<boost::interprocess::null_mutex_family>, boost::interprocess::iset_index> *, std::default_delete<boost::interprocess::basic_managed_mapped_file<char, boost::interprocess::rbtree_best_fit<boost::interprocess::null_mutex_family>, boost::interprocess::iset_index>>>=\"__value_\"^v}}"
- "{unique_ptr<pf::ArchiveLineParser, std::default_delete<pf::ArchiveLineParser>>={__compressed_pair<pf::ArchiveLineParser *, std::default_delete<pf::ArchiveLineParser>>=^{ArchiveLineParser}}}24@0:8@\"NSString\"16"
- "{unique_ptr<pf::ArchiveLineParser, std::default_delete<pf::ArchiveLineParser>>={__compressed_pair<pf::ArchiveLineParser *, std::default_delete<pf::ArchiveLineParser>>=^{ArchiveLineParser}}}24@0:8@16"

```
