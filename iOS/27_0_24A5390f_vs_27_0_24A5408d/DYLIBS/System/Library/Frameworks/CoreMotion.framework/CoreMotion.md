## CoreMotion

> `/System/Library/Frameworks/CoreMotion.framework/CoreMotion`

```diff

-3183.0.0.0.0
-  __TEXT.__text: 0x3ae150
-  __TEXT.__objc_methlist: 0xd0b4
-  __TEXT.__const: 0xc530
+3185.0.6.0.1
+  __TEXT.__text: 0x3b5ea4
+  __TEXT.__objc_methlist: 0xd0e4
+  __TEXT.__const: 0xc690
   __TEXT.__swift5_typeref: 0x257
   __TEXT.__swift5_reflstr: 0x2e
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__constg_swiftt: 0xb8
   __TEXT.__swift5_fieldmd: 0x70
   __TEXT.__swift5_capture: 0x40
-  __TEXT.__oslogstring: 0x2d130
-  __TEXT.__cstring: 0x457a3
+  __TEXT.__oslogstring: 0x2d273
+  __TEXT.__cstring: 0x459ba
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x10
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x30
-  __TEXT.__gcc_except_tab: 0xca1c
-  __TEXT.__unwind_info: 0xb6e0
+  __TEXT.__gcc_except_tab: 0xc9e4
+  __TEXT.__unwind_info: 0xb648
   __TEXT.__eh_frame: 0x178
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3a48
+  __DATA_CONST.__const: 0x3a08
   __DATA_CONST.__objc_classlist: 0x880
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x5488
+  __DATA_CONST.__objc_selrefs: 0x5480
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x770
   __DATA_CONST.__objc_arraydata: 0x240
   __DATA_CONST.__got: 0x7e8
-  __AUTH_CONST.__const: 0x14fc0
-  __AUTH_CONST.__cfstring: 0x135c0
-  __AUTH_CONST.__objc_const: 0x1c9f8
+  __AUTH_CONST.__const: 0x14f60
+  __AUTH_CONST.__cfstring: 0x136e0
+  __AUTH_CONST.__objc_const: 0x1caa8
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x258

   __AUTH_CONST.__auth_got: 0x1490
   __AUTH.__objc_data: 0x3f20
   __AUTH.__data: 0x220
-  __DATA.__objc_ivar: 0x16d8
+  __DATA.__objc_ivar: 0x16e8
   __DATA.__data: 0xde8
   __DATA.__bss: 0x4b0
   __DATA.__common: 0xf8

   __DATA_DIRTY.__objc_data: 0x15e0
   __DATA_DIRTY.__data: 0x138
   __DATA_DIRTY.__common: 0x89
-  __DATA_DIRTY.__bss: 0x1038
+  __DATA_DIRTY.__bss: 0x10a0
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 12363
-  Symbols:   1772
-  CStrings:  11071
+  Functions: 12331
+  Symbols:   1776
+  CStrings:  11104
 
Symbols:
+ _CMSuppressionType2ClientEvent
+ _CMSuppressionType2ClientType
+ _CMSuppressionType2EventTime
+ _CMSuppressionType2VOEvent
CStrings:
+ "%@, <recordId, %lu, startDate, %@, activityEndTime, %@, workoutSessionId %@, workoutType, %lu, hrRecovery, %f, lambda, %f, hrMax, %f, hrMinAdjusted, %f, recoveryOnsetTime, %@, steadyStateHR, %f, status, %lu, sessionHrRecovery, %f, peakHR, %f, hrRecoveryReference, %f, testType, %ld>"
+ "%@, <recordId, %lu, startDate, %@, workoutType, %ld, sessionId, %@, durationInSeconds, %f, pointCount, %llu, hrMax, %f, hrMin, %f, meanHr, %f, meanVo2, %f, meanSpeed, %f, meanGrade, %f, meanHrConfidence, %f, meanHrCadenceAgreement, %f, meanCadence, %f, vo2MaxModelSource, %ld, sessionType, %ld, platformSource, %ld>"
+ ", platformSource, %ld, testType, %ld"
+ "-[CMBody _startUpdatingBodyToken:]"
+ "-[CMBody _stopUpdatingBodyToken:]"
+ "Assertion failed: !empty(), file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/CMVectorBuffer.h, line 141,front() on empty buffer."
+ "Assertion failed: !empty(), file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/CMVectorBuffer.h, line 147,back() on empty buffer."
+ "Assertion failed: !empty(), file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/CMVectorBuffer.h, line 163,maxElement() on empty buffer."
+ "Assertion failed: !empty(), file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/CMVectorBuffer.h, line 185,minElement() on empty buffer."
+ "Assertion failed: !empty(), file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/CMVectorBuffer.h, line 225,variance() on empty buffer."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMFactoredMatrix.h, line 255,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMMatrix.h, line 71,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMMatrix.h, line 78,invalid col %zu > %zu."
+ "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMFactoredMatrix.h, line 250,invalid element %zu <= %zu."
+ "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMFactoredMatrix.h, line 256,invalid element %zu <= %zu."
+ "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMVector.h, line 315,invalid index %zu >= %zu."
+ "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMVector.h, line 321,invalid index %zu >= %zu."
+ "Assertion failed: lambda2 != 0, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMOQuaternion.cpp, line 152,invalid weights."
+ "Assertion failed: ldx < M*N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMMatrix.h, line 84,invalid element %zu >= %zu."
+ "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMMatrix.h, line 70,invalid row %zu > %zu."
+ "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMMatrix.h, line 77,invalid row %zu > %zu."
+ "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMFactoredMatrix.h, line 209,invalid row %zu > %zu."
+ "Assertion failed: start <= end && end <= fCapacity, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/CMQueue.h, line 267,start=%zu end=%zu fCapacity=%u."
+ "Assertion failed: static_cast<uint32_t>(Cap) == fCapacity, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/CMQueue.h, line 252,fastIndex Cap=%zu mismatches fCapacity=%u."
+ "Assertion failed: t >= 0 && t <= 1, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMOQuaternion.cpp, line 300,Invalid time t for slerp."
+ "CMVector<T, 3> CMFactoredMatrix<float, 3>::biermanObservationalUpdateSkew3(T, T, T, T, T, T, T) [T = float, N = 3, Dummy = void]"
+ "VOEvent"
+ "[CMBody] _startUpdatingBodyToken:%{public}@"
+ "[CMBody] _stopUpdatingBodyToken:%{public}@"
+ "adhrHeartRate"
+ "adhrHeartRateConfidence"
+ "alpha <= 0, matrix !positive definite"
+ "clientEvent"
+ "clientType"
+ "const T &CMQueue<CMVector<float, 3>>::fastIndex(const size_t) const [T = CMVector<float, 3>, Cap = 16UL]"
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
+ "kCMCardioFitnessResultsCodingKeyPlatformSource"
+ "kCMCardioFitnessResultsCodingKeyTestType"
+ "kCMCardioFitnessSummaryCodingKeyPlatformSource"
+ "kCMRecoverySessionCodingKeyTestType"
+ "scaledADHRMets"
+ "stictionDuration"
+ "stictionStatus"
+ "stictionThreshold"
+ "void CMQueue<CMVector<float, 1>>::linearRanges(size_t, size_t, const T **, size_t *, const T **, size_t *) const [T = CMVector<float, 1>]"
+ "void CMQueue<CMVector<float, 3>>::linearRanges(size_t, size_t, const T **, size_t *, const T **, size_t *) const [T = CMVector<float, 3>]"
+ "zgIsAHStateStable"
+ "zgIsFreefallA"
+ "zgIsFreefallB"
+ "zgMetaTotalZgTimeA"
+ "zgMetaTotalZgTimeB"
+ "zgSelectedVariant"
+ "zgSettledAHState"
+ "zgUsedSettledState"
- "%@, <recordId, %lu, startDate, %@, activityEndTime, %@, workoutSessionId %@, workoutType, %lu, hrRecovery, %f, lambda, %f, hrMax, %f, hrMinAdjusted, %f, recoveryOnsetTime, %@, steadyStateHR, %f, status, %lu, sessionHrRecovery, %f, peakHR, %f, hrRecoveryReference, %f>"
- "%@, <recordId, %lu, startDate, %@, workoutType, %ld, sessionId, %@, durationInSeconds, %f, pointCount, %llu, hrMax, %f, hrMin, %f, meanHr, %f, meanVo2, %f, meanSpeed, %f, meanGrade, %f, meanHrConfidence, %f, meanHrCadenceAgreement, %f, meanCadence, %f, vo2MaxModelSource, %ld, sessionType, %ld>"
- "-[CMBody _startUpdatingMotionManager:]"
- "-[CMBody _stopUpdatingMotionManager:]"
- "Assertion failed: !empty(), file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/CMVectorBuffer.h, line 139,front() on empty buffer."
- "Assertion failed: !empty(), file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/CMVectorBuffer.h, line 145,back() on empty buffer."
- "Assertion failed: !empty(), file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/CMVectorBuffer.h, line 161,maxElement() on empty buffer."
- "Assertion failed: !empty(), file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/CMVectorBuffer.h, line 183,minElement() on empty buffer."
- "Assertion failed: !empty(), file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/CMVectorBuffer.h, line 210,variance() on empty buffer."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMFactoredMatrix.h, line 242,invalid col %zu > %zu."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMMatrix.h, line 73,invalid col %zu > %zu."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMMatrix.h, line 80,invalid col %zu > %zu."
- "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMFactoredMatrix.h, line 237,invalid element %zu <= %zu."
- "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMFactoredMatrix.h, line 243,invalid element %zu <= %zu."
- "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMVector.h, line 299,invalid index %zu >= %zu."
- "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMVector.h, line 305,invalid index %zu >= %zu."
- "Assertion failed: i < size(), file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/CMVectorBuffer.h, line 39,out of buffer range %zu."
- "Assertion failed: lambda2 != 0, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMOQuaternion.cpp, line 208,invalid weights."
- "Assertion failed: ldx < M*N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMMatrix.h, line 86,invalid element %zu >= %zu."
- "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMMatrix.h, line 72,invalid row %zu > %zu."
- "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMMatrix.h, line 79,invalid row %zu > %zu."
- "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMFactoredMatrix.h, line 196,invalid row %zu > %zu."
- "Assertion failed: t >= 0 && t <= 1, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMOQuaternion.cpp, line 375,Invalid time t for slerp."
- "Element &CMVectorBufferBase<float, 1>::operator[](const size_t) [T = float, N = 1]"
- "Element &CMVectorBufferBase<float, 3>::operator[](const size_t) [T = float, N = 3]"
- "T &CMVector<float, 12>::operator[](const size_t) [T = float, N = 12]"
- "T &CMVector<float, 4>::operator[](const size_t) [T = float, N = 4]"
- "T &CMVector<float, 6>::operator[](const size_t) [T = float, N = 6]"
- "T &CMVector<float, 9>::operator[](const size_t) [T = float, N = 9]"
- "T CMVector<float, 12>::operator[](const size_t) const [T = float, N = 12]"
- "T CMVector<float, 2>::operator[](const size_t) const [T = float, N = 2]"
- "T CMVector<float, 3>::operator[](const size_t) const [T = float, N = 3]"
- "T CMVector<float, 4>::operator[](const size_t) const [T = float, N = 4]"
- "T CMVector<float, 6>::operator[](const size_t) const [T = float, N = 6]"
- "T CMVector<float, 9>::operator[](const size_t) const [T = float, N = 9]"
- "[CMBody] _startUpdatingMotionManager:%@"
- "[CMBody] _stopUpdatingMotionManager:%@"
```
