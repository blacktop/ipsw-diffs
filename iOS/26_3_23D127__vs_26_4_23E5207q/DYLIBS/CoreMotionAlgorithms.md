## CoreMotionAlgorithms

> `/System/Library/PrivateFrameworks/CoreMotionAlgorithms.framework/CoreMotionAlgorithms`

```diff

-3068.0.15.0.0
-  __TEXT.__text: 0x1abf88
-  __TEXT.__auth_stubs: 0xcf0
+3072.0.40.0.1
+  __TEXT.__text: 0x1a6080
+  __TEXT.__auth_stubs: 0xd20
   __TEXT.__objc_methlist: 0x9b4
-  __TEXT.__const: 0x5382
-  __TEXT.__gcc_except_tab: 0x4308
-  __TEXT.__cstring: 0x11769
-  __TEXT.__oslogstring: 0x5acb
+  __TEXT.__const: 0x5402
+  __TEXT.__gcc_except_tab: 0x44c4
+  __TEXT.__cstring: 0x13e5c
+  __TEXT.__oslogstring: 0x5efa
   __TEXT.__ustring: 0xce
-  __TEXT.__unwind_info: 0x51c8
+  __TEXT.__unwind_info: 0x5370
   __TEXT.__objc_classname: 0x1b5
   __TEXT.__objc_methname: 0x257c
   __TEXT.__objc_methtype: 0x2f7a
   __TEXT.__objc_stubs: 0x1880
   __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0x5e0
+  __DATA_CONST.__const: 0x600
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x7f0
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x688
-  __AUTH_CONST.__const: 0xabb0
+  __AUTH_CONST.__auth_got: 0x6a0
+  __AUTH_CONST.__const: 0xad60
   __AUTH_CONST.__cfstring: 0xa20
   __AUTH_CONST.__objc_const: 0x17c0
   __AUTH.__objc_data: 0x3c0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: DB4028DD-0831-395C-8386-CA4FE495F646
-  Functions: 5417
-  Symbols:   286
-  CStrings:  4332
+  UUID: 6C7CD75F-58E8-3B3A-9B21-B538BB6BD036
+  Functions: 5534
+  Symbols:   290
+  CStrings:  4390
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_autoreleaseReturnValue
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x26
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/iterator_operations.h:209: libc++ Hardening assertion __count == 0 || (__dist < 0) == (__count < 0) failed: __sentinel must precede __iter when __count < 0\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:122: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:127: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:158: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:164: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1522: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CILbugDq_gD4q-gXz2-hjsyvYk1Szsh-KSIre30/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "/Library/Caches/com.apple.xbs/FAC51266-0588-4014-9CE0-77CDDA9AB9AB/TemporaryDirectory.tGKc5k/Sources/CoreMotionAlgorithmsFramework/Framework/CoreMotionAlgorithms/PrecisionFinding/CMAPrecisionFindingManager.mm"
+ "/Library/Caches/com.apple.xbs/FAC51266-0588-4014-9CE0-77CDDA9AB9AB/TemporaryDirectory.tGKc5k/Sources/CoreMotionAlgorithmsFramework/Framework/MotionSensorLogging/MSLWriterManager.cpp"
+ "Assertion failed: (fIirFilterParams != __null) && (fIirFilterParams->filterOrder <= kMaxFilterOrder), file /Library/Caches/com.apple.xbs/FAC51266-0588-4014-9CE0-77CDDA9AB9AB/TemporaryDirectory.tGKc5k/Sources/CoreMotionAlgorithmsFramework/Oscar/CMIirFilter.cpp, line 17,IirFilterParams,%p,filterOrder,%d,maxFilterOrder,%d."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/FAC51266-0588-4014-9CE0-77CDDA9AB9AB/TemporaryDirectory.tGKc5k/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 231,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/FAC51266-0588-4014-9CE0-77CDDA9AB9AB/TemporaryDirectory.tGKc5k/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 237,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/FAC51266-0588-4014-9CE0-77CDDA9AB9AB/TemporaryDirectory.tGKc5k/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 71,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/FAC51266-0588-4014-9CE0-77CDDA9AB9AB/TemporaryDirectory.tGKc5k/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 78,invalid col %zu > %zu."
+ "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/FAC51266-0588-4014-9CE0-77CDDA9AB9AB/TemporaryDirectory.tGKc5k/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 232,invalid element %zu <= %zu."
+ "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/FAC51266-0588-4014-9CE0-77CDDA9AB9AB/TemporaryDirectory.tGKc5k/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 238,invalid element %zu <= %zu."
+ "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/FAC51266-0588-4014-9CE0-77CDDA9AB9AB/TemporaryDirectory.tGKc5k/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMVector.h, line 273,invalid index %zu >= %zu."
+ "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/FAC51266-0588-4014-9CE0-77CDDA9AB9AB/TemporaryDirectory.tGKc5k/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMVector.h, line 279,invalid index %zu >= %zu."
+ "Assertion failed: i < fCapacity, file /Library/Caches/com.apple.xbs/FAC51266-0588-4014-9CE0-77CDDA9AB9AB/TemporaryDirectory.tGKc5k/Sources/CoreMotionAlgorithmsFramework/Oscar/CMQueue.h, line 233,i,%zu,capacity,%u."
+ "Assertion failed: i0 < N-Ni+1 && j0 < N-Nj+1, file /Library/Caches/com.apple.xbs/FAC51266-0588-4014-9CE0-77CDDA9AB9AB/TemporaryDirectory.tGKc5k/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 302,indices exceed factored matrix size."
+ "Assertion failed: ldx < M*N, file /Library/Caches/com.apple.xbs/FAC51266-0588-4014-9CE0-77CDDA9AB9AB/TemporaryDirectory.tGKc5k/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 84,invalid element %zu >= %zu."
+ "Assertion failed: rhs.capacity() == capacity(), file /Library/Caches/com.apple.xbs/FAC51266-0588-4014-9CE0-77CDDA9AB9AB/TemporaryDirectory.tGKc5k/Sources/CoreMotionAlgorithmsFramework/Oscar/CMQueue.h, line 70,capacity,%zu,%zu."
+ "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/FAC51266-0588-4014-9CE0-77CDDA9AB9AB/TemporaryDirectory.tGKc5k/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 70,invalid row %zu > %zu."
+ "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/FAC51266-0588-4014-9CE0-77CDDA9AB9AB/TemporaryDirectory.tGKc5k/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 77,invalid row %zu > %zu."
+ "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/FAC51266-0588-4014-9CE0-77CDDA9AB9AB/TemporaryDirectory.tGKc5k/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 186,invalid row %zu > %zu."
+ "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/FAC51266-0588-4014-9CE0-77CDDA9AB9AB/TemporaryDirectory.tGKc5k/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 191,invalid row %zu > %zu."
+ "accumulatedRotation"
+ "angleThreshold"
+ "angularFenceReference"
+ "angularFenceState"
+ "budSide"
+ "centerXPixels"
+ "centerYPixels"
+ "detectionClass"
+ "detectionConfidence"
+ "didExceedAngleThreshold"
+ "displacementUncertaintyX"
+ "displacementUncertaintyY"
+ "displacementUncertaintyZ"
+ "entityKitBoundingBoxCorrection"
+ "entityKitBoundingBoxDataList"
+ "entityKitDataPoC"
+ "gtbTimestampUS"
+ "heightPixels"
+ "intentionState"
+ "numberOfTotalDetectedObjects"
+ "primaryBudSide"
+ "qBF"
+ "qCB"
+ "quaternionRefW"
+ "quaternionRefX"
+ "quaternionRefY"
+ "quaternionRefZ"
+ "rB_SB"
+ "rF_SB"
+ "timestampMicroSeconds"
+ "widthPixels"
- "/Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Framework/CoreMotionAlgorithms/PrecisionFinding/CMAPrecisionFindingManager.mm"
- "/Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Framework/MotionSensorLogging/MSLWriterManager.cpp"
- "Assertion failed: (fIirFilterParams != __null) && (fIirFilterParams->filterOrder <= kMaxFilterOrder), file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/CMIirFilter.cpp, line 17,IirFilterParams,%p,filterOrder,%d,maxFilterOrder,%d."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 231,invalid col %zu > %zu."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 237,invalid col %zu > %zu."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 71,invalid col %zu > %zu."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 78,invalid col %zu > %zu."
- "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 232,invalid element %zu <= %zu."
- "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 238,invalid element %zu <= %zu."
- "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMVector.h, line 273,invalid index %zu >= %zu."
- "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMVector.h, line 279,invalid index %zu >= %zu."
- "Assertion failed: i < fCapacity, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/CMQueue.h, line 233,i,%zu,capacity,%u."
- "Assertion failed: i0 < N-Ni+1 && j0 < N-Nj+1, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 302,indices exceed factored matrix size."
- "Assertion failed: ldx < M*N, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 84,invalid element %zu >= %zu."
- "Assertion failed: rhs.capacity() == capacity(), file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/CMQueue.h, line 70,capacity,%zu,%zu."
- "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 70,invalid row %zu > %zu."
- "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 77,invalid row %zu > %zu."
- "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 186,invalid row %zu > %zu."
- "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 191,invalid row %zu > %zu."

```
