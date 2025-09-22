## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

-904.2.0.0.0
-  __TEXT.__text: 0x1403dc
+905.0.0.0.0
+  __TEXT.__text: 0x13ffc8
   __TEXT.__auth_stubs: 0xea0
   __TEXT.__const: 0xbfe3
   __TEXT.__gcc_except_tab: 0x830
-  __TEXT.__oslogstring: 0x1049b
-  __TEXT.__cstring: 0x5b6c
+  __TEXT.__oslogstring: 0x103a4
+  __TEXT.__cstring: 0x5b53
   __TEXT.__unwind_info: 0x1840
   __DATA_CONST.__got: 0x350
   __DATA_CONST.__const: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x758
   __AUTH_CONST.__const: 0x42a0
-  __AUTH_CONST.__cfstring: 0x740
+  __AUTH_CONST.__cfstring: 0x720
   __DATA.__common: 0x38
   __DATA_DIRTY.__data: 0x78
   __DATA_DIRTY.__bss: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 66A15DE9-CF6B-3D28-ACCB-773A2A9780EC
-  Functions: 2116
-  Symbols:   5198
-  CStrings:  1998
+  UUID: 7BA5566F-49B4-35B4-B406-E621D46D3F90
+  Functions: 2115
+  Symbols:   5196
+  CStrings:  1993
 
Symbols:
- _AppleAVDWrapperFghrnDecoderCleanUpMVAV1Resources
Functions:
~ __Z23AppleAVDDisplayCallbackP22_sAppleAVDVideoContextjjj10RvraParams16DecProfileParamsjijjj : 5560 -> 5536
~ _DisplayCallBack : 268 -> 228
~ __ZN15CAVDHevcDecoder11VAGetParamsEjPj : 1352 -> 1372
~ __ZN14CAVDAvxDecoder13VADecodeFrameEPhijiiiP14avd_seq_params : 4728 -> 4708
~ _AppleAVDWrapperFghrnDecoderCreateInstance : 640 -> 628
~ _Fghrn_createSupportedPropertyDictionary : 924 -> 916
~ _AppleAVDWrapperFghrnDecoderCopyProperty : 1008 -> 976
~ _AppleAVDWrapperFghrnDecoderSetProperty : 1796 -> 1396
~ _AppleAVDWrapperFghrnDecoderCleanUp : 416 -> 408
- _AppleAVDWrapperFghrnDecoderCleanUpMVAV1Resources
~ _AppleAVDWrapperFghrnDecoderStartSession : 3636 -> 3456
~ _AppleAVDWrapperFghrnDecoderDecodeFrame : 5068 -> 4704
~ _AppleAVDWrapperFghrnDecoderDecodeTile : 2308 -> 2272
~ _CreateAVDFghrnInstance : 2280 -> 2188
~ _AppleAVDWrapperHEVCDecoderCanAcceptFormatDescription : 588 -> 872
CStrings:
+ "20:27:09"
+ "20:27:10"
+ "AppleAVD: %s(): **mismatch** w %d h %d cf %d ybd %d cbd %d nSz %d DpbSz %d vRange %u **new** w %d h %d cf %d ybd %d cbd %d nSz %d DpbSz %d vRange %u"
+ "Sep 16 2025"
- "20:23:28"
- "20:23:29"
- "AppleAVD: %s - kVTDecompressionPropertyKey_RequestedMVAV1SpatialVideoLayerIDs error"
- "AppleAVD: AppleAVD_FghrnDecoder - AppleAVDSetParameter kAppleAVDSetTaggedBufGroupArray returned ERROR"
- "AppleAVD: ERROR: %s() - AppleAVDSetParameter call for kAppleAVDSetMVAV1DisplayLayerIDs returned ERROR\n"
- "AppleAVD: WARNING: %s() - trying to set kAppleAVDSetMVAV1DisplayLayerIDs before videoContext was created!\n"
- "Aug 26 2025"
- "RequestedMVAV1SpatialIDs"

```
