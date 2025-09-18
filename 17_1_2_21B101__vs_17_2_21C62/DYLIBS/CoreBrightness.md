## CoreBrightness

> `/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`

```diff

-1603.42.1.0.0
-  __TEXT.__text: 0x17de3c
+1603.60.7.0.0
+  __TEXT.__text: 0x17ea54
   __TEXT.__auth_stubs: 0x1490
-  __TEXT.__objc_methlist: 0x6664
-  __TEXT.__cstring: 0x971d
+  __TEXT.__objc_methlist: 0x667c
+  __TEXT.__cstring: 0x9744
   __TEXT.__const: 0xee90
-  __TEXT.__oslogstring: 0x11430
+  __TEXT.__oslogstring: 0x114f5
   __TEXT.__gcc_except_tab: 0x1540
   __TEXT.__dlopen_cstrs: 0x14f
-  __TEXT.__unwind_info: 0x23e4
+  __TEXT.__unwind_info: 0x23f8
   __TEXT.__eh_frame: 0x60
   __TEXT.__objc_classname: 0x8df
-  __TEXT.__objc_methname: 0xf22a
-  __TEXT.__objc_methtype: 0x38be
-  __TEXT.__objc_stubs: 0xbb60
+  __TEXT.__objc_methname: 0xf252
+  __TEXT.__objc_methtype: 0x38b0
+  __TEXT.__objc_stubs: 0xbba0
   __DATA_CONST.__got: 0x218
   __DATA_CONST.__const: 0x1e30
   __DATA_CONST.__objc_classlist: 0x378

   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x13c88
-  __DATA_CONST.__objc_selrefs: 0x3690
+  __DATA_CONST.__objc_selrefs: 0x36a0
   __DATA_CONST.__objc_arraydata: 0x3d0
   __AUTH_CONST.__objc_const: 0x2d0
-  __AUTH_CONST.__cfstring: 0xa820
+  __AUTH_CONST.__cfstring: 0xa860
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__objc_arrayobj: 0x1e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 32B37BF7-16BC-31A4-9206-34CA9FF430A1
-  Functions: 3672
-  Symbols:   12076
-  CStrings:  8130
+  UUID: D845038B-F709-3C72-8DC4-8FF473256878
+  Functions: 3676
+  Symbols:   12086
+  CStrings:  8138
 
Symbols:
+ -[CBAODTransitionController updateAAPFactor:]
+ -[CBAODTransitionController updateAllBrightnessFeaturesForced:]
+ -[CBAODTransitionController updateWhitePoint:]
+ GCC_except_table142
+ GCC_except_table172
+ GCC_except_table235
+ GCC_except_table237
+ GCC_except_table241
+ GCC_except_table287
+ GCC_except_table303
+ GCC_except_table306
+ GCC_except_table362
+ GCC_except_table365
+ GCC_except_table368
+ GCC_except_table378
+ GCC_except_table382
+ __ZN4AABC18sendAOTCurvesToDCPEv
+ ___30-[BLControl waitForALSArrival]_block_invoke.273
+ ___30-[BLControl waitForALSArrival]_block_invoke.274
+ ___36-[BLControl handleCADisplayArrival:]_block_invoke.132
+ ___41-[BLControl handleCAWindowServerDisplay:]_block_invoke.131
+ ___47-[BLControl keyboardBacklightHIDDeviceArrived:]_block_invoke.325
+ ___58-[CBAODModule copyAndHandleEventWithTransitionParameters:]_block_invoke.284
+ ___DisplaySetProperty_block_invoke.562
+ ___DisplaySetState_block_invoke.362
+ ____DisplaySetBrightnessFactor_block_invoke.725
+ ____ZN4AABC20setPropertyForClientEPK10__CFStringPKvS4__block_invoke.753
+ _____DisplayUpdateSlider_block_invoke.1090
+ _____DisplayUpdateSlider_block_invoke.1092
+ ___block_literal_global.1015
+ ___os_log_helper_16_2_8_8_32_8_0_8_0_8_0_8_0_8_0_8_0_8_0
+ __unnamed_array_storage.312
+ __unnamed_array_storage.316
+ __unnamed_array_storage.317
+ _objc_msgSend$updateAAPFactor:
+ _objc_msgSend$updateAllBrightnessFeaturesForced:
+ _objc_msgSend$updateWhitePoint:
- -[CBAODTransitionController updateAAPFactor:rampDuration:]
- GCC_except_table104
- GCC_except_table234
- GCC_except_table236
- GCC_except_table240
- GCC_except_table286
- GCC_except_table301
- GCC_except_table305
- GCC_except_table361
- GCC_except_table364
- GCC_except_table367
- GCC_except_table377
- GCC_except_table381
- ___30-[BLControl waitForALSArrival]_block_invoke.270
- ___30-[BLControl waitForALSArrival]_block_invoke.271
- ___36-[BLControl handleCADisplayArrival:]_block_invoke.129
- ___41-[BLControl handleCAWindowServerDisplay:]_block_invoke.128
- ___47-[BLControl keyboardBacklightHIDDeviceArrived:]_block_invoke.322
- ___58-[CBAODModule copyAndHandleEventWithTransitionParameters:]_block_invoke.281
- ___DisplaySetProperty_block_invoke.556
- ___DisplaySetState_block_invoke.356
- ____DisplaySetBrightnessFactor_block_invoke.719
- ____ZN4AABC20setPropertyForClientEPK10__CFStringPKvS4__block_invoke.750
- _____DisplayUpdateSlider_block_invoke.1084
- _____DisplayUpdateSlider_block_invoke.1086
- ___block_literal_global.1012
- __unnamed_array_storage.306
- __unnamed_array_storage.308
- __unnamed_array_storage.313
- _objc_msgSend$updateAAPFactor:rampDuration:
CStrings:
+ "ERROR: Force commiting CB features to CA failed! (%@)"
+ "Force "
+ "RaiseHighCurve"
+ "[AOD update][CA] Pushing: %scommit all features: brightness = %f; WP = (%f; %f), pcc = %f, brightness limit = %f, twilight = %f, ammolite = %f"
+ "raise-high-curve"
+ "updateAAPFactor:"
+ "updateAllBrightnessFeaturesForced:"
+ "updateWhitePoint:"
- "updateAAPFactor:rampDuration:"
- "v28@0:8f16d20"

```
