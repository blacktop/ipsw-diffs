## AppleProResHWEncoder.videoencoder

> `/System/Library/VideoEncoders/AppleProResHWEncoder.videoencoder`

```diff

 600.53.0.0.0
-  __TEXT.__text: 0x203c4
+  __TEXT.__text: 0x204b0
   __TEXT.__const: 0x746f0
   __TEXT.__gcc_except_tab: 0x310
-  __TEXT.__cstring: 0x1491
+  __TEXT.__cstring: 0x14ac
   __TEXT.__oslogstring: 0x4140
   __TEXT.__unwind_info: 0x440
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libc++.1.dylib
   Functions: 496
   Symbols:   593
-  CStrings:  414
+  CStrings:  417
 
Functions:
~ __Z26interchange_compress_planePKvPhS1_jjjbj : 1440 -> 1456
~ __Z28interchange_decompress_planePKhS0_Pvjjjbj : 1512 -> 1516
~ __ZN23interchange_compression12decompressor10decompressEPKhjRA4_A8_A4_j : 4048 -> 4088
~ __ZN23interchange_compression10compressor14compute_deltasEjRA4_A8_A4_Kjjj : 1020 -> 1024
~ __ZN23interchange_compression10compressor11pack_pixelsERA4_A8_A4_KjjjPhRjS7_ : 668 -> 676
~ __ZN23interchange_compression12decompressor17decompress_pixelsEPKhjR8bit_packRA4_A8_A4_j : 1856 -> 1896
~ __ZN23interchange_compression12decompressor11decorrelateERA4_A8_A4_j : 304 -> 312
~ __Z32checkPlatformForProResRAWSupportv : 192 -> 252
~ __Z11decodeSlicePhP11ProResFrameP13ProResPictureiih : 1964 -> 1980
~ __ZL16GetFrameRateCodedjd : 156 -> 160
~ __Z16alphaScalingTaskPv : 348 -> 352
~ __ZN19ProResFrameReceiver21PerformAlphaUpscalingEP10__CVBufferPK8S_ImgFmt : 880 -> 884
~ __ZN19ProResFrameReceiver20QueueOutOfOrderFrameEP15ProResFrameInfoPvjbi : 236 -> 240
~ __ZN19ProResFrameReceiver14P2PrepareFrameEP16DoubleEncodeInfoP15ProResFrameInfoP14QpmAndEstStatsPhRm : 504 -> 512
~ __ZN19ProResFrameReceiver26CopyBitstreamToBlockBufferEP15ProResFrameInfoP19BitstreamBufferInfoPhjb : 1164 -> 1172
~ __ZNSt3__114__split_bufferIPPvNS_9allocatorIS2_EEE12emplace_backIJS2_EEEvDpOT_ : 264 -> 268
~ __ZNSt3__114__split_bufferIPPvRNS_9allocatorIS2_EEE12emplace_backIJS2_EEEvDpOT_ : 264 -> 268
CStrings:
+ "ApertureDiameter"
+ "V63"
+ "V64"
+ "V64s"
- "AD"
```
