## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

-898.2.0.0.0
-  __TEXT.__text: 0x12902c
+899.3.0.0.0
+  __TEXT.__text: 0x1293ac
   __TEXT.__auth_stubs: 0xe90
-  __TEXT.__const: 0xbe4f
+  __TEXT.__const: 0xbe5f
   __TEXT.__gcc_except_tab: 0x7a4
-  __TEXT.__oslogstring: 0xfd66
-  __TEXT.__cstring: 0x5a35
-  __TEXT.__unwind_info: 0x16b0
-  __DATA_CONST.__got: 0x348
+  __TEXT.__oslogstring: 0xfed1
+  __TEXT.__cstring: 0x5a6f
+  __TEXT.__unwind_info: 0x16b8
+  __DATA_CONST.__got: 0x350
   __DATA_CONST.__const: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x750
   __AUTH_CONST.__const: 0x3d40
-  __AUTH_CONST.__cfstring: 0x6e0
+  __AUTH_CONST.__cfstring: 0x720
   __DATA.__common: 0x38
   __DATA_DIRTY.__data: 0x78
   __DATA_DIRTY.__bss: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 57F779D4-0E45-36C8-A3E9-B72BDF8B6A27
-  Functions: 1981
-  Symbols:   4873
-  CStrings:  1967
+  UUID: D96073A1-94C4-3D3C-BA0D-3A8F694AE7BA
+  Functions: 1982
+  Symbols:   4876
+  CStrings:  1976
 
Symbols:
+ GCC_except_table12
+ __ZN15CAVDHevcDecoder23setHevcVideoParsingModeEv
+ _kIOSurfaceAcceleratorDefaultChromaDownsample
- GCC_except_table11
CStrings:
+ "20:51:15"
+ "20:51:16"
+ "AVD_EnableMultiVPParsing"
+ "AppleAVD: %s(): ERROR setting kAppleAVDSetMultiVPParsing failed"
+ "AppleAVD: CAVDAvcDecoder::DecodeGetRenderTargetRef rvra scaler backup buffers are not allocated!"
+ "AppleAVD: CAVDHevcDecoder::DecodeGetRenderTargetRef rvra scaler backup buffers are not allocated!"
+ "AppleAVD: ERROR: kVASetMultiVPParsing error: %d \n"
+ "AppleAVD: cfg3: %d %d %d %d %d %d %d %d %d %d"
+ "AppleAVD: linear_orig or linear_scaled is NULL\n"
+ "Jun 18 2025"
+ "support_mvhevcwithalpha_decoding"
- "19:40:35"
- "19:40:36"
- "AppleAVD: cfg3: %d %d %d %d %d %d %d %d"
- "May 30 2025"

```
