## MediaAnalysis

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis`

```diff

-305.10.3.0.0
-  __TEXT.__text: 0x41b648
-  __TEXT.__auth_stubs: 0x3510
-  __TEXT.__objc_methlist: 0x1ac18
-  __TEXT.__const: 0x14678
-  __TEXT.__gcc_except_tab: 0x5b810
-  __TEXT.__cstring: 0x1fae3
-  __TEXT.__oslogstring: 0x25f8b
+305.13.7.0.0
+  __TEXT.__text: 0x420bc8
+  __TEXT.__auth_stubs: 0x3520
+  __TEXT.__objc_methlist: 0x1ad10
+  __TEXT.__const: 0x146a8
+  __TEXT.__gcc_except_tab: 0x5c5a4
+  __TEXT.__cstring: 0x1ff33
+  __TEXT.__oslogstring: 0x267bb
   __TEXT.__dlopen_cstrs: 0x579
   __TEXT.__ustring: 0x40
   __TEXT.__swift5_typeref: 0x94

   __TEXT.__swift5_fieldmd: 0x44
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x101e0
+  __TEXT.__unwind_info: 0x102c8
   __TEXT.__eh_frame: 0x248
-  __TEXT.__objc_classname: 0x3ce7
-  __TEXT.__objc_methname: 0x3a3a4
-  __TEXT.__objc_methtype: 0xcd65
-  __TEXT.__objc_stubs: 0x27340
-  __DATA_CONST.__got: 0x19a0
-  __DATA_CONST.__const: 0x67b8
-  __DATA_CONST.__objc_classlist: 0x10c8
+  __TEXT.__objc_classname: 0x3cfd
+  __TEXT.__objc_methname: 0x3a705
+  __TEXT.__objc_methtype: 0xcd83
+  __TEXT.__objc_stubs: 0x27540
+  __DATA_CONST.__got: 0x19f8
+  __DATA_CONST.__const: 0x6820
+  __DATA_CONST.__objc_classlist: 0x10d0
   __DATA_CONST.__objc_catlist: 0x198
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbd90
+  __DATA_CONST.__objc_selrefs: 0xbe28
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0xde8
+  __DATA_CONST.__objc_superrefs: 0xdf0
   __DATA_CONST.__objc_arraydata: 0x1080
-  __AUTH_CONST.__auth_got: 0x1aa0
+  __AUTH_CONST.__auth_got: 0x1aa8
   __AUTH_CONST.__auth_ptr: 0xf8
-  __AUTH_CONST.__const: 0x56a8
-  __AUTH_CONST.__cfstring: 0x16200
-  __AUTH_CONST.__objc_const: 0x347a0
+  __AUTH_CONST.__const: 0x56c8
+  __AUTH_CONST.__cfstring: 0x16560
+  __AUTH_CONST.__objc_const: 0x349e8
   __AUTH_CONST.__objc_floatobj: 0x250
   __AUTH_CONST.__objc_doubleobj: 0x410
-  __AUTH_CONST.__objc_intobj: 0x2b08
+  __AUTH_CONST.__objc_intobj: 0x2b20
   __AUTH_CONST.__objc_arrayobj: 0xaf8
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0xc58
+  __AUTH.__objc_data: 0xca8
   __AUTH.__data: 0x28
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x9d0
-  __DATA.__objc_ivar: 0x3048
+  __DATA.__objc_ivar: 0x3074
   __DATA.__data: 0x18f8
   __DATA.__bss: 0x999
   __DATA.__common: 0x3b9

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 15643
-  Symbols:   19498
-  CStrings:  17926
+  Functions: 15676
+  Symbols:   19557
+  CStrings:  18017
 
Symbols:
+ _MediaAnalysisResultKeyFrameEmbeddingAttributeKey
+ _MediaAnalysisResultKeyFrameFaceAttributeKey
+ _MediaAnalysisResultKeyFrameHumanActionAttributeKey
+ _MediaAnalysisResultKeyFrameSceneAttributeKey
+ _MediaAnalysisResultPersonIDAttributeKey
+ _PHMediaProcessingAssetCountLivePhotoKey
+ _PHMediaProcessingAssetCountStillImageKey
+ _PHMediaProcessingAssetCountVideoKey
+ _VCPAnalysisCountStickyFailedKey
+ _VCPAnalysisStickyFailureAttemptsThreshold
+ _VCPKeyValueLastPerAssetBiomeReportBucket
+ _VCPKeyValueLastPerAssetBiomeReportEndTimestamp
+ _VCPKeyValueLastPerAssetBiomeReportStartTimestamp
+ _VCPKeyValueLastPerLibraryBiomeReportEndTimestamp
+ _VCPKeyValueLastPerLibraryBiomeReportStartTimestamp
+ _VCPMediaAnalyzerOption_MetadataWithHighlight
+ _VCPMediaAnalyzerOption_PersonIDWithHighlight
+ _VCPOSMajorOfLastVersionUpdateKeyForTask
+ _VCPOSMinorOfLastVersionUpdateKeyForTask
+ _kCVImageBufferTransferFunction_Linear
+ _kVTCompressionPropertyKey_ColorPrimaries
+ _kVTCompressionPropertyKey_HDRMetadataInsertionMode
+ _kVTCompressionPropertyKey_ProfileLevel
+ _kVTCompressionPropertyKey_TransferFunction
+ _kVTCompressionPropertyKey_YCbCrMatrix
+ _kVTHDRMetadataInsertionMode_Auto
+ _kVTProfileLevel_HEVC_Main10_AutoLevel
+ _mach_continuous_time
CStrings:
+ "\x04\x11\xd6\x15\x88"
+ "\x0f\x0e\x83"
+ "  Failed to delete FRC files with issues"
+ "%@ Complete"
+ "%@ Complete with on-demand analysis"
+ "%@ Complete without on-demand disabled"
+ "%@ Detected %lu faces, identifying ..."
+ "%@ Detected %lu faces, identifying top %lu faces (by confidence) ..."
+ "%@ Failed to classify face (%@) - %@; skipping"
+ "%@ Failed to configuate VNCreateFaceprintRequest"
+ "%@ Failed to configuate VNDetectFaceRectanglesRequest"
+ "%@ Failed to detect faces - %@"
+ "%@ Failed to fetch person with identifier %@ and mdID %@; skipping"
+ "%@ Failed to load image (%d) - %@"
+ "%@ Failed to load low-res image (%d) - %@"
+ "%@ Failed to print faces - %@"
+ "%@ Identified %lu faces"
+ "%@ No face detected from CVPixelBuffer"
+ "%@ No face to identify from CVPixelBuffer"
+ "%@ No valid identification to face (%@); skipping"
+ "%@ Prediction: %@, (mdid: %@), confidence: %.3f at %@"
+ "%@ Running request %@ ..."
+ "%{public, signpost.description:begin_time}llu  enableTelemetry=YES "
+ "%{public, signpost.description:begin_time}llu Component=%{public, signpost.telemetry:string1}s  enableTelemetry=YES "
+ "%{public, signpost.description:begin_time}llu QoS=%{public, signpost.telemetry:string1}s CalibrationRequested=%{public, signpost.telemetry:string2}s TextEncoderIsWarm=%{public, signpost.telemetry:number1}lld ContextLength=%{public, signpost.telemetry:number2}lld  enableTelemetry=YES "
+ "-[VCPDatabaseReader countForTaskID:minimumAttempts:]"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/SmartStyleMetaAnalyzer.mm"
+ "@48@0:8@16r^{?={?=qiIq}{?=qiIq}}24Q32^f40"
+ "Activity=%{public, signpost.telemetry:string1}s QoS=%{public, signpost.telemetry:string2}s  enableTelemetry=YES "
+ "Client=%{public, signpost.telemetry:string1}s CountFaces=%{public, signpost.telemetry:number1}lld  enableTelemetry=YES "
+ "Client=%{public, signpost.telemetry:string1}s CountFaces=%{public, signpost.telemetry:number1}lld CountLibraryAssets=%{public, signpost.telemetry:number2}lld  enableTelemetry=YES "
+ "ExecuteCalibration"
+ "ExecuteSafety"
+ "ExecuteTextEncoder"
+ "ExecuteThreshold"
+ "FaceAnalysisOSMajorOfLastVersionUpdate"
+ "FaceAnalysisOSMinorOfLastVersionUpdate"
+ "Failed to load image"
+ "Failure"
+ "FullImageAnalysisOSMajorOfLastVersionUpdate"
+ "FullImageAnalysisOSMinorOfLastVersionUpdate"
+ "LastPerAssetBiomeReportBucket"
+ "LastPerAssetBiomeReportEndTimestamp"
+ "LastPerAssetBiomeReportStartTimestamp"
+ "LastPerLibraryBiomeReportEndTimestamp"
+ "LastPerLibraryBiomeReportStartTimestamp"
+ "LoadCalibration"
+ "LoadSafety"
+ "LoadTextEncoder"
+ "MADTextEmbeddingThreshold_processEmbedding"
+ "MediaAnalysisOSMajorOfLastVersionUpdate"
+ "MediaAnalysisOSMinorOfLastVersionUpdate"
+ "Memory Full error!"
+ "MetadataWithHighlight"
+ "Mismatch in number of samples"
+ "Mismatch in sample PTS"
+ "OCRAnalysisOSMajorOfLastVersionUpdate"
+ "OCRAnalysisOSMinorOfLastVersionUpdate"
+ "PECAnalysisOSMajorOfLastVersionUpdate"
+ "PECAnalysisOSMinorOfLastVersionUpdate"
+ "PersonIDWithHighlight"
+ "QoS=%{public, signpost.telemetry:string1}s Status=%{public, signpost.telemetry:string2}s ContextLength=%{public, signpost.telemetry:number1}lld  enableTelemetry=YES "
+ "QoS=%{public, signpost.telemetry:string1}s Status=%{public, signpost.telemetry:string2}s IsWarm=%{public, signpost.telemetry:number1}lld ContextLength=%{public, signpost.telemetry:number2}lld  enableTelemetry=YES "
+ "Result=%{public, signpost.telemetry:string1}s Client=%{public, signpost.telemetry:string2}s  enableTelemetry=YES "
+ "Result=%{public, signpost.telemetry:string1}s Client=%{public, signpost.telemetry:string2}s CountFaces=%{public, signpost.telemetry:number1}lld CountLibraryAssets=%{public, signpost.telemetry:number2}lld  enableTelemetry=YES "
+ "SELECT COUNT(*) FROM ProcessingStatus WHERE taskID=(?) AND attempts>=(?);"
+ "Sample has different decode and presentation timestamps"
+ "SceneAnalysisOSMajorOfLastVersionUpdate"
+ "SceneAnalysisOSMinorOfLastVersionUpdate"
+ "TextEmbeddingGeneration"
+ "T{?=qiIq},N,V_duration"
+ "VCPClassificationInfo"
+ "VisualSearchAnalysisOSMajorOfLastVersionUpdate"
+ "VisualSearchAnalysisOSMinorOfLastVersionUpdate"
+ "[%@] Failed to get processed assets breakdown count from Photos (%@)"
+ "[%@] Failed to get total assets breakdown count from Photos (%@)"
+ "[%@][%@]"
+ "[MediaAnalyzer]Embedding add to Highlight - no highlight or embedding"
+ "[MediaAnalyzer]Embedding add to Highlight - no highlight or human action classification results"
+ "[MediaAnalyzer]Embedding add to Highlight - no highlight or scene classification results"
+ "[MediaAnalyzer]People UUID add to Highlight - no face results"
+ "[MediaAnalyzer]People UUID add to Highlight - no highlight or face results"
+ "_addEmbeddingToHighlightResults:"
+ "_addFaceIDToHighlightResults:forAsset:"
+ "_addHumanActionIDToHighlightResults:"
+ "_addMetadataToHighlightResults:forAsset:"
+ "_addSceneIDToHighlightResults:"
+ "_extendedContextLength"
+ "_isWarm"
+ "_originalLearnedPTSList"
+ "_originalLinearThumbnailPTSList"
+ "_originalVideoPTSList"
+ "_transferSessionDelta"
+ "_updatedLearnedPTSList"
+ "_updatedLinearThumbnailPTSList"
+ "_updatedVideoPTSList"
+ "appendOutput:toWriterInput:withUpdatedTimeFrom:withOriginalTimeFrom:"
+ "checkDecodeIssuesForTrack:"
+ "copyPixelBufferForDelta:toPixelBuffer:"
+ "countForTaskID:minimumAttempts:"
+ "countOfAssetsByMediaTypeForMediaProcessingTaskID:processed:algorithmVersion:error:"
+ "createDecoderForTrack:timerange:forAnalysisTypes:decodedFrameRate:"
+ "findLinearThumbnailTrack:"
+ "finishVideoSamplePTSUpdate"
+ "getOriginalSamplesListforTrack:"
+ "initWithTimeRange:confidence:"
+ "isTextEncoderWarm"
+ "isWarm"
+ "keyFrameEmbedding"
+ "keyFrameFace"
+ "keyFrameHumanAction"
+ "keyFrameScene"
+ "setIncludeTorsoAndFaceDetectionData:"
+ "sticky-failed"
+ "unsignedLongLongValue"
+ "update:confidence:"
+ "updateSamplesPTSForList:toList:"
+ "v68@0:8{?={?=qiIq}{?=qiIq}}16f64"
- "\x04\x11\xd6\x15\x82"
- "\x0f\x0es"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/SmartStyleMetaAnalyzer.m"
- "@52@0:8@16r^{?={?=qiIq}{?=qiIq}}24Q32^f40B48"
- "Activity=%{public, signpost.telemetry:string1}s QoS=%{public, signpost.telemetry:string2}s"
- "Result=%{public, signpost.telemetry:string1}s"
- "Result=%{public, signpost.telemetry:string1}s CountFaces=%{public, signpost.telemetry:number1}lld CountLibraryAssets=%{public, signpost.telemetry:number2}lld"
- "[%@] Detected %lu faces, identifying ..."
- "[%@] Detected %lu faces, identifying top %lu faces (by confidence) ..."
- "[%@] Failed to classify face (%@) - %@; skipping"
- "[%@] Failed to configuate VNCreateFaceprintRequest"
- "[%@] Failed to configuate VNDetectFaceRectanglesRequest"
- "[%@] Failed to detect faces - %@"
- "[%@] Failed to fetch person with identifier %@ and mdID %@; skipping"
- "[%@] Failed to print faces - %@"
- "[%@] Identified %lu faces"
- "[%@] No face detected from CVPixelBuffer"
- "[%@] No face to identify from CVPixelBuffer"
- "[%@] No valid identification to face (%@); skipping"
- "[%@] complete with on-demand analysis"
- "[%@] complete without on-demand process"
- "[%@] low res image loading failed"
- "[%@] prediction: %@, (mdid: %@), confidence: %.3f at %@"
- "[%@] running request %@ ..."
- "appendOutput:toWriterInput:"
- "createDecoderForTrack:timerange:forAnalysisTypes:decodedFrameRate:withLossySetting:"
- "mediaAnalysisAttributes.mediaAnalysisVersion >= %d"

```
