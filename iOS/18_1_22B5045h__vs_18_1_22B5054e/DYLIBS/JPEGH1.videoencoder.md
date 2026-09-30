## JPEGH1.videoencoder

> `/System/Library/VideoEncoders/JPEGH1.videoencoder`

```diff

-3175.6.2.11.2
-  __TEXT.__text: 0x3698
-  __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x4a0
-  __TEXT.__oslogstring: 0x5a8
+3175.8.3.11.1
+  __TEXT.__text: 0x2088
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__const: 0x10
+  __TEXT.__cstring: 0xd4
   __TEXT.__unwind_info: 0xc0
   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__const: 0x80
-  __AUTH_CONST.__auth_got: 0x2f8
+  __AUTH_CONST.__auth_got: 0x2c0
   __AUTH_CONST.__const: 0x188
-  __AUTH_CONST.__cfstring: 0x100
+  __AUTH_CONST.__cfstring: 0xc0
   __DATA.__data: 0x20
-  __DATA.__common: 0x20
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /usr/lib/libSystem.B.dylib
   Functions: 26
-  Symbols:   154
-  CStrings:  64
+  Symbols:   147
+  CStrings:  10
 
Symbols:
+ _FigSignalErrorAt
- __os_log_send_and_compose_impl
- _fig_note_initialize_category_with_default_work_cf
- _FigHostTimeToNanoseconds
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _FigGetUpTime
- _FigSignalErrorAt3
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _os_log_type_enabled
CStrings:
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): Encode Result: %!d(MISSING), time: %!f(MISSING) ms, surface size: %!d(MISSING), quality: %!d(MISSING) (%!d(MISSING))"
- "kVTParameterErr"
- "stevenote_accumulate"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): Frame %!d(MISSING) Start Encode"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): rate controller DISABLED"
- "H1JPEGEncoder_SetProperty"
- "JPEGH1Encoder.c"
- "hardware jpeg encode failed"
- "jpeg_encodeFrameSync"
- "openJPEGDriverUserClientConnection"
- "<-<<< JPEGEncoderRateController >>>-> %!s(MISSING): presentationTimeStamp_curr.value %!l(MISSING)ld presentationTimeStamp_curr.timescale %!d(MISSING)"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): Input pixelBuffer is not IOSurface backed"
- "CFDictionaryCreate failed"
- "jpegEncoder_createSupportedPropertyDictionary"
- "<-<<< JPEGEncoderRateController >>>-> %!s(MISSING): frame_bits_prev %!d(MISSING) < wanted_bits %!d(MISSING) deltaIndex (+%!d(MISSING) +%!d(MISSING)) Index (%!d(MISSING) %!d(MISSING))"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): Frame %!d(MISSING)"
- "bad quality value"
- "stevenote_rc_init"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): rate controller enabled, max Mbps: %!d(MISSING), window size (frames): %!d(MISSING)"
- "kVTAllocationFailedErr"
- "kVTPropertyNotSupportedErr"
- "stevenote_rc_update_index"
- "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): Emit Frame %!d(MISSING) Stop"
- "H1JPEGEncoder_CopySupportedPropertyDictionary"
- "bad quality"
- "H1JPEGEncoder_CreateInstance"
- "unrecognised property key"
- "<-<<< JPEGVTEncoder >>>->"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): Could not open connection to jpeg driver"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): Frame %!d(MISSING) Start Preproc"
- "H1JPEGEncoder_StartSession"
- "err"
- "jpeg_vtencoder_trace"
- "<-<<< JPEGEncoderRateController >>>-> %!s(MISSING): Init Index %!d(MISSING), bitrate %!d(MISSING)"
- "H1JPEGEncoder_CheckExistence"
- "H1JPEGEncoder_EncodeFrame"
- "<-<<< JPEGEncoderRateController >>>-> %!s(MISSING): presentationTimeStamp_prev.value %!l(MISSING)ld presentationTimeStamp_prev.timescale %!d(MISSING)"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): Waiting for previous frame to finish encoding to ensure in-order emits..."
- "jpeg_encoder_rc_trace"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): Emit Frame %!d(MISSING) Start"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): Frame %!d(MISSING) Finish Preproc"
- "H1JPEGEncoder_CopyProperty"
- "failed to obtain encodedBuffer struct"
- "ioErr"
- "FigDerivedObjectCreate failed"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): Frame %!d(MISSING) Finish Encode"
- "<-<<< JPEGVTEncoder >>>-> Fig"
- "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/JPEGH1Codec/JPEGH1Encoder.c"
- "CFDictionaryCreate failed (once)"
- "jpeg_emitEncodedFrame"
- "jpeg_encodeFrameAsyncInternal"
- "<-<<< JPEGEncoderRateController >>>-> %!s(MISSING): frame_bits %!d(MISSING) framerate %!d(MISSING)"
- "<-<<< JPEGEncoderRateController >>>-> %!s(MISSING): frame_bits_prev %!d(MISSING) > wanted_bits %!d(MISSING) deltaIndex (-%!d(MISSING) -%!d(MISSING)) Index (%!d(MISSING) %!d(MISSING))"

```
