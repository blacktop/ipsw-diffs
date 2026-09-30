## vImage

> `/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vImage.framework/Versions/A/vImage`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-650.0.0.0.0
-  __TEXT.__text: 0x371f8c
+650.0.1.0.0
+  __TEXT.__text: 0x37b57c
   __TEXT.__delay_stubs: 0x780
   __TEXT.__delay_helper: 0x5a4
-  __TEXT.__const: 0x9a570
-  __TEXT.__cstring: 0x6be2
-  __TEXT.__unwind_info: 0x2538
-  __TEXT.__eh_frame: 0x341c
+  __TEXT.__const: 0x9a5b0
+  __TEXT.__cstring: 0x6be6
+  __TEXT.__unwind_info: 0x2670
+  __TEXT.__eh_frame: 0x38a4
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x23e0
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xcb08
+  __AUTH_CONST.__const: 0xcd08
   __AUTH_CONST.__auth_got: 0x328
   __DATA.__data: 0x50
   __DATA.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
-  Functions: 3356
-  Symbols:   4297
+  Functions: 3431
+  Symbols:   4373
   CStrings:  404
 
Symbols:
+ _rpad_axis_fill
+ _rpad_axis_max_taps
+ _rpad_axis_zones
+ _rpad_compute_interior_row
+ _rpad_core
+ _rpad_fused_1_1_0
+ _rpad_fused_1_1_1
+ _rpad_fused_1_2_0
+ _rpad_fused_1_2_1
+ _rpad_fused_1_3_0
+ _rpad_fused_1_3_1
+ _rpad_fused_1_4_0
+ _rpad_fused_1_4_1
+ _rpad_fused_1_5_0
+ _rpad_fused_1_5_1
+ _rpad_fused_1_6_0
+ _rpad_fused_1_6_1
+ _rpad_fused_1_7_0
+ _rpad_fused_1_7_1
+ _rpad_fused_1_8_0
+ _rpad_fused_1_8_1
+ _rpad_fused_2_1_0
+ _rpad_fused_2_1_1
+ _rpad_fused_2_2_0
+ _rpad_fused_2_2_1
+ _rpad_fused_2_3_0
+ _rpad_fused_2_3_1
+ _rpad_fused_2_4_0
+ _rpad_fused_2_4_1
+ _rpad_fused_2_5_0
+ _rpad_fused_2_5_1
+ _rpad_fused_2_6_0
+ _rpad_fused_2_6_1
+ _rpad_fused_2_7_0
+ _rpad_fused_2_7_1
+ _rpad_fused_2_8_0
+ _rpad_fused_2_8_1
+ _rpad_fused_3_1_0
+ _rpad_fused_3_1_1
+ _rpad_fused_3_2_0
+ _rpad_fused_3_2_1
+ _rpad_fused_3_3_0
+ _rpad_fused_3_3_1
+ _rpad_fused_3_4_0
+ _rpad_fused_3_4_1
+ _rpad_fused_3_5_0
+ _rpad_fused_3_5_1
+ _rpad_fused_3_6_0
+ _rpad_fused_3_6_1
+ _rpad_fused_3_7_0
+ _rpad_fused_3_7_1
+ _rpad_fused_3_8_0
+ _rpad_fused_3_8_1
+ _rpad_fused_4_1_0
+ _rpad_fused_4_1_1
+ _rpad_fused_4_2_0
+ _rpad_fused_4_2_1
+ _rpad_fused_4_3_0
+ _rpad_fused_4_3_1
+ _rpad_fused_4_4_0
+ _rpad_fused_4_4_1
+ _rpad_fused_4_5_0
+ _rpad_fused_4_5_1
+ _rpad_fused_4_6_0
+ _rpad_fused_4_6_1
+ _rpad_fused_4_7_0
+ _rpad_fused_4_7_1
+ _rpad_fused_4_8_0
+ _rpad_fused_4_8_1
+ _rpad_fused_table
+ _rpad_scalar_pixel
+ _rpad_xgather_build
+ _vImageResizeFaceID_Planar16U
+ _vImageResizeFaceID_Planar8toPlanar16U
+ _vImageResizeWithPaddingFaceID_Planar16U
+ _vImageResizeWithPaddingFaceID_Planar8toPlanar16U
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8S3foz/Sources/vImage/Source/Alpha_CGComposite.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8S3foz/Sources/vImage/Source/Conversion.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8S3foz/Sources/vImage/Source/Conversion_YUV.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8S3foz/Sources/vImage/Source/ConvertAnyToAny.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8S3foz/Sources/vImage/Source/ConvertPass.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8S3foz/Sources/vImage/Source/ImageTilingInfo.c"
+ "650.0.1"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wNQtmJ/Sources/vImage/Source/Alpha_CGComposite.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wNQtmJ/Sources/vImage/Source/Conversion.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wNQtmJ/Sources/vImage/Source/Conversion_YUV.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wNQtmJ/Sources/vImage/Source/ConvertAnyToAny.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wNQtmJ/Sources/vImage/Source/ConvertPass.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wNQtmJ/Sources/vImage/Source/ImageTilingInfo.c"
- "650"
```
