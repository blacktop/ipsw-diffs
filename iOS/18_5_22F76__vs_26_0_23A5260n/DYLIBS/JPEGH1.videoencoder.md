## JPEGH1.videoencoder

> `/System/Library/VideoEncoders/JPEGH1.videoencoder`

```diff

-3225.7.1.0.0
-  __TEXT.__text: 0x20d0
-  __TEXT.__auth_stubs: 0x590
-  __TEXT.__const: 0x10
-  __TEXT.__cstring: 0xd4
-  __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__got: 0xf8
+3255.61.4.11.7
+  __TEXT.__text: 0x3704
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__const: 0x40
+  __TEXT.__cstring: 0x4a0
+  __TEXT.__oslogstring: 0x5a8
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x80
-  __AUTH_CONST.__auth_got: 0x2c8
+  __AUTH_CONST.__auth_got: 0x300
   __AUTH_CONST.__const: 0x188
-  __AUTH_CONST.__cfstring: 0xc0
+  __AUTH_CONST.__cfstring: 0x100
   __DATA.__data: 0x20
+  __DATA.__common: 0x20
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /usr/lib/libSystem.B.dylib
-  UUID: B3DB07C6-115E-340D-98F0-233E016E751D
+  UUID: 143CAD74-AA0B-3838-8488-7A120E89259F
   Functions: 28
-  Symbols:   192
-  CStrings:  16
+  Symbols:   202
+  CStrings:  72
 
Symbols:
+ _FigGetUpTime
+ _FigHostTimeToNanoseconds
+ _FigSignalErrorAt3
+ ___block_descriptor_tmp.24
+ ___block_descriptor_tmp.36
+ ___block_descriptor_tmp.41
+ ___block_literal_global.26
+ ___block_literal_global.43
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _gFigJPEGEncoderRateController
+ _gFigJPEGVTEncoderTrace
+ _kVTVideoEncoder_IsParavirtualizationAware
+ _os_log_type_enabled
- _FigSignalErrorAt
- ___block_descriptor_tmp.19
- ___block_descriptor_tmp.20
- ___block_descriptor_tmp.4
- ___block_literal_global.22
- ___block_literal_global.6
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/JPEGH1Codec/JPEGH1Encoder.c"
+ "<-<<< JPEGEncoderRateController >>>-> %s: Init Index %d, bitrate %d"
+ "<-<<< JPEGEncoderRateController >>>-> %s: frame_bits %d framerate %d"
+ "<-<<< JPEGEncoderRateController >>>-> %s: frame_bits_prev %d < wanted_bits %d deltaIndex (+%d +%d) Index (%d %d)"
+ "<-<<< JPEGEncoderRateController >>>-> %s: frame_bits_prev %d > wanted_bits %d deltaIndex (-%d -%d) Index (%d %d)"
+ "<-<<< JPEGEncoderRateController >>>-> %s: presentationTimeStamp_curr.value %lld presentationTimeStamp_curr.timescale %d"
+ "<-<<< JPEGEncoderRateController >>>-> %s: presentationTimeStamp_prev.value %lld presentationTimeStamp_prev.timescale %d"
+ "<-<<< JPEGVTEncoder >>>->"
+ "<-<<< JPEGVTEncoder >>>-> %s: Could not open connection to jpeg driver"
+ "<-<<< JPEGVTEncoder >>>-> %s: Emit Frame %d Start"
+ "<-<<< JPEGVTEncoder >>>-> %s: Emit Frame %d Stop"
+ "<-<<< JPEGVTEncoder >>>-> %s: Encode Result: %d, time: %.1f ms, surface size: %d, quality: %d (%d)"
+ "<-<<< JPEGVTEncoder >>>-> %s: Frame %d"
+ "<-<<< JPEGVTEncoder >>>-> %s: Frame %d Finish Encode"
+ "<-<<< JPEGVTEncoder >>>-> %s: Frame %d Finish Preproc"
+ "<-<<< JPEGVTEncoder >>>-> %s: Frame %d Start Encode"
+ "<-<<< JPEGVTEncoder >>>-> %s: Frame %d Start Preproc"
+ "<-<<< JPEGVTEncoder >>>-> %s: Input pixelBuffer is not IOSurface backed"
+ "<-<<< JPEGVTEncoder >>>-> %s: Waiting for previous frame to finish encoding to ensure in-order emits..."
+ "<-<<< JPEGVTEncoder >>>-> %s: rate controller DISABLED"
+ "<-<<< JPEGVTEncoder >>>-> %s: rate controller enabled, max Mbps: %d, window size (frames): %d"
+ "<-<<< JPEGVTEncoder >>>-> Fig"
+ "CFDictionaryCreate failed"
+ "CFDictionaryCreate failed (once)"
+ "FigDerivedObjectCreate failed"
+ "H1JPEGEncoder_CheckExistence"
+ "H1JPEGEncoder_CopyProperty"
+ "H1JPEGEncoder_CopySupportedPropertyDictionary"
+ "H1JPEGEncoder_CreateInstance"
+ "H1JPEGEncoder_EncodeFrame"
+ "H1JPEGEncoder_SetProperty"
+ "H1JPEGEncoder_StartSession"
+ "JPEGH1Encoder.c"
+ "bad quality"
+ "bad quality value"
+ "err"
+ "failed to obtain encodedBuffer struct"
+ "hardware jpeg encode failed"
+ "ioErr"
+ "jpegEncoder_createSupportedPropertyDictionary"
+ "jpeg_emitEncodedFrame"
+ "jpeg_encodeFrameAsyncInternal"
+ "jpeg_encodeFrameSync"
+ "jpeg_encoder_rc_trace"
+ "jpeg_vtencoder_trace"
+ "kVTAllocationFailedErr"
+ "kVTParameterErr"
+ "kVTPropertyNotSupportedErr"
+ "openJPEGDriverUserClientConnection"
+ "stevenote_accumulate"
+ "stevenote_rc_init"
+ "stevenote_rc_update_index"
+ "unrecognised property key"

```
