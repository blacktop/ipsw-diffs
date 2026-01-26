## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

-906.0.0.0.0
-  __TEXT.__text: 0x153b08
-  __TEXT.__auth_stubs: 0xea0
+908.0.0.0.0
+  __TEXT.__text: 0x153268
+  __TEXT.__auth_stubs: 0xe80
   __TEXT.__const: 0xc153
   __TEXT.__gcc_except_tab: 0x8bc
-  __TEXT.__oslogstring: 0x1035b
-  __TEXT.__cstring: 0x5bef
-  __TEXT.__unwind_info: 0x1990
-  __DATA_CONST.__got: 0x350
+  __TEXT.__oslogstring: 0x101fa
+  __TEXT.__cstring: 0x5ba9
+  __TEXT.__unwind_info: 0x1980
+  __DATA_CONST.__got: 0x338
   __DATA_CONST.__const: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x758
+  __AUTH_CONST.__auth_got: 0x748
   __AUTH_CONST.__const: 0x4800
-  __AUTH_CONST.__cfstring: 0x720
+  __AUTH_CONST.__cfstring: 0x700
   __DATA.__common: 0x30
   __DATA_DIRTY.__data: 0x78
   __DATA_DIRTY.__bss: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: FDE64D9D-BAC1-3A5F-AB18-ADB5626ADD09
+  UUID: 82B8CA2C-FB17-34D0-B4ED-11160CEF60DF
   Functions: 2245
-  Symbols:   5511
-  CStrings:  1992
+  Symbols:   5506
+  CStrings:  1981
 
Symbols:
- _IOSurfaceCreate
- _IOSurfaceGetCacheMode
- _kIOSurfaceAllocSize
- _kIOSurfaceCacheMode
- _kIOSurfacePixelFormat
Functions:
~ __Z27AppleAVDDecodeFrameResponsePvijiii : 1592 -> 1556
~ __Z23AppleAVDDisplayCallbackP22_sAppleAVDVideoContextjjj10RvraParams16DecProfileParamsjijjj : 5536 -> 5420
~ _AppleAVDInitializeDecoder : 1136 -> 1140
~ _AppleAVDDecodeFrame : 5392 -> 4296
~ __ZN22AppleAVDCommandBuilder36decodeFrameFigHelper_VASetParametersEP26_sAppleAVDDecodeFrameFigIn : 1572 -> 1492
~ __ZN22AppleAVDCommandBuilder14decodeFrameFigEP26_sAppleAVDDecodeFrameFigInP27_sAppleAVDDecodeFrameFigOut : 4548 -> 4572
~ __ZN15CAVDHevcDecoder11VASetParamsEjPj : 1396 -> 1132
~ sub_297ef1f94 -> sub_2993cb978 : 196 -> 192
~ sub_297ef2058 -> sub_2993cba38 : 196 -> 192
~ __ZN14CAVDAvxDecoder11VASetParamsEjPj : 1020 -> 812
~ __ZN14CAVDLghDecoder11VASetParamsEjPj : 928 -> 720
~ __ZN14CAVDAvcDecoder11VAGetParamsEjPj : 1424 -> 1232
~ __ZN14CAVDAvcDecoder11VASetParamsEjPj : 1056 -> 1028
CStrings:
+ "21:28:35"
+ "AppleAVD: ERROR: AVC decoder kVAGetVRAHDRBuff tag unsupported!"
+ "AppleAVD: ERROR: AVC decoder kVASetVRAHDRBuff tag unsupported!"
+ "AppleAVD: ERROR: Failed to set parameter kVASetVRATypeAndDimensions - status %d"
+ "AppleAVD: ERROR: HEVC decoder kVASetVRAHDRBuff tag unsupported for USP!"
+ "AppleAVD: ERROR: Invalid VRA Dimensions - w:%d h:%d"
+ "AppleAVD: ERROR: createDecoder() error creating rvra buffers!"
+ "Jan 22 2026"
- "20:10:18"
- "20:10:19"
- "AVD video decoder RVRA"
- "AppleAVD: %s(): ERROR! Failed to set parameter kVASetEnableRVRA - status %d"
- "AppleAVD: %s(): ERROR! Failed to set parameter kVASetVRATypeAndDimensions - status %d"
- "AppleAVD: %s(): ERROR! Invalid VRA Dimensions - w:%d h:%d"
- "AppleAVD: %s(): chromaFilterHdrBuff is not allocated! \n"
- "AppleAVD: AppleAVD_VideoDecoder - ERROR IOSurfaceCreate failed\n"
- "AppleAVD: AppleAVD_VideoDecoder - ERROR IOSurfaceLock failed\n"
- "AppleAVD: ERROR: %s(): Create RVRA HDR buffer Failed"
- "AppleAVD: ERROR: %s(): RVRA HDR buffer map failed: %d \n"
- "AppleAVD: ERROR: %s(): chromaFilterHdrBuffAllocated is false!\n"
- "AppleAVD: ERROR: %s: Incorrect Cache Mode=%d\n"
- "AppleAVD: ERROR: m_dec_hdr_c_size:%d > size of rvra header buffer:%d "
- "AppleAVD: createDecoder() error creating rvra buffers!"
- "CreateCompressedBitBuffer"
- "Jan  5 2026"
- "VASetParams"

```
