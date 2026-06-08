## Cinematic

> `/System/Library/Frameworks/Cinematic.framework/Cinematic`

```diff

-492.120.3.0.0
-  __TEXT.__text: 0x13664
-  __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_methlist: 0xdcc
-  __TEXT.__const: 0x9c8
-  __TEXT.__cstring: 0x349
-  __TEXT.__oslogstring: 0x6e2
-  __TEXT.__gcc_except_tab: 0x25c
+546.0.0.0.0
+  __TEXT.__text: 0x13fdc
+  __TEXT.__objc_methlist: 0xe9c
+  __TEXT.__cstring: 0x359
+  __TEXT.__const: 0x9d8
+  __TEXT.__oslogstring: 0x84d
+  __TEXT.__gcc_except_tab: 0x280
   __TEXT.__constg_swiftt: 0x5b0
   __TEXT.__swift5_typeref: 0x332
   __TEXT.__swift5_reflstr: 0x22d

   __TEXT.__swift5_types: 0x60
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x24
+  __TEXT.__swift_as_cont: 0x48
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x7b8
+  __TEXT.__unwind_info: 0x848
   __TEXT.__eh_frame: 0x448
-  __TEXT.__objc_classname: 0x2f8
-  __TEXT.__objc_methname: 0x2885
-  __TEXT.__objc_methtype: 0x90f
-  __TEXT.__objc_stubs: 0x2540
-  __DATA_CONST.__got: 0x288
-  __DATA_CONST.__const: 0x6e0
-  __DATA_CONST.__objc_classlist: 0xc8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x730
+  __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf0
+  __DATA_CONST.__objc_selrefs: 0xb78
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x470
+  __DATA_CONST.__got: 0x2c0
   __AUTH_CONST.__const: 0x850
   __AUTH_CONST.__cfstring: 0x1a0
-  __AUTH_CONST.__objc_const: 0x1b28
+  __AUTH_CONST.__objc_const: 0x1df0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH.__objc_data: 0x500
+  __AUTH_CONST.__objc_intobj: 0xc0
+  __AUTH_CONST.__auth_got: 0x4b8
+  __AUTH.__objc_data: 0x5a0
   __AUTH.__data: 0x840
-  __DATA.__objc_ivar: 0x6c
+  __DATA.__objc_ivar: 0x94
   __DATA.__data: 0x2c8
   __DATA.__bss: 0x740
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
+  - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/CinematicUtil.framework/CinematicUtil
   - /System/Library/PrivateFrameworks/Portrait.framework/Portrait
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7478F910-50CB-3065-AB52-11134BBE421E
-  Functions: 730
-  Symbols:   1676
-  CStrings:  642
+  UUID: 27A9F621-8846-3425-B4CD-9F808B2E5838
+  Functions: 748
+  Symbols:   1771
+  CStrings:  91
 
Symbols:
+ +[CNImageRenderingSession minimumTileExtendRectForTileRect:sourceRGBASize:]
+ +[CNImageRenderingSessionConfiguration isRenderingVersionSupported:]
+ +[CNImageRenderingSessionConfiguration latestRenderingVersion]
+ -[CNImageRenderingSession .cxx_destruct]
+ -[CNImageRenderingSession configuration]
+ -[CNImageRenderingSession encodeRenderToCommandBuffer:sourceRGBA:sourceDisparity:destinationRGBA:fNumber:focusDisparity:]
+ -[CNImageRenderingSession encodeRenderToCommandBuffer:sourceRGBA:sourceDisparity:destinationRGBA:fNumber:focusDisparity:].cold.1
+ -[CNImageRenderingSession encodeTileRenderToCommandBuffer:sourceTileRGBA:sourceDisparity:destinationTileRGBA:fNumber:focusDisparity:sourceRGBASize:tileOffset:tileExtendOffset:]
+ -[CNImageRenderingSession encodeTileRenderToCommandBuffer:sourceTileRGBA:sourceDisparity:destinationTileRGBA:fNumber:focusDisparity:sourceRGBASize:tileOffset:tileExtendOffset:].cold.1
+ -[CNImageRenderingSession encodeTileRenderToCommandBuffer:sourceTileRGBA:sourceDisparity:destinationTileRGBA:fNumber:focusDisparity:sourceRGBASize:tileOffset:tileExtendOffset:].cold.2
+ -[CNImageRenderingSession initWithConfiguration:]
+ -[CNImageRenderingSession lazyInstantiateTiledRendererWithTileSize:tileExtendSize:disparitySize:sourceRGBASize:]
+ -[CNImageRenderingSession lazyInstantiateTiledRendererWithTileSize:tileExtendSize:disparitySize:sourceRGBASize:].cold.1
+ -[CNImageRenderingSession lazyInstantiateTiledRendererWithTileSize:tileExtendSize:disparitySize:sourceRGBASize:].cold.2
+ -[CNImageRenderingSessionConfiguration initWithQuality:]
+ -[CNImageRenderingSessionConfiguration initWithQuality:renderingVersion:]
+ -[CNImageRenderingSessionConfiguration quality]
+ -[CNImageRenderingSessionConfiguration renderingVersion]
+ -[CNScript(Private) _performWithInternalScript:]
+ GCC_except_table114
+ GCC_except_table30
+ _AVMediaTypeAuxiliaryPicture
+ _CGSizeZero
+ _OBJC_CLASS_$_CNImageRenderingSession
+ _OBJC_CLASS_$_CNImageRenderingSessionConfiguration
+ _OBJC_CLASS_$_CNUPixelBufferUtil
+ _OBJC_CLASS_$_PTMetalContext
+ _OBJC_CLASS_$_PTRaytracingV5001
+ _OBJC_IVAR_$_CNAssetInfo._preprocessed
+ _OBJC_IVAR_$_CNImageRenderingSession._configuration
+ _OBJC_IVAR_$_CNImageRenderingSession._lastUsedDisparitySize
+ _OBJC_IVAR_$_CNImageRenderingSession._lastUsedTileExtendSize
+ _OBJC_IVAR_$_CNImageRenderingSession._lastUsedTileSize
+ _OBJC_IVAR_$_CNImageRenderingSession._lastUsedsourceRGBASize
+ _OBJC_IVAR_$_CNImageRenderingSession._metalContext
+ _OBJC_IVAR_$_CNImageRenderingSession._tiledRender
+ _OBJC_IVAR_$_CNImageRenderingSessionConfiguration._quality
+ _OBJC_IVAR_$_CNImageRenderingSessionConfiguration._renderingVersion
+ _OBJC_METACLASS_$_CNImageRenderingSession
+ _OBJC_METACLASS_$_CNImageRenderingSessionConfiguration
+ __OBJC_$_CLASS_METHODS_CNImageRenderingSession
+ __OBJC_$_CLASS_METHODS_CNImageRenderingSessionConfiguration
+ __OBJC_$_CLASS_PROP_LIST_CNImageRenderingSessionConfiguration
+ __OBJC_$_INSTANCE_METHODS_CNImageRenderingSession
+ __OBJC_$_INSTANCE_METHODS_CNImageRenderingSessionConfiguration
+ __OBJC_$_INSTANCE_METHODS_CNScript(Private)
+ __OBJC_$_INSTANCE_VARIABLES_CNImageRenderingSession
+ __OBJC_$_INSTANCE_VARIABLES_CNImageRenderingSessionConfiguration
+ __OBJC_$_PROP_LIST_CNImageRenderingSession
+ __OBJC_$_PROP_LIST_CNImageRenderingSessionConfiguration
+ __OBJC_CLASS_RO_$_CNImageRenderingSession
+ __OBJC_CLASS_RO_$_CNImageRenderingSessionConfiguration
+ __OBJC_METACLASS_RO_$_CNImageRenderingSession
+ __OBJC_METACLASS_RO_$_CNImageRenderingSessionConfiguration
+ ___48-[CNScript(Private) _performWithInternalScript:]_block_invoke
+ ___48-[CNScript(Private) _performWithInternalScript:]_block_invoke_2
+ ____CNLoadDisparityTrackForVideoTrack_block_invoke
+ ____CNLoadDisparityTrackForVideoTrack_block_invoke.cold.1
+ ___block_descriptor_48_e8_32s40bs_e5_8?0ls40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0lr48l8s40l8s32l8
+ ___block_literal_global.53
+ ___kCFBooleanFalse
+ ___swift_async_cont_functlets
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_Cinematic
+ _kCVImageBufferTransferFunction_Linear
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$commandQueue
+ _objc_msgSend$destinationColor
+ _objc_msgSend$encodeTileRenderToCommandBuffer:sourceTileRGBA:sourceDisparity:destinationTileRGBA:fNumber:focusDisparity:sourceRGBASize:tileOffset:tileExtendOffset:
+ _objc_msgSend$initWithCommandQueue:bundleClass:
+ _objc_msgSend$initWithMetalContext:colorSize:tileSize:tileExtend:disparitySize:debugRendering:verbose:options:quality:
+ _objc_msgSend$initWithQuality:renderingVersion:
+ _objc_msgSend$isRenderingVersionSupported:
+ _objc_msgSend$latestRenderingVersion
+ _objc_msgSend$lazyInstantiateTiledRendererWithTileSize:tileExtendSize:disparitySize:sourceRGBASize:
+ _objc_msgSend$renderContinuousWithSource:renderRequest:tileRect:tileExtendRect:
+ _objc_msgSend$setScissorRect:
+ _objc_msgSend$setTransferFunction:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x25
+ _objc_retain_x27
+ _objc_retain_x3
+ _swift_release_x19
+ _swift_release_x23
+ _swift_retain_x19
+ _swift_retain_x2
- GCC_except_table32
- _OBJC_CLASS_$_PTPixelBufferUtil
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- __CNLoadFirstAssociatedTrack
- __OBJC_$_INSTANCE_METHODS_CNScript
- ___61+[CNAssetInfo loadFromCinematicVideoTrack:completionHandler:]_block_invoke.4.cold.2
- ___block_literal_global.54
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_Cinematic
- _objc_retain_x28
CStrings:
+ "Error: (%@) unable to locate cinematic metadata track in asset for video track %@"
+ "Error: (%@) unable to locate disparity track associated with video track %@"
+ "Unexpected renderingQuality %i. Using CNRenderingQualityExport instead"
+ "error: Invalid destinationRGBA size. Expected %lu x %lu but was %lu x %lu"
+ "error: encoding rendering"
+ "error: invalid renderingVersion %li"
+ "error: sourceTileRGBA (%lu x %lu) must be larger than or equal to destinationTileRGBA (%lu x %lu)"
+ "warning: render version %li is not supported"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<MTLCommandBuffer>\"16@0:8"
- "@\"<MTLCommandBuffer>\"24@0:8@\"MTLCommandBufferDescriptor\"16"
- "@\"<MTLCommandQueue>\""
- "@\"<MTLDevice>\"16@0:8"
- "@\"<PTRenderState>\""
- "@\"AVAssetTrack\""
- "@\"CNRenderingSessionAttributes\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"PTCinematographyDecision\""
- "@\"PTCinematographyDetection\""
- "@\"PTCinematographyFrame\""
- "@\"PTCinematographyScript\""
- "@\"PTCinematographyTrack\""
- "@\"PTGlobalRenderingMetadata\""
- "@\"PTRenderPipeline\""
- "@\"PTTapToTrack\""
- "@\"PTTimedRenderingMetadata\""
- "@16@0:8"
- "@20@0:8f16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8^{opaqueCMSampleBuffer=}16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@28@0:8@16i24"
- "@28@0:8f16q20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8^{opaqueCMSampleBuffer=}16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8{?=qiIq}16"
- "@40@0:8{CGPoint=dd}16^{__CVBuffer=}32"
- "@52@0:8{?=qiIq}16q40B48"
- "@52@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16f48"
- "@56@0:8{?=qiIq}16^{__CVBuffer=}40^{__CVBuffer=}48"
- "@64@0:8{?=qiIq}16{?=qiIq}40"
- "@64@0:8{?={?=qiIq}{?=qiIq}}16"
- "@84@0:8{?=qiIq}16q40{CGRect={CGPoint=dd}{CGSize=dd}}48f80"
- "@88@0:8@16@24{CGAffineTransform=dddddd}32q80"
- "B104@0:8{?={?=qiIq}{?=qiIq}}16@64{?=qiIq}72^@96"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8q16"
- "B56@0:8@16@24^{__CVBuffer=}32^{__CVBuffer=}40@48"
- "B56@0:8@16@24^{__CVBuffer=}32^{__CVBuffer=}40^{__CVBuffer=}48"
- "B64@0:8@16@24^{__CVBuffer=}32^{__CVBuffer=}40@48@56"
- "B88@0:8{?=qiIq}16{CGRect={CGPoint=dd}{CGSize=dd}}40^{__CVBuffer=}72^{__CVBuffer=}80"
- "CNAssetInfo"
- "CNAssetSpatialAudioInfo"
- "CNBoundsPrediction"
- "CNComposition"
- "CNCompositionInfo"
- "CNCustomDetectionTrack"
- "CNDecision"
- "CNDetection"
- "CNDetectionTrack"
- "CNExtensions"
- "CNFixedDetectionTrack"
- "CNObjectTracker"
- "CNRenderingSession"
- "CNRenderingSessionAttributes"
- "CNRenderingSessionFrameAttributes"
- "CNScript"
- "CNScriptChanges"
- "CNScriptFrame"
- "Error: (%@) unable to locate metadata track for video track %@"
- "Error: located metadata track %@ for video track %@ does not have expected format"
- "MTLCommandQueue"
- "NSCopying"
- "NSMutableCopying"
- "NSObject"
- "Private"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<MTLCommandQueue>\",R,V_commandQueue"
- "T@\"<MTLDevice>\",R"
- "T@\"AVAsset\",R"
- "T@\"AVAssetTrack\",&,V_cinematicDisparityTrack"
- "T@\"AVAssetTrack\",&,V_cinematicMetadataTrack"
- "T@\"AVAssetTrack\",&,V_cinematicVideoTrack"
- "T@\"AVMutableCompositionTrack\",R,D"
- "T@\"CNDetection\",R"
- "T@\"CNRenderingSessionAttributes\",R,V_sessionAttributes"
- "T@\"NSArray\",R"
- "T@\"NSData\",R"
- "T@\"NSDictionary\",R,V_internalChanges"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_queue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C"
- "T@\"NSString\",R,C"
- "T@\"PTCinematographyDecision\",&,V_internalDecision"
- "T@\"PTCinematographyDetection\",&,V_internalDetection"
- "T@\"PTCinematographyDetection\",R"
- "T@\"PTCinematographyFrame\",&"
- "T@\"PTCinematographyFrame\",&,V_internalFrame"
- "T@\"PTCinematographyScript\",&,V_internalScript"
- "T@\"PTCinematographyTrack\",&"
- "T@\"PTCinematographyTrack\",&,V_internalTrack"
- "T@\"PTGlobalRenderingMetadata\",R,V_internalMetadata"
- "T@\"PTTapToTrack\",&,V_internalTapToTrack"
- "T@\"PTTimedRenderingMetadata\",R,V_internalMetadata"
- "TB,R"
- "TB,R,GisDiscrete"
- "TB,R,GisGroupDecision"
- "TB,R,GisStrongDecision"
- "TB,R,GisUserCreated"
- "TB,R,GisUserDecision"
- "TQ,R"
- "TQ,V_creationHash"
- "Tf"
- "Tf,R"
- "Tf,V_confidence"
- "Tf,V_fNumber"
- "Tf,V_focusDisparity"
- "Tq,R"
- "Tq,R,V_quality"
- "T{?=qiIq},R"
- "T{?={?=qiIq}{?=qiIq}},R"
- "T{CGAffineTransform=dddddd},R"
- "T{CGAffineTransform=dddddd},R,V_preferredTransform"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},V_normalizedBounds"
- "T{CGSize=dd},R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__CVMetalTextureCache=}"
- "_PTGlobalRenderingMetadataFromItems:"
- "_TtC9Cinematic11CNAssetInfo"
- "_TtC9Cinematic15CNObjectTracker"
- "_TtC9Cinematic16CNDetectionTrack"
- "_TtC9Cinematic17CNCompositionInfo"
- "_TtC9Cinematic18CNRenderingSession"
- "_TtC9Cinematic21CNFixedDetectionTrack"
- "_TtC9Cinematic22CNCustomDetectionTrack"
- "_TtC9Cinematic23CNAssetSpatialAudioInfo"
- "_TtC9Cinematic8CNScript"
- "_changesFromInternal:"
- "_cinematicDisparityTrack"
- "_cinematicMetadataTrack"
- "_cinematicVideoTrack"
- "_commandQueue"
- "_confidence"
- "_copyDecisionFromInternal:"
- "_copyDecisionsFromInternal:"
- "_copyDetectionFromInternal:"
- "_copyDetectionsFromInternal:"
- "_copyFrameFromInternal:"
- "_copyFramesFromInternal:"
- "_copyInternalFromDecisions:"
- "_copyInternalFromDetections:"
- "_copyInternalFromFrames:"
- "_creationHash"
- "_encodeRenderToCommandBuffer:frameAttributes:sourceImage:sourceDisparity:destinationTexture:"
- "_fNumber"
- "_focusDisparity"
- "_initCopyingInternalDecision:"
- "_initCopyingInternalDetection:"
- "_initCopyingInternalFrame:"
- "_initJustWithPTTimedRenderingMetadata:"
- "_initTakingInternalDecision:"
- "_initTakingInternalDetection:"
- "_initTakingInternalFrame:"
- "_initWithCinematographyDictionary:"
- "_initWithInternal:"
- "_initWithInternalChanges:"
- "_initWithInternalScript:"
- "_initWithNormalizedBounds:confidence:"
- "_initWithPTTimedRenderingMetadata:"
- "_initWithTimedData:"
- "_initWithTimedData:sessionAttributes:"
- "_initWithVideoTrack:disparityTrack:metadataTrack:"
- "_integrityCheck"
- "_internalChanges"
- "_internalCustomTrack"
- "_internalDecision"
- "_internalDetection"
- "_internalFixedTrack"
- "_internalFrame"
- "_internalFromTracks:"
- "_internalMetadata"
- "_internalScript"
- "_internalTapToTrack"
- "_internalTrack"
- "_loadPTGlobalRenderingMetadataFromAsset:completionHandler:"
- "_metadataBlob"
- "_mutableDecisionsWithCinematographyDictionaries:"
- "_normalizedBounds"
- "_predictionFromInternal:"
- "_preferredTransform"
- "_quality"
- "_queue"
- "_renderPipeline"
- "_renderState"
- "_sessionAttributes"
- "_spatialAudioTrack"
- "_takeDecisionsFromInternal:"
- "_textureCache"
- "_trackFromInternal:"
- "_tracksFromInternal:"
- "accessibilityLabelForDetectionType:"
- "addChild:withPendingUnitCount:"
- "addDetectionAndStartTrackingRect:time:colorBuffer:disparityBuffer:"
- "addDetectionForNextFrameAt:colorBuffer:disparityBuffer:"
- "addDetectionTrack:"
- "addEffect:"
- "addMutableTrackWithMediaType:preferredTrackID:"
- "addObject:"
- "addResidencySet:"
- "addResidencySets:count:"
- "addTrack:"
- "addTracksForCinematicAssetInfo:preferredStartingTrackID:"
- "addUserDecision:"
- "addedDetectionTracks"
- "allCinematicTracks"
- "allDetections"
- "aperture"
- "appendBytes:length:"
- "applyDetectionSmoothing"
- "applyToRenderRequest:"
- "applyToRenderState:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "array"
- "arrayWithObjects:count:"
- "asset"
- "assetReaderOutputSettingsForContentType:"
- "assetWriterInputSettingsForContentType:"
- "audioMix"
- "audioMixWithEffectIntensity:renderingStyle:"
- "autorelease"
- "baseDecisionsInTimeRange:"
- "bestDetectionForGroupID:"
- "bestDetectionForGroupIdentifier:"
- "boolValue"
- "changes"
- "changesDictionary"
- "changesDictionaryTrimmedByTimeRange:"
- "changesTrimmedByTimeRange:"
- "checkIfCinematic:completionHandler:"
- "checkIfContainsSpatialAudio:completionHandler:"
- "cinematicAudioEffectWithData:"
- "cinematicDisparityTrack"
- "cinematicMetadataTrack"
- "cinematicVideoTrack"
- "class"
- "code"
- "commandBuffer"
- "commandBufferWithDescriptor:"
- "commandBufferWithUnretainedReferences"
- "commandQueue"
- "confidence"
- "conformsToProtocol:"
- "containsObject:"
- "continueTrackingAt:sourceImage:sourceDisparity:"
- "copy"
- "copyMetadataTo:"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createFromPixelbuffer:device:textureCache:read:write:"
- "createRGBA:"
- "createRenderStateWithQuality:"
- "createSampleBufferForRequest:error:"
- "createTextureFromPixelBuffer:device:textureCache:sRGB:"
- "createYUV420:chroma:"
- "creationHash"
- "dataRepresentation"
- "dataValue"
- "dataWithBytes:length:"
- "dealloc"
- "debugDescription"
- "decisionAfterTime:"
- "decisionAtTime:tolerance:"
- "decisionBeforeTime:"
- "decisionNearestTime:"
- "decisionsInTimeRange:"
- "defaultEffectIntensity"
- "defaultRenderingStyle"
- "defaultSpatialAudioTrack"
- "description"
- "deserializeMetadataWithType:fromGlobalMetadata:error:"
- "destinationPixelFormatTypes"
- "detection"
- "detectionAtOrBeforeTime:"
- "detectionForID:"
- "detectionForTrackIdentifier:"
- "detectionGroupID"
- "detectionID"
- "detectionNearestTime:"
- "detectionTrackForDecision:"
- "detectionTrackForID:"
- "detectionType"
- "detectionsInTimeRange:"
- "device"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "discrete"
- "disparityInNormalizedRect:sourceDisparity:detectionType:priorDisparity:"
- "domain"
- "encodeRenderTo:withRenderRequest:"
- "encodeRenderToCommandBuffer:frameAttributes:sourceImage:sourceDisparity:destinationImage:"
- "encodeRenderToCommandBuffer:frameAttributes:sourceImage:sourceDisparity:destinationLuma:destinationChroma:"
- "encodeRenderToCommandBuffer:frameAttributes:sourceImage:sourceDisparity:destinationRGBA:"
- "errorWithDomain:code:userInfo:"
- "f"
- "f16@0:8"
- "f68@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16^{__CVBuffer=}48q56f64"
- "fNumber"
- "finalizeTrack"
- "findAssociatedRemixMetadata:completionHandler:"
- "findObjectAtPoint:sourceImage:"
- "finishDetectionTrack"
- "firstObject"
- "floatValue"
- "focusDetection"
- "focusDisparity"
- "focusDistance"
- "focusGroupIdentifier"
- "focusTrackIdentifier"
- "formatDescriptions"
- "frameAtTime:tolerance:"
- "frameTimingTrack"
- "framesInTimeRange:"
- "getRectForPoint:colorBuffer:"
- "groupDecision"
- "groupIdentifier"
- "hash"
- "height"
- "identifier"
- "indexOfObjectPassingTest:"
- "init"
- "initWithAsset:timebase:"
- "initWithCommandQueue:"
- "initWithCommandQueue:sessionAttributes:preferredTransform:quality:"
- "initWithDataRepresentation:"
- "initWithDescriptor:"
- "initWithDetection:"
- "initWithDetections:"
- "initWithDetections:smooth:"
- "initWithDevice:version:colorInputSize:colorOutputSize:disparitySize:"
- "initWithFocusDisparity:"
- "initWithFocusDistance:"
- "initWithOriginalDetection:"
- "initWithPTGlobalRenderingMetadata:"
- "initWithSampleBuffer:"
- "initWithSampleBuffer:sessionAttributes:"
- "initWithSpatialAudioTrack:metadataBlob:"
- "initWithStartCursor:"
- "initWithTime:detectionGroupID:strong:"
- "initWithTime:detectionID:strong:"
- "initWithTime:detectionType:normalizedRect:focusDisparity:"
- "initWithTime:groupIdentifier:options:"
- "initWithTime:rect:focusDistance:"
- "initWithTime:trackIdentifier:options:"
- "initWithTimedMetadataGroup:"
- "initWithTimedMetadataGroup:sessionAttributes:"
- "insertDebugCaptureBoundary"
- "insertTimeRange:ofCinematicAssetInfo:atTime:error:"
- "insertTimeRange:ofTrack:atTime:error:"
- "intValue"
- "integerValue"
- "internalCNAssetSpatialAudioInfo"
- "internalChanges"
- "internalCinematicAssetInfo"
- "internalDecision"
- "internalDetection"
- "internalFrame"
- "internalMetadata"
- "internalObjectTracker"
- "internalScript"
- "internalSession"
- "internalTapToTrack"
- "internalTrack"
- "invalidDetectionGroupID"
- "invalidDetectionID"
- "isDiscrete"
- "isEnabled"
- "isEqual:"
- "isEqualToString:"
- "isGroupDecision"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPlayable"
- "isProxy"
- "isRGB"
- "isStrongDecision"
- "isSupported"
- "isUserCreated"
- "isUserDecision"
- "isValidDetectionGroupID:"
- "isValidDetectionID:"
- "items"
- "key"
- "label"
- "loadAssociatedTracksOfType:completionHandler:"
- "loadFromAsset:changes:progress:completionHandler:"
- "loadFromAsset:completionHandler:"
- "loadFromCinematicVideoTrack:completionHandler:"
- "loadMetadataForFormat:completionHandler:"
- "loadTracksWithMediaType:completionHandler:"
- "loadValuesAsynchronouslyForKeys:completionHandler:"
- "loadWithAsset:changesDictionary:completion:"
- "majorVersion"
- "makeSampleCursorWithPresentationTimeStamp:"
- "mediaType"
- "minorVersion"
- "mutableCopy"
- "mutableCopyWithZone:"
- "name"
- "naturalSize"
- "normalizedBounds"
- "normalizedRect"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInt:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "objectFromData:error:"
- "objectFromData:withMajorVersion:minorVersion:"
- "originalDetection"
- "originalFNumber"
- "originalFocusDisparity"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "preferredSize"
- "preferredTransform"
- "primaryDecisionAtTime:"
- "progressWithTotalUnitCount:"
- "q"
- "q16@0:8"
- "q24@0:8@16"
- "quality"
- "queue"
- "rect"
- "release"
- "reloadWithChanges:"
- "reloadWithChangesDictionary:"
- "removeAllUserDecisions"
- "removeDetectionTrack:"
- "removeResidencySet:"
- "removeResidencySets:count:"
- "removeTimeRange:"
- "removeTrack:"
- "removeUserDecision:"
- "renderingVersion"
- "resetDetectionTrack"
- "resetTrack"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "sampleDataTrackIDs"
- "secondaryDecisionAtTime:"
- "self"
- "sessionAttributes"
- "setCinematicDisparityTrack:"
- "setCinematicMetadataTrack:"
- "setCinematicVideoTrack:"
- "setConfidence:"
- "setCreationHash:"
- "setDebugRendering:"
- "setDestinationColor:"
- "setDetectionType:"
- "setDialogMixBias:atTime:"
- "setDirection:"
- "setFNumber:"
- "setFocusDisparity:"
- "setGroupIdentifier:"
- "setInputParameters:"
- "setInternalDecision:"
- "setInternalDetection:"
- "setInternalFrame:"
- "setInternalScript:"
- "setInternalTapToTrack:"
- "setInternalTrack:"
- "setLabel:"
- "setMaxSampleCount:"
- "setNormalizedBounds:"
- "setPreferredMinSampleCount:"
- "setPreferredTransform:"
- "setQueue:"
- "setRenderState:"
- "setRenderingStyle:atTime:"
- "setSourceColor:"
- "setSourceDisparity:"
- "setTotalUnitCount:"
- "setTrackID:"
- "setTrackIdentifier:"
- "setUseRGBA:"
- "setUserAperture:"
- "setValue:forKey:"
- "setVerbose:"
- "setWithArray:"
- "sourceColor"
- "sourcePixelFormatTypes"
- "spatialAudioMixMetadata"
- "startTrackingAt:within:sourceImage:sourceDisparity:"
- "statusOfValueForKey:error:"
- "stringByAppendingString:"
- "strongDecision"
- "superclass"
- "time"
- "timeRange"
- "timeRangeOfTransitionAfterDecision:"
- "timeRangeOfTransitionBeforeDecision:"
- "totalUnitCount"
- "trackForDecision:"
- "trackForIdentifier:"
- "trackID"
- "trackIdentifier"
- "tracks"
- "unarchivedObjectOfClasses:fromData:error:"
- "unsignedIntValue"
- "userAperture"
- "userCreated"
- "userDecision"
- "userDecisions"
- "userDecisionsInTimeRange:"
- "v12@?0B8"
- "v16@0:8"
- "v20@0:8f16"
- "v24@0:8@\"<MTLResidencySet>\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@?0@\"CNRenderingSessionAttributes\"8@\"NSError\"16"
- "v24@?0@\"CNScript\"8@\"NSError\"16"
- "v32@0:8@16@?24"
- "v32@0:8r^@16Q24"
- "v48@0:8@16@24@32@?40"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "value"
- "videoCompositionTrackIDs"
- "videoCompositionTracks"
- "width"
- "zone"
- "{?=qiIq}16@0:8"
- "{?={?=qiIq}{?=qiIq}}16@0:8"
- "{?={?=qiIq}{?=qiIq}}24@0:8@16"
- "{CGAffineTransform=\"a\"d\"b\"d\"c\"d\"d\"d\"tx\"d\"ty\"d}"
- "{CGAffineTransform=dddddd}16@0:8"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGSize=dd}16@0:8"

```
