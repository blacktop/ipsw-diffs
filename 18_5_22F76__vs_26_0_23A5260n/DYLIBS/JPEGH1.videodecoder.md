## JPEGH1.videodecoder

> `/System/Library/VideoDecoders/JPEGH1.videodecoder`

```diff

-3225.7.1.0.0
-  __TEXT.__text: 0x2b08
-  __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__const: 0x34
-  __TEXT.__cstring: 0x9b
+3255.61.4.11.7
+  __TEXT.__text: 0x43c0
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__const: 0x54
+  __TEXT.__cstring: 0x67c
+  __TEXT.__oslogstring: 0x630
   __TEXT.__unwind_info: 0xd0
-  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__got: 0x150
   __DATA_CONST.__const: 0x40
-  __AUTH_CONST.__auth_got: 0x350
+  __AUTH_CONST.__auth_got: 0x390
   __AUTH_CONST.__const: 0xd8
-  __AUTH_CONST.__cfstring: 0x60
+  __AUTH_CONST.__cfstring: 0xa0
   __DATA.__bss: 0x48
   __DATA_DIRTY.__data: 0x30
-  __DATA_DIRTY.__bss: 0x20
+  __DATA_DIRTY.__common: 0x10
+  __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo

   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /usr/lib/libSystem.B.dylib
-  UUID: 406FE094-DD16-304B-BDD9-A985820681AD
-  Functions: 36
-  Symbols:   238
-  CStrings:  11
+  UUID: 8577C0A3-8103-3AFC-BEFD-15DC3B57FBB9
+  Functions: 49
+  Symbols:   270
+  CStrings:  82
 
Symbols:
+ _FigHostTimeToNanoseconds
+ _FigSignalErrorAt3
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _VTDecoderSessionCleanUpAfterDecode
+ _VTDecoderSessionCreatePixelBuffer
+ ___block_descriptor_tmp.47
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _gFigJPEGVTDecoderTrace
+ _kVTVideoDecoder_IsParavirtualizationAware
+ _os_log_type_enabled
- _FigSignalErrorAt
- ___block_descriptor_tmp.10
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "<-<<< JPEGVTDecoder >>>->"
+ "<-<<< JPEGVTDecoder >>>-> %s: Could not create H1JPEG software fallback session"
+ "<-<<< JPEGVTDecoder >>>-> %s: Decode complete for frame %d, total decode time: %.3f ms"
+ "<-<<< JPEGVTDecoder >>>-> %s: Frame %d"
+ "<-<<< JPEGVTDecoder >>>-> %s: Hardware decoder failed"
+ "<-<<< JPEGVTDecoder >>>-> %s: Postprocessing complete for frame %d (took %.3f ms)"
+ "<-<<< JPEGVTDecoder >>>-> %s: Received decoded frame from SW!"
+ "<-<<< JPEGVTDecoder >>>-> %s: Requested frame delivery rate of %f"
+ "<-<<< JPEGVTDecoder >>>-> %s: Software decode looks good, giving up on hardware decode"
+ "<-<<< JPEGVTDecoder >>>-> %s: Software decoder failed, status = %d"
+ "<-<<< JPEGVTDecoder >>>-> %s: VTSessionSetProperty(%@) returned err = %d"
+ "<-<<< JPEGVTDecoder >>>-> %s: Waiting on pending frames to complete"
+ "<-<<< JPEGVTDecoder >>>-> %s: We gave up on the hardware decoder; going straight to software"
+ "<-<<< JPEGVTDecoder >>>-> %s: called async for frame %d"
+ "<-<<< JPEGVTDecoder >>>-> %s: creating cached input surface %d of size %d bytes"
+ "<-<<< JPEGVTDecoder >>>-> %s: performing hardware decode"
+ "<-<<< JPEGVTDecoder >>>-> %s: performing software decode"
+ "<-<<< JPEGVTDecoder >>>-> %s: waiting for temp422Int surface to become available"
+ "<<<< H2JPEGDeviceInterface >>>> %s: WARNING: Got error code %d (0x%08X) when opening JPEG HW codec service. May fall back to using SW codec."
+ "<<<< H2JPEGDeviceInterface >>>> %s: WARNING: Got error code kIOReturnNotPermitted when opening JPEG HW codec service. You may need to add AppleJPEGDriverUserClient to your entitlements. See 60229261 for more information. May fall back to using SW codec."
+ "CFArrayCreate failed"
+ "CFDictionaryCreate failed"
+ "CFDictionaryCreate failed (once)"
+ "CFNumberCreate failed"
+ "Couldn't open driver connection"
+ "Failed allocating attributes dictionary"
+ "FigDerivedObjectCreate failed"
+ "H1JPEG decode failed"
+ "H1JPEGVideoDecoder_CopyProperty"
+ "H1JPEGVideoDecoder_CopySupportedPropertyDictionary"
+ "H1JPEGVideoDecoder_CreateInstance"
+ "H1JPEGVideoDecoder_DecodeFrame"
+ "H1JPEGVideoDecoder_Invalidate"
+ "H1JPEGVideoDecoder_SetProperty"
+ "H1JPEGVideoDecoder_StartSession"
+ "JPEGH1Decoder.c"
+ "ReducedFrameDelivery out of range 0.0...1.0"
+ "Stevenote mode not supported on this platform (must not require strict MCU)"
+ "VTDecoderSessionCreatePixelBuffer failed"
+ "_openDriverConnection"
+ "bad property value - should be CFNumber"
+ "com.apple.coremedia"
+ "createJPEGInputSurface"
+ "createPixelBufferAttributesDictionary"
+ "decode failed"
+ "err"
+ "height must be >16"
+ "jpeg_DecodeFrameAsynchronously"
+ "jpeg_DecodeFrameSynchronously"
+ "jpeg_DecodeFrameSynchronously_block_invoke"
+ "jpeg_asyncDecodeComplete"
+ "jpeg_createQualityOfServiceTier"
+ "jpeg_createSuggestedQualityOfServiceTiers"
+ "jpeg_createSupportedPropertyDictionary"
+ "jpeg_initializeStevenote444fMode"
+ "jpeg_vtdecoder_trace"
+ "kVTAllocationFailedErr"
+ "kVTParameterErr"
+ "kVTPropertyNotSupportedErr"
+ "kVTPropertyReadOnlyErr"
+ "kVTVideoDecoderNotAvailableNowErr"
+ "kVTVideoDecoderUnsupportedDataFormatErr"
+ "property is read-only"
+ "result"
+ "special444fMode requires async decompression!"
+ "temp422IntSurface creation failed"
+ "unrecognised property key"
+ "width must be >32"

```
