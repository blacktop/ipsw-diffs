## BiometricKitUI

> `/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`

```diff

-681.0.0.0.0
-  __TEXT.__text: 0x700a0
-  __TEXT.__objc_methlist: 0x72b8
+684.0.0.0.0
+  __TEXT.__text: 0x70538
+  __TEXT.__objc_methlist: 0x72c0
   __TEXT.__const: 0xd44
   __TEXT.__gcc_except_tab: 0xde4
-  __TEXT.__cstring: 0x2fc6
-  __TEXT.__oslogstring: 0x66a3
+  __TEXT.__cstring: 0x2fd6
+  __TEXT.__oslogstring: 0x6853
   __TEXT.__dlopen_cstrs: 0x292
   __TEXT.__swift5_typeref: 0x2c2
   __TEXT.__swift5_capture: 0x114

   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x48d0
+  __DATA_CONST.__objc_selrefs: 0x48d8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0x188
   __DATA_CONST.__got: 0x880
   __AUTH_CONST.__const: 0xc50
   __AUTH_CONST.__cfstring: 0x33a0
-  __AUTH_CONST.__objc_const: 0x106e0
+  __AUTH_CONST.__objc_const: 0x10700
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_floatobj: 0x80

   __AUTH_CONST.__auth_got: 0x970
   __AUTH.__objc_data: 0x1448
   __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0x9f8
+  __DATA.__objc_ivar: 0x9fc
   __DATA.__data: 0x11c0
   __DATA.__bss: 0x648
   __DATA.__common: 0x1f8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2867
-  Symbols:   6370
-  CStrings:  1061
+  Functions: 2868
+  Symbols:   6373
+  CStrings:  1068
 
Symbols:
+ -[BKUIPearlEnrollView resetPitchCorrection]
+ GCC_except_table71
+ GCC_except_table95
+ _OBJC_IVAR_$_BKUIPearlEnrollView._lastLoggedCenterBinCorrectedPitch
+ _objc_msgSend$resetPitchCorrection
- GCC_except_table70
- GCC_except_table94
CStrings:
+ "Displaying instruction to reposition: '%s'"
+ "Init: productType: %{public}ld, isZoomEnabled: %{public}d, shouldUseUnifiedMesaEnrollment: %{public}d"
+ "LOWER"
+ "RAISE"
+ "centerBin correctedPitch %0.2f (rawPitch %0.2f - pitchCorrection %0.2f), window [%0.2f, %0.2f]"
+ "correctedPitch %0.2f (rawPitch %0.2f - pitchCorrection %0.2f) vs window [%0.2f, %0.2f] -> %s"
+ "resetPitchCorrection - clearing pitchCorrection %0.2f (samples: %lu, observedPitchRange: [%0.2f, %0.2f], state: %ld)"
+ "seeded pitchCorrection %0.2f from %d initial samples (state: %ld)"
+ "\xf0\xf0\x82"
- "Init: isZoomEnabled: %{public}d, shouldUseUnifiedMesaEnrollment: %{public}d"
- "\xf0\xf0r"
```
