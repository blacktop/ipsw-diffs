## JPEGH1.videodecoder

> `/System/Library/VideoDecoders/JPEGH1.videodecoder`

```diff

-3320.8.1.1.0
-  __TEXT.__text: 0x2e44 sha256:741082c958a0808b5bf14f94c1968a3c213dc4ff2adf18c9fc82a5f0cfb76f59
-  __TEXT.__auth_stubs: 0x6d0 sha256:558c625f0a6c5965da1844a751a39c5a1a1fff26b82455a6adc3757fe867add1
-  __TEXT.__const: 0x34 sha256:d6eb1db4dd2f9b565a3b3069842a8e1acaf8f209e12fe622c8ac81e8232c79bd
-  __TEXT.__cstring: 0xe7 sha256:9234142216fba999f0962738b5271a0fef74f0c0137fefc701646d48ca7c9a9d
-  __TEXT.__unwind_info: 0xd0 sha256:4b699a94c7a9c987860f74d900bba7cd25eafa0c72e036397204d62c78fd31a3
-  __DATA_CONST.__got: 0x150 sha256:52a3e0804d93dc525ec3c67ef8ac5b01756ecf0513e36f3c19435e4c82cb5d29
-  __DATA_CONST.__const: 0x40 sha256:7a01c0c5cc0922feadb3b9a872df01943f5cc008977085fc1df4d19bd51ec26c
-  __AUTH_CONST.__auth_got: 0x368 sha256:232885aa9953d5c0890072e5589e9265c9a06f8354cb7403cde80d604c526f09
-  __AUTH_CONST.__const: 0xd8 sha256:54501b356394259d672d1bd3c3c268f40a90985ad3bfb5fc1a3b8ef6e970d625
-  __AUTH_CONST.__cfstring: 0x60 sha256:cfce061f874a857e873cbc4740b8f2990bcdb6cc79ce063836da5afb7c0f1abc
+3350.58.3.11.1
+  __TEXT.__text: 0x4378 sha256:7425e125afab8d635ca9ced0ad7ef1b9515d34345ce745b144393782bf5e773f
+  __TEXT.__const: 0x54 sha256:5c81a181ea102c0e1c81fb32d7ed40ddb0a2338c6350cab1d4793cf316a9a938
+  __TEXT.__cstring: 0x67c sha256:84a7b074573bb152d7b9178b8912ab312bb29d2ed466ab80bf3111af25a5a896
+  __TEXT.__oslogstring: 0x630 sha256:7efbf1d0b59f60f16243d62fb8d236a133b1e1ec11d0060c4af221e15f4cf76e
+  __TEXT.__unwind_info: 0xd8 sha256:59f3e4816027bb7ae0c7760b523d4ae8da00c6b174cf9c36553dddf3c1044812
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x40 sha256:2377d553391b6b7a4da40395b278cf92ed2e9578e77d51026240b2dc35677f72
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0xd8 sha256:a12aa96b2b814448a0c9555c7b985bde0854c5e7af23af5f45d17a8315ac4c98
+  __AUTH_CONST.__cfstring: 0xa0 sha256:7a914cfecaa07dc0efc36afefe4485f9d5c394636c6c92af7e3e30ef192c82f9
+  __AUTH_CONST.__auth_got: 0x390 sha256:d2710a3a6574fc3d509a62191d8933226f0046f7ffcd83fd8de6866684c5f73e
   __DATA.__bss: 0x48 sha256:834a709ba2534ebe3ee1397fd4f7bd288b2acc1d20a08d6c862dcd99b6f04400
   __DATA_DIRTY.__data: 0x30 sha256:6a02f10fd9678c104f33dcbf52d942dfe9b4abd1856577ecf3d97a16b8863b6d
+  __DATA_DIRTY.__common: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   __DATA_DIRTY.__bss: 0x28 sha256:2c34ce1df23b838c5abf2a7f6437cca3d3067ed509ff25f11df6b11b582b51eb
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /usr/lib/libSystem.B.dylib
-  UUID: 7C429EE6-E085-39AD-B600-4173C0022DAB
-  Functions: 41
-  Symbols:   248
-  CStrings:  14
+  UUID: 37D689A8-AC6C-37BF-A3CB-6716A08C330B
+  Functions: 58
+  Symbols:   288
+  CStrings:  82
 
Symbols:
+ _FigHostTimeToNanoseconds
+ _FigSignalErrorAt3
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ ___block_descriptor_tmp.47
+ ___jpeg_DecodeFrameSynchronously_block_invoke.cold.1
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _gFigJPEGVTDecoderTrace
+ _os_log_type_enabled
- _FigSignalErrorAtGM
- ___block_descriptor_tmp.14
- _fig_log_get_emitter
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
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
- "%s signalled err=%d at <>:%d"

```
