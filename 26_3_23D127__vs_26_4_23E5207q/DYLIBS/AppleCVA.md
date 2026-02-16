## AppleCVA

> `/System/Library/PrivateFrameworks/AppleCVA.framework/AppleCVA`

```diff

-1002.75.0.0.0
-  __TEXT.__text: 0xb54c0
-  __TEXT.__auth_stubs: 0x1a60
+1002.101.0.0.0
+  __TEXT.__text: 0xb9bc4
+  __TEXT.__auth_stubs: 0x1a00
   __TEXT.__objc_methlist: 0xb4
-  __TEXT.__const: 0x959
-  __TEXT.__gcc_except_tab: 0x4994
-  __TEXT.__cstring: 0x5a63
-  __TEXT.__oslogstring: 0x939d
-  __TEXT.__unwind_info: 0x1318
+  __TEXT.__const: 0x939
+  __TEXT.__gcc_except_tab: 0x49f4
+  __TEXT.__cstring: 0x8479
+  __TEXT.__oslogstring: 0x9537
+  __TEXT.__unwind_info: 0x1340
   __TEXT.__objc_classname: 0x67
   __TEXT.__objc_methname: 0xd69
   __TEXT.__objc_methtype: 0x1e6
   __TEXT.__objc_stubs: 0x1220
   __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0x1580
+  __DATA_CONST.__const: 0x1588
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x498
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0xd40
+  __AUTH_CONST.__auth_got: 0xd10
   __AUTH_CONST.__const: 0x1f58
-  __AUTH_CONST.__cfstring: 0x3960
+  __AUTH_CONST.__cfstring: 0x3980
   __AUTH_CONST.__objc_const: 0x348
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0xd8

   __AUTH_CONST.__objc_floatobj: 0xf0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x1c
-  __DATA.__bss: 0x280
+  __DATA.__bss: 0x290
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x40
-  __DATA_DIRTY.__bss: 0x220
+  __DATA_DIRTY.__bss: 0x2a8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 083F5CC8-2B3C-3F80-995C-63DFDEB748FA
-  Functions: 1181
-  Symbols:   966
-  CStrings:  2348
+  UUID: 6A32A81A-E42C-32DF-9A68-F06857B8CFE6
+  Functions: 1182
+  Symbols:   961
+  CStrings:  2383
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _kCVAFaceTracking_ClearTrackedFaces
+ _kCVAFaceTracking_DataFailureTrackedFacesCleared
+ _objc_retainAutoreleasedReturnValue
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7reserveEm
- __ZNSt3__19to_stringEi
- _kCVAViewpointCorrection_StereographicFisheyeStrength
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x4
- _objc_retain_x9
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:122: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:127: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:158: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:164: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1522: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1402: libc++ Hardening assertion !empty() failed: list::pop_front() called with empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1471: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugBxmWdYADgk8Ks4IJnLk5DxIaMTk7cfbmc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "/Library/Caches/com.apple.xbs/0D804C89-688B-4CE2-A79B-6200F559F107/TemporaryDirectory.NxQRVR/Sources/AppleCVA/shared/src/modules/avatar/facekit/accessibilityfilter.mm"
+ "/Library/Caches/com.apple.xbs/0D804C89-688B-4CE2-A79B-6200F559F107/TemporaryDirectory.NxQRVR/Sources/AppleCVA/shared/src/modules/avatar/facekit/facekitlitefilter.cpp"
+ "/Library/Caches/com.apple.xbs/0D804C89-688B-4CE2-A79B-6200F559F107/TemporaryDirectory.NxQRVR/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/geometry/src/three_d/identitytensor.cpp"
+ "/Library/Caches/com.apple.xbs/0D804C89-688B-4CE2-A79B-6200F559F107/TemporaryDirectory.NxQRVR/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/geometry/src/three_d/quad_mesh.cpp"
+ "/Library/Caches/com.apple.xbs/0D804C89-688B-4CE2-A79B-6200F559F107/TemporaryDirectory.NxQRVR/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/geometry/src/three_d/trackingriglite.cpp"
+ "/Library/Caches/com.apple.xbs/0D804C89-688B-4CE2-A79B-6200F559F107/TemporaryDirectory.NxQRVR/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/tracking/src/io/framesequencedata.cpp"
+ "/Library/Caches/com.apple.xbs/0D804C89-688B-4CE2-A79B-6200F559F107/TemporaryDirectory.NxQRVR/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/utils/src/CompressedDevice.cpp"
+ "/Library/Caches/com.apple.xbs/0D804C89-688B-4CE2-A79B-6200F559F107/TemporaryDirectory.NxQRVR/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/utils/src/FilePack.cpp"
+ "/Library/Caches/com.apple.xbs/0D804C89-688B-4CE2-A79B-6200F559F107/TemporaryDirectory.NxQRVR/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/utils/src/ThreadWorkGroup.cpp"
+ "/Library/Caches/com.apple.xbs/0D804C89-688B-4CE2-A79B-6200F559F107/TemporaryDirectory.NxQRVR/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/utils/src/fsByteArray.cpp"
+ "/Library/Caches/com.apple.xbs/0D804C89-688B-4CE2-A79B-6200F559F107/TemporaryDirectory.NxQRVR/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/utils/src/fsFileDevice.cpp"
+ "Assertion failed: CMTIME_IS_VALID(trackedFaces[j]->lastPositionUpdateTimestamp())"
+ "Assertion failed: landmarks.has_value()"
+ "Assertion failed: trackedFaces[i]->isValid()"
+ "Assertion failed: trackedFaces[j]->isValid()"
+ "Client requested tracked faces to be discarded"
+ "Client requested tracked faces to be discarded (coincided with frame drop)"
+ "Discarding face (UUID=%s) due to overlap with another face (UUID=%s)."
+ "Running addLandmarksToDictionary(*landmarks, faceDictionary) failed with %s, returning %s"
+ "Running appendNewTrackedFaces(m_trackedFaces, faces, timestamp, uprightFaceRollAngle, distanceThresholdsMultiplier, m_maxNumberOfTrackedFaces) failed with %s, returning %s"
+ "Running cropEyes(commandBuffer, *landmarks, data.virtualCameraOffset(), crops) failed with %s, returning %s"
+ "Running discardOverlappingTracks(m_trackedFaces, TrackedFace::DiscardFacePassKey()) failed with %s, returning %s"
+ "Running m_debugRenderer->encode(*landmarks, yuv, *debugRendererState) failed with %s, returning %s"
+ "Running trackedFace->update(inputFaces[i], true, uprightFaceRollAngle, distanceThresholdsMultiplier, timestamp) failed with %s, returning %s"
+ "Running updateTrackedFacesWithFaceDetections(m_trackedFaces, faces, timestamp, correctionEnabled, uprightFaceRollAngle, distanceThresholdsMultiplier, TrackedFace::DiscardFacePassKey()) failed with %s, returning %s"
+ "clear_faces"
+ "faces_cleared"
- "."
- "/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/facekit/accessibilityfilter.mm"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/facekit/facekitlitefilter.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/geometry/src/three_d/identitytensor.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/geometry/src/three_d/quad_mesh.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/geometry/src/three_d/trackingriglite.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/tracking/src/io/framesequencedata.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/utils/src/CompressedDevice.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/utils/src/FilePack.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/utils/src/TaskThreadPool.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/utils/src/ThreadWorkGroup.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/utils/src/fsByteArray.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/shrek/libs/alg/utils/src/fsFileDevice.cpp"
- "Fisheye strength has been deprecated and will be ignored."
- "Null or 0 vertices provided."
- "Running addLandmarksToDictionary(normalizedLandmarksToImage(**trackedFace.normalizedLandmarks(), crops.face.bbox), faceDictionary) failed with %s, returning %s"
- "Running cropEyes(commandBuffer, normalizedLandmarksToImage(**trackedFace.normalizedLandmarks(), crops.face.bbox), data.virtualCameraOffset(), crops) failed with %s, returning %s"
- "Running m_debugRenderer->encode(normalizedLandmarksToImage(**face->normalizedLandmarks(), regressorData->crops.face.bbox), yuv, *debugRendererState) failed with %s, returning %s"
- "Running trackedFace->update(faces[i], correctionEnabled, uprightFaceRollAngle, distanceThresholdsMultiplier, timestamp) failed with %s, returning %s"
- "Running updateTrackedFacesWithFaceDetections(m_trackedFaces, faces, timestamp, correctionEnabled, uprightFaceRollAngle, distanceThresholdsMultiplier) failed with %s, returning %s"
- "StereographicFisheyeStrength"
- "assert %s failed. A threadpool needs at least one thread.%s"
- "poolsize >= 1"

```
