## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

-796.1.0.0.0
-  __TEXT.__text: 0x114464
+798.1.0.0.0
+  __TEXT.__text: 0x1146ec
   __TEXT.__auth_stubs: 0xed0
   __TEXT.__const: 0xbb7b
-  __TEXT.__oslogstring: 0xeeaa
-  __TEXT.__cstring: 0x5aee
+  __TEXT.__oslogstring: 0xeeb3
+  __TEXT.__cstring: 0x5afc
   __TEXT.__gcc_except_tab: 0xb44
   __TEXT.__unwind_info: 0x18e0
-  __DATA_CONST.__got: 0x328
+  __DATA_CONST.__got: 0x338
   __DATA_CONST.__const: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x770

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 2075
-  Symbols:   2515
+  Functions: 2076
+  Symbols:   2518
   CStrings:  1853
 
Symbols:
+ _kVTDecompressionPropertyKey_AllowBitstreamToChangeFrameDimensions
+ _kVTDecompressionPropertyKey_UsingHardwareAcceleratedVideoDecoder
CStrings:
+ "21:28:19"
+ "21:28:20"
+ "21:28:21"
+ "AVD_AllowBitstreamToChangeFrameDimensions"
+ "AppleAVD: %!s(MISSING)(): ERROR setting kAppleAVDSetAllowBitstreamToChangeFrameDimensions failed"
+ "Aug  5 2024"
+ "virtual int CAVDAvcDecoder::VADecodeFrame(unsigned char *, int, uint32_t, int, int, int, avd_seq_params *)"
+ "virtual int CAVDAvxDecoder::VADecodeFrame(unsigned char *, int, uint32_t, int, int, int, avd_seq_params *)"
+ "virtual int CAVDHevcDecoder::VADecodeFrame(unsigned char *, int, uint32_t, int, int, int, avd_seq_params *)"
+ "virtual int CAVDLghDecoder::VADecodeFrame(unsigned char *, int, uint32_t, int, int, int, avd_seq_params *)"
+ "virtual int CAVDMvHevcDecoder::VADecodeFrame(unsigned char *, int, uint32_t, int, int, int, avd_seq_params *)"
- "21:15:40"
- "21:15:41"
- "AVD_EnableReducedDimensionOutput"
- "AppleAVD: %!s(MISSING)(): ERROR setting kAppleAVDSetEnableReducedDimensionOutput failed"
- "EnableUSPForLegacyDRMSchemes"
- "Jul 15 2024"
- "virtual int CAVDAvcDecoder::VADecodeFrame(unsigned char *, int, int, int, int, int, avd_seq_params *)"
- "virtual int CAVDAvxDecoder::VADecodeFrame(unsigned char *, int, int, int, int, int, avd_seq_params *)"
- "virtual int CAVDHevcDecoder::VADecodeFrame(unsigned char *, int, int, int, int, int, avd_seq_params *)"
- "virtual int CAVDLghDecoder::VADecodeFrame(unsigned char *, int, int, int, int, int, avd_seq_params *)"
- "virtual int CAVDMvHevcDecoder::VADecodeFrame(unsigned char *, int, int, int, int, int, avd_seq_params *)"

```
