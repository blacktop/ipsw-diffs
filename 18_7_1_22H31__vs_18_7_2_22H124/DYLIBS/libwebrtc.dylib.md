## libwebrtc.dylib

> `/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib`

```diff

-621.4.1.10.1
-  __TEXT.__text: 0xa6b528
+621.5.1.10.7
+  __TEXT.__text: 0xa6b5d0
   __TEXT.__auth_stubs: 0x1560
   __TEXT.__objc_methlist: 0x14e4
   __TEXT.__const: 0xb3a98
-  __TEXT.__cstring: 0x4bccd
+  __TEXT.__cstring: 0x4bce6
   __TEXT.__gcc_except_tab: 0x1864
   __TEXT.__unwind_info: 0x35f8
   __TEXT.__eh_frame: 0x1118

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B965E542-8667-3BA3-9FB2-AA661216BBD6
-  Functions: 18026
-  Symbols:   43555
-  CStrings:  9558
+  UUID: 423362B8-05F5-3890-9C9B-F23CC1E43AA0
+  Functions: 18030
+  Symbols:   43569
+  CStrings:  9559
 
Symbols:
+ _Convert8To16Plane
+ _Convert8To16Row_Any_NEON
+ _Convert8To16Row_C
+ _Convert8To16Row_NEON
+ __ZN6libyuvL14kMult38_Div664E
+ __ZN6libyuvL14kMult38_Div996E
+ __ZN6libyuvL29kScaleRowDown38_2_BoxIndices1E
+ __ZN6libyuvL29kScaleRowDown38_2_BoxIndices2E
+ __ZN6libyuvL29kScaleRowDown38_3_BoxIndices1E
+ __ZN6libyuvL29kScaleRowDown38_3_BoxIndices2E
+ __ZN6libyuvL29kScaleRowDown38_3_BoxIndices3E
+ __ZN6libyuvL29kScaleRowDown38_NarrowIndicesE
- __ZN6libyuvL12kMult38_Div6E
- __ZN6libyuvL12kMult38_Div9E
- __ZN6libyuvL9kShuf38_2E
Functions:
+ _Convert8To16Row_NEON
~ -[RTCVideoEncoderH264 encode:codecSpecificInfo:frameTypes:] : 2772 -> 2784
~ _ScaleRowDown38_NEON : 44 -> 68
~ _ScaleRowDown38_3_Box_NEON : 252 -> 200
~ _ScaleRowDown38_2_Box_NEON : 176 -> 156
~ _ScaleFilterCols_NEON : 344 -> 328
~ __ZN6webrtc20copyVideoFrameBufferERNS_16VideoFrameBufferEPh : 1712 -> 1724
~ __ZN6libyuvL10I4xxToI420EPKhiS1_iS1_iPhiS2_iS2_iiiii : 384 -> 376
~ _I400ToI420 : 232 -> 260
~ _NV12ToI420 : 340 -> 372
~ _RGB565ToI420 : 540 -> 604
~ _ARGB1555ToI420 : 604 -> 592
~ _ARGB4444ToI420 : 604 -> 592
~ _I420ToI010 : 1428 -> 320
~ _I420ToNV12 : 268 -> 292
~ _AArch64CpuCaps : 212 -> 268
+ _Convert8To16Plane
~ _MergeUVRow_Any_NEON : 328 -> 324
~ _MergeUVRow_16_Any_NEON : 336 -> 332
~ _ARGBToYRow_Any_NEON : 348 -> 344
~ _BGRAToYRow_Any_NEON : 348 -> 344
~ _ABGRToYRow_Any_NEON : 348 -> 344
~ _RGBAToYRow_Any_NEON : 348 -> 344
~ _RGB24ToYRow_Any_NEON : 360 -> 356
~ _RAWToYRow_Any_NEON : 360 -> 356
~ _RGB565ToYRow_Any_NEON : 412 -> 408
~ _ARGB1555ToYRow_Any_NEON : 412 -> 408
~ _ARGB4444ToYRow_Any_NEON : 396 -> 392
~ _YUY2ToYRow_Any_NEON : 244 -> 240
~ _UYVYToYRow_Any_NEON : 244 -> 240
+ _MultiplyRow_16_Any_NEON
~ _RGB24ToUVRow_Any_NEON : 608 -> 612
~ _RAWToUVRow_Any_NEON : 608 -> 612
~ _ARGBToUVRow_C : 348 -> 356
~ _BGRAToUVRow_C : 348 -> 356
~ _ABGRToUVRow_C : 348 -> 356
~ _RGBAToUVRow_C : 348 -> 356
~ _RGB24ToUVRow_C : 348 -> 356
~ _RAWToUVRow_C : 348 -> 356
~ _RGB565ToUVRow_C : 1476 -> 1564
~ _ARGB1555ToUVRow_C : 1496 -> 1560
~ _ARGB4444ToUVRow_C : 1372 -> 1508
+ _Convert8To16Row_C
~ _ScaleRowDown38_Any_NEON : 756 -> 780
~ _ScaleRowDown38_3_Box_Any_NEON : 340 -> 296
~ _ScaleRowDown38_2_Box_Any_NEON : 456 -> 432
~ _ScaleFilterCols_Any_NEON : 744 -> 736
CStrings:
+ "hw.optional.arm.FEAT_SME"

```
