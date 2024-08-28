## JPEGH1.videodecoder

> `/System/Library/VideoDecoders/JPEGH1.videodecoder`

```diff

-3175.2.11.1.0
-  __TEXT.__text: 0x2b38
-  __TEXT.__auth_stubs: 0x690
-  __TEXT.__const: 0x34
-  __TEXT.__cstring: 0x9b
+3175.4.1.0.0
+  __TEXT.__text: 0x4358
+  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__const: 0x54
+  __TEXT.__cstring: 0x67d
+  __TEXT.__oslogstring: 0x630
   __TEXT.__unwind_info: 0xc8
   __DATA_CONST.__got: 0x148
   __DATA_CONST.__const: 0x40
-  __AUTH_CONST.__auth_got: 0x348
+  __AUTH_CONST.__auth_got: 0x378
   __AUTH_CONST.__const: 0xd8
-  __AUTH_CONST.__cfstring: 0x60
+  __AUTH_CONST.__cfstring: 0xa0
   __DATA.__data: 0x30
+  __DATA.__common: 0x10
   __DATA.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /usr/lib/libSystem.B.dylib
   Functions: 30
-  Symbols:   177
-  CStrings:  8
+  Symbols:   183
+  CStrings:  77
 
Symbols:
+ __os_log_send_and_compose_impl
+ _FigHostTimeToNanoseconds
+ _os_log_type_enabled
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _FigSignalErrorAt3
+ _fig_note_initialize_category_with_default_work_cf
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _FigSignalErrorAt
CStrings:
+ "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): Could not create H1JPEG software fallback session"
+ "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): performing software decode"
+ "Failed allocating attributes dictionary"
+ "Stevenote mode not supported on this platform (must not require strict MCU)"
+ "kVTVideoDecoderUnsupportedDataFormatErr"
+ "CFDictionaryCreate failed (once)"
+ "Couldn't open driver connection"
+ "JPEGH1Decoder.c"
+ "decode failed"
+ "kVTParameterErr"
+ "CFArrayCreate failed"
+ "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): Received decoded frame from SW!"
+ "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): Software decode looks good, giving up on hardware decode"
+ "H1JPEGVideoDecoder_CopySupportedPropertyDictionary"
+ "H1JPEGVideoDecoder_StartSession"
+ "kVTPropertyReadOnlyErr"
+ "H1JPEGVideoDecoder_CopyProperty"
+ "H1JPEGVideoDecoder_CreateInstance"
+ "err"
+ "jpeg_createSuggestedQualityOfServiceTiers"
+ "unrecognised property key"
+ "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): creating cached input surface %!d(MISSING) of size %!d(MISSING) bytes"
+ "CFDictionaryCreate failed"
+ "kVTAllocationFailedErr"
+ "width must be >32"
+ "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): Requested frame delivery rate of %!f(MISSING)"
+ "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): Software decoder failed, status = %!d(MISSING)"
+ "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): called async for frame %!d(MISSING)"
+ "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): Frame %!d(MISSING)"
+ "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): We gave up on the hardware decoder; going straight to software"
+ "height must be >16"
+ "jpeg_DecodeFrameAsynchronously"
+ "jpeg_DecodeFrameSynchronously_block_invoke"
+ "jpeg_createSupportedPropertyDictionary"
+ "kVTVideoDecoderNotAvailableNowErr"
+ "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): Decode complete for frame %!d(MISSING), total decode time: %!f(MISSING) ms"
+ "H1JPEGVideoDecoder_Invalidate"
+ "property is read-only"
+ "FigDerivedObjectCreate failed"
+ "H1JPEGVideoDecoder_DecodeFrame"
+ "bad property value - should be CFNumber"
+ "com.apple.coremedia"
+ "jpeg_initializeStevenote444fMode"
+ "result"
+ "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): Postprocessing complete for frame %!d(MISSING) (took %!f(MISSING) ms)"
+ "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): Waiting on pending frames to complete"
+ "CVPixelBufferPoolCreatePixelBuffer failed"
+ "H1JPEG decode failed"
+ "jpeg_DecodeFrameSynchronously"
+ "temp422IntSurface creation failed"
+ "<<<< H2JPEGDeviceInterface >>>> %!s(MISSING): WARNING: Got error code kIOReturnNotPermitted when opening JPEG HW codec service. You may need to add AppleJPEGDriverUserClient to your entitlements. See 60229261 for more information. May fall back to using SW codec."
+ "_openDriverConnection"
+ "jpeg_vtdecoder_trace"
+ "special444fMode requires async decompression!"
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
+ "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): performing hardware decode"
+ "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): waiting for temp422Int surface to become available"
+ "ReducedFrameDelivery out of range 0.0...1.0"
+ "createPixelBufferAttributesDictionary"
+ "kVTPropertyNotSupportedErr"
+ "<-<<< JPEGVTDecoder >>>->"
+ "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): VTSessionSetProperty(%!@(MISSING)) returned err = %!d(MISSING)"
+ "<<<< H2JPEGDeviceInterface >>>> %!s(MISSING): WARNING: Got error code %!d(MISSING) (0x%!X(MISSING)) when opening JPEG HW codec service. May fall back to using SW codec."
+ "H1JPEGVideoDecoder_SetProperty"
+ "createJPEGInputSurface"
+ "jpeg_asyncDecodeComplete"
+ "jpeg_createQualityOfServiceTier"
+ "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): Hardware decoder failed"
+ "CFNumberCreate failed"

```
