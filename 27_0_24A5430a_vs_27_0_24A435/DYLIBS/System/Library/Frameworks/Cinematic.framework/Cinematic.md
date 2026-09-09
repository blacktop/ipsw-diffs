## Cinematic

> `/System/Library/Frameworks/Cinematic.framework/Cinematic`

```diff

 560.22.2.0.0
-  __TEXT.__text: 0x142f4
-  __TEXT.__objc_methlist: 0xeb4
-  __TEXT.__cstring: 0x369
-  __TEXT.__const: 0x9d8
-  __TEXT.__oslogstring: 0x98f
-  __TEXT.__gcc_except_tab: 0x2c0
-  __TEXT.__constg_swiftt: 0x5b0
-  __TEXT.__swift5_typeref: 0x332
-  __TEXT.__swift5_reflstr: 0x22d
-  __TEXT.__swift5_fieldmd: 0x338
-  __TEXT.__swift5_builtin: 0xa0
+  __TEXT.__text: 0x20dac
+  __TEXT.__objc_methlist: 0x1194
+  __TEXT.__cstring: 0x5c1
+  __TEXT.__const: 0xb08
+  __TEXT.__oslogstring: 0x1390
+  __TEXT.__gcc_except_tab: 0x9a0
+  __TEXT.__constg_swiftt: 0x644
+  __TEXT.__swift5_typeref: 0x3c2
+  __TEXT.__swift5_reflstr: 0x23d
+  __TEXT.__swift5_fieldmd: 0x354
+  __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x38
-  __TEXT.__swift5_types: 0x60
-  __TEXT.__swift_as_entry: 0x2c
-  __TEXT.__swift_as_ret: 0x24
-  __TEXT.__swift_as_cont: 0x48
+  __TEXT.__swift5_types: 0x68
+  __TEXT.__swift_as_entry: 0x48
+  __TEXT.__swift_as_ret: 0x40
+  __TEXT.__swift_as_cont: 0x80
+  __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x848
-  __TEXT.__eh_frame: 0x448
+  __TEXT.__unwind_info: 0xb98
+  __TEXT.__eh_frame: 0x910
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6e0
-  __DATA_CONST.__objc_classlist: 0xe0
+  __DATA_CONST.__const: 0xab0
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb78
+  __DATA_CONST.__objc_selrefs: 0xfd0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x90
-  __DATA_CONST.__objc_arraydata: 0x58
-  __DATA_CONST.__got: 0x2d0
-  __AUTH_CONST.__const: 0x850
-  __AUTH_CONST.__cfstring: 0x180
-  __AUTH_CONST.__objc_const: 0x1ee0
-  __AUTH_CONST.__objc_arrayobj: 0x48
+  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_arraydata: 0x68
+  __DATA_CONST.__got: 0x470
+  __AUTH_CONST.__const: 0x988
+  __AUTH_CONST.__cfstring: 0x1e0
+  __AUTH_CONST.__objc_const: 0x26f0
+  __AUTH_CONST.__objc_arrayobj: 0x78
+  __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH_CONST.__auth_got: 0x4e0
-  __AUTH.__objc_data: 0x5f0
-  __AUTH.__data: 0x840
-  __DATA.__objc_ivar: 0x98
-  __DATA.__data: 0x2c8
+  __AUTH_CONST.__auth_got: 0x6a8
+  __AUTH.__objc_data: 0x780
+  __AUTH.__data: 0x918
+  __DATA.__objc_ivar: 0x10c
+  __DATA.__data: 0x2f8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /System/Library/PrivateFrameworks/CinematicUtil.framework/CinematicUtil
   - /System/Library/PrivateFrameworks/Portrait.framework/Portrait
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 755
-  Symbols:   1293
-  CStrings:  84
+  Functions: 1020
+  Symbols:   1696
+  CStrings:  161
 
Symbols:
+ +[CNAssetInfo _allRenderingConfigurationsForResourceVersions:]
+ +[CNAssetInfo _allResourceVersions]
+ +[CNAssetInfo _downloadResourcesForMonocularDisparitySettings:timeout:completionHandler:]
+ +[CNAssetInfo _getCNDisparityResourceStatusForAssetInfo:callback:]
+ +[CNAssetInfo checkCinematicCapabilityForAsset:completionHandler:]
+ +[CNAssetInfo defaultResourceDownloadTimeout]
+ +[CNAssetInfo downloadResourcesForVersions:timeout:completionHandler:]
+ +[CNAssetInfo resourceStatusForVersions:]
+ +[CNAssetPreprocess preprocessAssetWithConfiguration:sourceAsset:completionHandler:]
+ -[CNAssetInfo cinematicCapability]
+ -[CNAssetInfo downloadResourcesWithTimeout:completionHandler:]
+ -[CNAssetInfo isPreprocessed]
+ -[CNAssetInfo preprocessAssetWithConfiguration:completionHandler:]
+ -[CNAssetInfo preprocessed]
+ -[CNAssetInfo resourceStatus]
+ -[CNAssetInfo setCinematicCapability:]
+ -[CNAssetInfo setPreprocessed:]
+ -[CNAssetInfo setResourceStatus:]
+ -[CNAssetPreprocess .cxx_destruct]
+ -[CNAssetPreprocess checkPreconditions]
+ -[CNAssetPreprocess createTemporaryMovURL]
+ -[CNAssetPreprocess dealloc]
+ -[CNAssetPreprocess initWithProgress:sourceAsset:configuration:]
+ -[CNAssetPreprocess loadAssetInfoFromAsset:assetInfo:]
+ -[CNAssetPreprocess loadGlobalRenderingMetadataFromAsset:globalCinematographyMetadata:]
+ -[CNAssetPreprocess loadTracksWithMediaTypeIntoArray:mediaType:fromAsset:]
+ -[CNAssetPreprocess makeCombinedAssetWithMetadataMovURL:disparityMovURL:]
+ -[CNAssetPreprocess process]
+ -[CNAssetPreprocessConfiguration .cxx_destruct]
+ -[CNAssetPreprocessConfiguration destinationAssetURL]
+ -[CNAssetPreprocessConfiguration initWithDestinationAssetURL:]
+ -[CNAssetPreprocessConfiguration referenceSourceAssetTracks]
+ -[CNAssetPreprocessConfiguration setReferenceSourceAssetTracks:]
+ -[CNAssetWriter .cxx_destruct]
+ -[CNAssetWriter appendTimedRenderingMetadata:]
+ -[CNAssetWriter appendTimedRenderingMetadata:cinematographyFrame:timeRange:]
+ -[CNAssetWriter finishSynchronously]
+ -[CNAssetWriter initWithOutputURL:size:pixelFormat:transform:globalRenderingMetadata:globalCinematographyMetadata:colorFormatDescription:trackType:]
+ -[CNAssetWriter pollPixelBuffersWithBlock:]
+ -[CNAssetWriterMetadata .cxx_destruct]
+ -[CNAssetWriterMetadata cinematographyFrame]
+ -[CNAssetWriterMetadata renderingMetadata]
+ -[CNAssetWriterMetadata setCinematographyFrame:]
+ -[CNAssetWriterMetadata setRenderingMetadata:]
+ -[CNAssetWriterMetadata setTimeRange:]
+ -[CNAssetWriterMetadata timeRange]
+ -[CNCinematicDisparityPreview .cxx_destruct]
+ -[CNCinematicDisparityPreview dealloc]
+ -[CNCinematicDisparityPreview disparity]
+ -[CNCinematicDisparityPreview focusDisparity]
+ -[CNCinematicDisparityPreview initWithDisparityProvider:assetInfo:]
+ -[CNCinematicDisparityPreview updateWithSourceImage:frameAttributes:]
+ -[CNRenderingSessionAttributes cinematicEverywhereAssetInfo]
+ -[CNRenderingSessionAttributes disparityPreview]
+ -[CNRenderingSessionAttributes setCinematicEverywhereAssetInfo:]
+ -[CNRenderingSessionAttributes setDisparityPreview:]
+ -[CNRenderingSessionFrameAttributes time]
+ GCC_except_table11
+ GCC_except_table12
+ GCC_except_table17
+ GCC_except_table2
+ GCC_except_table21
+ GCC_except_table4
+ GCC_except_table48
+ GCC_except_table68
+ GCC_except_table8
+ _AVAssetExportPresetPassthrough
+ _AVFileTypeQuickTimeMovie
+ _AVMetadataKeySpaceQuickTimeMetadata
+ _AVMetadataKeySpaceQuickTimeUserData
+ _AVMetadataQuickTimeUserDataKeyTaggedCharacteristic
+ _AVVideoCodecKey
+ _AVVideoCompressionPropertiesKey
+ _AVVideoHeightKey
+ _AVVideoProfileLevelKey
+ _AVVideoWidthKey
+ _CMMetadataFormatDescriptionCreateWithMetadataSpecifications
+ _CMSampleBufferGetImageBuffer
+ _CMSampleBufferGetNumSamples
+ _CMSampleBufferGetPresentationTimeStamp
+ _CMTimeRangeCopyDescription
+ _CVPixelBufferPoolCreate
+ _CVPixelBufferPoolCreatePixelBuffer
+ _CVPixelBufferPoolRelease
+ _CVPixelBufferRelease
+ _OBJC_CLASS_$_AVAsset
+ _OBJC_CLASS_$_AVAssetExportSession
+ _OBJC_CLASS_$_AVAssetReader
+ _OBJC_CLASS_$_AVAssetReaderTrackOutput
+ _OBJC_CLASS_$_AVAssetWriter
+ _OBJC_CLASS_$_AVAssetWriterInput
+ _OBJC_CLASS_$_AVAssetWriterInputMetadataAdaptor
+ _OBJC_CLASS_$_AVAssetWriterInputPixelBufferAdaptor
+ _OBJC_CLASS_$_AVMutableMetadataItem
+ _OBJC_CLASS_$_AVMutableMovie
+ _OBJC_CLASS_$_CNAssetPreprocess
+ _OBJC_CLASS_$_CNAssetPreprocessConfiguration
+ _OBJC_CLASS_$_CNAssetWriter
+ _OBJC_CLASS_$_CNAssetWriterMetadata
+ _OBJC_CLASS_$_CNCinematicDisparityPreview
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_PTCinematographyPostcaptureRefinement
+ _OBJC_CLASS_$_PTCinematographyScriptOptions
+ _OBJC_CLASS_$_PTGlobalRenderingMetadataVersion2
+ _OBJC_CLASS_$_PTMonocularDisparityProvider
+ _OBJC_CLASS_$_PTMonocularDisparitySettings
+ _OBJC_CLASS_$_PTTimedRenderingMetadataVersion2
+ _OBJC_IVAR_$_CNAssetInfo._cinematicCapability
+ _OBJC_IVAR_$_CNAssetInfo._resourceStatus
+ _OBJC_IVAR_$_CNAssetPreprocess._configuration
+ _OBJC_IVAR_$_CNAssetPreprocess._progress
+ _OBJC_IVAR_$_CNAssetPreprocess._sourceAsset
+ _OBJC_IVAR_$_CNAssetPreprocess._tmpMovFiles
+ _OBJC_IVAR_$_CNAssetPreprocess.semaphore
+ _OBJC_IVAR_$_CNAssetPreprocessConfiguration._destinationAssetURL
+ _OBJC_IVAR_$_CNAssetPreprocessConfiguration._referenceSourceAssetTracks
+ _OBJC_IVAR_$_CNAssetWriter._adaptorDisparity
+ _OBJC_IVAR_$_CNAssetWriter._assetWriter
+ _OBJC_IVAR_$_CNAssetWriter._metadata
+ _OBJC_IVAR_$_CNAssetWriter._metadataAdaptor
+ _OBJC_IVAR_$_CNAssetWriter._metadataWriterInput
+ _OBJC_IVAR_$_CNAssetWriter._sessionStarted
+ _OBJC_IVAR_$_CNAssetWriter._writerDisparityInput
+ _OBJC_IVAR_$_CNAssetWriterMetadata._cinematographyFrame
+ _OBJC_IVAR_$_CNAssetWriterMetadata._renderingMetadata
+ _OBJC_IVAR_$_CNAssetWriterMetadata._timeRange
+ _OBJC_IVAR_$_CNCinematicDisparityPreview._assetInfo
+ _OBJC_IVAR_$_CNCinematicDisparityPreview._disparityPixelBuffer
+ _OBJC_IVAR_$_CNCinematicDisparityPreview._disparityPixelBufferPool
+ _OBJC_IVAR_$_CNCinematicDisparityPreview._disparityProvider
+ _OBJC_IVAR_$_CNCinematicDisparityPreview._focusDisparity
+ _OBJC_IVAR_$_CNCinematicDisparityPreview._lastPTS
+ _OBJC_IVAR_$_CNCinematicDisparityPreview._snapshot
+ _OBJC_IVAR_$_CNRenderingSessionAttributes._cinematicEverywhereAssetInfo
+ _OBJC_IVAR_$_CNRenderingSessionAttributes._disparityPreview
+ _OBJC_IVAR_$_CNRenderingSessionFrameAttributes._internalTime
+ _OBJC_METACLASS_$_CNAssetPreprocess
+ _OBJC_METACLASS_$_CNAssetPreprocessConfiguration
+ _OBJC_METACLASS_$_CNAssetWriter
+ _OBJC_METACLASS_$_CNAssetWriterMetadata
+ _OBJC_METACLASS_$_CNCinematicDisparityPreview
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ __DATA__TtC9Cinematic30CNAssetPreprocessConfiguration
+ __IVARS__TtC9Cinematic30CNAssetPreprocessConfiguration
+ __METACLASS_DATA__TtC9Cinematic30CNAssetPreprocessConfiguration
+ __OBJC_$_CLASS_METHODS_CNAssetPreprocess
+ __OBJC_$_INSTANCE_METHODS_CNAssetPreprocess
+ __OBJC_$_INSTANCE_METHODS_CNAssetPreprocessConfiguration
+ __OBJC_$_INSTANCE_METHODS_CNAssetWriter
+ __OBJC_$_INSTANCE_METHODS_CNAssetWriterMetadata
+ __OBJC_$_INSTANCE_METHODS_CNCinematicDisparityPreview
+ __OBJC_$_INSTANCE_VARIABLES_CNAssetPreprocess
+ __OBJC_$_INSTANCE_VARIABLES_CNAssetPreprocessConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_CNAssetWriter
+ __OBJC_$_INSTANCE_VARIABLES_CNAssetWriterMetadata
+ __OBJC_$_INSTANCE_VARIABLES_CNCinematicDisparityPreview
+ __OBJC_$_PROP_LIST_CNAssetPreprocessConfiguration
+ __OBJC_$_PROP_LIST_CNAssetWriterMetadata
+ __OBJC_CLASS_RO_$_CNAssetPreprocess
+ __OBJC_CLASS_RO_$_CNAssetPreprocessConfiguration
+ __OBJC_CLASS_RO_$_CNAssetWriter
+ __OBJC_CLASS_RO_$_CNAssetWriterMetadata
+ __OBJC_CLASS_RO_$_CNCinematicDisparityPreview
+ __OBJC_METACLASS_RO_$_CNAssetPreprocess
+ __OBJC_METACLASS_RO_$_CNAssetPreprocessConfiguration
+ __OBJC_METACLASS_RO_$_CNAssetWriter
+ __OBJC_METACLASS_RO_$_CNAssetWriterMetadata
+ __OBJC_METACLASS_RO_$_CNCinematicDisparityPreview
+ ___28-[CNAssetPreprocess process]_block_invoke
+ ___28-[CNAssetPreprocess process]_block_invoke_2
+ ___36-[CNAssetWriter finishSynchronously]_block_invoke
+ ___36-[CNAssetWriter finishSynchronously]_block_invoke_2
+ ___39-[CNAssetPreprocess checkPreconditions]_block_invoke
+ ___43-[CNAssetWriter pollPixelBuffersWithBlock:]_block_invoke
+ ___54-[CNAssetPreprocess loadAssetInfoFromAsset:assetInfo:]_block_invoke
+ ___62-[CNAssetInfo downloadResourcesWithTimeout:completionHandler:]_block_invoke
+ ___62-[CNAssetInfo downloadResourcesWithTimeout:completionHandler:]_block_invoke_2
+ ___65+[CNAssetInfo _loadFromAsset:requireDisparity:completionHandler:]_block_invoke_2
+ ___66+[CNAssetInfo _getCNDisparityResourceStatusForAssetInfo:callback:]_block_invoke
+ ___66+[CNAssetInfo checkCinematicCapabilityForAsset:completionHandler:]_block_invoke
+ ___66+[CNAssetInfo checkCinematicCapabilityForAsset:completionHandler:]_block_invoke_2
+ ___66-[CNAssetInfo preprocessAssetWithConfiguration:completionHandler:]_block_invoke
+ ___73-[CNAssetPreprocess makeCombinedAssetWithMetadataMovURL:disparityMovURL:]_block_invoke
+ ___74-[CNAssetPreprocess loadTracksWithMediaTypeIntoArray:mediaType:fromAsset:]_block_invoke
+ ___74-[CNAssetPreprocess loadTracksWithMediaTypeIntoArray:mediaType:fromAsset:]_block_invoke_2
+ ___84+[CNAssetPreprocess preprocessAssetWithConfiguration:sourceAsset:completionHandler:]_block_invoke
+ ___87-[CNAssetPreprocess loadGlobalRenderingMetadataFromAsset:globalCinematographyMetadata:]_block_invoke
+ ___89+[CNAssetInfo _downloadResourcesForMonocularDisparitySettings:timeout:completionHandler:]_block_invoke
+ ___89+[CNAssetInfo _downloadResourcesForMonocularDisparitySettings:timeout:completionHandler:]_block_invoke_2
+ ___NSDictionary0__struct
+ ___block_descriptor_144_e8_32s40s48s56s64s72s80s_e32_B24?0^^{__CVBuffer}8^{?=qiIq}16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_40_e8_32bs_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32r_e49_v16?0"PTDisparityProviderInitializationStatus"8lr32l8
+ ___block_descriptor_48_e8_32bs40r_e33_v24?0"CNAssetInfo"8"NSError"16lr40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e47_v24?0"PTGlobalRenderingMetadata"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e8_v16?0q8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e20_v20?0B8"NSError"12lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e8_v16?0q8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e22_B16?0"AVAssetTrack"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ ___block_descriptor_49_e8_32s40bs_e47_v24?0"PTGlobalRenderingMetadata"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48r_e17_v16?0"NSError"8lr48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e33_v24?0"CNAssetInfo"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e33_v24?0"CNAssetInfo"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48r_e29_v24?0"NSArray"8"NSError"16lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_64_e8_32s40bs48r_e50_v24?0"CNRenderingSessionAttributes"8"NSError"16lr48l8s40l8s32l8
+ ___block_descriptor_64_e8_32s40bs48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_64_e8_32s40r48r56r_e29_v24?0"NSArray"8"NSError"16lr40l8r48l8r56l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_68_e8_32bs40r48r56r_e49_v16?0"PTDisparityProviderInitializationStatus"8lr40l8r48l8s32l8r56l8
+ ___kCFBooleanTrue
+ ___swift_closure_destructor
+ ___swift_closure_destructorTm
+ __swiftEmptySetSingleton
+ __swift_implicitisolationactor_to_executor_cast
+ _bzero
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _kCMMetadataBaseDataType_RawData
+ _kCMMetadataFormatDescriptionMetadataSpecificationKey_DataType
+ _kCMMetadataFormatDescriptionMetadataSpecificationKey_Identifier
+ _kCVPixelBufferHeightKey
+ _kCVPixelBufferIOSurfacePropertiesKey
+ _kCVPixelBufferMetalCompatibilityKey
+ _kCVPixelBufferPixelFormatTypeKey
+ _kCVPixelBufferWidthKey
+ _kMediaCharacteristicDepth
+ _kMediaCharacteristicDepthPostCapture
+ _kPTDisparityProviderDownloadTimeoutDefault
+ _kVTCompressionPropertyKey_AllowOpenGOP
+ _kVTCompressionPropertyKey_MaxAllowedFrameQP
+ _kVTCompressionPropertyKey_MinAllowedFrameQP
+ _kVTProfileLevel_HEVC_Monochrome_AutoLevel
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_msgSend$URLByAppendingPathComponent:
+ _objc_msgSend$_allRenderingConfigurationsForResourceVersions:
+ _objc_msgSend$_allResourceVersions
+ _objc_msgSend$_downloadResourcesForMonocularDisparitySettings:timeout:completionHandler:
+ _objc_msgSend$_getCNDisparityResourceStatusForAssetInfo:callback:
+ _objc_msgSend$_loadWithAsset:changesDictionary:error:
+ _objc_msgSend$_snapshot
+ _objc_msgSend$addInput:
+ _objc_msgSend$addMutableTrackWithMediaType:copySettingsFromTrack:options:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$addOutput:
+ _objc_msgSend$addTrackAssociationToTrack:type:
+ _objc_msgSend$appendPixelBuffer:withPresentationTime:
+ _objc_msgSend$appendTimedMetadataGroup:
+ _objc_msgSend$appendTimedRenderingMetadata:
+ _objc_msgSend$appendTimedRenderingMetadata:cinematographyFrame:timeRange:
+ _objc_msgSend$assetWithURL:
+ _objc_msgSend$assetWriterInputPixelBufferAdaptorWithAssetWriterInput:sourcePixelBufferAttributes:
+ _objc_msgSend$assetWriterInputWithMediaType:outputSettings:sourceFormatHint:
+ _objc_msgSend$canAddInput:
+ _objc_msgSend$cancel
+ _objc_msgSend$checkCinematicCapabilityForAsset:completionHandler:
+ _objc_msgSend$checkPreconditions
+ _objc_msgSend$cinematicCapability
+ _objc_msgSend$cinematicEverywhereAssetInfo
+ _objc_msgSend$cinematographyFrame
+ _objc_msgSend$copyNextSampleBuffer
+ _objc_msgSend$createTemporaryMovURL
+ _objc_msgSend$dataFromObject:options:error:
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$defaultResourceDownloadTimeout
+ _objc_msgSend$destinationAssetURL
+ _objc_msgSend$disparity
+ _objc_msgSend$disparityForColorBuffer:timedRenderingMetadata:time:outputBuffer:
+ _objc_msgSend$disparityPixelFormat
+ _objc_msgSend$disparityPreview
+ _objc_msgSend$disparitySize
+ _objc_msgSend$downloadResourcesForVersions:timeout:completionHandler:
+ _objc_msgSend$downloadResourcesWithTimeout:completionHandler:
+ _objc_msgSend$endInputs
+ _objc_msgSend$error
+ _objc_msgSend$exportAsynchronouslyWithCompletionHandler:
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$finishSynchronously
+ _objc_msgSend$finishWritingWithCompletionHandler:
+ _objc_msgSend$focusDistanceAtTime:disparityBuffer:
+ _objc_msgSend$globallyUniqueString
+ _objc_msgSend$initWithAsset:error:
+ _objc_msgSend$initWithAsset:presetName:
+ _objc_msgSend$initWithAssetWriterInput:
+ _objc_msgSend$initWithDestinationAssetURL:
+ _objc_msgSend$initWithDisparityProvider:assetInfo:
+ _objc_msgSend$initWithInteger:
+ _objc_msgSend$initWithItems:timeRange:
+ _objc_msgSend$initWithLength:
+ _objc_msgSend$initWithMediaType:outputSettings:
+ _objc_msgSend$initWithMinorVersion:
+ _objc_msgSend$initWithOutputURL:size:pixelFormat:transform:globalRenderingMetadata:globalCinematographyMetadata:colorFormatDescription:trackType:
+ _objc_msgSend$initWithProgress:sourceAsset:configuration:
+ _objc_msgSend$initWithQuality:globalMetadata:inputSize:temporalFilteringEnabled:
+ _objc_msgSend$initWithScript:samplesAllDetections:
+ _objc_msgSend$initWithSettings:downloadTimeout:initializationCallback:
+ _objc_msgSend$initWithTrack:outputSettings:
+ _objc_msgSend$initWithURL:fileType:error:
+ _objc_msgSend$insertTimeRange:ofTrack:atTime:copySampleData:error:
+ _objc_msgSend$isCancelled
+ _objc_msgSend$isPreprocessed
+ _objc_msgSend$isReadyForMoreMediaData
+ _objc_msgSend$loadAssetInfoFromAsset:assetInfo:
+ _objc_msgSend$loadGlobalRenderingMetadataFromAsset:globalCinematographyMetadata:
+ _objc_msgSend$loadTracksWithMediaCharacteristic:completionHandler:
+ _objc_msgSend$loadTracksWithMediaTypeIntoArray:mediaType:fromAsset:
+ _objc_msgSend$loadWithAsset:changesDictionary:disparityProvider:completion:
+ _objc_msgSend$loadWithAsset:changesDictionary:options:completion:
+ _objc_msgSend$makeCombinedAssetWithMetadataMovURL:disparityMovURL:
+ _objc_msgSend$markAsFinished
+ _objc_msgSend$metadata
+ _objc_msgSend$metadataItem
+ _objc_msgSend$movieWithURL:options:error:
+ _objc_msgSend$nextFrame
+ _objc_msgSend$outputURL
+ _objc_msgSend$path
+ _objc_msgSend$pollPixelBuffersWithBlock:
+ _objc_msgSend$preprocessAssetWithConfiguration:completionHandler:
+ _objc_msgSend$preprocessAssetWithConfiguration:sourceAsset:completionHandler:
+ _objc_msgSend$process
+ _objc_msgSend$processInfo
+ _objc_msgSend$processNextDisparityBuffer:
+ _objc_msgSend$referenceSourceAssetTracks
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$renderingMetadata
+ _objc_msgSend$requestMediaDataWhenReadyOnQueue:usingBlock:
+ _objc_msgSend$resetState
+ _objc_msgSend$resourceStatus
+ _objc_msgSend$resourceStatusForSettings:
+ _objc_msgSend$resourceStatusForVersions:
+ _objc_msgSend$setAlwaysCopiesSampleData:
+ _objc_msgSend$setCinematicCapability:
+ _objc_msgSend$setCinematicEverywhereAssetInfo:
+ _objc_msgSend$setCinematographyFrame:
+ _objc_msgSend$setCompletedUnitCount:
+ _objc_msgSend$setDisparityPrecompute:
+ _objc_msgSend$setDisparityPreview:
+ _objc_msgSend$setDuration:
+ _objc_msgSend$setExpectsMediaDataInRealTime:
+ _objc_msgSend$setKey:
+ _objc_msgSend$setKeySpace:
+ _objc_msgSend$setMetadata:
+ _objc_msgSend$setMetadata:ofType:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setOutputFileType:
+ _objc_msgSend$setOutputURL:
+ _objc_msgSend$setPreprocessed:
+ _objc_msgSend$setReferenceSourceAssetTracks:
+ _objc_msgSend$setRenderingMetadata:
+ _objc_msgSend$setRenderingVersion:
+ _objc_msgSend$setResourceStatus:
+ _objc_msgSend$setSensorID:
+ _objc_msgSend$setTime:
+ _objc_msgSend$setTimeRange:
+ _objc_msgSend$setTransform:
+ _objc_msgSend$setValue:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$sizeOfSerializedObjectWithOptions:
+ _objc_msgSend$startReading
+ _objc_msgSend$startSessionAtSourceTime:
+ _objc_msgSend$startWriting
+ _objc_msgSend$state
+ _objc_msgSend$status
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$temporaryDirectory
+ _objc_msgSend$totalExpectedBytes
+ _objc_msgSend$totalWrittenBytes
+ _objc_msgSend$track
+ _objc_msgSend$tracksWithMediaType:
+ _objc_msgSend$updateWithSourceImage:frameAttributes:
+ _objc_msgSend$writeMovieHeaderToURL:fileType:options:error:
+ _objc_msgSend$writeToData:withOptions:
+ _objc_retainBlock
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_bridgeObjectRetain
+ _swift_deallocObject
+ _swift_errorRetain
+ _swift_getObjectType
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x24
+ _swift_release_x8
+ _swift_retain_x20
+ _swift_task_addCancellationHandler
+ _swift_task_removeCancellationHandler
+ _symbolic ScCy___________pG 9Cinematic11CNAssetInfoC s5ErrorP
+ _symbolic ScCyyt______pG s5ErrorP
+ _symbolic Sccy__________G So21CNCinematicCapabilityV s5NeverO
+ _symbolic So10NSProgressCSg
+ _symbolic So30CNAssetPreprocessConfigurationC
+ _symbolic _____ 9Cinematic30CNAssetPreprocessConfigurationC
+ _symbolic _____ So21CNCinematicCapabilityV
+ _symbolic _____Sg 10Foundation11SubprogressV
+ _symbolic _____ySo8NSNumberCG s11_SetStorageC
- GCC_except_table15
- GCC_except_table33
- _CMTimeMakeWithSeconds
- ___block_descriptor_48_e8_32s40bs_e47_v24?0"PTGlobalRenderingMetadata"8"NSError"16ls32l8s40l8
- ___block_descriptor_57_e8_32s40bs_e5_v8?0ls32l8s40l8
- _objc_msgSend$loadWithAsset:changesDictionary:completion:
CStrings:
+ "%@.mov"
+ "A"
+ "B16@?0@\"AVAssetTrack\"8"
+ "B24@?0^^{__CVBuffer}8^{?=qiIq}16"
+ "CNAssetWriter: %@ failed: %@"
+ "CNAssetWriter: AVAssetWriter init failed: %@"
+ "CNAssetWriter: append failed at %f: %@"
+ "CNAssetWriter: canAddInput failed: %@"
+ "CNAssetWriter: canAddInput for metadata failed: %@"
+ "CNAssetWriter: failed to create metadata format description: %d"
+ "CNAssetWriter: finished writing to %@"
+ "CNAssetWriter: metadata input not ready at time %f"
+ "CNAssetWriter: renderingMetadata %@ cinematographyFrame %@ should both be not nil"
+ "CNAssetWriter: startWriting failed: %@"
+ "CNAssetWriter: timeRange invalid"
+ "Cannot add %@ track to output movie"
+ "Cannot add color track to output movie"
+ "Cannot allocate pixelbuffer"
+ "Cannot allocate pixelbufferpool"
+ "Cannot export to %@: Status: %i Error %@"
+ "Cannot find cinematic metadata track in output movie"
+ "Cannot initialize CNRenderingSession. Download resources using CNAssetInfo before initializing CNRenderingSessionAttributes and CNRenderingSession"
+ "Cannot instantiate script snapshot. Error: %@"
+ "Cannot load metadataSampleBuffer"
+ "Cannot open output file %@"
+ "Cannot read disparityTracks %@. Found %@"
+ "Cannot read metadata %@. Found %@"
+ "Cannot read tracks from source asset. Found %@"
+ "Cannot write movie header to output file"
+ "Error SerializeFrameWithTime %@"
+ "Error deleting %@: %@"
+ "Error estimating sourceDisparity"
+ "Error initializing disparity provider"
+ "Error initializing script for preview"
+ "Error instantiating disparity provider %@"
+ "Error loading MediaCharacteristic %@"
+ "Error making combined asset at %@ error %@"
+ "Expected 1 auxiliary picture track in output, found %lu"
+ "Failed creating disparity from configuration. Expected cinematicCapability to be CNCinematicCapabilityNeedsPreprocessing but was %li"
+ "Failed deleting %@ after preprocess cancelled %@"
+ "Missing rendering metadata for timestamp %f"
+ "Preconfigured config failed due to build"
+ "Preconfigured config failed to asset"
+ "Unable to get disparity pixelbuffer from pool"
+ "Unexpected metadata for preview. Cannot be used with legacy assets. Was %@"
+ "Unsupported asset. Capabilities was %i"
+ "_getCNDisparityResourceStatusForAsset: Error %@"
+ "_sourceAsset == nil"
+ "appendTimedMetadataGroup failed for time range %@"
+ "asset %@ is already renderable"
+ "asset %@ not cinematic"
+ "checkCinematicCapabilityForAsset: Error %@"
+ "com.apple.cinematic.DisparityResourceStatusForAssetInfo"
+ "com.apple.cinematic.checkCinematicCapabilityForAsset"
+ "com.apple.cinematic.downloadResources"
+ "com.apple.cinematic.downloadResourcesWithTimeout"
+ "com.apple.cinematic.preprocess"
+ "dish"
+ "downloadResources(timeout:subprogress:)"
+ "downloadResources(versions:timeout:subprogress:)"
+ "duration"
+ "insertTimeRange (reference) failed for %@ track"
+ "insertTimeRange (reference) failed for color track"
+ "insertTimeRange failed for %@ track"
+ "insertTimeRange failed for color track"
+ "insertTimeRange failed for disparity track"
+ "insertTimeRange failed for metadata track"
+ "preprocessAsset(configuration:subprogress:)"
+ "q"
+ "sourceDisparity must not be nil for this asset"
+ "sourceDisparity unexpected for preview"
+ "startReading failed"
+ "timedRenderingMetadata deserialization failed for timestamp %f. Class was %@"
+ "url %@ already exist"
+ "v16@?0@\"NSError\"8"
+ "v16@?0@\"PTDisparityProviderInitializationStatus\"8"
+ "v16@?0q8"
+ "v24@?0@\"CNRenderingSessionAttributes\"8@\"NSError\"16"
- "Error: (%@) unable to locate disparity track associated with video track %@"
```
