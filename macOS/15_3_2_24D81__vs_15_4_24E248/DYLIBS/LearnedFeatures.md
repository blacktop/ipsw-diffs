## LearnedFeatures

> `/System/Library/PrivateFrameworks/LearnedFeatures.framework/Versions/A/LearnedFeatures`

```diff

-7.14.2.0.0
-  __TEXT.__text: 0xedb9c
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__gcc_except_tab: 0xbd80
-  __TEXT.__cstring: 0x80b9
-  __TEXT.__const: 0xd9d3
+7.63.0.0.0
+  __TEXT.__text: 0x10be4c
+  __TEXT.__auth_stubs: 0xfe0
+  __TEXT.__const: 0xe8f3
+  __TEXT.__gcc_except_tab: 0xd1ec
+  __TEXT.__cstring: 0x9165
   __TEXT.__oslogstring: 0x34
-  __TEXT.__unwind_info: 0x4ab8
+  __TEXT.__unwind_info: 0x5170
   __TEXT.__objc_methname: 0x4f
   __TEXT.__objc_stubs: 0xa0
-  __DATA_CONST.__got: 0x1b0
+  __DATA_CONST.__got: 0x228
   __DATA_CONST.__const: 0xa50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x678
-  __AUTH_CONST.__const: 0x8cf8
-  __AUTH_CONST.__cfstring: 0x1e0
+  __AUTH_CONST.__auth_got: 0x800
+  __AUTH_CONST.__const: 0x9538
+  __AUTH_CONST.__cfstring: 0x200
   __AUTH.__data: 0x30
-  __DATA.__data: 0x25c0
+  __DATA.__data: 0x2600
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0xd20
+  __DATA.__bss: 0xce8
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vImage.framework/Versions/A/vImage
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreVideo.framework/Versions/A/CoreVideo

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B824CFD9-203B-31F9-B359-F75A7BBA59C6
-  Functions: 2933
-  Symbols:   316
-  CStrings:  622
+  UUID: 134BDC4D-5ED9-3D9E-A2F2-035B090DCD68
+  Functions: 3192
+  Symbols:   376
+  CStrings:  708
 
Symbols:
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEPKv
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ _e5rt_buffer_object_alloc
+ _e5rt_buffer_object_get_data_ptr
+ _e5rt_buffer_object_release
+ _e5rt_e5_compiler_compile
+ _e5rt_e5_compiler_config_options_create
+ _e5rt_e5_compiler_config_options_release
+ _e5rt_e5_compiler_config_options_set_cache_bundle_location
+ _e5rt_e5_compiler_create
+ _e5rt_e5_compiler_create_with_config
+ _e5rt_e5_compiler_is_new_compile_required
+ _e5rt_e5_compiler_options_create
+ _e5rt_e5_compiler_options_release
+ _e5rt_e5_compiler_release
+ _e5rt_error_code_get_string
+ _e5rt_execution_stream_create
+ _e5rt_execution_stream_encode_operation
+ _e5rt_execution_stream_execute_sync
+ _e5rt_execution_stream_operation_create_precompiled_compute_operation_with_options
+ _e5rt_execution_stream_operation_get_input_names
+ _e5rt_execution_stream_operation_get_num_inputs
+ _e5rt_execution_stream_operation_get_num_outputs
+ _e5rt_execution_stream_operation_get_output_names
+ _e5rt_execution_stream_operation_prepare_op_for_encode
+ _e5rt_execution_stream_operation_release
+ _e5rt_execution_stream_operation_retain_input_port
+ _e5rt_execution_stream_operation_retain_output_port
+ _e5rt_execution_stream_prewire_in_use_allocations
+ _e5rt_execution_stream_release
+ _e5rt_execution_stream_reset
+ _e5rt_get_last_error_message
+ _e5rt_io_port_bind_buffer_object
+ _e5rt_io_port_bind_surface_object
+ _e5rt_io_port_release
+ _e5rt_io_port_retain_tensor_desc
+ _e5rt_precompiled_compute_op_create_options_create_with_program_function
+ _e5rt_precompiled_compute_op_create_options_release
+ _e5rt_precompiled_compute_op_create_options_set_allocate_intermediate_buffers
+ _e5rt_program_function_release
+ _e5rt_program_library_create
+ _e5rt_program_library_get_function_metadata
+ _e5rt_program_library_get_function_names
+ _e5rt_program_library_get_num_functions
+ _e5rt_program_library_release
+ _e5rt_program_library_retain_program_function
+ _e5rt_surface_object_create_from_iosurface
+ _e5rt_surface_object_release
+ _e5rt_tensor_desc_create
+ _e5rt_tensor_desc_dtype_create
+ _e5rt_tensor_desc_dtype_get_component_dtype
+ _e5rt_tensor_desc_dtype_get_component_size
+ _e5rt_tensor_desc_dtype_get_element_size
+ _e5rt_tensor_desc_dtype_get_num_components
+ _e5rt_tensor_desc_dtype_release
+ _e5rt_tensor_desc_get_shape
+ _e5rt_tensor_desc_get_size
+ _e5rt_tensor_desc_get_strides
+ _e5rt_tensor_desc_release
+ _e5rt_tensor_desc_retain_dtype
+ _e5rt_tensor_utils_cast_from_fp16_to_fp32
+ _e5rt_tensor_utils_dequantize_from_u8_to_fp32
- _CFArrayGetCount
- _CFArrayGetValueAtIndex
- _CFDictionaryGetCount
- _CFDictionaryGetKeysAndValues
CStrings:
+ " Unable to find the specified function name: "
+ " Unable to load this espresso function for execution: "
+ " cache location : "
+ " for function"
+ " of size "
+ "!img::HasIOSurface(*buffer.image)"
+ "((std::is_same_v<UT, uint8_t> && data_type == BufferDataType::Uint8) || (std::is_same_v<UT, half> && data_type == BufferDataType::Float16) || (std::is_same_v<UT, float> && data_type == BufferDataType::Float32))"
+ ". Available ports are: "
+ ". Error: "
+ ". Last error message: "
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Essentials/Apple/src/BundlePath.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Essentials/Array/include/Essentials/Array/ArrayView.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Essentials/Array/src/ArrayBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Essentials/Common/include/Essentials/Common/Span.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Essentials/Resource/src/Resource.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/CoreVideo/include/Kit/CoreVideo/PixelBufferRef.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/CoreVideo/src/CVImage.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/CoreVideo/src/CVImage.cpp:55"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/CoreVideo/src/PixelBufferRef.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Foundation/src/BundleRef.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Foundation/src/Ref.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Foundation/src/URLRef.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/IOSurface/src/IOSurfaceRef.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/include/Kit/Image/FormatAlgorithm.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/include/Kit/Image/Image.h:1190"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/include/Kit/Image/ImageBuffer.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/include/Kit/Image/ImageView.h:1297"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/src/ImageStorage.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/src/Size.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ImageProcessing/src/NonMaximumSuppression.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/include/Kit/ML/DataView.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/DataView.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Execution.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Model.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Private/EspressoModelInstance.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Private/EspressoUtil.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Private/EspressoV2ModelInstance.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Private/EspressoV2StreamPool.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/PixelFormat/include/Kit/PixelFormat/Properties.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/Common/src/FeaturesData.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/include_private/LearnedFeatures/DescriptorExtraction/DescriptorExtractionUtil.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/src/DescriptorExtractionCommonUtil.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/src/DescriptorExtractionUtil.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/src/DescriptorModelDefinition.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/src/IDescriptorModel.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/EndToEndExtraction/include_private/LearnedFeatures/EndToEndExtraction/EndToEndModel.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/EndToEndExtraction/src/EndToEndModel.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/EndToEndExtraction/src/EndToEndModelDefinition.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/EndToEndExtraction/src/EndToEndUtils.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/FeatureExtraction/src/FeatureExtractor.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/KeypointDetection/include_private/LearnedFeatures/KeypointDetection/KeypointModel.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/KeypointDetection/src/KeypointDetector.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/KeypointDetection/src/KeypointModel.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/LearnedFeatures/include_private/LearnedFeatures/private/LearnedFeaturesConversion.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/LearnedFeatures/src/LearnedFeaturesInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/PatchCropping/include/LearnedFeatures/PatchCropping/ImagePatches.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/PatchCropping/src/PatchCropper.cpp"
+ "Buffer is not IOSurface backed."
+ "Buffer type mismatch"
+ "Compiler must be created before this"
+ "Conversions not supported yet"
+ "Copy from float to uint8 buffer is not allowed"
+ "Copy not supported yet."
+ "Datatype not supported"
+ "Error during creation of program library model with bundle expected at '"
+ "Error during creation of program library model with non-bundle format at'"
+ "EspressoStreamPool: Failed to create e5rt stream operation with options.  Return code: "
+ "EspressoStreamPool: Failed to create e5rt stream.  Return code: "
+ "Execution stream encode workload failed.  Return code: "
+ "Execution stream execute failed.  Return code: "
+ "Execution stream reset failed.  Return code: "
+ "Expect alteast one function for a model but got 0"
+ "Generic tensor(s) in `RunData` out of order, must be consistent for each configuration."
+ "GetAllocatedBufferForGenericTensor: Allocated buffer has null buffer_obj"
+ "Hardware not supported"
+ "Input size provided is different from config."
+ "Input/output port counts doesn't match."
+ "Invalid e5rt objects from pool."
+ "IsNonBundleSupported()"
+ "Number of components not supported yet"
+ "Only Gray8u and Gray32f input tensors supported"
+ "Only Grayscale or two component image direct binding supported now."
+ "Only single Grayscale input image or single two component input image is supported."
+ "Ops"
+ "Prewire pool limit size reached."
+ "The model is already running in this configuration."
+ "Unable create execution stream operation with precompiled compute operation with options: "
+ "Unable to bind generic input buffer to input port "
+ "Unable to bind input and output ports"
+ "Unable to bind output buffer to output port "
+ "Unable to bind output buffers for pre-wire in this configuration: "
+ "Unable to bind output buffers in this configuration: "
+ "Unable to bind surface object to input port.Please set \"experimental.aot.enable_surface_desc\" : \"1\"  in model.espresso.net properties"
+ "Unable to check if new compile required: "
+ "Unable to convert Float16 to Float32 output buffer."
+ "Unable to convert Uint8 to Float32 output buffer."
+ "Unable to create buffer for input port: "
+ "Unable to create buffer for output port: "
+ "Unable to create compiler config: "
+ "Unable to create compiler options: "
+ "Unable to create compiler with config: "
+ "Unable to create execution stream : "
+ "Unable to create precompiled compute op options with program function: "
+ "Unable to create program library: "
+ "Unable to create surface object from IOSurface"
+ "Unable to load program function: "
+ "Unable to retain input port."
+ "Unable to retain input port: "
+ "Unable to retain output port: "
+ "Unable to retain program library function : "
+ "Unable to set allocate intermediate buffers options for precompiled_compute_op: "
+ "Unable to set config options to cache bundle location : "
+ "Unable to set configuration to: "
+ "buffer.data_type != BufferDataType::Uint8"
+ "buffer.image"
+ "buffer_itr != input_buffer_map.end()"
+ "buffer_itr->second.buffer_obj"
+ "compiler"
+ "detail::IsValidShape(input_rank, input_shape, input_tensor_size, output_tensor_size)"
+ "espresso_library"
+ "espresso_stream_op != nullptr"
+ "in the list of available functions "
+ "m_configuration != nullptr"
+ "mem_ret == E5RT_ERROR_CODE_OK"
+ "num_inputs == data.inputs.size()"
+ "output.second"
+ "ret == E5RT_ERROR_CODE_OK"
+ "ret_tensor == E5RT_ERROR_CODE_OK"
+ "stream != nullptr && stream_op != nullptr"
+ "streams_and_ops_.size() == available_streams_.size()"
+ "string_view::substr"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Essentials/Apple/src/BundlePath.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Essentials/Array/include/Essentials/Array/ArrayView.h"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Essentials/Array/src/ArrayBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Essentials/Common/include/Essentials/Common/Span.h"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Essentials/Resource/src/Resource.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/CoreVideo/include/Kit/CoreVideo/PixelBufferRef.h"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/CoreVideo/src/CVImage.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/CoreVideo/src/CVImage.cpp:51"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/CoreVideo/src/PixelBufferRef.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Foundation/src/BundleRef.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Foundation/src/Ref.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Foundation/src/URLRef.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/include/Kit/Image/FormatAlgorithm.h"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/include/Kit/Image/Image.h:1190"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/include/Kit/Image/ImageBuffer.h"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/include/Kit/Image/ImageView.h:1297"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/src/ImageStorage.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/Image/src/Size.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ImageProcessing/src/NonMaximumSuppression.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/include/Kit/ML/DataView.h"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/DataView.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Execution.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Model.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Private/EspressoModelInstance.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/ML/src/Private/EspressoUtil.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/Kit/PixelFormat/include/Kit/PixelFormat/Properties.h"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/Common/src/FeaturesData.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/include_private/LearnedFeatures/DescriptorExtraction/DescriptorExtractionUtil.h"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/src/DescriptorExtractionCommonUtil.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/src/DescriptorExtractionUtil.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/src/DescriptorModelDefinition.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/DescriptorExtraction/src/IDescriptorModel.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/EndToEndExtraction/include_private/LearnedFeatures/EndToEndExtraction/EndToEndModel.h"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/EndToEndExtraction/src/EndToEndModel.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/EndToEndExtraction/src/EndToEndModelDefinition.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/EndToEndExtraction/src/EndToEndUtils.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/FeatureExtraction/src/FeatureExtractor.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/KeypointDetection/include_private/LearnedFeatures/KeypointDetection/KeypointModel.h"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/KeypointDetection/src/KeypointDetector.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/KeypointDetection/src/KeypointModel.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/LearnedFeatures/include_private/LearnedFeatures/private/LearnedFeaturesConversion.h"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/LearnedFeatures/src/LearnedFeaturesInterface.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/PatchCropping/include/LearnedFeatures/PatchCropping/ImagePatches.h"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/PatchCropping/src/PatchCropper.cpp"
- "Espresso models can only be instantiated on Apple platforms"
- "com.apple.cv3d"

```
