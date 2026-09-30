## VideoProcessing

> `/System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing`

```diff

 1335.5.1.1.1
-  __TEXT.__text: 0x1dbee0
-  __TEXT.__auth_stubs: 0x2220
+  __TEXT.__text: 0x1dbad8
+  __TEXT.__auth_stubs: 0x2200
   __TEXT.__objc_methlist: 0x914
   __TEXT.__const: 0x377a0
-  __TEXT.__cstring: 0x7229
-  __TEXT.__gcc_except_tab: 0x54bc
-  __TEXT.__oslogstring: 0xa4c4
+  __TEXT.__cstring: 0x71eb
+  __TEXT.__gcc_except_tab: 0x54b0
+  __TEXT.__oslogstring: 0xa387
   __TEXT.__ustring: 0xa4
   __TEXT.__unwind_info: 0x2bf8
   __TEXT.__eh_frame: 0x4c0
   __TEXT.__objc_classname: 0x190
   __TEXT.__objc_methname: 0x288a
-  __TEXT.__objc_methtype: 0x128f
+  __TEXT.__objc_methtype: 0x12a1
   __TEXT.__objc_stubs: 0x1ae0
   __DATA_CONST.__got: 0xd00
   __DATA_CONST.__const: 0x2d90

   __DATA_CONST.__objc_selrefs: 0x7d0
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x1120
+  __AUTH_CONST.__auth_got: 0x1110
   __AUTH_CONST.__const: 0x1d18
-  __AUTH_CONST.__cfstring: 0x4b40
+  __AUTH_CONST.__cfstring: 0x4b00
   __AUTH_CONST.__objc_const: 0x21f8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x228

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F4F00E26-8355-3F6C-A65F-5CC9A21D0CAB
-  Functions: 3306
-  Symbols:   1378
-  CStrings:  3144
+  UUID: 7FCB0861-98BD-3310-9C2C-7260B1478813
+  Functions: 3305
+  Symbols:   1376
+  CStrings:  3133
 
Symbols:
- _IORegistryEntryGetName
- _IOServiceNameMatching
CStrings:
+ "{VCPCNNVideoEnhancer=\"interpolation_time_ms_meter_\"{EMAMeter=\"alpha_\"f\"last_\"f\"value_\"f\"max_\"f\"min_\"f\"calls_\"Q}\"model_\"{VideoEnhancerModel=\"index_\"i\"scale_factor_\"i\"input_width_\"i\"input_height_\"i\"model_input_width_\"i\"model_input_height_\"i\"output_width_\"i\"output_height_\"i\"model_output_width_\"i\"model_output_height_\"i\"reshape_\"B\"path_\"{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"\"{?=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}\"input_buffer_attributes_\"^{__CFDictionary}\"output_buffer_attributes_\"^{__CFDictionary}}\"espresso_model_\"{unique_ptr<EspressoModel, std::default_delete<EspressoModel>>=\"\"{?=\"__ptr_\"^{EspressoModel}}}\"input_buffer_pool_\"{CF<__CVPixelBufferPool *>=\"value_\"^{__CVPixelBufferPool}}\"transfer_session_\"{CF<OpaqueVTPixelTransferSession *>=\"value_\"^{OpaqueVTPixelTransferSession}}\"prev_frame_\"^{__CVBuffer}\"is_initialized_\"B\"scaling_\"B\"mutex_\"{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}}"
+ "{VideoEnhancerModel=\"index_\"i\"scale_factor_\"i\"input_width_\"i\"input_height_\"i\"model_input_width_\"i\"model_input_height_\"i\"output_width_\"i\"output_height_\"i\"model_output_width_\"i\"model_output_height_\"i\"reshape_\"B\"path_\"{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"\"{?=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}\"input_buffer_attributes_\"^{__CFDictionary}\"output_buffer_attributes_\"^{__CFDictionary}}"
- "IOPlatformExpertDevice"
- "VCPEnc %p (%dx%d, %s): Got 10b input and set HDRMetadataInsertionMode_Auto/HEVC_Main10_AutoLevel/bitdepth10\n"
- "VCPEnc %p (%dx%d, %s): Got 10b input and set HDRMetadataInsertionMode_Auto/HEVC_Main44410_AutoLevel/bitdepth10\n"
- "VCPEnc %p (%dx%d, %s): Got 8b 444 input and set HEVC_Main444_AutoLevel\n"
- "VCPEnc: Detected H18 A0"
- "arm-io"
- "chip-revision"
- "device_type"
- "t8150"
- "{VCPCNNVideoEnhancer=\"interpolation_time_ms_meter_\"{EMAMeter=\"alpha_\"f\"last_\"f\"value_\"f\"max_\"f\"min_\"f\"calls_\"Q}\"model_\"{VideoEnhancerModel=\"index_\"i\"scale_factor_\"i\"input_width_\"i\"input_height_\"i\"model_input_width_\"i\"model_input_height_\"i\"output_width_\"i\"output_height_\"i\"model_output_width_\"i\"model_output_height_\"i\"reshape_\"B\"path_\"{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}\"input_buffer_attributes_\"^{__CFDictionary}\"output_buffer_attributes_\"^{__CFDictionary}}\"espresso_model_\"{unique_ptr<EspressoModel, std::default_delete<EspressoModel>>=\"__ptr_\"^{EspressoModel}}\"input_buffer_pool_\"{CF<__CVPixelBufferPool *>=\"value_\"^{__CVPixelBufferPool}}\"transfer_session_\"{CF<OpaqueVTPixelTransferSession *>=\"value_\"^{OpaqueVTPixelTransferSession}}\"prev_frame_\"^{__CVBuffer}\"is_initialized_\"B\"scaling_\"B\"mutex_\"{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}}"
- "{VideoEnhancerModel=\"index_\"i\"scale_factor_\"i\"input_width_\"i\"input_height_\"i\"model_input_width_\"i\"model_input_height_\"i\"output_width_\"i\"output_height_\"i\"model_output_width_\"i\"model_output_height_\"i\"reshape_\"B\"path_\"{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}\"input_buffer_attributes_\"^{__CFDictionary}\"output_buffer_attributes_\"^{__CFDictionary}}"

```
