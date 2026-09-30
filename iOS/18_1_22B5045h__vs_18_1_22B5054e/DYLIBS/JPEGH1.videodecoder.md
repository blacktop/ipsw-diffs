## JPEGH1.videodecoder

> `/System/Library/VideoDecoders/JPEGH1.videodecoder`

```diff

-3175.6.2.11.2
-  __TEXT.__text: 0x4358
-  __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__const: 0x54
-  __TEXT.__cstring: 0x67d
-  __TEXT.__oslogstring: 0x630
+3175.8.3.11.1
+  __TEXT.__text: 0x2b38
+  __TEXT.__auth_stubs: 0x690
+  __TEXT.__const: 0x34
+  __TEXT.__cstring: 0x9b
   __TEXT.__unwind_info: 0xc8
   __DATA_CONST.__got: 0x148
   __DATA_CONST.__const: 0x40
-  __AUTH_CONST.__auth_got: 0x378
+  __AUTH_CONST.__auth_got: 0x348
   __AUTH_CONST.__const: 0xd8
-  __AUTH_CONST.__cfstring: 0xa0
+  __AUTH_CONST.__cfstring: 0x60
   __DATA.__data: 0x30
-  __DATA.__common: 0x10
   __DATA.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /usr/lib/libSystem.B.dylib
   Functions: 30
-  Symbols:   183
-  CStrings:  77
+  Symbols:   177
+  CStrings:  8
 
Symbols:
+ _FigSignalErrorAt
- _os_log_type_enabled
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _FigHostTimeToNanoseconds
- _FigSignalErrorAt3
- __os_log_send_and_compose_impl
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _fig_note_initialize_category_with_default_work_cf
CStrings:
- "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): performing software decode"
- "H1JPEGVideoDecoder_SetProperty"
- "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): Frame %!d(MISSING)"
- "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): Waiting on pending frames to complete"
- "H1JPEGVideoDecoder_StartSession"
- "FigDerivedObjectCreate failed"
- "H1JPEGVideoDecoder_DecodeFrame"
- "err"
- "jpeg_createSuggestedQualityOfServiceTiers"
- "kVTParameterErr"
- "property is read-only"
- "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): called async for frame %!d(MISSING)"
- "JPEGH1Decoder.c"
- "ReducedFrameDelivery out of range 0.0...1.0"
- "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): We gave up on the hardware decoder; going straight to software"
- "CVPixelBufferPoolCreatePixelBuffer failed"
- "result"
- "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): Requested frame delivery rate of %!f(MISSING)"
- "CFArrayCreate failed"
- "height must be >16"
- "jpeg_DecodeFrameSynchronously_block_invoke"
- "unrecognised property key"
- "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): creating cached input surface %!d(MISSING) of size %!d(MISSING) bytes"
- "kVTPropertyNotSupportedErr"
- "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): Decode complete for frame %!d(MISSING), total decode time: %!f(MISSING) ms"
- "Failed allocating attributes dictionary"
- "H1JPEGVideoDecoder_CreateInstance"
- "com.apple.coremedia"
- "jpeg_createQualityOfServiceTier"
- "temp422IntSurface creation failed"
- "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): Could not create H1JPEG software fallback session"
- "<<<< H2JPEGDeviceInterface >>>> %!s(MISSING): WARNING: Got error code %!d(MISSING) (0x%!X(MISSING)) when opening JPEG HW codec service. May fall back to using SW codec."
- "jpeg_createSupportedPropertyDictionary"
- "kVTVideoDecoderNotAvailableNowErr"
- "width must be >32"
- "<-<<< JPEGVTDecoder >>>->"
- "CFDictionaryCreate failed"
- "CFNumberCreate failed"
- "H1JPEGVideoDecoder_Invalidate"
- "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): Hardware decoder failed"
- "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): Received decoded frame from SW!"
- "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): Software decode looks good, giving up on hardware decode"
- "<<<< H2JPEGDeviceInterface >>>> %!s(MISSING): WARNING: Got error code kIOReturnNotPermitted when opening JPEG HW codec service. You may need to add AppleJPEGDriverUserClient to your entitlements. See 60229261 for more information. May fall back to using SW codec."
- "decode failed"
- "kVTPropertyReadOnlyErr"
- "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): Software decoder failed, status = %!d(MISSING)"
- "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): waiting for temp422Int surface to become available"
- "Couldn't open driver connection"
- "createPixelBufferAttributesDictionary"
- "jpeg_asyncDecodeComplete"
- "jpeg_initializeStevenote444fMode"
- "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
- "H1JPEGVideoDecoder_CopyProperty"
- "_openDriverConnection"
- "createJPEGInputSurface"
- "kVTVideoDecoderUnsupportedDataFormatErr"
- "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): Postprocessing complete for frame %!d(MISSING) (took %!f(MISSING) ms)"
- "H1JPEG decode failed"
- "jpeg_DecodeFrameAsynchronously"
- "jpeg_vtdecoder_trace"
- "kVTAllocationFailedErr"
- "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): VTSessionSetProperty(%!@(MISSING)) returned err = %!d(MISSING)"
- "Stevenote mode not supported on this platform (must not require strict MCU)"
- "bad property value - should be CFNumber"
- "special444fMode requires async decompression!"
- "<-<<< JPEGVTDecoder >>>-> %!s(MISSING): performing hardware decode"
- "CFDictionaryCreate failed (once)"
- "H1JPEGVideoDecoder_CopySupportedPropertyDictionary"
- "jpeg_DecodeFrameSynchronously"

```
