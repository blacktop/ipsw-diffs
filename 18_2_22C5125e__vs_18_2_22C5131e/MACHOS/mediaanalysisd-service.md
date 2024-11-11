## mediaanalysisd-service

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service`

```diff

-290.9.2.0.0
-  __TEXT.__text: 0x19d2f0
+290.11.2.0.0
+  __TEXT.__text: 0x19e720
   __TEXT.__auth_stubs: 0x1110
-  __TEXT.__objc_stubs: 0x12800
-  __TEXT.__objc_methlist: 0x8424
-  __TEXT.__cstring: 0x14ad3
-  __TEXT.__objc_classname: 0x1bbe
-  __TEXT.__objc_methname: 0x190d2
-  __TEXT.__objc_methtype: 0x3681
+  __TEXT.__objc_stubs: 0x12960
+  __TEXT.__objc_methlist: 0x84ec
+  __TEXT.__cstring: 0x15085
+  __TEXT.__objc_classname: 0x1bd1
+  __TEXT.__objc_methname: 0x19317
+  __TEXT.__objc_methtype: 0x36de
   __TEXT.__const: 0x4a0
-  __TEXT.__gcc_except_tab: 0x2fc08
-  __TEXT.__oslogstring: 0x1fcc7
+  __TEXT.__gcc_except_tab: 0x2fdd8
+  __TEXT.__oslogstring: 0x1fe58
   __TEXT.__dlopen_cstrs: 0x60a
-  __TEXT.__unwind_info: 0x5ca0
+  __TEXT.__unwind_info: 0x5cd8
   __DATA_CONST.__auth_got: 0x8a0
-  __DATA_CONST.__got: 0xdb8
-  __DATA_CONST.__const: 0x5d00
-  __DATA_CONST.__cfstring: 0xd4e0
-  __DATA_CONST.__objc_classlist: 0x650
+  __DATA_CONST.__got: 0xdc0
+  __DATA_CONST.__const: 0x6060
+  __DATA_CONST.__cfstring: 0xdf40
+  __DATA_CONST.__objc_classlist: 0x658
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_classrefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x4e0
+  __DATA_CONST.__objc_superrefs: 0x4e8
   __DATA_CONST.__objc_intobj: 0x2370
   __DATA_CONST.__objc_arraydata: 0x7e8
   __DATA_CONST.__objc_arrayobj: 0x5b8
   __DATA_CONST.__objc_doubleobj: 0xd0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x13840
-  __DATA.__objc_selrefs: 0x4f48
-  __DATA.__objc_ivar: 0x1074
-  __DATA.__objc_data: 0x3f20
+  __DATA.__objc_const: 0x13a50
+  __DATA.__objc_selrefs: 0x4fa8
+  __DATA.__objc_ivar: 0x1094
+  __DATA.__objc_data: 0x3f70
   __DATA.__data: 0xa68
   __DATA.__bss: 0x6a0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 4652
-  Symbols:   723
-  CStrings:  8883
+  Functions: 4679
+  Symbols:   724
+  CStrings:  9003
 
Symbols:
+ _OBJC_CLASS_$_NSNull
CStrings:
+ "%!@(MISSING)/%!@(MISSING)"
+ "-[VCPDatabaseWriter(ProcessingStatus) fetchProcessingErrorCode:errorLine:taskID:localIndentifier:]"
+ "-[VCPDatabaseWriter(ProcessingStatus) updateProcessingStatus:andNextAttemptDate:andErrorCode:andErrorLine:forLocalIdentifier:andTaskID:]"
+ "@\"VCPClientHandler\""
+ "@108@0:8@16Q24Q32@40Q48B56@60B68@72B80@84Q92Q100"
+ "@40@0:8Q16Q24Q32"
+ "AdaptiveSegment"
+ "Audio"
+ "Blur"
+ "CNNBlur"
+ "CNNBlurEspresso"
+ "CNNBlurMPS"
+ "Effects"
+ "EmbeddingSummarization"
+ "EndOfRange"
+ "Exif"
+ "Failed to alloc MADErrorDescriptor during fail retrieval for activity %!d(MISSING)"
+ "FullVideo"
+ "HomeKitMotion"
+ "ImageBackbone"
+ "ImageBlur"
+ "ImageCaption"
+ "ImageComposition"
+ "ImageExposure"
+ "ImageExposurePre"
+ "ImageFaceExpression"
+ "ImageFaceQuality"
+ "ImageHands"
+ "ImageHumanAction"
+ "ImageHumanPose"
+ "ImageHumanPoseHolistic"
+ "ImageHumanPoseTopDown"
+ "ImageLivePhotoBlur"
+ "ImageMotionFlow"
+ "ImagePets"
+ "ImagePetsKeypoints"
+ "ImageQuality"
+ "ImageSaliency"
+ "ImageSaliencyBinary"
+ "ImageSaliencyFull"
+ "ImageSaliencyFullEspresso"
+ "InterAsset"
+ "Invalid"
+ "Junk"
+ "LightMotion"
+ "LightVideo"
+ "LivePhotoKeyFrame"
+ "Loudness"
+ "MADErrorDescriptor"
+ "MADMovieBlastDoor"
+ "Media"
+ "MotionFlow"
+ "MotionFlowSubtleMotion"
+ "MovieCuration"
+ "MovieHighlight"
+ "Parallax"
+ "Photo"
+ "Reporting daily top%!l(MISSING)ld Failure: %!@(MISSING)"
+ "SELECT errorCode, errorLine FROM ProcessingStatus WHERE taskID=(?) AND localIdentifier=(?);"
+ "SceneChange"
+ "SettlingEffect"
+ "SmartStyleMeta"
+ "StillImageMeta"
+ "TQ,N,V_errorCode"
+ "TQ,N,V_errorLine"
+ "TQ,R,N,V_previousErrorCode"
+ "TQ,R,N,V_previousErrorLine"
+ "TQ,V_count"
+ "TQ,V_errorCode"
+ "TQ,V_errorLine"
+ "Trying fetchProcessingErrorCodeCounts from DB returned err %!d(MISSING) for activity %!d(MISSING)"
+ "UPDATE ProcessingStatus SET status=(?), nextAttemptDate=(?), errorCode=(?), errorLine=(?) WHERE taskID=(?) AND localIdentifier=(?);"
+ "VCPAction"
+ "VCPColorNormalization"
+ "VCPFace"
+ "VCPPre"
+ "VCPSMO"
+ "VCPTrim"
+ "VCPWallpaper"
+ "Video"
+ "VideoActivity"
+ "VideoCNN"
+ "VideoCaption"
+ "VideoFaceMesh"
+ "VideoFacePose"
+ "VideoGlobal"
+ "VideoHumanAction"
+ "VideoKeyFrame"
+ "VideoMeta"
+ "VideoMetaFace"
+ "VideoMetaFocus"
+ "VideoMetaLivePhotoMeta"
+ "VideoMetaMotion"
+ "VideoMetaOrientation"
+ "VideoMetaSegment"
+ "VideoPets"
+ "VideoPetsAction"
+ "VideoSaliency"
+ "WatchFace"
+ "[MADEmbeddingStoreClientHandler] Failed to open photo library at %!@(MISSING)"
+ "_clientHandler"
+ "_errorCode"
+ "_errorLine"
+ "_previousErrorCode"
+ "_previousErrorLine"
+ "compareByCount:"
+ "embeddingStoreDirectoryForPhotoLibrary:"
+ "entryWithAsset:previousStatus:previousAttempts:lastAttemptDate:analysisTypes:imageOnlyAnalysis:existingAnalysis:isAnalysisFromComputeSync:downloadResource:needDownload:acceptableResources:previousErrorCode:previousErrorLine:"
+ "errorCode"
+ "errorLine"
+ "fetchProcessingErrorCode:errorLine:taskID:localIndentifier:"
+ "i48@0:8^Q16^Q24Q32@40"
+ "i64@0:8Q16@24Q32Q40@48Q56"
+ "initWithAsset:previousStatus:previousAttempts:lastAttemptDate:analysisTypes:imageOnlyAnalysis:existingAnalysis:isAnalysisFromComputeSync:downloadResource:needDownload:acceptableResources:previousErrorCode:previousErrorLine:"
+ "initWithErrorCode:count:errorLine:"
+ "null"
+ "previousErrorCode"
+ "previousErrorLine"
+ "q24@?0@\"MADErrorDescriptor\"8@\"MADErrorDescriptor\"16"
+ "setCount:"
+ "setErrorCode:"
+ "setErrorLine:"
+ "updateProcessingStatus:andNextAttemptDate:andErrorCode:andErrorLine:forLocalIdentifier:andTaskID:"
- "-[VCPDatabaseWriter(ProcessingStatus) updateProcessingStatus:andNextAttemptDate:forLocalIdentifier:andTaskID:]"
- "@92@0:8@16Q24Q32@40Q48B56@60B68@72B80@84"
- "UPDATE ProcessingStatus SET status=(?), nextAttemptDate=(?) WHERE taskID=(?) AND localIdentifier=(?);"
- "embeddingStoreDirectoryForPhotoLibraryURL:"
- "entryWithAsset:previousStatus:previousAttempts:lastAttemptDate:analysisTypes:imageOnlyAnalysis:existingAnalysis:isAnalysisFromComputeSync:downloadResource:needDownload:acceptableResources:"
- "initWithAsset:previousStatus:previousAttempts:lastAttemptDate:analysisTypes:imageOnlyAnalysis:existingAnalysis:isAnalysisFromComputeSync:downloadResource:needDownload:acceptableResources:"

```
