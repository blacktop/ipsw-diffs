## LearnedFeatures

> `/System/Library/PrivateFrameworks/LearnedFeatures.framework/LearnedFeatures`

```diff

-8.25.12.16.5
-  __TEXT.__text: 0x223d74
-  __TEXT.__auth_stubs: 0x14d0
-  __TEXT.__gcc_except_tab: 0x144fc
-  __TEXT.__cstring: 0xc1b0
-  __TEXT.__const: 0x17aef
+9.26.5.12.5
+  __TEXT.__text: 0x2356d8
+  __TEXT.__gcc_except_tab: 0x16a14
+  __TEXT.__cstring: 0xcf88
+  __TEXT.__const: 0x193a0
   __TEXT.__oslogstring: 0x87
-  __TEXT.__unwind_info: 0x7418
+  __TEXT.__unwind_info: 0x8100
   __TEXT.__eh_frame: 0x598
-  __TEXT.__objc_classname: 0xba
-  __TEXT.__objc_methname: 0x3d
-  __TEXT.__objc_stubs: 0xa0
-  __DATA_CONST.__got: 0x2d8
-  __DATA_CONST.__const: 0x1060
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __DATA_CONST.__const: 0x1138
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__weak_got: 0x28
   __DATA_CONST.__objc_selrefs: 0x28
-  __AUTH_CONST.__auth_got: 0xa78
-  __AUTH_CONST.__const: 0xf1e0
+  __DATA_CONST.__got: 0x310
+  __AUTH_CONST.__const: 0x10598
   __AUTH_CONST.__cfstring: 0x260
-  __AUTH_CONST.__objc_const: 0x2d0
-  __AUTH.__objc_data: 0xa0
-  __AUTH.__data: 0x8
-  __DATA.__data: 0x840
+  __AUTH_CONST.__objc_const: 0x630
+  __AUTH_CONST.__weak_auth_got: 0x40
+  __AUTH_CONST.__auth_got: 0xa68
+  __AUTH.__objc_data: 0x370
+  __AUTH.__data: 0x10
+  __AUTH.__thread_vars: 0x30
+  __AUTH.__thread_bss: 0x10
+  __DATA.__data: 0x880
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x890
+  __DATA.__bss: 0x8e8
   __DATA.__common: 0xb0
-  __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 46A20B3D-7964-3755-956F-F539CFB25CF7
-  Functions: 5221
-  Symbols:   540
-  CStrings:  993
+  UUID: D9D2DD34-FE68-3A9A-9B6F-1EB24365D209
+  Functions: 5606
+  Symbols:   572
+  CStrings:  1063
 
Symbols:
+ _CFDictionaryCreateMutableCopy
+ _LFV2MatchDescriptorsWithStateDatabase
+ _LFV2MatcherSupportsStateDatabaseMatching
+ _OBJC_CLASS_$_LearnedFeatures_ATUHardNetGlobalFeatModel_ResourceAnchor
+ _OBJC_CLASS_$_LearnedFeatures_AspCtxDescModel_ResourceAnchor
+ _OBJC_CLASS_$_LearnedFeatures_AspDescModel_ResourceAnchor
+ _OBJC_CLASS_$_LearnedFeatures_DenseFeat2Model_ResourceAnchor
+ _OBJC_CLASS_$_LearnedFeatures_DenseFeatNetModel_ResourceAnchor
+ _OBJC_CLASS_$_LearnedFeatures_DepthDenseFeat2Model_ResourceAnchor
+ _OBJC_CLASS_$_LearnedFeatures_GlobalFeatModel_ResourceAnchor
+ _OBJC_CLASS_$_LearnedFeatures_HammingMutualMatcherModel_ResourceAnchor
+ _OBJC_CLASS_$_LearnedFeatures_HardnetModel_ResourceAnchor
+ _OBJC_CLASS_$_LearnedFeatures_ImageRetrievalTop15L2Model_ResourceAnchor
+ _OBJC_CLASS_$_LearnedFeatures_KpNetModel_ResourceAnchor
+ _OBJC_METACLASS_$_LearnedFeatures_ATUHardNetGlobalFeatModel_ResourceAnchor
+ _OBJC_METACLASS_$_LearnedFeatures_AspCtxDescModel_ResourceAnchor
+ _OBJC_METACLASS_$_LearnedFeatures_AspDescModel_ResourceAnchor
+ _OBJC_METACLASS_$_LearnedFeatures_DenseFeat2Model_ResourceAnchor
+ _OBJC_METACLASS_$_LearnedFeatures_DenseFeatNetModel_ResourceAnchor
+ _OBJC_METACLASS_$_LearnedFeatures_DepthDenseFeat2Model_ResourceAnchor
+ _OBJC_METACLASS_$_LearnedFeatures_GlobalFeatModel_ResourceAnchor
+ _OBJC_METACLASS_$_LearnedFeatures_HammingMutualMatcherModel_ResourceAnchor
+ _OBJC_METACLASS_$_LearnedFeatures_HardnetModel_ResourceAnchor
+ _OBJC_METACLASS_$_LearnedFeatures_ImageRetrievalTop15L2Model_ResourceAnchor
+ _OBJC_METACLASS_$_LearnedFeatures_KpNetModel_ResourceAnchor
+ __tlv_bootstrap
+ _e5rt_e5_compiler_options_set_experimental_match_e5_minimal_cpu_patterns_for_states
+ _e5rt_execution_stream_operation_get_inout_names
+ _e5rt_execution_stream_operation_get_num_inouts
+ _e5rt_execution_stream_operation_retain_inout_port
+ _kCFErrorLocalizedFailureReasonKey
+ _kCFErrorUnderlyingErrorKey
+ _objc_claimAutoreleasedReturnValue
+ _snprintf
- _kCFErrorLocalizedDescriptionKey
- _objc_retainAutoreleasedReturnValue
CStrings:
+ " (inouts). Model input ports: ["
+ " : %.*s"
+ " allocating buffer for inout: "
+ " binding inout buffer: "
+ " does not match expected size "
+ " does not match image size "
+ " does not match keypoint count "
+ " getting tensor size for inout: "
+ " model inouts but received "
+ " must be at least (2, 2)"
+ " not supported by ATU descriptor model"
+ " not supported by DenseFeat2: "
+ " not supported by GlobalFeat: "
+ " not supported by either model. DenseFeat2: "
+ " not supported, expected (320, 256)"
+ " not supported, expected (320, 320)"
+ " not supported. "
+ " retaining inout port: "
+ " retaining tensor desc for inout: "
+ "%s: %s:%d"
+ "((std::is_same_v<UT, uint8_t> && data_type == BufferDataType::Uint8) || (std::is_same_v<UT, uint16_t> && data_type == BufferDataType::Uint16) || (std::is_same_v<UT, half> && data_type == BufferDataType::Float16) || (std::is_same_v<UT, float> && data_type == BufferDataType::Float32))"
+ "(params.inputs.size() + params.inouts.size()) >= 1"
+ ",\n"
+ ", GlobalFeat: "
+ ", which does not exists. Available resolutions are: "
+ ". Model inouts ports: ["
+ ". Model output ports: ["
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCV3D_LearnedFeatures/library/Kit/IOSurface/src/IOSurfaceRef_maybe_mno_unaligned_access.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Private/EspressoV2ModelInstance_maybe_mno_unaligned_access.mm"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCV3D_LearnedFeatures/library/Kit/Memory/include_private/Kit/Memory/ProtectedMemoryPrivate.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/EndToEndExtraction/src/GlobalAndDenseFeat2.cpp"
+ "<unknown>"
+ "ATUHardNetGlobalFeatModel does not support keypoint detection"
+ "Cannot nest CallProtected with different memory access implementations"
+ "CopyViewsProtected: protected copy failed"
+ "CreateChildSurface not supported for EXSurface on ExclaveKit"
+ "Database must have {8192, 1152} shape, got {"
+ "DetectKeypoints is not implemented for GlobalAndDenseFeat2Model"
+ "ExtractDescriptors is not implemented for GlobalAndDenseFeat2Model"
+ "ExtractLocalGlobalDescriptors is not implemented for GlobalAndDenseFeat2Model"
+ "Failed to capture stack pointer"
+ "Failed to convert bundle URL to string"
+ "Failed to create GlobalFeatModel"
+ "Failed to create HammingSecondNNMutualStateModel: "
+ "Failed to create HammingSecondNNMutualStateModel: Unknown error occurred"
+ "GlobalFeatModel does not support descriptor extraction"
+ "GlobalFeatModel does not support keypoint detection"
+ "HasAppleNeuralEngine"
+ "Image size "
+ "Invalid inout: The given view for inout "
+ "Invalid input image resolution: "
+ "LFReturn LFV2MatchDescriptorsWithStateDatabase(LFV2MutableMatcherHandleRef, CVPixelBufferRef, CVPixelBufferRef, CVPixelBufferRef, CVPixelBufferRef, LFV2MatchesRef *)"
+ "Models/LoFeatMatchState/"
+ "No model loaded for HammingSecondNNMutualStateModel"
+ "Only Gray8u, Gray16u, Gray16f, and Gray32f input tensors supported"
+ "State database matching is not supported by this matcher"
+ "State database matching not supported"
+ "The DataView does not contain uint16 data"
+ "Trying to access configuration: "
+ "Unable to create state matcher model: "
+ "Unable to retain inout port: "
+ "ValidViewStructure<uint8_t>(Structure(inout))"
+ "]"
+ "buffer is null"
+ "cv3d.cf"
+ "cv3d.featureextraction"
+ "cv3d.function"
+ "desciptors_database_state"
+ "descriptor count "
+ "descriptor size mismatch"
+ "descriptors1_index"
+ "descriptors2_index"
+ "end-to-end extractor requires no separate keypoint detector or descriptor extractor"
+ "format.Contains(FormatFlags::UINT16)"
+ "idx < p_->GetCachedBaseAddresses().size()"
+ "image size "
+ "incompatible pixel format: "
+ "inout.Format().IsValidFormat()"
+ "inout__"
+ "input_shapes: \n{"
+ "invalid descriptor extractor"
+ "invalid keypoint detector"
+ "io"
+ "mask size "
+ "multiple error causes"
+ "no end-to-end extractor"
+ "no valid descriptor extractor"
+ "no valid end-to-end extractor"
+ "no valid keypoint detector"
+ "outputs: \n{"
+ "pixel buffer is null"
+ "result"
+ "sp != nullptr"
+ "unknown feature extraction error"
+ "unsupported pixel format: "
- " : "
- "' path: "
- "'). "
- "'. "
- "': "
- "((std::is_same_v<UT, uint8_t> && data_type == BufferDataType::Uint8) || (std::is_same_v<UT, half> && data_type == BufferDataType::Float16) || (std::is_same_v<UT, float> && data_type == BufferDataType::Float32))"
- "+N9mZUAHooNvMiQnjeTJ8g"
- ", image "
- ", model="
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCV3D_LearnedFeatures/library/Kit/IOSurface/src/IOSurfaceRef.cpp"
- "Densefeat2ModelBundleIdentifier"
- "DepthDensefeat2ModelBundleIdentifier"
- "Failed to access bundle bundle resource '"
- "Failed to access model resource path"
- "GlobalFeatModelBundleIdentifier"
- "HammingMutualMatcherModelBundleIdentifier"
- "ImageRetrievalTop15L2ModelBundleIdentifier"
- "Only Gray8u and Gray32f input tensors supported"
- "UTF8String"
- "aneSubType"
- "bundleForClass:"
- "bundlePath"
- "description"
- "idx < p_->GetCachedBaseAddress().size()"
- "x"

```
