## JPEGH1.videoencoder

> `/System/Library/VideoEncoders/JPEGH1.videoencoder`

```diff

-3255.79.1.8.0
-  __TEXT.__text: 0x21fc
-  __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x10c
-  __TEXT.__unwind_info: 0xc0
+3285.5.1.11.1
+  __TEXT.__text: 0x3708
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__const: 0x40
+  __TEXT.__cstring: 0x4a0
+  __TEXT.__oslogstring: 0x5a8
+  __TEXT.__unwind_info: 0xc8
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x80
-  __AUTH_CONST.__auth_got: 0x2d0
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
-  UUID: 51379AF0-8B31-374A-B778-8314B6F5B2B1
+  UUID: 6DB660BC-3D9A-32DD-9B4B-BE06FD80FDCF
   Functions: 28
-  Symbols:   194
-  CStrings:  18
+  Symbols:   202
+  CStrings:  72
 
Symbols:
+ _FigGetUpTime
+ _FigHostTimeToNanoseconds
+ _FigSignalErrorAt3
+ ___block_descriptor_tmp.36
+ ___block_descriptor_tmp.41
+ ___block_literal_global.43
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _gFigJPEGEncoderRateController
+ _gFigJPEGVTEncoderTrace
+ _os_log_type_enabled
- _FigSignalErrorAtGM
- ___block_descriptor_tmp.23
- ___block_descriptor_tmp.8
- ___block_literal_global.10
- _fig_log_get_emitter
Functions:
~ _H1JPEGEncoder_CheckExistence : 148 -> 160
~ _H1JPEGEncoder_CreateInstance : 508 -> 848
~ _H1JPEGEncoder_CopyProperty : 192 -> 200
~ _H1JPEGEncoder_SetProperty : 388 -> 400
~ _H1JPEGEncoder_StartSession : 1652 -> 2084
~ _H1JPEGEncoder_EncodeFrame : 460 -> 944
~ _H1JPEGEncoder_CopySupportedPropertyDictionary : 176 -> 188
~ _jpeg_encodeFrameSync : 1380 -> 2032
~ ___jpeg_encodeFrameAsync_block_invoke : 672 -> 1580
~ _jpeg_emitEncodedFrame : 252 -> 968
~ _jpegEncoder_createSupportedPropertyDictionary : 428 -> 476
~ _JPEGRCMake : 140 -> 496
~ _JPEGRCGetEncodingQuality : 140 -> 792
~ _JPEGRCUpdate : 268 -> 996
~ ___jpeg_encodeFrameAsync_block_invoke.cold.1 : 108 -> 136
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_VideoToolbox/Sources/JPEGH1Codec/JPEGH1Encoder.c"
+ "<-<<< JPEGEncoderRateController >>>-> %s: Init Index %d, bitrate %d"
+ "<-<<< JPEGEncoderRateController >>>-> %s: frame_bits %d framerate %d"
+ "<-<<< JPEGEncoderRateController >>>-> %s: frame_bits_prev %d < wanted_bits %d deltaIndex (+%d +%d) Index (%d %d)"
+ "<-<<< JPEGEncoderRateController >>>-> %s: frame_bits_prev %d > wanted_bits %d deltaIndex (-%d -%d) Index (%d %d)"
+ "<-<<< JPEGEncoderRateController >>>-> %s: presentationTimeStamp_curr.value %lld presentationTimeStamp_curr.timescale %d"
+ "<-<<< JPEGEncoderRateController >>>-> %s: presentationTimeStamp_prev.value %lld presentationTimeStamp_prev.timescale %d"
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
- "%s signalled err=%d at <>:%d"

```
