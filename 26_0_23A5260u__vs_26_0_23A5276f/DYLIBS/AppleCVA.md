## AppleCVA

> `/System/Library/PrivateFrameworks/AppleCVA.framework/AppleCVA`

```diff

-1002.4.0.0.0
-  __TEXT.__text: 0xbd788
-  __TEXT.__auth_stubs: 0x1ab0
+1002.5.0.0.0
+  __TEXT.__text: 0xb3f7c
+  __TEXT.__auth_stubs: 0x1a60
   __TEXT.__objc_methlist: 0xb4
-  __TEXT.__const: 0x999
-  __TEXT.__gcc_except_tab: 0x4928
-  __TEXT.__cstring: 0x5bb8
-  __TEXT.__oslogstring: 0x8f87
-  __TEXT.__unwind_info: 0x1350
+  __TEXT.__const: 0x929
+  __TEXT.__gcc_except_tab: 0x4938
+  __TEXT.__cstring: 0x5a75
+  __TEXT.__oslogstring: 0x8f2d
+  __TEXT.__unwind_info: 0x1310
   __TEXT.__objc_classname: 0x67
   __TEXT.__objc_methname: 0xd69
   __TEXT.__objc_methtype: 0x1e6
   __TEXT.__objc_stubs: 0x1220
   __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0x1578
+  __DATA_CONST.__const: 0x1580
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x498
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0xd68
+  __AUTH_CONST.__auth_got: 0xd40
   __AUTH_CONST.__const: 0x1f20
-  __AUTH_CONST.__cfstring: 0x3960
+  __AUTH_CONST.__cfstring: 0x3980
   __AUTH_CONST.__objc_const: 0x348
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0xd8

   __AUTH_CONST.__objc_floatobj: 0xf0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x1c
-  __DATA.__bss: 0x300
+  __DATA.__bss: 0x280
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x40
   __DATA_DIRTY.__bss: 0x220

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 994518A6-2C3A-371C-9C86-D8C5BD84BF2F
-  Functions: 1198
-  Symbols:   972
-  CStrings:  2339
+  UUID: 3687DC7E-54BC-36D4-A259-20E15A781C52
+  Functions: 1174
+  Symbols:   968
+  CStrings:  2331
 
Symbols:
+ _kCVAViewpointCorrection_StereographicFisheyeFactor
- __ZN3cva11ItemHandler11createValueIyEES0_RKT_
- __ZNK3cva4Path8filenameEv
- _espresso_network_declare_input
- _espresso_network_declare_output
- _powf
CStrings:
+ "CVAEspressoRegressor"
+ "Disabling correction because the fisheye factor %f is lower than %f"
+ "FaceKitLiteFilter: found tracking failure with nonzero confidence, setting confidence to zero"
+ "FaceKitLiteFilterOutputConverter: found tracking failure with nonzero confidence"
+ "Fisheye factor value is %f"
+ "Fisheye strength has been deprecated and will be ignored."
+ "Invalid fisheye factor: %f"
+ "StereographicFisheyeFactor"
+ "ViewpointCorrection # frames: success (%i (+%i), %.1f ms (%.1f ms)), dropped (%i (+%i), %.1f ms (%.1f ms)), error (%i (+%i), %.1f ms (%.1f ms)), modified (%i (+%i), %.1f ms (%.1f ms)), skipped due to distortion (%i (+%i), %.1f ms (%.1f ms))"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/facekit/facekitdictionaryconverter.cpp"
- "Disabling correction since fisheye strength is %f"
- "Espresso"
- "Failed to extract blendshapes from the animation dictionary."
- "Failed to retrieve gaze from the animation dictionary."
- "Invalid fisheye strength: %f"
- "Missing key %s in the animation dictionary."
- "ViewpointCorrection # frames: success (%i (+%i), %.1f ms (%.1f ms)), dropped (%i (+%i), %.1f ms (%.1f ms)), error (%i (+%i), %.1f ms (%.1f ms)), modified (%i (+%i), %.1f ms (%.1f ms)), skipped due to fisheye strength (%i (+%i), %.1f ms (%.1f ms))"
- "could not declare input [%d, %s]"
- "could not declare output [%d, %s]"
- "could not find a corresponding json file [%s] to load custom input/output layers"
- "could not register the input and output layers"
- "couldn't convert face rectangle dictionary"
- "dictionary doesn't contain face detection keys"
- "espresso has already initialized"
- "fisheye strength value is %f"
- "invalid model json file, 'Inputs' must be an array"
- "invalid model json file, 'Outputs' must be an array"

```
