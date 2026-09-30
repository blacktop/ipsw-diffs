## MediaAnalysis

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis`

```diff

-460.7.1.0.0
-  __TEXT.__text: 0x4bf358
+460.8.2.0.0
+  __TEXT.__text: 0x4c518c
   __TEXT.__delay_stubs: 0xc0
   __TEXT.__delay_helper: 0x284
-  __TEXT.__objc_methlist: 0x22c98
+  __TEXT.__objc_methlist: 0x22d60
   __TEXT.__const: 0x16608
-  __TEXT.__gcc_except_tab: 0x67b94
-  __TEXT.__cstring: 0x2cac1
-  __TEXT.__oslogstring: 0x329bb
+  __TEXT.__gcc_except_tab: 0x686bc
+  __TEXT.__cstring: 0x2cd21
+  __TEXT.__oslogstring: 0x3312b
   __TEXT.__dlopen_cstrs: 0x4b8
   __TEXT.__ustring: 0x40
   __TEXT.__swift5_typeref: 0x9dc

   __TEXT.__swift_as_ret: 0x90
   __TEXT.__swift_as_cont: 0xd8
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x187d8
+  __TEXT.__unwind_info: 0x18938
   __TEXT.__eh_frame: 0x1a30
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7c80
-  __DATA_CONST.__objc_classlist: 0x15b8
+  __DATA_CONST.__const: 0x7c18
+  __DATA_CONST.__objc_classlist: 0x15c0
   __DATA_CONST.__objc_catlist: 0x1c8
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xf128
+  __DATA_CONST.__objc_selrefs: 0xf198
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0xfa0
+  __DATA_CONST.__objc_superrefs: 0xfa8
   __DATA_CONST.__objc_arraydata: 0x12c8
-  __DATA_CONST.__got: 0x2550
-  __AUTH_CONST.__const: 0x75c8
-  __AUTH_CONST.__cfstring: 0x1ea20
-  __AUTH_CONST.__objc_const: 0x41ba0
+  __DATA_CONST.__got: 0x2578
+  __AUTH_CONST.__const: 0x75e8
+  __AUTH_CONST.__cfstring: 0x1eb80
+  __AUTH_CONST.__objc_const: 0x41de8
   __AUTH_CONST.__weak_auth_got: 0x80
-  __AUTH_CONST.__objc_floatobj: 0x2f0
+  __AUTH_CONST.__objc_floatobj: 0x300
   __AUTH_CONST.__objc_arrayobj: 0xd08
   __AUTH_CONST.__objc_doubleobj: 0x490
-  __AUTH_CONST.__objc_intobj: 0x38d0
+  __AUTH_CONST.__objc_intobj: 0x3930
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__auth_got: 0x2580
-  __AUTH.__objc_data: 0x2f0
-  __AUTH.__data: 0x118
+  __AUTH_CONST.__auth_got: 0x2590
+  __AUTH.__objc_data: 0x50
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x10
-  __DATA.__objc_ivar: 0x36ac
-  __DATA.__data: 0x2010
+  __DATA.__objc_ivar: 0x36e0
+  __DATA.__data: 0xfb0
   __DATA.__common: 0x3c1
-  __DATA_DIRTY.__objc_data: 0xdc28
-  __DATA_DIRTY.__data: 0x2b8
-  __DATA_DIRTY.__bss: 0x938
+  __DATA_DIRTY.__objc_data: 0xdf18
+  __DATA_DIRTY.__data: 0x1410
+  __DATA_DIRTY.__bss: 0x958
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 20149
-  Symbols:   34844
-  CStrings:  8970
+  Functions: 20216
+  Symbols:   34899
+  CStrings:  9018
 
Symbols:
+ +[PHPhotoLibrary(MediaAnalysis) mad_isInitialAnalysisPass]
+ +[VCPMovieAssetWriter assetWriterWithURL:andTrack:andBitrate:withOutputSize:enableAudio:enableStyle:hasStyleApplied:enableTextureStyle:]
+ -[MADTextureStyleMetaAnalyzer .cxx_destruct]
+ -[MADTextureStyleMetaAnalyzer initWithRequestAnalyses:formatDescription:]
+ -[MADTextureStyleMetaAnalyzer privateResults]
+ -[MADTextureStyleMetaAnalyzer processMetadataGroup:flags:]
+ -[VCPMovieAssetWriter addSkinPixelBuffer:withTime:withAttachment:]
+ -[VCPMovieAssetWriter addTextureStyleInfoData:timerange:]
+ -[VCPMovieAssetWriter initWithURL:andTrack:andBitrate:withOutputSize:enableAudio:enableStyle:hasStyleApplied:enableTextureStyle:]
+ -[VCPMovieAssetWriter popSkinSample]
+ -[VCPMovieAssetWriter pushSkinSample:]
+ -[VCPMovieAssetWriter setupSkinTrack]
+ -[VCPVideoInterpolator createMetadataItem:identifier:timerange:]
+ -[VCPVideoInterpolator createSkinTrackDecoder:timerange:]
+ -[VCPVideoInterpolator createTextureStyleInfoMetadata:timerange:]
+ -[VCPVideoInterpolator deserializeMetadata:faceROIs:]
+ -[VCPVideoInterpolator enableTextureStyle]
+ -[VCPVideoInterpolator faceROIRect:fromDictionary:]
+ -[VCPVideoInterpolator findIntraFrameList:into:]
+ -[VCPVideoInterpolator hasIntraFrameAtEndBoundary]
+ -[VCPVideoInterpolator interpolateSkinMap]
+ _CMFormatDescriptionGetExtension
+ _MediaAnalysisMetaTSInfoResultsKey
+ _MediaAnalysisMetaTSResultsKey
+ _NSClassFromString
+ _OBJC_CLASS_$_MADTextureStyleMetaAnalyzer
+ _OBJC_IVAR_$_MADTextureStyleMetaAnalyzer._results
+ _OBJC_IVAR_$_VCPMovieAssetWriter._enableTextureStyle
+ _OBJC_IVAR_$_VCPMovieAssetWriter._skinDequeueSemaphore
+ _OBJC_IVAR_$_VCPMovieAssetWriter._skinEnqueueSemaphore
+ _OBJC_IVAR_$_VCPMovieAssetWriter._skinInput
+ _OBJC_IVAR_$_VCPMovieAssetWriter._skinQueue
+ _OBJC_IVAR_$_VCPMovieAssetWriter._skinsampleQueue
+ _OBJC_IVAR_$_VCPMovieAssetWriter._textureStyleInfoAdaptor
+ _OBJC_IVAR_$_VCPVideoInterpolator._enableTextureStyle
+ _OBJC_IVAR_$_VCPVideoInterpolator._previousTextureStyleMetadata
+ _OBJC_IVAR_$_VCPVideoInterpolator._stylesMetadataInterpolator
+ _OBJC_IVAR_$_VCPVideoInterpolator._textureStyleMetadata
+ _OBJC_IVAR_$_VCPVideoInterpolator._videoOutputTimeline
+ _OBJC_METACLASS_$_MADTextureStyleMetaAnalyzer
+ __OBJC_$_INSTANCE_METHODS_MADTextureStyleMetaAnalyzer
+ __OBJC_$_INSTANCE_VARIABLES_MADTextureStyleMetaAnalyzer
+ __OBJC_CLASS_RO_$_MADTextureStyleMetaAnalyzer
+ __OBJC_METACLASS_RO_$_MADTextureStyleMetaAnalyzer
+ __ZZ58+[PHPhotoLibrary(MediaAnalysis) mad_isInitialAnalysisPass]E21isInitialAnalysisPass
+ __ZZ58+[PHPhotoLibrary(MediaAnalysis) mad_isInitialAnalysisPass]E4once
+ ___58+[PHPhotoLibrary(MediaAnalysis) mad_isInitialAnalysisPass]_block_invoke
+ _kCMITextureStylesPersonInputDataKey_faceID
+ _kCMITextureStylesPersonInputDataKey_faceROI
+ _kVTCompressionPropertyKey_MaximumRealTimeFrameRate
+ _kVTProfileLevel_HEVC_Monochrome_AutoLevel
+ _objc_msgSend$addSkinPixelBuffer:withTime:withAttachment:
+ _objc_msgSend$addTextureStyleInfoData:timerange:
+ _objc_msgSend$assetWriterWithURL:andTrack:andBitrate:withOutputSize:enableAudio:enableStyle:hasStyleApplied:enableTextureStyle:
+ _objc_msgSend$createMetadataItem:identifier:timerange:
+ _objc_msgSend$createSkinTrackDecoder:timerange:
+ _objc_msgSend$createTextureStyleInfoMetadata:timerange:
+ _objc_msgSend$deserializeMetadata:faceROIs:
+ _objc_msgSend$faceROIRect:fromDictionary:
+ _objc_msgSend$findIntraFrameList:into:
+ _objc_msgSend$getReturnValue:
+ _objc_msgSend$hasIntraFrameAtEndBoundary
+ _objc_msgSend$initWithOptionalMetalCommandQueue:
+ _objc_msgSend$initWithURL:andTrack:andBitrate:withOutputSize:enableAudio:enableStyle:hasStyleApplied:enableTextureStyle:
+ _objc_msgSend$interpolateSkinMap
+ _objc_msgSend$mad_isInitialAnalysisPass
+ _objc_msgSend$popSkinSample
+ _objc_msgSend$pushSkinSample:
+ _objc_msgSend$setExpectsMediaDataInRealTime:
+ _objc_msgSend$setupSkinTrack
- +[PHAssetResourceManager(MediaAnalysis) vcp_inMemoryDownload:withTaskID:toData:cancel:]
- +[VCPMovieAssetWriter assetWriterWithURL:andTrack:andBitrate:withOutputSize:enableAudio:enableStyle:hasStyleApplied:]
- -[VCPMovieAssetWriter initWithURL:andTrack:andBitrate:withOutputSize:enableAudio:enableStyle:hasStyleApplied:]
- -[VCPVideoInterpolator deserializeMetadata:]
- -[VCPVideoInterpolator findIntraFrameList:]
- __ZZ44+[VCPVideoInterpolator processTextureStyles]E13textureStyles
- ___87+[PHAssetResourceManager(MediaAnalysis) vcp_inMemoryDownload:withTaskID:toData:cancel:]_block_invoke
- ___block_descriptor_40_e8_32s_e16_v16?0"NSData"8ls32l8
- ___block_descriptor_40_e8_32s_e8_v16?0d8ls32l8
- ___block_descriptor_64_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
- _objc_msgSend$assetWriterWithURL:andTrack:andBitrate:withOutputSize:enableAudio:enableStyle:hasStyleApplied:
- _objc_msgSend$deserializeMetadata:
- _objc_msgSend$findIntraFrameList:
- _objc_msgSend$initWithURL:andTrack:andBitrate:withOutputSize:enableAudio:enableStyle:hasStyleApplied:
- _objc_msgSend$interpolateCoefficientsFromStartFrameMetadataDict:startFrameTime:endFrameMetadataDict:endFrameTime:frameTimesToInterpolate:
CStrings:
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/MediaAnalysis/TextureStyleMetaAnalyzer.mm"
+ "CMIStylesMetadataInterpolator"
+ "Failed to append texturestyle-info at %.6f"
+ "Failed to create skin map decoder"
+ "Failed to create skin map writer input"
+ "Failed to splice the skin map segment (%@)"
+ "Failed to start FRC session for the skin map at usage %ld"
+ "Interpolated facebox %u has no usable faceROI, keys %@"
+ "MADInterpolatedFaceROIs"
+ "MetaTSInfoResults"
+ "MetaTSResults"
+ "Missing texture style metadata"
+ "No recorded video output timeline to follow"
+ "No skin map track on a texture styled asset"
+ "No skin map track to interpolate on a texture styled asset"
+ "No skin map writer input to append to"
+ "No texturestyle-info track to append to"
+ "Number of frames inconsistent with texture style metadata"
+ "Skin interpolation returned %lu frames for %lu expected between anchors %lu and %lu (%@)"
+ "Skin map %.0fx%.0f has no FRC usage"
+ "Skin map frame count does not match the video track timeline"
+ "Skin map ran out of samples at timeline entry %lu of %lu"
+ "Skin map sample %lu carries no image buffer"
+ "Skin map segment 1 is %.4f but video is %.4f"
+ "Skin map through the processed segment is %.4f but video is %.4f"
+ "Skin map track has %lu format descriptions"
+ "Styles metadata interpolation returned %lu results for %lu inserted frames over the gap at %.6f, payloads %@"
+ "Styles metadata interpolation returned no SmartStyle coefficients"
+ "Texture style enabled but the skin map is missing (processed %d, composition %d, original %d)"
+ "Texture style enabled but the texturestyle-info track is missing (processed %d, composition %d, original %d)"
+ "Video output timeline has %lu entries for %lu insertion points"
+ "[FRC] Failed to end the skin map FRC session"
+ "[FRC] Failed to read the sync samples of track %d"
+ "[FRC] Skin inserted frame %lu of pair %lu at %.6f, video track used %.6f"
+ "[FRC] Skin map encoding aborted"
+ "[FRC] Skin map encoding failed"
+ "[FRC] Skin map encoding finished"
+ "[FRC] Skipping asset: CMIStylesMetadataInterpolator %s"
+ "[FRC] Skipping asset: texturestyle-info without a style or a skin map"
+ "[MediaAnalysis] [MADTextureStyleMetaAnalyzer] Read %lu texture style info samples"
+ "[MediaAnalysis] [MADTextureStyleMetaAnalyzer] Texture style item carries no value"
+ "anchor"
+ "class not found"
+ "com.apple.mediaanalysisd.movieassetwriter.mediaDataRequest.skinEncoding"
+ "faceROIs"
+ "has no initialiser"
+ "has no interpolation method"
+ "inserted"
+ "interpolateStylesMetadataFromStartFrameMetadataDict:startFrameTime:endFrameMetadataDict:endFrameTime:frameTimesToInterpolate:"
+ "mdta/com.apple.quicktime.texturestyle-info"
+ "smartStyleMetadata"
+ "textureStyleMetadata"
- "Attempt to download resource: %@"
- "Cancelling download (ID:%d)"
- "Download resource timed-out (ID:%d)"
- "[%@] Download progress: %.2f"
```
