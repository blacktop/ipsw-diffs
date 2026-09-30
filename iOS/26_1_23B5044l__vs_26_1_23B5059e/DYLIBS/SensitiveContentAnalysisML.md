## SensitiveContentAnalysisML

> `/System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML`

```diff

-125.1.4.0.0
-  __TEXT.__text: 0xac674
-  __TEXT.__auth_stubs: 0x2b00
-  __TEXT.__objc_methlist: 0x19f4
-  __TEXT.__const: 0x917c
-  __TEXT.__gcc_except_tab: 0x5440
-  __TEXT.__cstring: 0x3e36
-  __TEXT.__oslogstring: 0x16c3
-  __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__swift5_typeref: 0x191f
-  __TEXT.__swift5_fieldmd: 0x14f4
-  __TEXT.__constg_swiftt: 0x1a04
-  __TEXT.__swift5_reflstr: 0xc3d
+125.1.6.0.0
+  __TEXT.__text: 0xb00e0
+  __TEXT.__auth_stubs: 0x2b50
+  __TEXT.__objc_methlist: 0x1a64
+  __TEXT.__const: 0x979c
+  __TEXT.__gcc_except_tab: 0x55f8
+  __TEXT.__cstring: 0x3ef6
+  __TEXT.__oslogstring: 0x1703
+  __TEXT.__dlopen_cstrs: 0x108
+  __TEXT.__swift5_typeref: 0x19f1
+  __TEXT.__swift5_fieldmd: 0x15c0
+  __TEXT.__constg_swiftt: 0x1abc
+  __TEXT.__swift5_reflstr: 0xc5d
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_assocty: 0x2b8
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__swift5_proto: 0x6b8
-  __TEXT.__swift5_types: 0x210
-  __TEXT.__swift_as_entry: 0xe8
-  __TEXT.__swift_as_ret: 0x168
+  __TEXT.__swift5_proto: 0x720
+  __TEXT.__swift5_types: 0x228
+  __TEXT.__swift_as_entry: 0xec
+  __TEXT.__swift_as_ret: 0x170
   __TEXT.__swift5_mpenum: 0x28
   __TEXT.__swift5_capture: 0x14c
-  __TEXT.__unwind_info: 0x3cc0
-  __TEXT.__eh_frame: 0x5030
-  __TEXT.__objc_classname: 0x352
-  __TEXT.__objc_methname: 0x3a42
-  __TEXT.__objc_methtype: 0x1ff4
-  __TEXT.__objc_stubs: 0x2e20
-  __DATA_CONST.__got: 0x7b8
-  __DATA_CONST.__const: 0x6d8
-  __DATA_CONST.__objc_classlist: 0x200
+  __TEXT.__unwind_info: 0x3e38
+  __TEXT.__eh_frame: 0x5308
+  __TEXT.__objc_classname: 0x365
+  __TEXT.__objc_methname: 0x3b5c
+  __TEXT.__objc_methtype: 0x2021
+  __TEXT.__objc_stubs: 0x2ec0
+  __DATA_CONST.__got: 0x7c0
+  __DATA_CONST.__const: 0x6f8
+  __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe88
-  __DATA_CONST.__objc_superrefs: 0x108
+  __DATA_CONST.__objc_selrefs: 0xec0
+  __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x1f8
-  __AUTH_CONST.__auth_got: 0x1598
-  __AUTH_CONST.__const: 0x5f18
+  __AUTH_CONST.__auth_got: 0x15c0
+  __AUTH_CONST.__const: 0x62f0
   __AUTH_CONST.__cfstring: 0x17a0
-  __AUTH_CONST.__objc_const: 0x4a70
+  __AUTH_CONST.__objc_const: 0x4b88
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH.__objc_data: 0x558
-  __AUTH.__data: 0x5f8
-  __DATA.__objc_ivar: 0x2c0
-  __DATA.__data: 0x1520
-  __DATA.__bss: 0xd2e0
-  __DATA.__common: 0x80
+  __AUTH.__objc_data: 0x5a8
+  __AUTH.__data: 0x5d0
+  __DATA.__objc_ivar: 0x2cc
+  __DATA.__data: 0x1590
+  __DATA.__bss: 0xde70
+  __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x1268
-  __DATA_DIRTY.__data: 0xe78
-  __DATA_DIRTY.__bss: 0x200
-  __DATA_DIRTY.__common: 0x68
+  __DATA_DIRTY.__data: 0xf08
+  __DATA_DIRTY.__bss: 0x3a0
+  __DATA_DIRTY.__common: 0x80
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E1DF9E11-2FD2-30A7-B0AB-089F9C327874
-  Functions: 4206
-  Symbols:   6010
-  CStrings:  1858
+  UUID: E72A4EDD-47A0-31F7-B793-AD7925DC573B
+  Functions: 4320
+  Symbols:   6119
+  CStrings:  1878
 
Symbols:
+ +[SCMLMADImageEncoder newRequestWithType:withVersion:error:]
+ +[SCMLMADTextEncoder getServiceWithError:]
+ +[SCMLMADTextEncoder newRequestWithError:withVersion:]
+ -[SCMLMADEmbeddingResult bias]
+ -[SCMLMADEmbeddingResult float32DataWithError:]
+ -[SCMLMADEmbeddingResult initWithType:data:shape:bias:scale:]
+ -[SCMLMADEmbeddingResult scale]
+ -[SCMLMADImageEncoder embedPixelBufferAsynchronously:requestType:version:completionHandler:]
+ -[SCMLMADTextEncoder .cxx_destruct]
+ -[SCMLMADTextEncoder embedTextAsynchronously:version:completionHandler:]
+ -[SCMLMADTextEncoder initWithError:]
+ _OBJC_CLASS_$_SCMLMADTextEncoder
+ _OBJC_IVAR_$_SCMLMADEmbeddingResult._bias
+ _OBJC_IVAR_$_SCMLMADEmbeddingResult._scale
+ _OBJC_IVAR_$_SCMLMADTextEncoder._service
+ _OBJC_METACLASS_$_SCMLMADTextEncoder
+ __OBJC_$_CLASS_METHODS_SCMLMADTextEncoder
+ __OBJC_$_INSTANCE_METHODS_SCMLMADTextEncoder
+ __OBJC_$_INSTANCE_VARIABLES_SCMLMADTextEncoder
+ __OBJC_CLASS_RO_$_SCMLMADTextEncoder
+ __OBJC_METACLASS_RO_$_SCMLMADTextEncoder
+ __ZL31getMADTextEmbeddingRequestClassv
+ __ZZL31getMADTextEmbeddingRequestClassvE9softClass.0
+ ___72-[SCMLMADTextEncoder embedTextAsynchronously:version:completionHandler:]_block_invoke
+ ___92-[SCMLMADImageEncoder embedPixelBufferAsynchronously:requestType:version:completionHandler:]_block_invoke
+ ____ZL31getMADTextEmbeddingRequestClassv_block_invoke
+ ____ZL31getMADTextEmbeddingRequestClassv_block_invoke.cold.1
+ ___swift_memcpy4_4
+ ___swift_project_boxed_opaque_existential_1Tm
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftMLCompute_$_SensitiveContentAnalysisML
+ _associated conformance 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV24EmbeddingSizesDoNotMatchV10CodingKeys33_91EDF48C1E7CBDF8BB3E19B9A00B1077LLOSHAASQ
+ _associated conformance 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV24EmbeddingSizesDoNotMatchV10CodingKeys33_91EDF48C1E7CBDF8BB3E19B9A00B1077LLOs0N3KeyAAs23CustomStringConvertible
+ _associated conformance 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV24EmbeddingSizesDoNotMatchV10CodingKeys33_91EDF48C1E7CBDF8BB3E19B9A00B1077LLOs0N3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV24EmbeddingSizesDoNotMatchV10Foundation13CustomNSErrorAAs5Error
+ _associated conformance 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV24EmbeddingSizesDoNotMatchV10Foundation14LocalizedErrorAAs0P0
+ _associated conformance 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV25InvalidEmbeddingSizeErrorV10CodingKeys33_91EDF48C1E7CBDF8BB3E19B9A00B1077LLOSHAASQ
+ _associated conformance 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV25InvalidEmbeddingSizeErrorV10CodingKeys33_91EDF48C1E7CBDF8BB3E19B9A00B1077LLOs0M3KeyAAs23CustomStringConvertible
+ _associated conformance 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV25InvalidEmbeddingSizeErrorV10CodingKeys33_91EDF48C1E7CBDF8BB3E19B9A00B1077LLOs0M3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV25InvalidEmbeddingSizeErrorV10Foundation09LocalizedL0AAs0L0
+ _associated conformance 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV25InvalidEmbeddingSizeErrorV10Foundation13CustomNSErrorAAs0L0
+ _block_copy_helper.1
+ _block_descriptor.3
+ _block_destroy_helper.2
+ _expf
+ _objc_msgSend$bias
+ _objc_msgSend$initWithType:data:shape:bias:scale:
+ _objc_msgSend$newRequestWithError:withVersion:
+ _objc_msgSend$newRequestWithType:withVersion:error:
+ _objc_msgSend$performRequests:text:identifier:completionHandler:
+ _objc_msgSend$scale
+ _objc_msgSend$setComputeThreshold:
+ _objc_retain_x5
+ _objectdestroy.33Tm
+ _symbolic Sf
+ _symbolic So18SCMLMADTextEncoderC
+ _symbolic _____ 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV
+ _symbolic _____ 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV24EmbeddingSizesDoNotMatchV
+ _symbolic _____ 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV24EmbeddingSizesDoNotMatchV10CodingKeys33_91EDF48C1E7CBDF8BB3E19B9A00B1077LLO
+ _symbolic _____ 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV25InvalidEmbeddingSizeErrorV
+ _symbolic _____ 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV25InvalidEmbeddingSizeErrorV10CodingKeys33_91EDF48C1E7CBDF8BB3E19B9A00B1077LLO
+ _symbolic _____ 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV6ResultV
+ _symbolic _____ySfG s23_ContiguousArrayStorageC
+ _symbolic _____y_____G s22KeyedDecodingContainerV 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV24EmbeddingSizesDoNotMatchV10CodingKeys33_91EDF48C1E7CBDF8BB3E19B9A00B1077LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV25InvalidEmbeddingSizeErrorV10CodingKeys33_91EDF48C1E7CBDF8BB3E19B9A00B1077LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV24EmbeddingSizesDoNotMatchV10CodingKeys33_91EDF48C1E7CBDF8BB3E19B9A00B1077LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV25InvalidEmbeddingSizeErrorV10CodingKeys33_91EDF48C1E7CBDF8BB3E19B9A00B1077LLO
+ _toMADUnifiedEmbeddingVersion
+ _toSCMLMADEmbeddingType
+ _type_layout_string 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV
+ _type_layout_string 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV24EmbeddingSizesDoNotMatchV
+ _type_layout_string 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV25InvalidEmbeddingSizeErrorV
+ _type_layout_string 26SensitiveContentAnalysisML28TextImageAlignmentCalculatorV6ResultV
- +[SCMLMADImageEncoder newRequestWithType:error:]
- -[SCMLMADEmbeddingResult initWithType:data:shape:]
- -[SCMLMADImageEncoder embedPixelBufferAsynchronously:requestType:completionHandler:]
- ___84-[SCMLMADImageEncoder embedPixelBufferAsynchronously:requestType:completionHandler:]_block_invoke
- _objc_msgSend$initWithType:data:shape:
- _objc_msgSend$newRequestWithType:error:
- _objectdestroy.32Tm
CStrings:
+ "@32@0:8^@16Q24"
+ "@40@0:8Q16Q24^@32"
+ "@56@0:8Q16@24@32@40@48"
+ "Failed to compute unified image embedding"
+ "MADTextEmbeddingRequest"
+ "SCMLMADTextEncoder"
+ "T@\"NSNumber\",R,N,V_bias"
+ "T@\"NSNumber\",R,N,V_scale"
+ "Unified image embedding type=%d count=%d shape=[%@]"
+ "Unified text embedding type=%d count=%d shape=[%@]"
+ "_bias"
+ "_scale"
+ "bias"
+ "embedPixelBufferAsynchronously:requestType:version:completionHandler:"
+ "embedTextAsynchronously:version:completionHandler:"
+ "failed to alloc MADTextEmbeddingRequest"
+ "failed to get MADTextEmbeddingRequest class"
+ "failed to init MADTextEmbeddingRequest"
+ "float32DataWithError:"
+ "initWithType:data:shape:bias:scale:"
+ "newRequestWithError:withVersion:"
+ "newRequestWithType:withVersion:error:"
+ "performRequests:text:identifier:completionHandler:"
+ "scale"
+ "setComputeThreshold:"
+ "v40@0:8@16Q24@?32"
+ "v48@0:8^{__CVBuffer=}16Q24Q32@?40"
- "@32@0:8Q16^@24"
- "@40@0:8Q16@24@32"
- "Bridge embedding type=%d count=%d shape=[%@]"
- "embedPixelBufferAsynchronously:requestType:completionHandler:"
- "initWithType:data:shape:"
- "newRequestWithType:error:"
- "v40@0:8^{__CVBuffer=}16Q24@?32"

```
