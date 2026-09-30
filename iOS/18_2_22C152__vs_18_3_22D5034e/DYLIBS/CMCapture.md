## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`

```diff

-587.62.18.0.0
-  __TEXT.__text: 0x503f24
-  __TEXT.__auth_stubs: 0x4db0
-  __TEXT.__objc_methlist: 0x2a5ac
-  __TEXT.__const: 0x1504f8
-  __TEXT.__cstring: 0x71fb0
-  __TEXT.__oslogstring: 0x24e00
-  __TEXT.__gcc_except_tab: 0x28c0
+587.80.7.0.1
+  __TEXT.__text: 0x506598
+  __TEXT.__auth_stubs: 0x4dc0
+  __TEXT.__objc_methlist: 0x2a784
+  __TEXT.__const: 0x150508
+  __TEXT.__cstring: 0x7246f
+  __TEXT.__oslogstring: 0x24ea5
+  __TEXT.__gcc_except_tab: 0x28b0
   __TEXT.__dlopen_cstrs: 0x686
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0xbed0
-  __TEXT.__objc_classname: 0x7562
-  __TEXT.__objc_methname: 0x91946
-  __TEXT.__objc_methtype: 0x139af
-  __TEXT.__objc_stubs: 0x3f4e0
-  __DATA_CONST.__got: 0x5f00
-  __DATA_CONST.__const: 0x97a0
-  __DATA_CONST.__objc_classlist: 0x18a8
+  __TEXT.__unwind_info: 0xbf48
+  __TEXT.__objc_classname: 0x75c4
+  __TEXT.__objc_methname: 0x91e8e
+  __TEXT.__objc_methtype: 0x139e3
+  __TEXT.__objc_stubs: 0x3f760
+  __DATA_CONST.__got: 0x5ef0
+  __DATA_CONST.__const: 0x97f8
+  __DATA_CONST.__objc_classlist: 0x18c0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x4e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x120c0
+  __DATA_CONST.__objc_selrefs: 0x12168
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0x1720
-  __DATA_CONST.__objc_arraydata: 0x3568
-  __AUTH_CONST.__auth_got: 0x26e8
+  __DATA_CONST.__objc_superrefs: 0x1738
+  __DATA_CONST.__objc_arraydata: 0x35d8
+  __AUTH_CONST.__auth_got: 0x26f0
   __AUTH_CONST.__auth_ptr: 0x90
-  __AUTH_CONST.__const: 0x3a90
-  __AUTH_CONST.__cfstring: 0x37880
-  __AUTH_CONST.__objc_const: 0x86308
-  __AUTH_CONST.__objc_intobj: 0x4e18
-  __AUTH_CONST.__objc_arrayobj: 0x2568
-  __AUTH_CONST.__objc_doubleobj: 0x9c0
-  __AUTH_CONST.__objc_floatobj: 0x220
+  __AUTH_CONST.__const: 0x3b10
+  __AUTH_CONST.__cfstring: 0x37ba0
+  __AUTH_CONST.__objc_const: 0x86830
+  __AUTH_CONST.__objc_intobj: 0x4e30
+  __AUTH_CONST.__objc_arrayobj: 0x2598
+  __AUTH_CONST.__objc_doubleobj: 0xa80
+  __AUTH_CONST.__objc_floatobj: 0x230
   __AUTH_CONST.__objc_dictobj: 0x1798
-  __AUTH.__objc_data: 0x730
-  __DATA.__objc_ivar: 0x9404
+  __AUTH.__objc_data: 0x820
+  __DATA.__objc_ivar: 0x943c
   __DATA.__data: 0x48f0
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x5e0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 20580
-  Symbols:   26241
-  CStrings:  36372
+  Functions: 20635
+  Symbols:   26294
+  CStrings:  36445
 
Symbols:
+ _bsearch
+ _kFigCaptureSourceAttributeKey_MetadataFrameRateControlSupported
- _OBJC_CLASS_$_BWMovingWindowStats
- _OBJC_CLASS_$_BWStats
- _OBJC_METACLASS_$_BWMovingWindowStats
- _OBJC_METACLASS_$_BWStats
CStrings:
+ "%@ movies:%d, suspended:%d, preserveSuspended:%d, movieDur:%.2fs, trim:%d, %lldfps, preparedID:%lld%@%@%@%@%@%@%@ maxQuality:%d%@%@%@%@%@%@%@%@%@"
+ "%@, median: %lf%@ over %lu samples"
+ ", (ApplyStandardSmartStyleForStillsWhenNoStyleRequested ON)"
+ ", targetFrameRate:%.2f"
+ "-[BWFigCaptureDeviceVendor registerClientWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithFlashlightAllowed:clientIsShareableFlashlight:deviceAvailabilityChangedHandler:]_block_invoke"
+ "-[BWHistogramStats addDataPointP:]"
+ "-[BWPhotonicEngineNode _handleSampleBufferForFocusPixelDisparityInputIfNeeded:]"
+ "/Cropper"
+ "0 <= foundIndex && foundIndex < _binsCount"
+ "<<<< BWInferenceSynchronizerNode >>>> %s: [%{private}@] Not synchronizing inferences (captureID:%{public}lld); %{public}@ frame: %{public}@"
+ "<<<< BWStillImageProcessingNode >>>> %s: Adding frame to focus pixel disparity input for captureID:%{public}lld: %{public}@"
+ "<<<< FigCapturePhotonicEngineSinkPipeline >>>> %s: Still Image PhotonicEngine Pipeline Configuration:%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@"
+ "<<<< FigFlashlight >>>> %s: %{public}s Created flashlight (%p), clientType: %@."
+ "<FigCaptureSession %@ retainCount: %ld%s allocator: %p>"
+ "@\"BWHistogramStats\""
+ "@\"BWMedianStats\""
+ "@56@0:8@16@24Q32Q40B48f52"
+ "ApplyStandardSmartStyleForStillsWhenNoStyleRequestedSupported"
+ "B24@0:8d16"
+ "BWHistogramStats"
+ "BWMedianStats"
+ "BWStillImageConditionalRouterFocusPixelDisparityInputConfiguration"
+ "Default/FocusPixel Sync"
+ "DeviceSharingWithFlashlightAllowed"
+ "Failed to determine denormalizedSourceCropRect, skipping Focus pixel disparity generation"
+ "Focus Pixel Disparity Input Frame Router"
+ "Histogram bins are invalid"
+ "Index out of range"
+ "Invalid median max number of samples"
+ "Invalid quantile count"
+ "MOC %p: <%@>%@ -> <%@> E:%d MetadataIdentifiers:{%@}%@%@%@%@%@%@%@%@%@%@"
+ "MetadataFrameRateControlSupported"
+ "Number of samples: %lld, min: %lf%@, max: %lf%@, average: %lf%@, standard deviation: %lf%@"
+ "SmartStyleRenderingEnabled"
+ "SoftISP Focus Pixel Disparity Input"
+ "SoftISP focus pixel disparity input frame"
+ "SoftISP focus pixel disparity input frame for '%@'"
+ "T@\"BWMedianStats\",C,N,V_videoFrameDurationStats"
+ "T@\"NSDictionary\",&,N,V_luxHistogram"
+ "TB,N,V_applyStandardSmartStyleForStillsWhenNoStyleRequested"
+ "TB,N,V_unstyledBufferEmitted"
+ "TB,R,GisApplyStandardSmartStyleForStillsWhenNoStyleRequestedSupported"
+ "TB,R,N,V_clientIsShareableFlashlight"
+ "TB,R,N,V_deviceSharingWithFlashlightAllowed"
+ "Td,R,N,V_estimatedMedian"
+ "Tf,N,V_medianLuxValue"
+ "Tf,N,V_objectDetectionTargetFrameRate"
+ "T{?=ii},N,V_deferredPhotoFinalRawThumbnailDimensions"
+ "T{?=ii},N,V_deferredPhotoFinalThumbnailDimensions"
+ "[super addNode:focusPixelDisparityInputOutputSynchronizer error:&error]"
+ "[super addNode:focusPixelDisparityInputRouterNode error:&error]"
+ "_applyStandardSmartStyleForStillsWhenNoStyleRequested"
+ "_areas"
+ "_bins"
+ "_binsCount"
+ "_clientIsShareableFlashlight"
+ "_counts"
+ "_currentZoomFactorForFocusPixelDisparityGenerator"
+ "_deferredPhotoFinalRawThumbnailDimensions"
+ "_deferredPhotoFinalThumbnailDimensions"
+ "_deviceSharingWithFlashlightAllowed"
+ "_estimatedMedian"
+ "_luxHistogram"
+ "_medianLuxValue"
+ "_unstyledBufferEmitted"
+ "addDataPointP:"
+ "alsLuxBin%@"
+ "applyStandardSmartStyleForStillsWhenNoStyleRequested"
+ "applyStandardSmartStyleForStillsWhenNoStyleRequestedSupported"
+ "clientID: %d, pid: %d, clientApplicationID: %@, clientDescription: %@, clientPriority: %@, canStealFromClientsWithSamePriority: %d, deviceSharingWithOtherClientsAllowed: %d, deviceSharingWithFlashlightAllowed: %d, clientIsShareableFlashlight: %d, handler: %p"
+ "clientIsShareableFlashlight"
+ "com.apple.coremedia.capture.stillimage.concurrent"
+ "com.blackmagic-design.DaVinciCamera"
+ "deferredPhotoFinalDimensions"
+ "deferredPhotoFinalRawThumbnailDimensions"
+ "deferredPhotoFinalRawThumbnailDimensionsHeight"
+ "deferredPhotoFinalRawThumbnailDimensionsWidth"
+ "deferredPhotoFinalThumbnailDimensions"
+ "deferredPhotoFinalThumbnailDimensionsHeight"
+ "deferredPhotoFinalThumbnailDimensionsWidth"
+ "description=CameraCapture-587.80.7.0.1"
+ "deviceSharingWithFlashlightAllowed"
+ "estimatedMedian"
+ "focusPixelDisparityInputConfiguration"
+ "focusPixelDisparityInputOutputIndex"
+ "focusPixelDisparityTuningParametersForPortType:sensorIDString:zoomFactor:"
+ "getEstimatedQuantiles:n:"
+ "histogramAsDictionary"
+ "initWithBins:"
+ "initWithMaxNumberOfSamplesForMedianCalculation:"
+ "initWithNodeConfiguration:sensorConfiguration:disparityMapWidth:disparityMapHeight:depthIsAlwaysHighQuality:defaultZoomFactor:"
+ "initWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithFlashlightAllowed:clientIsShareableFlashlight:deviceAvailabilityChangedHandler:"
+ "isApplyStandardSmartStyleForStillsWhenNoStyleRequestedSupported"
+ "luxHistogram"
+ "medianLuxValue"
+ "metadataFrameRateControlSupported"
+ "outputLinearRGBPixelBuffer"
+ "rawThumbnailDimensions"
+ "registerClientWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithFlashlightAllowed:clientIsShareableFlashlight:deviceAvailabilityChangedHandler:"
+ "registerClientWithPID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithFlashlightAllowed:clientIsShareableFlashlight:deviceAvailabilityChangedHandler:"
+ "setApplyStandardSmartStyleForStillsWhenNoStyleRequested:"
+ "setDeferredPhotoFinalRawThumbnailDimensions:"
+ "setDeferredPhotoFinalThumbnailDimensions:"
+ "setLuxHistogram:"
+ "setMedianLuxValue:"
+ "setObjectDetectionTargetFrameRate:forSessionID:"
+ "setOutputLinearRGBPixelBuffer:"
+ "setUnstyledBufferEmitted:"
+ "thumbnailDimensions"
+ "unstyledBufferEmitted"
+ "v28@0:8^d16i24"
- "%@ movies:%d, suspended:%d, preserveSuspended:%d, movieDur:%.2fs, trim:%d, %lldfps, preparedID:%lld%@%@%@%@%@%@%@ maxQuality:%d%@%@%@%@%@%@%@%@"
- ", median: %lf%@"
- "-[BWFigCaptureDeviceVendor registerClientWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithAVFlashlightAllowed:clientIsAVFlashlight:deviceAvailabilityChangedHandler:]_block_invoke"
- "<<<< BWInferenceSynchronizerNode >>>> %s: Not synchronizing inferences (captureID:%{public}lld); %{public}@ frame: %{public}@"
- "<<<< FigCapturePhotonicEngineSinkPipeline >>>> %s: Still Image PhotonicEngine Pipeline Configuration:%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@"
- "<<<< FigCaptureTempFileUtilities >>>> Fig"
- "<<<< FigFlashlight >>>> %s: %{public}s Created flashlight (%p)"
- "<FigCaptureSession %@ retainCount: %ld%s allocator: %p, "
- "@28@0:8B16q20"
- "@52@0:8@16@24Q32Q40B48"
- "DeviceSharingWithAVFlashlightAllowed"
- "FigCaptureTempFileUtilities.m"
- "MOC %p: <%@>%@ -> <%@> E:%d MetadataIdentifiers:{%@}%@%@%@%@%@%@%@%@%@"
- "Number of samples: %lld, min: %lf%@, max: %lf%@, average: %lf%@, standard deviation: %lf%@ %@"
- "T@\"BWStats\",C,N,V_videoFrameDurationStats"
- "TB,R,N,V_clientIsAVFlashlight"
- "TB,R,N,V_deviceSharingWithAVFlashlightAllowed"
- "Td,R,N,V_max"
- "Td,R,N,V_min"
- "Tq,N,V_nextDataPointIndex"
- "Unable to configure the FocusPixelDisparityGenerator"
- "_clientIsAVFlashlight"
- "_dataPoints"
- "_deviceSharingWithAVFlashlightAllowed"
- "_medianCalculationEnabled"
- "_nextDataPointIndex"
- "_numDataPoints"
- "_updateMetadataOutputWithoutDisabling"
- "clientID: %d, pid: %d, clientApplicationID: %@, clientDescription: %@, clientPriority: %@, canStealFromClientsWithSamePriority: %d, deviceSharingWithOtherClientsAllowed: %d, deviceSharingWithAVFlashlightAllowed: %d, clientIsAVFlashlight: %d, handler: %p"
- "clientIsAVFlashlight"
- "description=CameraCapture-587.62.18"
- "deviceSharingWithAVFlashlightAllowed"
- "focusPixelDisparityParametersForPortType:sensorIDString:"
- "initWithMedianCalculationEnabled:maxNumberOfSamplesForMedianCalculation:"
- "initWithNodeConfiguration:sensorConfiguration:disparityMapWidth:disparityMapHeight:depthIsAlwaysHighQuality:"
- "initWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithAVFlashlightAllowed:clientIsAVFlashlight:deviceAvailabilityChangedHandler:"
- "nextDataPointIndex"
- "registerClientWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithAVFlashlightAllowed:clientIsAVFlashlight:deviceAvailabilityChangedHandler:"
- "registerClientWithPID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithAVFlashlightAllowed:clientIsAVFlashlight:deviceAvailabilityChangedHandler:"
- "removeDataPoint:"
- "setNextDataPointIndex:"

```
