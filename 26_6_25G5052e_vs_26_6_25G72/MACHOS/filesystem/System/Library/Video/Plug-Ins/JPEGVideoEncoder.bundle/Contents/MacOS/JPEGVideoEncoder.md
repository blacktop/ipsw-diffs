## JPEGVideoEncoder

> `/System/Library/Video/Plug-Ins/JPEGVideoEncoder.bundle/Contents/MacOS/JPEGVideoEncoder`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`

```diff

-3330.10.1.0.0
-  __TEXT.__text: 0x36e8
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x505
-  __TEXT.__oslogstring: 0x5a8
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x300
+3330.13.2.0.0
+  __TEXT.__text: 0x21dc
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__const: 0x10
+  __TEXT.__cstring: 0x10c
+  __TEXT.__unwind_info: 0xc0
+  __DATA_CONST.__auth_got: 0x2d0
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x208
-  __DATA_CONST.__cfstring: 0x100
+  __DATA_CONST.__cfstring: 0xc0
   __DATA.__data: 0x20
-  __DATA.__common: 0x20
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia

   - /System/Library/Frameworks/VideoToolbox.framework/Versions/A/VideoToolbox
   - /usr/lib/libSystem.B.dylib
   Functions: 28
-  Symbols:   135
-  CStrings:  64
+  Symbols:   129
+  CStrings:  12
 
Symbols:
+ _FigSignalErrorAtGM
+ _fig_log_get_emitter
- _FigGetUpTime
- _FigHostTimeToNanoseconds
- _FigSignalErrorAt3
- __os_log_send_and_compose_impl
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _fig_note_initialize_category_with_default_work_cf
- _os_log_type_enabled
Functions:
~ _H1JPEGEncoder_CheckExistence : 160 -> 148
~ _H1JPEGEncoder_CreateInstance : 848 -> 508
~ sub_ed4 -> sub_cd4 : 200 -> 192
~ sub_f9c -> sub_d94 : 400 -> 388
~ sub_1130 -> sub_f1c : 2084 -> 1652
~ sub_1954 -> sub_1590 : 944 -> 460
~ sub_1d4c -> sub_17a4 : 188 -> 176
~ sub_1ee8 -> sub_1934 : 2032 -> 1380
~ sub_26d8 -> sub_1e98 : 1548 -> 640
~ sub_2ce4 -> sub_2118 : 968 -> 252
~ sub_30b0 -> sub_2218 : 476 -> 428
~ sub_328c -> sub_23c4 : 496 -> 140
~ sub_34c0 -> sub_2494 : 792 -> 140
~ sub_37d8 -> sub_2520 : 996 -> 268
~ sub_3fa0 -> sub_2a10 : 136 -> 108
CStrings:
+ "%s signalled err=%d at <>:%d"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LDgQDU/Sources/CoreMedia_VideoToolbox/Sources/JPEGH1Codec/JPEGH1Encoder.c"
- "<-<<< JPEGEncoderRateController >>>-> %s: Init Index %d, bitrate %d"
- "<-<<< JPEGEncoderRateController >>>-> %s: frame_bits %d framerate %d"
- "<-<<< JPEGEncoderRateController >>>-> %s: frame_bits_prev %d < wanted_bits %d deltaIndex (+%d +%d) Index (%d %d)"
- "<-<<< JPEGEncoderRateController >>>-> %s: frame_bits_prev %d > wanted_bits %d deltaIndex (-%d -%d) Index (%d %d)"
- "<-<<< JPEGEncoderRateController >>>-> %s: presentationTimeStamp_curr.value %lld presentationTimeStamp_curr.timescale %d"
- "<-<<< JPEGEncoderRateController >>>-> %s: presentationTimeStamp_prev.value %lld presentationTimeStamp_prev.timescale %d"
- "<-<<< JPEGVTEncoder >>>-> %s: Could not open connection to jpeg driver"
- "<-<<< JPEGVTEncoder >>>-> %s: Emit Frame %d Start"
- "<-<<< JPEGVTEncoder >>>-> %s: Emit Frame %d Stop"
- "<-<<< JPEGVTEncoder >>>-> %s: Encode Result: %d, time: %.1f ms, surface size: %d, quality: %d (%d)"
- "<-<<< JPEGVTEncoder >>>-> %s: Frame %d"
- "<-<<< JPEGVTEncoder >>>-> %s: Frame %d Finish Encode"
- "<-<<< JPEGVTEncoder >>>-> %s: Frame %d Finish Preproc"
- "<-<<< JPEGVTEncoder >>>-> %s: Frame %d Start Encode"
- "<-<<< JPEGVTEncoder >>>-> %s: Frame %d Start Preproc"
- "<-<<< JPEGVTEncoder >>>-> %s: Input pixelBuffer is not IOSurface backed"
- "<-<<< JPEGVTEncoder >>>-> %s: Waiting for previous frame to finish encoding to ensure in-order emits..."
- "<-<<< JPEGVTEncoder >>>-> %s: rate controller DISABLED"
- "<-<<< JPEGVTEncoder >>>-> %s: rate controller enabled, max Mbps: %d, window size (frames): %d"
- "<-<<< JPEGVTEncoder >>>-> Fig"
- "CFDictionaryCreate failed"
- "CFDictionaryCreate failed (once)"
- "FigDerivedObjectCreate failed"
- "H1JPEGEncoder_CheckExistence"
- "H1JPEGEncoder_CopyProperty"
- "H1JPEGEncoder_CopySupportedPropertyDictionary"
- "H1JPEGEncoder_CreateInstance"
- "H1JPEGEncoder_EncodeFrame"
- "H1JPEGEncoder_SetProperty"
- "H1JPEGEncoder_StartSession"
- "JPEGH1Encoder.c"
- "bad quality"
- "bad quality value"
- "err"
- "failed to obtain encodedBuffer struct"
- "hardware jpeg encode failed"
- "ioErr"
- "jpegEncoder_createSupportedPropertyDictionary"
- "jpeg_emitEncodedFrame"
- "jpeg_encodeFrameAsyncInternal"
- "jpeg_encodeFrameSync"
- "jpeg_encoder_rc_trace"
- "jpeg_vtencoder_trace"
- "kVTAllocationFailedErr"
- "kVTParameterErr"
- "kVTPropertyNotSupportedErr"
- "openJPEGDriverUserClientConnection"
- "stevenote_accumulate"
- "stevenote_rc_init"
- "stevenote_rc_update_index"
- "unrecognised property key"
```
