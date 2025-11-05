## AppleCVA

> `/System/Library/PrivateFrameworks/AppleCVA.framework/Versions/A/AppleCVA`

```diff

-1001.150.0.0.0
-  __TEXT.__text: 0x8f158
-  __TEXT.__auth_stubs: 0x1510
+1001.202.0.0.0
+  __TEXT.__text: 0x8bd6c
+  __TEXT.__auth_stubs: 0x1500
   __TEXT.__objc_methlist: 0x64
-  __TEXT.__gcc_except_tab: 0x231c
-  __TEXT.__const: 0x709
-  __TEXT.__cstring: 0x4711
-  __TEXT.__oslogstring: 0x2e22
+  __TEXT.__const: 0x729
+  __TEXT.__gcc_except_tab: 0x1f60
+  __TEXT.__cstring: 0x4804
+  __TEXT.__oslogstring: 0x2dec
   __TEXT.__unwind_info: 0xce0
   __TEXT.__objc_classname: 0x46
-  __TEXT.__objc_methname: 0x443
+  __TEXT.__objc_methname: 0x3f6
   __TEXT.__objc_methtype: 0xfd
-  __TEXT.__objc_stubs: 0x640
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0xe70
+  __TEXT.__objc_stubs: 0x5a0
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__const: 0xe78
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x190
+  __DATA_CONST.__objc_selrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0xa98
+  __AUTH_CONST.__auth_got: 0xa90
   __AUTH_CONST.__const: 0x1a88
-  __AUTH_CONST.__cfstring: 0x1b60
+  __AUTH_CONST.__cfstring: 0x1b80
   __AUTH_CONST.__objc_const: 0x160
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x18

   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0x88
-  __DATA.__bss: 0x3b0
+  __DATA.__bss: 0x3a8
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B3FE4B24-8EFE-33F9-AA4B-2EDABF79A84C
-  Functions: 892
+  UUID: BBE611C6-55F4-3E7C-8EC4-7A9971BD187E
+  Functions: 898
   Symbols:   621
-  CStrings:  1297
+  CStrings:  1298
 
Symbols:
+ _CVAFaceTrackingLiteGetCreateOptionsForFeatures
+ _CVAFaceTrackingLiteSetColorImageWithDistortion
+ __ZNSt3__122__libcpp_verbose_abortEPKcz
+ _kCVAFaceTracking_ConfidenceLevel
- _CVAFaceTrackingTransformData
- _OBJC_CLASS_$_NSMutableDictionary
- __ZNK3cva11ItemHandler9getVectorIjEENS_6MatrixIT_Lj0ELj1EXclsr6detailE7IsSmallIS3_XLj0EEXLj1EEEEEEEv
- _objc_alloc_init
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/facekit/accessibilityfilter.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/facekit/facekitdictionaryconverter.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/facekit/facekitlitefilter.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/geometry/src/three_d/identitytensor.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/geometry/src/three_d/quad_mesh.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/geometry/src/three_d/trackingriglite.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/tracking/src/io/framesequencedata.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/utils/src/CompressedDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/utils/src/FilePack.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/utils/src/ThreadWorkGroup.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/utils/src/fsByteArray.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/utils/src/fsFileDevice.cpp"
+ "Color camera extrinsics: (%.3f %.3f %.3f %.3f), (%.3f %.3f %.3f %.3f), (%.3f %.3f %.3f %.3f)"
+ "Color camera intrinsics: (%.3f %.3f %.3f), (%.3f %.3f %.3f), (%.3f %.3f %.3f)"
+ "Color camera resolution: %d x %d"
+ "bad_function_call was thrown in -fno-exceptions mode"
+ "bad_variant_access was thrown in -fno-exceptions mode"
+ "confidence_level"
+ "face_selection_offcenter_penalty"
+ "future_error was thrown in -fno-exceptions mode"
+ "off-center penalty for face selection"
+ "using strict error thresholds until tracking is stable (user %s)"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/facekit/accessibilityfilter.mm"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/facekit/facekitdictionaryconverter.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/facekit/facekitlitefilter.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/geometry/src/three_d/identitytensor.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/geometry/src/three_d/quad_mesh.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/geometry/src/three_d/trackingriglite.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/tracking/src/io/framesequencedata.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/utils/src/CompressedDevice.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/utils/src/FilePack.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/utils/src/ThreadWorkGroup.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/utils/src/fsByteArray.cpp"
- "/AppleInternal/Library/BuildRoots/16eafa31-bf9e-11ef-9851-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/utils/src/fsFileDevice.cpp"
- "Decreasing max distance for tracking to %f mm; due to previous error detected (user %s)."
- "Increasing min distance for tracking to %f mm; due to previous error detected (user %s)."
- "Set network failure threshold to %f; due to previous error detected (user %s)."
- "allKeys"
- "copy"
- "data dictionary contains invalid data"
- "initWithCapacity:"
- "invalid number of faces: %d"
- "isEqualToString:"
- "setObject:forKeyedSubscript:"

```
