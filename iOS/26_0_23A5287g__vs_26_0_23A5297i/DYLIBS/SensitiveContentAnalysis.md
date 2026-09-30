## SensitiveContentAnalysis

> `/System/Library/Frameworks/SensitiveContentAnalysis.framework/SensitiveContentAnalysis`

```diff

-119.1.1.0.0
-  __TEXT.__text: 0x8d918
-  __TEXT.__auth_stubs: 0x23e0
-  __TEXT.__objc_methlist: 0xe9c
-  __TEXT.__const: 0x7370
-  __TEXT.__cstring: 0x2ffb
-  __TEXT.__oslogstring: 0x1664
-  __TEXT.__gcc_except_tab: 0x310
+123.0.0.0.0
+  __TEXT.__text: 0x94458
+  __TEXT.__auth_stubs: 0x2480
+  __TEXT.__objc_methlist: 0xef4
+  __TEXT.__const: 0x7750
+  __TEXT.__cstring: 0x32db
+  __TEXT.__oslogstring: 0x18a4
+  __TEXT.__gcc_except_tab: 0x33c
   __TEXT.__dlopen_cstrs: 0x1ee
-  __TEXT.__swift5_typeref: 0x2b85
-  __TEXT.__constg_swiftt: 0x1ef8
-  __TEXT.__swift5_reflstr: 0x1230
-  __TEXT.__swift5_fieldmd: 0x18bc
-  __TEXT.__swift5_proto: 0x75c
-  __TEXT.__swift5_types: 0x2c0
-  __TEXT.__swift5_assocty: 0x520
-  __TEXT.__swift5_capture: 0xdb0
-  __TEXT.__swift5_builtin: 0x168
+  __TEXT.__swift5_typeref: 0x2c3f
+  __TEXT.__constg_swiftt: 0x1f9c
+  __TEXT.__swift5_reflstr: 0x13d0
+  __TEXT.__swift5_fieldmd: 0x1a0c
+  __TEXT.__swift5_proto: 0x78c
+  __TEXT.__swift5_types: 0x2ec
+  __TEXT.__swift5_assocty: 0x5b0
+  __TEXT.__swift5_capture: 0xde4
+  __TEXT.__swift5_builtin: 0x1cc
   __TEXT.__swift_as_entry: 0x1dc
   __TEXT.__swift_as_ret: 0x1bc
-  __TEXT.__swift5_mpenum: 0x48
+  __TEXT.__swift5_mpenum: 0x6c
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__unwind_info: 0x2fa0
-  __TEXT.__eh_frame: 0x5fd8
-  __TEXT.__objc_classname: 0x19e
-  __TEXT.__objc_methname: 0x24d5
-  __TEXT.__objc_methtype: 0x566
-  __TEXT.__objc_stubs: 0x1040
-  __DATA_CONST.__got: 0x608
-  __DATA_CONST.__const: 0x520
-  __DATA_CONST.__objc_classlist: 0x148
+  __TEXT.__unwind_info: 0x30c8
+  __TEXT.__eh_frame: 0x6098
+  __TEXT.__objc_classname: 0x1b6
+  __TEXT.__objc_methname: 0x26cc
+  __TEXT.__objc_methtype: 0x5ad
+  __TEXT.__objc_stubs: 0x1100
+  __DATA_CONST.__got: 0x630
+  __DATA_CONST.__const: 0x540
+  __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x998
+  __DATA_CONST.__objc_selrefs: 0xa10
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x1200
-  __AUTH_CONST.__const: 0x5048
+  __DATA_CONST.__objc_superrefs: 0x50
+  __AUTH_CONST.__auth_got: 0x1250
+  __AUTH_CONST.__const: 0x5358
   __AUTH_CONST.__cfstring: 0x200
-  __AUTH_CONST.__objc_const: 0x2b18
-  __AUTH.__objc_data: 0x998
-  __AUTH.__data: 0x880
-  __DATA.__objc_ivar: 0x64
-  __DATA.__data: 0x1080
-  __DATA.__bss: 0xadb0
-  __DATA.__common: 0x128
+  __AUTH_CONST.__objc_const: 0x2c80
+  __AUTH.__objc_data: 0x9e0
+  __AUTH.__data: 0x890
+  __DATA.__objc_ivar: 0x6c
+  __DATA.__data: 0x10e0
+  __DATA.__bss: 0xb3f0
+  __DATA.__common: 0x130
   __DATA_DIRTY.__objc_data: 0x6f0
   __DATA_DIRTY.__data: 0xbf0
   __DATA_DIRTY.__bss: 0x14d0
   __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9F40511E-527A-39F7-A15A-03A0A87BF79B
-  Functions: 3676
-  Symbols:   2381
-  CStrings:  967
+  UUID: 36B0B4FA-AB59-32FB-8F8E-5B3B29E3EC0F
+  Functions: 3794
+  Symbols:   2463
+  CStrings:  1017
 
Symbols:
+ -[SCMADVideoSession processPixelBuffer:timestamp:orientation:regionOfInterest:resultHandler:]
+ -[SCMADVideoSessionResult .cxx_destruct]
+ -[SCMADVideoSessionResult analysis]
+ -[SCMADVideoSessionResult confidenceScore]
+ -[SCMADVideoSessionResult initWithAnalysis:confidenceScore:]
+ GCC_except_table9
+ _CGRectEqualToRect
+ _CGRectGetHeight
+ _CGRectGetWidth
+ _OBJC_CLASS_$_NSValue
+ _OBJC_CLASS_$_SCMADVideoSessionResult
+ _OBJC_IVAR_$_SCMADVideoSessionResult._analysis
+ _OBJC_IVAR_$_SCMADVideoSessionResult._confidenceScore
+ _OBJC_METACLASS_$_SCMADVideoSessionResult
+ _SCIsVCPDecompressionSessionSetContentAnalyzer2Available
+ _SCVCPDecompressionSessionSetContentAnalyzer2
+ _SCVCPDecompressionSessionSetContentAnalyzer2.cold.1
+ _VTDecompressionSessionSetContentAnalyzer2
+ _VideoProcessingLibrary
+ _VideoProcessingLibraryCore
+ __OBJC_$_INSTANCE_METHODS_SCMADVideoSessionResult
+ __OBJC_$_INSTANCE_VARIABLES_SCMADVideoSessionResult
+ __OBJC_$_PROP_LIST_SCMADVideoSessionResult
+ __OBJC_CLASS_RO_$_SCMADVideoSessionResult
+ __OBJC_METACLASS_RO_$_SCMADVideoSessionResult
+ __PROPERTIES__TtC24SensitiveContentAnalysis11SampleTimer
+ ___93-[SCMADVideoSession processPixelBuffer:timestamp:orientation:regionOfInterest:resultHandler:]_block_invoke
+ ___getMADVideoSessionFramePropertiesClass_block_invoke
+ ___getVCPDecompressionSessionSetContentAnalyzer2SymbolLoc_block_invoke
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_memcpy32_8
+ ___swift_memcpy57_8
+ ___swift_memcpy82_8
+ ___swift_memcpy98_8
+ _associated conformance So28SCVideoStreamAnalysisOptionsVs10SetAlgebraSCSQ
+ _associated conformance So28SCVideoStreamAnalysisOptionsVs10SetAlgebraSCs25ExpressibleByArrayLiteral
+ _associated conformance So28SCVideoStreamAnalysisOptionsVs9OptionSetSCSY
+ _associated conformance So28SCVideoStreamAnalysisOptionsVs9OptionSetSCs0F7Algebra
+ _block_copy_helper.16
+ _block_copy_helper.33
+ _block_copy_helper.69
+ _block_copy_helper.79
+ _block_descriptor.18
+ _block_descriptor.35
+ _block_descriptor.71
+ _block_descriptor.81
+ _block_destroy_helper.17
+ _block_destroy_helper.34
+ _block_destroy_helper.70
+ _block_destroy_helper.80
+ _getMADVideoSessionFramePropertiesClass
+ _getMADVideoSessionFramePropertiesClass.softClass
+ _getVCPDecompressionSessionSetContentAnalyzer2SymbolLoc
+ _getVCPDecompressionSessionSetContentAnalyzer2SymbolLoc.ptr
+ _kVTDecodeFrameOptionKey_ContentAnalyzerCropRectangle
+ _kVTDecodeFrameOptionKey_ContentAnalyzerRotation
+ _objc_msgSend$confidenceTypeN
+ _objc_msgSend$initWithAnalysis:confidenceScore:
+ _objc_msgSend$processPixelBuffer:frameProperties:resultHandler:
+ _objc_msgSend$setOrientation:
+ _objc_msgSend$setRegionOfInterest:
+ _objc_msgSend$setTimestamp:
+ _objc_retainBlock
+ _objc_retain_x28
+ _symbolic SDy_____Say_____y_____GGG So13audit_token_ta 24SensitiveContentAnalysis17ResumedConnectionV AC019VideoStreamAnalyzerG6ConfigV
+ _symbolic Si6offset______7elementt 24SensitiveContentAnalysis19SamplingPrioritizerC5Entry33_D84D1D7BE99E0E8C15C8B3F40A8E9BD2LLV
+ _symbolic _____ 12CoreGraphics7CGFloatV
+ _symbolic _____ 24SensitiveContentAnalysis12FrameDetailsV
+ _symbolic _____ 24SensitiveContentAnalysis19VideoStreamAnalyzerC7SamplerC5StatsV
+ _symbolic _____ 24SensitiveContentAnalysis6SampleO
+ _symbolic _____ So6CGRectV
+ _symbolic _____ So6CGSizeV
+ _symbolic _____ So7CGPointV
+ _symbolic _____Sg 24SensitiveContentAnalysis12FrameDetailsV
+ _symbolic _____Sg So13audit_token_ta
+ _symbolic _____Sg So6CGRectV
+ _symbolic ______SdSgt 24SensitiveContentAnalysis011SensitivityC0V
+ _symbolic _____ySDy_____Say_____y_____GGGG 24SensitiveContentAnalysis6AtomicV So13audit_token_ta AA17ResumedConnectionV AA019VideoStreamAnalyzerH6ConfigV
+ _symbolic _____ySbSgG s9TaskLocalC
+ _symbolic _____y_____G 24SensitiveContentAnalysis6AtomicV AA19VideoStreamAnalyzerC7SamplerC5StatsV
+ _symbolic _____y_____Say_____y_____GGG s18_DictionaryStorageC So13audit_token_ta 24SensitiveContentAnalysis17ResumedConnectionV AE019VideoStreamAnalyzerI6ConfigV
+ _type_layout_string 24SensitiveContentAnalysis12FrameDetailsV
+ _type_layout_string 24SensitiveContentAnalysis19VideoStreamAnalyzerC7SamplerC5StatsV
+ _type_layout_string So6CGRectV
+ _type_layout_string So6CGSizeV
- -[SCMADVideoSession processPixelBuffer:timestamp:orientation:resultHandler:]
- GCC_except_table7
- _VTDecompressionSessionSetContentAnalyzer
- ___76-[SCMADVideoSession processPixelBuffer:timestamp:orientation:resultHandler:]_block_invoke
- ___swift_memcpy33_8
- _block_copy_helper.31
- _block_copy_helper.66
- _block_copy_helper.73
- _block_descriptor.33
- _block_descriptor.68
- _block_descriptor.75
- _block_destroy_helper.32
- _block_destroy_helper.67
- _block_destroy_helper.74
- _symbolic ShySo21NSXPCListenerEndpointCG
- _symbolic SiSg
- _symbolic _____ySSG s20CollectionDifferenceV
- _symbolic _____y_____ySSGG s16IndexingIteratorV s20CollectionDifferenceV
- _type_layout_string So28SCVideoStreamAnalysisOptionsV
CStrings:
+ "\n%{private}s"
+ "@\"NSNumber\""
+ "@\"SCSensitivityAnalysis\""
+ "B92@0:8^{__CVBuffer=}16{?=qiIq}24I48{CGRect={CGPoint=dd}{CGSize=dd}}52@?84"
+ "Finished.%{private}s"
+ "Fired change handler on \"%s\": %{private}hu, %{private}hu"
+ "MADVideoSessionFrameProperties"
+ "New region of interest above minimum (%fx%f,%sx%s) for stream \"%s\" "
+ "New region of interest below minimum (%fx%f,%sx%s) for stream \"%s\" "
+ "Non-triggering positive"
+ "SCMADVideoSessionResult"
+ "SCVideoStreamAnalyzerForcedSampleRate"
+ "SCVideoStreamAnalyzerTargetAverageSampleRate"
+ "SCVideoStreamAnalyzerVerboseSamplingLogging"
+ "SensitiveContentAnalysis.VideoStreamAnalysisDispatcher"
+ "Started tracking stream \"%s\" (%s)"
+ "Stats:BelowMinimumRes:"
+ "Stopped tracking stream \"%s\""
+ "Stream \"%s\" (%s) is buffering frames for TTR. (%ld)"
+ "Stream \"%s\" (%s) will not buffer frames for TTR"
+ "Stream \"%s\" continued."
+ "Stream \"%s\" made visible (%llu) "
+ "T@\"NSNumber\",R,V_confidenceScore"
+ "T@\"NSString\",N,R"
+ "T@\"SCSensitivityAnalysis\",R,V_analysis"
+ "Tried to connect to parent without audit token"
+ "Tried to update frame size for untracked stream \"%s\" "
+ "Using forced sample rate algorithm from defaults: .forced(%f)"
+ "Using target average sample rate algorithm from defaults: .targetAverageSampleRate(%f)"
+ "VCPDecompressionSessionSetContentAnalyzer2"
+ "_confidenceScore"
+ "_stats"
+ "analyzePixelBuffer:orientation:regionOfInterest:"
+ "auditToken"
+ "childFrameDetailsChangedWithAnalyzerUUID:newFrameSize:newRegionOfInterest:newOrientation:"
+ "conferencing_detection_power"
+ "confidenceScore"
+ "confidenceTypeN"
+ "connection"
+ "continueStream called on \"%s\""
+ "initWithAnalysis:confidenceScore:"
+ "isOutgoing"
+ "latestFrameDetails"
+ "notAnalyzableAnalysis"
+ "processPixelBuffer:frameProperties:resultHandler:"
+ "processPixelBuffer:timestamp:orientation:regionOfInterest:resultHandler:"
+ "rectValue"
+ "setOrientation:"
+ "setRegionOfInterest:"
+ "setTimestamp:"
+ "sizeValue"
+ "v44@0:8@\"NSString\"16@\"NSValue\"24@\"NSValue\"32I40"
+ "v44@0:8@16@24@32I40"
+ "v56@?0^{__CVBuffer=}8{?=qiIq}16r^{__CFDictionary=}40^{?=CC}48"
+ "v60@0:8^{__CVBuffer=}16I24{CGRect={CGPoint=dd}{CGSize=dd}}28"
+ "valueWithRect:"
+ "valueWithSize:"
+ "verboseLogging"
- "B60@0:8^{__CVBuffer=}16{?=qiIq}24I48@?52"
- "Called continueStream"
- "Finished. Initial: %{private}ld, Follow-up: %{private}ld, continues: %{private}ld"
- "Fired change handler: %{private}hu, %{private}hu"
- "Stream \"%s\" is buffering frames for TTR. (%ld)"
- "Stream \"%s\" will not buffer frames for TTR"
- "childFrameAreaChangedWithAnalyzerUUID:newFrameArea:"
- "connected"
- "initWithInteger:"
- "latestFrameArea"
- "photos and videos"

```
