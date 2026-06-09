## JPEGH1.videoencoder

> `/System/Library/VideoEncoders/JPEGH1.videoencoder`

```diff

-3320.8.1.1.0
-  __TEXT.__text: 0x21dc sha256:811f9bf892127ca085ddbfade9dcad1378c1561fcbd1b33d2c727995973bf436
-  __TEXT.__auth_stubs: 0x5a0 sha256:d4c402ef88446c5e7e9db2f2c150fac465c77e13df6ba6e2a9bd9f14ad4f67e5
-  __TEXT.__const: 0x10 sha256:5007724b823bb4760349887708e8d827ac788feed704a37544eeb3b17bb3547c
-  __TEXT.__cstring: 0x10c sha256:127b664d6de92fc28db8d513dc0fe98e143b940b85ca7b3f8e0fb9ae66411d4d
-  __TEXT.__unwind_info: 0xc0 sha256:e48ee4a3ba8a0da30c54ca31806eb81024f3e3781e6bbc64cfe046941faa1754
-  __DATA_CONST.__got: 0x100 sha256:5341e6b2646979a70e57653007a1f310169421ec9bdd9f1a5648f75ade005af1
-  __DATA_CONST.__const: 0x80 sha256:cd5770ac9fa6b5462ebd2b52a8a8c2a928fd1d8fc1e91a810481f9e83f41c7f7
-  __AUTH_CONST.__auth_got: 0x2d0 sha256:fe2f74a1e0b16a66452888eb4d734bc455cf1304481bb495d59afa8cf9cae93b
-  __AUTH_CONST.__const: 0x188 sha256:e2d9fe430d0e265759114dc7e3dfc4e0bc5b26791903a4eb1ae59d32db8d9434
-  __AUTH_CONST.__cfstring: 0xc0 sha256:6a6b89f0a21bba20125e55c5396fff1dfa5c8220f094135db133c953bd2861bf
-  __DATA.__data: 0x20 sha256:fb26965c1023fc37cab69368459de78b7f4b4149f799a55c08dc9747f97200e6
+3350.58.3.11.1
+  __TEXT.__text: 0x36e8 sha256:6fbe0dc4f683b8ac95d59f66f6cba26a1490a01cfa625d29a6939f66b1e49e88
+  __TEXT.__const: 0x40 sha256:1414d57d472630cb25e5a7df989dc992dd62344bf0d6ca0b657c5c00b1c22a3a
+  __TEXT.__cstring: 0x4df sha256:ffe3c96ae76b1607016f32784d96efc777c69ffc1c1b8036468ff948f3a89015
+  __TEXT.__oslogstring: 0x5a8 sha256:a53c624848989614c63bfb0a0f4500c04b706973051b959b02a2e903ca88ac00
+  __TEXT.__unwind_info: 0xd8 sha256:927a88adc38e5a06b9300ef10bbdd09676a4664fe4bcbf4edba84be755b9fc69
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x80 sha256:413c7b21b53fff9941d0e3df04ce1cf590f5bac4787ba7f86720d1587ca0c4e6
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x188 sha256:159666383f7605ed186c00ab5c011536751f4e480a1438f6d0c675a8b85a101b
+  __AUTH_CONST.__cfstring: 0x100 sha256:ec3183538e0d12aeae978bd6f8b819a9bf51e79af65c65f0ddfbf6c0b4b2354f
+  __AUTH_CONST.__auth_got: 0x300 sha256:ef115a0e0c15cdc41958ca46b5b14b456115f4baec5e3ca68599d2a8f435e3b8
+  __DATA.__data: 0x20 sha256:260f1623400e8ef32fc27e671c1b6432e44d007cbde4944ff2968dc52e9a4274
+  __DATA.__common: 0x20 sha256:66687aadf862bd776c8fc18b8e9f8e20089714856ee233b3902a591d0d5f2925
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /usr/lib/libSystem.B.dylib
-  UUID: 9C274990-6A66-3A0D-9914-6D7A41B74286
-  Functions: 28
-  Symbols:   194
-  CStrings:  18
+  UUID: E8B4AC5F-8762-350D-8744-01D4344044AF
+  Functions: 42
+  Symbols:   229
+  CStrings:  72
 
Symbols:
+ _FigGetUpTime
+ _FigHostTimeToNanoseconds
+ _FigSignalErrorAt3
+ _H1JPEGEncoder_StartSession.cold.2
+ _H1JPEGEncoder_StartSession.cold.3
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ __MergedGlobals
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
- _H1JPEGEncoder_StartSession.sRateControllerMBitCap
- _H1JPEGEncoder_StartSession.sRateControllerWindowSizeFrames
- ___block_descriptor_tmp.23
- ___block_descriptor_tmp.8
- ___block_literal_global.10
- _fig_log_get_emitter
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMedia_VideoToolbox/Sources/JPEGH1Codec/JPEGH1Encoder.c"
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
