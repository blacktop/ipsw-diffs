## AppC3D

> `/System/Library/PrivateFrameworks/AppC3D.framework/AppC3D`

```diff

-1.13.1.0.0
-  __TEXT.__text: 0x2b345c
-  __TEXT.__auth_stubs: 0x1b70
-  __TEXT.__const: 0x2c829
-  __TEXT.__gcc_except_tab: 0x15598
-  __TEXT.__cstring: 0xc476
+1.13.7.0.0
+  __TEXT.__text: 0x2e8f5c
+  __TEXT.__auth_stubs: 0x1b60
+  __TEXT.__const: 0x2c5af
+  __TEXT.__gcc_except_tab: 0x18174
+  __TEXT.__cstring: 0xcee4
   __TEXT.__oslogstring: 0x56
-  __TEXT.__unwind_info: 0x83a8
+  __TEXT.__unwind_info: 0x8704
   __TEXT.__eh_frame: 0x238
   __TEXT.__objc_methname: 0x46
   __TEXT.__objc_stubs: 0x80
   __DATA_CONST.__got: 0x300
-  __DATA_CONST.__const: 0x13e0
+  __DATA_CONST.__const: 0x1538
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x20
-  __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__auth_ptr: 0x60
+  __DATA_CONST.__objc_classrefs: 0x18
+  __AUTH_CONST.__const: 0x1448
+  __AUTH_CONST.__auth_ptr: 0x68
   __AUTH_CONST.__cfstring: 0x280
-  __AUTH_CONST.__auth_got: 0xdc8
+  __AUTH_CONST.__auth_got: 0xdc0
+  __AUTH.__data: 0x8
   __DATA.__got_weak: 0x8
-  __DATA.__objc_classrefs: 0x18
-  __DATA.__data: 0x3e38
+  __DATA.__data: 0x3ed0
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x48
+  __DATA.__bss: 0x68
   __DATA.__common: 0x28
-  __DATA_DIRTY.__const: 0xf958
-  __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__bss: 0x6f8
+  __DATA_DIRTY.__const: 0xec70
+  __DATA_DIRTY.__data: 0x58
+  __DATA_DIRTY.__bss: 0x718
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6486
-  Symbols:   585
-  CStrings:  1110
+  Functions: 6601
+  Symbols:   582
+  CStrings:  1204
 
Symbols:
+ __ZNSt13runtime_errorC1ERKS_
+ __ZNSt3__118condition_variable4waitERNS_11unique_lockINS_5mutexEEE
+ __ZNSt3__14__fs10filesystem16_FilesystemClock3nowEv
+ __ZNSt3__16thread4joinEv
+ __ZnamSt11align_val_t
+ __os_log_pack_fill
+ __os_log_pack_size
+ _cblas_sgemv$NEWLAPACK
+ _dsysv$NEWLAPACK
+ _malloc_type_aligned_alloc
+ _os_log_pack_send
+ _sgesvd$NEWLAPACK
+ _snprintf
+ _spotrf$NEWLAPACK
+ _ssytrf$NEWLAPACK
+ _ssytrs$NEWLAPACK
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEcm
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE5rfindEcm
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE5eraseEmm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_mmRKS4_
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strERKNS_12basic_stringIcS2_S4_EE
- _cblas_sgemv
- _dsysv_
- _sgesvd_
- _spotrf_
- _ssytrf_
- _ssytrs_
- _strtoul
CStrings:
+ " Class ID out of range!"
+ " Espresso inputs can't have pre processing with direct bind."
+ " at line "
+ "!(needs_pp && use_direct_bind)"
+ "!einput.rgb_bias && !einput.scale_factor && !einput.use_bgr"
+ "','"
+ "':'"
+ "'['"
+ "'[', '{', or a literal"
+ "']'"
+ "'{'"
+ "'}'"
+ "((std::is_same_v<UT, uint8_t> && data_type == BufferDataType::Uint8) || (std::is_same_v<UT, half> && data_type == BufferDataType::Float16) || (std::is_same_v<UT, float> && data_type == BufferDataType::Float32))"
+ "(camera_stream_id == 0 || camera_stream_id == 1)"
+ ", column "
+ "- "
+ ". Last error message: "
+ "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Essentials/Thread/src/DispatchQueue.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Essentials/Thread/src/DispatchQueueTypeUtil.cpp"
+ "; last read: '"
+ "<U+%.4X>"
+ "Abort: "
+ "Bound espresso buffer is not of storage type float"
+ "Buffer type mismatch"
+ "CVPixelBufferGetIOSurface(ref)"
+ "Context may not be nullptr"
+ "Copy from float to uint8 buffer is not allowed"
+ "Empty tracker configs is not supported. Instantiate DetectODTPipelineType::Detect instead"
+ "Empty variant lens model invoked."
+ "Espresso execution with 1 non-float color component but multiple channels not yet implemented. Use interleaved (RGBA/BGRA) images instead"
+ "Espresso execution with non-float input of batch size greater than 1 not yet implemented."
+ "EspressoBufferToConstDataView32f currently expects FLOAT32 storage. Other buffer types not yet implemented."
+ "EspressoStreamPool: Failed to create e5rt stream operation.  Return code: "
+ "EspressoStreamPool: Failed to create e5rt stream.  Return code: "
+ "Execution stream encode workload failed.  Return code: "
+ "Execution stream execute failed.  Return code: "
+ "Execution stream reset failed.  Return code: "
+ "Failed to create pixel buffer"
+ "Function should contain valid target"
+ "Generic tensor(s) in `RunData` out of order, must be consistent for each configuration."
+ "GetAllocatedBufferForGenericTensor: Allocated buffer has null buffer_obj"
+ "Given data block is too big to be represented by uint32_t indexed ArrayView"
+ "Incorrect stread id"
+ "Invalid e5rt objects from pool."
+ "Invalid runtime device specified."
+ "Must have valid lens model to compute frustum extrema."
+ "OSLogAppender"
+ "Plane index can't be more than total number of planes"
+ "Pose unavailable for world tracking congifuration"
+ "Preprocessing arguments are not yet supported for generic input tensors"
+ "Requested 8-bit image, but buffer is 16-bit"
+ "The DataView does not contain float data"
+ "The DataView does not contain half data"
+ "The DataView does not contain uint8 data"
+ "The DetectTrackRefinePipeline doesn't seem to exist, it has to be created once before reconfiguring"
+ "The input buffer is not IOSurface backed"
+ "[json.exception."
+ "] "
+ "_f"
+ "array"
+ "binary"
+ "boolean"
+ "buffer.data_type != BufferDataType::Uint8"
+ "buffer_itr != input_buffer_map.end()"
+ "buffer_itr->second.buffer_obj"
+ "camera_stream_id == 0"
+ "cannot use erase() with "
+ "cannot use operator[] with a string argument with "
+ "cbcr_pixel_buffer"
+ "com.apple.odt.duplicates_visibility_threshold"
+ "context"
+ "context != nullptr"
+ "device != EspressoDevice::Any"
+ "dispatch_group_wait failed"
+ "dispatch_queue"
+ "error == 0"
+ "format.Contains(FormatFlags::FLOAT16)"
+ "format.Contains(FormatFlags::FLOAT32)"
+ "format.Contains(FormatFlags::UINT8)"
+ "inf.max_batch_size == 1 || (inf.max_batch_size >= objects.size() && inf.num_inference_cameras > 1) || (inf.max_batch_size >= objects.size() * num_inference_cams && inf.num_inference_cameras == 1)"
+ "input.BatchSize() == 1"
+ "input.Planes() == 1"
+ "invalid BOM; must be 0xEF 0xBB 0xBF if given"
+ "invalid comment; expecting '/' or '*' after '/'"
+ "invalid comment; missing closing '*/'"
+ "invalid literal"
+ "invalid number; expected '+', '-', or digit after exponent"
+ "invalid number; expected digit after '-'"
+ "invalid number; expected digit after '.'"
+ "invalid number; expected digit after exponent sign"
+ "invalid string: '\\u' must be followed by 4 hex digits"
+ "invalid string: control character U+0000 (NUL) must be escaped to \\u0000"
+ "invalid string: control character U+0001 (SOH) must be escaped to \\u0001"
+ "invalid string: control character U+0002 (STX) must be escaped to \\u0002"
+ "invalid string: control character U+0003 (ETX) must be escaped to \\u0003"
+ "invalid string: control character U+0004 (EOT) must be escaped to \\u0004"
+ "invalid string: control character U+0005 (ENQ) must be escaped to \\u0005"
+ "invalid string: control character U+0006 (ACK) must be escaped to \\u0006"
+ "invalid string: control character U+0007 (BEL) must be escaped to \\u0007"
+ "invalid string: control character U+0008 (BS) must be escaped to \\u0008 or \\b"
+ "invalid string: control character U+0009 (HT) must be escaped to \\u0009 or \\t"
+ "invalid string: control character U+000A (LF) must be escaped to \\u000A or \\n"
+ "invalid string: control character U+000B (VT) must be escaped to \\u000B"
+ "invalid string: control character U+000C (FF) must be escaped to \\u000C or \\f"
+ "invalid string: control character U+000D (CR) must be escaped to \\u000D or \\r"
+ "invalid string: control character U+000E (SO) must be escaped to \\u000E"
+ "invalid string: control character U+000F (SI) must be escaped to \\u000F"
+ "invalid string: control character U+0010 (DLE) must be escaped to \\u0010"
+ "invalid string: control character U+0011 (DC1) must be escaped to \\u0011"
+ "invalid string: control character U+0012 (DC2) must be escaped to \\u0012"
+ "invalid string: control character U+0013 (DC3) must be escaped to \\u0013"
+ "invalid string: control character U+0014 (DC4) must be escaped to \\u0014"
+ "invalid string: control character U+0015 (NAK) must be escaped to \\u0015"
+ "invalid string: control character U+0016 (SYN) must be escaped to \\u0016"
+ "invalid string: control character U+0017 (ETB) must be escaped to \\u0017"
+ "invalid string: control character U+0018 (CAN) must be escaped to \\u0018"
+ "invalid string: control character U+0019 (EM) must be escaped to \\u0019"
+ "invalid string: control character U+001A (SUB) must be escaped to \\u001A"
+ "invalid string: control character U+001B (ESC) must be escaped to \\u001B"
+ "invalid string: control character U+001C (FS) must be escaped to \\u001C"
+ "invalid string: control character U+001D (GS) must be escaped to \\u001D"
+ "invalid string: control character U+001E (RS) must be escaped to \\u001E"
+ "invalid string: control character U+001F (US) must be escaped to \\u001F"
+ "invalid string: forbidden character after backslash"
+ "invalid string: ill-formed UTF-8 byte"
+ "invalid string: missing closing quote"
+ "invalid string: surrogate U+D800..U+DBFF must be followed by U+DC00..U+DFFF"
+ "invalid string: surrogate U+DC00..U+DFFF must follow U+D800..U+DBFF"
+ "invalid_iterator"
+ "iterator out of range"
+ "k16BitDepth"
+ "m_ != nullptr"
+ "main"
+ "min_num_triangulation"
+ "null"
+ "num_inference_cams <= T_c0cn_vec_.size()"
+ "number"
+ "number overflow parsing '"
+ "object"
+ "object key"
+ "object separator"
+ "out_of_range"
+ "parse error"
+ "parse_error"
+ "plane_index < num_planes"
+ "priv().initialized_root_appenders_ == current_root_appenders"
+ "results.storage_type == ESPRESSO_STORAGE_TYPE_FLOAT32"
+ "root appenders have been illegally modified between Initialize() and Enable() of APILogging"
+ "scheduler must be valid"
+ "std::holds_alternative<DataView32f>(buffer_view)"
+ "stream != nullptr && stream_op != nullptr"
+ "string"
+ "syntax error "
+ "total_size < std::numeric_limits<uint32_t>::max()"
+ "tracker_config.class_id < m_->num_classes"
+ "type_error"
+ "unexpected "
+ "unique_lock::lock: already locked"
+ "unique_lock::lock: references null mutex"
+ "unique_lock::unlock: not locked"
+ "validate()"
+ "vio_to_cam_opt"
+ "while parsing "
+ "widthStep >= minimum_width_step"
+ "widthStep must be at least as big as minimum_width_step."
+ "y_pixel_buffer"
- "\b"
- "\t"
- "\f"
- "\r"
- "!(needs_pp && use_direct_bind) && \" Espresso inputs can't have pre processing with direct bind.\""
- "!config.tracker_configs.empty() && \"Empty tracker configs is not supported. Instantiate \" \"DetectODTPipelineType::Detect instead\""
- "!einput.rgb_bias && !einput.scale_factor && !einput.use_bgr && \"Preprocessing arguments are not yet supported for generic input tensors\""
- "\""
- "((std::is_same_v<UT, uint8_t> && data_type == BufferDataType::Uint8) || (std::is_same_v<UT, half> && data_type == BufferDataType::Float16) || (std::is_same_v<UT, float> && data_type == BufferDataType::Float32)) && \"Buffer type mismatch\""
- "(camera_stream_id == 0 || camera_stream_id == 1) && \"Incorrect stread id\""
- ". Supported functions are: "
- "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/AppCode/AppCodeAPI/src/AppCodeContext.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Essentials/Thread/src/WorkQueue.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Essentials/Thread/src/WorkQueueTypeUtil.cpp"
- "3DKeyPoints"
- "AppCodeProcessorNode"
- "CVPixelBufferGetIOSurface(ref) && \"The input buffer is not IOSurface backed\""
- "Execution stream encode workload failed."
- "Execution stream execute failed."
- "Execution stream reset failed."
- "OSLogSurrogateAppender"
- "Production"
- "\\"
- "_f && \"Function should contain valid target\""
- "buffer.data_type != BufferDataType::Uint8 && \"Copy from float to uint8 buffer is not allowed\""
- "buffer_itr != input_buffer_map.end() && \"Generic tensor(s) in `RunData` out of order, must be consistent for \" \"each configuration.\""
- "buffer_itr->second.buffer_obj && \"GetAllocatedBufferForGenericTensor: Allocated buffer has null buffer_obj\""
- "camera_stream_id == 0 && \"Incorrect stread id\""
- "cannot use operator[] with "
- "cannot use push_back() with "
- "cbcr_pixel_buffer && \"Failed to create pixel buffer\""
- "code points above 0x10FFFF are invalid"
- "context != nullptr && \"Context may not be nullptr\""
- "context && \"Context may not be nullptr\""
- "coords_"
- "data_container_->group_ && \"Dispatch group is not initialized\""
- "data_container_->queue_ && \"Dispatch queue is not initialized\""
- "device != EspressoDevice::Any && \"Invalid runtime device specified.\""
- "e0e9cdfebebb3f26959b58bc471c60446f569593"
- "error == 0 && \"dispatch_group_wait failed\""
- "false && \"Empty variant lens model invoked.\""
- "format.Contains(FormatFlags::FLOAT16) && \"The DataView does not contain half data\""
- "format.Contains(FormatFlags::FLOAT32) && \"The DataView does not contain float data\""
- "format.Contains(FormatFlags::UINT8) && \"The DataView does not contain uint8 data\""
- "hw.optional.arm.FEAT_SME"
- "inf.max_batch_size == 1 || (inf.max_batch_size >= objects.size() && inf.num_inference_cameras > 1) || (inf.max_batch_size >= objects.size() * num_cams && inf.num_inference_cameras == 1)"
- "input.BatchSize() == 1 && \"Espresso execution with non-float input of batch size greater than 1 \" \"not yet implemented.\""
- "input.Planes() == 1 && \"Espresso execution with 1 non-float color component but multiple \" \"channels not yet implemented. Use interleaved (RGBA/BGRA) images instead\""
- "k16BitDepth && \"Requested 8-bit image, but buffer is 16-bit\""
- "low_res_"
- "m_ != nullptr && \"The DetectTrackRefinePipeline doesn't seem to exist, it has to be \" \"created once before reconfiguring\""
- "missing high surrogate"
- "missing low surrogate"
- "missing or wrong low surrogate"
- "model.bundle"
- "parse error - unexpected "
- "pixel_buffers_processed.size() == T_c0cn_vec_.size()"
- "plane_index < num_planes && \"Plane index can't be more than total number of planes\""
- "priv().initialized_root_appenders_ == current_root_appenders && \"root appenders have been illegally modified between Initialize() and \" \"Enable() of APILogging\""
- "results.storage_type == ESPRESSO_STORAGE_TYPE_FLOAT32 && \"EspressoBufferToConstDataView32f currently expects FLOAT32 storage. Other buffer types \" \"not yet implemented.\""
- "scheduler_ && \"scheduler must be valid\""
- "std::holds_alternative<DataView32f>(buffer_view) && \"Bound espresso buffer is not of storage type float\""
- "stream != nullptr && stream_op != nullptr && \"Invalid e5rt objects from pool.\""
- "stream error"
- "stream_op_ret == E5RT_ERROR_CODE_OK && stream_op != nullptr && \"EspressoStreamPool: Failed to create e5rt stream operation.\""
- "stream_ret == E5RT_ERROR_CODE_OK && stream != nullptr && \"EspressoStreamPool: Failed to create e5rt stream.\""
- "total_size < std::numeric_limits<uint32_t>::max() && \"Given data block is too big to be represented by uint32_t indexed ArrayView\""
- "tracker_config.class_id < m_->num_classes && \" Class ID out of range!\""
- "validate() && \"Must have valid lens model to compute frustum extrema.\""
- "vio_to_cam_opt && \"Pose unavailable for world tracking congifuration\""
- "widthStep >= minimum_width_step && \"widthStep must be at least as big as minimum_width_step.\""
- "y_pixel_buffer && \"Failed to create pixel buffer\""

```
