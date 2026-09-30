## VisionCore

> `/System/Library/PrivateFrameworks/VisionCore.framework/VisionCore`

```diff

-8.0.34.0.0
-  __TEXT.__text: 0x2c0ec
-  __TEXT.__auth_stubs: 0xe80
+8.0.36.0.0
+  __TEXT.__text: 0x2b2ac
+  __TEXT.__auth_stubs: 0xe60
   __TEXT.__objc_methlist: 0x24e4
   __TEXT.__gcc_except_tab: 0x255c
   __TEXT.__const: 0xf4
-  __TEXT.__cstring: 0x3bdf
+  __TEXT.__cstring: 0x3256
   __TEXT.__dlopen_cstrs: 0x130
   __TEXT.__oslogstring: 0x1d5
-  __TEXT.__unwind_info: 0xef0
+  __TEXT.__unwind_info: 0xee8
   __TEXT.__objc_classname: 0xa13
-  __TEXT.__objc_methname: 0x74ae
+  __TEXT.__objc_methname: 0x74d0
   __TEXT.__objc_methtype: 0x20b3
   __TEXT.__objc_stubs: 0x3c60
   __DATA_CONST.__got: 0x348

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1548
+  __DATA_CONST.__objc_selrefs: 0x1550
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__auth_got: 0x758
+  __AUTH_CONST.__auth_got: 0x748
   __AUTH_CONST.__const: 0x260
   __AUTH_CONST.__cfstring: 0x3380
   __AUTH_CONST.__objc_const: 0x54c0
   __AUTH_CONST.__objc_intobj: 0x3a8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x2d0
+  __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x2f8
   __DATA.__data: 0x3c0
-  __DATA.__bss: 0x160
-  __DATA_DIRTY.__objc_data: 0x1090
+  __DATA.__bss: 0x120
+  __DATA_DIRTY.__objc_data: 0x1270
   __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 891
-  Symbols:   1364
-  CStrings:  1896
+  Functions: 888
+  Symbols:   1360
+  CStrings:  1840
 
Symbols:
- _snprintf
- _syslog
CStrings:
+ "stringByDeletingLastPathComponent"
- "%!s(MISSING) error %!l(MISSING)ld:%!s(MISSING) in %!s(MISSING) @ %!s(MISSING):%!d(MISSING)\n"
- "/Library/Caches/com.apple.xbs/Sources/VisionCore/Libraries/cvml-Core/Geometry2D/Geometry2D_Homography.c"
- "/Library/Caches/com.apple.xbs/Sources/VisionCore/Libraries/cvml-Core/Geometry2D/Geometry2D_Normalization.c"
- "/Library/Caches/com.apple.xbs/Sources/VisionCore/Libraries/cvml-Core/RANSAC/RANSAC_Common.c"
- "CVML_status Geometry2D_computeAdjointAndDeterminant(const float *, float *, float *)"
- "CVML_status Geometry2D_estimateHomography(const Geometry2D_cart2D *, const Geometry2D_cart2D *, float *)"
- "CVML_status Geometry2D_estimateHomographyMSS(const Geometry2D_cart2D *, const Geometry2D_cart2D *, float *, __CLPK_integer, float *)"
- "CVML_status Geometry2D_estimateHomographyOD(const Geometry2D_cart2D *, const Geometry2D_cart2D *, float *, __CLPK_integer, float *)"
- "CVML_status Geometry2D_estimateRANSACHomography(const Geometry2D_cart2D *, const Geometry2D_cart2D *, const RANSAC_Parameters *, float *, _Bool *)"
- "CVML_status Geometry2D_invertHomography(const float *, float *)"
- "CVML_status Geometry2D_mapHomography(const Geometry2D_cart2D *, const float *, Geometry2D_cart2D *)"
- "CVML_status Geometry2D_normalizePoints(const Geometry2D_cart2D *, float *, Geometry2D_cart2D *, float *, float *, float *)"
- "CVML_status Geometry2D_reprojectionErrorHomography(const Geometry2D_cart2D *, const float *, const Geometry2D_cart2D *, float *)"
- "CVML_status Geometry2D_symmetricReprojectionErrorHomography(const Geometry2D_cart2D *, const float *, const Geometry2D_cart2D *, float *)"
- "CVML_status RANSAC_estimateIterationThreshold(int, int, int, const RANSAC_Parameters *, int *)"
- "CVML_status module %!d(MISSING) error %!l(MISSING)ld"
- "Espresso error"
- "General error"
- "Geometry2D"
- "I/O error"
- "LAPACK error"
- "Not supported error"
- "OpenGL error"
- "batch size violation"
- "computation kill request was issued"
- "data inconsistency error"
- "delegate error"
- "division by zero"
- "error with projection computation"
- "feature extraction error"
- "hash already in use"
- "inconsistent state error"
- "incorrect binserializer key"
- "initialization error"
- "internal error"
- "invalid ID"
- "invalid data type"
- "invalid format"
- "invalid option"
- "invalid parameter"
- "memory allocation error"
- "missing option"
- "missing positional parameter"
- "no saved state to revert"
- "nominal distance not changed"
- "not implemented error"
- "ok"
- "out of bounds"
- "platform endianess not supported"
- "singular point configuration error"
- "small sparsity error"
- "too few IDs to build VIP model"
- "unexpected null pointer"
- "unknown option"
- "vImage related error"
- "video error"
- "warping error"

```
