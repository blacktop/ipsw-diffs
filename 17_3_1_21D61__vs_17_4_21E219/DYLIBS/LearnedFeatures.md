## LearnedFeatures

> `/System/Library/PrivateFrameworks/LearnedFeatures.framework/LearnedFeatures`

```diff

-6.31.53.0.0
-  __TEXT.__text: 0x14a5bc
-  __TEXT.__auth_stubs: 0x1190
-  __TEXT.__const: 0x1447b
-  __TEXT.__gcc_except_tab: 0xf488
-  __TEXT.__cstring: 0x95d5
-  __TEXT.__oslogstring: 0x2e
-  __TEXT.__unwind_info: 0x634c
+6.58.55.0.0
+  __TEXT.__text: 0x15ac38
+  __TEXT.__auth_stubs: 0x10a0
+  __TEXT.__const: 0x13ec6
+  __TEXT.__gcc_except_tab: 0x10a78
+  __TEXT.__cstring: 0x938f
+  __TEXT.__oslogstring: 0x34
+  __TEXT.__unwind_info: 0x611c
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_methname: 0x52
   __TEXT.__objc_stubs: 0xa0
-  __DATA_CONST.__got: 0x258
-  __DATA_CONST.__const: 0xa88
+  __DATA_CONST.__got: 0x238
+  __DATA_CONST.__const: 0xa50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x28
-  __AUTH_CONST.__const: 0xc5c0
+  __DATA_CONST.__objc_classrefs: 0x18
+  __AUTH_CONST.__const: 0xc1d0
   __AUTH_CONST.__cfstring: 0x200
-  __AUTH_CONST.__auth_got: 0x8d8
-  __AUTH.__data: 0x18
+  __AUTH_CONST.__auth_got: 0x860
+  __AUTH.__data: 0x38
   __DATA.__got_weak: 0x8
-  __DATA.__objc_classrefs: 0x18
-  __DATA.__data: 0x3e58
+  __DATA.__data: 0x3e78
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x660
+  __DATA.__bss: 0x210
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/vImage
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F89F2CEA-1C40-3823-B64A-BD66CEDB009B
-  Functions: 4292
-  Symbols:   410
-  CStrings:  739
+  UUID: BFF06BD5-9F21-3F8F-9351-4B7CFC3FC4C8
+  Functions: 4142
+  Symbols:   393
+  CStrings:  742
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
+ __os_signpost_emit_unreliably_with_name_impl
+ _os_retain
+ _os_signpost_enabled
+ _pthread_threadid_np
+ _timespec_get
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEcm
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE5eraseEmm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_mmRKS4_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_
- __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b
- __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEx
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strERKNS_12basic_stringIcS2_S4_EE
- __ZNSt3__14cerrE
- __ZNSt3__14coutE
- __ZNSt3__16chrono12steady_clock3nowEv
- __ZNSt3__16chrono12system_clock3nowEv
- __ZNSt3__16chrono12system_clock9to_time_tERKNS0_10time_pointIS1_NS0_8durationIxNS_5ratioILl1ELl1000000EEEEEEE
- _localtime_r
- _pthread_self
- _strftime
- _strncpy
- _strrchr
- _vsnprintf
CStrings:
+ " Espresso inputs can't have pre processing with direct bind."
+ "!(needs_pp && use_direct_bind)"
+ "!einput.rgb_bias && !einput.scale_factor && !einput.use_bgr"
+ "!m_param.op_desc_quant.has_value()"
+ "((std::is_same_v<UT, uint8_t> && data_type == BufferDataType::Uint8) || (std::is_same_v<UT, half> && data_type == BufferDataType::Float16) || (std::is_same_v<UT, float> && data_type == BufferDataType::Float32))"
+ "Abort: "
+ "Append descriptors failed"
+ "Append features failed"
+ "Both detector and descriptor PSHandle handles must be same for EndToEndModel."
+ "Bound espresso buffer is not of storage type float"
+ "Buffer type mismatch"
+ "CVPixelBufferGetIOSurface(ref)"
+ "Copy from float to uint8 buffer is not allowed"
+ "Data is not contiguous"
+ "Espresso execution with 1 non-float color component but multiple channels not yet implemented. Use interleaved (RGBA/BGRA) images instead"
+ "Espresso execution with non-float input of batch size greater than 1 not yet implemented."
+ "EspressoBufferToConstDataView32f currently expects FLOAT32 storage. Other buffer types not yet implemented."
+ "Generic tensor(s) in `RunData` out of order, must be consistent for each configuration."
+ "GetAllocatedBufferForGenericTensor: Allocated buffer has null buffer_obj"
+ "Given data block is too big to be represented by uint32_t indexed ArrayView"
+ "Index is larger than descriptors count"
+ "Invalid e5rt objects from pool."
+ "Invalid runtime device specified."
+ "IsContiguousMemory(data_view)"
+ "No error detected but output empty."
+ "Not implemented desc_quantization for binary network."
+ "Not implemented desc_quantization for float network."
+ "Number of used patches must be equal or less than the number of pathces."
+ "Only DeviceType::Any supported for EspressoV2"
+ "Plane index can't be more than total number of planes"
+ "Preprocessing arguments are not yet supported for generic input tensors"
+ "The DataView does not contain float data"
+ "The DataView does not contain half data"
+ "The DataView does not contain uint8 data"
+ "The input buffer is not IOSurface backed"
+ "Trace"
+ "Unable to set model configuration"
+ "_num_used_patches <= num_allocated_patches"
+ "append_ret"
+ "buffer.data_type != BufferDataType::Uint8"
+ "buffer_itr != input_buffer_map.end()"
+ "buffer_itr->second.buffer_obj"
+ "detector_ps_handle == descriptor_ps_handle"
+ "device != EspressoDevice::Any"
+ "format.Contains(FormatFlags::FLOAT16)"
+ "format.Contains(FormatFlags::FLOAT32)"
+ "format.Contains(FormatFlags::UINT8)"
+ "i < Size()"
+ "input.BatchSize() == 1"
+ "input.Planes() == 1"
+ "key_points size must be equal or less than the specified max size."
+ "m().config.max_keypoint_size >= key_points.size()"
+ "main"
+ "param.device == DeviceType::Any"
+ "results.storage_type == ESPRESSO_STORAGE_TYPE_FLOAT32"
+ "ret.outputs.has_value()"
+ "ret_config == kml::MLResultCode::NoError"
+ "std::holds_alternative<DataView32f>(buffer_view)"
+ "stream != nullptr && stream_op != nullptr"
+ "total_size < std::numeric_limits<uint32_t>::max()"
+ "tracing"
- " INFO"
- " NONE"
- " WARN"
- "!(needs_pp && use_direct_bind) && \" Espresso inputs can't have pre processing with direct bind.\""
- "!einput.rgb_bias && !einput.scale_factor && !einput.use_bgr && \"Preprocessing arguments are not yet supported for generic input tensors\""
- "!m_param.op_desc_quant.has_value() && \"Not implemented desc_quantization for binary network.\""
- "!m_param.op_desc_quant.has_value() && \"Not implemented desc_quantization for float network.\""
- "%"
- "%d [%t] %p %c: %m%n"
- "((std::is_same_v<UT, uint8_t> && data_type == BufferDataType::Uint8) || (std::is_same_v<UT, half> && data_type == BufferDataType::Float16) || (std::is_same_v<UT, float> && data_type == BufferDataType::Float32)) && \"Buffer type mismatch\""
- "0"
- "00"
- "00000000000000000000000000000000000000000"
- "CVPixelBufferGetIOSurface(ref) && \"The input buffer is not IOSurface backed\""
- "ConsoleAppender"
- "DEBUG"
- "ERROR"
- "FATAL"
- "ILayout"
- "IsContiguousMemory(data_view) && \"Data is not contiguous\""
- "PatternLayout"
- "Production"
- "TRACE"
- "_"
- "_num_used_patches <= num_allocated_patches && \"Number of used patches must be equal or less than the number of pathces.\""
- "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_."
- "append_ret && \"Append descriptors failed\""
- "append_ret && \"Append features failed\""
- "buffer.data_type != BufferDataType::Uint8 && \"Copy from float to uint8 buffer is not allowed\""
- "buffer_itr != input_buffer_map.end() && \"Generic tensor(s) in `RunData` out of order, must be consistent for \" \"each configuration.\""
- "buffer_itr->second.buffer_obj && \"GetAllocatedBufferForGenericTensor: Allocated buffer has null buffer_obj\""
- "bundle"
- "cv3dapi.lf"
- "descriptors_1"
- "detector_ps_handle == descriptor_ps_handle && \"Both detector and descriptor PSHandle handles must be same for EndToEndModel.\""
- "device != EspressoDevice::Any && \"Invalid runtime device specified.\""
- "format.Contains(FormatFlags::FLOAT16) && \"The DataView does not contain half data\""
- "format.Contains(FormatFlags::FLOAT32) && \"The DataView does not contain float data\""
- "format.Contains(FormatFlags::UINT8) && \"The DataView does not contain uint8 data\""
- "global_descriptor"
- "i < Size() && \"Index is larger than descriptors count\""
- "input.BatchSize() == 1 && \"Espresso execution with non-float input of batch size greater than 1 \" \"not yet implemented.\""
- "input.Planes() == 1 && \"Espresso execution with 1 non-float color component but multiple \" \"channels not yet implemented. Use interleaved (RGBA/BGRA) images instead\""
- "input_image"
- "input_keypoints"
- "input_patches"
- "keypoints"
- "local_descriptor_map"
- "m().config.max_keypoint_size >= key_points.size() && \"key_points size must be equal or less than the specified max size.\""
- "param.device == DeviceType::Any && \"Only DeviceType::Any supported for EspressoV2\""
- "plane_index < num_planes && \"Plane index can't be more than total number of planes\""
- "results.storage_type == ESPRESSO_STORAGE_TYPE_FLOAT32 && \"EspressoBufferToConstDataView32f currently expects FLOAT32 storage. Other buffer types \" \"not yet implemented.\""
- "ret.outputs.has_value() && \"No error detected but output empty.\""
- "ret_config == kml::MLResultCode::NoError && \"Unable to set model configuration\""
- "std::holds_alternative<DataView32f>(buffer_view) && \"Bound espresso buffer is not of storage type float\""
- "stream != nullptr && stream_op != nullptr && \"Invalid e5rt objects from pool.\""
- "total_size < std::numeric_limits<uint32_t>::max() && \"Given data block is too big to be represented by uint32_t indexed ArrayView\""
- "unknown file"
- "unknown function"
- "yyyy.mm.dd.HH-MM.SS.fff"

```
