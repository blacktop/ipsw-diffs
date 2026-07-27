## vImage

> `/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vImage.framework/Versions/A/vImage`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

 632.120.2.0.0
-  __TEXT.__text: 0x35fa6c
-  __TEXT.__auth_stubs: 0x470
+  __TEXT.__text: 0x37ab20
+  __TEXT.__auth_stubs: 0x480
   __TEXT.__delay_stubs: 0x780
   __TEXT.__delay_helper: 0x5a4
-  __TEXT.__const: 0x9a5b0
+  __TEXT.__const: 0x9a6b0
   __TEXT.__cstring: 0x6be8
-  __TEXT.__unwind_info: 0x24d0
-  __TEXT.__eh_frame: 0x37a4
+  __TEXT.__unwind_info: 0x25a0
+  __TEXT.__eh_frame: 0x3eac
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__const: 0x23e0
-  __AUTH_CONST.__auth_got: 0x328
+  __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0xcb08
   __DATA.__data: 0x50
   __DATA.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
-  Functions: 3355
-  Symbols:   4297
+  Functions: 3390
+  Symbols:   4334
   CStrings:  404
 
Symbols:
+ ___sme_memset
+ _vHorizontal_Reflect_ARGB_8888_SME2
+ _vHorizontal_Reflect_ARGB_8888_SME2_internal
+ _vHorizontal_Reflect_Planar_UInt16_SME2
+ _vHorizontal_Reflect_Planar_UInt16_SME2_internal
+ _vHorizontal_Reflect_Planar_UInt8_SME2
+ _vHorizontal_Reflect_Planar_UInt8_SME2_internal
+ _vHorizontal_Scale_ARGB_8888_SME_64x16
+ _vHorizontal_Scale_ARGB_8888_SME_64x16_internal
+ _vHorizontal_Scale_CbCr8_SME_64x16
+ _vHorizontal_Scale_CbCr8_SME_64x16_internal
+ _vHorizontal_Scale_Planar_UInt8_SME_64x16
+ _vHorizontal_Scale_Planar_UInt8_SME_64x16_internal
+ _vRotateClockwise270Degree_ARGB8888_SME2_internal
+ _vRotateClockwise270Degree_UInt16_SME2
+ _vRotateClockwise270Degree_UInt16_SME2_internal
+ _vRotateClockwise270Degree_UInt8_SME2
+ _vRotateClockwise270Degree_UInt8_SME2_internal
+ _vRotateClockwise90Degree_ARGB8888_SME2_internal
+ _vRotateClockwise90Degree_UInt16_SME2
+ _vRotateClockwise90Degree_UInt16_SME2_internal
+ _vRotateClockwise90Degree_UInt8_SME2
+ _vRotateClockwise90Degree_UInt8_SME2_internal
+ _vRotate_90_ARGB_8888_270Degree_SME2
+ _vRotate_90_ARGB_8888_90Degree_SME2
+ _vVertical_Reflect_ARGB_16S_SME2
+ _vVertical_Reflect_ARGB_16U_SME2
+ _vVertical_Reflect_ARGB_8888_SME2
+ _vVertical_Reflect_ARGB_8888_SME2_internal
+ _vVertical_Reflect_Planar_UInt8_SME2
+ _vVertical_Reflect_Planar_UInt8_SME2_internal
+ _vVertical_Scale_ARGB_8888_SME_64x16
+ _vVertical_Scale_ARGB_8888_SME_64x16_internal
+ _vVertical_Scale_CbCr8_SME_64x16
+ _vVertical_Scale_CbCr8_SME_64x16_internal
+ _vVertical_Scale_Planar_UInt8_SME_64x16
+ _vVertical_Scale_Planar_UInt8_SME_64x16_internal
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vFHJX1/Sources/vImage/Source/Alpha_CGComposite.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vFHJX1/Sources/vImage/Source/Conversion.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vFHJX1/Sources/vImage/Source/Conversion_YUV.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vFHJX1/Sources/vImage/Source/ConvertAnyToAny.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vFHJX1/Sources/vImage/Source/ConvertPass.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vFHJX1/Sources/vImage/Source/ImageTilingInfo.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YRxokG/Sources/vImage/Source/Alpha_CGComposite.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YRxokG/Sources/vImage/Source/Conversion.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YRxokG/Sources/vImage/Source/Conversion_YUV.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YRxokG/Sources/vImage/Source/ConvertAnyToAny.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YRxokG/Sources/vImage/Source/ConvertPass.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YRxokG/Sources/vImage/Source/ImageTilingInfo.c"
```
