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
- _FigGetUpTime
- _FigHostTimeToNanoseconds
- _fig_note_initialize_category_with_default_work_cf
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _FigSignalErrorAt3
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- __os_log_send_and_compose_impl
- _os_log_type_enabled
CStrings:
- "<-<<< JPEGEncoderRateController >>>-> %!s(MISSING): Init Index %!d(MISSING), bitrate %!d(MISSING)"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): Emit Frame %!d(MISSING) Stop"
- "CFDictionaryCreate failed"
- "failed to obtain encodedBuffer struct"
- "jpeg_encodeFrameAsyncInternal"
- "openJPEGDriverUserClientConnection"
- "H1JPEGEncoder_CreateInstance"
- "hardware jpeg encode failed"
- "H1JPEGEncoder_CopySupportedPropertyDictionary"
- "stevenote_rc_update_index"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): Encode Result: %!d(MISSING), time: %!f(MISSING) ms, surface size: %!d(MISSING), quality: %!d(MISSING) (%!d(MISSING))"
- "H1JPEGEncoder_EncodeFrame"
- "bad quality"
- "err"
- "kVTParameterErr"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): rate controller enabled, max Mbps: %!d(MISSING), window size (frames): %!d(MISSING)"
- "<-<<< JPEGVTEncoder >>>-> Fig"
- "FigDerivedObjectCreate failed"
- "unrecognised property key"
- "<-<<< JPEGEncoderRateController >>>-> %!s(MISSING): presentationTimeStamp_curr.value %!l(MISSING)ld presentationTimeStamp_curr.timescale %!d(MISSING)"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): Could not open connection to jpeg driver"
- "H1JPEGEncoder_CopyProperty"
- "ioErr"
- "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/JPEGH1Codec/JPEGH1Encoder.c"
- "<-<<< JPEGEncoderRateController >>>-> %!s(MISSING): frame_bits_prev %!d(MISSING) > wanted_bits %!d(MISSING) deltaIndex (-%!d(MISSING) -%!d(MISSING)) Index (%!d(MISSING) %!d(MISSING))"
- "<-<<< JPEGEncoderRateController >>>-> %!s(MISSING): presentationTimeStamp_prev.value %!l(MISSING)ld presentationTimeStamp_prev.timescale %!d(MISSING)"
- "<-<<< JPEGVTEncoder >>>->"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): Frame %!d(MISSING) Finish Encode"
- "jpeg_vtencoder_trace"
- "stevenote_rc_init"
- "H1JPEGEncoder_CheckExistence"
- "H1JPEGEncoder_SetProperty"
- "jpeg_encodeFrameSync"
- "jpeg_encoder_rc_trace"
- "kVTPropertyNotSupportedErr"
- "<-<<< JPEGEncoderRateController >>>-> %!s(MISSING): frame_bits %!d(MISSING) framerate %!d(MISSING)"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): Emit Frame %!d(MISSING) Start"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): Frame %!d(MISSING) Start Encode"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): Frame %!d(MISSING) Start Preproc"
- "CFDictionaryCreate failed (once)"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): Frame %!d(MISSING) Finish Preproc"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): rate controller DISABLED"
- "<-<<< JPEGEncoderRateController >>>-> %!s(MISSING): frame_bits_prev %!d(MISSING) < wanted_bits %!d(MISSING) deltaIndex (+%!d(MISSING) +%!d(MISSING)) Index (%!d(MISSING) %!d(MISSING))"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): Waiting for previous frame to finish encoding to ensure in-order emits..."
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): Frame %!d(MISSING)"
- "bad quality value"
- "jpegEncoder_createSupportedPropertyDictionary"
- "jpeg_emitEncodedFrame"
- "stevenote_accumulate"
- "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
- "<-<<< JPEGVTEncoder >>>-> %!s(MISSING): Input pixelBuffer is not IOSurface backed"
- "H1JPEGEncoder_StartSession"
- "JPEGH1Encoder.c"
- "kVTAllocationFailedErr"

```
