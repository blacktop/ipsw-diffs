## NeutrinoCore

> `/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore`

```diff

-742.0.141.0.0
-  __TEXT.__text: 0x1cb360
-  __TEXT.__auth_stubs: 0x1c10
-  __TEXT.__objc_methlist: 0x12498
-  __TEXT.__const: 0x1e78
-  __TEXT.__gcc_except_tab: 0x7ca4
-  __TEXT.__cstring: 0x228e0
-  __TEXT.__oslogstring: 0x33e1
+750.5.104.0.0
+  __TEXT.__text: 0x1cd318
+  __TEXT.__auth_stubs: 0x1c40
+  __TEXT.__objc_methlist: 0x13a7c
+  __TEXT.__const: 0x1f68
+  __TEXT.__gcc_except_tab: 0x7fa4
+  __TEXT.__cstring: 0x22afb
+  __TEXT.__oslogstring: 0x3548
   __TEXT.__dlopen_cstrs: 0x8a
-  __TEXT.__unwind_info: 0x55e0
-  __TEXT.__objc_classname: 0x2df8
-  __TEXT.__objc_methname: 0x1f513
-  __TEXT.__objc_methtype: 0x5481
-  __TEXT.__objc_stubs: 0x18140
-  __DATA_CONST.__got: 0x18d0
-  __DATA_CONST.__const: 0x2470
-  __DATA_CONST.__objc_classlist: 0xdf8
+  __TEXT.__unwind_info: 0x55d0
+  __TEXT.__objc_classname: 0x2e29
+  __TEXT.__objc_methname: 0x1f823
+  __TEXT.__objc_methtype: 0x560e
+  __TEXT.__objc_stubs: 0x183c0
+  __DATA_CONST.__got: 0x1908
+  __DATA_CONST.__const: 0x24c8
+  __DATA_CONST.__objc_classlist: 0xe08
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x2e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x77f0
+  __DATA_CONST.__objc_selrefs: 0x7900
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x9e8
+  __DATA_CONST.__objc_superrefs: 0x9f8
   __DATA_CONST.__objc_arraydata: 0x968
-  __AUTH_CONST.__auth_got: 0xe20
+  __AUTH_CONST.__auth_got: 0xe38
+  __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x2ee8
-  __AUTH_CONST.__cfstring: 0x105a0
-  __AUTH_CONST.__objc_const: 0x26708
+  __AUTH_CONST.__cfstring: 0x10680
+  __AUTH_CONST.__objc_const: 0x24548
   __AUTH_CONST.__objc_intobj: 0x7f8
   __AUTH_CONST.__objc_dictobj: 0x280
   __AUTH_CONST.__objc_doubleobj: 0xe0
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH.__objc_data: 0xaf0
-  __DATA.__objc_ivar: 0x1210
+  __AUTH.__objc_data: 0xb40
+  __DATA.__objc_ivar: 0x1240
   __DATA.__data: 0x23b8
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x278
+  __DATA.__bss: 0x268
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x80c0
-  __DATA_DIRTY.__bss: 0x188
+  __DATA_DIRTY.__objc_data: 0x8110
+  __DATA_DIRTY.__bss: 0x198
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7159
-  Symbols:   9036
-  CStrings:  11083
+  Functions: 7160
+  Symbols:   9077
+  CStrings:  11159
 
Symbols:
+ _AVMetadataQuickTimeMetadataKeyMake
+ _AVMetadataQuickTimeMetadataKeyModel
+ _AVMetadataQuickTimeMetadataKeySoftware
+ _FigLivePhotoMetadataComputeDeserializationSize
+ _FigLivePhotoMetadataDeserializeIntoBuffer
+ _OBJC_CLASS_$_NUVideoMetadataExtractor
+ _OBJC_CLASS_$_NUVideoTimedMetadata
+ _OBJC_METACLASS_$_NUVideoMetadataExtractor
+ _OBJC_METACLASS_$_NUVideoTimedMetadata
+ __Z24isLivePhotoMetadataTrackP12AVAssetTrack
+ ___chkstk_darwin
+ _kCMTimeRangeInvalid
+ _kFigMetadataDataType_QuickTimeMetadataLivePhotoInfo
+ _objc_retain_x10
CStrings:
+ "\x03\xc1"
+ "\x0f\x03"
+ "+[NUVideoUtilities asset:containsDuplicatePTSSamples:assetTrack:error:]"
+ "+[NUVideoUtilities validateAsset:error:]"
+ "+[NUVideoUtilities validateMainVideoTrack:potentiallyCorruptedRange:error:]"
+ "-[NUVideoMetadataExtractor extractMetadata]"
+ "-[NUVideoMetadataExtractor motionBlurVectorFromMetadata:]"
+ "0 && \"unexpected metadata data type\""
+ "0 && \"unexpected metadata identifier\""
+ "18.0"
+ "18.1"
+ "18.2"
+ "@\"AVAssetTrack\""
+ "Asset does not contain Live Photo metadata track"
+ "B16@?0@\"NUVideoTimedMetadata\"8"
+ "B24@0:8r^{?=S[9f]QQCcC[13c]}16"
+ "B40@0:8@16o^{?={?=qiIq}{?=qiIq}}24o^@32"
+ "B48@0:8@16^B24@32o^@40"
+ "Can't add metadata output for asset"
+ "Can't find enabled video track in asset: %@"
+ "CorruptedMainVideoTrack"
+ "Could not add output to reader"
+ "Could not determine if the asset has corrupted main video frames - assuming it's invalid. %{public}@"
+ "Detected invalid video asset for:\n%{public}@"
+ "Error creating asset reader: %@"
+ "Failed to start reading asset"
+ "Finished metadata extraction"
+ "NUFactory: releasing cached VNSession resources"
+ "NUVideoMetadataExtractor"
+ "NUVideoMetadataExtractor.mm"
+ "NUVideoTimedMetadata"
+ "NU_VISION_SESSION_EVICTION_DELAY"
+ "Starting metadata extraction"
+ "T@\"NSArray\",R,N,VtimedMetadataArray"
+ "TB,R,V_interpolatedFrame"
+ "TB,R,V_interpolatedFrameValid"
+ "Track does not contain V3 metadata"
+ "T{?=[3]},R,V_trajectoryHomography"
+ "T{?=qiIq},R,V_time"
+ "T{CGVector=dd},R,V_estimatedCenterMotion"
+ "T{CGVector=dd},R,V_estimatedMotionBlur"
+ "_estimatedCenterMotion"
+ "_estimatedMotionBlur"
+ "_evictVisionSessionIfNotUsedSince:"
+ "_interpolatedFrame"
+ "_interpolatedFrameValid"
+ "_mdataTrack"
+ "_scheduleEvictionOfVisionSession"
+ "_trajectoryHomography"
+ "_videoTrack"
+ "_visionSessionLastUseTime"
+ "asset:containsDuplicatePTSSamples:assetTrack:error:"
+ "canProvideMetadataForAVAsset:"
+ "centerMotionVectorFromMetadata:"
+ "depthData"
+ "err == noErr"
+ "estimatedCenterMotion"
+ "estimatedMotionBlur"
+ "extractMetadata"
+ "iPhone"
+ "imageWithDepthData:"
+ "init is not a valid initializer"
+ "initWithAVAsset:"
+ "interpolatedFrame"
+ "interpolatedFrameFromMetadata:"
+ "interpolatedFrameValid"
+ "interpolatedFrameValidFromMetadata:"
+ "mdataGroup.items.count == 1"
+ "mdta/com.apple.quicktime.live-photo-info"
+ "metadataTrackWithLivePhotoInfoInAsset:"
+ "motionBlurVectorFromMetadata:"
+ "ndcMetadataTransform"
+ "outDuplicatePTS != NULL"
+ "outRange != NULL"
+ "pxlMetadataTransform"
+ "releaseCachedResources"
+ "setEstimatedCenterMotion:"
+ "setEstimatedMotionBlur:"
+ "setInterpolatedFrame:"
+ "setInterpolatedFrameValid:"
+ "setTrajectoryHomography:"
+ "setVisionSessionEvictionDelay:"
+ "timedMetadataArray"
+ "trajectoryHomography"
+ "trajectoryeHomographyFromMetadata:"
+ "v1"
+ "v32@0:8{CGVector=dd}16"
+ "v32@?0@\"NUVideoTimedMetadata\"8Q16^B24"
+ "v64@0:8{?=[3]}16"
+ "validateAsset:error:"
+ "validateMainVideoTrack:potentiallyCorruptedRange:error:"
+ "visionSessionEvictionDelay"
+ "{?=\"columns\"[3]}"
+ "{?=[3]}16@0:8"
+ "{?=[3]}24@0:8r^{?=S[9f]QQCcC[13c]}16"
+ "{CGVector=\"dx\"d\"dy\"d}"
+ "{CGVector=dd}16@0:8"
+ "{CGVector=dd}24@0:8r^{FigLivePhotoMetadata=I{FigLivePhotoMetadataV1Struct=fqffffffccSI[0{FigLivePhotoDetectedFaceV1Struct=qffffisS}]}}16"
- "\x0f\x01"
- "!isnan(order)"
- "+[NUVideoUtilities assetContainsDuplicatePTSSamples:assetTrack:error:]"
- "+[NUVideoUtilities validateSemanticStyleAsset:error:]"
- "Detected invalid video asset for semantic styles:\n%{public}@"
- "Failed to validate semantic style video asset: %{public}@"
- "NU_INPAINT_ENABLE_REFINEMENT"
- "NU_INPAINT_SHOWS_SURROUND_OUTLINE"
- "T@\"NURenderNode\",&,N,V_lastFrameRenderNode"
- "TB,N,V_shouldKeepLastFrameRenderNode"
- "_lastFrameRenderNode"
- "_shouldKeepLastFrameRenderNode"
- "assetContainsDuplicatePTSSamples:assetTrack:error:"
- "inpaintEnablesRefinementPass"
- "inpaintShowsSurroundOutline"
- "isAssetStyled:"
- "lastFrameRenderNode"
- "setInpaintEnablesRefinementPass:"
- "setInpaintShowsSurroundOutline:"
- "setLastFrameRenderNode:"
- "setShouldKeepLastFrameRenderNode:"
- "shouldKeepLastFrameRenderNode"
- "validateSemanticStyleAsset:error:"

```
