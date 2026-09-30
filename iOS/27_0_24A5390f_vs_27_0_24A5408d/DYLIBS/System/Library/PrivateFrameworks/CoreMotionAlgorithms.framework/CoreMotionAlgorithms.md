## CoreMotionAlgorithms

> `/System/Library/PrivateFrameworks/CoreMotionAlgorithms.framework/CoreMotionAlgorithms`

```diff

-3183.0.0.0.0
-  __TEXT.__text: 0x1b15a0
+3185.0.6.0.1
+  __TEXT.__text: 0x1b401c
   __TEXT.__objc_methlist: 0x9b4
-  __TEXT.__const: 0x5800
-  __TEXT.__gcc_except_tab: 0x4344
-  __TEXT.__cstring: 0x131ac
-  __TEXT.__oslogstring: 0x5efa
+  __TEXT.__const: 0x58a0
+  __TEXT.__gcc_except_tab: 0x4338
+  __TEXT.__cstring: 0x13420
+  __TEXT.__oslogstring: 0x5cdd
   __TEXT.__ustring: 0xce
-  __TEXT.__unwind_info: 0x5658
+  __TEXT.__unwind_info: 0x55f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x600
+  __DATA_CONST.__const: 0x608
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__objc_selrefs: 0x7f0
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__got: 0x120
-  __AUTH_CONST.__const: 0xb7b0
+  __DATA_CONST.__got: 0x138
+  __AUTH_CONST.__const: 0xb7f0
   __AUTH_CONST.__cfstring: 0xa20
   __AUTH_CONST.__objc_const: 0x17c0
   __AUTH_CONST.__weak_auth_got: 0x18

   __AUTH.__data: 0x8
   __DATA.__objc_ivar: 0x180
   __DATA.__data: 0xc8
-  __DATA.__bss: 0x1460
+  __DATA.__bss: 0x1480
   __DATA.__common: 0x110
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5813
-  Symbols:   289
-  CStrings:  4099
+  Functions: 5803
+  Symbols:   292
+  CStrings:  4128
 
Symbols:
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
CStrings:
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 249,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 255,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 71,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 78,invalid col %zu > %zu."
+ "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 250,invalid element %zu <= %zu."
+ "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 256,invalid element %zu <= %zu."
+ "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMVector.h, line 321,invalid index %zu >= %zu."
+ "Assertion failed: i0 < N-Ni+1 && j0 < N-Nj+1, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 320,indices exceed factored matrix size."
+ "Assertion failed: ldx < M*N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 84,invalid element %zu >= %zu."
+ "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 70,invalid row %zu > %zu."
+ "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 77,invalid row %zu > %zu."
+ "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 204,invalid row %zu > %zu."
+ "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 209,invalid row %zu > %zu."
+ "adhrHeartRate"
+ "adhrHeartRateConfidence"
+ "epochsWithInsufficientHGForStiction"
+ "epochsWithStiction"
+ "epochsWithoutStiction"
+ "groupADeltaVThreshold1"
+ "groupADeltaVThreshold2"
+ "groupAMaxAccelNormThreshold"
+ "groupAPeakPressure"
+ "groupAShortAudioNumThreshold"
+ "groupAZgTimeThreshold"
+ "groupApplied"
+ "groupBDeltaVThreshold1"
+ "groupBDeltaVThreshold2"
+ "groupBMaxAccelNormThreshold"
+ "groupBPeakPressure"
+ "groupBShortAudioNumThreshold"
+ "groupBZgTimeThreshold"
+ "groupIsA"
+ "scaledADHRMets"
+ "stictionDuration"
+ "stictionStatus"
+ "stictionThreshold"
+ "zgIsAHStateStable"
+ "zgIsFreefallA"
+ "zgIsFreefallB"
+ "zgMetaTotalZgTimeA"
+ "zgMetaTotalZgTimeB"
+ "zgSelectedVariant"
+ "zgSettledAHState"
+ "zgUsedSettledState"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf01"
- "Assertion failed: (fIirFilterParams != __null) && (fIirFilterParams->filterOrder <= kMaxFilterOrder), file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/CMIirFilter.cpp, line 17,IirFilterParams,%p,filterOrder,%d,maxFilterOrder,%d."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 236,invalid col %zu > %zu."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 242,invalid col %zu > %zu."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 73,invalid col %zu > %zu."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 80,invalid col %zu > %zu."
- "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 237,invalid element %zu <= %zu."
- "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 243,invalid element %zu <= %zu."
- "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMVector.h, line 299,invalid index %zu >= %zu."
- "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMVector.h, line 305,invalid index %zu >= %zu."
- "Assertion failed: i0 < N-Ni+1 && j0 < N-Nj+1, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 307,indices exceed factored matrix size."
- "Assertion failed: ldx < M*N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 86,invalid element %zu >= %zu."
- "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 72,invalid row %zu > %zu."
- "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 79,invalid row %zu > %zu."
- "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 191,invalid row %zu > %zu."
- "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 196,invalid row %zu > %zu."
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0q"
```
